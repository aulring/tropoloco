from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class IngestEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-channel-ingestendpoint.html
    Properties:
        - Name: Id
        - Name: Url
    
    """
    
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-channel-ingestendpoint.html#cfn-mediapackagev2-channel-ingestendpoint-id""", alias="Id")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-channel-ingestendpoint.html#cfn-mediapackagev2-channel-ingestendpoint-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.mediapackagev2.IngestEndpoint:
        from troposphere.mediapackagev2 import IngestEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Encryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryption.html
    Properties:
        - Name: KeyRotationIntervalSeconds
        - Name: ConstantInitializationVector
        - Name: SpekeKeyProvider
        - Name: EncryptionMethod
    
    """
    
    KeyRotationIntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryption.html#cfn-mediapackagev2-originendpoint-encryption-keyrotationintervalseconds""", alias="KeyRotationIntervalSeconds")
    ConstantInitializationVector_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryption.html#cfn-mediapackagev2-originendpoint-encryption-constantinitializationvector""", alias="ConstantInitializationVector")
    SpekeKeyProvider_: 'SpekeKeyProvider' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryption.html#cfn-mediapackagev2-originendpoint-encryption-spekekeyprovider""", alias="SpekeKeyProvider")
    EncryptionMethod_: 'EncryptionMethod' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryption.html#cfn-mediapackagev2-originendpoint-encryption-encryptionmethod""", alias="EncryptionMethod")
    


    @property
    def tropo_type(self) -> troposphere.mediapackagev2.Encryption:
        from troposphere.mediapackagev2 import Encryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionContractConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryptioncontractconfiguration.html
    Properties:
        - Name: PresetSpeke20Audio
        - Name: PresetSpeke20Video
    
    """
    
    PresetSpeke20Audio_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryptioncontractconfiguration.html#cfn-mediapackagev2-originendpoint-encryptioncontractconfiguration-presetspeke20audio""", alias="PresetSpeke20Audio")
    PresetSpeke20Video_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryptioncontractconfiguration.html#cfn-mediapackagev2-originendpoint-encryptioncontractconfiguration-presetspeke20video""", alias="PresetSpeke20Video")
    


    @property
    def tropo_type(self) -> troposphere.mediapackagev2.EncryptionContractConfiguration:
        from troposphere.mediapackagev2 import EncryptionContractConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionMethod(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryptionmethod.html
    Properties:
        - Name: CmafEncryptionMethod
        - Name: TsEncryptionMethod
    
    """
    
    CmafEncryptionMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryptionmethod.html#cfn-mediapackagev2-originendpoint-encryptionmethod-cmafencryptionmethod""", alias="CmafEncryptionMethod")
    TsEncryptionMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-encryptionmethod.html#cfn-mediapackagev2-originendpoint-encryptionmethod-tsencryptionmethod""", alias="TsEncryptionMethod")
    


    @property
    def tropo_type(self) -> troposphere.mediapackagev2.EncryptionMethod:
        from troposphere.mediapackagev2 import EncryptionMethod as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsManifestConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html
    Properties:
        - Name: ManifestWindowSeconds
        - Name: ManifestName
        - Name: ProgramDateTimeIntervalSeconds
        - Name: ChildManifestName
        - Name: ScteHls
        - Name: Url
    
    """
    
    ManifestWindowSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-manifestwindowseconds""", alias="ManifestWindowSeconds")
    ManifestName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-manifestname""", alias="ManifestName")
    ProgramDateTimeIntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-programdatetimeintervalseconds""", alias="ProgramDateTimeIntervalSeconds")
    ChildManifestName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-childmanifestname""", alias="ChildManifestName")
    ScteHls_: Optional['ScteHls'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-sctehls""", alias="ScteHls")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-hlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-hlsmanifestconfiguration-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.mediapackagev2.HlsManifestConfiguration:
        from troposphere.mediapackagev2 import HlsManifestConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LowLatencyHlsManifestConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html
    Properties:
        - Name: ManifestWindowSeconds
        - Name: ManifestName
        - Name: ProgramDateTimeIntervalSeconds
        - Name: ChildManifestName
        - Name: ScteHls
        - Name: Url
    
    """
    
    ManifestWindowSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-manifestwindowseconds""", alias="ManifestWindowSeconds")
    ManifestName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-manifestname""", alias="ManifestName")
    ProgramDateTimeIntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-programdatetimeintervalseconds""", alias="ProgramDateTimeIntervalSeconds")
    ChildManifestName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-childmanifestname""", alias="ChildManifestName")
    ScteHls_: Optional['ScteHls'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-sctehls""", alias="ScteHls")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifestconfiguration-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.mediapackagev2.LowLatencyHlsManifestConfiguration:
        from troposphere.mediapackagev2 import LowLatencyHlsManifestConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Scte(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-scte.html
    Properties:
        - Name: ScteFilter
    
    """
    
    ScteFilter_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-scte.html#cfn-mediapackagev2-originendpoint-scte-sctefilter""", alias="ScteFilter")
    


    @property
    def tropo_type(self) -> troposphere.mediapackagev2.Scte:
        from troposphere.mediapackagev2 import Scte as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScteHls(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-sctehls.html
    Properties:
        - Name: AdMarkerHls
    
    """
    
    AdMarkerHls_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-sctehls.html#cfn-mediapackagev2-originendpoint-sctehls-admarkerhls""", alias="AdMarkerHls")
    


    @property
    def tropo_type(self) -> troposphere.mediapackagev2.ScteHls:
        from troposphere.mediapackagev2 import ScteHls as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Segment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html
    Properties:
        - Name: SegmentName
        - Name: TsUseAudioRenditionGroup
        - Name: IncludeIframeOnlyStreams
        - Name: Scte
        - Name: TsIncludeDvbSubtitles
        - Name: SegmentDurationSeconds
        - Name: Encryption
    
    """
    
    SegmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-segmentname""", alias="SegmentName")
    TsUseAudioRenditionGroup_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-tsuseaudiorenditiongroup""", alias="TsUseAudioRenditionGroup")
    IncludeIframeOnlyStreams_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-includeiframeonlystreams""", alias="IncludeIframeOnlyStreams")
    Scte_: Optional['Scte'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-scte""", alias="Scte")
    TsIncludeDvbSubtitles_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-tsincludedvbsubtitles""", alias="TsIncludeDvbSubtitles")
    SegmentDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-segmentdurationseconds""", alias="SegmentDurationSeconds")
    Encryption_: Optional['Encryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-segment.html#cfn-mediapackagev2-originendpoint-segment-encryption""", alias="Encryption")
    


    @property
    def tropo_type(self) -> troposphere.mediapackagev2.Segment:
        from troposphere.mediapackagev2 import Segment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpekeKeyProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-spekekeyprovider.html
    Properties:
        - Name: DrmSystems
        - Name: ResourceId
        - Name: EncryptionContractConfiguration
        - Name: RoleArn
        - Name: Url
    
    """
    
    DrmSystems_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-spekekeyprovider.html#cfn-mediapackagev2-originendpoint-spekekeyprovider-drmsystems""", alias="DrmSystems")
    ResourceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-spekekeyprovider.html#cfn-mediapackagev2-originendpoint-spekekeyprovider-resourceid""", alias="ResourceId")
    EncryptionContractConfiguration_: 'EncryptionContractConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-spekekeyprovider.html#cfn-mediapackagev2-originendpoint-spekekeyprovider-encryptioncontractconfiguration""", alias="EncryptionContractConfiguration")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-spekekeyprovider.html#cfn-mediapackagev2-originendpoint-spekekeyprovider-rolearn""", alias="RoleArn")
    Url_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackagev2-originendpoint-spekekeyprovider.html#cfn-mediapackagev2-originendpoint-spekekeyprovider-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.mediapackagev2.SpekeKeyProvider:
        from troposphere.mediapackagev2 import SpekeKeyProvider as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Channel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html
    Properties:
        - Name: ChannelName
        - Name: Description
        - Name: ChannelGroupName
        - Name: Tags
    Attributes:
        - Name: ModifiedAt
        - Name: IngestEndpoints
        - Name: CreatedAt
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ChannelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html#cfn-mediapackagev2-channel-channelname""", alias="ChannelName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html#cfn-mediapackagev2-channel-description""", alias="Description")
    ChannelGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html#cfn-mediapackagev2-channel-channelgroupname""", alias="ChannelGroupName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channel.html#cfn-mediapackagev2-channel-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.mediapackagev2.Channel:
        from troposphere.mediapackagev2 import Channel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediapackagev2 import Channel as TropoT
        return resource_to_troposphere(self, TropoT)


class ChannelGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelgroup.html
    Properties:
        - Name: Description
        - Name: ChannelGroupName
        - Name: Tags
    Attributes:
        - Name: ModifiedAt
        - Name: CreatedAt
        - Name: Arn
        - Name: EgressDomain
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelgroup.html#cfn-mediapackagev2-channelgroup-description""", alias="Description")
    ChannelGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelgroup.html#cfn-mediapackagev2-channelgroup-channelgroupname""", alias="ChannelGroupName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelgroup.html#cfn-mediapackagev2-channelgroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.mediapackagev2.ChannelGroup:
        from troposphere.mediapackagev2 import ChannelGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediapackagev2 import ChannelGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class ChannelPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelpolicy.html
    Properties:
        - Name: Policy
        - Name: ChannelName
        - Name: ChannelGroupName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelpolicy.html#cfn-mediapackagev2-channelpolicy-policy""", alias="Policy")
    ChannelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelpolicy.html#cfn-mediapackagev2-channelpolicy-channelname""", alias="ChannelName")
    ChannelGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelpolicy.html#cfn-mediapackagev2-channelpolicy-channelgroupname""", alias="ChannelGroupName")
    

    @property
    def tropo_type(self) -> troposphere.mediapackagev2.ChannelPolicy:
        from troposphere.mediapackagev2 import ChannelPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediapackagev2 import ChannelPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class OriginEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html
    Properties:
        - Name: Description
        - Name: ChannelName
        - Name: LowLatencyHlsManifests
        - Name: ContainerType
        - Name: OriginEndpointName
        - Name: HlsManifests
        - Name: ChannelGroupName
        - Name: Segment
        - Name: Tags
        - Name: StartoverWindowSeconds
    Attributes:
        - Name: ModifiedAt
        - Name: CreatedAt
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-description""", alias="Description")
    ChannelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-channelname""", alias="ChannelName")
    LowLatencyHlsManifests_: Optional[List['LowLatencyHlsManifestConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-lowlatencyhlsmanifests""", alias="LowLatencyHlsManifests")
    ContainerType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-containertype""", alias="ContainerType")
    OriginEndpointName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-originendpointname""", alias="OriginEndpointName")
    HlsManifests_: Optional[List['HlsManifestConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-hlsmanifests""", alias="HlsManifests")
    ChannelGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-channelgroupname""", alias="ChannelGroupName")
    Segment_: Optional['Segment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-segment""", alias="Segment")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-tags""", alias="Tags")
    StartoverWindowSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpoint.html#cfn-mediapackagev2-originendpoint-startoverwindowseconds""", alias="StartoverWindowSeconds")
    

    @property
    def tropo_type(self) -> troposphere.mediapackagev2.OriginEndpoint:
        from troposphere.mediapackagev2 import OriginEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediapackagev2 import OriginEndpoint as TropoT
        return resource_to_troposphere(self, TropoT)


class OriginEndpointPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpointpolicy.html
    Properties:
        - Name: Policy
        - Name: ChannelName
        - Name: OriginEndpointName
        - Name: ChannelGroupName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpointpolicy.html#cfn-mediapackagev2-originendpointpolicy-policy""", alias="Policy")
    ChannelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpointpolicy.html#cfn-mediapackagev2-originendpointpolicy-channelname""", alias="ChannelName")
    OriginEndpointName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpointpolicy.html#cfn-mediapackagev2-originendpointpolicy-originendpointname""", alias="OriginEndpointName")
    ChannelGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-originendpointpolicy.html#cfn-mediapackagev2-originendpointpolicy-channelgroupname""", alias="ChannelGroupName")
    

    @property
    def tropo_type(self) -> troposphere.mediapackagev2.OriginEndpointPolicy:
        from troposphere.mediapackagev2 import OriginEndpointPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediapackagev2 import OriginEndpointPolicy as TropoT
        return resource_to_troposphere(self, TropoT)

