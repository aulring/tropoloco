from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class StreamEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesis-stream-streamencryption.html
    Properties:
        - Name: EncryptionType
        - Name: KeyId
    
    """
    
    EncryptionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesis-stream-streamencryption.html#cfn-kinesis-stream-streamencryption-encryptiontype""", alias="EncryptionType")
    KeyId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesis-stream-streamencryption.html#cfn-kinesis-stream-streamencryption-keyid""", alias="KeyId")
    


    @property
    def tropo_type(self) -> troposphere.kinesis.StreamEncryption:
        from troposphere.kinesis import StreamEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StreamModeDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesis-stream-streammodedetails.html
    Properties:
        - Name: StreamMode
    
    """
    
    StreamMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesis-stream-streammodedetails.html#cfn-kinesis-stream-streammodedetails-streammode""", alias="StreamMode")
    


    @property
    def tropo_type(self) -> troposphere.kinesis.StreamModeDetails:
        from troposphere.kinesis import StreamModeDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Stream(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html
    Properties:
        - Name: StreamModeDetails
        - Name: StreamEncryption
        - Name: RetentionPeriodHours
        - Name: Tags
        - Name: Name
        - Name: ShardCount
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StreamModeDetails_: Optional['StreamModeDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-streammodedetails""", alias="StreamModeDetails")
    StreamEncryption_: Optional['StreamEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-streamencryption""", alias="StreamEncryption")
    RetentionPeriodHours_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-retentionperiodhours""", alias="RetentionPeriodHours")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-name""", alias="Name")
    ShardCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html#cfn-kinesis-stream-shardcount""", alias="ShardCount")
    

    @property
    def tropo_type(self) -> troposphere.kinesis.Stream:
        from troposphere.kinesis import Stream as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kinesis import Stream as TropoT
        return resource_to_troposphere(self, TropoT)


class StreamConsumer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-streamconsumer.html
    Properties:
        - Name: ConsumerName
        - Name: StreamARN
    Attributes:
        - Name: ConsumerCreationTimestamp
        - Name: ConsumerName
        - Name: ConsumerARN
        - Name: ConsumerStatus
        - Name: StreamARN
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConsumerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-streamconsumer.html#cfn-kinesis-streamconsumer-consumername""", alias="ConsumerName")
    StreamARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-streamconsumer.html#cfn-kinesis-streamconsumer-streamarn""", alias="StreamARN")
    

    @property
    def tropo_type(self) -> troposphere.kinesis.StreamConsumer:
        from troposphere.kinesis import StreamConsumer as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kinesis import StreamConsumer as TropoT
        return resource_to_troposphere(self, TropoT)

