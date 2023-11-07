from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CloudWatchLogsDestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration.html
    Properties:
        - Name: LogGroupName
    
    """
    
    LogGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration.html#cfn-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration-loggroupname""", alias="LogGroupName")
    


    @property
    def tropo_type(self) -> troposphere.ivschat.CloudWatchLogsDestinationConfiguration:
        from troposphere.ivschat import CloudWatchLogsDestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-destinationconfiguration.html
    Properties:
        - Name: S3
        - Name: Firehose
        - Name: CloudWatchLogs
    
    """
    
    S3_: Optional['S3DestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-destinationconfiguration.html#cfn-ivschat-loggingconfiguration-destinationconfiguration-s3""", alias="S3")
    Firehose_: Optional['FirehoseDestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-destinationconfiguration.html#cfn-ivschat-loggingconfiguration-destinationconfiguration-firehose""", alias="Firehose")
    CloudWatchLogs_: Optional['CloudWatchLogsDestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-destinationconfiguration.html#cfn-ivschat-loggingconfiguration-destinationconfiguration-cloudwatchlogs""", alias="CloudWatchLogs")
    


    @property
    def tropo_type(self) -> troposphere.ivschat.DestinationConfiguration:
        from troposphere.ivschat import DestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FirehoseDestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-firehosedestinationconfiguration.html
    Properties:
        - Name: DeliveryStreamName
    
    """
    
    DeliveryStreamName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-firehosedestinationconfiguration.html#cfn-ivschat-loggingconfiguration-firehosedestinationconfiguration-deliverystreamname""", alias="DeliveryStreamName")
    


    @property
    def tropo_type(self) -> troposphere.ivschat.FirehoseDestinationConfiguration:
        from troposphere.ivschat import FirehoseDestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3DestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-s3destinationconfiguration.html
    Properties:
        - Name: BucketName
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-s3destinationconfiguration.html#cfn-ivschat-loggingconfiguration-s3destinationconfiguration-bucketname""", alias="BucketName")
    


    @property
    def tropo_type(self) -> troposphere.ivschat.S3DestinationConfiguration:
        from troposphere.ivschat import S3DestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MessageReviewHandler(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-room-messagereviewhandler.html
    Properties:
        - Name: FallbackResult
        - Name: Uri
    
    """
    
    FallbackResult_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-room-messagereviewhandler.html#cfn-ivschat-room-messagereviewhandler-fallbackresult""", alias="FallbackResult")
    Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-room-messagereviewhandler.html#cfn-ivschat-room-messagereviewhandler-uri""", alias="Uri")
    


    @property
    def tropo_type(self) -> troposphere.ivschat.MessageReviewHandler:
        from troposphere.ivschat import MessageReviewHandler as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class LoggingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-loggingconfiguration.html
    Properties:
        - Name: DestinationConfiguration
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: State
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DestinationConfiguration_: 'DestinationConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-loggingconfiguration.html#cfn-ivschat-loggingconfiguration-destinationconfiguration""", alias="DestinationConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-loggingconfiguration.html#cfn-ivschat-loggingconfiguration-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-loggingconfiguration.html#cfn-ivschat-loggingconfiguration-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ivschat.LoggingConfiguration:
        from troposphere.ivschat import LoggingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ivschat import LoggingConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class Room(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html
    Properties:
        - Name: MaximumMessageRatePerSecond
        - Name: MaximumMessageLength
        - Name: MessageReviewHandler
        - Name: LoggingConfigurationIdentifiers
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MaximumMessageRatePerSecond_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html#cfn-ivschat-room-maximummessageratepersecond""", alias="MaximumMessageRatePerSecond")
    MaximumMessageLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html#cfn-ivschat-room-maximummessagelength""", alias="MaximumMessageLength")
    MessageReviewHandler_: Optional['MessageReviewHandler'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html#cfn-ivschat-room-messagereviewhandler""", alias="MessageReviewHandler")
    LoggingConfigurationIdentifiers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html#cfn-ivschat-room-loggingconfigurationidentifiers""", alias="LoggingConfigurationIdentifiers")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html#cfn-ivschat-room-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html#cfn-ivschat-room-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ivschat.Room:
        from troposphere.ivschat import Room as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ivschat import Room as TropoT
        return resource_to_troposphere(self, TropoT)

