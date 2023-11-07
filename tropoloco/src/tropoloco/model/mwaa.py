from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class LoggingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html
    Properties:
        - Name: SchedulerLogs
        - Name: TaskLogs
        - Name: DagProcessingLogs
        - Name: WebserverLogs
        - Name: WorkerLogs
    
    """
    
    SchedulerLogs_: Optional['ModuleLoggingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-schedulerlogs""", alias="SchedulerLogs")
    TaskLogs_: Optional['ModuleLoggingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-tasklogs""", alias="TaskLogs")
    DagProcessingLogs_: Optional['ModuleLoggingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-dagprocessinglogs""", alias="DagProcessingLogs")
    WebserverLogs_: Optional['ModuleLoggingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-webserverlogs""", alias="WebserverLogs")
    WorkerLogs_: Optional['ModuleLoggingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-workerlogs""", alias="WorkerLogs")
    


    @property
    def tropo_type(self) -> troposphere.mwaa.LoggingConfiguration:
        from troposphere.mwaa import LoggingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModuleLoggingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html
    Properties:
        - Name: CloudWatchLogGroupArn
        - Name: Enabled
        - Name: LogLevel
    
    """
    
    CloudWatchLogGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-cloudwatchloggrouparn""", alias="CloudWatchLogGroupArn")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-enabled""", alias="Enabled")
    LogLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-loglevel""", alias="LogLevel")
    


    @property
    def tropo_type(self) -> troposphere.mwaa.ModuleLoggingConfiguration:
        from troposphere.mwaa import ModuleLoggingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html
    Properties:
        - Name: SubnetIds
        - Name: SecurityGroupIds
    
    """
    
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html#cfn-mwaa-environment-networkconfiguration-subnetids""", alias="SubnetIds")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html#cfn-mwaa-environment-networkconfiguration-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.mwaa.NetworkConfiguration:
        from troposphere.mwaa import NetworkConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Environment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html
    Properties:
        - Name: AirflowConfigurationOptions
        - Name: MaxWorkers
        - Name: EnvironmentClass
        - Name: Schedulers
        - Name: RequirementsS3Path
        - Name: PluginsS3Path
        - Name: MinWorkers
        - Name: AirflowVersion
        - Name: StartupScriptS3Path
        - Name: Name
        - Name: RequirementsS3ObjectVersion
        - Name: SourceBucketArn
        - Name: ExecutionRoleArn
        - Name: WeeklyMaintenanceWindowStart
        - Name: PluginsS3ObjectVersion
        - Name: StartupScriptS3ObjectVersion
        - Name: DagS3Path
        - Name: LoggingConfiguration
        - Name: WebserverAccessMode
        - Name: NetworkConfiguration
        - Name: KmsKey
        - Name: Tags
    Attributes:
        - Name: LoggingConfiguration.TaskLogs.CloudWatchLogGroupArn
        - Name: LoggingConfiguration.WebserverLogs.CloudWatchLogGroupArn
        - Name: LoggingConfiguration.DagProcessingLogs.CloudWatchLogGroupArn
        - Name: WebserverUrl
        - Name: LoggingConfiguration.SchedulerLogs.CloudWatchLogGroupArn
        - Name: Arn
        - Name: LoggingConfiguration.WorkerLogs.CloudWatchLogGroupArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AirflowConfigurationOptions_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowconfigurationoptions""", alias="AirflowConfigurationOptions")
    MaxWorkers_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-maxworkers""", alias="MaxWorkers")
    EnvironmentClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-environmentclass""", alias="EnvironmentClass")
    Schedulers_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-schedulers""", alias="Schedulers")
    RequirementsS3Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3path""", alias="RequirementsS3Path")
    PluginsS3Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3path""", alias="PluginsS3Path")
    MinWorkers_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-minworkers""", alias="MinWorkers")
    AirflowVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowversion""", alias="AirflowVersion")
    StartupScriptS3Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-startupscripts3path""", alias="StartupScriptS3Path")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-name""", alias="Name")
    RequirementsS3ObjectVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3objectversion""", alias="RequirementsS3ObjectVersion")
    SourceBucketArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-sourcebucketarn""", alias="SourceBucketArn")
    ExecutionRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-executionrolearn""", alias="ExecutionRoleArn")
    WeeklyMaintenanceWindowStart_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-weeklymaintenancewindowstart""", alias="WeeklyMaintenanceWindowStart")
    PluginsS3ObjectVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3objectversion""", alias="PluginsS3ObjectVersion")
    StartupScriptS3ObjectVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-startupscripts3objectversion""", alias="StartupScriptS3ObjectVersion")
    DagS3Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-dags3path""", alias="DagS3Path")
    LoggingConfiguration_: Optional['LoggingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-loggingconfiguration""", alias="LoggingConfiguration")
    WebserverAccessMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-webserveraccessmode""", alias="WebserverAccessMode")
    NetworkConfiguration_: Optional['NetworkConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-networkconfiguration""", alias="NetworkConfiguration")
    KmsKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-kmskey""", alias="KmsKey")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.mwaa.Environment:
        from troposphere.mwaa import Environment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mwaa import Environment as TropoT
        return resource_to_troposphere(self, TropoT)

