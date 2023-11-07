import json
from typing import Any, Dict, List, Optional, Union, Tuple

import jinja2
import requests
from pydantic import BaseModel


CLOUDFORMATION_SPEC_URL = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
JINJA_ENV = jinja2.Environment(keep_trailing_newline=True)


#NOTE: wafv2 has duplicate property names "FieldToMatch"... which we now need to handle lol.

TYPE_MAP = {
    "String": "str",
    "List": "List",
    "Map": "Dict",
    "Timestamp": "datetime.datetime",
    "Integer": "int",
    "Double": "float",
    "Long": "int",
    "Boolean": "bool",
    "Json": "Dict",
    "list": "List",
}

TROPO_TYPE_PROPERTY_OVERRIDES = {
    ("amazonmq", "LogList"): "LogsConfiguration",
    ("ec2", "TagSpecification"): "TagSpecifications",
    ("ecr", "ReplicationConfiguration"): "ReplicationConfigurationProperty",
    ("ecs", "ClusterSettings"): "ClusterSetting",
    ("iotanalytics", "Datastore"): "ActivityDatastore",
    ("iotanalytics", "Channel"): "ActivityChannel",
    ("lakeformation", "ExternalDataFilteringAllowList"): "List",
    ("lakeformation", "CreateTableDefaultPermissions"): "List",
    ("lakeformation", "CreateDatabaseDefaultPermissions"): "List",
    ("lakeformation", "Resource"): "TagAssociationResource",
    ("lakeformation", "TableWithColumnsResource"): "TagAssociationTableWithColumnsResource",
    ("lambda", "VpcConfig"): "VPCConfig",
    ("networkfirewall", "RuleGroup"): "RuleGroupProperty",
    ("redshift", "Parameter"): "AmazonRedshiftParameter",
    #("wafv2", "FieldToMatch"): "LoggingConfigurationFieldToMatch",
}

TROPO_PROPERTY_NAME_OVERRIDES = {
    ("ecr", "ReplicationConfiguration"): "ReplicationConfigurationProperty",
    ("iotanalytics", "Datastore"): "ActivityDatastore",
    ("iotanalytics", "Channel"): "ActivityChannel",
    ("lakeformation", "Admins"): "DataLakePrincipal",
    ("lakeformation", "Resource"): "TagAssociationResource",
    ("lambda", "VpcConfig"): "VPCConfig",
    ("networkfirewall", "RuleGroup"): "RuleGroupProperty",
    ("redshift", "Parameter"): "AmazonRedshiftParameter",
    #("wafv2", "FieldToMatch"): "LoggingConfigurationFieldToMatch",
    
}

PROPERTY_CLASS_RENAMES = {
    ("wafv2.py", "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html", "'FieldToMatch'"): "'LoggingConfigurationFieldToMatch'",
    ("wafv2.py", "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html", "'FieldToMatch'"): "'LoggingConfigurationFieldToMatch'",

}

RESOURCE_TYPING_OVERRIDES = {
    ("Activity", "'Channel'"): "'ActivityChannel'",
    ("Activity", "'Datastore'"): "'ActivityDatastore'",
    ("lakeformation", "'ExternalDataFilteringAllowList'"): "'List'",
    ("lakeformation", "'CreateTableDefaultPermissions'"): "'List'",
    ("lakeformation", "'CreateDatabaseDefaultPermissions'"): "'List'",
    ("lakeformation", "'Admins'"): "List['DataLakePrincipal']",
    ("lakeformation", "'Resource'"): "'TagAssociationResource'",
    ("lakeformation", "'TableWithColumnsResource'"): "'TagAssociationTableWithColumnsResource'",
    ("lambda", "'VpcConfig'"): "'VPCConfig'",
    ("macie", "List['Tag']"): "Tags",
    ("networkfirewall", "'RuleGroup'"): "'RuleGroupProperty'",
    ("redshift", "List['Parameter']"): "List['AmazonRedshiftParameter']",
    ("rekognition", "Dict"): "List[List[Dict[str, float]]]", #TODO this is a hack. This is the only Dict So I could override it this way... hacky.
    ("route53", "List['HealthCheckTag']"): "Tags",
    ("stepfunctions", "List['TagsEntry']"): "Tags",
    ("transfer", "List['Protocol']"): "List[str]",
    ("wafv2", "'FieldToMatch'"): "'LoggingConfigurationFieldToMatch'",
    #("ByteMatchStatement", "'FieldToMatch'"): "'LoggingConfigurationFieldToMatch'",
    #("RegexMatchStatement", "'FieldToMatch'"): "'LoggingConfigurationFieldToMatch'",
    #("RegexPatternSetReferenceStatement", "'FieldToMatch'"): "'LoggingConfigurationFieldToMatch'",
    #("XssMatchStatement", "'FieldToMatch'"): "'LoggingConfigurationFieldToMatch'",
    #("SqliMatchStatement", "'FieldToMatch'"): "'LoggingConfigurationFieldToMatch'",
    #("SizeConstraintStatement", "'FieldToMatch'"): "'LoggingConfigurationFieldToMatch'",
    #("RegexPatternSetReferenceStatement", "'FieldToMatch'"): "'LoggingConfigurationFieldToMatch'",
    #("wafv2", "List['FieldToMatch']"): "List['LoggingConfigurationFieldToMatch']",

}

TROPO_RESOURCE_RENAMES = {
    ("route53", "RecordSet"): "RecordSetType"
}

HAS_DUPLICATE_PROPERTY = [
    ("wafv2", "FieldToMatch")
]


def get_typing(t: Any):
    if isinstance(t, str):
        if t in TYPE_MAP:
            return TYPE_MAP.get(t, "Any")
        else:
            if t in TROPO_PROPERTY_NAME_OVERRIDES:
                return f"'{TROPO_TYPE_PROPERTY_OVERRIDES[t]}'"
            else:
                return f"'{t}'"
    elif isinstance(t, list):
        ts = []

        if t[0] == "List":
            return f"List[{get_typing(t[1])}]"
        elif t[0] == "Map":
            return f"Dict[str, {get_typing(t[1])}]"
        for item in t:
            print(item)
            t_item = get_typing(item)
            print(t_item)
            ts.append(t_item)
        return f"Union[{', '.join(ts)}]"
    else:
        return "Any"


class Property(BaseModel):
    Documentation: str
    UpdateType: Optional[str] = None
    Required: Optional[bool] = None
    Type: Optional[Any] = None
    PrimitiveType: Optional[Any] = None
    PrimitiveItemType: Optional[Any] = None
    DuplicatesAllowed: Optional[bool] = None
    ItemType: Optional[Any] = None
    typing: Optional[str] = None
    service_name: Optional[str] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__["typing"] = get_typing(self._type())

        key = (self.service_name, self.typing)
        if key in RESOURCE_TYPING_OVERRIDES:
            self.__dict__["typing"] = RESOURCE_TYPING_OVERRIDES[key]

    def _type(self):
        types = [
            t
            for t in [
                self.Type,
                self.PrimitiveType,
                self.PrimitiveItemType,
                self.ItemType,
            ]
            if t
        ]
        if len(types) == 1:
            return types[0]
        return types


class Attribute(BaseModel):
    Type: Optional[Any] = None
    ItemType: Optional[Any] = None
    PrimitiveType: Optional[Any] = None
    PrimitiveItemType: Optional[Any] = None
    typing: Optional[str] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        t = self._type()
        self.__dict__["typing"] = get_typing(self._type())

    def _type(self):
        types = [
            t
            for t in [
                self.Type,
                self.PrimitiveType,
                self.PrimitiveItemType,
                self.ItemType,
            ]
            if t
        ]
        if len(types) == 1:
            return types[0]
        return types


class AWSProperty(BaseModel):
    name: str
    tropo_name: str
    Documentation: str
    Properties: Optional[Dict[str, Property]] = None
    lookup_key: Optional[Union[tuple, str]] = ""

    def __hash__(self):
        return hash(self.Documentation)


class AWSResource(BaseModel):
    name: str
    Documentation: str
    Properties: Dict[str, Property]
    service_name: Optional[str]
    Attributes: Optional[Dict[str, Attribute]] = None


def download_spec():
    response = requests.get(CLOUDFORMATION_SPEC_URL)
    cfn_spec = json.loads(response.text)

    return cfn_spec


def order_properties(properties: list):
    property_names_set = set([p.name for p in properties])
    if len(properties) != len(property_names_set):
        raise ValueError("Encountered non-unique property names")

    for aws_prop in properties:
        for prop in aws_prop.Properties:
            typing = prop.typing


def main():
    spec = download_spec()
    resource_types = spec["ResourceTypes"]
    property_types = spec["PropertyTypes"]

    lookup = {}
    
    for property, spec in property_types.items():
        if "." not in property and property != "Tag":
            raise ValueError("Unknown Property type. Isn't Tag and doesn't have '.' ")

        drop_property = property.split(".")[0]
        property_name = property.split(".")[-1]
        property_parent_resource = drop_property.split("::")[-1]
        service_key = "::".join(drop_property.split("::")[:2])

        if not service_key == "Tag":
            if (service_key.split('::')[1].lower(), property_name) in HAS_DUPLICATE_PROPERTY:
                print("DUPLICATE KEY OVERRIDE")
                property_name = property_parent_resource + property_name

        prop = AWSProperty(name=property_name, tropo_name=property_name, **spec)
        prop.lookup_key = property_name
        if (
            property_name in TROPO_TYPE_PROPERTY_OVERRIDES
            or (service_key.split("::")[-1].lower(), property_name)
            in TROPO_TYPE_PROPERTY_OVERRIDES
        ):
            print("PROPERTY TYPE OVERRIDE OVERRIDE", property_name)
            if (
                service_key.split("::")[-1].lower(),
                property_name,
            ) in TROPO_TYPE_PROPERTY_OVERRIDES:
                prop.tropo_name = TROPO_TYPE_PROPERTY_OVERRIDES[
                    (service_key.split("::")[-1].lower(), property_name)
                ]
                prop.lookup_key = (service_key.split("::")[-1].lower(), property_name)
                print(prop.tropo_name)
            else:
                prop.tropo_name = TROPO_TYPE_PROPERTY_OVERRIDES[property_name]
            print(prop.tropo_name)
        if (
            property_name in TROPO_PROPERTY_NAME_OVERRIDES
            or (service_key.split("::")[-1].lower(), property_name)
            in TROPO_PROPERTY_NAME_OVERRIDES
        ):
            print("PROPERTY NAME OVERRIDE OVERRIDE", property_name)
            if (
                service_key.split("::")[-1].lower(),
                property_name,
            ) in TROPO_PROPERTY_NAME_OVERRIDES:
                prop.name = TROPO_PROPERTY_NAME_OVERRIDES[
                    (service_key.split("::")[-1].lower(), property_name)
                ]
            else:
                prop.name = TROPO_PROPERTY_NAME_OVERRIDES[property_name]

        if service_key not in lookup:
            lookup[service_key] = {
                "properties": [prop],
                "resources": [],
            }
        else:
            lookup[service_key]["properties"].append(prop)

    for resource, spec in resource_types.items():
        resource_name = resource.split("::")[-1]
        service_key = "::".join(resource.split("::")[:2])
        service_name = service_key.split("::")[-1].lower()

        if service_key not in lookup and prop.Properties:
            lookup[service_key] = {
                "resources": [
                    AWSResource(name=resource_name, service_name=service_name, **spec)
                ],
                "properties": [],
            }
        else:
            if prop.Properties:
                lookup[service_key]["resources"].append(
                    AWSResource(name=resource_name, service_name=service_name, **spec)
                )

    for service in lookup.keys():
        if service == "AWS::Lambda":
            output_file_name = "awslambda"
            output_file = f"{output_file_name}.py"
        else:
            output_file_name = service.split("::")[-1].lower()
            output_file = f"{output_file_name}.py"

        with open("templates/troposphere_aws_service2.py.tpl.j2") as template_file:
            template = JINJA_ENV.from_string(template_file.read())

        with open(
            f"../tropoloco/src/tropoloco/model/{output_file}", "w"
        ) as output_file:
            resources = lookup[service]["resources"]
            properties = lookup[service]["properties"]

            template.stream(
                resources=resources,
                properties=properties,
                output_file_name=output_file_name,
                service_name=output_file_name.replace(".py", ""),
                tropo_property_name_overrides=TROPO_PROPERTY_NAME_OVERRIDES,
                #tropo_property_type_overrides=PROPERTY_TYPING_OVERRIDES,
                tropo_resource_typing_overrides=RESOURCE_TYPING_OVERRIDES,
                tropo_resource_renames=TROPO_RESOURCE_RENAMES
            ).dump(output_file)


if __name__ == "__main__":
    main()
