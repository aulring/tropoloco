from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Policy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group-policy.html
    Properties:
        - Name: PolicyName
        - Name: PolicyDocument
    
    """
    
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group-policy.html#cfn-iam-group-policy-policyname""", alias="PolicyName")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group-policy.html#cfn-iam-group-policy-policydocument""", alias="PolicyDocument")
    


    @property
    def tropo_type(self) -> troposphere.iam.Policy:
        from troposphere.iam import Policy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Policy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html
    Properties:
        - Name: PolicyName
        - Name: PolicyDocument
    
    """
    
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html#cfn-iam-role-policy-policyname""", alias="PolicyName")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html#cfn-iam-role-policy-policydocument""", alias="PolicyDocument")
    


    @property
    def tropo_type(self) -> troposphere.iam.Policy:
        from troposphere.iam import Policy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoginProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-loginprofile.html
    Properties:
        - Name: PasswordResetRequired
        - Name: Password
    
    """
    
    PasswordResetRequired_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-loginprofile.html#cfn-iam-user-loginprofile-passwordresetrequired""", alias="PasswordResetRequired")
    Password_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-loginprofile.html#cfn-iam-user-loginprofile-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.iam.LoginProfile:
        from troposphere.iam import LoginProfile as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Policy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-policy.html
    Properties:
        - Name: PolicyName
        - Name: PolicyDocument
    
    """
    
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-policy.html#cfn-iam-user-policy-policyname""", alias="PolicyName")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-policy.html#cfn-iam-user-policy-policydocument""", alias="PolicyDocument")
    


    @property
    def tropo_type(self) -> troposphere.iam.Policy:
        from troposphere.iam import Policy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AccessKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html
    Properties:
        - Name: Serial
        - Name: Status
        - Name: UserName
    Attributes:
        - Name: SecretAccessKey
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Serial_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html#cfn-iam-accesskey-serial""", alias="Serial")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html#cfn-iam-accesskey-status""", alias="Status")
    UserName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html#cfn-iam-accesskey-username""", alias="UserName")
    

    @property
    def tropo_type(self) -> troposphere.iam.AccessKey:
        from troposphere.iam import AccessKey as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import AccessKey as TropoT
        return resource_to_troposphere(self, TropoT)


class Group(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html
    Properties:
        - Name: GroupName
        - Name: Path
        - Name: ManagedPolicyArns
        - Name: Policies
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html#cfn-iam-group-groupname""", alias="GroupName")
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html#cfn-iam-group-path""", alias="Path")
    ManagedPolicyArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html#cfn-iam-group-managedpolicyarns""", alias="ManagedPolicyArns")
    Policies_: Optional[List['Policy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html#cfn-iam-group-policies""", alias="Policies")
    

    @property
    def tropo_type(self) -> troposphere.iam.Group:
        from troposphere.iam import Group as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import Group as TropoT
        return resource_to_troposphere(self, TropoT)


class GroupPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-grouppolicy.html
    Properties:
        - Name: GroupName
        - Name: PolicyName
        - Name: PolicyDocument
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-grouppolicy.html#cfn-iam-grouppolicy-groupname""", alias="GroupName")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-grouppolicy.html#cfn-iam-grouppolicy-policyname""", alias="PolicyName")
    PolicyDocument_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-grouppolicy.html#cfn-iam-grouppolicy-policydocument""", alias="PolicyDocument")
    

    @property
    def tropo_type(self) -> troposphere.iam.GroupPolicy:
        from troposphere.iam import GroupPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import GroupPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class InstanceProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html
    Properties:
        - Name: Path
        - Name: InstanceProfileName
        - Name: Roles
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html#cfn-iam-instanceprofile-path""", alias="Path")
    InstanceProfileName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html#cfn-iam-instanceprofile-instanceprofilename""", alias="InstanceProfileName")
    Roles_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html#cfn-iam-instanceprofile-roles""", alias="Roles")
    

    @property
    def tropo_type(self) -> troposphere.iam.InstanceProfile:
        from troposphere.iam import InstanceProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import InstanceProfile as TropoT
        return resource_to_troposphere(self, TropoT)


class ManagedPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html
    Properties:
        - Name: ManagedPolicyName
        - Name: Path
        - Name: Description
        - Name: Groups
        - Name: PolicyDocument
        - Name: Roles
        - Name: Users
    Attributes:
        - Name: IsAttachable
        - Name: UpdateDate
        - Name: PermissionsBoundaryUsageCount
        - Name: AttachmentCount
        - Name: PolicyArn
        - Name: DefaultVersionId
        - Name: CreateDate
        - Name: PolicyId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ManagedPolicyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-managedpolicyname""", alias="ManagedPolicyName")
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-path""", alias="Path")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-description""", alias="Description")
    Groups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-groups""", alias="Groups")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-policydocument""", alias="PolicyDocument")
    Roles_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-roles""", alias="Roles")
    Users_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-users""", alias="Users")
    

    @property
    def tropo_type(self) -> troposphere.iam.ManagedPolicy:
        from troposphere.iam import ManagedPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import ManagedPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class OIDCProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-oidcprovider.html
    Properties:
        - Name: ClientIdList
        - Name: ThumbprintList
        - Name: Url
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ClientIdList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-oidcprovider.html#cfn-iam-oidcprovider-clientidlist""", alias="ClientIdList")
    ThumbprintList_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-oidcprovider.html#cfn-iam-oidcprovider-thumbprintlist""", alias="ThumbprintList")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-oidcprovider.html#cfn-iam-oidcprovider-url""", alias="Url")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-oidcprovider.html#cfn-iam-oidcprovider-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iam.OIDCProvider:
        from troposphere.iam import OIDCProvider as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import OIDCProvider as TropoT
        return resource_to_troposphere(self, TropoT)


class Policy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html
    Properties:
        - Name: Groups
        - Name: PolicyName
        - Name: PolicyDocument
        - Name: Roles
        - Name: Users
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Groups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-groups""", alias="Groups")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policyname""", alias="PolicyName")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument""", alias="PolicyDocument")
    Roles_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-roles""", alias="Roles")
    Users_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-users""", alias="Users")
    

    @property
    def tropo_type(self) -> troposphere.iam.Policy:
        from troposphere.iam import Policy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import Policy as TropoT
        return resource_to_troposphere(self, TropoT)


class Role(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html
    Properties:
        - Name: Path
        - Name: ManagedPolicyArns
        - Name: MaxSessionDuration
        - Name: RoleName
        - Name: Description
        - Name: Policies
        - Name: AssumeRolePolicyDocument
        - Name: Tags
        - Name: PermissionsBoundary
    Attributes:
        - Name: Arn
        - Name: RoleId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-path""", alias="Path")
    ManagedPolicyArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-managedpolicyarns""", alias="ManagedPolicyArns")
    MaxSessionDuration_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-maxsessionduration""", alias="MaxSessionDuration")
    RoleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-rolename""", alias="RoleName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-description""", alias="Description")
    Policies_: Optional[List['Policy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-policies""", alias="Policies")
    AssumeRolePolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-assumerolepolicydocument""", alias="AssumeRolePolicyDocument")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-tags""", alias="Tags")
    PermissionsBoundary_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-permissionsboundary""", alias="PermissionsBoundary")
    

    @property
    def tropo_type(self) -> troposphere.iam.Role:
        from troposphere.iam import Role as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import Role as TropoT
        return resource_to_troposphere(self, TropoT)


class RolePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-rolepolicy.html
    Properties:
        - Name: RoleName
        - Name: PolicyName
        - Name: PolicyDocument
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RoleName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-rolepolicy.html#cfn-iam-rolepolicy-rolename""", alias="RoleName")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-rolepolicy.html#cfn-iam-rolepolicy-policyname""", alias="PolicyName")
    PolicyDocument_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-rolepolicy.html#cfn-iam-rolepolicy-policydocument""", alias="PolicyDocument")
    

    @property
    def tropo_type(self) -> troposphere.iam.RolePolicy:
        from troposphere.iam import RolePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import RolePolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class SAMLProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.html
    Properties:
        - Name: SamlMetadataDocument
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SamlMetadataDocument_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.html#cfn-iam-samlprovider-samlmetadatadocument""", alias="SamlMetadataDocument")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.html#cfn-iam-samlprovider-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.html#cfn-iam-samlprovider-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iam.SAMLProvider:
        from troposphere.iam import SAMLProvider as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import SAMLProvider as TropoT
        return resource_to_troposphere(self, TropoT)


class ServerCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html
    Properties:
        - Name: CertificateBody
        - Name: Path
        - Name: PrivateKey
        - Name: CertificateChain
        - Name: ServerCertificateName
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CertificateBody_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html#cfn-iam-servercertificate-certificatebody""", alias="CertificateBody")
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html#cfn-iam-servercertificate-path""", alias="Path")
    PrivateKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html#cfn-iam-servercertificate-privatekey""", alias="PrivateKey")
    CertificateChain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html#cfn-iam-servercertificate-certificatechain""", alias="CertificateChain")
    ServerCertificateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html#cfn-iam-servercertificate-servercertificatename""", alias="ServerCertificateName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html#cfn-iam-servercertificate-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iam.ServerCertificate:
        from troposphere.iam import ServerCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import ServerCertificate as TropoT
        return resource_to_troposphere(self, TropoT)


class ServiceLinkedRole(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html
    Properties:
        - Name: CustomSuffix
        - Name: Description
        - Name: AWSServiceName
    Attributes:
        - Name: RoleName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CustomSuffix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html#cfn-iam-servicelinkedrole-customsuffix""", alias="CustomSuffix")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html#cfn-iam-servicelinkedrole-description""", alias="Description")
    AWSServiceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html#cfn-iam-servicelinkedrole-awsservicename""", alias="AWSServiceName")
    

    @property
    def tropo_type(self) -> troposphere.iam.ServiceLinkedRole:
        from troposphere.iam import ServiceLinkedRole as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import ServiceLinkedRole as TropoT
        return resource_to_troposphere(self, TropoT)


class User(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html
    Properties:
        - Name: Path
        - Name: ManagedPolicyArns
        - Name: Policies
        - Name: UserName
        - Name: Groups
        - Name: LoginProfile
        - Name: Tags
        - Name: PermissionsBoundary
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-path""", alias="Path")
    ManagedPolicyArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-managedpolicyarns""", alias="ManagedPolicyArns")
    Policies_: Optional[List['Policy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-policies""", alias="Policies")
    UserName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-username""", alias="UserName")
    Groups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-groups""", alias="Groups")
    LoginProfile_: Optional['LoginProfile'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-loginprofile""", alias="LoginProfile")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-tags""", alias="Tags")
    PermissionsBoundary_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-permissionsboundary""", alias="PermissionsBoundary")
    

    @property
    def tropo_type(self) -> troposphere.iam.User:
        from troposphere.iam import User as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import User as TropoT
        return resource_to_troposphere(self, TropoT)


class UserPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-userpolicy.html
    Properties:
        - Name: UserName
        - Name: PolicyName
        - Name: PolicyDocument
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UserName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-userpolicy.html#cfn-iam-userpolicy-username""", alias="UserName")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-userpolicy.html#cfn-iam-userpolicy-policyname""", alias="PolicyName")
    PolicyDocument_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-userpolicy.html#cfn-iam-userpolicy-policydocument""", alias="PolicyDocument")
    

    @property
    def tropo_type(self) -> troposphere.iam.UserPolicy:
        from troposphere.iam import UserPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import UserPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class UserToGroupAddition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html
    Properties:
        - Name: GroupName
        - Name: Users
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html#cfn-iam-addusertogroup-groupname""", alias="GroupName")
    Users_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html#cfn-iam-addusertogroup-users""", alias="Users")
    

    @property
    def tropo_type(self) -> troposphere.iam.UserToGroupAddition:
        from troposphere.iam import UserToGroupAddition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import UserToGroupAddition as TropoT
        return resource_to_troposphere(self, TropoT)


class VirtualMFADevice(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-virtualmfadevice.html
    Properties:
        - Name: Path
        - Name: VirtualMfaDeviceName
        - Name: Users
        - Name: Tags
    Attributes:
        - Name: SerialNumber
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-virtualmfadevice.html#cfn-iam-virtualmfadevice-path""", alias="Path")
    VirtualMfaDeviceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-virtualmfadevice.html#cfn-iam-virtualmfadevice-virtualmfadevicename""", alias="VirtualMfaDeviceName")
    Users_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-virtualmfadevice.html#cfn-iam-virtualmfadevice-users""", alias="Users")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-virtualmfadevice.html#cfn-iam-virtualmfadevice-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iam.VirtualMFADevice:
        from troposphere.iam import VirtualMFADevice as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iam import VirtualMFADevice as TropoT
        return resource_to_troposphere(self, TropoT)

