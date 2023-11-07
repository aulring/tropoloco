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


class Account(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html
    Properties:
        - Name: RoleName
        - Name: Email
        - Name: ParentIds
        - Name: Tags
        - Name: AccountName
    Attributes:
        - Name: JoinedMethod
        - Name: Status
        - Name: JoinedTimestamp
        - Name: AccountId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RoleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html#cfn-organizations-account-rolename""", alias="RoleName")
    Email_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html#cfn-organizations-account-email""", alias="Email")
    ParentIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html#cfn-organizations-account-parentids""", alias="ParentIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html#cfn-organizations-account-tags""", alias="Tags")
    AccountName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html#cfn-organizations-account-accountname""", alias="AccountName")
    

    @property
    def tropo_type(self) -> troposphere.organizations.Account:
        from troposphere.organizations import Account as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.organizations import Account as TropoT
        return resource_to_troposphere(self, TropoT)


class Organization(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organization.html
    Properties:
        - Name: FeatureSet
    Attributes:
        - Name: RootId
        - Name: Id
        - Name: Arn
        - Name: ManagementAccountArn
        - Name: ManagementAccountId
        - Name: ManagementAccountEmail
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FeatureSet_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organization.html#cfn-organizations-organization-featureset""", alias="FeatureSet")
    

    @property
    def tropo_type(self) -> troposphere.organizations.Organization:
        from troposphere.organizations import Organization as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.organizations import Organization as TropoT
        return resource_to_troposphere(self, TropoT)


class OrganizationalUnit(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html
    Properties:
        - Name: ParentId
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ParentId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html#cfn-organizations-organizationalunit-parentid""", alias="ParentId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html#cfn-organizations-organizationalunit-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html#cfn-organizations-organizationalunit-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.organizations.OrganizationalUnit:
        from troposphere.organizations import OrganizationalUnit as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.organizations import OrganizationalUnit as TropoT
        return resource_to_troposphere(self, TropoT)


class Policy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html
    Properties:
        - Name: Type
        - Name: TargetIds
        - Name: Description
        - Name: Content
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
        - Name: AwsManaged
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html#cfn-organizations-policy-type""", alias="Type")
    TargetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html#cfn-organizations-policy-targetids""", alias="TargetIds")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html#cfn-organizations-policy-description""", alias="Description")
    Content_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html#cfn-organizations-policy-content""", alias="Content")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html#cfn-organizations-policy-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html#cfn-organizations-policy-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.organizations.Policy:
        from troposphere.organizations import Policy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.organizations import Policy as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourcePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-resourcepolicy.html
    Properties:
        - Name: Content
        - Name: Tags
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Content_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-resourcepolicy.html#cfn-organizations-resourcepolicy-content""", alias="Content")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-resourcepolicy.html#cfn-organizations-resourcepolicy-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.organizations.ResourcePolicy:
        from troposphere.organizations import ResourcePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.organizations import ResourcePolicy as TropoT
        return resource_to_troposphere(self, TropoT)

