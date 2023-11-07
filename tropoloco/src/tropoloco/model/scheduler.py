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
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html
    Properties:
        - Name: SecurityGroups
        - Name: Subnets
        - Name: AssignPublicIp
    
    """
    
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html#cfn-scheduler-schedule-awsvpcconfiguration-securitygroups""", alias="SecurityGroups")
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html#cfn-scheduler-schedule-awsvpcconfiguration-subnets""", alias="Subnets")
    AssignPublicIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html#cfn-scheduler-schedule-awsvpcconfiguration-assignpublicip""", alias="AssignPublicIp")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.AwsVpcConfiguration:
        from troposphere.scheduler import AwsVpcConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacityProviderStrategyItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html
    Properties:
        - Name: CapacityProvider
        - Name: Weight
        - Name: Base
    
    """
    
    CapacityProvider_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html#cfn-scheduler-schedule-capacityproviderstrategyitem-capacityprovider""", alias="CapacityProvider")
    Weight_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html#cfn-scheduler-schedule-capacityproviderstrategyitem-weight""", alias="Weight")
    Base_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html#cfn-scheduler-schedule-capacityproviderstrategyitem-base""", alias="Base")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.CapacityProviderStrategyItem:
        from troposphere.scheduler import CapacityProviderStrategyItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeadLetterConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-deadletterconfig.html
    Properties:
        - Name: Arn
    
    """
    
    Arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-deadletterconfig.html#cfn-scheduler-schedule-deadletterconfig-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.DeadLetterConfig:
        from troposphere.scheduler import DeadLetterConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EcsParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html
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
        - Name: NetworkConfiguration
        - Name: Tags
        - Name: TaskDefinitionArn
    
    """
    
    PlatformVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-platformversion""", alias="PlatformVersion")
    Group_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-group""", alias="Group")
    EnableECSManagedTags_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-enableecsmanagedtags""", alias="EnableECSManagedTags")
    TaskCount_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-taskcount""", alias="TaskCount")
    EnableExecuteCommand_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-enableexecutecommand""", alias="EnableExecuteCommand")
    PlacementConstraints_: Optional[List['PlacementConstraint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-placementconstraints""", alias="PlacementConstraints")
    PropagateTags_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-propagatetags""", alias="PropagateTags")
    PlacementStrategy_: Optional[List['PlacementStrategy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-placementstrategy""", alias="PlacementStrategy")
    LaunchType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-launchtype""", alias="LaunchType")
    CapacityProviderStrategy_: Optional[List['CapacityProviderStrategyItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-capacityproviderstrategy""", alias="CapacityProviderStrategy")
    ReferenceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-referenceid""", alias="ReferenceId")
    NetworkConfiguration_: Optional['NetworkConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-networkconfiguration""", alias="NetworkConfiguration")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-tags""", alias="Tags")
    TaskDefinitionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-taskdefinitionarn""", alias="TaskDefinitionArn")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.EcsParameters:
        from troposphere.scheduler import EcsParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EventBridgeParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-eventbridgeparameters.html
    Properties:
        - Name: DetailType
        - Name: Source
    
    """
    
    DetailType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-eventbridgeparameters.html#cfn-scheduler-schedule-eventbridgeparameters-detailtype""", alias="DetailType")
    Source_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-eventbridgeparameters.html#cfn-scheduler-schedule-eventbridgeparameters-source""", alias="Source")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.EventBridgeParameters:
        from troposphere.scheduler import EventBridgeParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FlexibleTimeWindow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-flexibletimewindow.html
    Properties:
        - Name: Mode
        - Name: MaximumWindowInMinutes
    
    """
    
    Mode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-flexibletimewindow.html#cfn-scheduler-schedule-flexibletimewindow-mode""", alias="Mode")
    MaximumWindowInMinutes_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-flexibletimewindow.html#cfn-scheduler-schedule-flexibletimewindow-maximumwindowinminutes""", alias="MaximumWindowInMinutes")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.FlexibleTimeWindow:
        from troposphere.scheduler import FlexibleTimeWindow as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-kinesisparameters.html
    Properties:
        - Name: PartitionKey
    
    """
    
    PartitionKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-kinesisparameters.html#cfn-scheduler-schedule-kinesisparameters-partitionkey""", alias="PartitionKey")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.KinesisParameters:
        from troposphere.scheduler import KinesisParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-networkconfiguration.html
    Properties:
        - Name: AwsvpcConfiguration
    
    """
    
    AwsvpcConfiguration_: Optional['AwsVpcConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-networkconfiguration.html#cfn-scheduler-schedule-networkconfiguration-awsvpcconfiguration""", alias="AwsvpcConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.NetworkConfiguration:
        from troposphere.scheduler import NetworkConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PlacementConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementconstraint.html
    Properties:
        - Name: Type
        - Name: Expression
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementconstraint.html#cfn-scheduler-schedule-placementconstraint-type""", alias="Type")
    Expression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementconstraint.html#cfn-scheduler-schedule-placementconstraint-expression""", alias="Expression")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.PlacementConstraint:
        from troposphere.scheduler import PlacementConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PlacementStrategy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementstrategy.html
    Properties:
        - Name: Field
        - Name: Type
    
    """
    
    Field_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementstrategy.html#cfn-scheduler-schedule-placementstrategy-field""", alias="Field")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementstrategy.html#cfn-scheduler-schedule-placementstrategy-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.PlacementStrategy:
        from troposphere.scheduler import PlacementStrategy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RetryPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-retrypolicy.html
    Properties:
        - Name: MaximumRetryAttempts
        - Name: MaximumEventAgeInSeconds
    
    """
    
    MaximumRetryAttempts_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-retrypolicy.html#cfn-scheduler-schedule-retrypolicy-maximumretryattempts""", alias="MaximumRetryAttempts")
    MaximumEventAgeInSeconds_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-retrypolicy.html#cfn-scheduler-schedule-retrypolicy-maximumeventageinseconds""", alias="MaximumEventAgeInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.RetryPolicy:
        from troposphere.scheduler import RetryPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SageMakerPipelineParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameter.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameter.html#cfn-scheduler-schedule-sagemakerpipelineparameter-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameter.html#cfn-scheduler-schedule-sagemakerpipelineparameter-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.SageMakerPipelineParameter:
        from troposphere.scheduler import SageMakerPipelineParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SageMakerPipelineParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameters.html
    Properties:
        - Name: PipelineParameterList
    
    """
    
    PipelineParameterList_: Optional[List['SageMakerPipelineParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameters.html#cfn-scheduler-schedule-sagemakerpipelineparameters-pipelineparameterlist""", alias="PipelineParameterList")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.SageMakerPipelineParameters:
        from troposphere.scheduler import SageMakerPipelineParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SqsParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sqsparameters.html
    Properties:
        - Name: MessageGroupId
    
    """
    
    MessageGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sqsparameters.html#cfn-scheduler-schedule-sqsparameters-messagegroupid""", alias="MessageGroupId")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.SqsParameters:
        from troposphere.scheduler import SqsParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Target(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html
    Properties:
        - Name: Input
        - Name: SqsParameters
        - Name: DeadLetterConfig
        - Name: EcsParameters
        - Name: EventBridgeParameters
        - Name: Arn
        - Name: KinesisParameters
        - Name: SageMakerPipelineParameters
        - Name: RetryPolicy
        - Name: RoleArn
    
    """
    
    Input_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-input""", alias="Input")
    SqsParameters_: Optional['SqsParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-sqsparameters""", alias="SqsParameters")
    DeadLetterConfig_: Optional['DeadLetterConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-deadletterconfig""", alias="DeadLetterConfig")
    EcsParameters_: Optional['EcsParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-ecsparameters""", alias="EcsParameters")
    EventBridgeParameters_: Optional['EventBridgeParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-eventbridgeparameters""", alias="EventBridgeParameters")
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-arn""", alias="Arn")
    KinesisParameters_: Optional['KinesisParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-kinesisparameters""", alias="KinesisParameters")
    SageMakerPipelineParameters_: Optional['SageMakerPipelineParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-sagemakerpipelineparameters""", alias="SageMakerPipelineParameters")
    RetryPolicy_: Optional['RetryPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-retrypolicy""", alias="RetryPolicy")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.scheduler.Target:
        from troposphere.scheduler import Target as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Schedule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html
    Properties:
        - Name: GroupName
        - Name: StartDate
        - Name: ScheduleExpression
        - Name: Target
        - Name: Description
        - Name: KmsKeyArn
        - Name: State
        - Name: FlexibleTimeWindow
        - Name: ScheduleExpressionTimezone
        - Name: EndDate
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-groupname""", alias="GroupName")
    StartDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-startdate""", alias="StartDate")
    ScheduleExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-scheduleexpression""", alias="ScheduleExpression")
    Target_: 'Target' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-target""", alias="Target")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-description""", alias="Description")
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-kmskeyarn""", alias="KmsKeyArn")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-state""", alias="State")
    FlexibleTimeWindow_: 'FlexibleTimeWindow' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-flexibletimewindow""", alias="FlexibleTimeWindow")
    ScheduleExpressionTimezone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-scheduleexpressiontimezone""", alias="ScheduleExpressionTimezone")
    EndDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-enddate""", alias="EndDate")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.scheduler.Schedule:
        from troposphere.scheduler import Schedule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.scheduler import Schedule as TropoT
        return resource_to_troposphere(self, TropoT)


class ScheduleGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html
    Properties:
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: CreationDate
        - Name: State
        - Name: LastModificationDate
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html#cfn-scheduler-schedulegroup-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html#cfn-scheduler-schedulegroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.scheduler.ScheduleGroup:
        from troposphere.scheduler import ScheduleGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.scheduler import ScheduleGroup as TropoT
        return resource_to_troposphere(self, TropoT)

