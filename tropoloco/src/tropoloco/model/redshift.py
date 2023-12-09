from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Endpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html
    Properties:
        - Name: Address
        - Name: Port
    
    """
    
    Address_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html#cfn-redshift-cluster-endpoint-address""", alias="Address")
    Port_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html#cfn-redshift-cluster-endpoint-port""", alias="Port")
    


    @property
    def tropo_type(self) -> troposphere.redshift.Endpoint:
        from troposphere.redshift import Endpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggingProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html
    Properties:
        - Name: BucketName
        - Name: S3KeyPrefix
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-bucketname""", alias="BucketName")
    S3KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-s3keyprefix""", alias="S3KeyPrefix")
    


    @property
    def tropo_type(self) -> troposphere.redshift.LoggingProperties:
        from troposphere.redshift import LoggingProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AmazonRedshiftParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-clusterparametergroup-parameter.html
    Properties:
        - Name: ParameterValue
        - Name: ParameterName
    
    """
    
    ParameterValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-clusterparametergroup-parameter.html#cfn-redshift-clusterparametergroup-parameter-parametervalue""", alias="ParameterValue")
    ParameterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-clusterparametergroup-parameter.html#cfn-redshift-clusterparametergroup-parameter-parametername""", alias="ParameterName")
    


    @property
    def tropo_type(self) -> troposphere.redshift.AmazonRedshiftParameter:
        from troposphere.redshift import AmazonRedshiftParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkInterface(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-networkinterface.html
    Properties:
        - Name: PrivateIpAddress
        - Name: AvailabilityZone
        - Name: SubnetId
        - Name: NetworkInterfaceId
    
    """
    
    PrivateIpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-networkinterface.html#cfn-redshift-endpointaccess-networkinterface-privateipaddress""", alias="PrivateIpAddress")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-networkinterface.html#cfn-redshift-endpointaccess-networkinterface-availabilityzone""", alias="AvailabilityZone")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-networkinterface.html#cfn-redshift-endpointaccess-networkinterface-subnetid""", alias="SubnetId")
    NetworkInterfaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-networkinterface.html#cfn-redshift-endpointaccess-networkinterface-networkinterfaceid""", alias="NetworkInterfaceId")
    


    @property
    def tropo_type(self) -> troposphere.redshift.NetworkInterface:
        from troposphere.redshift import NetworkInterface as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcendpoint.html
    Properties:
        - Name: VpcId
        - Name: NetworkInterfaces
        - Name: VpcEndpointId
    
    """
    
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcendpoint.html#cfn-redshift-endpointaccess-vpcendpoint-vpcid""", alias="VpcId")
    NetworkInterfaces_: Optional[List['NetworkInterface']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcendpoint.html#cfn-redshift-endpointaccess-vpcendpoint-networkinterfaces""", alias="NetworkInterfaces")
    VpcEndpointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcendpoint.html#cfn-redshift-endpointaccess-vpcendpoint-vpcendpointid""", alias="VpcEndpointId")
    


    @property
    def tropo_type(self) -> troposphere.redshift.VpcEndpoint:
        from troposphere.redshift import VpcEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcSecurityGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcsecuritygroup.html
    Properties:
        - Name: Status
        - Name: VpcSecurityGroupId
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcsecuritygroup.html#cfn-redshift-endpointaccess-vpcsecuritygroup-status""", alias="Status")
    VpcSecurityGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcsecuritygroup.html#cfn-redshift-endpointaccess-vpcsecuritygroup-vpcsecuritygroupid""", alias="VpcSecurityGroupId")
    


    @property
    def tropo_type(self) -> troposphere.redshift.VpcSecurityGroup:
        from troposphere.redshift import VpcSecurityGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PauseClusterMessage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-pauseclustermessage.html
    Properties:
        - Name: ClusterIdentifier
    
    """
    
    ClusterIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-pauseclustermessage.html#cfn-redshift-scheduledaction-pauseclustermessage-clusteridentifier""", alias="ClusterIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.redshift.PauseClusterMessage:
        from troposphere.redshift import PauseClusterMessage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResizeClusterMessage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html
    Properties:
        - Name: NodeType
        - Name: NumberOfNodes
        - Name: ClusterType
        - Name: Classic
        - Name: ClusterIdentifier
    
    """
    
    NodeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html#cfn-redshift-scheduledaction-resizeclustermessage-nodetype""", alias="NodeType")
    NumberOfNodes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html#cfn-redshift-scheduledaction-resizeclustermessage-numberofnodes""", alias="NumberOfNodes")
    ClusterType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html#cfn-redshift-scheduledaction-resizeclustermessage-clustertype""", alias="ClusterType")
    Classic_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html#cfn-redshift-scheduledaction-resizeclustermessage-classic""", alias="Classic")
    ClusterIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html#cfn-redshift-scheduledaction-resizeclustermessage-clusteridentifier""", alias="ClusterIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.redshift.ResizeClusterMessage:
        from troposphere.redshift import ResizeClusterMessage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResumeClusterMessage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resumeclustermessage.html
    Properties:
        - Name: ClusterIdentifier
    
    """
    
    ClusterIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resumeclustermessage.html#cfn-redshift-scheduledaction-resumeclustermessage-clusteridentifier""", alias="ClusterIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.redshift.ResumeClusterMessage:
        from troposphere.redshift import ResumeClusterMessage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScheduledActionType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-scheduledactiontype.html
    Properties:
        - Name: PauseCluster
        - Name: ResumeCluster
        - Name: ResizeCluster
    
    """
    
    PauseCluster_: Optional['PauseClusterMessage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-scheduledactiontype.html#cfn-redshift-scheduledaction-scheduledactiontype-pausecluster""", alias="PauseCluster")
    ResumeCluster_: Optional['ResumeClusterMessage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-scheduledactiontype.html#cfn-redshift-scheduledaction-scheduledactiontype-resumecluster""", alias="ResumeCluster")
    ResizeCluster_: Optional['ResizeClusterMessage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-scheduledactiontype.html#cfn-redshift-scheduledaction-scheduledactiontype-resizecluster""", alias="ResizeCluster")
    


    @property
    def tropo_type(self) -> troposphere.redshift.ScheduledActionType:
        from troposphere.redshift import ScheduledActionType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Cluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html
    Properties:
        - Name: RevisionTarget
        - Name: AutomatedSnapshotRetentionPeriod
        - Name: Encrypted
        - Name: Port
        - Name: NumberOfNodes
        - Name: DestinationRegion
        - Name: AllowVersionUpgrade
        - Name: Endpoint
        - Name: MaintenanceTrackName
        - Name: OwnerAccount
        - Name: MultiAZ
        - Name: Tags
        - Name: SnapshotClusterIdentifier
        - Name: IamRoles
        - Name: KmsKeyId
        - Name: SnapshotCopyManual
        - Name: AvailabilityZone
        - Name: ClusterSecurityGroups
        - Name: ClusterIdentifier
        - Name: MasterUserPassword
        - Name: ClusterSubnetGroupName
        - Name: LoggingProperties
        - Name: DeferMaintenance
        - Name: NodeType
        - Name: MasterUsername
        - Name: PubliclyAccessible
        - Name: ManualSnapshotRetentionPeriod
        - Name: ResourceAction
        - Name: HsmClientCertificateIdentifier
        - Name: ElasticIp
        - Name: AvailabilityZoneRelocationStatus
        - Name: AquaConfigurationStatus
        - Name: SnapshotIdentifier
        - Name: AvailabilityZoneRelocation
        - Name: SnapshotCopyGrantName
        - Name: EnhancedVpcRouting
        - Name: ClusterParameterGroupName
        - Name: DeferMaintenanceEndTime
        - Name: RotateEncryptionKey
        - Name: VpcSecurityGroupIds
        - Name: ClusterVersion
        - Name: HsmConfigurationIdentifier
        - Name: PreferredMaintenanceWindow
        - Name: DeferMaintenanceStartTime
        - Name: ClusterType
        - Name: Classic
        - Name: DeferMaintenanceDuration
        - Name: DBName
        - Name: SnapshotCopyRetentionPeriod
    Attributes:
        - Name: Endpoint.Address
        - Name: Endpoint.Port
        - Name: Id
        - Name: DeferMaintenanceIdentifier
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RevisionTarget_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-revisiontarget""", alias="RevisionTarget")
    AutomatedSnapshotRetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-automatedsnapshotretentionperiod""", alias="AutomatedSnapshotRetentionPeriod")
    Encrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-encrypted""", alias="Encrypted")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-port""", alias="Port")
    NumberOfNodes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-numberofnodes""", alias="NumberOfNodes")
    DestinationRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-destinationregion""", alias="DestinationRegion")
    AllowVersionUpgrade_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-allowversionupgrade""", alias="AllowVersionUpgrade")
    Endpoint_: Optional['Endpoint'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-endpoint""", alias="Endpoint")
    MaintenanceTrackName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-maintenancetrackname""", alias="MaintenanceTrackName")
    OwnerAccount_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-owneraccount""", alias="OwnerAccount")
    MultiAZ_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-multiaz""", alias="MultiAZ")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-tags""", alias="Tags")
    SnapshotClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotclusteridentifier""", alias="SnapshotClusterIdentifier")
    IamRoles_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-iamroles""", alias="IamRoles")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-kmskeyid""", alias="KmsKeyId")
    SnapshotCopyManual_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotcopymanual""", alias="SnapshotCopyManual")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-availabilityzone""", alias="AvailabilityZone")
    ClusterSecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clustersecuritygroups""", alias="ClusterSecurityGroups")
    ClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clusteridentifier""", alias="ClusterIdentifier")
    MasterUserPassword_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-masteruserpassword""", alias="MasterUserPassword")
    ClusterSubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clustersubnetgroupname""", alias="ClusterSubnetGroupName")
    LoggingProperties_: Optional['LoggingProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-loggingproperties""", alias="LoggingProperties")
    DeferMaintenance_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenance""", alias="DeferMaintenance")
    NodeType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-nodetype""", alias="NodeType")
    MasterUsername_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-masterusername""", alias="MasterUsername")
    PubliclyAccessible_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-publiclyaccessible""", alias="PubliclyAccessible")
    ManualSnapshotRetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-manualsnapshotretentionperiod""", alias="ManualSnapshotRetentionPeriod")
    ResourceAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-resourceaction""", alias="ResourceAction")
    HsmClientCertificateIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-hsmclientcertificateidentifier""", alias="HsmClientCertificateIdentifier")
    ElasticIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-elasticip""", alias="ElasticIp")
    AvailabilityZoneRelocationStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-availabilityzonerelocationstatus""", alias="AvailabilityZoneRelocationStatus")
    AquaConfigurationStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-aquaconfigurationstatus""", alias="AquaConfigurationStatus")
    SnapshotIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotidentifier""", alias="SnapshotIdentifier")
    AvailabilityZoneRelocation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-availabilityzonerelocation""", alias="AvailabilityZoneRelocation")
    SnapshotCopyGrantName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotcopygrantname""", alias="SnapshotCopyGrantName")
    EnhancedVpcRouting_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-enhancedvpcrouting""", alias="EnhancedVpcRouting")
    ClusterParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clusterparametergroupname""", alias="ClusterParameterGroupName")
    DeferMaintenanceEndTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenanceendtime""", alias="DeferMaintenanceEndTime")
    RotateEncryptionKey_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-rotateencryptionkey""", alias="RotateEncryptionKey")
    VpcSecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-vpcsecuritygroupids""", alias="VpcSecurityGroupIds")
    ClusterVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clusterversion""", alias="ClusterVersion")
    HsmConfigurationIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-hsmconfigurationidentifier""", alias="HsmConfigurationIdentifier")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    DeferMaintenanceStartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenancestarttime""", alias="DeferMaintenanceStartTime")
    ClusterType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clustertype""", alias="ClusterType")
    Classic_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-classic""", alias="Classic")
    DeferMaintenanceDuration_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenanceduration""", alias="DeferMaintenanceDuration")
    DBName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-dbname""", alias="DBName")
    SnapshotCopyRetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotcopyretentionperiod""", alias="SnapshotCopyRetentionPeriod")
    

    @property
    def tropo_type(self) -> troposphere.redshift.Cluster:
        from troposphere.redshift import Cluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.redshift import Cluster as TropoT
        return resource_to_troposphere(self, TropoT)


class ClusterParameterGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html
    Properties:
        - Name: Description
        - Name: Parameters
        - Name: ParameterGroupName
        - Name: ParameterGroupFamily
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-description""", alias="Description")
    Parameters_: Optional[List['AmazonRedshiftParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-parameters""", alias="Parameters")
    ParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-parametergroupname""", alias="ParameterGroupName")
    ParameterGroupFamily_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-parametergroupfamily""", alias="ParameterGroupFamily")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.redshift.ClusterParameterGroup:
        from troposphere.redshift import ClusterParameterGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.redshift import ClusterParameterGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class ClusterSecurityGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html
    Properties:
        - Name: Description
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html#cfn-redshift-clustersecuritygroup-description""", alias="Description")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html#cfn-redshift-clustersecuritygroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.redshift.ClusterSecurityGroup:
        from troposphere.redshift import ClusterSecurityGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.redshift import ClusterSecurityGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class ClusterSecurityGroupIngress(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html
    Properties:
        - Name: CIDRIP
        - Name: ClusterSecurityGroupName
        - Name: EC2SecurityGroupName
        - Name: EC2SecurityGroupOwnerId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CIDRIP_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-cidrip""", alias="CIDRIP")
    ClusterSecurityGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-clustersecuritygroupname""", alias="ClusterSecurityGroupName")
    EC2SecurityGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-ec2securitygroupname""", alias="EC2SecurityGroupName")
    EC2SecurityGroupOwnerId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-ec2securitygroupownerid""", alias="EC2SecurityGroupOwnerId")
    

    @property
    def tropo_type(self) -> troposphere.redshift.ClusterSecurityGroupIngress:
        from troposphere.redshift import ClusterSecurityGroupIngress as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.redshift import ClusterSecurityGroupIngress as TropoT
        return resource_to_troposphere(self, TropoT)


class ClusterSubnetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html
    Properties:
        - Name: Description
        - Name: SubnetIds
        - Name: Tags
    Attributes:
        - Name: ClusterSubnetGroupName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html#cfn-redshift-clustersubnetgroup-description""", alias="Description")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html#cfn-redshift-clustersubnetgroup-subnetids""", alias="SubnetIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html#cfn-redshift-clustersubnetgroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.redshift.ClusterSubnetGroup:
        from troposphere.redshift import ClusterSubnetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.redshift import ClusterSubnetGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class EndpointAccess(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html
    Properties:
        - Name: EndpointName
        - Name: VpcSecurityGroupIds
        - Name: ResourceOwner
        - Name: SubnetGroupName
        - Name: ClusterIdentifier
    Attributes:
        - Name: EndpointStatus
        - Name: VpcEndpoint
        - Name: Address
        - Name: Port
        - Name: EndpointCreateTime
        - Name: VpcEndpoint.VpcId
        - Name: VpcEndpoint.NetworkInterfaces
        - Name: VpcSecurityGroups
        - Name: VpcEndpoint.VpcEndpointId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EndpointName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-endpointname""", alias="EndpointName")
    VpcSecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-vpcsecuritygroupids""", alias="VpcSecurityGroupIds")
    ResourceOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-resourceowner""", alias="ResourceOwner")
    SubnetGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-subnetgroupname""", alias="SubnetGroupName")
    ClusterIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-clusteridentifier""", alias="ClusterIdentifier")
    

    @property
    def tropo_type(self) -> troposphere.redshift.EndpointAccess:
        from troposphere.redshift import EndpointAccess as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.redshift import EndpointAccess as TropoT
        return resource_to_troposphere(self, TropoT)


class EndpointAuthorization(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html
    Properties:
        - Name: Account
        - Name: Force
        - Name: VpcIds
        - Name: ClusterIdentifier
    Attributes:
        - Name: Status
        - Name: Grantee
        - Name: Grantor
        - Name: EndpointCount
        - Name: AuthorizeTime
        - Name: AllowedVPCs
        - Name: AllowedAllVPCs
        - Name: ClusterStatus
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Account_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-account""", alias="Account")
    Force_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-force""", alias="Force")
    VpcIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-vpcids""", alias="VpcIds")
    ClusterIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-clusteridentifier""", alias="ClusterIdentifier")
    

    @property
    def tropo_type(self) -> troposphere.redshift.EndpointAuthorization:
        from troposphere.redshift import EndpointAuthorization as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.redshift import EndpointAuthorization as TropoT
        return resource_to_troposphere(self, TropoT)


class EventSubscription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html
    Properties:
        - Name: SourceType
        - Name: EventCategories
        - Name: Enabled
        - Name: Severity
        - Name: SubscriptionName
        - Name: SourceIds
        - Name: SnsTopicArn
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: CustSubscriptionId
        - Name: EventCategoriesList
        - Name: SourceIdsList
        - Name: SubscriptionCreationTime
        - Name: CustomerAwsId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-sourcetype""", alias="SourceType")
    EventCategories_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-eventcategories""", alias="EventCategories")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-enabled""", alias="Enabled")
    Severity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-severity""", alias="Severity")
    SubscriptionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-subscriptionname""", alias="SubscriptionName")
    SourceIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-sourceids""", alias="SourceIds")
    SnsTopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-snstopicarn""", alias="SnsTopicArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.redshift.EventSubscription:
        from troposphere.redshift import EventSubscription as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.redshift import EventSubscription as TropoT
        return resource_to_troposphere(self, TropoT)


class ScheduledAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html
    Properties:
        - Name: ScheduledActionDescription
        - Name: ScheduledActionName
        - Name: EndTime
        - Name: Schedule
        - Name: IamRole
        - Name: StartTime
        - Name: Enable
        - Name: TargetAction
    Attributes:
        - Name: State
        - Name: NextInvocations
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ScheduledActionDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-scheduledactiondescription""", alias="ScheduledActionDescription")
    ScheduledActionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-scheduledactionname""", alias="ScheduledActionName")
    EndTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-endtime""", alias="EndTime")
    Schedule_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-schedule""", alias="Schedule")
    IamRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-iamrole""", alias="IamRole")
    StartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-starttime""", alias="StartTime")
    Enable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-enable""", alias="Enable")
    TargetAction_: Optional['ScheduledActionType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-targetaction""", alias="TargetAction")
    

    @property
    def tropo_type(self) -> troposphere.redshift.ScheduledAction:
        from troposphere.redshift import ScheduledAction as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.redshift import ScheduledAction as TropoT
        return resource_to_troposphere(self, TropoT)

