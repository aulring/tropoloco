from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ArtifactConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-artifactconfig.html
    Properties:
        - Name: S3Encryption
    
    """
    
    S3Encryption_: Optional['S3Encryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-artifactconfig.html#cfn-synthetics-canary-artifactconfig-s3encryption""", alias="S3Encryption")
    


    @property
    def tropo_type(self) -> troposphere.synthetics.ArtifactConfig:
        from troposphere.synthetics import ArtifactConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BaseScreenshot(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html
    Properties:
        - Name: IgnoreCoordinates
        - Name: ScreenshotName
    
    """
    
    IgnoreCoordinates_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html#cfn-synthetics-canary-basescreenshot-ignorecoordinates""", alias="IgnoreCoordinates")
    ScreenshotName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html#cfn-synthetics-canary-basescreenshot-screenshotname""", alias="ScreenshotName")
    


    @property
    def tropo_type(self) -> troposphere.synthetics.BaseScreenshot:
        from troposphere.synthetics import BaseScreenshot as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Code(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html
    Properties:
        - Name: Script
        - Name: S3ObjectVersion
        - Name: S3Bucket
        - Name: S3Key
        - Name: Handler
        - Name: SourceLocationArn
    
    """
    
    Script_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-script""", alias="Script")
    S3ObjectVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3objectversion""", alias="S3ObjectVersion")
    S3Bucket_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3bucket""", alias="S3Bucket")
    S3Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3key""", alias="S3Key")
    Handler_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-handler""", alias="Handler")
    SourceLocationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-sourcelocationarn""", alias="SourceLocationArn")
    


    @property
    def tropo_type(self) -> troposphere.synthetics.Code:
        from troposphere.synthetics import Code as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RunConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html
    Properties:
        - Name: TimeoutInSeconds
        - Name: EnvironmentVariables
        - Name: MemoryInMB
        - Name: ActiveTracing
    
    """
    
    TimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-timeoutinseconds""", alias="TimeoutInSeconds")
    EnvironmentVariables_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-environmentvariables""", alias="EnvironmentVariables")
    MemoryInMB_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-memoryinmb""", alias="MemoryInMB")
    ActiveTracing_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-activetracing""", alias="ActiveTracing")
    


    @property
    def tropo_type(self) -> troposphere.synthetics.RunConfig:
        from troposphere.synthetics import RunConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Encryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html
    Properties:
        - Name: KmsKeyArn
        - Name: EncryptionMode
    
    """
    
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html#cfn-synthetics-canary-s3encryption-kmskeyarn""", alias="KmsKeyArn")
    EncryptionMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html#cfn-synthetics-canary-s3encryption-encryptionmode""", alias="EncryptionMode")
    


    @property
    def tropo_type(self) -> troposphere.synthetics.S3Encryption:
        from troposphere.synthetics import S3Encryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Schedule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html
    Properties:
        - Name: DurationInSeconds
        - Name: Expression
    
    """
    
    DurationInSeconds_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html#cfn-synthetics-canary-schedule-durationinseconds""", alias="DurationInSeconds")
    Expression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html#cfn-synthetics-canary-schedule-expression""", alias="Expression")
    


    @property
    def tropo_type(self) -> troposphere.synthetics.Schedule:
        from troposphere.synthetics import Schedule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VPCConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html
    Properties:
        - Name: VpcId
        - Name: SubnetIds
        - Name: SecurityGroupIds
    
    """
    
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-vpcid""", alias="VpcId")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-subnetids""", alias="SubnetIds")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.synthetics.VPCConfig:
        from troposphere.synthetics import VPCConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VisualReference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html
    Properties:
        - Name: BaseScreenshots
        - Name: BaseCanaryRunId
    
    """
    
    BaseScreenshots_: Optional[List['BaseScreenshot']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html#cfn-synthetics-canary-visualreference-basescreenshots""", alias="BaseScreenshots")
    BaseCanaryRunId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html#cfn-synthetics-canary-visualreference-basecanaryrunid""", alias="BaseCanaryRunId")
    


    @property
    def tropo_type(self) -> troposphere.synthetics.VisualReference:
        from troposphere.synthetics import VisualReference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Canary(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html
    Properties:
        - Name: VisualReference
        - Name: ArtifactConfig
        - Name: SuccessRetentionPeriod
        - Name: RuntimeVersion
        - Name: VPCConfig
        - Name: RunConfig
        - Name: FailureRetentionPeriod
        - Name: Code
        - Name: Name
        - Name: ExecutionRoleArn
        - Name: Schedule
        - Name: ArtifactS3Location
        - Name: Tags
        - Name: StartCanaryAfterCreation
    Attributes:
        - Name: Code.SourceLocationArn
        - Name: State
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VisualReference_: Optional['VisualReference'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-visualreference""", alias="VisualReference")
    ArtifactConfig_: Optional['ArtifactConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-artifactconfig""", alias="ArtifactConfig")
    SuccessRetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-successretentionperiod""", alias="SuccessRetentionPeriod")
    RuntimeVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-runtimeversion""", alias="RuntimeVersion")
    VPCConfig_: Optional['VPCConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-vpcconfig""", alias="VPCConfig")
    RunConfig_: Optional['RunConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-runconfig""", alias="RunConfig")
    FailureRetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-failureretentionperiod""", alias="FailureRetentionPeriod")
    Code_: 'Code' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-code""", alias="Code")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-name""", alias="Name")
    ExecutionRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-executionrolearn""", alias="ExecutionRoleArn")
    Schedule_: 'Schedule' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-schedule""", alias="Schedule")
    ArtifactS3Location_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-artifacts3location""", alias="ArtifactS3Location")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-tags""", alias="Tags")
    StartCanaryAfterCreation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-startcanaryaftercreation""", alias="StartCanaryAfterCreation")
    

    @property
    def tropo_type(self) -> troposphere.synthetics.Canary:
        from troposphere.synthetics import Canary as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.synthetics import Canary as TropoT
        return resource_to_troposphere(self, TropoT)


class Group(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html
    Properties:
        - Name: ResourceArns
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html#cfn-synthetics-group-resourcearns""", alias="ResourceArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html#cfn-synthetics-group-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html#cfn-synthetics-group-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.synthetics.Group:
        from troposphere.synthetics import Group as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.synthetics import Group as TropoT
        return resource_to_troposphere(self, TropoT)

