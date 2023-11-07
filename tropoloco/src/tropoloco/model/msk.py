from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class BrokerLogs(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html
    Properties:
        - Name: S3
        - Name: Firehose
        - Name: CloudWatchLogs
    
    """
    
    S3_: Optional['S3'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-s3""", alias="S3")
    Firehose_: Optional['Firehose'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-firehose""", alias="Firehose")
    CloudWatchLogs_: Optional['CloudWatchLogs'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-cloudwatchlogs""", alias="CloudWatchLogs")
    


    @property
    def tropo_type(self) -> troposphere.msk.BrokerLogs:
        from troposphere.msk import BrokerLogs as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BrokerNodeGroupInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html
    Properties:
        - Name: SecurityGroups
        - Name: ClientSubnets
        - Name: ConnectivityInfo
        - Name: StorageInfo
        - Name: BrokerAZDistribution
        - Name: InstanceType
    
    """
    
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-securitygroups""", alias="SecurityGroups")
    ClientSubnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-clientsubnets""", alias="ClientSubnets")
    ConnectivityInfo_: Optional['ConnectivityInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-connectivityinfo""", alias="ConnectivityInfo")
    StorageInfo_: Optional['StorageInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-storageinfo""", alias="StorageInfo")
    BrokerAZDistribution_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-brokerazdistribution""", alias="BrokerAZDistribution")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-instancetype""", alias="InstanceType")
    


    @property
    def tropo_type(self) -> troposphere.msk.BrokerNodeGroupInfo:
        from troposphere.msk import BrokerNodeGroupInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClientAuthentication(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html
    Properties:
        - Name: Sasl
        - Name: Unauthenticated
        - Name: Tls
    
    """
    
    Sasl_: Optional['Sasl'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-sasl""", alias="Sasl")
    Unauthenticated_: Optional['Unauthenticated'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-unauthenticated""", alias="Unauthenticated")
    Tls_: Optional['Tls'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-tls""", alias="Tls")
    


    @property
    def tropo_type(self) -> troposphere.msk.ClientAuthentication:
        from troposphere.msk import ClientAuthentication as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchLogs(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html
    Properties:
        - Name: LogGroup
        - Name: Enabled
    
    """
    
    LogGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html#cfn-msk-cluster-cloudwatchlogs-loggroup""", alias="LogGroup")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html#cfn-msk-cluster-cloudwatchlogs-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.msk.CloudWatchLogs:
        from troposphere.msk import CloudWatchLogs as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfigurationInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html
    Properties:
        - Name: Revision
        - Name: Arn
    
    """
    
    Revision_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html#cfn-msk-cluster-configurationinfo-revision""", alias="Revision")
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html#cfn-msk-cluster-configurationinfo-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.msk.ConfigurationInfo:
        from troposphere.msk import ConfigurationInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectivityInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-connectivityinfo.html
    Properties:
        - Name: VpcConnectivity
        - Name: PublicAccess
    
    """
    
    VpcConnectivity_: Optional['VpcConnectivity'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-connectivityinfo.html#cfn-msk-cluster-connectivityinfo-vpcconnectivity""", alias="VpcConnectivity")
    PublicAccess_: Optional['PublicAccess'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-connectivityinfo.html#cfn-msk-cluster-connectivityinfo-publicaccess""", alias="PublicAccess")
    


    @property
    def tropo_type(self) -> troposphere.msk.ConnectivityInfo:
        from troposphere.msk import ConnectivityInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EBSStorageInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html
    Properties:
        - Name: ProvisionedThroughput
        - Name: VolumeSize
    
    """
    
    ProvisionedThroughput_: Optional['ProvisionedThroughput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html#cfn-msk-cluster-ebsstorageinfo-provisionedthroughput""", alias="ProvisionedThroughput")
    VolumeSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html#cfn-msk-cluster-ebsstorageinfo-volumesize""", alias="VolumeSize")
    


    @property
    def tropo_type(self) -> troposphere.msk.EBSStorageInfo:
        from troposphere.msk import EBSStorageInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionAtRest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html
    Properties:
        - Name: DataVolumeKMSKeyId
    
    """
    
    DataVolumeKMSKeyId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html#cfn-msk-cluster-encryptionatrest-datavolumekmskeyid""", alias="DataVolumeKMSKeyId")
    


    @property
    def tropo_type(self) -> troposphere.msk.EncryptionAtRest:
        from troposphere.msk import EncryptionAtRest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionInTransit(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html
    Properties:
        - Name: ClientBroker
        - Name: InCluster
    
    """
    
    ClientBroker_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html#cfn-msk-cluster-encryptionintransit-clientbroker""", alias="ClientBroker")
    InCluster_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html#cfn-msk-cluster-encryptionintransit-incluster""", alias="InCluster")
    


    @property
    def tropo_type(self) -> troposphere.msk.EncryptionInTransit:
        from troposphere.msk import EncryptionInTransit as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html
    Properties:
        - Name: EncryptionAtRest
        - Name: EncryptionInTransit
    
    """
    
    EncryptionAtRest_: Optional['EncryptionAtRest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionatrest""", alias="EncryptionAtRest")
    EncryptionInTransit_: Optional['EncryptionInTransit'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionintransit""", alias="EncryptionInTransit")
    


    @property
    def tropo_type(self) -> troposphere.msk.EncryptionInfo:
        from troposphere.msk import EncryptionInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Firehose(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html
    Properties:
        - Name: DeliveryStream
        - Name: Enabled
    
    """
    
    DeliveryStream_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html#cfn-msk-cluster-firehose-deliverystream""", alias="DeliveryStream")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html#cfn-msk-cluster-firehose-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.msk.Firehose:
        from troposphere.msk import Firehose as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Iam(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-iam.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-iam.html#cfn-msk-cluster-iam-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.msk.Iam:
        from troposphere.msk import Iam as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JmxExporter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html
    Properties:
        - Name: EnabledInBroker
    
    """
    
    EnabledInBroker_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html#cfn-msk-cluster-jmxexporter-enabledinbroker""", alias="EnabledInBroker")
    


    @property
    def tropo_type(self) -> troposphere.msk.JmxExporter:
        from troposphere.msk import JmxExporter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggingInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html
    Properties:
        - Name: BrokerLogs
    
    """
    
    BrokerLogs_: 'BrokerLogs' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html#cfn-msk-cluster-logginginfo-brokerlogs""", alias="BrokerLogs")
    


    @property
    def tropo_type(self) -> troposphere.msk.LoggingInfo:
        from troposphere.msk import LoggingInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NodeExporter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html
    Properties:
        - Name: EnabledInBroker
    
    """
    
    EnabledInBroker_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html#cfn-msk-cluster-nodeexporter-enabledinbroker""", alias="EnabledInBroker")
    


    @property
    def tropo_type(self) -> troposphere.msk.NodeExporter:
        from troposphere.msk import NodeExporter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OpenMonitoring(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html
    Properties:
        - Name: Prometheus
    
    """
    
    Prometheus_: 'Prometheus' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html#cfn-msk-cluster-openmonitoring-prometheus""", alias="Prometheus")
    


    @property
    def tropo_type(self) -> troposphere.msk.OpenMonitoring:
        from troposphere.msk import OpenMonitoring as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Prometheus(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html
    Properties:
        - Name: JmxExporter
        - Name: NodeExporter
    
    """
    
    JmxExporter_: Optional['JmxExporter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-jmxexporter""", alias="JmxExporter")
    NodeExporter_: Optional['NodeExporter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-nodeexporter""", alias="NodeExporter")
    


    @property
    def tropo_type(self) -> troposphere.msk.Prometheus:
        from troposphere.msk import Prometheus as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProvisionedThroughput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html
    Properties:
        - Name: VolumeThroughput
        - Name: Enabled
    
    """
    
    VolumeThroughput_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html#cfn-msk-cluster-provisionedthroughput-volumethroughput""", alias="VolumeThroughput")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html#cfn-msk-cluster-provisionedthroughput-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.msk.ProvisionedThroughput:
        from troposphere.msk import ProvisionedThroughput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PublicAccess(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-publicaccess.html
    Properties:
        - Name: Type
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-publicaccess.html#cfn-msk-cluster-publicaccess-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.msk.PublicAccess:
        from troposphere.msk import PublicAccess as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html
    Properties:
        - Name: Bucket
        - Name: Enabled
        - Name: Prefix
    
    """
    
    Bucket_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-bucket""", alias="Bucket")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-enabled""", alias="Enabled")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.msk.S3:
        from troposphere.msk import S3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Sasl(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html
    Properties:
        - Name: Iam
        - Name: Scram
    
    """
    
    Iam_: Optional['Iam'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-iam""", alias="Iam")
    Scram_: Optional['Scram'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-scram""", alias="Scram")
    


    @property
    def tropo_type(self) -> troposphere.msk.Sasl:
        from troposphere.msk import Sasl as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Scram(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html#cfn-msk-cluster-scram-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.msk.Scram:
        from troposphere.msk import Scram as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StorageInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html
    Properties:
        - Name: EBSStorageInfo
    
    """
    
    EBSStorageInfo_: Optional['EBSStorageInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html#cfn-msk-cluster-storageinfo-ebsstorageinfo""", alias="EBSStorageInfo")
    


    @property
    def tropo_type(self) -> troposphere.msk.StorageInfo:
        from troposphere.msk import StorageInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tls(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html
    Properties:
        - Name: Enabled
        - Name: CertificateAuthorityArnList
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html#cfn-msk-cluster-tls-enabled""", alias="Enabled")
    CertificateAuthorityArnList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html#cfn-msk-cluster-tls-certificateauthorityarnlist""", alias="CertificateAuthorityArnList")
    


    @property
    def tropo_type(self) -> troposphere.msk.Tls:
        from troposphere.msk import Tls as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Unauthenticated(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-unauthenticated.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-unauthenticated.html#cfn-msk-cluster-unauthenticated-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.msk.Unauthenticated:
        from troposphere.msk import Unauthenticated as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConnectivity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivity.html
    Properties:
        - Name: ClientAuthentication
    
    """
    
    ClientAuthentication_: Optional['VpcConnectivityClientAuthentication'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivity.html#cfn-msk-cluster-vpcconnectivity-clientauthentication""", alias="ClientAuthentication")
    


    @property
    def tropo_type(self) -> troposphere.msk.VpcConnectivity:
        from troposphere.msk import VpcConnectivity as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConnectivityClientAuthentication(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityclientauthentication.html
    Properties:
        - Name: Sasl
        - Name: Tls
    
    """
    
    Sasl_: Optional['VpcConnectivitySasl'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityclientauthentication.html#cfn-msk-cluster-vpcconnectivityclientauthentication-sasl""", alias="Sasl")
    Tls_: Optional['VpcConnectivityTls'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityclientauthentication.html#cfn-msk-cluster-vpcconnectivityclientauthentication-tls""", alias="Tls")
    


    @property
    def tropo_type(self) -> troposphere.msk.VpcConnectivityClientAuthentication:
        from troposphere.msk import VpcConnectivityClientAuthentication as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConnectivityIam(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityiam.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityiam.html#cfn-msk-cluster-vpcconnectivityiam-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.msk.VpcConnectivityIam:
        from troposphere.msk import VpcConnectivityIam as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConnectivitySasl(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivitysasl.html
    Properties:
        - Name: Iam
        - Name: Scram
    
    """
    
    Iam_: Optional['VpcConnectivityIam'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivitysasl.html#cfn-msk-cluster-vpcconnectivitysasl-iam""", alias="Iam")
    Scram_: Optional['VpcConnectivityScram'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivitysasl.html#cfn-msk-cluster-vpcconnectivitysasl-scram""", alias="Scram")
    


    @property
    def tropo_type(self) -> troposphere.msk.VpcConnectivitySasl:
        from troposphere.msk import VpcConnectivitySasl as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConnectivityScram(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityscram.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivityscram.html#cfn-msk-cluster-vpcconnectivityscram-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.msk.VpcConnectivityScram:
        from troposphere.msk import VpcConnectivityScram as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConnectivityTls(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivitytls.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-vpcconnectivitytls.html#cfn-msk-cluster-vpcconnectivitytls-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.msk.VpcConnectivityTls:
        from troposphere.msk import VpcConnectivityTls as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LatestRevision(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-configuration-latestrevision.html
    Properties:
        - Name: Description
        - Name: Revision
        - Name: CreationTime
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-configuration-latestrevision.html#cfn-msk-configuration-latestrevision-description""", alias="Description")
    Revision_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-configuration-latestrevision.html#cfn-msk-configuration-latestrevision-revision""", alias="Revision")
    CreationTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-configuration-latestrevision.html#cfn-msk-configuration-latestrevision-creationtime""", alias="CreationTime")
    


    @property
    def tropo_type(self) -> troposphere.msk.LatestRevision:
        from troposphere.msk import LatestRevision as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AmazonMskCluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-amazonmskcluster.html
    Properties:
        - Name: MskClusterArn
    
    """
    
    MskClusterArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-amazonmskcluster.html#cfn-msk-replicator-amazonmskcluster-mskclusterarn""", alias="MskClusterArn")
    


    @property
    def tropo_type(self) -> troposphere.msk.AmazonMskCluster:
        from troposphere.msk import AmazonMskCluster as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConsumerGroupReplication(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-consumergroupreplication.html
    Properties:
        - Name: ConsumerGroupsToReplicate
        - Name: ConsumerGroupsToExclude
        - Name: SynchroniseConsumerGroupOffsets
        - Name: DetectAndCopyNewConsumerGroups
    
    """
    
    ConsumerGroupsToReplicate_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-consumergroupreplication.html#cfn-msk-replicator-consumergroupreplication-consumergroupstoreplicate""", alias="ConsumerGroupsToReplicate")
    ConsumerGroupsToExclude_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-consumergroupreplication.html#cfn-msk-replicator-consumergroupreplication-consumergroupstoexclude""", alias="ConsumerGroupsToExclude")
    SynchroniseConsumerGroupOffsets_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-consumergroupreplication.html#cfn-msk-replicator-consumergroupreplication-synchroniseconsumergroupoffsets""", alias="SynchroniseConsumerGroupOffsets")
    DetectAndCopyNewConsumerGroups_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-consumergroupreplication.html#cfn-msk-replicator-consumergroupreplication-detectandcopynewconsumergroups""", alias="DetectAndCopyNewConsumerGroups")
    


    @property
    def tropo_type(self) -> troposphere.msk.ConsumerGroupReplication:
        from troposphere.msk import ConsumerGroupReplication as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KafkaCluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-kafkacluster.html
    Properties:
        - Name: VpcConfig
        - Name: AmazonMskCluster
    
    """
    
    VpcConfig_: 'KafkaClusterClientVpcConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-kafkacluster.html#cfn-msk-replicator-kafkacluster-vpcconfig""", alias="VpcConfig")
    AmazonMskCluster_: 'AmazonMskCluster' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-kafkacluster.html#cfn-msk-replicator-kafkacluster-amazonmskcluster""", alias="AmazonMskCluster")
    


    @property
    def tropo_type(self) -> troposphere.msk.KafkaCluster:
        from troposphere.msk import KafkaCluster as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KafkaClusterClientVpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-kafkaclusterclientvpcconfig.html
    Properties:
        - Name: SecurityGroupIds
        - Name: SubnetIds
    
    """
    
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-kafkaclusterclientvpcconfig.html#cfn-msk-replicator-kafkaclusterclientvpcconfig-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-kafkaclusterclientvpcconfig.html#cfn-msk-replicator-kafkaclusterclientvpcconfig-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.msk.KafkaClusterClientVpcConfig:
        from troposphere.msk import KafkaClusterClientVpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-replicationinfo.html
    Properties:
        - Name: TargetCompressionType
        - Name: TopicReplication
        - Name: ConsumerGroupReplication
        - Name: SourceKafkaClusterArn
        - Name: TargetKafkaClusterArn
    
    """
    
    TargetCompressionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-replicationinfo.html#cfn-msk-replicator-replicationinfo-targetcompressiontype""", alias="TargetCompressionType")
    TopicReplication_: 'TopicReplication' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-replicationinfo.html#cfn-msk-replicator-replicationinfo-topicreplication""", alias="TopicReplication")
    ConsumerGroupReplication_: 'ConsumerGroupReplication' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-replicationinfo.html#cfn-msk-replicator-replicationinfo-consumergroupreplication""", alias="ConsumerGroupReplication")
    SourceKafkaClusterArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-replicationinfo.html#cfn-msk-replicator-replicationinfo-sourcekafkaclusterarn""", alias="SourceKafkaClusterArn")
    TargetKafkaClusterArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-replicationinfo.html#cfn-msk-replicator-replicationinfo-targetkafkaclusterarn""", alias="TargetKafkaClusterArn")
    


    @property
    def tropo_type(self) -> troposphere.msk.ReplicationInfo:
        from troposphere.msk import ReplicationInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TopicReplication(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-topicreplication.html
    Properties:
        - Name: TopicsToReplicate
        - Name: TopicsToExclude
        - Name: CopyTopicConfigurations
        - Name: DetectAndCopyNewTopics
        - Name: CopyAccessControlListsForTopics
    
    """
    
    TopicsToReplicate_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-topicreplication.html#cfn-msk-replicator-topicreplication-topicstoreplicate""", alias="TopicsToReplicate")
    TopicsToExclude_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-topicreplication.html#cfn-msk-replicator-topicreplication-topicstoexclude""", alias="TopicsToExclude")
    CopyTopicConfigurations_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-topicreplication.html#cfn-msk-replicator-topicreplication-copytopicconfigurations""", alias="CopyTopicConfigurations")
    DetectAndCopyNewTopics_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-topicreplication.html#cfn-msk-replicator-topicreplication-detectandcopynewtopics""", alias="DetectAndCopyNewTopics")
    CopyAccessControlListsForTopics_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-replicator-topicreplication.html#cfn-msk-replicator-topicreplication-copyaccesscontrollistsfortopics""", alias="CopyAccessControlListsForTopics")
    


    @property
    def tropo_type(self) -> troposphere.msk.TopicReplication:
        from troposphere.msk import TopicReplication as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClientAuthentication(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-clientauthentication.html
    Properties:
        - Name: Sasl
    
    """
    
    Sasl_: 'Sasl' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-clientauthentication.html#cfn-msk-serverlesscluster-clientauthentication-sasl""", alias="Sasl")
    


    @property
    def tropo_type(self) -> troposphere.msk.ClientAuthentication:
        from troposphere.msk import ClientAuthentication as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Iam(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-iam.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-iam.html#cfn-msk-serverlesscluster-iam-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.msk.Iam:
        from troposphere.msk import Iam as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Sasl(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-sasl.html
    Properties:
        - Name: Iam
    
    """
    
    Iam_: 'Iam' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-sasl.html#cfn-msk-serverlesscluster-sasl-iam""", alias="Iam")
    


    @property
    def tropo_type(self) -> troposphere.msk.Sasl:
        from troposphere.msk import Sasl as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-vpcconfig.html
    Properties:
        - Name: SecurityGroups
        - Name: SubnetIds
    
    """
    
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-vpcconfig.html#cfn-msk-serverlesscluster-vpcconfig-securitygroups""", alias="SecurityGroups")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-vpcconfig.html#cfn-msk-serverlesscluster-vpcconfig-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.msk.VpcConfig:
        from troposphere.msk import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class BatchScramSecret(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html
    Properties:
        - Name: ClusterArn
        - Name: SecretArnList
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ClusterArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html#cfn-msk-batchscramsecret-clusterarn""", alias="ClusterArn")
    SecretArnList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html#cfn-msk-batchscramsecret-secretarnlist""", alias="SecretArnList")
    

    @property
    def tropo_type(self) -> troposphere.msk.BatchScramSecret:
        from troposphere.msk import BatchScramSecret as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.msk import BatchScramSecret as TropoT
        return resource_to_troposphere(self, TropoT)


class Cluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html
    Properties:
        - Name: KafkaVersion
        - Name: NumberOfBrokerNodes
        - Name: EncryptionInfo
        - Name: OpenMonitoring
        - Name: CurrentVersion
        - Name: StorageMode
        - Name: ConfigurationInfo
        - Name: BrokerNodeGroupInfo
        - Name: EnhancedMonitoring
        - Name: ClusterName
        - Name: ClientAuthentication
        - Name: LoggingInfo
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KafkaVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-kafkaversion""", alias="KafkaVersion")
    NumberOfBrokerNodes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-numberofbrokernodes""", alias="NumberOfBrokerNodes")
    EncryptionInfo_: Optional['EncryptionInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-encryptioninfo""", alias="EncryptionInfo")
    OpenMonitoring_: Optional['OpenMonitoring'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-openmonitoring""", alias="OpenMonitoring")
    CurrentVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-currentversion""", alias="CurrentVersion")
    StorageMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-storagemode""", alias="StorageMode")
    ConfigurationInfo_: Optional['ConfigurationInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-configurationinfo""", alias="ConfigurationInfo")
    BrokerNodeGroupInfo_: 'BrokerNodeGroupInfo' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-brokernodegroupinfo""", alias="BrokerNodeGroupInfo")
    EnhancedMonitoring_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-enhancedmonitoring""", alias="EnhancedMonitoring")
    ClusterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clustername""", alias="ClusterName")
    ClientAuthentication_: Optional['ClientAuthentication'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clientauthentication""", alias="ClientAuthentication")
    LoggingInfo_: Optional['LoggingInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-logginginfo""", alias="LoggingInfo")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.msk.Cluster:
        from troposphere.msk import Cluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.msk import Cluster as TropoT
        return resource_to_troposphere(self, TropoT)


class ClusterPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-clusterpolicy.html
    Properties:
        - Name: Policy
        - Name: ClusterArn
    Attributes:
        - Name: CurrentVersion
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-clusterpolicy.html#cfn-msk-clusterpolicy-policy""", alias="Policy")
    ClusterArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-clusterpolicy.html#cfn-msk-clusterpolicy-clusterarn""", alias="ClusterArn")
    

    @property
    def tropo_type(self) -> troposphere.msk.ClusterPolicy:
        from troposphere.msk import ClusterPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.msk import ClusterPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class Configuration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html
    Properties:
        - Name: Description
        - Name: LatestRevision
        - Name: ServerProperties
        - Name: KafkaVersionsList
        - Name: Name
    Attributes:
        - Name: LatestRevision.Revision
        - Name: LatestRevision.CreationTime
        - Name: LatestRevision.Description
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-description""", alias="Description")
    LatestRevision_: Optional['LatestRevision'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-latestrevision""", alias="LatestRevision")
    ServerProperties_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-serverproperties""", alias="ServerProperties")
    KafkaVersionsList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-kafkaversionslist""", alias="KafkaVersionsList")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.msk.Configuration:
        from troposphere.msk import Configuration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.msk import Configuration as TropoT
        return resource_to_troposphere(self, TropoT)


class Replicator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-replicator.html
    Properties:
        - Name: Description
        - Name: CurrentVersion
        - Name: ServiceExecutionRoleArn
        - Name: ReplicatorName
        - Name: ReplicationInfoList
        - Name: KafkaClusters
        - Name: Tags
    Attributes:
        - Name: ReplicatorArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-replicator.html#cfn-msk-replicator-description""", alias="Description")
    CurrentVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-replicator.html#cfn-msk-replicator-currentversion""", alias="CurrentVersion")
    ServiceExecutionRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-replicator.html#cfn-msk-replicator-serviceexecutionrolearn""", alias="ServiceExecutionRoleArn")
    ReplicatorName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-replicator.html#cfn-msk-replicator-replicatorname""", alias="ReplicatorName")
    ReplicationInfoList_: List['ReplicationInfo'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-replicator.html#cfn-msk-replicator-replicationinfolist""", alias="ReplicationInfoList")
    KafkaClusters_: List['KafkaCluster'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-replicator.html#cfn-msk-replicator-kafkaclusters""", alias="KafkaClusters")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-replicator.html#cfn-msk-replicator-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.msk.Replicator:
        from troposphere.msk import Replicator as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.msk import Replicator as TropoT
        return resource_to_troposphere(self, TropoT)


class ServerlessCluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html
    Properties:
        - Name: VpcConfigs
        - Name: ClusterName
        - Name: ClientAuthentication
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VpcConfigs_: List['VpcConfig'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-vpcconfigs""", alias="VpcConfigs")
    ClusterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-clustername""", alias="ClusterName")
    ClientAuthentication_: 'ClientAuthentication' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-clientauthentication""", alias="ClientAuthentication")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.msk.ServerlessCluster:
        from troposphere.msk import ServerlessCluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.msk import ServerlessCluster as TropoT
        return resource_to_troposphere(self, TropoT)


class VpcConnection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html
    Properties:
        - Name: SecurityGroups
        - Name: TargetClusterArn
        - Name: ClientSubnets
        - Name: VpcId
        - Name: Authentication
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SecurityGroups_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html#cfn-msk-vpcconnection-securitygroups""", alias="SecurityGroups")
    TargetClusterArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html#cfn-msk-vpcconnection-targetclusterarn""", alias="TargetClusterArn")
    ClientSubnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html#cfn-msk-vpcconnection-clientsubnets""", alias="ClientSubnets")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html#cfn-msk-vpcconnection-vpcid""", alias="VpcId")
    Authentication_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html#cfn-msk-vpcconnection-authentication""", alias="Authentication")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-vpcconnection.html#cfn-msk-vpcconnection-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.msk.VpcConnection:
        from troposphere.msk import VpcConnection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.msk import VpcConnection as TropoT
        return resource_to_troposphere(self, TropoT)

