from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class FileConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-fileconfiguration.html
    Properties:
        - Name: Filters
        - Name: Folders
    
    """
    
    Filters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-fileconfiguration.html#cfn-appintegrations-dataintegration-fileconfiguration-filters""", alias="Filters")
    Folders_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-fileconfiguration.html#cfn-appintegrations-dataintegration-fileconfiguration-folders""", alias="Folders")
    


    @property
    def tropo_type(self) -> troposphere.appintegrations.FileConfiguration:
        from troposphere.appintegrations import FileConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScheduleConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html
    Properties:
        - Name: FirstExecutionFrom
        - Name: ScheduleExpression
        - Name: Object
    
    """
    
    FirstExecutionFrom_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html#cfn-appintegrations-dataintegration-scheduleconfig-firstexecutionfrom""", alias="FirstExecutionFrom")
    ScheduleExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html#cfn-appintegrations-dataintegration-scheduleconfig-scheduleexpression""", alias="ScheduleExpression")
    Object_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html#cfn-appintegrations-dataintegration-scheduleconfig-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appintegrations.ScheduleConfig:
        from troposphere.appintegrations import ScheduleConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EventFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventfilter.html
    Properties:
        - Name: Source
    
    """
    
    Source_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventfilter.html#cfn-appintegrations-eventintegration-eventfilter-source""", alias="Source")
    


    @property
    def tropo_type(self) -> troposphere.appintegrations.EventFilter:
        from troposphere.appintegrations import EventFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class DataIntegration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html
    Properties:
        - Name: ScheduleConfig
        - Name: FileConfiguration
        - Name: Description
        - Name: SourceURI
        - Name: ObjectConfiguration
        - Name: KmsKey
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: DataIntegrationArn
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ScheduleConfig_: Optional['ScheduleConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-scheduleconfig""", alias="ScheduleConfig")
    FileConfiguration_: Optional['FileConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-fileconfiguration""", alias="FileConfiguration")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-description""", alias="Description")
    SourceURI_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-sourceuri""", alias="SourceURI")
    ObjectConfiguration_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-objectconfiguration""", alias="ObjectConfiguration")
    KmsKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-kmskey""", alias="KmsKey")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.appintegrations.DataIntegration:
        from troposphere.appintegrations import DataIntegration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appintegrations import DataIntegration as TropoT
        return resource_to_troposphere(self, TropoT)


class EventIntegration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html
    Properties:
        - Name: Description
        - Name: EventBridgeBus
        - Name: EventFilter
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: EventIntegrationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-description""", alias="Description")
    EventBridgeBus_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-eventbridgebus""", alias="EventBridgeBus")
    EventFilter_: 'EventFilter' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-eventfilter""", alias="EventFilter")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.appintegrations.EventIntegration:
        from troposphere.appintegrations import EventIntegration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appintegrations import EventIntegration as TropoT
        return resource_to_troposphere(self, TropoT)

