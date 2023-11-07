from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class EgressEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html
    Properties:
        - Name: PackagingConfigurationId
        - Name: Url
    
    """
    
    PackagingConfigurationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html#cfn-mediapackage-asset-egressendpoint-packagingconfigurationid""", alias="PackagingConfigurationId")
    Url_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html#cfn-mediapackage-asset-egressendpoint-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.EgressEndpoint:
        from troposphere.mediapackage import EgressEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsIngest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-hlsingest.html
    Properties:
        - Name: ingestEndpoints
    
    """
    
    ingestEndpoints_: Optional[List['IngestEndpoint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-hlsingest.html#cfn-mediapackage-channel-hlsingest-ingestendpoints""", alias="ingestEndpoints")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.HlsIngest:
        from troposphere.mediapackage import HlsIngest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IngestEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-ingestendpoint.html
    Properties:
        - Name: Username
        - Name: Id
        - Name: Url
        - Name: Password
    
    """
    
    Username_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-ingestendpoint.html#cfn-mediapackage-channel-ingestendpoint-username""", alias="Username")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-ingestendpoint.html#cfn-mediapackage-channel-ingestendpoint-id""", alias="Id")
    Url_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-ingestendpoint.html#cfn-mediapackage-channel-ingestendpoint-url""", alias="Url")
    Password_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-ingestendpoint.html#cfn-mediapackage-channel-ingestendpoint-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.IngestEndpoint:
        from troposphere.mediapackage import IngestEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-logconfiguration.html
    Properties:
        - Name: LogGroupName
    
    """
    
    LogGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-logconfiguration.html#cfn-mediapackage-channel-logconfiguration-loggroupname""", alias="LogGroupName")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.LogConfiguration:
        from troposphere.mediapackage import LogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Authorization(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html
    Properties:
        - Name: SecretsRoleArn
        - Name: CdnIdentifierSecret
    
    """
    
    SecretsRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html#cfn-mediapackage-originendpoint-authorization-secretsrolearn""", alias="SecretsRoleArn")
    CdnIdentifierSecret_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html#cfn-mediapackage-originendpoint-authorization-cdnidentifiersecret""", alias="CdnIdentifierSecret")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.Authorization:
        from troposphere.mediapackage import Authorization as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CmafEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html
    Properties:
        - Name: KeyRotationIntervalSeconds
        - Name: SpekeKeyProvider
        - Name: ConstantInitializationVector
        - Name: EncryptionMethod
    
    """
    
    KeyRotationIntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-keyrotationintervalseconds""", alias="KeyRotationIntervalSeconds")
    SpekeKeyProvider_: 'SpekeKeyProvider' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-spekekeyprovider""", alias="SpekeKeyProvider")
    ConstantInitializationVector_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-constantinitializationvector""", alias="ConstantInitializationVector")
    EncryptionMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-encryptionmethod""", alias="EncryptionMethod")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.CmafEncryption:
        from troposphere.mediapackage import CmafEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CmafPackage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html
    Properties:
        - Name: SegmentPrefix
        - Name: StreamSelection
        - Name: SegmentDurationSeconds
        - Name: Encryption
        - Name: HlsManifests
    
    """
    
    SegmentPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-segmentprefix""", alias="SegmentPrefix")
    StreamSelection_: Optional['StreamSelection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-streamselection""", alias="StreamSelection")
    SegmentDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-segmentdurationseconds""", alias="SegmentDurationSeconds")
    Encryption_: Optional['CmafEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-encryption""", alias="Encryption")
    HlsManifests_: Optional[List['HlsManifest']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-hlsmanifests""", alias="HlsManifests")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.CmafPackage:
        from troposphere.mediapackage import CmafPackage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DashEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html
    Properties:
        - Name: KeyRotationIntervalSeconds
        - Name: SpekeKeyProvider
    
    """
    
    KeyRotationIntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html#cfn-mediapackage-originendpoint-dashencryption-keyrotationintervalseconds""", alias="KeyRotationIntervalSeconds")
    SpekeKeyProvider_: 'SpekeKeyProvider' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html#cfn-mediapackage-originendpoint-dashencryption-spekekeyprovider""", alias="SpekeKeyProvider")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.DashEncryption:
        from troposphere.mediapackage import DashEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DashPackage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html
    Properties:
        - Name: ManifestWindowSeconds
        - Name: AdsOnDeliveryRestrictions
        - Name: ManifestLayout
        - Name: StreamSelection
        - Name: IncludeIframeOnlyStream
        - Name: SegmentTemplateFormat
        - Name: Encryption
        - Name: AdTriggers
        - Name: Profile
        - Name: PeriodTriggers
        - Name: SuggestedPresentationDelaySeconds
        - Name: UtcTiming
        - Name: MinBufferTimeSeconds
        - Name: SegmentDurationSeconds
        - Name: MinUpdatePeriodSeconds
        - Name: UtcTimingUri
    
    """
    
    ManifestWindowSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-manifestwindowseconds""", alias="ManifestWindowSeconds")
    AdsOnDeliveryRestrictions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-adsondeliveryrestrictions""", alias="AdsOnDeliveryRestrictions")
    ManifestLayout_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-manifestlayout""", alias="ManifestLayout")
    StreamSelection_: Optional['StreamSelection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-streamselection""", alias="StreamSelection")
    IncludeIframeOnlyStream_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-includeiframeonlystream""", alias="IncludeIframeOnlyStream")
    SegmentTemplateFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-segmenttemplateformat""", alias="SegmentTemplateFormat")
    Encryption_: Optional['DashEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-encryption""", alias="Encryption")
    AdTriggers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-adtriggers""", alias="AdTriggers")
    Profile_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-profile""", alias="Profile")
    PeriodTriggers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-periodtriggers""", alias="PeriodTriggers")
    SuggestedPresentationDelaySeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-suggestedpresentationdelayseconds""", alias="SuggestedPresentationDelaySeconds")
    UtcTiming_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-utctiming""", alias="UtcTiming")
    MinBufferTimeSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-minbuffertimeseconds""", alias="MinBufferTimeSeconds")
    SegmentDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-segmentdurationseconds""", alias="SegmentDurationSeconds")
    MinUpdatePeriodSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-minupdateperiodseconds""", alias="MinUpdatePeriodSeconds")
    UtcTimingUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-utctiminguri""", alias="UtcTimingUri")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.DashPackage:
        from troposphere.mediapackage import DashPackage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionContractConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-encryptioncontractconfiguration.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.mediapackage.EncryptionContractConfiguration:
        from troposphere.mediapackage import EncryptionContractConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html
    Properties:
        - Name: KeyRotationIntervalSeconds
        - Name: RepeatExtXKey
        - Name: ConstantInitializationVector
        - Name: SpekeKeyProvider
        - Name: EncryptionMethod
    
    """
    
    KeyRotationIntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-keyrotationintervalseconds""", alias="KeyRotationIntervalSeconds")
    RepeatExtXKey_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-repeatextxkey""", alias="RepeatExtXKey")
    ConstantInitializationVector_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-constantinitializationvector""", alias="ConstantInitializationVector")
    SpekeKeyProvider_: 'SpekeKeyProvider' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-spekekeyprovider""", alias="SpekeKeyProvider")
    EncryptionMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-encryptionmethod""", alias="EncryptionMethod")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.HlsEncryption:
        from troposphere.mediapackage import HlsEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsManifest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html
    Properties:
        - Name: AdsOnDeliveryRestrictions
        - Name: ManifestName
        - Name: AdMarkers
        - Name: ProgramDateTimeIntervalSeconds
        - Name: PlaylistWindowSeconds
        - Name: IncludeIframeOnlyStream
        - Name: Id
        - Name: PlaylistType
        - Name: AdTriggers
        - Name: Url
    
    """
    
    AdsOnDeliveryRestrictions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-adsondeliveryrestrictions""", alias="AdsOnDeliveryRestrictions")
    ManifestName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-manifestname""", alias="ManifestName")
    AdMarkers_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-admarkers""", alias="AdMarkers")
    ProgramDateTimeIntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-programdatetimeintervalseconds""", alias="ProgramDateTimeIntervalSeconds")
    PlaylistWindowSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-playlistwindowseconds""", alias="PlaylistWindowSeconds")
    IncludeIframeOnlyStream_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-includeiframeonlystream""", alias="IncludeIframeOnlyStream")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-id""", alias="Id")
    PlaylistType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-playlisttype""", alias="PlaylistType")
    AdTriggers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-adtriggers""", alias="AdTriggers")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.HlsManifest:
        from troposphere.mediapackage import HlsManifest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsPackage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html
    Properties:
        - Name: AdsOnDeliveryRestrictions
        - Name: AdMarkers
        - Name: ProgramDateTimeIntervalSeconds
        - Name: StreamSelection
        - Name: PlaylistWindowSeconds
        - Name: IncludeIframeOnlyStream
        - Name: UseAudioRenditionGroup
        - Name: SegmentDurationSeconds
        - Name: Encryption
        - Name: PlaylistType
        - Name: AdTriggers
        - Name: IncludeDvbSubtitles
    
    """
    
    AdsOnDeliveryRestrictions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-adsondeliveryrestrictions""", alias="AdsOnDeliveryRestrictions")
    AdMarkers_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-admarkers""", alias="AdMarkers")
    ProgramDateTimeIntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-programdatetimeintervalseconds""", alias="ProgramDateTimeIntervalSeconds")
    StreamSelection_: Optional['StreamSelection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-streamselection""", alias="StreamSelection")
    PlaylistWindowSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-playlistwindowseconds""", alias="PlaylistWindowSeconds")
    IncludeIframeOnlyStream_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-includeiframeonlystream""", alias="IncludeIframeOnlyStream")
    UseAudioRenditionGroup_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-useaudiorenditiongroup""", alias="UseAudioRenditionGroup")
    SegmentDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-segmentdurationseconds""", alias="SegmentDurationSeconds")
    Encryption_: Optional['HlsEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-encryption""", alias="Encryption")
    PlaylistType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-playlisttype""", alias="PlaylistType")
    AdTriggers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-adtriggers""", alias="AdTriggers")
    IncludeDvbSubtitles_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-includedvbsubtitles""", alias="IncludeDvbSubtitles")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.HlsPackage:
        from troposphere.mediapackage import HlsPackage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MssEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-mssencryption.html
    Properties:
        - Name: SpekeKeyProvider
    
    """
    
    SpekeKeyProvider_: 'SpekeKeyProvider' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-mssencryption.html#cfn-mediapackage-originendpoint-mssencryption-spekekeyprovider""", alias="SpekeKeyProvider")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.MssEncryption:
        from troposphere.mediapackage import MssEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MssPackage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html
    Properties:
        - Name: ManifestWindowSeconds
        - Name: StreamSelection
        - Name: SegmentDurationSeconds
        - Name: Encryption
    
    """
    
    ManifestWindowSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-manifestwindowseconds""", alias="ManifestWindowSeconds")
    StreamSelection_: Optional['StreamSelection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-streamselection""", alias="StreamSelection")
    SegmentDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-segmentdurationseconds""", alias="SegmentDurationSeconds")
    Encryption_: Optional['MssEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-encryption""", alias="Encryption")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.MssPackage:
        from troposphere.mediapackage import MssPackage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpekeKeyProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html
    Properties:
        - Name: ResourceId
        - Name: SystemIds
        - Name: EncryptionContractConfiguration
        - Name: Url
        - Name: RoleArn
        - Name: CertificateArn
    
    """
    
    ResourceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-resourceid""", alias="ResourceId")
    SystemIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-systemids""", alias="SystemIds")
    EncryptionContractConfiguration_: Optional['EncryptionContractConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-encryptioncontractconfiguration""", alias="EncryptionContractConfiguration")
    Url_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-url""", alias="Url")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-rolearn""", alias="RoleArn")
    CertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-certificatearn""", alias="CertificateArn")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.SpekeKeyProvider:
        from troposphere.mediapackage import SpekeKeyProvider as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StreamSelection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html
    Properties:
        - Name: MinVideoBitsPerSecond
        - Name: StreamOrder
        - Name: MaxVideoBitsPerSecond
    
    """
    
    MinVideoBitsPerSecond_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-minvideobitspersecond""", alias="MinVideoBitsPerSecond")
    StreamOrder_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-streamorder""", alias="StreamOrder")
    MaxVideoBitsPerSecond_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-maxvideobitspersecond""", alias="MaxVideoBitsPerSecond")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.StreamSelection:
        from troposphere.mediapackage import StreamSelection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CmafEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafencryption.html
    Properties:
        - Name: SpekeKeyProvider
    
    """
    
    SpekeKeyProvider_: 'SpekeKeyProvider' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafencryption.html#cfn-mediapackage-packagingconfiguration-cmafencryption-spekekeyprovider""", alias="SpekeKeyProvider")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.CmafEncryption:
        from troposphere.mediapackage import CmafEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CmafPackage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html
    Properties:
        - Name: SegmentDurationSeconds
        - Name: Encryption
        - Name: HlsManifests
        - Name: IncludeEncoderConfigurationInSegments
    
    """
    
    SegmentDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-segmentdurationseconds""", alias="SegmentDurationSeconds")
    Encryption_: Optional['CmafEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-encryption""", alias="Encryption")
    HlsManifests_: List['HlsManifest'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-hlsmanifests""", alias="HlsManifests")
    IncludeEncoderConfigurationInSegments_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-includeencoderconfigurationinsegments""", alias="IncludeEncoderConfigurationInSegments")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.CmafPackage:
        from troposphere.mediapackage import CmafPackage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DashEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashencryption.html
    Properties:
        - Name: SpekeKeyProvider
    
    """
    
    SpekeKeyProvider_: 'SpekeKeyProvider' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashencryption.html#cfn-mediapackage-packagingconfiguration-dashencryption-spekekeyprovider""", alias="SpekeKeyProvider")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.DashEncryption:
        from troposphere.mediapackage import DashEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DashManifest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html
    Properties:
        - Name: ScteMarkersSource
        - Name: ManifestName
        - Name: ManifestLayout
        - Name: StreamSelection
        - Name: MinBufferTimeSeconds
        - Name: Profile
    
    """
    
    ScteMarkersSource_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-sctemarkerssource""", alias="ScteMarkersSource")
    ManifestName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestname""", alias="ManifestName")
    ManifestLayout_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestlayout""", alias="ManifestLayout")
    StreamSelection_: Optional['StreamSelection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-streamselection""", alias="StreamSelection")
    MinBufferTimeSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-minbuffertimeseconds""", alias="MinBufferTimeSeconds")
    Profile_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-profile""", alias="Profile")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.DashManifest:
        from troposphere.mediapackage import DashManifest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DashPackage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html
    Properties:
        - Name: PeriodTriggers
        - Name: IncludeIframeOnlyStream
        - Name: SegmentDurationSeconds
        - Name: Encryption
        - Name: SegmentTemplateFormat
        - Name: IncludeEncoderConfigurationInSegments
        - Name: DashManifests
    
    """
    
    PeriodTriggers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-periodtriggers""", alias="PeriodTriggers")
    IncludeIframeOnlyStream_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-includeiframeonlystream""", alias="IncludeIframeOnlyStream")
    SegmentDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-segmentdurationseconds""", alias="SegmentDurationSeconds")
    Encryption_: Optional['DashEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-encryption""", alias="Encryption")
    SegmentTemplateFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-segmenttemplateformat""", alias="SegmentTemplateFormat")
    IncludeEncoderConfigurationInSegments_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-includeencoderconfigurationinsegments""", alias="IncludeEncoderConfigurationInSegments")
    DashManifests_: List['DashManifest'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-dashmanifests""", alias="DashManifests")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.DashPackage:
        from troposphere.mediapackage import DashPackage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionContractConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration.html
    Properties:
        - Name: PresetSpeke20Audio
        - Name: PresetSpeke20Video
    
    """
    
    PresetSpeke20Audio_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration.html#cfn-mediapackage-packagingconfiguration-encryptioncontractconfiguration-presetspeke20audio""", alias="PresetSpeke20Audio")
    PresetSpeke20Video_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration.html#cfn-mediapackage-packagingconfiguration-encryptioncontractconfiguration-presetspeke20video""", alias="PresetSpeke20Video")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.EncryptionContractConfiguration:
        from troposphere.mediapackage import EncryptionContractConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html
    Properties:
        - Name: ConstantInitializationVector
        - Name: SpekeKeyProvider
        - Name: EncryptionMethod
    
    """
    
    ConstantInitializationVector_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-constantinitializationvector""", alias="ConstantInitializationVector")
    SpekeKeyProvider_: 'SpekeKeyProvider' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-spekekeyprovider""", alias="SpekeKeyProvider")
    EncryptionMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-encryptionmethod""", alias="EncryptionMethod")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.HlsEncryption:
        from troposphere.mediapackage import HlsEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsManifest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html
    Properties:
        - Name: AdMarkers
        - Name: ManifestName
        - Name: ProgramDateTimeIntervalSeconds
        - Name: StreamSelection
        - Name: RepeatExtXKey
        - Name: IncludeIframeOnlyStream
    
    """
    
    AdMarkers_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-admarkers""", alias="AdMarkers")
    ManifestName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-manifestname""", alias="ManifestName")
    ProgramDateTimeIntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-programdatetimeintervalseconds""", alias="ProgramDateTimeIntervalSeconds")
    StreamSelection_: Optional['StreamSelection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-streamselection""", alias="StreamSelection")
    RepeatExtXKey_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-repeatextxkey""", alias="RepeatExtXKey")
    IncludeIframeOnlyStream_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-includeiframeonlystream""", alias="IncludeIframeOnlyStream")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.HlsManifest:
        from troposphere.mediapackage import HlsManifest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsPackage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html
    Properties:
        - Name: UseAudioRenditionGroup
        - Name: SegmentDurationSeconds
        - Name: Encryption
        - Name: HlsManifests
        - Name: IncludeDvbSubtitles
    
    """
    
    UseAudioRenditionGroup_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-useaudiorenditiongroup""", alias="UseAudioRenditionGroup")
    SegmentDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-segmentdurationseconds""", alias="SegmentDurationSeconds")
    Encryption_: Optional['HlsEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-encryption""", alias="Encryption")
    HlsManifests_: List['HlsManifest'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-hlsmanifests""", alias="HlsManifests")
    IncludeDvbSubtitles_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-includedvbsubtitles""", alias="IncludeDvbSubtitles")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.HlsPackage:
        from troposphere.mediapackage import HlsPackage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MssEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssencryption.html
    Properties:
        - Name: SpekeKeyProvider
    
    """
    
    SpekeKeyProvider_: 'SpekeKeyProvider' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssencryption.html#cfn-mediapackage-packagingconfiguration-mssencryption-spekekeyprovider""", alias="SpekeKeyProvider")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.MssEncryption:
        from troposphere.mediapackage import MssEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MssManifest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html
    Properties:
        - Name: ManifestName
        - Name: StreamSelection
    
    """
    
    ManifestName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html#cfn-mediapackage-packagingconfiguration-mssmanifest-manifestname""", alias="ManifestName")
    StreamSelection_: Optional['StreamSelection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html#cfn-mediapackage-packagingconfiguration-mssmanifest-streamselection""", alias="StreamSelection")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.MssManifest:
        from troposphere.mediapackage import MssManifest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MssPackage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html
    Properties:
        - Name: MssManifests
        - Name: SegmentDurationSeconds
        - Name: Encryption
    
    """
    
    MssManifests_: List['MssManifest'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-mssmanifests""", alias="MssManifests")
    SegmentDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-segmentdurationseconds""", alias="SegmentDurationSeconds")
    Encryption_: Optional['MssEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-encryption""", alias="Encryption")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.MssPackage:
        from troposphere.mediapackage import MssPackage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpekeKeyProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html
    Properties:
        - Name: SystemIds
        - Name: EncryptionContractConfiguration
        - Name: RoleArn
        - Name: Url
    
    """
    
    SystemIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-systemids""", alias="SystemIds")
    EncryptionContractConfiguration_: Optional['EncryptionContractConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-encryptioncontractconfiguration""", alias="EncryptionContractConfiguration")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-rolearn""", alias="RoleArn")
    Url_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.SpekeKeyProvider:
        from troposphere.mediapackage import SpekeKeyProvider as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StreamSelection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html
    Properties:
        - Name: MinVideoBitsPerSecond
        - Name: StreamOrder
        - Name: MaxVideoBitsPerSecond
    
    """
    
    MinVideoBitsPerSecond_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-minvideobitspersecond""", alias="MinVideoBitsPerSecond")
    StreamOrder_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-streamorder""", alias="StreamOrder")
    MaxVideoBitsPerSecond_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-maxvideobitspersecond""", alias="MaxVideoBitsPerSecond")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.StreamSelection:
        from troposphere.mediapackage import StreamSelection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Authorization(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html
    Properties:
        - Name: SecretsRoleArn
        - Name: CdnIdentifierSecret
    
    """
    
    SecretsRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html#cfn-mediapackage-packaginggroup-authorization-secretsrolearn""", alias="SecretsRoleArn")
    CdnIdentifierSecret_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html#cfn-mediapackage-packaginggroup-authorization-cdnidentifiersecret""", alias="CdnIdentifierSecret")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.Authorization:
        from troposphere.mediapackage import Authorization as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-logconfiguration.html
    Properties:
        - Name: LogGroupName
    
    """
    
    LogGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-logconfiguration.html#cfn-mediapackage-packaginggroup-logconfiguration-loggroupname""", alias="LogGroupName")
    


    @property
    def tropo_type(self) -> troposphere.mediapackage.LogConfiguration:
        from troposphere.mediapackage import LogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Asset(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html
    Properties:
        - Name: SourceArn
        - Name: ResourceId
        - Name: Id
        - Name: PackagingGroupId
        - Name: EgressEndpoints
        - Name: Tags
        - Name: SourceRoleArn
    Attributes:
        - Name: CreatedAt
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-sourcearn""", alias="SourceArn")
    ResourceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-resourceid""", alias="ResourceId")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-id""", alias="Id")
    PackagingGroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-packaginggroupid""", alias="PackagingGroupId")
    EgressEndpoints_: Optional[List['EgressEndpoint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-egressendpoints""", alias="EgressEndpoints")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-tags""", alias="Tags")
    SourceRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-sourcerolearn""", alias="SourceRoleArn")
    

    @property
    def tropo_type(self) -> troposphere.mediapackage.Asset:
        from troposphere.mediapackage import Asset as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediapackage import Asset as TropoT
        return resource_to_troposphere(self, TropoT)


class Channel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html
    Properties:
        - Name: Description
        - Name: IngressAccessLogs
        - Name: HlsIngest
        - Name: Id
        - Name: EgressAccessLogs
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-description""", alias="Description")
    IngressAccessLogs_: Optional['LogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-ingressaccesslogs""", alias="IngressAccessLogs")
    HlsIngest_: Optional['HlsIngest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-hlsingest""", alias="HlsIngest")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-id""", alias="Id")
    EgressAccessLogs_: Optional['LogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-egressaccesslogs""", alias="EgressAccessLogs")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.mediapackage.Channel:
        from troposphere.mediapackage import Channel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediapackage import Channel as TropoT
        return resource_to_troposphere(self, TropoT)


class OriginEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html
    Properties:
        - Name: MssPackage
        - Name: Description
        - Name: ChannelId
        - Name: TimeDelaySeconds
        - Name: Origination
        - Name: Authorization
        - Name: ManifestName
        - Name: CmafPackage
        - Name: Whitelist
        - Name: Id
        - Name: HlsPackage
        - Name: DashPackage
        - Name: Tags
        - Name: StartoverWindowSeconds
    Attributes:
        - Name: Arn
        - Name: Url
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MssPackage_: Optional['MssPackage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-msspackage""", alias="MssPackage")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-description""", alias="Description")
    ChannelId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-channelid""", alias="ChannelId")
    TimeDelaySeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-timedelayseconds""", alias="TimeDelaySeconds")
    Origination_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-origination""", alias="Origination")
    Authorization_: Optional['Authorization'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-authorization""", alias="Authorization")
    ManifestName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-manifestname""", alias="ManifestName")
    CmafPackage_: Optional['CmafPackage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-cmafpackage""", alias="CmafPackage")
    Whitelist_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-whitelist""", alias="Whitelist")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-id""", alias="Id")
    HlsPackage_: Optional['HlsPackage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-hlspackage""", alias="HlsPackage")
    DashPackage_: Optional['DashPackage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-dashpackage""", alias="DashPackage")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-tags""", alias="Tags")
    StartoverWindowSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-startoverwindowseconds""", alias="StartoverWindowSeconds")
    

    @property
    def tropo_type(self) -> troposphere.mediapackage.OriginEndpoint:
        from troposphere.mediapackage import OriginEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediapackage import OriginEndpoint as TropoT
        return resource_to_troposphere(self, TropoT)


class PackagingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html
    Properties:
        - Name: MssPackage
        - Name: CmafPackage
        - Name: Id
        - Name: HlsPackage
        - Name: PackagingGroupId
        - Name: DashPackage
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MssPackage_: Optional['MssPackage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-msspackage""", alias="MssPackage")
    CmafPackage_: Optional['CmafPackage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-cmafpackage""", alias="CmafPackage")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-id""", alias="Id")
    HlsPackage_: Optional['HlsPackage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-hlspackage""", alias="HlsPackage")
    PackagingGroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-packaginggroupid""", alias="PackagingGroupId")
    DashPackage_: Optional['DashPackage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-dashpackage""", alias="DashPackage")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.mediapackage.PackagingConfiguration:
        from troposphere.mediapackage import PackagingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediapackage import PackagingConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class PackagingGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html
    Properties:
        - Name: Authorization
        - Name: Id
        - Name: EgressAccessLogs
        - Name: Tags
    Attributes:
        - Name: DomainName
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Authorization_: Optional['Authorization'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-authorization""", alias="Authorization")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-id""", alias="Id")
    EgressAccessLogs_: Optional['LogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-egressaccesslogs""", alias="EgressAccessLogs")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.mediapackage.PackagingGroup:
        from troposphere.mediapackage import PackagingGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediapackage import PackagingGroup as TropoT
        return resource_to_troposphere(self, TropoT)

