from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AccessControlAttribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: 'AccessControlAttributeValue' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.sso.AccessControlAttribute:
        from troposphere.sso import AccessControlAttribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessControlAttributeValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html
    Properties:
        - Name: Source
    
    """
    
    Source_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue-source""", alias="Source")
    


    @property
    def tropo_type(self) -> troposphere.sso.AccessControlAttributeValue:
        from troposphere.sso import AccessControlAttributeValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomerManagedPolicyReference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html
    Properties:
        - Name: Path
        - Name: Name
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html#cfn-sso-permissionset-customermanagedpolicyreference-path""", alias="Path")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html#cfn-sso-permissionset-customermanagedpolicyreference-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.sso.CustomerManagedPolicyReference:
        from troposphere.sso import CustomerManagedPolicyReference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PermissionsBoundary(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html
    Properties:
        - Name: CustomerManagedPolicyReference
        - Name: ManagedPolicyArn
    
    """
    
    CustomerManagedPolicyReference_: Optional['CustomerManagedPolicyReference'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html#cfn-sso-permissionset-permissionsboundary-customermanagedpolicyreference""", alias="CustomerManagedPolicyReference")
    ManagedPolicyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html#cfn-sso-permissionset-permissionsboundary-managedpolicyarn""", alias="ManagedPolicyArn")
    


    @property
    def tropo_type(self) -> troposphere.sso.PermissionsBoundary:
        from troposphere.sso import PermissionsBoundary as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Assignment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html
    Properties:
        - Name: PrincipalId
        - Name: InstanceArn
        - Name: TargetType
        - Name: PermissionSetArn
        - Name: PrincipalType
        - Name: TargetId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PrincipalId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principalid""", alias="PrincipalId")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-instancearn""", alias="InstanceArn")
    TargetType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targettype""", alias="TargetType")
    PermissionSetArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-permissionsetarn""", alias="PermissionSetArn")
    PrincipalType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principaltype""", alias="PrincipalType")
    TargetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targetid""", alias="TargetId")
    

    @property
    def tropo_type(self) -> troposphere.sso.Assignment:
        from troposphere.sso import Assignment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sso import Assignment as TropoT
        return resource_to_troposphere(self, TropoT)


class InstanceAccessControlAttributeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html
    Properties:
        - Name: InstanceArn
        - Name: AccessControlAttributes
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instancearn""", alias="InstanceArn")
    AccessControlAttributes_: Optional[List['AccessControlAttribute']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributes""", alias="AccessControlAttributes")
    

    @property
    def tropo_type(self) -> troposphere.sso.InstanceAccessControlAttributeConfiguration:
        from troposphere.sso import InstanceAccessControlAttributeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sso import InstanceAccessControlAttributeConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class PermissionSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html
    Properties:
        - Name: RelayStateType
        - Name: CustomerManagedPolicyReferences
        - Name: SessionDuration
        - Name: Description
        - Name: InstanceArn
        - Name: InlinePolicy
        - Name: ManagedPolicies
        - Name: Tags
        - Name: Name
        - Name: PermissionsBoundary
    Attributes:
        - Name: PermissionSetArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RelayStateType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-relaystatetype""", alias="RelayStateType")
    CustomerManagedPolicyReferences_: Optional[List['CustomerManagedPolicyReference']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-customermanagedpolicyreferences""", alias="CustomerManagedPolicyReferences")
    SessionDuration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-sessionduration""", alias="SessionDuration")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-description""", alias="Description")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-instancearn""", alias="InstanceArn")
    InlinePolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-inlinepolicy""", alias="InlinePolicy")
    ManagedPolicies_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-managedpolicies""", alias="ManagedPolicies")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-name""", alias="Name")
    PermissionsBoundary_: Optional['PermissionsBoundary'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-permissionsboundary""", alias="PermissionsBoundary")
    

    @property
    def tropo_type(self) -> troposphere.sso.PermissionSet:
        from troposphere.sso import PermissionSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sso import PermissionSet as TropoT
        return resource_to_troposphere(self, TropoT)

