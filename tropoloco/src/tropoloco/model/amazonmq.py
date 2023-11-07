from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ConfigurationId(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-configurationid.html
    Properties:
        - Name: Revision
        - Name: Id
    
    """
    
    Revision_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-configurationid.html#cfn-amazonmq-broker-configurationid-revision""", alias="Revision")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-configurationid.html#cfn-amazonmq-broker-configurationid-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.amazonmq.ConfigurationId:
        from troposphere.amazonmq import ConfigurationId as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-encryptionoptions.html
    Properties:
        - Name: KmsKeyId
        - Name: UseAwsOwnedKey
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-encryptionoptions.html#cfn-amazonmq-broker-encryptionoptions-kmskeyid""", alias="KmsKeyId")
    UseAwsOwnedKey_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-encryptionoptions.html#cfn-amazonmq-broker-encryptionoptions-useawsownedkey""", alias="UseAwsOwnedKey")
    


    @property
    def tropo_type(self) -> troposphere.amazonmq.EncryptionOptions:
        from troposphere.amazonmq import EncryptionOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LdapServerMetadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html
    Properties:
        - Name: Hosts
        - Name: UserRoleName
        - Name: UserSearchMatching
        - Name: RoleName
        - Name: UserBase
        - Name: UserSearchSubtree
        - Name: RoleSearchMatching
        - Name: ServiceAccountUsername
        - Name: RoleBase
        - Name: ServiceAccountPassword
        - Name: RoleSearchSubtree
    
    """
    
    Hosts_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-hosts""", alias="Hosts")
    UserRoleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-userrolename""", alias="UserRoleName")
    UserSearchMatching_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-usersearchmatching""", alias="UserSearchMatching")
    RoleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-rolename""", alias="RoleName")
    UserBase_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-userbase""", alias="UserBase")
    UserSearchSubtree_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-usersearchsubtree""", alias="UserSearchSubtree")
    RoleSearchMatching_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-rolesearchmatching""", alias="RoleSearchMatching")
    ServiceAccountUsername_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-serviceaccountusername""", alias="ServiceAccountUsername")
    RoleBase_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-rolebase""", alias="RoleBase")
    ServiceAccountPassword_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-serviceaccountpassword""", alias="ServiceAccountPassword")
    RoleSearchSubtree_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-rolesearchsubtree""", alias="RoleSearchSubtree")
    


    @property
    def tropo_type(self) -> troposphere.amazonmq.LdapServerMetadata:
        from troposphere.amazonmq import LdapServerMetadata as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogList(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-loglist.html
    Properties:
        - Name: Audit
        - Name: General
    
    """
    
    Audit_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-loglist.html#cfn-amazonmq-broker-loglist-audit""", alias="Audit")
    General_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-loglist.html#cfn-amazonmq-broker-loglist-general""", alias="General")
    


    @property
    def tropo_type(self) -> troposphere.amazonmq.LogsConfiguration:
        from troposphere.amazonmq import LogsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MaintenanceWindow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html
    Properties:
        - Name: DayOfWeek
        - Name: TimeOfDay
        - Name: TimeZone
    
    """
    
    DayOfWeek_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html#cfn-amazonmq-broker-maintenancewindow-dayofweek""", alias="DayOfWeek")
    TimeOfDay_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html#cfn-amazonmq-broker-maintenancewindow-timeofday""", alias="TimeOfDay")
    TimeZone_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html#cfn-amazonmq-broker-maintenancewindow-timezone""", alias="TimeZone")
    


    @property
    def tropo_type(self) -> troposphere.amazonmq.MaintenanceWindow:
        from troposphere.amazonmq import MaintenanceWindow as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagsEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-tagsentry.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-tagsentry.html#cfn-amazonmq-broker-tagsentry-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-tagsentry.html#cfn-amazonmq-broker-tagsentry-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.amazonmq.TagsEntry:
        from troposphere.amazonmq import TagsEntry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class User(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html
    Properties:
        - Name: Username
        - Name: Groups
        - Name: ConsoleAccess
        - Name: Password
    
    """
    
    Username_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html#cfn-amazonmq-broker-user-username""", alias="Username")
    Groups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html#cfn-amazonmq-broker-user-groups""", alias="Groups")
    ConsoleAccess_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html#cfn-amazonmq-broker-user-consoleaccess""", alias="ConsoleAccess")
    Password_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html#cfn-amazonmq-broker-user-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.amazonmq.User:
        from troposphere.amazonmq import User as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagsEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configuration-tagsentry.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configuration-tagsentry.html#cfn-amazonmq-configuration-tagsentry-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configuration-tagsentry.html#cfn-amazonmq-configuration-tagsentry-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.amazonmq.TagsEntry:
        from troposphere.amazonmq import TagsEntry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfigurationId(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configurationassociation-configurationid.html
    Properties:
        - Name: Revision
        - Name: Id
    
    """
    
    Revision_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configurationassociation-configurationid.html#cfn-amazonmq-configurationassociation-configurationid-revision""", alias="Revision")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configurationassociation-configurationid.html#cfn-amazonmq-configurationassociation-configurationid-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.amazonmq.ConfigurationId:
        from troposphere.amazonmq import ConfigurationId as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Broker(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html
    Properties:
        - Name: SecurityGroups
        - Name: DataReplicationPrimaryBrokerArn
        - Name: StorageType
        - Name: EngineVersion
        - Name: Configuration
        - Name: AuthenticationStrategy
        - Name: MaintenanceWindowStartTime
        - Name: HostInstanceType
        - Name: AutoMinorVersionUpgrade
        - Name: Users
        - Name: Logs
        - Name: SubnetIds
        - Name: DataReplicationMode
        - Name: BrokerName
        - Name: LdapServerMetadata
        - Name: DeploymentMode
        - Name: EngineType
        - Name: PubliclyAccessible
        - Name: EncryptionOptions
        - Name: Tags
    Attributes:
        - Name: IpAddresses
        - Name: OpenWireEndpoints
        - Name: ConfigurationRevision
        - Name: StompEndpoints
        - Name: MqttEndpoints
        - Name: AmqpEndpoints
        - Name: Arn
        - Name: ConfigurationId
        - Name: WssEndpoints
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-securitygroups""", alias="SecurityGroups")
    DataReplicationPrimaryBrokerArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-datareplicationprimarybrokerarn""", alias="DataReplicationPrimaryBrokerArn")
    StorageType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-storagetype""", alias="StorageType")
    EngineVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-engineversion""", alias="EngineVersion")
    Configuration_: Optional['ConfigurationId'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-configuration""", alias="Configuration")
    AuthenticationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-authenticationstrategy""", alias="AuthenticationStrategy")
    MaintenanceWindowStartTime_: Optional['MaintenanceWindow'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-maintenancewindowstarttime""", alias="MaintenanceWindowStartTime")
    HostInstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-hostinstancetype""", alias="HostInstanceType")
    AutoMinorVersionUpgrade_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-autominorversionupgrade""", alias="AutoMinorVersionUpgrade")
    Users_: List['User'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-users""", alias="Users")
    Logs_: Optional['LogList'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-logs""", alias="Logs")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-subnetids""", alias="SubnetIds")
    DataReplicationMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-datareplicationmode""", alias="DataReplicationMode")
    BrokerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-brokername""", alias="BrokerName")
    LdapServerMetadata_: Optional['LdapServerMetadata'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-ldapservermetadata""", alias="LdapServerMetadata")
    DeploymentMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-deploymentmode""", alias="DeploymentMode")
    EngineType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-enginetype""", alias="EngineType")
    PubliclyAccessible_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-publiclyaccessible""", alias="PubliclyAccessible")
    EncryptionOptions_: Optional['EncryptionOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-encryptionoptions""", alias="EncryptionOptions")
    Tags_: Optional[List['TagsEntry']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.amazonmq.Broker:
        from troposphere.amazonmq import Broker as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.amazonmq import Broker as TropoT
        return resource_to_troposphere(self, TropoT)


class Configuration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html
    Properties:
        - Name: EngineVersion
        - Name: Description
        - Name: AuthenticationStrategy
        - Name: EngineType
        - Name: Data
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Revision
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EngineVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-engineversion""", alias="EngineVersion")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-description""", alias="Description")
    AuthenticationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-authenticationstrategy""", alias="AuthenticationStrategy")
    EngineType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-enginetype""", alias="EngineType")
    Data_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-data""", alias="Data")
    Tags_: Optional[List['TagsEntry']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.amazonmq.Configuration:
        from troposphere.amazonmq import Configuration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.amazonmq import Configuration as TropoT
        return resource_to_troposphere(self, TropoT)


class ConfigurationAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html
    Properties:
        - Name: Broker
        - Name: Configuration
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Broker_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html#cfn-amazonmq-configurationassociation-broker""", alias="Broker")
    Configuration_: 'ConfigurationId' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html#cfn-amazonmq-configurationassociation-configuration""", alias="Configuration")
    

    @property
    def tropo_type(self) -> troposphere.amazonmq.ConfigurationAssociation:
        from troposphere.amazonmq import ConfigurationAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.amazonmq import ConfigurationAssociation as TropoT
        return resource_to_troposphere(self, TropoT)

