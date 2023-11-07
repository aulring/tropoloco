from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################




######################################################################
# AWS Resource
######################################################################


class Permission(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-permission.html
    Properties:
        - Name: ResourceType
        - Name: PolicyTemplate
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Version
        - Name: PermissionType
        - Name: Arn
        - Name: IsResourceTypeDefault
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-permission.html#cfn-ram-permission-resourcetype""", alias="ResourceType")
    PolicyTemplate_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-permission.html#cfn-ram-permission-policytemplate""", alias="PolicyTemplate")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-permission.html#cfn-ram-permission-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-permission.html#cfn-ram-permission-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ram.Permission:
        from troposphere.ram import Permission as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ram import Permission as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourceShare(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html
    Properties:
        - Name: PermissionArns
        - Name: Principals
        - Name: AllowExternalPrincipals
        - Name: ResourceArns
        - Name: Sources
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PermissionArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-permissionarns""", alias="PermissionArns")
    Principals_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-principals""", alias="Principals")
    AllowExternalPrincipals_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-allowexternalprincipals""", alias="AllowExternalPrincipals")
    ResourceArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-resourcearns""", alias="ResourceArns")
    Sources_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-sources""", alias="Sources")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ram.ResourceShare:
        from troposphere.ram import ResourceShare as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ram import ResourceShare as TropoT
        return resource_to_troposphere(self, TropoT)

