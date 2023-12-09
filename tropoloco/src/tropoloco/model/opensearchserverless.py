from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class SamlConfigOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-samlconfigoptions.html
    Properties:
        - Name: SessionTimeout
        - Name: UserAttribute
        - Name: Metadata
        - Name: GroupAttribute
    
    """
    
    SessionTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-samlconfigoptions.html#cfn-opensearchserverless-securityconfig-samlconfigoptions-sessiontimeout""", alias="SessionTimeout")
    UserAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-samlconfigoptions.html#cfn-opensearchserverless-securityconfig-samlconfigoptions-userattribute""", alias="UserAttribute")
    Metadata_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-samlconfigoptions.html#cfn-opensearchserverless-securityconfig-samlconfigoptions-metadata""", alias="Metadata")
    GroupAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchserverless-securityconfig-samlconfigoptions.html#cfn-opensearchserverless-securityconfig-samlconfigoptions-groupattribute""", alias="GroupAttribute")
    


    @property
    def tropo_type(self) -> troposphere.opensearchserverless.SamlConfigOptions:
        from troposphere.opensearchserverless import SamlConfigOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AccessPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-accesspolicy.html
    Properties:
        - Name: Policy
        - Name: Type
        - Name: Description
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-accesspolicy.html#cfn-opensearchserverless-accesspolicy-policy""", alias="Policy")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-accesspolicy.html#cfn-opensearchserverless-accesspolicy-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-accesspolicy.html#cfn-opensearchserverless-accesspolicy-description""", alias="Description")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-accesspolicy.html#cfn-opensearchserverless-accesspolicy-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.opensearchserverless.AccessPolicy:
        from troposphere.opensearchserverless import AccessPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opensearchserverless import AccessPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class Collection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: StandbyReplicas
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: CollectionEndpoint
        - Name: Id
        - Name: Arn
        - Name: DashboardEndpoint
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html#cfn-opensearchserverless-collection-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html#cfn-opensearchserverless-collection-description""", alias="Description")
    StandbyReplicas_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html#cfn-opensearchserverless-collection-standbyreplicas""", alias="StandbyReplicas")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html#cfn-opensearchserverless-collection-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html#cfn-opensearchserverless-collection-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.opensearchserverless.Collection:
        from troposphere.opensearchserverless import Collection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opensearchserverless import Collection as TropoT
        return resource_to_troposphere(self, TropoT)


class LifecyclePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-lifecyclepolicy.html
    Properties:
        - Name: Policy
        - Name: Type
        - Name: Description
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-lifecyclepolicy.html#cfn-opensearchserverless-lifecyclepolicy-policy""", alias="Policy")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-lifecyclepolicy.html#cfn-opensearchserverless-lifecyclepolicy-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-lifecyclepolicy.html#cfn-opensearchserverless-lifecyclepolicy-description""", alias="Description")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-lifecyclepolicy.html#cfn-opensearchserverless-lifecyclepolicy-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.opensearchserverless.LifecyclePolicy:
        from troposphere.opensearchserverless import LifecyclePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opensearchserverless import LifecyclePolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class SecurityConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securityconfig.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: SamlOptions
        - Name: Name
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securityconfig.html#cfn-opensearchserverless-securityconfig-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securityconfig.html#cfn-opensearchserverless-securityconfig-description""", alias="Description")
    SamlOptions_: Optional['SamlConfigOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securityconfig.html#cfn-opensearchserverless-securityconfig-samloptions""", alias="SamlOptions")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securityconfig.html#cfn-opensearchserverless-securityconfig-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.opensearchserverless.SecurityConfig:
        from troposphere.opensearchserverless import SecurityConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opensearchserverless import SecurityConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class SecurityPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securitypolicy.html
    Properties:
        - Name: Policy
        - Name: Type
        - Name: Description
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securitypolicy.html#cfn-opensearchserverless-securitypolicy-policy""", alias="Policy")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securitypolicy.html#cfn-opensearchserverless-securitypolicy-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securitypolicy.html#cfn-opensearchserverless-securitypolicy-description""", alias="Description")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securitypolicy.html#cfn-opensearchserverless-securitypolicy-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.opensearchserverless.SecurityPolicy:
        from troposphere.opensearchserverless import SecurityPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opensearchserverless import SecurityPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class VpcEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-vpcendpoint.html
    Properties:
        - Name: VpcId
        - Name: SecurityGroupIds
        - Name: SubnetIds
        - Name: Name
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-vpcendpoint.html#cfn-opensearchserverless-vpcendpoint-vpcid""", alias="VpcId")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-vpcendpoint.html#cfn-opensearchserverless-vpcendpoint-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-vpcendpoint.html#cfn-opensearchserverless-vpcendpoint-subnetids""", alias="SubnetIds")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-vpcendpoint.html#cfn-opensearchserverless-vpcendpoint-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.opensearchserverless.VpcEndpoint:
        from troposphere.opensearchserverless import VpcEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opensearchserverless import VpcEndpoint as TropoT
        return resource_to_troposphere(self, TropoT)

