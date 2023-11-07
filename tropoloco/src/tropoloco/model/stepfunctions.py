from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class TagsEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.stepfunctions.TagsEntry:
        from troposphere.stepfunctions import TagsEntry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchLogsLogGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html
    Properties:
        - Name: LogGroupArn
    
    """
    
    LogGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html#cfn-stepfunctions-statemachine-cloudwatchlogsloggroup-loggrouparn""", alias="LogGroupArn")
    


    @property
    def tropo_type(self) -> troposphere.stepfunctions.CloudWatchLogsLogGroup:
        from troposphere.stepfunctions import CloudWatchLogsLogGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html
    Properties:
        - Name: CloudWatchLogsLogGroup
    
    """
    
    CloudWatchLogsLogGroup_: Optional['CloudWatchLogsLogGroup'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html#cfn-stepfunctions-statemachine-logdestination-cloudwatchlogsloggroup""", alias="CloudWatchLogsLogGroup")
    


    @property
    def tropo_type(self) -> troposphere.stepfunctions.LogDestination:
        from troposphere.stepfunctions import LogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html
    Properties:
        - Name: IncludeExecutionData
        - Name: Destinations
        - Name: Level
    
    """
    
    IncludeExecutionData_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-includeexecutiondata""", alias="IncludeExecutionData")
    Destinations_: Optional[List['LogDestination']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-destinations""", alias="Destinations")
    Level_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-level""", alias="Level")
    


    @property
    def tropo_type(self) -> troposphere.stepfunctions.LoggingConfiguration:
        from troposphere.stepfunctions import LoggingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html
    Properties:
        - Name: Bucket
        - Name: Version
        - Name: Key
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-bucket""", alias="Bucket")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-version""", alias="Version")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.stepfunctions.S3Location:
        from troposphere.stepfunctions import S3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagsEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.stepfunctions.TagsEntry:
        from troposphere.stepfunctions import TagsEntry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TracingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html#cfn-stepfunctions-statemachine-tracingconfiguration-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.stepfunctions.TracingConfiguration:
        from troposphere.stepfunctions import TracingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentPreference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html
    Properties:
        - Name: Type
        - Name: StateMachineVersionArn
        - Name: Percentage
        - Name: Alarms
        - Name: Interval
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-type""", alias="Type")
    StateMachineVersionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-statemachineversionarn""", alias="StateMachineVersionArn")
    Percentage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-percentage""", alias="Percentage")
    Alarms_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-alarms""", alias="Alarms")
    Interval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-interval""", alias="Interval")
    


    @property
    def tropo_type(self) -> troposphere.stepfunctions.DeploymentPreference:
        from troposphere.stepfunctions import DeploymentPreference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RoutingConfigurationVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-routingconfigurationversion.html
    Properties:
        - Name: StateMachineVersionArn
        - Name: Weight
    
    """
    
    StateMachineVersionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-routingconfigurationversion.html#cfn-stepfunctions-statemachinealias-routingconfigurationversion-statemachineversionarn""", alias="StateMachineVersionArn")
    Weight_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-routingconfigurationversion.html#cfn-stepfunctions-statemachinealias-routingconfigurationversion-weight""", alias="Weight")
    


    @property
    def tropo_type(self) -> troposphere.stepfunctions.RoutingConfigurationVersion:
        from troposphere.stepfunctions import RoutingConfigurationVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Activity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html
    Properties:
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Tags_: Optional[Tags] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.stepfunctions.Activity:
        from troposphere.stepfunctions import Activity as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.stepfunctions import Activity as TropoT
        return resource_to_troposphere(self, TropoT)


class StateMachine(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html
    Properties:
        - Name: DefinitionString
        - Name: LoggingConfiguration
        - Name: DefinitionSubstitutions
        - Name: Definition
        - Name: DefinitionS3Location
        - Name: StateMachineName
        - Name: RoleArn
        - Name: Tags
        - Name: StateMachineType
        - Name: TracingConfiguration
    Attributes:
        - Name: StateMachineRevisionId
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DefinitionString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionstring""", alias="DefinitionString")
    LoggingConfiguration_: Optional['LoggingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-loggingconfiguration""", alias="LoggingConfiguration")
    DefinitionSubstitutions_: Optional[Dict[str, Dict]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionsubstitutions""", alias="DefinitionSubstitutions")
    Definition_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definition""", alias="Definition")
    DefinitionS3Location_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitions3location""", alias="DefinitionS3Location")
    StateMachineName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinename""", alias="StateMachineName")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-rolearn""", alias="RoleArn")
    Tags_: Optional[Tags] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tags""", alias="Tags")
    StateMachineType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinetype""", alias="StateMachineType")
    TracingConfiguration_: Optional['TracingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tracingconfiguration""", alias="TracingConfiguration")
    

    @property
    def tropo_type(self) -> troposphere.stepfunctions.StateMachine:
        from troposphere.stepfunctions import StateMachine as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.stepfunctions import StateMachine as TropoT
        return resource_to_troposphere(self, TropoT)


class StateMachineAlias(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachinealias.html
    Properties:
        - Name: Description
        - Name: RoutingConfiguration
        - Name: DeploymentPreference
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachinealias.html#cfn-stepfunctions-statemachinealias-description""", alias="Description")
    RoutingConfiguration_: Optional[List['RoutingConfigurationVersion']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachinealias.html#cfn-stepfunctions-statemachinealias-routingconfiguration""", alias="RoutingConfiguration")
    DeploymentPreference_: Optional['DeploymentPreference'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachinealias.html#cfn-stepfunctions-statemachinealias-deploymentpreference""", alias="DeploymentPreference")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachinealias.html#cfn-stepfunctions-statemachinealias-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.stepfunctions.StateMachineAlias:
        from troposphere.stepfunctions import StateMachineAlias as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.stepfunctions import StateMachineAlias as TropoT
        return resource_to_troposphere(self, TropoT)


class StateMachineVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachineversion.html
    Properties:
        - Name: Description
        - Name: StateMachineRevisionId
        - Name: StateMachineArn
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachineversion.html#cfn-stepfunctions-statemachineversion-description""", alias="Description")
    StateMachineRevisionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachineversion.html#cfn-stepfunctions-statemachineversion-statemachinerevisionid""", alias="StateMachineRevisionId")
    StateMachineArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachineversion.html#cfn-stepfunctions-statemachineversion-statemachinearn""", alias="StateMachineArn")
    

    @property
    def tropo_type(self) -> troposphere.stepfunctions.StateMachineVersion:
        from troposphere.stepfunctions import StateMachineVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.stepfunctions import StateMachineVersion as TropoT
        return resource_to_troposphere(self, TropoT)

