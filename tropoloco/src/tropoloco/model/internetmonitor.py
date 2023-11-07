from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class HealthEventsConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-healtheventsconfig.html
    Properties:
        - Name: AvailabilityLocalHealthEventsConfig
        - Name: PerformanceScoreThreshold
        - Name: PerformanceLocalHealthEventsConfig
        - Name: AvailabilityScoreThreshold
    
    """
    
    AvailabilityLocalHealthEventsConfig_: Optional['LocalHealthEventsConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-healtheventsconfig.html#cfn-internetmonitor-monitor-healtheventsconfig-availabilitylocalhealtheventsconfig""", alias="AvailabilityLocalHealthEventsConfig")
    PerformanceScoreThreshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-healtheventsconfig.html#cfn-internetmonitor-monitor-healtheventsconfig-performancescorethreshold""", alias="PerformanceScoreThreshold")
    PerformanceLocalHealthEventsConfig_: Optional['LocalHealthEventsConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-healtheventsconfig.html#cfn-internetmonitor-monitor-healtheventsconfig-performancelocalhealtheventsconfig""", alias="PerformanceLocalHealthEventsConfig")
    AvailabilityScoreThreshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-healtheventsconfig.html#cfn-internetmonitor-monitor-healtheventsconfig-availabilityscorethreshold""", alias="AvailabilityScoreThreshold")
    


    @property
    def tropo_type(self) -> troposphere.internetmonitor.HealthEventsConfig:
        from troposphere.internetmonitor import HealthEventsConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InternetMeasurementsLogDelivery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-internetmeasurementslogdelivery.html
    Properties:
        - Name: S3Config
    
    """
    
    S3Config_: Optional['S3Config'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-internetmeasurementslogdelivery.html#cfn-internetmonitor-monitor-internetmeasurementslogdelivery-s3config""", alias="S3Config")
    


    @property
    def tropo_type(self) -> troposphere.internetmonitor.InternetMeasurementsLogDelivery:
        from troposphere.internetmonitor import InternetMeasurementsLogDelivery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LocalHealthEventsConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-localhealtheventsconfig.html
    Properties:
        - Name: Status
        - Name: HealthScoreThreshold
        - Name: MinTrafficImpact
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-localhealtheventsconfig.html#cfn-internetmonitor-monitor-localhealtheventsconfig-status""", alias="Status")
    HealthScoreThreshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-localhealtheventsconfig.html#cfn-internetmonitor-monitor-localhealtheventsconfig-healthscorethreshold""", alias="HealthScoreThreshold")
    MinTrafficImpact_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-localhealtheventsconfig.html#cfn-internetmonitor-monitor-localhealtheventsconfig-mintrafficimpact""", alias="MinTrafficImpact")
    


    @property
    def tropo_type(self) -> troposphere.internetmonitor.LocalHealthEventsConfig:
        from troposphere.internetmonitor import LocalHealthEventsConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Config(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-s3config.html
    Properties:
        - Name: BucketName
        - Name: LogDeliveryStatus
        - Name: BucketPrefix
    
    """
    
    BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-s3config.html#cfn-internetmonitor-monitor-s3config-bucketname""", alias="BucketName")
    LogDeliveryStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-s3config.html#cfn-internetmonitor-monitor-s3config-logdeliverystatus""", alias="LogDeliveryStatus")
    BucketPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-s3config.html#cfn-internetmonitor-monitor-s3config-bucketprefix""", alias="BucketPrefix")
    


    @property
    def tropo_type(self) -> troposphere.internetmonitor.S3Config:
        from troposphere.internetmonitor import S3Config as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Monitor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html
    Properties:
        - Name: Status
        - Name: TrafficPercentageToMonitor
        - Name: HealthEventsConfig
        - Name: ResourcesToAdd
        - Name: InternetMeasurementsLogDelivery
        - Name: MonitorName
        - Name: ResourcesToRemove
        - Name: Resources
        - Name: MaxCityNetworksToMonitor
        - Name: Tags
    Attributes:
        - Name: ModifiedAt
        - Name: MonitorArn
        - Name: CreatedAt
        - Name: ProcessingStatusInfo
        - Name: ProcessingStatus
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-status""", alias="Status")
    TrafficPercentageToMonitor_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-trafficpercentagetomonitor""", alias="TrafficPercentageToMonitor")
    HealthEventsConfig_: Optional['HealthEventsConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-healtheventsconfig""", alias="HealthEventsConfig")
    ResourcesToAdd_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-resourcestoadd""", alias="ResourcesToAdd")
    InternetMeasurementsLogDelivery_: Optional['InternetMeasurementsLogDelivery'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-internetmeasurementslogdelivery""", alias="InternetMeasurementsLogDelivery")
    MonitorName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-monitorname""", alias="MonitorName")
    ResourcesToRemove_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-resourcestoremove""", alias="ResourcesToRemove")
    Resources_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-resources""", alias="Resources")
    MaxCityNetworksToMonitor_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-maxcitynetworkstomonitor""", alias="MaxCityNetworksToMonitor")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.internetmonitor.Monitor:
        from troposphere.internetmonitor import Monitor as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.internetmonitor import Monitor as TropoT
        return resource_to_troposphere(self, TropoT)

