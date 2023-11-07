from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CloudWatchLogsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-cloudwatchlogsconfiguration.html
    Properties:
        - Name: LogGroupArn
    
    """
    
    LogGroupArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-cloudwatchlogsconfiguration.html#cfn-fis-experimenttemplate-cloudwatchlogsconfiguration-loggrouparn""", alias="LogGroupArn")
    


    @property
    def tropo_type(self) -> troposphere.fis.CloudWatchLogsConfiguration:
        from troposphere.fis import CloudWatchLogsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExperimentTemplateAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html
    Properties:
        - Name: ActionId
        - Name: Description
        - Name: Parameters
        - Name: Targets
        - Name: StartAfter
    
    """
    
    ActionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-actionid""", alias="ActionId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-description""", alias="Description")
    Parameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-parameters""", alias="Parameters")
    Targets_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-targets""", alias="Targets")
    StartAfter_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-startafter""", alias="StartAfter")
    


    @property
    def tropo_type(self) -> troposphere.fis.ExperimentTemplateAction:
        from troposphere.fis import ExperimentTemplateAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExperimentTemplateLogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatelogconfiguration.html
    Properties:
        - Name: S3Configuration
        - Name: LogSchemaVersion
        - Name: CloudWatchLogsConfiguration
    
    """
    
    S3Configuration_: Optional['S3Configuration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatelogconfiguration.html#cfn-fis-experimenttemplate-experimenttemplatelogconfiguration-s3configuration""", alias="S3Configuration")
    LogSchemaVersion_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatelogconfiguration.html#cfn-fis-experimenttemplate-experimenttemplatelogconfiguration-logschemaversion""", alias="LogSchemaVersion")
    CloudWatchLogsConfiguration_: Optional['CloudWatchLogsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatelogconfiguration.html#cfn-fis-experimenttemplate-experimenttemplatelogconfiguration-cloudwatchlogsconfiguration""", alias="CloudWatchLogsConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.fis.ExperimentTemplateLogConfiguration:
        from troposphere.fis import ExperimentTemplateLogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExperimentTemplateStopCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html
    Properties:
        - Name: Value
        - Name: Source
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html#cfn-fis-experimenttemplate-experimenttemplatestopcondition-value""", alias="Value")
    Source_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html#cfn-fis-experimenttemplate-experimenttemplatestopcondition-source""", alias="Source")
    


    @property
    def tropo_type(self) -> troposphere.fis.ExperimentTemplateStopCondition:
        from troposphere.fis import ExperimentTemplateStopCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExperimentTemplateTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html
    Properties:
        - Name: Filters
        - Name: Parameters
        - Name: ResourceTags
        - Name: ResourceType
        - Name: ResourceArns
        - Name: SelectionMode
    
    """
    
    Filters_: Optional[List['ExperimentTemplateTargetFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-filters""", alias="Filters")
    Parameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-parameters""", alias="Parameters")
    ResourceTags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetags""", alias="ResourceTags")
    ResourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetype""", alias="ResourceType")
    ResourceArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcearns""", alias="ResourceArns")
    SelectionMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-selectionmode""", alias="SelectionMode")
    


    @property
    def tropo_type(self) -> troposphere.fis.ExperimentTemplateTarget:
        from troposphere.fis import ExperimentTemplateTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExperimentTemplateTargetFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html
    Properties:
        - Name: Path
        - Name: Values
    
    """
    
    Path_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html#cfn-fis-experimenttemplate-experimenttemplatetargetfilter-path""", alias="Path")
    Values_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html#cfn-fis-experimenttemplate-experimenttemplatetargetfilter-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.fis.ExperimentTemplateTargetFilter:
        from troposphere.fis import ExperimentTemplateTargetFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Configuration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-s3configuration.html
    Properties:
        - Name: BucketName
        - Name: Prefix
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-s3configuration.html#cfn-fis-experimenttemplate-s3configuration-bucketname""", alias="BucketName")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-s3configuration.html#cfn-fis-experimenttemplate-s3configuration-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.fis.S3Configuration:
        from troposphere.fis import S3Configuration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ExperimentTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html
    Properties:
        - Name: Description
        - Name: Actions
        - Name: StopConditions
        - Name: Targets
        - Name: LogConfiguration
        - Name: RoleArn
        - Name: Tags
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-description""", alias="Description")
    Actions_: Optional[Dict[str, 'ExperimentTemplateAction']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-actions""", alias="Actions")
    StopConditions_: List['ExperimentTemplateStopCondition'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-stopconditions""", alias="StopConditions")
    Targets_: Dict[str, 'ExperimentTemplateTarget'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-targets""", alias="Targets")
    LogConfiguration_: Optional['ExperimentTemplateLogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-logconfiguration""", alias="LogConfiguration")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-rolearn""", alias="RoleArn")
    Tags_: Dict[str, str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.fis.ExperimentTemplate:
        from troposphere.fis import ExperimentTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.fis import ExperimentTemplate as TropoT
        return resource_to_troposphere(self, TropoT)

