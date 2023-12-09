from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AwsVpcConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-awsvpcconfiguration.html
    Properties:
        - Name: SecurityGroups
        - Name: Subnets
        - Name: AssignPublicIp
    
    """
    
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-awsvpcconfiguration.html#cfn-pipes-pipe-awsvpcconfiguration-securitygroups""", alias="SecurityGroups")
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-awsvpcconfiguration.html#cfn-pipes-pipe-awsvpcconfiguration-subnets""", alias="Subnets")
    AssignPublicIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-awsvpcconfiguration.html#cfn-pipes-pipe-awsvpcconfiguration-assignpublicip""", alias="AssignPublicIp")
    


    @property
    def tropo_type(self) -> troposphere.pipes.AwsVpcConfiguration:
        from troposphere.pipes import AwsVpcConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchArrayProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batcharrayproperties.html
    Properties:
        - Name: Size
    
    """
    
    Size_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batcharrayproperties.html#cfn-pipes-pipe-batcharrayproperties-size""", alias="Size")
    


    @property
    def tropo_type(self) -> troposphere.pipes.BatchArrayProperties:
        from troposphere.pipes import BatchArrayProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchContainerOverrides(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchcontaineroverrides.html
    Properties:
        - Name: Command
        - Name: Environment
        - Name: InstanceType
        - Name: ResourceRequirements
    
    """
    
    Command_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchcontaineroverrides.html#cfn-pipes-pipe-batchcontaineroverrides-command""", alias="Command")
    Environment_: Optional[List['BatchEnvironmentVariable']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchcontaineroverrides.html#cfn-pipes-pipe-batchcontaineroverrides-environment""", alias="Environment")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchcontaineroverrides.html#cfn-pipes-pipe-batchcontaineroverrides-instancetype""", alias="InstanceType")
    ResourceRequirements_: Optional[List['BatchResourceRequirement']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchcontaineroverrides.html#cfn-pipes-pipe-batchcontaineroverrides-resourcerequirements""", alias="ResourceRequirements")
    


    @property
    def tropo_type(self) -> troposphere.pipes.BatchContainerOverrides:
        from troposphere.pipes import BatchContainerOverrides as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchEnvironmentVariable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchenvironmentvariable.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchenvironmentvariable.html#cfn-pipes-pipe-batchenvironmentvariable-value""", alias="Value")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchenvironmentvariable.html#cfn-pipes-pipe-batchenvironmentvariable-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.pipes.BatchEnvironmentVariable:
        from troposphere.pipes import BatchEnvironmentVariable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchJobDependency(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchjobdependency.html
    Properties:
        - Name: Type
        - Name: JobId
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchjobdependency.html#cfn-pipes-pipe-batchjobdependency-type""", alias="Type")
    JobId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchjobdependency.html#cfn-pipes-pipe-batchjobdependency-jobid""", alias="JobId")
    


    @property
    def tropo_type(self) -> troposphere.pipes.BatchJobDependency:
        from troposphere.pipes import BatchJobDependency as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchResourceRequirement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchresourcerequirement.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchresourcerequirement.html#cfn-pipes-pipe-batchresourcerequirement-type""", alias="Type")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchresourcerequirement.html#cfn-pipes-pipe-batchresourcerequirement-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.pipes.BatchResourceRequirement:
        from troposphere.pipes import BatchResourceRequirement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchRetryStrategy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchretrystrategy.html
    Properties:
        - Name: Attempts
    
    """
    
    Attempts_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchretrystrategy.html#cfn-pipes-pipe-batchretrystrategy-attempts""", alias="Attempts")
    


    @property
    def tropo_type(self) -> troposphere.pipes.BatchRetryStrategy:
        from troposphere.pipes import BatchRetryStrategy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacityProviderStrategyItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-capacityproviderstrategyitem.html
    Properties:
        - Name: CapacityProvider
        - Name: Weight
        - Name: Base
    
    """
    
    CapacityProvider_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-capacityproviderstrategyitem.html#cfn-pipes-pipe-capacityproviderstrategyitem-capacityprovider""", alias="CapacityProvider")
    Weight_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-capacityproviderstrategyitem.html#cfn-pipes-pipe-capacityproviderstrategyitem-weight""", alias="Weight")
    Base_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-capacityproviderstrategyitem.html#cfn-pipes-pipe-capacityproviderstrategyitem-base""", alias="Base")
    


    @property
    def tropo_type(self) -> troposphere.pipes.CapacityProviderStrategyItem:
        from troposphere.pipes import CapacityProviderStrategyItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudwatchLogsLogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-cloudwatchlogslogdestination.html
    Properties:
        - Name: LogGroupArn
    
    """
    
    LogGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-cloudwatchlogslogdestination.html#cfn-pipes-pipe-cloudwatchlogslogdestination-loggrouparn""", alias="LogGroupArn")
    


    @property
    def tropo_type(self) -> troposphere.pipes.CloudwatchLogsLogDestination:
        from troposphere.pipes import CloudwatchLogsLogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeadLetterConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-deadletterconfig.html
    Properties:
        - Name: Arn
    
    """
    
    Arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-deadletterconfig.html#cfn-pipes-pipe-deadletterconfig-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.pipes.DeadLetterConfig:
        from troposphere.pipes import DeadLetterConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EcsContainerOverride(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html
    Properties:
        - Name: MemoryReservation
        - Name: Command
        - Name: Memory
        - Name: Cpu
        - Name: Environment
        - Name: ResourceRequirements
        - Name: EnvironmentFiles
        - Name: Name
    
    """
    
    MemoryReservation_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-memoryreservation""", alias="MemoryReservation")
    Command_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-command""", alias="Command")
    Memory_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-memory""", alias="Memory")
    Cpu_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-cpu""", alias="Cpu")
    Environment_: Optional[List['EcsEnvironmentVariable']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-environment""", alias="Environment")
    ResourceRequirements_: Optional[List['EcsResourceRequirement']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-resourcerequirements""", alias="ResourceRequirements")
    EnvironmentFiles_: Optional[List['EcsEnvironmentFile']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-environmentfiles""", alias="EnvironmentFiles")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.pipes.EcsContainerOverride:
        from troposphere.pipes import EcsContainerOverride as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EcsEnvironmentFile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentfile.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentfile.html#cfn-pipes-pipe-ecsenvironmentfile-type""", alias="Type")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentfile.html#cfn-pipes-pipe-ecsenvironmentfile-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.pipes.EcsEnvironmentFile:
        from troposphere.pipes import EcsEnvironmentFile as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EcsEnvironmentVariable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentvariable.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentvariable.html#cfn-pipes-pipe-ecsenvironmentvariable-value""", alias="Value")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentvariable.html#cfn-pipes-pipe-ecsenvironmentvariable-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.pipes.EcsEnvironmentVariable:
        from troposphere.pipes import EcsEnvironmentVariable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EcsEphemeralStorage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsephemeralstorage.html
    Properties:
        - Name: SizeInGiB
    
    """
    
    SizeInGiB_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsephemeralstorage.html#cfn-pipes-pipe-ecsephemeralstorage-sizeingib""", alias="SizeInGiB")
    


    @property
    def tropo_type(self) -> troposphere.pipes.EcsEphemeralStorage:
        from troposphere.pipes import EcsEphemeralStorage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EcsInferenceAcceleratorOverride(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsinferenceacceleratoroverride.html
    Properties:
        - Name: DeviceType
        - Name: DeviceName
    
    """
    
    DeviceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsinferenceacceleratoroverride.html#cfn-pipes-pipe-ecsinferenceacceleratoroverride-devicetype""", alias="DeviceType")
    DeviceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsinferenceacceleratoroverride.html#cfn-pipes-pipe-ecsinferenceacceleratoroverride-devicename""", alias="DeviceName")
    


    @property
    def tropo_type(self) -> troposphere.pipes.EcsInferenceAcceleratorOverride:
        from troposphere.pipes import EcsInferenceAcceleratorOverride as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EcsResourceRequirement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsresourcerequirement.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsresourcerequirement.html#cfn-pipes-pipe-ecsresourcerequirement-type""", alias="Type")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsresourcerequirement.html#cfn-pipes-pipe-ecsresourcerequirement-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.pipes.EcsResourceRequirement:
        from troposphere.pipes import EcsResourceRequirement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EcsTaskOverride(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html
    Properties:
        - Name: ExecutionRoleArn
        - Name: TaskRoleArn
        - Name: Memory
        - Name: Cpu
        - Name: InferenceAcceleratorOverrides
        - Name: EphemeralStorage
        - Name: ContainerOverrides
    
    """
    
    ExecutionRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-executionrolearn""", alias="ExecutionRoleArn")
    TaskRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-taskrolearn""", alias="TaskRoleArn")
    Memory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-memory""", alias="Memory")
    Cpu_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-cpu""", alias="Cpu")
    InferenceAcceleratorOverrides_: Optional[List['EcsInferenceAcceleratorOverride']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-inferenceacceleratoroverrides""", alias="InferenceAcceleratorOverrides")
    EphemeralStorage_: Optional['EcsEphemeralStorage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-ephemeralstorage""", alias="EphemeralStorage")
    ContainerOverrides_: Optional[List['EcsContainerOverride']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-containeroverrides""", alias="ContainerOverrides")
    


    @property
    def tropo_type(self) -> troposphere.pipes.EcsTaskOverride:
        from troposphere.pipes import EcsTaskOverride as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Filter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-filter.html
    Properties:
        - Name: Pattern
    
    """
    
    Pattern_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-filter.html#cfn-pipes-pipe-filter-pattern""", alias="Pattern")
    


    @property
    def tropo_type(self) -> troposphere.pipes.Filter:
        from troposphere.pipes import Filter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FilterCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-filtercriteria.html
    Properties:
        - Name: Filters
    
    """
    
    Filters_: Optional[List['Filter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-filtercriteria.html#cfn-pipes-pipe-filtercriteria-filters""", alias="Filters")
    


    @property
    def tropo_type(self) -> troposphere.pipes.FilterCriteria:
        from troposphere.pipes import FilterCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FirehoseLogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-firehoselogdestination.html
    Properties:
        - Name: DeliveryStreamArn
    
    """
    
    DeliveryStreamArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-firehoselogdestination.html#cfn-pipes-pipe-firehoselogdestination-deliverystreamarn""", alias="DeliveryStreamArn")
    


    @property
    def tropo_type(self) -> troposphere.pipes.FirehoseLogDestination:
        from troposphere.pipes import FirehoseLogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MQBrokerAccessCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-mqbrokeraccesscredentials.html
    Properties:
        - Name: BasicAuth
    
    """
    
    BasicAuth_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-mqbrokeraccesscredentials.html#cfn-pipes-pipe-mqbrokeraccesscredentials-basicauth""", alias="BasicAuth")
    


    @property
    def tropo_type(self) -> troposphere.pipes.MQBrokerAccessCredentials:
        from troposphere.pipes import MQBrokerAccessCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MSKAccessCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-mskaccesscredentials.html
    Properties:
        - Name: ClientCertificateTlsAuth
        - Name: SaslScram512Auth
    
    """
    
    ClientCertificateTlsAuth_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-mskaccesscredentials.html#cfn-pipes-pipe-mskaccesscredentials-clientcertificatetlsauth""", alias="ClientCertificateTlsAuth")
    SaslScram512Auth_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-mskaccesscredentials.html#cfn-pipes-pipe-mskaccesscredentials-saslscram512auth""", alias="SaslScram512Auth")
    


    @property
    def tropo_type(self) -> troposphere.pipes.MSKAccessCredentials:
        from troposphere.pipes import MSKAccessCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-networkconfiguration.html
    Properties:
        - Name: AwsvpcConfiguration
    
    """
    
    AwsvpcConfiguration_: Optional['AwsVpcConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-networkconfiguration.html#cfn-pipes-pipe-networkconfiguration-awsvpcconfiguration""", alias="AwsvpcConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.pipes.NetworkConfiguration:
        from troposphere.pipes import NetworkConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeEnrichmentHttpParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmenthttpparameters.html
    Properties:
        - Name: PathParameterValues
        - Name: HeaderParameters
        - Name: QueryStringParameters
    
    """
    
    PathParameterValues_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmenthttpparameters.html#cfn-pipes-pipe-pipeenrichmenthttpparameters-pathparametervalues""", alias="PathParameterValues")
    HeaderParameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmenthttpparameters.html#cfn-pipes-pipe-pipeenrichmenthttpparameters-headerparameters""", alias="HeaderParameters")
    QueryStringParameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmenthttpparameters.html#cfn-pipes-pipe-pipeenrichmenthttpparameters-querystringparameters""", alias="QueryStringParameters")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeEnrichmentHttpParameters:
        from troposphere.pipes import PipeEnrichmentHttpParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeEnrichmentParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmentparameters.html
    Properties:
        - Name: HttpParameters
        - Name: InputTemplate
    
    """
    
    HttpParameters_: Optional['PipeEnrichmentHttpParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmentparameters.html#cfn-pipes-pipe-pipeenrichmentparameters-httpparameters""", alias="HttpParameters")
    InputTemplate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmentparameters.html#cfn-pipes-pipe-pipeenrichmentparameters-inputtemplate""", alias="InputTemplate")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeEnrichmentParameters:
        from troposphere.pipes import PipeEnrichmentParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeLogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipelogconfiguration.html
    Properties:
        - Name: FirehoseLogDestination
        - Name: CloudwatchLogsLogDestination
        - Name: IncludeExecutionData
        - Name: S3LogDestination
        - Name: Level
    
    """
    
    FirehoseLogDestination_: Optional['FirehoseLogDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipelogconfiguration.html#cfn-pipes-pipe-pipelogconfiguration-firehoselogdestination""", alias="FirehoseLogDestination")
    CloudwatchLogsLogDestination_: Optional['CloudwatchLogsLogDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipelogconfiguration.html#cfn-pipes-pipe-pipelogconfiguration-cloudwatchlogslogdestination""", alias="CloudwatchLogsLogDestination")
    IncludeExecutionData_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipelogconfiguration.html#cfn-pipes-pipe-pipelogconfiguration-includeexecutiondata""", alias="IncludeExecutionData")
    S3LogDestination_: Optional['S3LogDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipelogconfiguration.html#cfn-pipes-pipe-pipelogconfiguration-s3logdestination""", alias="S3LogDestination")
    Level_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipelogconfiguration.html#cfn-pipes-pipe-pipelogconfiguration-level""", alias="Level")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeLogConfiguration:
        from troposphere.pipes import PipeLogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeSourceActiveMQBrokerParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters.html
    Properties:
        - Name: BatchSize
        - Name: QueueName
        - Name: Credentials
        - Name: MaximumBatchingWindowInSeconds
    
    """
    
    BatchSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters.html#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-batchsize""", alias="BatchSize")
    QueueName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters.html#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-queuename""", alias="QueueName")
    Credentials_: 'MQBrokerAccessCredentials' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters.html#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-credentials""", alias="Credentials")
    MaximumBatchingWindowInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters.html#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-maximumbatchingwindowinseconds""", alias="MaximumBatchingWindowInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeSourceActiveMQBrokerParameters:
        from troposphere.pipes import PipeSourceActiveMQBrokerParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeSourceDynamoDBStreamParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html
    Properties:
        - Name: StartingPosition
        - Name: BatchSize
        - Name: MaximumRetryAttempts
        - Name: OnPartialBatchItemFailure
        - Name: DeadLetterConfig
        - Name: ParallelizationFactor
        - Name: MaximumRecordAgeInSeconds
        - Name: MaximumBatchingWindowInSeconds
    
    """
    
    StartingPosition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-startingposition""", alias="StartingPosition")
    BatchSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-batchsize""", alias="BatchSize")
    MaximumRetryAttempts_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumretryattempts""", alias="MaximumRetryAttempts")
    OnPartialBatchItemFailure_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-onpartialbatchitemfailure""", alias="OnPartialBatchItemFailure")
    DeadLetterConfig_: Optional['DeadLetterConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-deadletterconfig""", alias="DeadLetterConfig")
    ParallelizationFactor_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-parallelizationfactor""", alias="ParallelizationFactor")
    MaximumRecordAgeInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumrecordageinseconds""", alias="MaximumRecordAgeInSeconds")
    MaximumBatchingWindowInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumbatchingwindowinseconds""", alias="MaximumBatchingWindowInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeSourceDynamoDBStreamParameters:
        from troposphere.pipes import PipeSourceDynamoDBStreamParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeSourceKinesisStreamParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html
    Properties:
        - Name: StartingPosition
        - Name: BatchSize
        - Name: MaximumRetryAttempts
        - Name: OnPartialBatchItemFailure
        - Name: DeadLetterConfig
        - Name: ParallelizationFactor
        - Name: MaximumRecordAgeInSeconds
        - Name: StartingPositionTimestamp
        - Name: MaximumBatchingWindowInSeconds
    
    """
    
    StartingPosition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-startingposition""", alias="StartingPosition")
    BatchSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-batchsize""", alias="BatchSize")
    MaximumRetryAttempts_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-maximumretryattempts""", alias="MaximumRetryAttempts")
    OnPartialBatchItemFailure_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-onpartialbatchitemfailure""", alias="OnPartialBatchItemFailure")
    DeadLetterConfig_: Optional['DeadLetterConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-deadletterconfig""", alias="DeadLetterConfig")
    ParallelizationFactor_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-parallelizationfactor""", alias="ParallelizationFactor")
    MaximumRecordAgeInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-maximumrecordageinseconds""", alias="MaximumRecordAgeInSeconds")
    StartingPositionTimestamp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-startingpositiontimestamp""", alias="StartingPositionTimestamp")
    MaximumBatchingWindowInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-maximumbatchingwindowinseconds""", alias="MaximumBatchingWindowInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeSourceKinesisStreamParameters:
        from troposphere.pipes import PipeSourceKinesisStreamParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeSourceManagedStreamingKafkaParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html
    Properties:
        - Name: StartingPosition
        - Name: BatchSize
        - Name: ConsumerGroupID
        - Name: Credentials
        - Name: TopicName
        - Name: MaximumBatchingWindowInSeconds
    
    """
    
    StartingPosition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-startingposition""", alias="StartingPosition")
    BatchSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-batchsize""", alias="BatchSize")
    ConsumerGroupID_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-consumergroupid""", alias="ConsumerGroupID")
    Credentials_: Optional['MSKAccessCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-credentials""", alias="Credentials")
    TopicName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-topicname""", alias="TopicName")
    MaximumBatchingWindowInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-maximumbatchingwindowinseconds""", alias="MaximumBatchingWindowInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeSourceManagedStreamingKafkaParameters:
        from troposphere.pipes import PipeSourceManagedStreamingKafkaParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeSourceParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html
    Properties:
        - Name: ManagedStreamingKafkaParameters
        - Name: DynamoDBStreamParameters
        - Name: SelfManagedKafkaParameters
        - Name: RabbitMQBrokerParameters
        - Name: SqsQueueParameters
        - Name: KinesisStreamParameters
        - Name: FilterCriteria
        - Name: ActiveMQBrokerParameters
    
    """
    
    ManagedStreamingKafkaParameters_: Optional['PipeSourceManagedStreamingKafkaParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-managedstreamingkafkaparameters""", alias="ManagedStreamingKafkaParameters")
    DynamoDBStreamParameters_: Optional['PipeSourceDynamoDBStreamParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-dynamodbstreamparameters""", alias="DynamoDBStreamParameters")
    SelfManagedKafkaParameters_: Optional['PipeSourceSelfManagedKafkaParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-selfmanagedkafkaparameters""", alias="SelfManagedKafkaParameters")
    RabbitMQBrokerParameters_: Optional['PipeSourceRabbitMQBrokerParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-rabbitmqbrokerparameters""", alias="RabbitMQBrokerParameters")
    SqsQueueParameters_: Optional['PipeSourceSqsQueueParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-sqsqueueparameters""", alias="SqsQueueParameters")
    KinesisStreamParameters_: Optional['PipeSourceKinesisStreamParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-kinesisstreamparameters""", alias="KinesisStreamParameters")
    FilterCriteria_: Optional['FilterCriteria'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-filtercriteria""", alias="FilterCriteria")
    ActiveMQBrokerParameters_: Optional['PipeSourceActiveMQBrokerParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-activemqbrokerparameters""", alias="ActiveMQBrokerParameters")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeSourceParameters:
        from troposphere.pipes import PipeSourceParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeSourceRabbitMQBrokerParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html
    Properties:
        - Name: BatchSize
        - Name: VirtualHost
        - Name: QueueName
        - Name: Credentials
        - Name: MaximumBatchingWindowInSeconds
    
    """
    
    BatchSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-batchsize""", alias="BatchSize")
    VirtualHost_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-virtualhost""", alias="VirtualHost")
    QueueName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-queuename""", alias="QueueName")
    Credentials_: 'MQBrokerAccessCredentials' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-credentials""", alias="Credentials")
    MaximumBatchingWindowInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-maximumbatchingwindowinseconds""", alias="MaximumBatchingWindowInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeSourceRabbitMQBrokerParameters:
        from troposphere.pipes import PipeSourceRabbitMQBrokerParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeSourceSelfManagedKafkaParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html
    Properties:
        - Name: StartingPosition
        - Name: BatchSize
        - Name: ConsumerGroupID
        - Name: AdditionalBootstrapServers
        - Name: Vpc
        - Name: Credentials
        - Name: ServerRootCaCertificate
        - Name: TopicName
        - Name: MaximumBatchingWindowInSeconds
    
    """
    
    StartingPosition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-startingposition""", alias="StartingPosition")
    BatchSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-batchsize""", alias="BatchSize")
    ConsumerGroupID_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-consumergroupid""", alias="ConsumerGroupID")
    AdditionalBootstrapServers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-additionalbootstrapservers""", alias="AdditionalBootstrapServers")
    Vpc_: Optional['SelfManagedKafkaAccessConfigurationVpc'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-vpc""", alias="Vpc")
    Credentials_: Optional['SelfManagedKafkaAccessConfigurationCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-credentials""", alias="Credentials")
    ServerRootCaCertificate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-serverrootcacertificate""", alias="ServerRootCaCertificate")
    TopicName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-topicname""", alias="TopicName")
    MaximumBatchingWindowInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-maximumbatchingwindowinseconds""", alias="MaximumBatchingWindowInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeSourceSelfManagedKafkaParameters:
        from troposphere.pipes import PipeSourceSelfManagedKafkaParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeSourceSqsQueueParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcesqsqueueparameters.html
    Properties:
        - Name: BatchSize
        - Name: MaximumBatchingWindowInSeconds
    
    """
    
    BatchSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcesqsqueueparameters.html#cfn-pipes-pipe-pipesourcesqsqueueparameters-batchsize""", alias="BatchSize")
    MaximumBatchingWindowInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcesqsqueueparameters.html#cfn-pipes-pipe-pipesourcesqsqueueparameters-maximumbatchingwindowinseconds""", alias="MaximumBatchingWindowInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeSourceSqsQueueParameters:
        from troposphere.pipes import PipeSourceSqsQueueParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeTargetBatchJobParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html
    Properties:
        - Name: DependsOn
        - Name: Parameters
        - Name: ArrayProperties
        - Name: JobName
        - Name: RetryStrategy
        - Name: JobDefinition
        - Name: ContainerOverrides
    
    """
    
    DependsOn_: Optional[List['BatchJobDependency']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-dependson""", alias="DependsOn")
    Parameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-parameters""", alias="Parameters")
    ArrayProperties_: Optional['BatchArrayProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-arrayproperties""", alias="ArrayProperties")
    JobName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-jobname""", alias="JobName")
    RetryStrategy_: Optional['BatchRetryStrategy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-retrystrategy""", alias="RetryStrategy")
    JobDefinition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-jobdefinition""", alias="JobDefinition")
    ContainerOverrides_: Optional['BatchContainerOverrides'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-containeroverrides""", alias="ContainerOverrides")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeTargetBatchJobParameters:
        from troposphere.pipes import PipeTargetBatchJobParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeTargetCloudWatchLogsParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetcloudwatchlogsparameters.html
    Properties:
        - Name: LogStreamName
        - Name: Timestamp
    
    """
    
    LogStreamName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetcloudwatchlogsparameters.html#cfn-pipes-pipe-pipetargetcloudwatchlogsparameters-logstreamname""", alias="LogStreamName")
    Timestamp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetcloudwatchlogsparameters.html#cfn-pipes-pipe-pipetargetcloudwatchlogsparameters-timestamp""", alias="Timestamp")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeTargetCloudWatchLogsParameters:
        from troposphere.pipes import PipeTargetCloudWatchLogsParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeTargetEcsTaskParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html
    Properties:
        - Name: PlatformVersion
        - Name: Group
        - Name: EnableECSManagedTags
        - Name: TaskCount
        - Name: EnableExecuteCommand
        - Name: PlacementConstraints
        - Name: PropagateTags
        - Name: PlacementStrategy
        - Name: LaunchType
        - Name: CapacityProviderStrategy
        - Name: ReferenceId
        - Name: Overrides
        - Name: NetworkConfiguration
        - Name: Tags
        - Name: TaskDefinitionArn
    
    """
    
    PlatformVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-platformversion""", alias="PlatformVersion")
    Group_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-group""", alias="Group")
    EnableECSManagedTags_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-enableecsmanagedtags""", alias="EnableECSManagedTags")
    TaskCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-taskcount""", alias="TaskCount")
    EnableExecuteCommand_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-enableexecutecommand""", alias="EnableExecuteCommand")
    PlacementConstraints_: Optional[List['PlacementConstraint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-placementconstraints""", alias="PlacementConstraints")
    PropagateTags_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-propagatetags""", alias="PropagateTags")
    PlacementStrategy_: Optional[List['PlacementStrategy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-placementstrategy""", alias="PlacementStrategy")
    LaunchType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-launchtype""", alias="LaunchType")
    CapacityProviderStrategy_: Optional[List['CapacityProviderStrategyItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-capacityproviderstrategy""", alias="CapacityProviderStrategy")
    ReferenceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-referenceid""", alias="ReferenceId")
    Overrides_: Optional['EcsTaskOverride'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-overrides""", alias="Overrides")
    NetworkConfiguration_: Optional['NetworkConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-networkconfiguration""", alias="NetworkConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-tags""", alias="Tags")
    TaskDefinitionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-taskdefinitionarn""", alias="TaskDefinitionArn")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeTargetEcsTaskParameters:
        from troposphere.pipes import PipeTargetEcsTaskParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeTargetEventBridgeEventBusParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargeteventbridgeeventbusparameters.html
    Properties:
        - Name: DetailType
        - Name: EndpointId
        - Name: Time
        - Name: Resources
        - Name: Source
    
    """
    
    DetailType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargeteventbridgeeventbusparameters.html#cfn-pipes-pipe-pipetargeteventbridgeeventbusparameters-detailtype""", alias="DetailType")
    EndpointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargeteventbridgeeventbusparameters.html#cfn-pipes-pipe-pipetargeteventbridgeeventbusparameters-endpointid""", alias="EndpointId")
    Time_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargeteventbridgeeventbusparameters.html#cfn-pipes-pipe-pipetargeteventbridgeeventbusparameters-time""", alias="Time")
    Resources_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargeteventbridgeeventbusparameters.html#cfn-pipes-pipe-pipetargeteventbridgeeventbusparameters-resources""", alias="Resources")
    Source_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargeteventbridgeeventbusparameters.html#cfn-pipes-pipe-pipetargeteventbridgeeventbusparameters-source""", alias="Source")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeTargetEventBridgeEventBusParameters:
        from troposphere.pipes import PipeTargetEventBridgeEventBusParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeTargetHttpParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargethttpparameters.html
    Properties:
        - Name: PathParameterValues
        - Name: HeaderParameters
        - Name: QueryStringParameters
    
    """
    
    PathParameterValues_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargethttpparameters.html#cfn-pipes-pipe-pipetargethttpparameters-pathparametervalues""", alias="PathParameterValues")
    HeaderParameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargethttpparameters.html#cfn-pipes-pipe-pipetargethttpparameters-headerparameters""", alias="HeaderParameters")
    QueryStringParameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargethttpparameters.html#cfn-pipes-pipe-pipetargethttpparameters-querystringparameters""", alias="QueryStringParameters")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeTargetHttpParameters:
        from troposphere.pipes import PipeTargetHttpParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeTargetKinesisStreamParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetkinesisstreamparameters.html
    Properties:
        - Name: PartitionKey
    
    """
    
    PartitionKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetkinesisstreamparameters.html#cfn-pipes-pipe-pipetargetkinesisstreamparameters-partitionkey""", alias="PartitionKey")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeTargetKinesisStreamParameters:
        from troposphere.pipes import PipeTargetKinesisStreamParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeTargetLambdaFunctionParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetlambdafunctionparameters.html
    Properties:
        - Name: InvocationType
    
    """
    
    InvocationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetlambdafunctionparameters.html#cfn-pipes-pipe-pipetargetlambdafunctionparameters-invocationtype""", alias="InvocationType")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeTargetLambdaFunctionParameters:
        from troposphere.pipes import PipeTargetLambdaFunctionParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeTargetParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html
    Properties:
        - Name: StepFunctionStateMachineParameters
        - Name: HttpParameters
        - Name: SqsQueueParameters
        - Name: CloudWatchLogsParameters
        - Name: KinesisStreamParameters
        - Name: InputTemplate
        - Name: SageMakerPipelineParameters
        - Name: EventBridgeEventBusParameters
        - Name: LambdaFunctionParameters
        - Name: EcsTaskParameters
        - Name: BatchJobParameters
        - Name: RedshiftDataParameters
    
    """
    
    StepFunctionStateMachineParameters_: Optional['PipeTargetStateMachineParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-stepfunctionstatemachineparameters""", alias="StepFunctionStateMachineParameters")
    HttpParameters_: Optional['PipeTargetHttpParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-httpparameters""", alias="HttpParameters")
    SqsQueueParameters_: Optional['PipeTargetSqsQueueParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-sqsqueueparameters""", alias="SqsQueueParameters")
    CloudWatchLogsParameters_: Optional['PipeTargetCloudWatchLogsParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-cloudwatchlogsparameters""", alias="CloudWatchLogsParameters")
    KinesisStreamParameters_: Optional['PipeTargetKinesisStreamParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-kinesisstreamparameters""", alias="KinesisStreamParameters")
    InputTemplate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-inputtemplate""", alias="InputTemplate")
    SageMakerPipelineParameters_: Optional['PipeTargetSageMakerPipelineParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-sagemakerpipelineparameters""", alias="SageMakerPipelineParameters")
    EventBridgeEventBusParameters_: Optional['PipeTargetEventBridgeEventBusParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-eventbridgeeventbusparameters""", alias="EventBridgeEventBusParameters")
    LambdaFunctionParameters_: Optional['PipeTargetLambdaFunctionParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-lambdafunctionparameters""", alias="LambdaFunctionParameters")
    EcsTaskParameters_: Optional['PipeTargetEcsTaskParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-ecstaskparameters""", alias="EcsTaskParameters")
    BatchJobParameters_: Optional['PipeTargetBatchJobParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-batchjobparameters""", alias="BatchJobParameters")
    RedshiftDataParameters_: Optional['PipeTargetRedshiftDataParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-redshiftdataparameters""", alias="RedshiftDataParameters")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeTargetParameters:
        from troposphere.pipes import PipeTargetParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeTargetRedshiftDataParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html
    Properties:
        - Name: StatementName
        - Name: Sqls
        - Name: Database
        - Name: SecretManagerArn
        - Name: DbUser
        - Name: WithEvent
    
    """
    
    StatementName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html#cfn-pipes-pipe-pipetargetredshiftdataparameters-statementname""", alias="StatementName")
    Sqls_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html#cfn-pipes-pipe-pipetargetredshiftdataparameters-sqls""", alias="Sqls")
    Database_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html#cfn-pipes-pipe-pipetargetredshiftdataparameters-database""", alias="Database")
    SecretManagerArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html#cfn-pipes-pipe-pipetargetredshiftdataparameters-secretmanagerarn""", alias="SecretManagerArn")
    DbUser_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html#cfn-pipes-pipe-pipetargetredshiftdataparameters-dbuser""", alias="DbUser")
    WithEvent_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html#cfn-pipes-pipe-pipetargetredshiftdataparameters-withevent""", alias="WithEvent")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeTargetRedshiftDataParameters:
        from troposphere.pipes import PipeTargetRedshiftDataParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeTargetSageMakerPipelineParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetsagemakerpipelineparameters.html
    Properties:
        - Name: PipelineParameterList
    
    """
    
    PipelineParameterList_: Optional[List['SageMakerPipelineParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetsagemakerpipelineparameters.html#cfn-pipes-pipe-pipetargetsagemakerpipelineparameters-pipelineparameterlist""", alias="PipelineParameterList")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeTargetSageMakerPipelineParameters:
        from troposphere.pipes import PipeTargetSageMakerPipelineParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeTargetSqsQueueParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetsqsqueueparameters.html
    Properties:
        - Name: MessageGroupId
        - Name: MessageDeduplicationId
    
    """
    
    MessageGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetsqsqueueparameters.html#cfn-pipes-pipe-pipetargetsqsqueueparameters-messagegroupid""", alias="MessageGroupId")
    MessageDeduplicationId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetsqsqueueparameters.html#cfn-pipes-pipe-pipetargetsqsqueueparameters-messagededuplicationid""", alias="MessageDeduplicationId")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeTargetSqsQueueParameters:
        from troposphere.pipes import PipeTargetSqsQueueParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipeTargetStateMachineParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetstatemachineparameters.html
    Properties:
        - Name: InvocationType
    
    """
    
    InvocationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetstatemachineparameters.html#cfn-pipes-pipe-pipetargetstatemachineparameters-invocationtype""", alias="InvocationType")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PipeTargetStateMachineParameters:
        from troposphere.pipes import PipeTargetStateMachineParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PlacementConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementconstraint.html
    Properties:
        - Name: Type
        - Name: Expression
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementconstraint.html#cfn-pipes-pipe-placementconstraint-type""", alias="Type")
    Expression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementconstraint.html#cfn-pipes-pipe-placementconstraint-expression""", alias="Expression")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PlacementConstraint:
        from troposphere.pipes import PlacementConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PlacementStrategy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementstrategy.html
    Properties:
        - Name: Field
        - Name: Type
    
    """
    
    Field_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementstrategy.html#cfn-pipes-pipe-placementstrategy-field""", alias="Field")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementstrategy.html#cfn-pipes-pipe-placementstrategy-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.pipes.PlacementStrategy:
        from troposphere.pipes import PlacementStrategy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3LogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-s3logdestination.html
    Properties:
        - Name: BucketName
        - Name: OutputFormat
        - Name: Prefix
        - Name: BucketOwner
    
    """
    
    BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-s3logdestination.html#cfn-pipes-pipe-s3logdestination-bucketname""", alias="BucketName")
    OutputFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-s3logdestination.html#cfn-pipes-pipe-s3logdestination-outputformat""", alias="OutputFormat")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-s3logdestination.html#cfn-pipes-pipe-s3logdestination-prefix""", alias="Prefix")
    BucketOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-s3logdestination.html#cfn-pipes-pipe-s3logdestination-bucketowner""", alias="BucketOwner")
    


    @property
    def tropo_type(self) -> troposphere.pipes.S3LogDestination:
        from troposphere.pipes import S3LogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SageMakerPipelineParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-sagemakerpipelineparameter.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-sagemakerpipelineparameter.html#cfn-pipes-pipe-sagemakerpipelineparameter-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-sagemakerpipelineparameter.html#cfn-pipes-pipe-sagemakerpipelineparameter-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.pipes.SageMakerPipelineParameter:
        from troposphere.pipes import SageMakerPipelineParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SelfManagedKafkaAccessConfigurationCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials.html
    Properties:
        - Name: BasicAuth
        - Name: SaslScram256Auth
        - Name: ClientCertificateTlsAuth
        - Name: SaslScram512Auth
    
    """
    
    BasicAuth_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials.html#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-basicauth""", alias="BasicAuth")
    SaslScram256Auth_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials.html#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-saslscram256auth""", alias="SaslScram256Auth")
    ClientCertificateTlsAuth_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials.html#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-clientcertificatetlsauth""", alias="ClientCertificateTlsAuth")
    SaslScram512Auth_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials.html#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-saslscram512auth""", alias="SaslScram512Auth")
    


    @property
    def tropo_type(self) -> troposphere.pipes.SelfManagedKafkaAccessConfigurationCredentials:
        from troposphere.pipes import SelfManagedKafkaAccessConfigurationCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SelfManagedKafkaAccessConfigurationVpc(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc.html
    Properties:
        - Name: Subnets
        - Name: SecurityGroup
    
    """
    
    Subnets_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc.html#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-subnets""", alias="Subnets")
    SecurityGroup_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc.html#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-securitygroup""", alias="SecurityGroup")
    


    @property
    def tropo_type(self) -> troposphere.pipes.SelfManagedKafkaAccessConfigurationVpc:
        from troposphere.pipes import SelfManagedKafkaAccessConfigurationVpc as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Pipe(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html
    Properties:
        - Name: Enrichment
        - Name: Target
        - Name: Description
        - Name: DesiredState
        - Name: TargetParameters
        - Name: LogConfiguration
        - Name: EnrichmentParameters
        - Name: RoleArn
        - Name: Source
        - Name: SourceParameters
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: StateReason
        - Name: CurrentState
        - Name: CreationTime
        - Name: LastModifiedTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Enrichment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-enrichment""", alias="Enrichment")
    Target_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-target""", alias="Target")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-description""", alias="Description")
    DesiredState_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-desiredstate""", alias="DesiredState")
    TargetParameters_: Optional['PipeTargetParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-targetparameters""", alias="TargetParameters")
    LogConfiguration_: Optional['PipeLogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-logconfiguration""", alias="LogConfiguration")
    EnrichmentParameters_: Optional['PipeEnrichmentParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-enrichmentparameters""", alias="EnrichmentParameters")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-rolearn""", alias="RoleArn")
    Source_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-source""", alias="Source")
    SourceParameters_: Optional['PipeSourceParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-sourceparameters""", alias="SourceParameters")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.pipes.Pipe:
        from troposphere.pipes import Pipe as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pipes import Pipe as TropoT
        return resource_to_troposphere(self, TropoT)

