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
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html
    Properties:
        - Name: AnonymousAuthEnabled
        - Name: Enabled
        - Name: InternalUserDatabaseEnabled
        - Name: MasterUserOptions
    
    """
    
    AnonymousAuthEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-anonymousauthenabled""", alias="AnonymousAuthEnabled")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-enabled""", alias="Enabled")
    InternalUserDatabaseEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-internaluserdatabaseenabled""", alias="InternalUserDatabaseEnabled")
    MasterUserOptions_: Optional['MasterUserOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-masteruseroptions""", alias="MasterUserOptions")
    


    @property
    def tropo_type(self) -> troposphere.elasticsearch.AdvancedSecurityOptionsInput:
        from troposphere.elasticsearch import AdvancedSecurityOptionsInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CognitoOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html
    Properties:
        - Name: Enabled
        - Name: IdentityPoolId
        - Name: RoleArn
        - Name: UserPoolId
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-enabled""", alias="Enabled")
    IdentityPoolId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-identitypoolid""", alias="IdentityPoolId")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-rolearn""", alias="RoleArn")
    UserPoolId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-userpoolid""", alias="UserPoolId")
    


    @property
    def tropo_type(self) -> troposphere.elasticsearch.CognitoOptions:
        from troposphere.elasticsearch import CognitoOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ColdStorageOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-coldstorageoptions.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-coldstorageoptions.html#cfn-elasticsearch-domain-coldstorageoptions-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.elasticsearch.ColdStorageOptions:
        from troposphere.elasticsearch import ColdStorageOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DomainEndpointOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html
    Properties:
        - Name: CustomEndpoint
        - Name: CustomEndpointCertificateArn
        - Name: CustomEndpointEnabled
        - Name: EnforceHTTPS
        - Name: TLSSecurityPolicy
    
    """
    
    CustomEndpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-customendpoint""", alias="CustomEndpoint")
    CustomEndpointCertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-customendpointcertificatearn""", alias="CustomEndpointCertificateArn")
    CustomEndpointEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-customendpointenabled""", alias="CustomEndpointEnabled")
    EnforceHTTPS_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-enforcehttps""", alias="EnforceHTTPS")
    TLSSecurityPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-tlssecuritypolicy""", alias="TLSSecurityPolicy")
    


    @property
    def tropo_type(self) -> troposphere.elasticsearch.DomainEndpointOptions:
        from troposphere.elasticsearch import DomainEndpointOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EBSOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html
    Properties:
        - Name: EBSEnabled
        - Name: Iops
        - Name: VolumeSize
        - Name: VolumeType
    
    """
    
    EBSEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-ebsenabled""", alias="EBSEnabled")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-iops""", alias="Iops")
    VolumeSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-volumesize""", alias="VolumeSize")
    VolumeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-volumetype""", alias="VolumeType")
    


    @property
    def tropo_type(self) -> troposphere.elasticsearch.EBSOptions:
        from troposphere.elasticsearch import EBSOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ElasticsearchClusterConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html
    Properties:
        - Name: ColdStorageOptions
        - Name: DedicatedMasterCount
        - Name: DedicatedMasterEnabled
        - Name: DedicatedMasterType
        - Name: InstanceCount
        - Name: InstanceType
        - Name: WarmCount
        - Name: WarmEnabled
        - Name: WarmType
        - Name: ZoneAwarenessConfig
        - Name: ZoneAwarenessEnabled
    
    """
    
    ColdStorageOptions_: Optional['ColdStorageOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-coldstorageoptions""", alias="ColdStorageOptions")
    DedicatedMasterCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmastercount""", alias="DedicatedMasterCount")
    DedicatedMasterEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmasterenabled""", alias="DedicatedMasterEnabled")
    DedicatedMasterType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmastertype""", alias="DedicatedMasterType")
    InstanceCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-instancecount""", alias="InstanceCount")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-instnacetype""", alias="InstanceType")
    WarmCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-warmcount""", alias="WarmCount")
    WarmEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-warmenabled""", alias="WarmEnabled")
    WarmType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-warmtype""", alias="WarmType")
    ZoneAwarenessConfig_: Optional['ZoneAwarenessConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-zoneawarenessconfig""", alias="ZoneAwarenessConfig")
    ZoneAwarenessEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-zoneawarenessenabled""", alias="ZoneAwarenessEnabled")
    


    @property
    def tropo_type(self) -> troposphere.elasticsearch.ElasticsearchClusterConfig:
        from troposphere.elasticsearch import ElasticsearchClusterConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionAtRestOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-encryptionatrestoptions.html
    Properties:
        - Name: Enabled
        - Name: KmsKeyId
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-encryptionatrestoptions.html#cfn-elasticsearch-domain-encryptionatrestoptions-enabled""", alias="Enabled")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-encryptionatrestoptions.html#cfn-elasticsearch-domain-encryptionatrestoptions-kmskeyid""", alias="KmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.elasticsearch.EncryptionAtRestOptions:
        from troposphere.elasticsearch import EncryptionAtRestOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogPublishingOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-logpublishingoption.html
    Properties:
        - Name: CloudWatchLogsLogGroupArn
        - Name: Enabled
    
    """
    
    CloudWatchLogsLogGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-logpublishingoption.html#cfn-elasticsearch-domain-logpublishingoption-cloudwatchlogsloggrouparn""", alias="CloudWatchLogsLogGroupArn")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-logpublishingoption.html#cfn-elasticsearch-domain-logpublishingoption-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.elasticsearch.LogPublishingOption:
        from troposphere.elasticsearch import LogPublishingOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MasterUserOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html
    Properties:
        - Name: MasterUserARN
        - Name: MasterUserName
        - Name: MasterUserPassword
    
    """
    
    MasterUserARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html#cfn-elasticsearch-domain-masteruseroptions-masteruserarn""", alias="MasterUserARN")
    MasterUserName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html#cfn-elasticsearch-domain-masteruseroptions-masterusername""", alias="MasterUserName")
    MasterUserPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html#cfn-elasticsearch-domain-masteruseroptions-masteruserpassword""", alias="MasterUserPassword")
    


    @property
    def tropo_type(self) -> troposphere.elasticsearch.MasterUserOptions:
        from troposphere.elasticsearch import MasterUserOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NodeToNodeEncryptionOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-nodetonodeencryptionoptions.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-nodetonodeencryptionoptions.html#cfn-elasticsearch-domain-nodetonodeencryptionoptions-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.elasticsearch.NodeToNodeEncryptionOptions:
        from troposphere.elasticsearch import NodeToNodeEncryptionOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnapshotOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-snapshotoptions.html
    Properties:
        - Name: AutomatedSnapshotStartHour
    
    """
    
    AutomatedSnapshotStartHour_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-snapshotoptions.html#cfn-elasticsearch-domain-snapshotoptions-automatedsnapshotstarthour""", alias="AutomatedSnapshotStartHour")
    


    @property
    def tropo_type(self) -> troposphere.elasticsearch.SnapshotOptions:
        from troposphere.elasticsearch import SnapshotOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VPCOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-vpcoptions.html
    Properties:
        - Name: SecurityGroupIds
        - Name: SubnetIds
    
    """
    
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-vpcoptions.html#cfn-elasticsearch-domain-vpcoptions-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-vpcoptions.html#cfn-elasticsearch-domain-vpcoptions-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.elasticsearch.VPCOptions:
        from troposphere.elasticsearch import VPCOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ZoneAwarenessConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-zoneawarenessconfig.html
    Properties:
        - Name: AvailabilityZoneCount
    
    """
    
    AvailabilityZoneCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-zoneawarenessconfig.html#cfn-elasticsearch-domain-zoneawarenessconfig-availabilityzonecount""", alias="AvailabilityZoneCount")
    


    @property
    def tropo_type(self) -> troposphere.elasticsearch.ZoneAwarenessConfig:
        from troposphere.elasticsearch import ZoneAwarenessConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Domain(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html
    Properties:
        - Name: AccessPolicies
        - Name: AdvancedOptions
        - Name: AdvancedSecurityOptions
        - Name: CognitoOptions
        - Name: DomainEndpointOptions
        - Name: DomainName
        - Name: EBSOptions
        - Name: ElasticsearchClusterConfig
        - Name: ElasticsearchVersion
        - Name: EncryptionAtRestOptions
        - Name: LogPublishingOptions
        - Name: NodeToNodeEncryptionOptions
        - Name: SnapshotOptions
        - Name: Tags
        - Name: VPCOptions
    Attributes:
        - Name: Arn
        - Name: DomainArn
        - Name: DomainEndpoint
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AccessPolicies_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-accesspolicies""", alias="AccessPolicies")
    AdvancedOptions_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-advancedoptions""", alias="AdvancedOptions")
    AdvancedSecurityOptions_: Optional['AdvancedSecurityOptionsInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-advancedsecurityoptions""", alias="AdvancedSecurityOptions")
    CognitoOptions_: Optional['CognitoOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-cognitooptions""", alias="CognitoOptions")
    DomainEndpointOptions_: Optional['DomainEndpointOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-domainendpointoptions""", alias="DomainEndpointOptions")
    DomainName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-domainname""", alias="DomainName")
    EBSOptions_: Optional['EBSOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-ebsoptions""", alias="EBSOptions")
    ElasticsearchClusterConfig_: Optional['ElasticsearchClusterConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-elasticsearchclusterconfig""", alias="ElasticsearchClusterConfig")
    ElasticsearchVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-elasticsearchversion""", alias="ElasticsearchVersion")
    EncryptionAtRestOptions_: Optional['EncryptionAtRestOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-encryptionatrestoptions""", alias="EncryptionAtRestOptions")
    LogPublishingOptions_: Optional[Dict[str, 'LogPublishingOption']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-logpublishingoptions""", alias="LogPublishingOptions")
    NodeToNodeEncryptionOptions_: Optional['NodeToNodeEncryptionOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-nodetonodeencryptionoptions""", alias="NodeToNodeEncryptionOptions")
    SnapshotOptions_: Optional['SnapshotOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-snapshotoptions""", alias="SnapshotOptions")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-tags""", alias="Tags")
    VPCOptions_: Optional['VPCOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-vpcoptions""", alias="VPCOptions")
    

    @property
    def tropo_type(self) -> troposphere.elasticsearch.Domain:
        from troposphere.elasticsearch import Domain as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticsearch import Domain as TropoT
        return resource_to_troposphere(self, TropoT)

