import ast
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from loguru import logger

from scrape import ScrapedMeta


@dataclass
class Fields:
    name: str
    type: Any
    required: bool
    scraped_properties: Optional[ScrapedMeta] = None


@dataclass
class ParsedTroposphereObject:
    name: str
    docstring: Optional[str]
    url: Optional[str]
    obj_type: str
    fields: Optional[List[Fields]] = None


def extract_docstring_url(docstring: str) -> Optional[str]:
    pattern = r"`(.+?) <(.+?)>`__"
    match = re.search(pattern, docstring)
    if match:
        label = match.group(1)
        url = match.group(2)
        print(f"Label: {label}")
        print(f"URL: {url}")
        return url
    else:
        logger.error("Pattern not found in docstring.")
        return None


def extract_value_from_node(node, tropo_types) -> Tuple[str, bool]:
    required = True

    if isinstance(node, ast.Assign):
        required = False
        node = node.value

    type_name = _extract_type_from_node(node, tropo_types)
    return type_name, required


def _extract_type_from_node(node, tropo_types) -> str:
    if hasattr(node, "value"):
        print("VALUE", node.value)
    if isinstance(node, ast.Name):
        # TODO handle troposphere validation checks with scraped doc data. Implement as enums

        if node.id == "Criteria":
            print("HEEEEEELLLLOOOOOOOOOOOOO")
            print(tropo_types)
            print(node.id in tropo_types)

        if node.id in tropo_types:
            print("I SHOULD RUN")
            return node.id
        else:
            print(f"node id not in tropo types: {node.id}")
            print(tropo_types)

        type_mappings = {
            "str": "str",
            "int": "int",
            "integer": "int",  # This will map 'integer' to 'int'
            "bool": "bool",
        }
        print("MIGHT BE SETTING ANY")
        return type_mappings.get(node.id, "Any")
    elif isinstance(node, ast.Str):
        print(f"node is str: {node}")
        return "str"
    elif isinstance(node, ast.List):
        print(f"node is list: {node}")
        try:
            inner_type, _ = (
                extract_value_from_node(node.elts[0], tropo_types)
                if node.elts
                else "Any"
            )
        # ValueError: too many values to unpack (expected 2)
        except ValueError:
            inner_type = (
                extract_value_from_node(node.elts[0], tropo_types)
                if node.elts
                else "Any"
            )

        return f"List[{inner_type}]"
    elif isinstance(node, ast.Dict):
        print(f"node is dict: {node}")
        key_type, _ = (
            extract_value_from_node(node.keys[0], tropo_types) if node.keys else "Any"
        )
        value_type, _ = (
            extract_value_from_node(node.values[0]),
            tropo_types if node.values else "Any",
        )
        return f"Dict[{key_type}, {value_type}]"
    elif isinstance(node, ast.Num):
        if isinstance(node.n, int):
            print(f"node is int: {node}")
            return "int"
        elif isinstance(node.n, float):
            print(f"node is float: {node}")
            return "float"
    elif isinstance(node, ast.BoolOp):
        print(f"node is bool: {node}")
        return "bool"
    elif isinstance(node, ast.Constant):
        if isinstance(node.value, str):
            return "str"
        elif isinstance(node.value, int):
            return "int"
        elif isinstance(node.value, float):
            return "float"
        elif isinstance(node.value, bool):
            return "bool"
    elif isinstance(node, ast.Tuple):
        print(f"node is tuple: {node}")
        types = [extract_value_from_node(elt, tropo_types)[0] for elt in node.elts]
        return f"Tuple[{', '.join(types)}]"

    # NOTE: I don't think this is valid condition
    elif hasattr(node, "value"):
        if node.value in tropo_types:
            return node.value
    else:
        print("I FUGGING RAN")
        print(type(node))
        print(node)
        return "Any"


def is_troposphere_property_or_object(tree):
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            base_classes = [
                base.id for base in node.bases if isinstance(base, ast.Name)
            ]
            if not any(bc in ["AWSProperty", "AWSObject"] for bc in base_classes):
                continue
            yield node


def extract_class_data_from_code(code) -> List[ParsedTroposphereObject]:
    tree = ast.parse(code)
    classes = []

    discovered_tropo_types = []
    for node in is_troposphere_property_or_object(tree):
        discovered_tropo_types.append(node.name)

    for node in is_troposphere_property_or_object(tree):
        if isinstance(node, ast.ClassDef):
            base_classes = [
                base.id for base in node.bases if isinstance(base, ast.Name)
            ]
            if not any(bc in ["AWSProperty", "AWSObject"] for bc in base_classes):
                continue

            docstring = None
            url = None
            if "AWSObject" in base_classes:
                obj_type = "AWSObject"
                docstring = ast.get_docstring(node)
                if docstring:
                    url = extract_docstring_url(docstring=docstring)
            else:
                obj_type = "AWSProperty"

            class_data = ParsedTroposphereObject(
                name=node.name,
                docstring=docstring,
                url=url,
                obj_type=obj_type,
            )

            for item in node.body:
                target = None
                value = None

                if isinstance(item, ast.Assign):
                    target = item.targets[0]
                    value = item.value
                elif isinstance(item, ast.AnnAssign):
                    target = item.target
                    value = item.value

                if target and isinstance(target, ast.Name) and target.id == "props":
                    fields_list = []
                    for key, value in zip(value.keys, value.values):
                        print(key.s)
                        if not isinstance(value, ast.Tuple):
                            print(f"stopping on: {type(value)}")
                            continue
                            # raise ValueError(f"Every troposphere property should be a tuple. Unknown type: {node}")

                        type_, required = value.elts
                        type_, _ = extract_value_from_node(
                            type_, discovered_tropo_types
                        )
                        fields = Fields(name=key.s, type=type_, required=required)
                        if not required:
                            print("NOT REQ is FALSE THIS SHOULD BE THE CASE A LOT")
                        fields_list.append(fields)
                    class_data.fields = fields_list
            classes.append(class_data)

    return classes


def parse_troposphere_file(file_path: str) -> List[ParsedTroposphereObject]:
    with open(file_path, "r") as file:
        code = file.read()

    parsed_troposphere_obj = extract_class_data_from_code(code)
    return parsed_troposphere_obj
