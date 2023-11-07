from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Connector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html
    Properties:
        - Name: ConnectorArn
        - Name: Parameters
        - Name: Id
    
    """
    
    ConnectorArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html#cfn-greengrass-connectordefinition-connector-connectorarn""", alias="ConnectorArn")
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html#cfn-greengrass-connectordefinition-connector-parameters""", alias="Parameters")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html#cfn-greengrass-connectordefinition-connector-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Connector:
        from troposphere.greengrass import Connector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectorDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connectordefinitionversion.html
    Properties:
        - Name: Connectors
    
    """
    
    Connectors_: List['Connector'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connectordefinitionversion.html#cfn-greengrass-connectordefinition-connectordefinitionversion-connectors""", alias="Connectors")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.ConnectorDefinitionVersion:
        from troposphere.greengrass import ConnectorDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Connector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html
    Properties:
        - Name: ConnectorArn
        - Name: Parameters
        - Name: Id
    
    """
    
    ConnectorArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html#cfn-greengrass-connectordefinitionversion-connector-connectorarn""", alias="ConnectorArn")
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html#cfn-greengrass-connectordefinitionversion-connector-parameters""", alias="Parameters")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html#cfn-greengrass-connectordefinitionversion-connector-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Connector:
        from troposphere.greengrass import Connector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Core(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html
    Properties:
        - Name: SyncShadow
        - Name: ThingArn
        - Name: Id
        - Name: CertificateArn
    
    """
    
    SyncShadow_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-syncshadow""", alias="SyncShadow")
    ThingArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-thingarn""", alias="ThingArn")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-id""", alias="Id")
    CertificateArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-certificatearn""", alias="CertificateArn")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Core:
        from troposphere.greengrass import Core as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CoreDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-coredefinitionversion.html
    Properties:
        - Name: Cores
    
    """
    
    Cores_: List['Core'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-coredefinitionversion.html#cfn-greengrass-coredefinition-coredefinitionversion-cores""", alias="Cores")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.CoreDefinitionVersion:
        from troposphere.greengrass import CoreDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Core(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html
    Properties:
        - Name: SyncShadow
        - Name: ThingArn
        - Name: Id
        - Name: CertificateArn
    
    """
    
    SyncShadow_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-syncshadow""", alias="SyncShadow")
    ThingArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-thingarn""", alias="ThingArn")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-id""", alias="Id")
    CertificateArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-certificatearn""", alias="CertificateArn")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Core:
        from troposphere.greengrass import Core as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Device(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html
    Properties:
        - Name: SyncShadow
        - Name: ThingArn
        - Name: Id
        - Name: CertificateArn
    
    """
    
    SyncShadow_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-syncshadow""", alias="SyncShadow")
    ThingArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-thingarn""", alias="ThingArn")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-id""", alias="Id")
    CertificateArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-certificatearn""", alias="CertificateArn")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Device:
        from troposphere.greengrass import Device as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeviceDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-devicedefinitionversion.html
    Properties:
        - Name: Devices
    
    """
    
    Devices_: List['Device'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-devicedefinitionversion.html#cfn-greengrass-devicedefinition-devicedefinitionversion-devices""", alias="Devices")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.DeviceDefinitionVersion:
        from troposphere.greengrass import DeviceDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Device(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html
    Properties:
        - Name: SyncShadow
        - Name: ThingArn
        - Name: Id
        - Name: CertificateArn
    
    """
    
    SyncShadow_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-syncshadow""", alias="SyncShadow")
    ThingArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-thingarn""", alias="ThingArn")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-id""", alias="Id")
    CertificateArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-certificatearn""", alias="CertificateArn")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Device:
        from troposphere.greengrass import Device as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefaultConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-defaultconfig.html
    Properties:
        - Name: Execution
    
    """
    
    Execution_: 'Execution' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-defaultconfig.html#cfn-greengrass-functiondefinition-defaultconfig-execution""", alias="Execution")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.DefaultConfig:
        from troposphere.greengrass import DefaultConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Environment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html
    Properties:
        - Name: Variables
        - Name: Execution
        - Name: ResourceAccessPolicies
        - Name: AccessSysfs
    
    """
    
    Variables_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-variables""", alias="Variables")
    Execution_: Optional['Execution'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-execution""", alias="Execution")
    ResourceAccessPolicies_: Optional[List['ResourceAccessPolicy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-resourceaccesspolicies""", alias="ResourceAccessPolicies")
    AccessSysfs_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-accesssysfs""", alias="AccessSysfs")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Environment:
        from troposphere.greengrass import Environment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Execution(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html
    Properties:
        - Name: IsolationMode
        - Name: RunAs
    
    """
    
    IsolationMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html#cfn-greengrass-functiondefinition-execution-isolationmode""", alias="IsolationMode")
    RunAs_: Optional['RunAs'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html#cfn-greengrass-functiondefinition-execution-runas""", alias="RunAs")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Execution:
        from troposphere.greengrass import Execution as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Function(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html
    Properties:
        - Name: FunctionArn
        - Name: FunctionConfiguration
        - Name: Id
    
    """
    
    FunctionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html#cfn-greengrass-functiondefinition-function-functionarn""", alias="FunctionArn")
    FunctionConfiguration_: 'FunctionConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html#cfn-greengrass-functiondefinition-function-functionconfiguration""", alias="FunctionConfiguration")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html#cfn-greengrass-functiondefinition-function-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Function:
        from troposphere.greengrass import Function as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FunctionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html
    Properties:
        - Name: MemorySize
        - Name: Pinned
        - Name: ExecArgs
        - Name: Timeout
        - Name: EncodingType
        - Name: Environment
        - Name: Executable
    
    """
    
    MemorySize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-memorysize""", alias="MemorySize")
    Pinned_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-pinned""", alias="Pinned")
    ExecArgs_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-execargs""", alias="ExecArgs")
    Timeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-timeout""", alias="Timeout")
    EncodingType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-encodingtype""", alias="EncodingType")
    Environment_: Optional['Environment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-environment""", alias="Environment")
    Executable_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-executable""", alias="Executable")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.FunctionConfiguration:
        from troposphere.greengrass import FunctionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FunctionDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html
    Properties:
        - Name: DefaultConfig
        - Name: Functions
    
    """
    
    DefaultConfig_: Optional['DefaultConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html#cfn-greengrass-functiondefinition-functiondefinitionversion-defaultconfig""", alias="DefaultConfig")
    Functions_: List['Function'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html#cfn-greengrass-functiondefinition-functiondefinitionversion-functions""", alias="Functions")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.FunctionDefinitionVersion:
        from troposphere.greengrass import FunctionDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceAccessPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html
    Properties:
        - Name: ResourceId
        - Name: Permission
    
    """
    
    ResourceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html#cfn-greengrass-functiondefinition-resourceaccesspolicy-resourceid""", alias="ResourceId")
    Permission_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html#cfn-greengrass-functiondefinition-resourceaccesspolicy-permission""", alias="Permission")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.ResourceAccessPolicy:
        from troposphere.greengrass import ResourceAccessPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RunAs(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-runas.html
    Properties:
        - Name: Uid
        - Name: Gid
    
    """
    
    Uid_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-runas.html#cfn-greengrass-functiondefinition-runas-uid""", alias="Uid")
    Gid_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-runas.html#cfn-greengrass-functiondefinition-runas-gid""", alias="Gid")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.RunAs:
        from troposphere.greengrass import RunAs as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefaultConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html
    Properties:
        - Name: Execution
    
    """
    
    Execution_: 'Execution' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html#cfn-greengrass-functiondefinitionversion-defaultconfig-execution""", alias="Execution")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.DefaultConfig:
        from troposphere.greengrass import DefaultConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Environment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html
    Properties:
        - Name: Variables
        - Name: Execution
        - Name: ResourceAccessPolicies
        - Name: AccessSysfs
    
    """
    
    Variables_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-variables""", alias="Variables")
    Execution_: Optional['Execution'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-execution""", alias="Execution")
    ResourceAccessPolicies_: Optional[List['ResourceAccessPolicy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-resourceaccesspolicies""", alias="ResourceAccessPolicies")
    AccessSysfs_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-accesssysfs""", alias="AccessSysfs")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Environment:
        from troposphere.greengrass import Environment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Execution(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html
    Properties:
        - Name: IsolationMode
        - Name: RunAs
    
    """
    
    IsolationMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html#cfn-greengrass-functiondefinitionversion-execution-isolationmode""", alias="IsolationMode")
    RunAs_: Optional['RunAs'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html#cfn-greengrass-functiondefinitionversion-execution-runas""", alias="RunAs")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Execution:
        from troposphere.greengrass import Execution as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Function(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html
    Properties:
        - Name: FunctionArn
        - Name: FunctionConfiguration
        - Name: Id
    
    """
    
    FunctionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html#cfn-greengrass-functiondefinitionversion-function-functionarn""", alias="FunctionArn")
    FunctionConfiguration_: 'FunctionConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html#cfn-greengrass-functiondefinitionversion-function-functionconfiguration""", alias="FunctionConfiguration")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html#cfn-greengrass-functiondefinitionversion-function-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Function:
        from troposphere.greengrass import Function as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FunctionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html
    Properties:
        - Name: MemorySize
        - Name: Pinned
        - Name: ExecArgs
        - Name: Timeout
        - Name: EncodingType
        - Name: Environment
        - Name: Executable
    
    """
    
    MemorySize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-memorysize""", alias="MemorySize")
    Pinned_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-pinned""", alias="Pinned")
    ExecArgs_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-execargs""", alias="ExecArgs")
    Timeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-timeout""", alias="Timeout")
    EncodingType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-encodingtype""", alias="EncodingType")
    Environment_: Optional['Environment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-environment""", alias="Environment")
    Executable_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-executable""", alias="Executable")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.FunctionConfiguration:
        from troposphere.greengrass import FunctionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceAccessPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-resourceaccesspolicy.html
    Properties:
        - Name: ResourceId
        - Name: Permission
    
    """
    
    ResourceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-resourceaccesspolicy.html#cfn-greengrass-functiondefinitionversion-resourceaccesspolicy-resourceid""", alias="ResourceId")
    Permission_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-resourceaccesspolicy.html#cfn-greengrass-functiondefinitionversion-resourceaccesspolicy-permission""", alias="Permission")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.ResourceAccessPolicy:
        from troposphere.greengrass import ResourceAccessPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RunAs(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-runas.html
    Properties:
        - Name: Uid
        - Name: Gid
    
    """
    
    Uid_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-runas.html#cfn-greengrass-functiondefinitionversion-runas-uid""", alias="Uid")
    Gid_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-runas.html#cfn-greengrass-functiondefinitionversion-runas-gid""", alias="Gid")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.RunAs:
        from troposphere.greengrass import RunAs as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GroupVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html
    Properties:
        - Name: LoggerDefinitionVersionArn
        - Name: DeviceDefinitionVersionArn
        - Name: FunctionDefinitionVersionArn
        - Name: CoreDefinitionVersionArn
        - Name: ResourceDefinitionVersionArn
        - Name: ConnectorDefinitionVersionArn
        - Name: SubscriptionDefinitionVersionArn
    
    """
    
    LoggerDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-loggerdefinitionversionarn""", alias="LoggerDefinitionVersionArn")
    DeviceDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-devicedefinitionversionarn""", alias="DeviceDefinitionVersionArn")
    FunctionDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-functiondefinitionversionarn""", alias="FunctionDefinitionVersionArn")
    CoreDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-coredefinitionversionarn""", alias="CoreDefinitionVersionArn")
    ResourceDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-resourcedefinitionversionarn""", alias="ResourceDefinitionVersionArn")
    ConnectorDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-connectordefinitionversionarn""", alias="ConnectorDefinitionVersionArn")
    SubscriptionDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-subscriptiondefinitionversionarn""", alias="SubscriptionDefinitionVersionArn")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.GroupVersion:
        from troposphere.greengrass import GroupVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Logger(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html
    Properties:
        - Name: Space
        - Name: Type
        - Name: Level
        - Name: Id
        - Name: Component
    
    """
    
    Space_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-space""", alias="Space")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-type""", alias="Type")
    Level_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-level""", alias="Level")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-id""", alias="Id")
    Component_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-component""", alias="Component")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Logger:
        from troposphere.greengrass import Logger as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggerDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-loggerdefinitionversion.html
    Properties:
        - Name: Loggers
    
    """
    
    Loggers_: List['Logger'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-loggerdefinitionversion.html#cfn-greengrass-loggerdefinition-loggerdefinitionversion-loggers""", alias="Loggers")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.LoggerDefinitionVersion:
        from troposphere.greengrass import LoggerDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Logger(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html
    Properties:
        - Name: Space
        - Name: Type
        - Name: Level
        - Name: Id
        - Name: Component
    
    """
    
    Space_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-space""", alias="Space")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-type""", alias="Type")
    Level_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-level""", alias="Level")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-id""", alias="Id")
    Component_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-component""", alias="Component")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Logger:
        from troposphere.greengrass import Logger as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GroupOwnerSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-groupownersetting.html
    Properties:
        - Name: AutoAddGroupOwner
        - Name: GroupOwner
    
    """
    
    AutoAddGroupOwner_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-groupownersetting.html#cfn-greengrass-resourcedefinition-groupownersetting-autoaddgroupowner""", alias="AutoAddGroupOwner")
    GroupOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-groupownersetting.html#cfn-greengrass-resourcedefinition-groupownersetting-groupowner""", alias="GroupOwner")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.GroupOwnerSetting:
        from troposphere.greengrass import GroupOwnerSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LocalDeviceResourceData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html
    Properties:
        - Name: SourcePath
        - Name: GroupOwnerSetting
    
    """
    
    SourcePath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html#cfn-greengrass-resourcedefinition-localdeviceresourcedata-sourcepath""", alias="SourcePath")
    GroupOwnerSetting_: Optional['GroupOwnerSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html#cfn-greengrass-resourcedefinition-localdeviceresourcedata-groupownersetting""", alias="GroupOwnerSetting")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.LocalDeviceResourceData:
        from troposphere.greengrass import LocalDeviceResourceData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LocalVolumeResourceData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html
    Properties:
        - Name: SourcePath
        - Name: DestinationPath
        - Name: GroupOwnerSetting
    
    """
    
    SourcePath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html#cfn-greengrass-resourcedefinition-localvolumeresourcedata-sourcepath""", alias="SourcePath")
    DestinationPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html#cfn-greengrass-resourcedefinition-localvolumeresourcedata-destinationpath""", alias="DestinationPath")
    GroupOwnerSetting_: Optional['GroupOwnerSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html#cfn-greengrass-resourcedefinition-localvolumeresourcedata-groupownersetting""", alias="GroupOwnerSetting")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.LocalVolumeResourceData:
        from troposphere.greengrass import LocalVolumeResourceData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceDataContainer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html
    Properties:
        - Name: SecretsManagerSecretResourceData
        - Name: SageMakerMachineLearningModelResourceData
        - Name: LocalVolumeResourceData
        - Name: LocalDeviceResourceData
        - Name: S3MachineLearningModelResourceData
    
    """
    
    SecretsManagerSecretResourceData_: Optional['SecretsManagerSecretResourceData'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-secretsmanagersecretresourcedata""", alias="SecretsManagerSecretResourceData")
    SageMakerMachineLearningModelResourceData_: Optional['SageMakerMachineLearningModelResourceData'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-sagemakermachinelearningmodelresourcedata""", alias="SageMakerMachineLearningModelResourceData")
    LocalVolumeResourceData_: Optional['LocalVolumeResourceData'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-localvolumeresourcedata""", alias="LocalVolumeResourceData")
    LocalDeviceResourceData_: Optional['LocalDeviceResourceData'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-localdeviceresourcedata""", alias="LocalDeviceResourceData")
    S3MachineLearningModelResourceData_: Optional['S3MachineLearningModelResourceData'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-s3machinelearningmodelresourcedata""", alias="S3MachineLearningModelResourceData")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.ResourceDataContainer:
        from troposphere.greengrass import ResourceDataContainer as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedefinitionversion.html
    Properties:
        - Name: Resources
    
    """
    
    Resources_: List['ResourceInstance'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedefinitionversion.html#cfn-greengrass-resourcedefinition-resourcedefinitionversion-resources""", alias="Resources")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.ResourceDefinitionVersion:
        from troposphere.greengrass import ResourceDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceDownloadOwnerSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.html
    Properties:
        - Name: GroupOwner
        - Name: GroupPermission
    
    """
    
    GroupOwner_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinition-resourcedownloadownersetting-groupowner""", alias="GroupOwner")
    GroupPermission_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinition-resourcedownloadownersetting-grouppermission""", alias="GroupPermission")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.ResourceDownloadOwnerSetting:
        from troposphere.greengrass import ResourceDownloadOwnerSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceInstance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html
    Properties:
        - Name: ResourceDataContainer
        - Name: Id
        - Name: Name
    
    """
    
    ResourceDataContainer_: 'ResourceDataContainer' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html#cfn-greengrass-resourcedefinition-resourceinstance-resourcedatacontainer""", alias="ResourceDataContainer")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html#cfn-greengrass-resourcedefinition-resourceinstance-id""", alias="Id")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html#cfn-greengrass-resourcedefinition-resourceinstance-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.ResourceInstance:
        from troposphere.greengrass import ResourceInstance as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3MachineLearningModelResourceData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html
    Properties:
        - Name: OwnerSetting
        - Name: DestinationPath
        - Name: S3Uri
    
    """
    
    OwnerSetting_: Optional['ResourceDownloadOwnerSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-ownersetting""", alias="OwnerSetting")
    DestinationPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-destinationpath""", alias="DestinationPath")
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-s3uri""", alias="S3Uri")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.S3MachineLearningModelResourceData:
        from troposphere.greengrass import S3MachineLearningModelResourceData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SageMakerMachineLearningModelResourceData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html
    Properties:
        - Name: OwnerSetting
        - Name: DestinationPath
        - Name: SageMakerJobArn
    
    """
    
    OwnerSetting_: Optional['ResourceDownloadOwnerSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata-ownersetting""", alias="OwnerSetting")
    DestinationPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata-destinationpath""", alias="DestinationPath")
    SageMakerJobArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata-sagemakerjobarn""", alias="SageMakerJobArn")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.SageMakerMachineLearningModelResourceData:
        from troposphere.greengrass import SageMakerMachineLearningModelResourceData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SecretsManagerSecretResourceData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-secretsmanagersecretresourcedata.html
    Properties:
        - Name: ARN
        - Name: AdditionalStagingLabelsToDownload
    
    """
    
    ARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinition-secretsmanagersecretresourcedata-arn""", alias="ARN")
    AdditionalStagingLabelsToDownload_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinition-secretsmanagersecretresourcedata-additionalstaginglabelstodownload""", alias="AdditionalStagingLabelsToDownload")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.SecretsManagerSecretResourceData:
        from troposphere.greengrass import SecretsManagerSecretResourceData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GroupOwnerSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html
    Properties:
        - Name: AutoAddGroupOwner
        - Name: GroupOwner
    
    """
    
    AutoAddGroupOwner_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html#cfn-greengrass-resourcedefinitionversion-groupownersetting-autoaddgroupowner""", alias="AutoAddGroupOwner")
    GroupOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html#cfn-greengrass-resourcedefinitionversion-groupownersetting-groupowner""", alias="GroupOwner")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.GroupOwnerSetting:
        from troposphere.greengrass import GroupOwnerSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LocalDeviceResourceData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html
    Properties:
        - Name: SourcePath
        - Name: GroupOwnerSetting
    
    """
    
    SourcePath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html#cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-sourcepath""", alias="SourcePath")
    GroupOwnerSetting_: Optional['GroupOwnerSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html#cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-groupownersetting""", alias="GroupOwnerSetting")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.LocalDeviceResourceData:
        from troposphere.greengrass import LocalDeviceResourceData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LocalVolumeResourceData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html
    Properties:
        - Name: SourcePath
        - Name: DestinationPath
        - Name: GroupOwnerSetting
    
    """
    
    SourcePath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html#cfn-greengrass-resourcedefinitionversion-localvolumeresourcedata-sourcepath""", alias="SourcePath")
    DestinationPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html#cfn-greengrass-resourcedefinitionversion-localvolumeresourcedata-destinationpath""", alias="DestinationPath")
    GroupOwnerSetting_: Optional['GroupOwnerSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html#cfn-greengrass-resourcedefinitionversion-localvolumeresourcedata-groupownersetting""", alias="GroupOwnerSetting")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.LocalVolumeResourceData:
        from troposphere.greengrass import LocalVolumeResourceData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceDataContainer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html
    Properties:
        - Name: SecretsManagerSecretResourceData
        - Name: SageMakerMachineLearningModelResourceData
        - Name: LocalVolumeResourceData
        - Name: LocalDeviceResourceData
        - Name: S3MachineLearningModelResourceData
    
    """
    
    SecretsManagerSecretResourceData_: Optional['SecretsManagerSecretResourceData'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-secretsmanagersecretresourcedata""", alias="SecretsManagerSecretResourceData")
    SageMakerMachineLearningModelResourceData_: Optional['SageMakerMachineLearningModelResourceData'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-sagemakermachinelearningmodelresourcedata""", alias="SageMakerMachineLearningModelResourceData")
    LocalVolumeResourceData_: Optional['LocalVolumeResourceData'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localvolumeresourcedata""", alias="LocalVolumeResourceData")
    LocalDeviceResourceData_: Optional['LocalDeviceResourceData'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localdeviceresourcedata""", alias="LocalDeviceResourceData")
    S3MachineLearningModelResourceData_: Optional['S3MachineLearningModelResourceData'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-s3machinelearningmodelresourcedata""", alias="S3MachineLearningModelResourceData")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.ResourceDataContainer:
        from troposphere.greengrass import ResourceDataContainer as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceDownloadOwnerSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedownloadownersetting.html
    Properties:
        - Name: GroupOwner
        - Name: GroupPermission
    
    """
    
    GroupOwner_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinitionversion-resourcedownloadownersetting-groupowner""", alias="GroupOwner")
    GroupPermission_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinitionversion-resourcedownloadownersetting-grouppermission""", alias="GroupPermission")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.ResourceDownloadOwnerSetting:
        from troposphere.greengrass import ResourceDownloadOwnerSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceInstance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html
    Properties:
        - Name: ResourceDataContainer
        - Name: Id
        - Name: Name
    
    """
    
    ResourceDataContainer_: 'ResourceDataContainer' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html#cfn-greengrass-resourcedefinitionversion-resourceinstance-resourcedatacontainer""", alias="ResourceDataContainer")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html#cfn-greengrass-resourcedefinitionversion-resourceinstance-id""", alias="Id")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html#cfn-greengrass-resourcedefinitionversion-resourceinstance-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.ResourceInstance:
        from troposphere.greengrass import ResourceInstance as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3MachineLearningModelResourceData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html
    Properties:
        - Name: OwnerSetting
        - Name: DestinationPath
        - Name: S3Uri
    
    """
    
    OwnerSetting_: Optional['ResourceDownloadOwnerSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata-ownersetting""", alias="OwnerSetting")
    DestinationPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata-destinationpath""", alias="DestinationPath")
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata-s3uri""", alias="S3Uri")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.S3MachineLearningModelResourceData:
        from troposphere.greengrass import S3MachineLearningModelResourceData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SageMakerMachineLearningModelResourceData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html
    Properties:
        - Name: OwnerSetting
        - Name: DestinationPath
        - Name: SageMakerJobArn
    
    """
    
    OwnerSetting_: Optional['ResourceDownloadOwnerSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata-ownersetting""", alias="OwnerSetting")
    DestinationPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata-destinationpath""", alias="DestinationPath")
    SageMakerJobArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata-sagemakerjobarn""", alias="SageMakerJobArn")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.SageMakerMachineLearningModelResourceData:
        from troposphere.greengrass import SageMakerMachineLearningModelResourceData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SecretsManagerSecretResourceData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html
    Properties:
        - Name: ARN
        - Name: AdditionalStagingLabelsToDownload
    
    """
    
    ARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-arn""", alias="ARN")
    AdditionalStagingLabelsToDownload_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-additionalstaginglabelstodownload""", alias="AdditionalStagingLabelsToDownload")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.SecretsManagerSecretResourceData:
        from troposphere.greengrass import SecretsManagerSecretResourceData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Subscription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html
    Properties:
        - Name: Target
        - Name: Id
        - Name: Source
        - Name: Subject
    
    """
    
    Target_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-target""", alias="Target")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-id""", alias="Id")
    Source_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-source""", alias="Source")
    Subject_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-subject""", alias="Subject")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Subscription:
        from troposphere.greengrass import Subscription as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SubscriptionDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion.html
    Properties:
        - Name: Subscriptions
    
    """
    
    Subscriptions_: List['Subscription'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion.html#cfn-greengrass-subscriptiondefinition-subscriptiondefinitionversion-subscriptions""", alias="Subscriptions")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.SubscriptionDefinitionVersion:
        from troposphere.greengrass import SubscriptionDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Subscription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html
    Properties:
        - Name: Target
        - Name: Id
        - Name: Source
        - Name: Subject
    
    """
    
    Target_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-target""", alias="Target")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-id""", alias="Id")
    Source_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-source""", alias="Source")
    Subject_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-subject""", alias="Subject")
    


    @property
    def tropo_type(self) -> troposphere.greengrass.Subscription:
        from troposphere.greengrass import Subscription as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ConnectorDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html
    Properties:
        - Name: InitialVersion
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LatestVersionArn
        - Name: Id
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InitialVersion_: Optional['ConnectorDefinitionVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#cfn-greengrass-connectordefinition-initialversion""", alias="InitialVersion")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#cfn-greengrass-connectordefinition-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#cfn-greengrass-connectordefinition-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.ConnectorDefinition:
        from troposphere.greengrass import ConnectorDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import ConnectorDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class ConnectorDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html
    Properties:
        - Name: Connectors
        - Name: ConnectorDefinitionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Connectors_: List['Connector'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html#cfn-greengrass-connectordefinitionversion-connectors""", alias="Connectors")
    ConnectorDefinitionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html#cfn-greengrass-connectordefinitionversion-connectordefinitionid""", alias="ConnectorDefinitionId")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.ConnectorDefinitionVersion:
        from troposphere.greengrass import ConnectorDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import ConnectorDefinitionVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class CoreDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html
    Properties:
        - Name: InitialVersion
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LatestVersionArn
        - Name: Id
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InitialVersion_: Optional['CoreDefinitionVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#cfn-greengrass-coredefinition-initialversion""", alias="InitialVersion")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#cfn-greengrass-coredefinition-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#cfn-greengrass-coredefinition-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.CoreDefinition:
        from troposphere.greengrass import CoreDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import CoreDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class CoreDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html
    Properties:
        - Name: Cores
        - Name: CoreDefinitionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Cores_: List['Core'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html#cfn-greengrass-coredefinitionversion-cores""", alias="Cores")
    CoreDefinitionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html#cfn-greengrass-coredefinitionversion-coredefinitionid""", alias="CoreDefinitionId")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.CoreDefinitionVersion:
        from troposphere.greengrass import CoreDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import CoreDefinitionVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class DeviceDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html
    Properties:
        - Name: InitialVersion
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LatestVersionArn
        - Name: Id
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InitialVersion_: Optional['DeviceDefinitionVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#cfn-greengrass-devicedefinition-initialversion""", alias="InitialVersion")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#cfn-greengrass-devicedefinition-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#cfn-greengrass-devicedefinition-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.DeviceDefinition:
        from troposphere.greengrass import DeviceDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import DeviceDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class DeviceDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html
    Properties:
        - Name: DeviceDefinitionId
        - Name: Devices
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DeviceDefinitionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html#cfn-greengrass-devicedefinitionversion-devicedefinitionid""", alias="DeviceDefinitionId")
    Devices_: List['Device'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html#cfn-greengrass-devicedefinitionversion-devices""", alias="Devices")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.DeviceDefinitionVersion:
        from troposphere.greengrass import DeviceDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import DeviceDefinitionVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class FunctionDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html
    Properties:
        - Name: InitialVersion
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LatestVersionArn
        - Name: Id
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InitialVersion_: Optional['FunctionDefinitionVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#cfn-greengrass-functiondefinition-initialversion""", alias="InitialVersion")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#cfn-greengrass-functiondefinition-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#cfn-greengrass-functiondefinition-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.FunctionDefinition:
        from troposphere.greengrass import FunctionDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import FunctionDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class FunctionDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html
    Properties:
        - Name: DefaultConfig
        - Name: Functions
        - Name: FunctionDefinitionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DefaultConfig_: Optional['DefaultConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html#cfn-greengrass-functiondefinitionversion-defaultconfig""", alias="DefaultConfig")
    Functions_: List['Function'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html#cfn-greengrass-functiondefinitionversion-functions""", alias="Functions")
    FunctionDefinitionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html#cfn-greengrass-functiondefinitionversion-functiondefinitionid""", alias="FunctionDefinitionId")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.FunctionDefinitionVersion:
        from troposphere.greengrass import FunctionDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import FunctionDefinitionVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class Group(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html
    Properties:
        - Name: InitialVersion
        - Name: RoleArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: RoleAttachedAt
        - Name: LatestVersionArn
        - Name: Id
        - Name: Arn
        - Name: RoleArn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InitialVersion_: Optional['GroupVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-initialversion""", alias="InitialVersion")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-rolearn""", alias="RoleArn")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.Group:
        from troposphere.greengrass import Group as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import Group as TropoT
        return resource_to_troposphere(self, TropoT)


class GroupVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html
    Properties:
        - Name: LoggerDefinitionVersionArn
        - Name: DeviceDefinitionVersionArn
        - Name: FunctionDefinitionVersionArn
        - Name: CoreDefinitionVersionArn
        - Name: ResourceDefinitionVersionArn
        - Name: ConnectorDefinitionVersionArn
        - Name: SubscriptionDefinitionVersionArn
        - Name: GroupId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LoggerDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-loggerdefinitionversionarn""", alias="LoggerDefinitionVersionArn")
    DeviceDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-devicedefinitionversionarn""", alias="DeviceDefinitionVersionArn")
    FunctionDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-functiondefinitionversionarn""", alias="FunctionDefinitionVersionArn")
    CoreDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-coredefinitionversionarn""", alias="CoreDefinitionVersionArn")
    ResourceDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-resourcedefinitionversionarn""", alias="ResourceDefinitionVersionArn")
    ConnectorDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-connectordefinitionversionarn""", alias="ConnectorDefinitionVersionArn")
    SubscriptionDefinitionVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-subscriptiondefinitionversionarn""", alias="SubscriptionDefinitionVersionArn")
    GroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-groupid""", alias="GroupId")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.GroupVersion:
        from troposphere.greengrass import GroupVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import GroupVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class LoggerDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html
    Properties:
        - Name: InitialVersion
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LatestVersionArn
        - Name: Id
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InitialVersion_: Optional['LoggerDefinitionVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#cfn-greengrass-loggerdefinition-initialversion""", alias="InitialVersion")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#cfn-greengrass-loggerdefinition-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#cfn-greengrass-loggerdefinition-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.LoggerDefinition:
        from troposphere.greengrass import LoggerDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import LoggerDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class LoggerDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html
    Properties:
        - Name: LoggerDefinitionId
        - Name: Loggers
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LoggerDefinitionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html#cfn-greengrass-loggerdefinitionversion-loggerdefinitionid""", alias="LoggerDefinitionId")
    Loggers_: List['Logger'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html#cfn-greengrass-loggerdefinitionversion-loggers""", alias="Loggers")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.LoggerDefinitionVersion:
        from troposphere.greengrass import LoggerDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import LoggerDefinitionVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourceDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html
    Properties:
        - Name: InitialVersion
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LatestVersionArn
        - Name: Id
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InitialVersion_: Optional['ResourceDefinitionVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#cfn-greengrass-resourcedefinition-initialversion""", alias="InitialVersion")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#cfn-greengrass-resourcedefinition-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#cfn-greengrass-resourcedefinition-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.ResourceDefinition:
        from troposphere.greengrass import ResourceDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import ResourceDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourceDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html
    Properties:
        - Name: Resources
        - Name: ResourceDefinitionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Resources_: List['ResourceInstance'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html#cfn-greengrass-resourcedefinitionversion-resources""", alias="Resources")
    ResourceDefinitionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html#cfn-greengrass-resourcedefinitionversion-resourcedefinitionid""", alias="ResourceDefinitionId")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.ResourceDefinitionVersion:
        from troposphere.greengrass import ResourceDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import ResourceDefinitionVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class SubscriptionDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html
    Properties:
        - Name: InitialVersion
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LatestVersionArn
        - Name: Id
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InitialVersion_: Optional['SubscriptionDefinitionVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#cfn-greengrass-subscriptiondefinition-initialversion""", alias="InitialVersion")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#cfn-greengrass-subscriptiondefinition-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#cfn-greengrass-subscriptiondefinition-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.SubscriptionDefinition:
        from troposphere.greengrass import SubscriptionDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import SubscriptionDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class SubscriptionDefinitionVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html
    Properties:
        - Name: SubscriptionDefinitionId
        - Name: Subscriptions
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SubscriptionDefinitionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html#cfn-greengrass-subscriptiondefinitionversion-subscriptiondefinitionid""", alias="SubscriptionDefinitionId")
    Subscriptions_: List['Subscription'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html#cfn-greengrass-subscriptiondefinitionversion-subscriptions""", alias="Subscriptions")
    

    @property
    def tropo_type(self) -> troposphere.greengrass.SubscriptionDefinitionVersion:
        from troposphere.greengrass import SubscriptionDefinitionVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrass import SubscriptionDefinitionVersion as TropoT
        return resource_to_troposphere(self, TropoT)

