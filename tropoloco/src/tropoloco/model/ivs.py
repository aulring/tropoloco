from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-destinationconfiguration.html
    Properties:
        - Name: S3
    
    """
    
    S3_: Optional['S3DestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-destinationconfiguration.html#cfn-ivs-recordingconfiguration-destinationconfiguration-s3""", alias="S3")
    


    @property
    def tropo_type(self) -> troposphere.ivs.DestinationConfiguration:
        from troposphere.ivs import DestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RenditionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-renditionconfiguration.html
    Properties:
        - Name: RenditionSelection
        - Name: Renditions
    
    """
    
    RenditionSelection_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-renditionconfiguration.html#cfn-ivs-recordingconfiguration-renditionconfiguration-renditionselection""", alias="RenditionSelection")
    Renditions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-renditionconfiguration.html#cfn-ivs-recordingconfiguration-renditionconfiguration-renditions""", alias="Renditions")
    


    @property
    def tropo_type(self) -> troposphere.ivs.RenditionConfiguration:
        from troposphere.ivs import RenditionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3DestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html
    Properties:
        - Name: BucketName
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html#cfn-ivs-recordingconfiguration-s3destinationconfiguration-bucketname""", alias="BucketName")
    


    @property
    def tropo_type(self) -> troposphere.ivs.S3DestinationConfiguration:
        from troposphere.ivs import S3DestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ThumbnailConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html
    Properties:
        - Name: TargetIntervalSeconds
        - Name: Storage
        - Name: RecordingMode
        - Name: Resolution
    
    """
    
    TargetIntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-targetintervalseconds""", alias="TargetIntervalSeconds")
    Storage_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-storage""", alias="Storage")
    RecordingMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-recordingmode""", alias="RecordingMode")
    Resolution_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-resolution""", alias="Resolution")
    


    @property
    def tropo_type(self) -> troposphere.ivs.ThumbnailConfiguration:
        from troposphere.ivs import ThumbnailConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Channel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html
    Properties:
        - Name: Type
        - Name: RecordingConfigurationArn
        - Name: Authorized
        - Name: Preset
        - Name: InsecureIngest
        - Name: LatencyMode
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: PlaybackUrl
        - Name: IngestEndpoint
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-type""", alias="Type")
    RecordingConfigurationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-recordingconfigurationarn""", alias="RecordingConfigurationArn")
    Authorized_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-authorized""", alias="Authorized")
    Preset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-preset""", alias="Preset")
    InsecureIngest_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-insecureingest""", alias="InsecureIngest")
    LatencyMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-latencymode""", alias="LatencyMode")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ivs.Channel:
        from troposphere.ivs import Channel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ivs import Channel as TropoT
        return resource_to_troposphere(self, TropoT)


class PlaybackKeyPair(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html
    Properties:
        - Name: PublicKeyMaterial
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Fingerprint
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PublicKeyMaterial_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html#cfn-ivs-playbackkeypair-publickeymaterial""", alias="PublicKeyMaterial")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html#cfn-ivs-playbackkeypair-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html#cfn-ivs-playbackkeypair-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ivs.PlaybackKeyPair:
        from troposphere.ivs import PlaybackKeyPair as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ivs import PlaybackKeyPair as TropoT
        return resource_to_troposphere(self, TropoT)


class RecordingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html
    Properties:
        - Name: DestinationConfiguration
        - Name: RenditionConfiguration
        - Name: RecordingReconnectWindowSeconds
        - Name: Tags
        - Name: ThumbnailConfiguration
        - Name: Name
    Attributes:
        - Name: State
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DestinationConfiguration_: 'DestinationConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-destinationconfiguration""", alias="DestinationConfiguration")
    RenditionConfiguration_: Optional['RenditionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-renditionconfiguration""", alias="RenditionConfiguration")
    RecordingReconnectWindowSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-recordingreconnectwindowseconds""", alias="RecordingReconnectWindowSeconds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-tags""", alias="Tags")
    ThumbnailConfiguration_: Optional['ThumbnailConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration""", alias="ThumbnailConfiguration")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ivs.RecordingConfiguration:
        from troposphere.ivs import RecordingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ivs import RecordingConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class StreamKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-streamkey.html
    Properties:
        - Name: ChannelArn
        - Name: Tags
    Attributes:
        - Name: Value
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ChannelArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-streamkey.html#cfn-ivs-streamkey-channelarn""", alias="ChannelArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-streamkey.html#cfn-ivs-streamkey-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ivs.StreamKey:
        from troposphere.ivs import StreamKey as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ivs import StreamKey as TropoT
        return resource_to_troposphere(self, TropoT)

