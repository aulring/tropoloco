from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AutoStartConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostartconfiguration.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostartconfiguration.html#cfn-emrserverless-application-autostartconfiguration-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.emrserverless.AutoStartConfiguration:
        from troposphere.emrserverless import AutoStartConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoStopConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostopconfiguration.html
    Properties:
        - Name: Enabled
        - Name: IdleTimeoutMinutes
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostopconfiguration.html#cfn-emrserverless-application-autostopconfiguration-enabled""", alias="Enabled")
    IdleTimeoutMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostopconfiguration.html#cfn-emrserverless-application-autostopconfiguration-idletimeoutminutes""", alias="IdleTimeoutMinutes")
    


    @property
    def tropo_type(self) -> troposphere.emrserverless.AutoStopConfiguration:
        from troposphere.emrserverless import AutoStopConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfigurationObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-configurationobject.html
    Properties:
        - Name: Classification
        - Name: Properties
        - Name: Configurations
    
    """
    
    Classification_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-configurationobject.html#cfn-emrserverless-application-configurationobject-classification""", alias="Classification")
    Properties_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-configurationobject.html#cfn-emrserverless-application-configurationobject-properties""", alias="Properties")
    Configurations_: Optional[List['ConfigurationObject']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-configurationobject.html#cfn-emrserverless-application-configurationobject-configurations""", alias="Configurations")
    


    @property
    def tropo_type(self) -> troposphere.emrserverless.ConfigurationObject:
        from troposphere.emrserverless import ConfigurationObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImageConfigurationInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-imageconfigurationinput.html
    Properties:
        - Name: ImageUri
    
    """
    
    ImageUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-imageconfigurationinput.html#cfn-emrserverless-application-imageconfigurationinput-imageuri""", alias="ImageUri")
    


    @property
    def tropo_type(self) -> troposphere.emrserverless.ImageConfigurationInput:
        from troposphere.emrserverless import ImageConfigurationInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InitialCapacityConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfig.html
    Properties:
        - Name: WorkerConfiguration
        - Name: WorkerCount
    
    """
    
    WorkerConfiguration_: 'WorkerConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfig.html#cfn-emrserverless-application-initialcapacityconfig-workerconfiguration""", alias="WorkerConfiguration")
    WorkerCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfig.html#cfn-emrserverless-application-initialcapacityconfig-workercount""", alias="WorkerCount")
    


    @property
    def tropo_type(self) -> troposphere.emrserverless.InitialCapacityConfig:
        from troposphere.emrserverless import InitialCapacityConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InitialCapacityConfigKeyValuePair(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: 'InitialCapacityConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair.html#cfn-emrserverless-application-initialcapacityconfigkeyvaluepair-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair.html#cfn-emrserverless-application-initialcapacityconfigkeyvaluepair-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.emrserverless.InitialCapacityConfigKeyValuePair:
        from troposphere.emrserverless import InitialCapacityConfigKeyValuePair as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ManagedPersistenceMonitoringConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-managedpersistencemonitoringconfiguration.html
    Properties:
        - Name: EncryptionKeyArn
        - Name: Enabled
    
    """
    
    EncryptionKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-managedpersistencemonitoringconfiguration.html#cfn-emrserverless-application-managedpersistencemonitoringconfiguration-encryptionkeyarn""", alias="EncryptionKeyArn")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-managedpersistencemonitoringconfiguration.html#cfn-emrserverless-application-managedpersistencemonitoringconfiguration-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.emrserverless.ManagedPersistenceMonitoringConfiguration:
        from troposphere.emrserverless import ManagedPersistenceMonitoringConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MaximumAllowedResources(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html
    Properties:
        - Name: Memory
        - Name: Cpu
        - Name: Disk
    
    """
    
    Memory_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html#cfn-emrserverless-application-maximumallowedresources-memory""", alias="Memory")
    Cpu_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html#cfn-emrserverless-application-maximumallowedresources-cpu""", alias="Cpu")
    Disk_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html#cfn-emrserverless-application-maximumallowedresources-disk""", alias="Disk")
    


    @property
    def tropo_type(self) -> troposphere.emrserverless.MaximumAllowedResources:
        from troposphere.emrserverless import MaximumAllowedResources as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-monitoringconfiguration.html
    Properties:
        - Name: S3MonitoringConfiguration
        - Name: ManagedPersistenceMonitoringConfiguration
    
    """
    
    S3MonitoringConfiguration_: Optional['S3MonitoringConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-monitoringconfiguration.html#cfn-emrserverless-application-monitoringconfiguration-s3monitoringconfiguration""", alias="S3MonitoringConfiguration")
    ManagedPersistenceMonitoringConfiguration_: Optional['ManagedPersistenceMonitoringConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-monitoringconfiguration.html#cfn-emrserverless-application-monitoringconfiguration-managedpersistencemonitoringconfiguration""", alias="ManagedPersistenceMonitoringConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.emrserverless.MonitoringConfiguration:
        from troposphere.emrserverless import MonitoringConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-networkconfiguration.html
    Properties:
        - Name: SubnetIds
        - Name: SecurityGroupIds
    
    """
    
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-networkconfiguration.html#cfn-emrserverless-application-networkconfiguration-subnetids""", alias="SubnetIds")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-networkconfiguration.html#cfn-emrserverless-application-networkconfiguration-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.emrserverless.NetworkConfiguration:
        from troposphere.emrserverless import NetworkConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3MonitoringConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-s3monitoringconfiguration.html
    Properties:
        - Name: LogUri
        - Name: EncryptionKeyArn
    
    """
    
    LogUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-s3monitoringconfiguration.html#cfn-emrserverless-application-s3monitoringconfiguration-loguri""", alias="LogUri")
    EncryptionKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-s3monitoringconfiguration.html#cfn-emrserverless-application-s3monitoringconfiguration-encryptionkeyarn""", alias="EncryptionKeyArn")
    


    @property
    def tropo_type(self) -> troposphere.emrserverless.S3MonitoringConfiguration:
        from troposphere.emrserverless import S3MonitoringConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WorkerConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html
    Properties:
        - Name: Memory
        - Name: Cpu
        - Name: Disk
    
    """
    
    Memory_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html#cfn-emrserverless-application-workerconfiguration-memory""", alias="Memory")
    Cpu_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html#cfn-emrserverless-application-workerconfiguration-cpu""", alias="Cpu")
    Disk_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html#cfn-emrserverless-application-workerconfiguration-disk""", alias="Disk")
    


    @property
    def tropo_type(self) -> troposphere.emrserverless.WorkerConfiguration:
        from troposphere.emrserverless import WorkerConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WorkerTypeSpecificationInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workertypespecificationinput.html
    Properties:
        - Name: ImageConfiguration
    
    """
    
    ImageConfiguration_: Optional['ImageConfigurationInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workertypespecificationinput.html#cfn-emrserverless-application-workertypespecificationinput-imageconfiguration""", alias="ImageConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.emrserverless.WorkerTypeSpecificationInput:
        from troposphere.emrserverless import WorkerTypeSpecificationInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Application(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html
    Properties:
        - Name: AutoStartConfiguration
        - Name: Architecture
        - Name: WorkerTypeSpecifications
        - Name: MonitoringConfiguration
        - Name: MaximumCapacity
        - Name: AutoStopConfiguration
        - Name: RuntimeConfiguration
        - Name: Name
        - Name: Type
        - Name: InitialCapacity
        - Name: ImageConfiguration
        - Name: NetworkConfiguration
        - Name: ReleaseLabel
        - Name: Tags
    Attributes:
        - Name: Arn
        - Name: ApplicationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AutoStartConfiguration_: Optional['AutoStartConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-autostartconfiguration""", alias="AutoStartConfiguration")
    Architecture_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-architecture""", alias="Architecture")
    WorkerTypeSpecifications_: Optional[Dict[str, 'WorkerTypeSpecificationInput']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-workertypespecifications""", alias="WorkerTypeSpecifications")
    MonitoringConfiguration_: Optional['MonitoringConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-monitoringconfiguration""", alias="MonitoringConfiguration")
    MaximumCapacity_: Optional['MaximumAllowedResources'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-maximumcapacity""", alias="MaximumCapacity")
    AutoStopConfiguration_: Optional['AutoStopConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-autostopconfiguration""", alias="AutoStopConfiguration")
    RuntimeConfiguration_: Optional[List['ConfigurationObject']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-runtimeconfiguration""", alias="RuntimeConfiguration")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-name""", alias="Name")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-type""", alias="Type")
    InitialCapacity_: Optional[List['InitialCapacityConfigKeyValuePair']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-initialcapacity""", alias="InitialCapacity")
    ImageConfiguration_: Optional['ImageConfigurationInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-imageconfiguration""", alias="ImageConfiguration")
    NetworkConfiguration_: Optional['NetworkConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-networkconfiguration""", alias="NetworkConfiguration")
    ReleaseLabel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-releaselabel""", alias="ReleaseLabel")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html#cfn-emrserverless-application-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.emrserverless.Application:
        from troposphere.emrserverless import Application as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.emrserverless import Application as TropoT
        return resource_to_troposphere(self, TropoT)

