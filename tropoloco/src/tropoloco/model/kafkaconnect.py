from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ApacheKafkaCluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html
    Properties:
        - Name: Vpc
        - Name: BootstrapServers
    
    """
    
    Vpc_: 'Vpc' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html#cfn-kafkaconnect-connector-apachekafkacluster-vpc""", alias="Vpc")
    BootstrapServers_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html#cfn-kafkaconnect-connector-apachekafkacluster-bootstrapservers""", alias="BootstrapServers")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.ApacheKafkaCluster:
        from troposphere.kafkaconnect import ApacheKafkaCluster as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoScaling(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html
    Properties:
        - Name: ScaleOutPolicy
        - Name: ScaleInPolicy
        - Name: MaxWorkerCount
        - Name: MinWorkerCount
        - Name: McuCount
    
    """
    
    ScaleOutPolicy_: 'ScaleOutPolicy' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-scaleoutpolicy""", alias="ScaleOutPolicy")
    ScaleInPolicy_: 'ScaleInPolicy' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-scaleinpolicy""", alias="ScaleInPolicy")
    MaxWorkerCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-maxworkercount""", alias="MaxWorkerCount")
    MinWorkerCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-minworkercount""", alias="MinWorkerCount")
    McuCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-mcucount""", alias="McuCount")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.AutoScaling:
        from troposphere.kafkaconnect import AutoScaling as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Capacity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html
    Properties:
        - Name: ProvisionedCapacity
        - Name: AutoScaling
    
    """
    
    ProvisionedCapacity_: Optional['ProvisionedCapacity'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html#cfn-kafkaconnect-connector-capacity-provisionedcapacity""", alias="ProvisionedCapacity")
    AutoScaling_: Optional['AutoScaling'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html#cfn-kafkaconnect-connector-capacity-autoscaling""", alias="AutoScaling")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.Capacity:
        from troposphere.kafkaconnect import Capacity as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchLogsLogDelivery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html
    Properties:
        - Name: LogGroup
        - Name: Enabled
    
    """
    
    LogGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html#cfn-kafkaconnect-connector-cloudwatchlogslogdelivery-loggroup""", alias="LogGroup")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html#cfn-kafkaconnect-connector-cloudwatchlogslogdelivery-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.CloudWatchLogsLogDelivery:
        from troposphere.kafkaconnect import CloudWatchLogsLogDelivery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomPlugin(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html
    Properties:
        - Name: CustomPluginArn
        - Name: Revision
    
    """
    
    CustomPluginArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html#cfn-kafkaconnect-connector-customplugin-custompluginarn""", alias="CustomPluginArn")
    Revision_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html#cfn-kafkaconnect-connector-customplugin-revision""", alias="Revision")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.CustomPlugin:
        from troposphere.kafkaconnect import CustomPlugin as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FirehoseLogDelivery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html
    Properties:
        - Name: DeliveryStream
        - Name: Enabled
    
    """
    
    DeliveryStream_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html#cfn-kafkaconnect-connector-firehoselogdelivery-deliverystream""", alias="DeliveryStream")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html#cfn-kafkaconnect-connector-firehoselogdelivery-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.FirehoseLogDelivery:
        from troposphere.kafkaconnect import FirehoseLogDelivery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KafkaCluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkacluster.html
    Properties:
        - Name: ApacheKafkaCluster
    
    """
    
    ApacheKafkaCluster_: 'ApacheKafkaCluster' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkacluster.html#cfn-kafkaconnect-connector-kafkacluster-apachekafkacluster""", alias="ApacheKafkaCluster")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.KafkaCluster:
        from troposphere.kafkaconnect import KafkaCluster as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KafkaClusterClientAuthentication(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication.html
    Properties:
        - Name: AuthenticationType
    
    """
    
    AuthenticationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication.html#cfn-kafkaconnect-connector-kafkaclusterclientauthentication-authenticationtype""", alias="AuthenticationType")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.KafkaClusterClientAuthentication:
        from troposphere.kafkaconnect import KafkaClusterClientAuthentication as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KafkaClusterEncryptionInTransit(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit.html
    Properties:
        - Name: EncryptionType
    
    """
    
    EncryptionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit.html#cfn-kafkaconnect-connector-kafkaclusterencryptionintransit-encryptiontype""", alias="EncryptionType")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.KafkaClusterEncryptionInTransit:
        from troposphere.kafkaconnect import KafkaClusterEncryptionInTransit as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogDelivery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-logdelivery.html
    Properties:
        - Name: WorkerLogDelivery
    
    """
    
    WorkerLogDelivery_: 'WorkerLogDelivery' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-logdelivery.html#cfn-kafkaconnect-connector-logdelivery-workerlogdelivery""", alias="WorkerLogDelivery")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.LogDelivery:
        from troposphere.kafkaconnect import LogDelivery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Plugin(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-plugin.html
    Properties:
        - Name: CustomPlugin
    
    """
    
    CustomPlugin_: 'CustomPlugin' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-plugin.html#cfn-kafkaconnect-connector-plugin-customplugin""", alias="CustomPlugin")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.Plugin:
        from troposphere.kafkaconnect import Plugin as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProvisionedCapacity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html
    Properties:
        - Name: WorkerCount
        - Name: McuCount
    
    """
    
    WorkerCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html#cfn-kafkaconnect-connector-provisionedcapacity-workercount""", alias="WorkerCount")
    McuCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html#cfn-kafkaconnect-connector-provisionedcapacity-mcucount""", alias="McuCount")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.ProvisionedCapacity:
        from troposphere.kafkaconnect import ProvisionedCapacity as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3LogDelivery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html
    Properties:
        - Name: Bucket
        - Name: Enabled
        - Name: Prefix
    
    """
    
    Bucket_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-bucket""", alias="Bucket")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-enabled""", alias="Enabled")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.S3LogDelivery:
        from troposphere.kafkaconnect import S3LogDelivery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScaleInPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleinpolicy.html
    Properties:
        - Name: CpuUtilizationPercentage
    
    """
    
    CpuUtilizationPercentage_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleinpolicy.html#cfn-kafkaconnect-connector-scaleinpolicy-cpuutilizationpercentage""", alias="CpuUtilizationPercentage")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.ScaleInPolicy:
        from troposphere.kafkaconnect import ScaleInPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScaleOutPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleoutpolicy.html
    Properties:
        - Name: CpuUtilizationPercentage
    
    """
    
    CpuUtilizationPercentage_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleoutpolicy.html#cfn-kafkaconnect-connector-scaleoutpolicy-cpuutilizationpercentage""", alias="CpuUtilizationPercentage")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.ScaleOutPolicy:
        from troposphere.kafkaconnect import ScaleOutPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Vpc(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html
    Properties:
        - Name: SecurityGroups
        - Name: Subnets
    
    """
    
    SecurityGroups_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html#cfn-kafkaconnect-connector-vpc-securitygroups""", alias="SecurityGroups")
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html#cfn-kafkaconnect-connector-vpc-subnets""", alias="Subnets")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.Vpc:
        from troposphere.kafkaconnect import Vpc as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WorkerConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html
    Properties:
        - Name: Revision
        - Name: WorkerConfigurationArn
    
    """
    
    Revision_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html#cfn-kafkaconnect-connector-workerconfiguration-revision""", alias="Revision")
    WorkerConfigurationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html#cfn-kafkaconnect-connector-workerconfiguration-workerconfigurationarn""", alias="WorkerConfigurationArn")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.WorkerConfiguration:
        from troposphere.kafkaconnect import WorkerConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WorkerLogDelivery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html
    Properties:
        - Name: S3
        - Name: Firehose
        - Name: CloudWatchLogs
    
    """
    
    S3_: Optional['S3LogDelivery'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-s3""", alias="S3")
    Firehose_: Optional['FirehoseLogDelivery'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-firehose""", alias="Firehose")
    CloudWatchLogs_: Optional['CloudWatchLogsLogDelivery'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-cloudwatchlogs""", alias="CloudWatchLogs")
    


    @property
    def tropo_type(self) -> troposphere.kafkaconnect.WorkerLogDelivery:
        from troposphere.kafkaconnect import WorkerLogDelivery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Connector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html
    Properties:
        - Name: KafkaCluster
        - Name: KafkaConnectVersion
        - Name: WorkerConfiguration
        - Name: Capacity
        - Name: KafkaClusterEncryptionInTransit
        - Name: ConnectorDescription
        - Name: KafkaClusterClientAuthentication
        - Name: ConnectorName
        - Name: ServiceExecutionRoleArn
        - Name: ConnectorConfiguration
        - Name: LogDelivery
        - Name: Plugins
    Attributes:
        - Name: ConnectorArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KafkaCluster_: 'KafkaCluster' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkacluster""", alias="KafkaCluster")
    KafkaConnectVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaconnectversion""", alias="KafkaConnectVersion")
    WorkerConfiguration_: Optional['WorkerConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-workerconfiguration""", alias="WorkerConfiguration")
    Capacity_: 'Capacity' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-capacity""", alias="Capacity")
    KafkaClusterEncryptionInTransit_: 'KafkaClusterEncryptionInTransit' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaclusterencryptionintransit""", alias="KafkaClusterEncryptionInTransit")
    ConnectorDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectordescription""", alias="ConnectorDescription")
    KafkaClusterClientAuthentication_: 'KafkaClusterClientAuthentication' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaclusterclientauthentication""", alias="KafkaClusterClientAuthentication")
    ConnectorName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectorname""", alias="ConnectorName")
    ServiceExecutionRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-serviceexecutionrolearn""", alias="ServiceExecutionRoleArn")
    ConnectorConfiguration_: Dict[str, str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectorconfiguration""", alias="ConnectorConfiguration")
    LogDelivery_: Optional['LogDelivery'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-logdelivery""", alias="LogDelivery")
    Plugins_: List['Plugin'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-plugins""", alias="Plugins")
    

    @property
    def tropo_type(self) -> troposphere.kafkaconnect.Connector:
        from troposphere.kafkaconnect import Connector as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kafkaconnect import Connector as TropoT
        return resource_to_troposphere(self, TropoT)

