from datetime import datetime
from troposphere import Tags
from tropoloco.tag import Tags as TropoTags

TAGS_ANALOG = set(["UserAttributesForFindings_", "ResourceGroupTags_", "HealthCheckTags_"])


def convert_property_type(obj, tropo_type):
    kwargs = {}
    model_fields = obj.model_fields
    for name, value in iter(obj):
        if value:
            kwargs[model_fields[name].alias] = value
    return tropo_type(**kwargs)


def property_to_troposphere(obj):
    for name, value in obj:
        if name == "Tags_" or name in TAGS_ANALOG:
            if value:
                if isinstance(value, list):
                    print(value)
                    first_entry = value[0]
                    print(first_entry)
                    print(type(first_entry))
                    # checking for special type TagCollection
                    if not "AppBoundaryKey_" in first_entry.model_fields:
                        # NOTE: should we check they passed valid/unique tags?
                        try:
                            tags_kwargs = {item.Key: item.Value for item in value}
                        except AttributeError as e: #eek
                            #Special case aps_Workspace.yaml
                            tags_kwargs = {item.Key_: item.Value_ for item in value}

                        obj.__dict__[name] = Tags(**tags_kwargs)
                    # This is our special TagCollection case
                    else:
                        # NOTE will this always be one item?
                        tag_key = first_entry.AppBoundaryKey_
                        tag_value = ",".join(first_entry.TagValues_)
                        obj.__dict__[name] = Tags({tag_key: tag_value})

                elif isinstance(value, dict):
                    obj.__dict__[name] = Tags(value)
                elif isinstance(value, TropoTags):
                    print("IRAAAAAAN")
                    tags_kwargs = {item["Key"]: item["Value"] for item in value.model_dump()}
                    obj.__dict__[name] = Tags(**tags_kwargs)
                else:
                    raise TypeError("Tags_ is not list or dict")
            else:
                obj.__dict__[name] = None

        if value is None:
            continue
        elif isinstance(value, (str, int, float, bool, datetime)):
            print(f"{name} is a primitive type: {value}")
            continue
        elif hasattr(value, "to_troposphere"):
            print(f"Converting {name} to its troposphere representation...")
            value.to_troposphere()
            prop = convert_property_type(value, value.tropo_type)
            obj.__dict__[name] = prop
        elif isinstance(value, list):
            new_props = []
            for item in value:
                if hasattr(item, "to_troposphere"):
                    item.to_troposphere()
                    new_prop = convert_property_type(item, item.tropo_type)
                    new_props.append(new_prop)
                    # print("IM GONNA BREAK", item, value)
                    # prop = convert_property_type(value, value.tropo_type)
            if new_props:
                obj.__dict__[name] = new_props
        elif isinstance(value, dict):
            for item in value.values():
                if hasattr(item, "to_troposphere"):
                    print(item)
                    item.to_troposphere()
                    print(value)
                    prop = convert_property_type(item, item.tropo_type)
                    obj.__dict__[name] = prop
        
        elif isinstance(value, TropoTags):
            print("TropoTag encountered")
            continue
        else:
            print(type(value))
            raise ValueError(
                "Failure to process property. Did not satisfy known condition"
            )


def resource_to_troposphere(obj, tropo_type):
    print("starting main property to object")
    property_to_troposphere(obj)
    print("keys should have been converted. ")
    kwargs = {}
    model_fields = obj.model_fields
    for name, value in iter(obj):
        if value:
            kwargs[model_fields[name].alias] = value
    print(kwargs)
    return tropo_type(**kwargs)
