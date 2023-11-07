from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class S3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-s3location.html
    Properties:
        - Name: S3Bucket
        - Name: S3Key
    
    """
    
    S3Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-s3location.html#cfn-appstream-appblock-s3location-s3bucket""", alias="S3Bucket")
    S3Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-s3location.html#cfn-appstream-appblock-s3location-s3key""", alias="S3Key")
    


    @property
    def tropo_type(self) -> troposphere.appstream.S3Location:
        from troposphere.appstream import S3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScriptDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-scriptdetails.html
    Properties:
        - Name: TimeoutInSeconds
        - Name: ScriptS3Location
        - Name: ExecutablePath
        - Name: ExecutableParameters
    
    """
    
    TimeoutInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-scriptdetails.html#cfn-appstream-appblock-scriptdetails-timeoutinseconds""", alias="TimeoutInSeconds")
    ScriptS3Location_: 'S3Location' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-scriptdetails.html#cfn-appstream-appblock-scriptdetails-scripts3location""", alias="ScriptS3Location")
    ExecutablePath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-scriptdetails.html#cfn-appstream-appblock-scriptdetails-executablepath""", alias="ExecutablePath")
    ExecutableParameters_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-scriptdetails.html#cfn-appstream-appblock-scriptdetails-executableparameters""", alias="ExecutableParameters")
    


    @property
    def tropo_type(self) -> troposphere.appstream.ScriptDetails:
        from troposphere.appstream import ScriptDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblockbuilder-accessendpoint.html
    Properties:
        - Name: EndpointType
        - Name: VpceId
    
    """
    
    EndpointType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblockbuilder-accessendpoint.html#cfn-appstream-appblockbuilder-accessendpoint-endpointtype""", alias="EndpointType")
    VpceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblockbuilder-accessendpoint.html#cfn-appstream-appblockbuilder-accessendpoint-vpceid""", alias="VpceId")
    


    @property
    def tropo_type(self) -> troposphere.appstream.AccessEndpoint:
        from troposphere.appstream import AccessEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblockbuilder-vpcconfig.html
    Properties:
        - Name: SecurityGroupIds
        - Name: SubnetIds
    
    """
    
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblockbuilder-vpcconfig.html#cfn-appstream-appblockbuilder-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblockbuilder-vpcconfig.html#cfn-appstream-appblockbuilder-vpcconfig-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.appstream.VpcConfig:
        from troposphere.appstream import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-application-s3location.html
    Properties:
        - Name: S3Bucket
        - Name: S3Key
    
    """
    
    S3Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-application-s3location.html#cfn-appstream-application-s3location-s3bucket""", alias="S3Bucket")
    S3Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-application-s3location.html#cfn-appstream-application-s3location-s3key""", alias="S3Key")
    


    @property
    def tropo_type(self) -> troposphere.appstream.S3Location:
        from troposphere.appstream import S3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CertificateBasedAuthProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-certificatebasedauthproperties.html
    Properties:
        - Name: Status
        - Name: CertificateAuthorityArn
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-certificatebasedauthproperties.html#cfn-appstream-directoryconfig-certificatebasedauthproperties-status""", alias="Status")
    CertificateAuthorityArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-certificatebasedauthproperties.html#cfn-appstream-directoryconfig-certificatebasedauthproperties-certificateauthorityarn""", alias="CertificateAuthorityArn")
    


    @property
    def tropo_type(self) -> troposphere.appstream.CertificateBasedAuthProperties:
        from troposphere.appstream import CertificateBasedAuthProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceAccountCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-serviceaccountcredentials.html
    Properties:
        - Name: AccountName
        - Name: AccountPassword
    
    """
    
    AccountName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-serviceaccountcredentials.html#cfn-appstream-directoryconfig-serviceaccountcredentials-accountname""", alias="AccountName")
    AccountPassword_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-serviceaccountcredentials.html#cfn-appstream-directoryconfig-serviceaccountcredentials-accountpassword""", alias="AccountPassword")
    


    @property
    def tropo_type(self) -> troposphere.appstream.ServiceAccountCredentials:
        from troposphere.appstream import ServiceAccountCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Attribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-entitlement-attribute.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-entitlement-attribute.html#cfn-appstream-entitlement-attribute-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-entitlement-attribute.html#cfn-appstream-entitlement-attribute-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.appstream.Attribute:
        from troposphere.appstream import Attribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComputeCapacity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-computecapacity.html
    Properties:
        - Name: DesiredInstances
        - Name: DesiredSessions
    
    """
    
    DesiredInstances_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-computecapacity.html#cfn-appstream-fleet-computecapacity-desiredinstances""", alias="DesiredInstances")
    DesiredSessions_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-computecapacity.html#cfn-appstream-fleet-computecapacity-desiredsessions""", alias="DesiredSessions")
    


    @property
    def tropo_type(self) -> troposphere.appstream.ComputeCapacity:
        from troposphere.appstream import ComputeCapacity as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DomainJoinInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-domainjoininfo.html
    Properties:
        - Name: OrganizationalUnitDistinguishedName
        - Name: DirectoryName
    
    """
    
    OrganizationalUnitDistinguishedName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-domainjoininfo.html#cfn-appstream-fleet-domainjoininfo-organizationalunitdistinguishedname""", alias="OrganizationalUnitDistinguishedName")
    DirectoryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-domainjoininfo.html#cfn-appstream-fleet-domainjoininfo-directoryname""", alias="DirectoryName")
    


    @property
    def tropo_type(self) -> troposphere.appstream.DomainJoinInfo:
        from troposphere.appstream import DomainJoinInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-s3location.html
    Properties:
        - Name: S3Bucket
        - Name: S3Key
    
    """
    
    S3Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-s3location.html#cfn-appstream-fleet-s3location-s3bucket""", alias="S3Bucket")
    S3Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-s3location.html#cfn-appstream-fleet-s3location-s3key""", alias="S3Key")
    


    @property
    def tropo_type(self) -> troposphere.appstream.S3Location:
        from troposphere.appstream import S3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-vpcconfig.html
    Properties:
        - Name: SubnetIds
        - Name: SecurityGroupIds
    
    """
    
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-vpcconfig.html#cfn-appstream-fleet-vpcconfig-subnetids""", alias="SubnetIds")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-vpcconfig.html#cfn-appstream-fleet-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.appstream.VpcConfig:
        from troposphere.appstream import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-accessendpoint.html
    Properties:
        - Name: EndpointType
        - Name: VpceId
    
    """
    
    EndpointType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-accessendpoint.html#cfn-appstream-imagebuilder-accessendpoint-endpointtype""", alias="EndpointType")
    VpceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-accessendpoint.html#cfn-appstream-imagebuilder-accessendpoint-vpceid""", alias="VpceId")
    


    @property
    def tropo_type(self) -> troposphere.appstream.AccessEndpoint:
        from troposphere.appstream import AccessEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DomainJoinInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-domainjoininfo.html
    Properties:
        - Name: OrganizationalUnitDistinguishedName
        - Name: DirectoryName
    
    """
    
    OrganizationalUnitDistinguishedName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-domainjoininfo.html#cfn-appstream-imagebuilder-domainjoininfo-organizationalunitdistinguishedname""", alias="OrganizationalUnitDistinguishedName")
    DirectoryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-domainjoininfo.html#cfn-appstream-imagebuilder-domainjoininfo-directoryname""", alias="DirectoryName")
    


    @property
    def tropo_type(self) -> troposphere.appstream.DomainJoinInfo:
        from troposphere.appstream import DomainJoinInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-vpcconfig.html
    Properties:
        - Name: SecurityGroupIds
        - Name: SubnetIds
    
    """
    
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-vpcconfig.html#cfn-appstream-imagebuilder-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-vpcconfig.html#cfn-appstream-imagebuilder-vpcconfig-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.appstream.VpcConfig:
        from troposphere.appstream import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-accessendpoint.html
    Properties:
        - Name: EndpointType
        - Name: VpceId
    
    """
    
    EndpointType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-accessendpoint.html#cfn-appstream-stack-accessendpoint-endpointtype""", alias="EndpointType")
    VpceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-accessendpoint.html#cfn-appstream-stack-accessendpoint-vpceid""", alias="VpceId")
    


    @property
    def tropo_type(self) -> troposphere.appstream.AccessEndpoint:
        from troposphere.appstream import AccessEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ApplicationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-applicationsettings.html
    Properties:
        - Name: SettingsGroup
        - Name: Enabled
    
    """
    
    SettingsGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-applicationsettings.html#cfn-appstream-stack-applicationsettings-settingsgroup""", alias="SettingsGroup")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-applicationsettings.html#cfn-appstream-stack-applicationsettings-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.appstream.ApplicationSettings:
        from troposphere.appstream import ApplicationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StorageConnector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-storageconnector.html
    Properties:
        - Name: Domains
        - Name: ResourceIdentifier
        - Name: ConnectorType
    
    """
    
    Domains_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-storageconnector.html#cfn-appstream-stack-storageconnector-domains""", alias="Domains")
    ResourceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-storageconnector.html#cfn-appstream-stack-storageconnector-resourceidentifier""", alias="ResourceIdentifier")
    ConnectorType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-storageconnector.html#cfn-appstream-stack-storageconnector-connectortype""", alias="ConnectorType")
    


    @property
    def tropo_type(self) -> troposphere.appstream.StorageConnector:
        from troposphere.appstream import StorageConnector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StreamingExperienceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-streamingexperiencesettings.html
    Properties:
        - Name: PreferredProtocol
    
    """
    
    PreferredProtocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-streamingexperiencesettings.html#cfn-appstream-stack-streamingexperiencesettings-preferredprotocol""", alias="PreferredProtocol")
    


    @property
    def tropo_type(self) -> troposphere.appstream.StreamingExperienceSettings:
        from troposphere.appstream import StreamingExperienceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-usersetting.html
    Properties:
        - Name: Action
        - Name: MaximumLength
        - Name: Permission
    
    """
    
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-usersetting.html#cfn-appstream-stack-usersetting-action""", alias="Action")
    MaximumLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-usersetting.html#cfn-appstream-stack-usersetting-maximumlength""", alias="MaximumLength")
    Permission_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-usersetting.html#cfn-appstream-stack-usersetting-permission""", alias="Permission")
    


    @property
    def tropo_type(self) -> troposphere.appstream.UserSetting:
        from troposphere.appstream import UserSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AppBlock(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html
    Properties:
        - Name: SetupScriptDetails
        - Name: Description
        - Name: PostSetupScriptDetails
        - Name: DisplayName
        - Name: SourceS3Location
        - Name: Tags
        - Name: PackagingType
        - Name: Name
    Attributes:
        - Name: CreatedTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SetupScriptDetails_: Optional['ScriptDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-setupscriptdetails""", alias="SetupScriptDetails")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-description""", alias="Description")
    PostSetupScriptDetails_: Optional['ScriptDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-postsetupscriptdetails""", alias="PostSetupScriptDetails")
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-displayname""", alias="DisplayName")
    SourceS3Location_: 'S3Location' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-sources3location""", alias="SourceS3Location")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-tags""", alias="Tags")
    PackagingType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-packagingtype""", alias="PackagingType")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html#cfn-appstream-appblock-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.appstream.AppBlock:
        from troposphere.appstream import AppBlock as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appstream import AppBlock as TropoT
        return resource_to_troposphere(self, TropoT)


class AppBlockBuilder(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html
    Properties:
        - Name: Description
        - Name: Platform
        - Name: VpcConfig
        - Name: AppBlockArns
        - Name: EnableDefaultInternetAccess
        - Name: DisplayName
        - Name: IamRoleArn
        - Name: InstanceType
        - Name: Tags
        - Name: Name
        - Name: AccessEndpoints
    Attributes:
        - Name: CreatedTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-description""", alias="Description")
    Platform_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-platform""", alias="Platform")
    VpcConfig_: 'VpcConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-vpcconfig""", alias="VpcConfig")
    AppBlockArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-appblockarns""", alias="AppBlockArns")
    EnableDefaultInternetAccess_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-enabledefaultinternetaccess""", alias="EnableDefaultInternetAccess")
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-displayname""", alias="DisplayName")
    IamRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-iamrolearn""", alias="IamRoleArn")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-instancetype""", alias="InstanceType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-name""", alias="Name")
    AccessEndpoints_: Optional[List['AccessEndpoint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblockbuilder.html#cfn-appstream-appblockbuilder-accessendpoints""", alias="AccessEndpoints")
    

    @property
    def tropo_type(self) -> troposphere.appstream.AppBlockBuilder:
        from troposphere.appstream import AppBlockBuilder as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appstream import AppBlockBuilder as TropoT
        return resource_to_troposphere(self, TropoT)


class Application(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html
    Properties:
        - Name: WorkingDirectory
        - Name: Platforms
        - Name: AppBlockArn
        - Name: Description
        - Name: InstanceFamilies
        - Name: AttributesToDelete
        - Name: DisplayName
        - Name: LaunchPath
        - Name: LaunchParameters
        - Name: Tags
        - Name: Name
        - Name: IconS3Location
    Attributes:
        - Name: CreatedTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    WorkingDirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-workingdirectory""", alias="WorkingDirectory")
    Platforms_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-platforms""", alias="Platforms")
    AppBlockArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-appblockarn""", alias="AppBlockArn")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-description""", alias="Description")
    InstanceFamilies_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-instancefamilies""", alias="InstanceFamilies")
    AttributesToDelete_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-attributestodelete""", alias="AttributesToDelete")
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-displayname""", alias="DisplayName")
    LaunchPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-launchpath""", alias="LaunchPath")
    LaunchParameters_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-launchparameters""", alias="LaunchParameters")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-name""", alias="Name")
    IconS3Location_: 'S3Location' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html#cfn-appstream-application-icons3location""", alias="IconS3Location")
    

    @property
    def tropo_type(self) -> troposphere.appstream.Application:
        from troposphere.appstream import Application as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appstream import Application as TropoT
        return resource_to_troposphere(self, TropoT)


class ApplicationEntitlementAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationentitlementassociation.html
    Properties:
        - Name: EntitlementName
        - Name: ApplicationIdentifier
        - Name: StackName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EntitlementName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationentitlementassociation.html#cfn-appstream-applicationentitlementassociation-entitlementname""", alias="EntitlementName")
    ApplicationIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationentitlementassociation.html#cfn-appstream-applicationentitlementassociation-applicationidentifier""", alias="ApplicationIdentifier")
    StackName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationentitlementassociation.html#cfn-appstream-applicationentitlementassociation-stackname""", alias="StackName")
    

    @property
    def tropo_type(self) -> troposphere.appstream.ApplicationEntitlementAssociation:
        from troposphere.appstream import ApplicationEntitlementAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appstream import ApplicationEntitlementAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class ApplicationFleetAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationfleetassociation.html
    Properties:
        - Name: FleetName
        - Name: ApplicationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FleetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationfleetassociation.html#cfn-appstream-applicationfleetassociation-fleetname""", alias="FleetName")
    ApplicationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationfleetassociation.html#cfn-appstream-applicationfleetassociation-applicationarn""", alias="ApplicationArn")
    

    @property
    def tropo_type(self) -> troposphere.appstream.ApplicationFleetAssociation:
        from troposphere.appstream import ApplicationFleetAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appstream import ApplicationFleetAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class DirectoryConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html
    Properties:
        - Name: OrganizationalUnitDistinguishedNames
        - Name: ServiceAccountCredentials
        - Name: CertificateBasedAuthProperties
        - Name: DirectoryName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OrganizationalUnitDistinguishedNames_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html#cfn-appstream-directoryconfig-organizationalunitdistinguishednames""", alias="OrganizationalUnitDistinguishedNames")
    ServiceAccountCredentials_: 'ServiceAccountCredentials' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html#cfn-appstream-directoryconfig-serviceaccountcredentials""", alias="ServiceAccountCredentials")
    CertificateBasedAuthProperties_: Optional['CertificateBasedAuthProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html#cfn-appstream-directoryconfig-certificatebasedauthproperties""", alias="CertificateBasedAuthProperties")
    DirectoryName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html#cfn-appstream-directoryconfig-directoryname""", alias="DirectoryName")
    

    @property
    def tropo_type(self) -> troposphere.appstream.DirectoryConfig:
        from troposphere.appstream import DirectoryConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appstream import DirectoryConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class Entitlement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html
    Properties:
        - Name: AppVisibility
        - Name: Description
        - Name: Attributes
        - Name: StackName
        - Name: Name
    Attributes:
        - Name: CreatedTime
        - Name: LastModifiedTime
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AppVisibility_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html#cfn-appstream-entitlement-appvisibility""", alias="AppVisibility")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html#cfn-appstream-entitlement-description""", alias="Description")
    Attributes_: List['Attribute'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html#cfn-appstream-entitlement-attributes""", alias="Attributes")
    StackName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html#cfn-appstream-entitlement-stackname""", alias="StackName")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html#cfn-appstream-entitlement-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.appstream.Entitlement:
        from troposphere.appstream import Entitlement as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appstream import Entitlement as TropoT
        return resource_to_troposphere(self, TropoT)


class Fleet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html
    Properties:
        - Name: Description
        - Name: ComputeCapacity
        - Name: Platform
        - Name: VpcConfig
        - Name: FleetType
        - Name: EnableDefaultInternetAccess
        - Name: DomainJoinInfo
        - Name: SessionScriptS3Location
        - Name: Name
        - Name: ImageName
        - Name: MaxUserDurationInSeconds
        - Name: IdleDisconnectTimeoutInSeconds
        - Name: UsbDeviceFilterStrings
        - Name: DisconnectTimeoutInSeconds
        - Name: DisplayName
        - Name: StreamView
        - Name: IamRoleArn
        - Name: MaxSessionsPerInstance
        - Name: InstanceType
        - Name: MaxConcurrentSessions
        - Name: Tags
        - Name: ImageArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-description""", alias="Description")
    ComputeCapacity_: Optional['ComputeCapacity'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-computecapacity""", alias="ComputeCapacity")
    Platform_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-platform""", alias="Platform")
    VpcConfig_: Optional['VpcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-vpcconfig""", alias="VpcConfig")
    FleetType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-fleettype""", alias="FleetType")
    EnableDefaultInternetAccess_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-enabledefaultinternetaccess""", alias="EnableDefaultInternetAccess")
    DomainJoinInfo_: Optional['DomainJoinInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-domainjoininfo""", alias="DomainJoinInfo")
    SessionScriptS3Location_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-sessionscripts3location""", alias="SessionScriptS3Location")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-name""", alias="Name")
    ImageName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-imagename""", alias="ImageName")
    MaxUserDurationInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-maxuserdurationinseconds""", alias="MaxUserDurationInSeconds")
    IdleDisconnectTimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-idledisconnecttimeoutinseconds""", alias="IdleDisconnectTimeoutInSeconds")
    UsbDeviceFilterStrings_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-usbdevicefilterstrings""", alias="UsbDeviceFilterStrings")
    DisconnectTimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-disconnecttimeoutinseconds""", alias="DisconnectTimeoutInSeconds")
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-displayname""", alias="DisplayName")
    StreamView_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-streamview""", alias="StreamView")
    IamRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-iamrolearn""", alias="IamRoleArn")
    MaxSessionsPerInstance_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-maxsessionsperinstance""", alias="MaxSessionsPerInstance")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-instancetype""", alias="InstanceType")
    MaxConcurrentSessions_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-maxconcurrentsessions""", alias="MaxConcurrentSessions")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-tags""", alias="Tags")
    ImageArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html#cfn-appstream-fleet-imagearn""", alias="ImageArn")
    

    @property
    def tropo_type(self) -> troposphere.appstream.Fleet:
        from troposphere.appstream import Fleet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appstream import Fleet as TropoT
        return resource_to_troposphere(self, TropoT)


class ImageBuilder(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html
    Properties:
        - Name: Description
        - Name: VpcConfig
        - Name: EnableDefaultInternetAccess
        - Name: DomainJoinInfo
        - Name: AppstreamAgentVersion
        - Name: Name
        - Name: ImageName
        - Name: DisplayName
        - Name: IamRoleArn
        - Name: InstanceType
        - Name: Tags
        - Name: ImageArn
        - Name: AccessEndpoints
    Attributes:
        - Name: StreamingUrl
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-description""", alias="Description")
    VpcConfig_: Optional['VpcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-vpcconfig""", alias="VpcConfig")
    EnableDefaultInternetAccess_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-enabledefaultinternetaccess""", alias="EnableDefaultInternetAccess")
    DomainJoinInfo_: Optional['DomainJoinInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-domainjoininfo""", alias="DomainJoinInfo")
    AppstreamAgentVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-appstreamagentversion""", alias="AppstreamAgentVersion")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-name""", alias="Name")
    ImageName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-imagename""", alias="ImageName")
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-displayname""", alias="DisplayName")
    IamRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-iamrolearn""", alias="IamRoleArn")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-instancetype""", alias="InstanceType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-tags""", alias="Tags")
    ImageArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-imagearn""", alias="ImageArn")
    AccessEndpoints_: Optional[List['AccessEndpoint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html#cfn-appstream-imagebuilder-accessendpoints""", alias="AccessEndpoints")
    

    @property
    def tropo_type(self) -> troposphere.appstream.ImageBuilder:
        from troposphere.appstream import ImageBuilder as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appstream import ImageBuilder as TropoT
        return resource_to_troposphere(self, TropoT)


class Stack(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html
    Properties:
        - Name: Description
        - Name: StorageConnectors
        - Name: DeleteStorageConnectors
        - Name: EmbedHostDomains
        - Name: UserSettings
        - Name: AttributesToDelete
        - Name: RedirectURL
        - Name: StreamingExperienceSettings
        - Name: Name
        - Name: FeedbackURL
        - Name: ApplicationSettings
        - Name: DisplayName
        - Name: Tags
        - Name: AccessEndpoints
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-description""", alias="Description")
    StorageConnectors_: Optional[List['StorageConnector']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-storageconnectors""", alias="StorageConnectors")
    DeleteStorageConnectors_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-deletestorageconnectors""", alias="DeleteStorageConnectors")
    EmbedHostDomains_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-embedhostdomains""", alias="EmbedHostDomains")
    UserSettings_: Optional[List['UserSetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-usersettings""", alias="UserSettings")
    AttributesToDelete_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-attributestodelete""", alias="AttributesToDelete")
    RedirectURL_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-redirecturl""", alias="RedirectURL")
    StreamingExperienceSettings_: Optional['StreamingExperienceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-streamingexperiencesettings""", alias="StreamingExperienceSettings")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-name""", alias="Name")
    FeedbackURL_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-feedbackurl""", alias="FeedbackURL")
    ApplicationSettings_: Optional['ApplicationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-applicationsettings""", alias="ApplicationSettings")
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-displayname""", alias="DisplayName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-tags""", alias="Tags")
    AccessEndpoints_: Optional[List['AccessEndpoint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html#cfn-appstream-stack-accessendpoints""", alias="AccessEndpoints")
    

    @property
    def tropo_type(self) -> troposphere.appstream.Stack:
        from troposphere.appstream import Stack as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appstream import Stack as TropoT
        return resource_to_troposphere(self, TropoT)


class StackFleetAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html
    Properties:
        - Name: FleetName
        - Name: StackName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FleetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html#cfn-appstream-stackfleetassociation-fleetname""", alias="FleetName")
    StackName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html#cfn-appstream-stackfleetassociation-stackname""", alias="StackName")
    

    @property
    def tropo_type(self) -> troposphere.appstream.StackFleetAssociation:
        from troposphere.appstream import StackFleetAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appstream import StackFleetAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class StackUserAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html
    Properties:
        - Name: SendEmailNotification
        - Name: UserName
        - Name: StackName
        - Name: AuthenticationType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SendEmailNotification_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html#cfn-appstream-stackuserassociation-sendemailnotification""", alias="SendEmailNotification")
    UserName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html#cfn-appstream-stackuserassociation-username""", alias="UserName")
    StackName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html#cfn-appstream-stackuserassociation-stackname""", alias="StackName")
    AuthenticationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html#cfn-appstream-stackuserassociation-authenticationtype""", alias="AuthenticationType")
    

    @property
    def tropo_type(self) -> troposphere.appstream.StackUserAssociation:
        from troposphere.appstream import StackUserAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appstream import StackUserAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class User(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html
    Properties:
        - Name: UserName
        - Name: FirstName
        - Name: MessageAction
        - Name: LastName
        - Name: AuthenticationType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UserName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html#cfn-appstream-user-username""", alias="UserName")
    FirstName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html#cfn-appstream-user-firstname""", alias="FirstName")
    MessageAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html#cfn-appstream-user-messageaction""", alias="MessageAction")
    LastName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html#cfn-appstream-user-lastname""", alias="LastName")
    AuthenticationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html#cfn-appstream-user-authenticationtype""", alias="AuthenticationType")
    

    @property
    def tropo_type(self) -> troposphere.appstream.User:
        from troposphere.appstream import User as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appstream import User as TropoT
        return resource_to_troposphere(self, TropoT)

