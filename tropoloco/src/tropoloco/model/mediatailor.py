from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DashPlaylistSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-dashplaylistsettings.html
    Properties:
        - Name: ManifestWindowSeconds
        - Name: SuggestedPresentationDelaySeconds
        - Name: MinBufferTimeSeconds
        - Name: MinUpdatePeriodSeconds
    
    """
    
    ManifestWindowSeconds_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-dashplaylistsettings.html#cfn-mediatailor-channel-dashplaylistsettings-manifestwindowseconds""", alias="ManifestWindowSeconds")
    SuggestedPresentationDelaySeconds_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-dashplaylistsettings.html#cfn-mediatailor-channel-dashplaylistsettings-suggestedpresentationdelayseconds""", alias="SuggestedPresentationDelaySeconds")
    MinBufferTimeSeconds_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-dashplaylistsettings.html#cfn-mediatailor-channel-dashplaylistsettings-minbuffertimeseconds""", alias="MinBufferTimeSeconds")
    MinUpdatePeriodSeconds_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-dashplaylistsettings.html#cfn-mediatailor-channel-dashplaylistsettings-minupdateperiodseconds""", alias="MinUpdatePeriodSeconds")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.DashPlaylistSettings:
        from troposphere.mediatailor import DashPlaylistSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsPlaylistSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-hlsplaylistsettings.html
    Properties:
        - Name: ManifestWindowSeconds
        - Name: AdMarkupType
    
    """
    
    ManifestWindowSeconds_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-hlsplaylistsettings.html#cfn-mediatailor-channel-hlsplaylistsettings-manifestwindowseconds""", alias="ManifestWindowSeconds")
    AdMarkupType_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-hlsplaylistsettings.html#cfn-mediatailor-channel-hlsplaylistsettings-admarkuptype""", alias="AdMarkupType")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.HlsPlaylistSettings:
        from troposphere.mediatailor import HlsPlaylistSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogConfigurationForChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-logconfigurationforchannel.html
    Properties:
        - Name: LogTypes
    
    """
    
    LogTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-logconfigurationforchannel.html#cfn-mediatailor-channel-logconfigurationforchannel-logtypes""", alias="LogTypes")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.LogConfigurationForChannel:
        from troposphere.mediatailor import LogConfigurationForChannel as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RequestOutputItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-requestoutputitem.html
    Properties:
        - Name: ManifestName
        - Name: DashPlaylistSettings
        - Name: HlsPlaylistSettings
        - Name: SourceGroup
    
    """
    
    ManifestName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-requestoutputitem.html#cfn-mediatailor-channel-requestoutputitem-manifestname""", alias="ManifestName")
    DashPlaylistSettings_: Optional['DashPlaylistSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-requestoutputitem.html#cfn-mediatailor-channel-requestoutputitem-dashplaylistsettings""", alias="DashPlaylistSettings")
    HlsPlaylistSettings_: Optional['HlsPlaylistSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-requestoutputitem.html#cfn-mediatailor-channel-requestoutputitem-hlsplaylistsettings""", alias="HlsPlaylistSettings")
    SourceGroup_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-requestoutputitem.html#cfn-mediatailor-channel-requestoutputitem-sourcegroup""", alias="SourceGroup")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.RequestOutputItem:
        from troposphere.mediatailor import RequestOutputItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlateSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-slatesource.html
    Properties:
        - Name: VodSourceName
        - Name: SourceLocationName
    
    """
    
    VodSourceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-slatesource.html#cfn-mediatailor-channel-slatesource-vodsourcename""", alias="VodSourceName")
    SourceLocationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-channel-slatesource.html#cfn-mediatailor-channel-slatesource-sourcelocationname""", alias="SourceLocationName")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.SlateSource:
        from troposphere.mediatailor import SlateSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpPackageConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-livesource-httppackageconfiguration.html
    Properties:
        - Name: Path
        - Name: Type
        - Name: SourceGroup
    
    """
    
    Path_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-livesource-httppackageconfiguration.html#cfn-mediatailor-livesource-httppackageconfiguration-path""", alias="Path")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-livesource-httppackageconfiguration.html#cfn-mediatailor-livesource-httppackageconfiguration-type""", alias="Type")
    SourceGroup_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-livesource-httppackageconfiguration.html#cfn-mediatailor-livesource-httppackageconfiguration-sourcegroup""", alias="SourceGroup")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.HttpPackageConfiguration:
        from troposphere.mediatailor import HttpPackageConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AdMarkerPassthrough(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-admarkerpassthrough.html#cfn-mediatailor-playbackconfiguration-admarkerpassthrough-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.AdMarkerPassthrough:
        from troposphere.mediatailor import AdMarkerPassthrough as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AvailSuppression(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-availsuppression.html
    Properties:
        - Name: Mode
        - Name: Value
    
    """
    
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-availsuppression.html#cfn-mediatailor-playbackconfiguration-availsuppression-mode""", alias="Mode")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-availsuppression.html#cfn-mediatailor-playbackconfiguration-availsuppression-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.AvailSuppression:
        from troposphere.mediatailor import AvailSuppression as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Bumper(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-bumper.html
    Properties:
        - Name: StartUrl
        - Name: EndUrl
    
    """
    
    StartUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-bumper.html#cfn-mediatailor-playbackconfiguration-bumper-starturl""", alias="StartUrl")
    EndUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-bumper.html#cfn-mediatailor-playbackconfiguration-bumper-endurl""", alias="EndUrl")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.Bumper:
        from troposphere.mediatailor import Bumper as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CdnConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-cdnconfiguration.html
    Properties:
        - Name: AdSegmentUrlPrefix
        - Name: ContentSegmentUrlPrefix
    
    """
    
    AdSegmentUrlPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-cdnconfiguration.html#cfn-mediatailor-playbackconfiguration-cdnconfiguration-adsegmenturlprefix""", alias="AdSegmentUrlPrefix")
    ContentSegmentUrlPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-cdnconfiguration.html#cfn-mediatailor-playbackconfiguration-cdnconfiguration-contentsegmenturlprefix""", alias="ContentSegmentUrlPrefix")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.CdnConfiguration:
        from troposphere.mediatailor import CdnConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DashConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html
    Properties:
        - Name: MpdLocation
        - Name: ManifestEndpointPrefix
        - Name: OriginManifestType
    
    """
    
    MpdLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html#cfn-mediatailor-playbackconfiguration-dashconfiguration-mpdlocation""", alias="MpdLocation")
    ManifestEndpointPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html#cfn-mediatailor-playbackconfiguration-dashconfiguration-manifestendpointprefix""", alias="ManifestEndpointPrefix")
    OriginManifestType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html#cfn-mediatailor-playbackconfiguration-dashconfiguration-originmanifesttype""", alias="OriginManifestType")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.DashConfiguration:
        from troposphere.mediatailor import DashConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-hlsconfiguration.html
    Properties:
        - Name: ManifestEndpointPrefix
    
    """
    
    ManifestEndpointPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-hlsconfiguration.html#cfn-mediatailor-playbackconfiguration-hlsconfiguration-manifestendpointprefix""", alias="ManifestEndpointPrefix")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.HlsConfiguration:
        from troposphere.mediatailor import HlsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LivePreRollConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.html
    Properties:
        - Name: AdDecisionServerUrl
        - Name: MaxDurationSeconds
    
    """
    
    AdDecisionServerUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.html#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-addecisionserverurl""", alias="AdDecisionServerUrl")
    MaxDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-liveprerollconfiguration.html#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration-maxdurationseconds""", alias="MaxDurationSeconds")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.LivePreRollConfiguration:
        from troposphere.mediatailor import LivePreRollConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ManifestProcessingRules(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules.html
    Properties:
        - Name: AdMarkerPassthrough
    
    """
    
    AdMarkerPassthrough_: Optional['AdMarkerPassthrough'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-manifestprocessingrules.html#cfn-mediatailor-playbackconfiguration-manifestprocessingrules-admarkerpassthrough""", alias="AdMarkerPassthrough")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.ManifestProcessingRules:
        from troposphere.mediatailor import ManifestProcessingRules as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-accessconfiguration.html
    Properties:
        - Name: SecretsManagerAccessTokenConfiguration
        - Name: AccessType
    
    """
    
    SecretsManagerAccessTokenConfiguration_: Optional['SecretsManagerAccessTokenConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-accessconfiguration.html#cfn-mediatailor-sourcelocation-accessconfiguration-secretsmanageraccesstokenconfiguration""", alias="SecretsManagerAccessTokenConfiguration")
    AccessType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-accessconfiguration.html#cfn-mediatailor-sourcelocation-accessconfiguration-accesstype""", alias="AccessType")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.AccessConfiguration:
        from troposphere.mediatailor import AccessConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefaultSegmentDeliveryConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-defaultsegmentdeliveryconfiguration.html
    Properties:
        - Name: BaseUrl
    
    """
    
    BaseUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-defaultsegmentdeliveryconfiguration.html#cfn-mediatailor-sourcelocation-defaultsegmentdeliveryconfiguration-baseurl""", alias="BaseUrl")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.DefaultSegmentDeliveryConfiguration:
        from troposphere.mediatailor import DefaultSegmentDeliveryConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-httpconfiguration.html
    Properties:
        - Name: BaseUrl
    
    """
    
    BaseUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-httpconfiguration.html#cfn-mediatailor-sourcelocation-httpconfiguration-baseurl""", alias="BaseUrl")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.HttpConfiguration:
        from troposphere.mediatailor import HttpConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SecretsManagerAccessTokenConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration.html
    Properties:
        - Name: SecretArn
        - Name: HeaderName
        - Name: SecretStringKey
    
    """
    
    SecretArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration.html#cfn-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration-secretarn""", alias="SecretArn")
    HeaderName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration.html#cfn-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration-headername""", alias="HeaderName")
    SecretStringKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration.html#cfn-mediatailor-sourcelocation-secretsmanageraccesstokenconfiguration-secretstringkey""", alias="SecretStringKey")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.SecretsManagerAccessTokenConfiguration:
        from troposphere.mediatailor import SecretsManagerAccessTokenConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SegmentDeliveryConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-segmentdeliveryconfiguration.html
    Properties:
        - Name: BaseUrl
        - Name: Name
    
    """
    
    BaseUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-segmentdeliveryconfiguration.html#cfn-mediatailor-sourcelocation-segmentdeliveryconfiguration-baseurl""", alias="BaseUrl")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-sourcelocation-segmentdeliveryconfiguration.html#cfn-mediatailor-sourcelocation-segmentdeliveryconfiguration-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.SegmentDeliveryConfiguration:
        from troposphere.mediatailor import SegmentDeliveryConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpPackageConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-vodsource-httppackageconfiguration.html
    Properties:
        - Name: Path
        - Name: Type
        - Name: SourceGroup
    
    """
    
    Path_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-vodsource-httppackageconfiguration.html#cfn-mediatailor-vodsource-httppackageconfiguration-path""", alias="Path")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-vodsource-httppackageconfiguration.html#cfn-mediatailor-vodsource-httppackageconfiguration-type""", alias="Type")
    SourceGroup_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-vodsource-httppackageconfiguration.html#cfn-mediatailor-vodsource-httppackageconfiguration-sourcegroup""", alias="SourceGroup")
    


    @property
    def tropo_type(self) -> troposphere.mediatailor.HttpPackageConfiguration:
        from troposphere.mediatailor import HttpPackageConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Channel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html
    Properties:
        - Name: FillerSlate
        - Name: ChannelName
        - Name: Tier
        - Name: Outputs
        - Name: LogConfiguration
        - Name: PlaybackMode
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FillerSlate_: Optional['SlateSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-fillerslate""", alias="FillerSlate")
    ChannelName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-channelname""", alias="ChannelName")
    Tier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-tier""", alias="Tier")
    Outputs_: List['RequestOutputItem'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-outputs""", alias="Outputs")
    LogConfiguration_: Optional['LogConfigurationForChannel'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-logconfiguration""", alias="LogConfiguration")
    PlaybackMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-playbackmode""", alias="PlaybackMode")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channel.html#cfn-mediatailor-channel-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.mediatailor.Channel:
        from troposphere.mediatailor import Channel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediatailor import Channel as TropoT
        return resource_to_troposphere(self, TropoT)


class ChannelPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channelpolicy.html
    Properties:
        - Name: Policy
        - Name: ChannelName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channelpolicy.html#cfn-mediatailor-channelpolicy-policy""", alias="Policy")
    ChannelName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-channelpolicy.html#cfn-mediatailor-channelpolicy-channelname""", alias="ChannelName")
    

    @property
    def tropo_type(self) -> troposphere.mediatailor.ChannelPolicy:
        from troposphere.mediatailor import ChannelPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediatailor import ChannelPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class LiveSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-livesource.html
    Properties:
        - Name: LiveSourceName
        - Name: SourceLocationName
        - Name: HttpPackageConfigurations
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LiveSourceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-livesource.html#cfn-mediatailor-livesource-livesourcename""", alias="LiveSourceName")
    SourceLocationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-livesource.html#cfn-mediatailor-livesource-sourcelocationname""", alias="SourceLocationName")
    HttpPackageConfigurations_: List['HttpPackageConfiguration'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-livesource.html#cfn-mediatailor-livesource-httppackageconfigurations""", alias="HttpPackageConfigurations")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-livesource.html#cfn-mediatailor-livesource-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.mediatailor.LiveSource:
        from troposphere.mediatailor import LiveSource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediatailor import LiveSource as TropoT
        return resource_to_troposphere(self, TropoT)


class PlaybackConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html
    Properties:
        - Name: Bumper
        - Name: DashConfiguration
        - Name: CdnConfiguration
        - Name: ManifestProcessingRules
        - Name: PersonalizationThresholdSeconds
        - Name: LivePreRollConfiguration
        - Name: HlsConfiguration
        - Name: VideoContentSourceUrl
        - Name: Name
        - Name: TranscodeProfileName
        - Name: ConfigurationAliases
        - Name: AdDecisionServerUrl
        - Name: SlateAdUrl
        - Name: AvailSuppression
        - Name: Tags
    Attributes:
        - Name: HlsConfiguration.ManifestEndpointPrefix
        - Name: SessionInitializationEndpointPrefix
        - Name: DashConfiguration.ManifestEndpointPrefix
        - Name: PlaybackConfigurationArn
        - Name: PlaybackEndpointPrefix
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Bumper_: Optional['Bumper'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-bumper""", alias="Bumper")
    DashConfiguration_: Optional['DashConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-dashconfiguration""", alias="DashConfiguration")
    CdnConfiguration_: Optional['CdnConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-cdnconfiguration""", alias="CdnConfiguration")
    ManifestProcessingRules_: Optional['ManifestProcessingRules'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-manifestprocessingrules""", alias="ManifestProcessingRules")
    PersonalizationThresholdSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-personalizationthresholdseconds""", alias="PersonalizationThresholdSeconds")
    LivePreRollConfiguration_: Optional['LivePreRollConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-liveprerollconfiguration""", alias="LivePreRollConfiguration")
    HlsConfiguration_: Optional['HlsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-hlsconfiguration""", alias="HlsConfiguration")
    VideoContentSourceUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-videocontentsourceurl""", alias="VideoContentSourceUrl")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-name""", alias="Name")
    TranscodeProfileName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-transcodeprofilename""", alias="TranscodeProfileName")
    ConfigurationAliases_: Optional[Dict[str, Dict]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-configurationaliases""", alias="ConfigurationAliases")
    AdDecisionServerUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-addecisionserverurl""", alias="AdDecisionServerUrl")
    SlateAdUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-slateadurl""", alias="SlateAdUrl")
    AvailSuppression_: Optional['AvailSuppression'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-availsuppression""", alias="AvailSuppression")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-playbackconfiguration.html#cfn-mediatailor-playbackconfiguration-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.mediatailor.PlaybackConfiguration:
        from troposphere.mediatailor import PlaybackConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediatailor import PlaybackConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class SourceLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html
    Properties:
        - Name: SourceLocationName
        - Name: DefaultSegmentDeliveryConfiguration
        - Name: SegmentDeliveryConfigurations
        - Name: HttpConfiguration
        - Name: AccessConfiguration
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SourceLocationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html#cfn-mediatailor-sourcelocation-sourcelocationname""", alias="SourceLocationName")
    DefaultSegmentDeliveryConfiguration_: Optional['DefaultSegmentDeliveryConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html#cfn-mediatailor-sourcelocation-defaultsegmentdeliveryconfiguration""", alias="DefaultSegmentDeliveryConfiguration")
    SegmentDeliveryConfigurations_: Optional[List['SegmentDeliveryConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html#cfn-mediatailor-sourcelocation-segmentdeliveryconfigurations""", alias="SegmentDeliveryConfigurations")
    HttpConfiguration_: 'HttpConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html#cfn-mediatailor-sourcelocation-httpconfiguration""", alias="HttpConfiguration")
    AccessConfiguration_: Optional['AccessConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html#cfn-mediatailor-sourcelocation-accessconfiguration""", alias="AccessConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-sourcelocation.html#cfn-mediatailor-sourcelocation-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.mediatailor.SourceLocation:
        from troposphere.mediatailor import SourceLocation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediatailor import SourceLocation as TropoT
        return resource_to_troposphere(self, TropoT)


class VodSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-vodsource.html
    Properties:
        - Name: VodSourceName
        - Name: SourceLocationName
        - Name: HttpPackageConfigurations
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VodSourceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-vodsource.html#cfn-mediatailor-vodsource-vodsourcename""", alias="VodSourceName")
    SourceLocationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-vodsource.html#cfn-mediatailor-vodsource-sourcelocationname""", alias="SourceLocationName")
    HttpPackageConfigurations_: List['HttpPackageConfiguration'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-vodsource.html#cfn-mediatailor-vodsource-httppackageconfigurations""", alias="HttpPackageConfigurations")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-vodsource.html#cfn-mediatailor-vodsource-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.mediatailor.VodSource:
        from troposphere.mediatailor import VodSource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediatailor import VodSource as TropoT
        return resource_to_troposphere(self, TropoT)

