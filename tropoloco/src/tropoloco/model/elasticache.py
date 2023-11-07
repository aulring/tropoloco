from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CloudWatchLogsDestinationDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-cloudwatchlogsdestinationdetails.html
    Properties:
        - Name: LogGroup
    
    """
    
    LogGroup_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-cloudwatchlogsdestinationdetails.html#cfn-elasticache-cachecluster-cloudwatchlogsdestinationdetails-loggroup""", alias="LogGroup")
    


    @property
    def tropo_type(self) -> troposphere.elasticache.CloudWatchLogsDestinationDetails:
        from troposphere.elasticache import CloudWatchLogsDestinationDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DestinationDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-destinationdetails.html
    Properties:
        - Name: CloudWatchLogsDetails
        - Name: KinesisFirehoseDetails
    
    """
    
    CloudWatchLogsDetails_: Optional['CloudWatchLogsDestinationDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-destinationdetails.html#cfn-elasticache-cachecluster-destinationdetails-cloudwatchlogsdetails""", alias="CloudWatchLogsDetails")
    KinesisFirehoseDetails_: Optional['KinesisFirehoseDestinationDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-destinationdetails.html#cfn-elasticache-cachecluster-destinationdetails-kinesisfirehosedetails""", alias="KinesisFirehoseDetails")
    


    @property
    def tropo_type(self) -> troposphere.elasticache.DestinationDetails:
        from troposphere.elasticache import DestinationDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisFirehoseDestinationDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-kinesisfirehosedestinationdetails.html
    Properties:
        - Name: DeliveryStream
    
    """
    
    DeliveryStream_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-kinesisfirehosedestinationdetails.html#cfn-elasticache-cachecluster-kinesisfirehosedestinationdetails-deliverystream""", alias="DeliveryStream")
    


    @property
    def tropo_type(self) -> troposphere.elasticache.KinesisFirehoseDestinationDetails:
        from troposphere.elasticache import KinesisFirehoseDestinationDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogDeliveryConfigurationRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html
    Properties:
        - Name: DestinationDetails
        - Name: DestinationType
        - Name: LogFormat
        - Name: LogType
    
    """
    
    DestinationDetails_: 'DestinationDetails' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html#cfn-elasticache-cachecluster-logdeliveryconfigurationrequest-destinationdetails""", alias="DestinationDetails")
    DestinationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html#cfn-elasticache-cachecluster-logdeliveryconfigurationrequest-destinationtype""", alias="DestinationType")
    LogFormat_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html#cfn-elasticache-cachecluster-logdeliveryconfigurationrequest-logformat""", alias="LogFormat")
    LogType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html#cfn-elasticache-cachecluster-logdeliveryconfigurationrequest-logtype""", alias="LogType")
    


    @property
    def tropo_type(self) -> troposphere.elasticache.LogDeliveryConfigurationRequest:
        from troposphere.elasticache import LogDeliveryConfigurationRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GlobalReplicationGroupMember(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html
    Properties:
        - Name: Role
        - Name: ReplicationGroupRegion
        - Name: ReplicationGroupId
    
    """
    
    Role_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupmember-role""", alias="Role")
    ReplicationGroupRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupmember-replicationgroupregion""", alias="ReplicationGroupRegion")
    ReplicationGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupmember-replicationgroupid""", alias="ReplicationGroupId")
    


    @property
    def tropo_type(self) -> troposphere.elasticache.GlobalReplicationGroupMember:
        from troposphere.elasticache import GlobalReplicationGroupMember as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RegionalConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html
    Properties:
        - Name: ReplicationGroupRegion
        - Name: ReplicationGroupId
        - Name: ReshardingConfigurations
    
    """
    
    ReplicationGroupRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html#cfn-elasticache-globalreplicationgroup-regionalconfiguration-replicationgroupregion""", alias="ReplicationGroupRegion")
    ReplicationGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html#cfn-elasticache-globalreplicationgroup-regionalconfiguration-replicationgroupid""", alias="ReplicationGroupId")
    ReshardingConfigurations_: Optional[List['ReshardingConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html#cfn-elasticache-globalreplicationgroup-regionalconfiguration-reshardingconfigurations""", alias="ReshardingConfigurations")
    


    @property
    def tropo_type(self) -> troposphere.elasticache.RegionalConfiguration:
        from troposphere.elasticache import RegionalConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReshardingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration.html
    Properties:
        - Name: NodeGroupId
        - Name: PreferredAvailabilityZones
    
    """
    
    NodeGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration.html#cfn-elasticache-globalreplicationgroup-reshardingconfiguration-nodegroupid""", alias="NodeGroupId")
    PreferredAvailabilityZones_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration.html#cfn-elasticache-globalreplicationgroup-reshardingconfiguration-preferredavailabilityzones""", alias="PreferredAvailabilityZones")
    


    @property
    def tropo_type(self) -> troposphere.elasticache.ReshardingConfiguration:
        from troposphere.elasticache import ReshardingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchLogsDestinationDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-cloudwatchlogsdestinationdetails.html
    Properties:
        - Name: LogGroup
    
    """
    
    LogGroup_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-cloudwatchlogsdestinationdetails.html#cfn-elasticache-replicationgroup-cloudwatchlogsdestinationdetails-loggroup""", alias="LogGroup")
    


    @property
    def tropo_type(self) -> troposphere.elasticache.CloudWatchLogsDestinationDetails:
        from troposphere.elasticache import CloudWatchLogsDestinationDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DestinationDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-destinationdetails.html
    Properties:
        - Name: CloudWatchLogsDetails
        - Name: KinesisFirehoseDetails
    
    """
    
    CloudWatchLogsDetails_: Optional['CloudWatchLogsDestinationDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-destinationdetails.html#cfn-elasticache-replicationgroup-destinationdetails-cloudwatchlogsdetails""", alias="CloudWatchLogsDetails")
    KinesisFirehoseDetails_: Optional['KinesisFirehoseDestinationDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-destinationdetails.html#cfn-elasticache-replicationgroup-destinationdetails-kinesisfirehosedetails""", alias="KinesisFirehoseDetails")
    


    @property
    def tropo_type(self) -> troposphere.elasticache.DestinationDetails:
        from troposphere.elasticache import DestinationDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisFirehoseDestinationDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-kinesisfirehosedestinationdetails.html
    Properties:
        - Name: DeliveryStream
    
    """
    
    DeliveryStream_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-kinesisfirehosedestinationdetails.html#cfn-elasticache-replicationgroup-kinesisfirehosedestinationdetails-deliverystream""", alias="DeliveryStream")
    


    @property
    def tropo_type(self) -> troposphere.elasticache.KinesisFirehoseDestinationDetails:
        from troposphere.elasticache import KinesisFirehoseDestinationDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogDeliveryConfigurationRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html
    Properties:
        - Name: DestinationDetails
        - Name: DestinationType
        - Name: LogFormat
        - Name: LogType
    
    """
    
    DestinationDetails_: 'DestinationDetails' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-destinationdetails""", alias="DestinationDetails")
    DestinationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-destinationtype""", alias="DestinationType")
    LogFormat_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-logformat""", alias="LogFormat")
    LogType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-logtype""", alias="LogType")
    


    @property
    def tropo_type(self) -> troposphere.elasticache.LogDeliveryConfigurationRequest:
        from troposphere.elasticache import LogDeliveryConfigurationRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NodeGroupConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html
    Properties:
        - Name: NodeGroupId
        - Name: PrimaryAvailabilityZone
        - Name: ReplicaAvailabilityZones
        - Name: ReplicaCount
        - Name: Slots
    
    """
    
    NodeGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-nodegroupid""", alias="NodeGroupId")
    PrimaryAvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-primaryavailabilityzone""", alias="PrimaryAvailabilityZone")
    ReplicaAvailabilityZones_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-replicaavailabilityzones""", alias="ReplicaAvailabilityZones")
    ReplicaCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-replicacount""", alias="ReplicaCount")
    Slots_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-slots""", alias="Slots")
    


    @property
    def tropo_type(self) -> troposphere.elasticache.NodeGroupConfiguration:
        from troposphere.elasticache import NodeGroupConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuthenticationMode(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-user-authenticationmode.html
    Properties:
        - Name: Type
        - Name: Passwords
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-user-authenticationmode.html#cfn-elasticache-user-authenticationmode-type""", alias="Type")
    Passwords_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-user-authenticationmode.html#cfn-elasticache-user-authenticationmode-passwords""", alias="Passwords")
    


    @property
    def tropo_type(self) -> troposphere.elasticache.AuthenticationMode:
        from troposphere.elasticache import AuthenticationMode as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class CacheCluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html
    Properties:
        - Name: AZMode
        - Name: AutoMinorVersionUpgrade
        - Name: CacheNodeType
        - Name: CacheParameterGroupName
        - Name: CacheSecurityGroupNames
        - Name: CacheSubnetGroupName
        - Name: ClusterName
        - Name: Engine
        - Name: EngineVersion
        - Name: IpDiscovery
        - Name: LogDeliveryConfigurations
        - Name: NetworkType
        - Name: NotificationTopicArn
        - Name: NumCacheNodes
        - Name: Port
        - Name: PreferredAvailabilityZone
        - Name: PreferredAvailabilityZones
        - Name: PreferredMaintenanceWindow
        - Name: SnapshotArns
        - Name: SnapshotName
        - Name: SnapshotRetentionLimit
        - Name: SnapshotWindow
        - Name: Tags
        - Name: TransitEncryptionEnabled
        - Name: VpcSecurityGroupIds
    Attributes:
        - Name: ConfigurationEndpoint.Address
        - Name: ConfigurationEndpoint.Port
        - Name: RedisEndpoint.Address
        - Name: RedisEndpoint.Port
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AZMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-azmode""", alias="AZMode")
    AutoMinorVersionUpgrade_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-autominorversionupgrade""", alias="AutoMinorVersionUpgrade")
    CacheNodeType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-cachenodetype""", alias="CacheNodeType")
    CacheParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-cacheparametergroupname""", alias="CacheParameterGroupName")
    CacheSecurityGroupNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-cachesecuritygroupnames""", alias="CacheSecurityGroupNames")
    CacheSubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-cachesubnetgroupname""", alias="CacheSubnetGroupName")
    ClusterName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-clustername""", alias="ClusterName")
    Engine_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-engine""", alias="Engine")
    EngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-engineversion""", alias="EngineVersion")
    IpDiscovery_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-ipdiscovery""", alias="IpDiscovery")
    LogDeliveryConfigurations_: Optional[List['LogDeliveryConfigurationRequest']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-logdeliveryconfigurations""", alias="LogDeliveryConfigurations")
    NetworkType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-networktype""", alias="NetworkType")
    NotificationTopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-notificationtopicarn""", alias="NotificationTopicArn")
    NumCacheNodes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-numcachenodes""", alias="NumCacheNodes")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-port""", alias="Port")
    PreferredAvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-preferredavailabilityzone""", alias="PreferredAvailabilityZone")
    PreferredAvailabilityZones_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-preferredavailabilityzones""", alias="PreferredAvailabilityZones")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    SnapshotArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-snapshotarns""", alias="SnapshotArns")
    SnapshotName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-snapshotname""", alias="SnapshotName")
    SnapshotRetentionLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-snapshotretentionlimit""", alias="SnapshotRetentionLimit")
    SnapshotWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-snapshotwindow""", alias="SnapshotWindow")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-tags""", alias="Tags")
    TransitEncryptionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-transitencryptionenabled""", alias="TransitEncryptionEnabled")
    VpcSecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-vpcsecuritygroupids""", alias="VpcSecurityGroupIds")
    

    @property
    def tropo_type(self) -> troposphere.elasticache.CacheCluster:
        from troposphere.elasticache import CacheCluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticache import CacheCluster as TropoT
        return resource_to_troposphere(self, TropoT)


class GlobalReplicationGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html
    Properties:
        - Name: GlobalReplicationGroupIdSuffix
        - Name: CacheNodeType
        - Name: EngineVersion
        - Name: GlobalReplicationGroupDescription
        - Name: RegionalConfigurations
        - Name: CacheParameterGroupName
        - Name: Members
        - Name: AutomaticFailoverEnabled
        - Name: GlobalNodeGroupCount
    Attributes:
        - Name: Status
        - Name: GlobalReplicationGroupId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GlobalReplicationGroupIdSuffix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupidsuffix""", alias="GlobalReplicationGroupIdSuffix")
    CacheNodeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-cachenodetype""", alias="CacheNodeType")
    EngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-engineversion""", alias="EngineVersion")
    GlobalReplicationGroupDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupdescription""", alias="GlobalReplicationGroupDescription")
    RegionalConfigurations_: Optional[List['RegionalConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-regionalconfigurations""", alias="RegionalConfigurations")
    CacheParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-cacheparametergroupname""", alias="CacheParameterGroupName")
    Members_: List['GlobalReplicationGroupMember'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-members""", alias="Members")
    AutomaticFailoverEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-automaticfailoverenabled""", alias="AutomaticFailoverEnabled")
    GlobalNodeGroupCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-globalnodegroupcount""", alias="GlobalNodeGroupCount")
    

    @property
    def tropo_type(self) -> troposphere.elasticache.GlobalReplicationGroup:
        from troposphere.elasticache import GlobalReplicationGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticache import GlobalReplicationGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class ParameterGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html
    Properties:
        - Name: CacheParameterGroupFamily
        - Name: Description
        - Name: Properties
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CacheParameterGroupFamily_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html#cfn-elasticache-parametergroup-cacheparametergroupfamily""", alias="CacheParameterGroupFamily")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html#cfn-elasticache-parametergroup-description""", alias="Description")
    Properties_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html#cfn-elasticache-parametergroup-properties""", alias="Properties")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html#cfn-elasticache-parametergroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.elasticache.ParameterGroup:
        from troposphere.elasticache import ParameterGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticache import ParameterGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class ReplicationGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html
    Properties:
        - Name: AtRestEncryptionEnabled
        - Name: AuthToken
        - Name: AutoMinorVersionUpgrade
        - Name: AutomaticFailoverEnabled
        - Name: CacheNodeType
        - Name: CacheParameterGroupName
        - Name: CacheSecurityGroupNames
        - Name: CacheSubnetGroupName
        - Name: ClusterMode
        - Name: DataTieringEnabled
        - Name: Engine
        - Name: EngineVersion
        - Name: GlobalReplicationGroupId
        - Name: IpDiscovery
        - Name: KmsKeyId
        - Name: LogDeliveryConfigurations
        - Name: MultiAZEnabled
        - Name: NetworkType
        - Name: NodeGroupConfiguration
        - Name: NotificationTopicArn
        - Name: NumCacheClusters
        - Name: NumNodeGroups
        - Name: Port
        - Name: PreferredCacheClusterAZs
        - Name: PreferredMaintenanceWindow
        - Name: PrimaryClusterId
        - Name: ReplicasPerNodeGroup
        - Name: ReplicationGroupDescription
        - Name: ReplicationGroupId
        - Name: SecurityGroupIds
        - Name: SnapshotArns
        - Name: SnapshotName
        - Name: SnapshotRetentionLimit
        - Name: SnapshotWindow
        - Name: SnapshottingClusterId
        - Name: Tags
        - Name: TransitEncryptionEnabled
        - Name: TransitEncryptionMode
        - Name: UserGroupIds
    Attributes:
        - Name: ConfigurationEndPoint.Address
        - Name: ConfigurationEndPoint.Port
        - Name: PrimaryEndPoint.Address
        - Name: PrimaryEndPoint.Port
        - Name: ReadEndPoint.Addresses
        - Name: ReadEndPoint.Addresses.List
        - Name: ReadEndPoint.Ports
        - Name: ReadEndPoint.Ports.List
        - Name: ReaderEndPoint.Address
        - Name: ReaderEndPoint.Port
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AtRestEncryptionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-atrestencryptionenabled""", alias="AtRestEncryptionEnabled")
    AuthToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-authtoken""", alias="AuthToken")
    AutoMinorVersionUpgrade_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-autominorversionupgrade""", alias="AutoMinorVersionUpgrade")
    AutomaticFailoverEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-automaticfailoverenabled""", alias="AutomaticFailoverEnabled")
    CacheNodeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cachenodetype""", alias="CacheNodeType")
    CacheParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cacheparametergroupname""", alias="CacheParameterGroupName")
    CacheSecurityGroupNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cachesecuritygroupnames""", alias="CacheSecurityGroupNames")
    CacheSubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cachesubnetgroupname""", alias="CacheSubnetGroupName")
    ClusterMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-clustermode""", alias="ClusterMode")
    DataTieringEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-datatieringenabled""", alias="DataTieringEnabled")
    Engine_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-engine""", alias="Engine")
    EngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-engineversion""", alias="EngineVersion")
    GlobalReplicationGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-globalreplicationgroupid""", alias="GlobalReplicationGroupId")
    IpDiscovery_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-ipdiscovery""", alias="IpDiscovery")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-kmskeyid""", alias="KmsKeyId")
    LogDeliveryConfigurations_: Optional[List['LogDeliveryConfigurationRequest']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-logdeliveryconfigurations""", alias="LogDeliveryConfigurations")
    MultiAZEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-multiazenabled""", alias="MultiAZEnabled")
    NetworkType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-networktype""", alias="NetworkType")
    NodeGroupConfiguration_: Optional[List['NodeGroupConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-nodegroupconfiguration""", alias="NodeGroupConfiguration")
    NotificationTopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-notificationtopicarn""", alias="NotificationTopicArn")
    NumCacheClusters_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-numcacheclusters""", alias="NumCacheClusters")
    NumNodeGroups_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-numnodegroups""", alias="NumNodeGroups")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-port""", alias="Port")
    PreferredCacheClusterAZs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-preferredcacheclusterazs""", alias="PreferredCacheClusterAZs")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    PrimaryClusterId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-primaryclusterid""", alias="PrimaryClusterId")
    ReplicasPerNodeGroup_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-replicaspernodegroup""", alias="ReplicasPerNodeGroup")
    ReplicationGroupDescription_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-replicationgroupdescription""", alias="ReplicationGroupDescription")
    ReplicationGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-replicationgroupid""", alias="ReplicationGroupId")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-securitygroupids""", alias="SecurityGroupIds")
    SnapshotArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotarns""", alias="SnapshotArns")
    SnapshotName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotname""", alias="SnapshotName")
    SnapshotRetentionLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotretentionlimit""", alias="SnapshotRetentionLimit")
    SnapshotWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotwindow""", alias="SnapshotWindow")
    SnapshottingClusterId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshottingclusterid""", alias="SnapshottingClusterId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-tags""", alias="Tags")
    TransitEncryptionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-transitencryptionenabled""", alias="TransitEncryptionEnabled")
    TransitEncryptionMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-transitencryptionmode""", alias="TransitEncryptionMode")
    UserGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-usergroupids""", alias="UserGroupIds")
    

    @property
    def tropo_type(self) -> troposphere.elasticache.ReplicationGroup:
        from troposphere.elasticache import ReplicationGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticache import ReplicationGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class SecurityGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group.html
    Properties:
        - Name: Description
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group.html#cfn-elasticache-securitygroup-description""", alias="Description")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group.html#cfn-elasticache-securitygroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.elasticache.SecurityGroup:
        from troposphere.elasticache import SecurityGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticache import SecurityGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class SecurityGroupIngress(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html
    Properties:
        - Name: CacheSecurityGroupName
        - Name: EC2SecurityGroupName
        - Name: EC2SecurityGroupOwnerId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CacheSecurityGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html#cfn-elasticache-securitygroupingress-cachesecuritygroupname""", alias="CacheSecurityGroupName")
    EC2SecurityGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html#cfn-elasticache-securitygroupingress-ec2securitygroupname""", alias="EC2SecurityGroupName")
    EC2SecurityGroupOwnerId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html#cfn-elasticache-securitygroupingress-ec2securitygroupownerid""", alias="EC2SecurityGroupOwnerId")
    

    @property
    def tropo_type(self) -> troposphere.elasticache.SecurityGroupIngress:
        from troposphere.elasticache import SecurityGroupIngress as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticache import SecurityGroupIngress as TropoT
        return resource_to_troposphere(self, TropoT)


class SubnetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-subnetgroup.html
    Properties:
        - Name: Description
        - Name: CacheSubnetGroupName
        - Name: SubnetIds
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-description""", alias="Description")
    CacheSubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-cachesubnetgroupname""", alias="CacheSubnetGroupName")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-subnetids""", alias="SubnetIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.elasticache.SubnetGroup:
        from troposphere.elasticache import SubnetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticache import SubnetGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class User(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html
    Properties:
        - Name: AuthenticationMode
        - Name: UserName
        - Name: NoPasswordRequired
        - Name: AccessString
        - Name: UserId
        - Name: Passwords
        - Name: Engine
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AuthenticationMode_: Optional['AuthenticationMode'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-authenticationmode""", alias="AuthenticationMode")
    UserName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-username""", alias="UserName")
    NoPasswordRequired_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-nopasswordrequired""", alias="NoPasswordRequired")
    AccessString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-accessstring""", alias="AccessString")
    UserId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-userid""", alias="UserId")
    Passwords_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-passwords""", alias="Passwords")
    Engine_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-engine""", alias="Engine")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.elasticache.User:
        from troposphere.elasticache import User as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticache import User as TropoT
        return resource_to_troposphere(self, TropoT)


class UserGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html
    Properties:
        - Name: UserGroupId
        - Name: Engine
        - Name: UserIds
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UserGroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-usergroupid""", alias="UserGroupId")
    Engine_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-engine""", alias="Engine")
    UserIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-userids""", alias="UserIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.elasticache.UserGroup:
        from troposphere.elasticache import UserGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticache import UserGroup as TropoT
        return resource_to_troposphere(self, TropoT)

