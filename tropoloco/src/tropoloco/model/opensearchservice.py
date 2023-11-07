from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AdvancedSecurityOptionsInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html
    Properties:
        - Name: AnonymousAuthEnabled
        - Name: InternalUserDatabaseEnabled
        - Name: SAMLOptions
        - Name: Enabled
        - Name: AnonymousAuthDisableDate
        - Name: MasterUserOptions
    
    """
    
    AnonymousAuthEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-anonymousauthenabled""", alias="AnonymousAuthEnabled")
    InternalUserDatabaseEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-internaluserdatabaseenabled""", alias="InternalUserDatabaseEnabled")
    SAMLOptions_: Optional['SAMLOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-samloptions""", alias="SAMLOptions")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-enabled""", alias="Enabled")
    AnonymousAuthDisableDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-anonymousauthdisabledate""", alias="AnonymousAuthDisableDate")
    MasterUserOptions_: Optional['MasterUserOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-masteruseroptions""", alias="MasterUserOptions")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.AdvancedSecurityOptionsInput:
        from troposphere.opensearchservice import AdvancedSecurityOptionsInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClusterConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html
    Properties:
        - Name: InstanceCount
        - Name: MultiAZWithStandbyEnabled
        - Name: WarmEnabled
        - Name: WarmCount
        - Name: DedicatedMasterEnabled
        - Name: ZoneAwarenessConfig
        - Name: DedicatedMasterCount
        - Name: InstanceType
        - Name: WarmType
        - Name: ZoneAwarenessEnabled
        - Name: DedicatedMasterType
    
    """
    
    InstanceCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-instancecount""", alias="InstanceCount")
    MultiAZWithStandbyEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-multiazwithstandbyenabled""", alias="MultiAZWithStandbyEnabled")
    WarmEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-warmenabled""", alias="WarmEnabled")
    WarmCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-warmcount""", alias="WarmCount")
    DedicatedMasterEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-dedicatedmasterenabled""", alias="DedicatedMasterEnabled")
    ZoneAwarenessConfig_: Optional['ZoneAwarenessConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-zoneawarenessconfig""", alias="ZoneAwarenessConfig")
    DedicatedMasterCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-dedicatedmastercount""", alias="DedicatedMasterCount")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-instancetype""", alias="InstanceType")
    WarmType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-warmtype""", alias="WarmType")
    ZoneAwarenessEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-zoneawarenessenabled""", alias="ZoneAwarenessEnabled")
    DedicatedMasterType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-dedicatedmastertype""", alias="DedicatedMasterType")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.ClusterConfig:
        from troposphere.opensearchservice import ClusterConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CognitoOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html
    Properties:
        - Name: UserPoolId
        - Name: Enabled
        - Name: IdentityPoolId
        - Name: RoleArn
    
    """
    
    UserPoolId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-userpoolid""", alias="UserPoolId")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-enabled""", alias="Enabled")
    IdentityPoolId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-identitypoolid""", alias="IdentityPoolId")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.CognitoOptions:
        from troposphere.opensearchservice import CognitoOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DomainEndpointOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html
    Properties:
        - Name: CustomEndpointEnabled
        - Name: EnforceHTTPS
        - Name: CustomEndpointCertificateArn
        - Name: CustomEndpoint
        - Name: TLSSecurityPolicy
    
    """
    
    CustomEndpointEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-customendpointenabled""", alias="CustomEndpointEnabled")
    EnforceHTTPS_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-enforcehttps""", alias="EnforceHTTPS")
    CustomEndpointCertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-customendpointcertificatearn""", alias="CustomEndpointCertificateArn")
    CustomEndpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-customendpoint""", alias="CustomEndpoint")
    TLSSecurityPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-tlssecuritypolicy""", alias="TLSSecurityPolicy")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.DomainEndpointOptions:
        from troposphere.opensearchservice import DomainEndpointOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EBSOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html
    Properties:
        - Name: EBSEnabled
        - Name: VolumeType
        - Name: Throughput
        - Name: Iops
        - Name: VolumeSize
    
    """
    
    EBSEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-ebsenabled""", alias="EBSEnabled")
    VolumeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-volumetype""", alias="VolumeType")
    Throughput_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-throughput""", alias="Throughput")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-iops""", alias="Iops")
    VolumeSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-volumesize""", alias="VolumeSize")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.EBSOptions:
        from troposphere.opensearchservice import EBSOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionAtRestOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html
    Properties:
        - Name: KmsKeyId
        - Name: Enabled
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html#cfn-opensearchservice-domain-encryptionatrestoptions-kmskeyid""", alias="KmsKeyId")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html#cfn-opensearchservice-domain-encryptionatrestoptions-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.EncryptionAtRestOptions:
        from troposphere.opensearchservice import EncryptionAtRestOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Idp(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-idp.html
    Properties:
        - Name: EntityId
        - Name: MetadataContent
    
    """
    
    EntityId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-idp.html#cfn-opensearchservice-domain-idp-entityid""", alias="EntityId")
    MetadataContent_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-idp.html#cfn-opensearchservice-domain-idp-metadatacontent""", alias="MetadataContent")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.Idp:
        from troposphere.opensearchservice import Idp as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogPublishingOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-logpublishingoption.html
    Properties:
        - Name: CloudWatchLogsLogGroupArn
        - Name: Enabled
    
    """
    
    CloudWatchLogsLogGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-logpublishingoption.html#cfn-opensearchservice-domain-logpublishingoption-cloudwatchlogsloggrouparn""", alias="CloudWatchLogsLogGroupArn")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-logpublishingoption.html#cfn-opensearchservice-domain-logpublishingoption-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.LogPublishingOption:
        from troposphere.opensearchservice import LogPublishingOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MasterUserOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html
    Properties:
        - Name: MasterUserPassword
        - Name: MasterUserARN
        - Name: MasterUserName
    
    """
    
    MasterUserPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html#cfn-opensearchservice-domain-masteruseroptions-masteruserpassword""", alias="MasterUserPassword")
    MasterUserARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html#cfn-opensearchservice-domain-masteruseroptions-masteruserarn""", alias="MasterUserARN")
    MasterUserName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html#cfn-opensearchservice-domain-masteruseroptions-masterusername""", alias="MasterUserName")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.MasterUserOptions:
        from troposphere.opensearchservice import MasterUserOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NodeToNodeEncryptionOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-nodetonodeencryptionoptions.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-nodetonodeencryptionoptions.html#cfn-opensearchservice-domain-nodetonodeencryptionoptions-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.NodeToNodeEncryptionOptions:
        from troposphere.opensearchservice import NodeToNodeEncryptionOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OffPeakWindow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-offpeakwindow.html
    Properties:
        - Name: WindowStartTime
    
    """
    
    WindowStartTime_: Optional['WindowStartTime'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-offpeakwindow.html#cfn-opensearchservice-domain-offpeakwindow-windowstarttime""", alias="WindowStartTime")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.OffPeakWindow:
        from troposphere.opensearchservice import OffPeakWindow as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OffPeakWindowOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-offpeakwindowoptions.html
    Properties:
        - Name: OffPeakWindow
        - Name: Enabled
    
    """
    
    OffPeakWindow_: Optional['OffPeakWindow'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-offpeakwindowoptions.html#cfn-opensearchservice-domain-offpeakwindowoptions-offpeakwindow""", alias="OffPeakWindow")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-offpeakwindowoptions.html#cfn-opensearchservice-domain-offpeakwindowoptions-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.OffPeakWindowOptions:
        from troposphere.opensearchservice import OffPeakWindowOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SAMLOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html
    Properties:
        - Name: MasterBackendRole
        - Name: SubjectKey
        - Name: Idp
        - Name: SessionTimeoutMinutes
        - Name: RolesKey
        - Name: Enabled
        - Name: MasterUserName
    
    """
    
    MasterBackendRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-masterbackendrole""", alias="MasterBackendRole")
    SubjectKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-subjectkey""", alias="SubjectKey")
    Idp_: Optional['Idp'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-idp""", alias="Idp")
    SessionTimeoutMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-sessiontimeoutminutes""", alias="SessionTimeoutMinutes")
    RolesKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-roleskey""", alias="RolesKey")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-enabled""", alias="Enabled")
    MasterUserName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-samloptions.html#cfn-opensearchservice-domain-samloptions-masterusername""", alias="MasterUserName")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.SAMLOptions:
        from troposphere.opensearchservice import SAMLOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceSoftwareOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html
    Properties:
        - Name: NewVersion
        - Name: UpdateStatus
        - Name: Description
        - Name: Cancellable
        - Name: CurrentVersion
        - Name: AutomatedUpdateDate
        - Name: UpdateAvailable
        - Name: OptionalDeployment
    
    """
    
    NewVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-newversion""", alias="NewVersion")
    UpdateStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-updatestatus""", alias="UpdateStatus")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-description""", alias="Description")
    Cancellable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-cancellable""", alias="Cancellable")
    CurrentVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-currentversion""", alias="CurrentVersion")
    AutomatedUpdateDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-automatedupdatedate""", alias="AutomatedUpdateDate")
    UpdateAvailable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-updateavailable""", alias="UpdateAvailable")
    OptionalDeployment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-servicesoftwareoptions.html#cfn-opensearchservice-domain-servicesoftwareoptions-optionaldeployment""", alias="OptionalDeployment")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.ServiceSoftwareOptions:
        from troposphere.opensearchservice import ServiceSoftwareOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnapshotOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-snapshotoptions.html
    Properties:
        - Name: AutomatedSnapshotStartHour
    
    """
    
    AutomatedSnapshotStartHour_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-snapshotoptions.html#cfn-opensearchservice-domain-snapshotoptions-automatedsnapshotstarthour""", alias="AutomatedSnapshotStartHour")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.SnapshotOptions:
        from troposphere.opensearchservice import SnapshotOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SoftwareUpdateOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-softwareupdateoptions.html
    Properties:
        - Name: AutoSoftwareUpdateEnabled
    
    """
    
    AutoSoftwareUpdateEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-softwareupdateoptions.html#cfn-opensearchservice-domain-softwareupdateoptions-autosoftwareupdateenabled""", alias="AutoSoftwareUpdateEnabled")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.SoftwareUpdateOptions:
        from troposphere.opensearchservice import SoftwareUpdateOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VPCOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-vpcoptions.html
    Properties:
        - Name: SecurityGroupIds
        - Name: SubnetIds
    
    """
    
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-vpcoptions.html#cfn-opensearchservice-domain-vpcoptions-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-vpcoptions.html#cfn-opensearchservice-domain-vpcoptions-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.VPCOptions:
        from troposphere.opensearchservice import VPCOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WindowStartTime(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-windowstarttime.html
    Properties:
        - Name: Hours
        - Name: Minutes
    
    """
    
    Hours_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-windowstarttime.html#cfn-opensearchservice-domain-windowstarttime-hours""", alias="Hours")
    Minutes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-windowstarttime.html#cfn-opensearchservice-domain-windowstarttime-minutes""", alias="Minutes")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.WindowStartTime:
        from troposphere.opensearchservice import WindowStartTime as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ZoneAwarenessConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-zoneawarenessconfig.html
    Properties:
        - Name: AvailabilityZoneCount
    
    """
    
    AvailabilityZoneCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-zoneawarenessconfig.html#cfn-opensearchservice-domain-zoneawarenessconfig-availabilityzonecount""", alias="AvailabilityZoneCount")
    


    @property
    def tropo_type(self) -> troposphere.opensearchservice.ZoneAwarenessConfig:
        from troposphere.opensearchservice import ZoneAwarenessConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Domain(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html
    Properties:
        - Name: EngineVersion
        - Name: SoftwareUpdateOptions
        - Name: DomainName
        - Name: LogPublishingOptions
        - Name: SnapshotOptions
        - Name: VPCOptions
        - Name: NodeToNodeEncryptionOptions
        - Name: AccessPolicies
        - Name: DomainEndpointOptions
        - Name: CognitoOptions
        - Name: AdvancedOptions
        - Name: AdvancedSecurityOptions
        - Name: EBSOptions
        - Name: EncryptionAtRestOptions
        - Name: OffPeakWindowOptions
        - Name: Tags
        - Name: ClusterConfig
    Attributes:
        - Name: ServiceSoftwareOptions.OptionalDeployment
        - Name: ServiceSoftwareOptions.Description
        - Name: ServiceSoftwareOptions.UpdateStatus
        - Name: ServiceSoftwareOptions.AutomatedUpdateDate
        - Name: ServiceSoftwareOptions.CurrentVersion
        - Name: DomainEndpoints
        - Name: DomainArn
        - Name: ServiceSoftwareOptions.UpdateAvailable
        - Name: DomainEndpoint
        - Name: ServiceSoftwareOptions
        - Name: AdvancedSecurityOptions.AnonymousAuthDisableDate
        - Name: ServiceSoftwareOptions.NewVersion
        - Name: Id
        - Name: Arn
        - Name: ServiceSoftwareOptions.Cancellable
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-engineversion""", alias="EngineVersion")
    SoftwareUpdateOptions_: Optional['SoftwareUpdateOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-softwareupdateoptions""", alias="SoftwareUpdateOptions")
    DomainName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-domainname""", alias="DomainName")
    LogPublishingOptions_: Optional[Dict[str, 'LogPublishingOption']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-logpublishingoptions""", alias="LogPublishingOptions")
    SnapshotOptions_: Optional['SnapshotOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-snapshotoptions""", alias="SnapshotOptions")
    VPCOptions_: Optional['VPCOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-vpcoptions""", alias="VPCOptions")
    NodeToNodeEncryptionOptions_: Optional['NodeToNodeEncryptionOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-nodetonodeencryptionoptions""", alias="NodeToNodeEncryptionOptions")
    AccessPolicies_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-accesspolicies""", alias="AccessPolicies")
    DomainEndpointOptions_: Optional['DomainEndpointOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-domainendpointoptions""", alias="DomainEndpointOptions")
    CognitoOptions_: Optional['CognitoOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-cognitooptions""", alias="CognitoOptions")
    AdvancedOptions_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-advancedoptions""", alias="AdvancedOptions")
    AdvancedSecurityOptions_: Optional['AdvancedSecurityOptionsInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-advancedsecurityoptions""", alias="AdvancedSecurityOptions")
    EBSOptions_: Optional['EBSOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-ebsoptions""", alias="EBSOptions")
    EncryptionAtRestOptions_: Optional['EncryptionAtRestOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-encryptionatrestoptions""", alias="EncryptionAtRestOptions")
    OffPeakWindowOptions_: Optional['OffPeakWindowOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-offpeakwindowoptions""", alias="OffPeakWindowOptions")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-tags""", alias="Tags")
    ClusterConfig_: Optional['ClusterConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-clusterconfig""", alias="ClusterConfig")
    

    @property
    def tropo_type(self) -> troposphere.opensearchservice.Domain:
        from troposphere.opensearchservice import Domain as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opensearchservice import Domain as TropoT
        return resource_to_troposphere(self, TropoT)

