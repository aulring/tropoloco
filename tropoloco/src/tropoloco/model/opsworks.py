from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html
    Properties:
        - Name: Arn
        - Name: DatabaseName
        - Name: Type
    
    """
    
    Arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-arn""", alias="Arn")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-databasename""", alias="DatabaseName")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.DataSource:
        from troposphere.opsworks import DataSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnvironmentVariable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html
    Properties:
        - Name: Key
        - Name: Secure
        - Name: Value
    
    """
    
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html#cfn-opsworks-app-environment-key""", alias="Key")
    Secure_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html#cfn-opsworks-app-environment-secure""", alias="Secure")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html#value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.EnvironmentVariable:
        from troposphere.opsworks import EnvironmentVariable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Source(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html
    Properties:
        - Name: Password
        - Name: Revision
        - Name: SshKey
        - Name: Type
        - Name: Url
        - Name: Username
    
    """
    
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-pw""", alias="Password")
    Revision_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-revision""", alias="Revision")
    SshKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-sshkey""", alias="SshKey")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-type""", alias="Type")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-url""", alias="Url")
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-username""", alias="Username")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.Source:
        from troposphere.opsworks import Source as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SslConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html
    Properties:
        - Name: Certificate
        - Name: Chain
        - Name: PrivateKey
    
    """
    
    Certificate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfig-certificate""", alias="Certificate")
    Chain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfig-chain""", alias="Chain")
    PrivateKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfig-privatekey""", alias="PrivateKey")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.SslConfiguration:
        from troposphere.opsworks import SslConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BlockDeviceMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html
    Properties:
        - Name: DeviceName
        - Name: Ebs
        - Name: NoDevice
        - Name: VirtualName
    
    """
    
    DeviceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-devicename""", alias="DeviceName")
    Ebs_: Optional['EbsBlockDevice'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-ebs""", alias="Ebs")
    NoDevice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-nodevice""", alias="NoDevice")
    VirtualName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-virtualname""", alias="VirtualName")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.BlockDeviceMapping:
        from troposphere.opsworks import BlockDeviceMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EbsBlockDevice(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html
    Properties:
        - Name: DeleteOnTermination
        - Name: Iops
        - Name: SnapshotId
        - Name: VolumeSize
        - Name: VolumeType
    
    """
    
    DeleteOnTermination_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-deleteontermination""", alias="DeleteOnTermination")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-iops""", alias="Iops")
    SnapshotId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-snapshotid""", alias="SnapshotId")
    VolumeSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-volumesize""", alias="VolumeSize")
    VolumeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-volumetype""", alias="VolumeType")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.EbsBlockDevice:
        from troposphere.opsworks import EbsBlockDevice as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimeBasedAutoScaling(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html
    Properties:
        - Name: Friday
        - Name: Monday
        - Name: Saturday
        - Name: Sunday
        - Name: Thursday
        - Name: Tuesday
        - Name: Wednesday
    
    """
    
    Friday_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-friday""", alias="Friday")
    Monday_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-monday""", alias="Monday")
    Saturday_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-saturday""", alias="Saturday")
    Sunday_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-sunday""", alias="Sunday")
    Thursday_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-thursday""", alias="Thursday")
    Tuesday_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-tuesday""", alias="Tuesday")
    Wednesday_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-wednesday""", alias="Wednesday")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.TimeBasedAutoScaling:
        from troposphere.opsworks import TimeBasedAutoScaling as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoScalingThresholds(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html
    Properties:
        - Name: CpuThreshold
        - Name: IgnoreMetricsTime
        - Name: InstanceCount
        - Name: LoadThreshold
        - Name: MemoryThreshold
        - Name: ThresholdsWaitTime
    
    """
    
    CpuThreshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-cputhreshold""", alias="CpuThreshold")
    IgnoreMetricsTime_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-ignoremetricstime""", alias="IgnoreMetricsTime")
    InstanceCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-instancecount""", alias="InstanceCount")
    LoadThreshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-loadthreshold""", alias="LoadThreshold")
    MemoryThreshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-memorythreshold""", alias="MemoryThreshold")
    ThresholdsWaitTime_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-thresholdwaittime""", alias="ThresholdsWaitTime")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.AutoScalingThresholds:
        from troposphere.opsworks import AutoScalingThresholds as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LifecycleEventConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration.html
    Properties:
        - Name: ShutdownEventConfiguration
    
    """
    
    ShutdownEventConfiguration_: Optional['ShutdownEventConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration""", alias="ShutdownEventConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.LifecycleEventConfiguration:
        from troposphere.opsworks import LifecycleEventConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoadBasedAutoScaling(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html
    Properties:
        - Name: DownScaling
        - Name: Enable
        - Name: UpScaling
    
    """
    
    DownScaling_: Optional['AutoScalingThresholds'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-downscaling""", alias="DownScaling")
    Enable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-enable""", alias="Enable")
    UpScaling_: Optional['AutoScalingThresholds'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-upscaling""", alias="UpScaling")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.LoadBasedAutoScaling:
        from troposphere.opsworks import LoadBasedAutoScaling as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Recipes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html
    Properties:
        - Name: Configure
        - Name: Deploy
        - Name: Setup
        - Name: Shutdown
        - Name: Undeploy
    
    """
    
    Configure_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-configure""", alias="Configure")
    Deploy_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-deploy""", alias="Deploy")
    Setup_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-setup""", alias="Setup")
    Shutdown_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-shutdown""", alias="Shutdown")
    Undeploy_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-undeploy""", alias="Undeploy")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.Recipes:
        from troposphere.opsworks import Recipes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ShutdownEventConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html
    Properties:
        - Name: DelayUntilElbConnectionsDrained
        - Name: ExecutionTimeout
    
    """
    
    DelayUntilElbConnectionsDrained_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration-delayuntilelbconnectionsdrained""", alias="DelayUntilElbConnectionsDrained")
    ExecutionTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration-executiontimeout""", alias="ExecutionTimeout")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.ShutdownEventConfiguration:
        from troposphere.opsworks import ShutdownEventConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VolumeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html
    Properties:
        - Name: Encrypted
        - Name: Iops
        - Name: MountPoint
        - Name: NumberOfDisks
        - Name: RaidLevel
        - Name: Size
        - Name: VolumeType
    
    """
    
    Encrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volumeconfiguration-encrypted""", alias="Encrypted")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-iops""", alias="Iops")
    MountPoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-mountpoint""", alias="MountPoint")
    NumberOfDisks_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-numberofdisks""", alias="NumberOfDisks")
    RaidLevel_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-raidlevel""", alias="RaidLevel")
    Size_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-size""", alias="Size")
    VolumeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-volumetype""", alias="VolumeType")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.VolumeConfiguration:
        from troposphere.opsworks import VolumeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ChefConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html
    Properties:
        - Name: BerkshelfVersion
        - Name: ManageBerkshelf
    
    """
    
    BerkshelfVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html#cfn-opsworks-chefconfiguration-berkshelfversion""", alias="BerkshelfVersion")
    ManageBerkshelf_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html#cfn-opsworks-chefconfiguration-berkshelfversion""", alias="ManageBerkshelf")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.ChefConfiguration:
        from troposphere.opsworks import ChefConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ElasticIp(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html
    Properties:
        - Name: Ip
        - Name: Name
    
    """
    
    Ip_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html#cfn-opsworks-stack-elasticip-ip""", alias="Ip")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html#cfn-opsworks-stack-elasticip-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.ElasticIp:
        from troposphere.opsworks import ElasticIp as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RdsDbInstance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html
    Properties:
        - Name: DbPassword
        - Name: DbUser
        - Name: RdsDbInstanceArn
    
    """
    
    DbPassword_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-dbpassword""", alias="DbPassword")
    DbUser_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-dbuser""", alias="DbUser")
    RdsDbInstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-rdsdbinstancearn""", alias="RdsDbInstanceArn")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.RdsDbInstance:
        from troposphere.opsworks import RdsDbInstance as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Source(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html
    Properties:
        - Name: Password
        - Name: Revision
        - Name: SshKey
        - Name: Type
        - Name: Url
        - Name: Username
    
    """
    
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-password""", alias="Password")
    Revision_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-revision""", alias="Revision")
    SshKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-sshkey""", alias="SshKey")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-type""", alias="Type")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-url""", alias="Url")
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-username""", alias="Username")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.Source:
        from troposphere.opsworks import Source as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StackConfigurationManager(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigmanager.html
    Properties:
        - Name: Name
        - Name: Version
    
    """
    
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigmanager.html#cfn-opsworks-configmanager-name""", alias="Name")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigmanager.html#cfn-opsworks-configmanager-version""", alias="Version")
    


    @property
    def tropo_type(self) -> troposphere.opsworks.StackConfigurationManager:
        from troposphere.opsworks import StackConfigurationManager as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class App(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html
    Properties:
        - Name: AppSource
        - Name: Attributes
        - Name: DataSources
        - Name: Description
        - Name: Domains
        - Name: EnableSsl
        - Name: Environment
        - Name: Name
        - Name: Shortname
        - Name: SslConfiguration
        - Name: StackId
        - Name: Type
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AppSource_: Optional['Source'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-appsource""", alias="AppSource")
    Attributes_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-attributes""", alias="Attributes")
    DataSources_: Optional[List['DataSource']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-datasources""", alias="DataSources")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-description""", alias="Description")
    Domains_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-domains""", alias="Domains")
    EnableSsl_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-enablessl""", alias="EnableSsl")
    Environment_: Optional[List['EnvironmentVariable']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-environment""", alias="Environment")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-name""", alias="Name")
    Shortname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-shortname""", alias="Shortname")
    SslConfiguration_: Optional['SslConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-sslconfiguration""", alias="SslConfiguration")
    StackId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-stackid""", alias="StackId")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-type""", alias="Type")
    

    @property
    def tropo_type(self) -> troposphere.opsworks.App:
        from troposphere.opsworks import App as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opsworks import App as TropoT
        return resource_to_troposphere(self, TropoT)


class ElasticLoadBalancerAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html
    Properties:
        - Name: ElasticLoadBalancerName
        - Name: LayerId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ElasticLoadBalancerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html#cfn-opsworks-elbattachment-elbname""", alias="ElasticLoadBalancerName")
    LayerId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html#cfn-opsworks-elbattachment-layerid""", alias="LayerId")
    

    @property
    def tropo_type(self) -> troposphere.opsworks.ElasticLoadBalancerAttachment:
        from troposphere.opsworks import ElasticLoadBalancerAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opsworks import ElasticLoadBalancerAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class Instance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html
    Properties:
        - Name: AgentVersion
        - Name: AmiId
        - Name: Architecture
        - Name: AutoScalingType
        - Name: AvailabilityZone
        - Name: BlockDeviceMappings
        - Name: EbsOptimized
        - Name: ElasticIps
        - Name: Hostname
        - Name: InstallUpdatesOnBoot
        - Name: InstanceType
        - Name: LayerIds
        - Name: Os
        - Name: RootDeviceType
        - Name: SshKeyName
        - Name: StackId
        - Name: SubnetId
        - Name: Tenancy
        - Name: TimeBasedAutoScaling
        - Name: VirtualizationType
        - Name: Volumes
    Attributes:
        - Name: AvailabilityZone
        - Name: PrivateDnsName
        - Name: PrivateIp
        - Name: PublicDnsName
        - Name: PublicIp
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AgentVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-agentversion""", alias="AgentVersion")
    AmiId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-amiid""", alias="AmiId")
    Architecture_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-architecture""", alias="Architecture")
    AutoScalingType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-autoscalingtype""", alias="AutoScalingType")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-availabilityzone""", alias="AvailabilityZone")
    BlockDeviceMappings_: Optional[List['BlockDeviceMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-blockdevicemappings""", alias="BlockDeviceMappings")
    EbsOptimized_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-ebsoptimized""", alias="EbsOptimized")
    ElasticIps_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-elasticips""", alias="ElasticIps")
    Hostname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-hostname""", alias="Hostname")
    InstallUpdatesOnBoot_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-installupdatesonboot""", alias="InstallUpdatesOnBoot")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-instancetype""", alias="InstanceType")
    LayerIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-layerids""", alias="LayerIds")
    Os_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-os""", alias="Os")
    RootDeviceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-rootdevicetype""", alias="RootDeviceType")
    SshKeyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-sshkeyname""", alias="SshKeyName")
    StackId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-stackid""", alias="StackId")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-subnetid""", alias="SubnetId")
    Tenancy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-tenancy""", alias="Tenancy")
    TimeBasedAutoScaling_: Optional['TimeBasedAutoScaling'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-timebasedautoscaling""", alias="TimeBasedAutoScaling")
    VirtualizationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-virtualizationtype""", alias="VirtualizationType")
    Volumes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-volumes""", alias="Volumes")
    

    @property
    def tropo_type(self) -> troposphere.opsworks.Instance:
        from troposphere.opsworks import Instance as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opsworks import Instance as TropoT
        return resource_to_troposphere(self, TropoT)


class Layer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html
    Properties:
        - Name: Attributes
        - Name: AutoAssignElasticIps
        - Name: AutoAssignPublicIps
        - Name: CustomInstanceProfileArn
        - Name: CustomJson
        - Name: CustomRecipes
        - Name: CustomSecurityGroupIds
        - Name: EnableAutoHealing
        - Name: InstallUpdatesOnBoot
        - Name: LifecycleEventConfiguration
        - Name: LoadBasedAutoScaling
        - Name: Name
        - Name: Packages
        - Name: Shortname
        - Name: StackId
        - Name: Tags
        - Name: Type
        - Name: UseEbsOptimizedInstances
        - Name: VolumeConfigurations
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Attributes_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-attributes""", alias="Attributes")
    AutoAssignElasticIps_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-autoassignelasticips""", alias="AutoAssignElasticIps")
    AutoAssignPublicIps_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-autoassignpublicips""", alias="AutoAssignPublicIps")
    CustomInstanceProfileArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-custominstanceprofilearn""", alias="CustomInstanceProfileArn")
    CustomJson_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customjson""", alias="CustomJson")
    CustomRecipes_: Optional['Recipes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customrecipes""", alias="CustomRecipes")
    CustomSecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customsecuritygroupids""", alias="CustomSecurityGroupIds")
    EnableAutoHealing_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-enableautohealing""", alias="EnableAutoHealing")
    InstallUpdatesOnBoot_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-installupdatesonboot""", alias="InstallUpdatesOnBoot")
    LifecycleEventConfiguration_: Optional['LifecycleEventConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-lifecycleeventconfiguration""", alias="LifecycleEventConfiguration")
    LoadBasedAutoScaling_: Optional['LoadBasedAutoScaling'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-loadbasedautoscaling""", alias="LoadBasedAutoScaling")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-name""", alias="Name")
    Packages_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-packages""", alias="Packages")
    Shortname_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-shortname""", alias="Shortname")
    StackId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-stackid""", alias="StackId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-tags""", alias="Tags")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-type""", alias="Type")
    UseEbsOptimizedInstances_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-useebsoptimizedinstances""", alias="UseEbsOptimizedInstances")
    VolumeConfigurations_: Optional[List['VolumeConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-volumeconfigurations""", alias="VolumeConfigurations")
    

    @property
    def tropo_type(self) -> troposphere.opsworks.Layer:
        from troposphere.opsworks import Layer as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opsworks import Layer as TropoT
        return resource_to_troposphere(self, TropoT)


class Stack(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html
    Properties:
        - Name: AgentVersion
        - Name: Attributes
        - Name: ChefConfiguration
        - Name: CloneAppIds
        - Name: ClonePermissions
        - Name: ConfigurationManager
        - Name: CustomCookbooksSource
        - Name: CustomJson
        - Name: DefaultAvailabilityZone
        - Name: DefaultInstanceProfileArn
        - Name: DefaultOs
        - Name: DefaultRootDeviceType
        - Name: DefaultSshKeyName
        - Name: DefaultSubnetId
        - Name: EcsClusterArn
        - Name: ElasticIps
        - Name: HostnameTheme
        - Name: Name
        - Name: RdsDbInstances
        - Name: ServiceRoleArn
        - Name: SourceStackId
        - Name: Tags
        - Name: UseCustomCookbooks
        - Name: UseOpsworksSecurityGroups
        - Name: VpcId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AgentVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-agentversion""", alias="AgentVersion")
    Attributes_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-attributes""", alias="Attributes")
    ChefConfiguration_: Optional['ChefConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-chefconfiguration""", alias="ChefConfiguration")
    CloneAppIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-cloneappids""", alias="CloneAppIds")
    ClonePermissions_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-clonepermissions""", alias="ClonePermissions")
    ConfigurationManager_: Optional['StackConfigurationManager'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-configmanager""", alias="ConfigurationManager")
    CustomCookbooksSource_: Optional['Source'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-custcookbooksource""", alias="CustomCookbooksSource")
    CustomJson_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-custjson""", alias="CustomJson")
    DefaultAvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultaz""", alias="DefaultAvailabilityZone")
    DefaultInstanceProfileArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultinstanceprof""", alias="DefaultInstanceProfileArn")
    DefaultOs_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultos""", alias="DefaultOs")
    DefaultRootDeviceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultrootdevicetype""", alias="DefaultRootDeviceType")
    DefaultSshKeyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultsshkeyname""", alias="DefaultSshKeyName")
    DefaultSubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#defaultsubnet""", alias="DefaultSubnetId")
    EcsClusterArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-ecsclusterarn""", alias="EcsClusterArn")
    ElasticIps_: Optional[List['ElasticIp']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-elasticips""", alias="ElasticIps")
    HostnameTheme_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-hostnametheme""", alias="HostnameTheme")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-name""", alias="Name")
    RdsDbInstances_: Optional[List['RdsDbInstance']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-rdsdbinstances""", alias="RdsDbInstances")
    ServiceRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-servicerolearn""", alias="ServiceRoleArn")
    SourceStackId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-sourcestackid""", alias="SourceStackId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-tags""", alias="Tags")
    UseCustomCookbooks_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#usecustcookbooks""", alias="UseCustomCookbooks")
    UseOpsworksSecurityGroups_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-useopsworkssecuritygroups""", alias="UseOpsworksSecurityGroups")
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-vpcid""", alias="VpcId")
    

    @property
    def tropo_type(self) -> troposphere.opsworks.Stack:
        from troposphere.opsworks import Stack as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opsworks import Stack as TropoT
        return resource_to_troposphere(self, TropoT)


class UserProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html
    Properties:
        - Name: AllowSelfManagement
        - Name: IamUserArn
        - Name: SshPublicKey
        - Name: SshUsername
    Attributes:
        - Name: SshUsername
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AllowSelfManagement_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-allowselfmanagement""", alias="AllowSelfManagement")
    IamUserArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-iamuserarn""", alias="IamUserArn")
    SshPublicKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-sshpublickey""", alias="SshPublicKey")
    SshUsername_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-sshusername""", alias="SshUsername")
    

    @property
    def tropo_type(self) -> troposphere.opsworks.UserProfile:
        from troposphere.opsworks import UserProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opsworks import UserProfile as TropoT
        return resource_to_troposphere(self, TropoT)


class Volume(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html
    Properties:
        - Name: Ec2VolumeId
        - Name: MountPoint
        - Name: Name
        - Name: StackId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Ec2VolumeId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-ec2volumeid""", alias="Ec2VolumeId")
    MountPoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-mountpoint""", alias="MountPoint")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-name""", alias="Name")
    StackId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-stackid""", alias="StackId")
    

    @property
    def tropo_type(self) -> troposphere.opsworks.Volume:
        from troposphere.opsworks import Volume as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.opsworks import Volume as TropoT
        return resource_to_troposphere(self, TropoT)

