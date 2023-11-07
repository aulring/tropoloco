from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class TraceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-observabilityconfiguration-traceconfiguration.html
    Properties:
        - Name: Vendor
    
    """
    
    Vendor_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-observabilityconfiguration-traceconfiguration.html#cfn-apprunner-observabilityconfiguration-traceconfiguration-vendor""", alias="Vendor")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.TraceConfiguration:
        from troposphere.apprunner import TraceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuthenticationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html
    Properties:
        - Name: AccessRoleArn
        - Name: ConnectionArn
    
    """
    
    AccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-accessrolearn""", alias="AccessRoleArn")
    ConnectionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-connectionarn""", alias="ConnectionArn")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.AuthenticationConfiguration:
        from troposphere.apprunner import AuthenticationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CodeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html
    Properties:
        - Name: ConfigurationSource
        - Name: CodeConfigurationValues
    
    """
    
    ConfigurationSource_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-configurationsource""", alias="ConfigurationSource")
    CodeConfigurationValues_: Optional['CodeConfigurationValues'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-codeconfigurationvalues""", alias="CodeConfigurationValues")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.CodeConfiguration:
        from troposphere.apprunner import CodeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CodeConfigurationValues(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html
    Properties:
        - Name: RuntimeEnvironmentSecrets
        - Name: Runtime
        - Name: StartCommand
        - Name: RuntimeEnvironmentVariables
        - Name: Port
        - Name: BuildCommand
    
    """
    
    RuntimeEnvironmentSecrets_: Optional[List['KeyValuePair']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtimeenvironmentsecrets""", alias="RuntimeEnvironmentSecrets")
    Runtime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtime""", alias="Runtime")
    StartCommand_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-startcommand""", alias="StartCommand")
    RuntimeEnvironmentVariables_: Optional[List['KeyValuePair']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtimeenvironmentvariables""", alias="RuntimeEnvironmentVariables")
    Port_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-port""", alias="Port")
    BuildCommand_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-buildcommand""", alias="BuildCommand")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.CodeConfigurationValues:
        from troposphere.apprunner import CodeConfigurationValues as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CodeRepository(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html
    Properties:
        - Name: SourceCodeVersion
        - Name: CodeConfiguration
        - Name: SourceDirectory
        - Name: RepositoryUrl
    
    """
    
    SourceCodeVersion_: 'SourceCodeVersion' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-sourcecodeversion""", alias="SourceCodeVersion")
    CodeConfiguration_: Optional['CodeConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-codeconfiguration""", alias="CodeConfiguration")
    SourceDirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-sourcedirectory""", alias="SourceDirectory")
    RepositoryUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-repositoryurl""", alias="RepositoryUrl")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.CodeRepository:
        from troposphere.apprunner import CodeRepository as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EgressConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html
    Properties:
        - Name: VpcConnectorArn
        - Name: EgressType
    
    """
    
    VpcConnectorArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html#cfn-apprunner-service-egressconfiguration-vpcconnectorarn""", alias="VpcConnectorArn")
    EgressType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html#cfn-apprunner-service-egressconfiguration-egresstype""", alias="EgressType")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.EgressConfiguration:
        from troposphere.apprunner import EgressConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html
    Properties:
        - Name: KmsKey
    
    """
    
    KmsKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html#cfn-apprunner-service-encryptionconfiguration-kmskey""", alias="KmsKey")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.EncryptionConfiguration:
        from troposphere.apprunner import EncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HealthCheckConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html
    Properties:
        - Name: Path
        - Name: UnhealthyThreshold
        - Name: Timeout
        - Name: HealthyThreshold
        - Name: Protocol
        - Name: Interval
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-path""", alias="Path")
    UnhealthyThreshold_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-unhealthythreshold""", alias="UnhealthyThreshold")
    Timeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-timeout""", alias="Timeout")
    HealthyThreshold_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-healthythreshold""", alias="HealthyThreshold")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-protocol""", alias="Protocol")
    Interval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-interval""", alias="Interval")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.HealthCheckConfiguration:
        from troposphere.apprunner import HealthCheckConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImageConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html
    Properties:
        - Name: RuntimeEnvironmentSecrets
        - Name: StartCommand
        - Name: RuntimeEnvironmentVariables
        - Name: Port
    
    """
    
    RuntimeEnvironmentSecrets_: Optional[List['KeyValuePair']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-runtimeenvironmentsecrets""", alias="RuntimeEnvironmentSecrets")
    StartCommand_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-startcommand""", alias="StartCommand")
    RuntimeEnvironmentVariables_: Optional[List['KeyValuePair']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-runtimeenvironmentvariables""", alias="RuntimeEnvironmentVariables")
    Port_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-port""", alias="Port")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.ImageConfiguration:
        from troposphere.apprunner import ImageConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImageRepository(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html
    Properties:
        - Name: ImageIdentifier
        - Name: ImageConfiguration
        - Name: ImageRepositoryType
    
    """
    
    ImageIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageidentifier""", alias="ImageIdentifier")
    ImageConfiguration_: Optional['ImageConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageconfiguration""", alias="ImageConfiguration")
    ImageRepositoryType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imagerepositorytype""", alias="ImageRepositoryType")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.ImageRepository:
        from troposphere.apprunner import ImageRepository as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IngressConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-ingressconfiguration.html
    Properties:
        - Name: IsPubliclyAccessible
    
    """
    
    IsPubliclyAccessible_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-ingressconfiguration.html#cfn-apprunner-service-ingressconfiguration-ispubliclyaccessible""", alias="IsPubliclyAccessible")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.IngressConfiguration:
        from troposphere.apprunner import IngressConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html
    Properties:
        - Name: InstanceRoleArn
        - Name: Memory
        - Name: Cpu
    
    """
    
    InstanceRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-instancerolearn""", alias="InstanceRoleArn")
    Memory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-memory""", alias="Memory")
    Cpu_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-cpu""", alias="Cpu")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.InstanceConfiguration:
        from troposphere.apprunner import InstanceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeyValuePair(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-value""", alias="Value")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.KeyValuePair:
        from troposphere.apprunner import KeyValuePair as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html
    Properties:
        - Name: IpAddressType
        - Name: EgressConfiguration
        - Name: IngressConfiguration
    
    """
    
    IpAddressType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html#cfn-apprunner-service-networkconfiguration-ipaddresstype""", alias="IpAddressType")
    EgressConfiguration_: Optional['EgressConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html#cfn-apprunner-service-networkconfiguration-egressconfiguration""", alias="EgressConfiguration")
    IngressConfiguration_: Optional['IngressConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html#cfn-apprunner-service-networkconfiguration-ingressconfiguration""", alias="IngressConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.NetworkConfiguration:
        from troposphere.apprunner import NetworkConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceObservabilityConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html
    Properties:
        - Name: ObservabilityEnabled
        - Name: ObservabilityConfigurationArn
    
    """
    
    ObservabilityEnabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html#cfn-apprunner-service-serviceobservabilityconfiguration-observabilityenabled""", alias="ObservabilityEnabled")
    ObservabilityConfigurationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html#cfn-apprunner-service-serviceobservabilityconfiguration-observabilityconfigurationarn""", alias="ObservabilityConfigurationArn")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.ServiceObservabilityConfiguration:
        from troposphere.apprunner import ServiceObservabilityConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceCodeVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-type""", alias="Type")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.SourceCodeVersion:
        from troposphere.apprunner import SourceCodeVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html
    Properties:
        - Name: AuthenticationConfiguration
        - Name: CodeRepository
        - Name: ImageRepository
        - Name: AutoDeploymentsEnabled
    
    """
    
    AuthenticationConfiguration_: Optional['AuthenticationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-authenticationconfiguration""", alias="AuthenticationConfiguration")
    CodeRepository_: Optional['CodeRepository'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-coderepository""", alias="CodeRepository")
    ImageRepository_: Optional['ImageRepository'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-imagerepository""", alias="ImageRepository")
    AutoDeploymentsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-autodeploymentsenabled""", alias="AutoDeploymentsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.SourceConfiguration:
        from troposphere.apprunner import SourceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IngressVpcConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration.html
    Properties:
        - Name: VpcId
        - Name: VpcEndpointId
    
    """
    
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration.html#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcid""", alias="VpcId")
    VpcEndpointId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration.html#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcendpointid""", alias="VpcEndpointId")
    


    @property
    def tropo_type(self) -> troposphere.apprunner.IngressVpcConfiguration:
        from troposphere.apprunner import IngressVpcConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AutoScalingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-autoscalingconfiguration.html
    Properties:
        - Name: MinSize
        - Name: MaxConcurrency
        - Name: AutoScalingConfigurationName
        - Name: MaxSize
        - Name: Tags
    Attributes:
        - Name: AutoScalingConfigurationRevision
        - Name: AutoScalingConfigurationArn
        - Name: Latest
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MinSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-autoscalingconfiguration.html#cfn-apprunner-autoscalingconfiguration-minsize""", alias="MinSize")
    MaxConcurrency_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-autoscalingconfiguration.html#cfn-apprunner-autoscalingconfiguration-maxconcurrency""", alias="MaxConcurrency")
    AutoScalingConfigurationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-autoscalingconfiguration.html#cfn-apprunner-autoscalingconfiguration-autoscalingconfigurationname""", alias="AutoScalingConfigurationName")
    MaxSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-autoscalingconfiguration.html#cfn-apprunner-autoscalingconfiguration-maxsize""", alias="MaxSize")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-autoscalingconfiguration.html#cfn-apprunner-autoscalingconfiguration-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.apprunner.AutoScalingConfiguration:
        from troposphere.apprunner import AutoScalingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apprunner import AutoScalingConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class ObservabilityConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html
    Properties:
        - Name: TraceConfiguration
        - Name: ObservabilityConfigurationName
        - Name: Tags
    Attributes:
        - Name: ObservabilityConfigurationRevision
        - Name: ObservabilityConfigurationArn
        - Name: Latest
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TraceConfiguration_: Optional['TraceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-traceconfiguration""", alias="TraceConfiguration")
    ObservabilityConfigurationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-observabilityconfigurationname""", alias="ObservabilityConfigurationName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.apprunner.ObservabilityConfiguration:
        from troposphere.apprunner import ObservabilityConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apprunner import ObservabilityConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class Service(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html
    Properties:
        - Name: HealthCheckConfiguration
        - Name: InstanceConfiguration
        - Name: EncryptionConfiguration
        - Name: ServiceName
        - Name: ObservabilityConfiguration
        - Name: SourceConfiguration
        - Name: AutoScalingConfigurationArn
        - Name: NetworkConfiguration
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: ServiceUrl
        - Name: ServiceArn
        - Name: ServiceId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    HealthCheckConfiguration_: Optional['HealthCheckConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-healthcheckconfiguration""", alias="HealthCheckConfiguration")
    InstanceConfiguration_: Optional['InstanceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-instanceconfiguration""", alias="InstanceConfiguration")
    EncryptionConfiguration_: Optional['EncryptionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-encryptionconfiguration""", alias="EncryptionConfiguration")
    ServiceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-servicename""", alias="ServiceName")
    ObservabilityConfiguration_: Optional['ServiceObservabilityConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-observabilityconfiguration""", alias="ObservabilityConfiguration")
    SourceConfiguration_: 'SourceConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-sourceconfiguration""", alias="SourceConfiguration")
    AutoScalingConfigurationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-autoscalingconfigurationarn""", alias="AutoScalingConfigurationArn")
    NetworkConfiguration_: Optional['NetworkConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-networkconfiguration""", alias="NetworkConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.apprunner.Service:
        from troposphere.apprunner import Service as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apprunner import Service as TropoT
        return resource_to_troposphere(self, TropoT)


class VpcConnector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html
    Properties:
        - Name: SecurityGroups
        - Name: Subnets
        - Name: VpcConnectorName
        - Name: Tags
    Attributes:
        - Name: VpcConnectorArn
        - Name: VpcConnectorRevision
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-securitygroups""", alias="SecurityGroups")
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-subnets""", alias="Subnets")
    VpcConnectorName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-vpcconnectorname""", alias="VpcConnectorName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.apprunner.VpcConnector:
        from troposphere.apprunner import VpcConnector as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apprunner import VpcConnector as TropoT
        return resource_to_troposphere(self, TropoT)


class VpcIngressConnection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html
    Properties:
        - Name: VpcIngressConnectionName
        - Name: ServiceArn
        - Name: Tags
        - Name: IngressVpcConfiguration
    Attributes:
        - Name: Status
        - Name: DomainName
        - Name: VpcIngressConnectionArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VpcIngressConnectionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-vpcingressconnectionname""", alias="VpcIngressConnectionName")
    ServiceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-servicearn""", alias="ServiceArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-tags""", alias="Tags")
    IngressVpcConfiguration_: 'IngressVpcConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration""", alias="IngressVpcConfiguration")
    

    @property
    def tropo_type(self) -> troposphere.apprunner.VpcIngressConnection:
        from troposphere.apprunner import VpcIngressConnection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apprunner import VpcIngressConnection as TropoT
        return resource_to_troposphere(self, TropoT)

