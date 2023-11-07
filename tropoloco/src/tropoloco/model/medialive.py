from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AacSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html
    Properties:
        - Name: CodingMode
        - Name: RateControlMode
        - Name: SampleRate
        - Name: InputType
        - Name: VbrQuality
        - Name: RawFormat
        - Name: Spec
        - Name: Bitrate
        - Name: Profile
    
    """
    
    CodingMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-codingmode""", alias="CodingMode")
    RateControlMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-ratecontrolmode""", alias="RateControlMode")
    SampleRate_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-samplerate""", alias="SampleRate")
    InputType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-inputtype""", alias="InputType")
    VbrQuality_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-vbrquality""", alias="VbrQuality")
    RawFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-rawformat""", alias="RawFormat")
    Spec_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-spec""", alias="Spec")
    Bitrate_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-bitrate""", alias="Bitrate")
    Profile_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html#cfn-medialive-channel-aacsettings-profile""", alias="Profile")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AacSettings:
        from troposphere.medialive import AacSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ac3Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html
    Properties:
        - Name: CodingMode
        - Name: DrcProfile
        - Name: MetadataControl
        - Name: Dialnorm
        - Name: LfeFilter
        - Name: BitstreamMode
        - Name: AttenuationControl
        - Name: Bitrate
    
    """
    
    CodingMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-codingmode""", alias="CodingMode")
    DrcProfile_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-drcprofile""", alias="DrcProfile")
    MetadataControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-metadatacontrol""", alias="MetadataControl")
    Dialnorm_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-dialnorm""", alias="Dialnorm")
    LfeFilter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-lfefilter""", alias="LfeFilter")
    BitstreamMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-bitstreammode""", alias="BitstreamMode")
    AttenuationControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-attenuationcontrol""", alias="AttenuationControl")
    Bitrate_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html#cfn-medialive-channel-ac3settings-bitrate""", alias="Bitrate")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Ac3Settings:
        from troposphere.medialive import Ac3Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AncillarySourceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ancillarysourcesettings.html
    Properties:
        - Name: SourceAncillaryChannelNumber
    
    """
    
    SourceAncillaryChannelNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ancillarysourcesettings.html#cfn-medialive-channel-ancillarysourcesettings-sourceancillarychannelnumber""", alias="SourceAncillaryChannelNumber")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AncillarySourceSettings:
        from troposphere.medialive import AncillarySourceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ArchiveCdnSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecdnsettings.html
    Properties:
        - Name: ArchiveS3Settings
    
    """
    
    ArchiveS3Settings_: Optional['ArchiveS3Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecdnsettings.html#cfn-medialive-channel-archivecdnsettings-archives3settings""", alias="ArchiveS3Settings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.ArchiveCdnSettings:
        from troposphere.medialive import ArchiveCdnSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ArchiveContainerSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html
    Properties:
        - Name: RawSettings
        - Name: M2tsSettings
    
    """
    
    RawSettings_: Optional['RawSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html#cfn-medialive-channel-archivecontainersettings-rawsettings""", alias="RawSettings")
    M2tsSettings_: Optional['M2tsSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html#cfn-medialive-channel-archivecontainersettings-m2tssettings""", alias="M2tsSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.ArchiveContainerSettings:
        from troposphere.medialive import ArchiveContainerSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ArchiveGroupSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html
    Properties:
        - Name: Destination
        - Name: ArchiveCdnSettings
        - Name: RolloverInterval
    
    """
    
    Destination_: Optional['OutputLocationRef'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html#cfn-medialive-channel-archivegroupsettings-destination""", alias="Destination")
    ArchiveCdnSettings_: Optional['ArchiveCdnSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html#cfn-medialive-channel-archivegroupsettings-archivecdnsettings""", alias="ArchiveCdnSettings")
    RolloverInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html#cfn-medialive-channel-archivegroupsettings-rolloverinterval""", alias="RolloverInterval")
    


    @property
    def tropo_type(self) -> troposphere.medialive.ArchiveGroupSettings:
        from troposphere.medialive import ArchiveGroupSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ArchiveOutputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html
    Properties:
        - Name: Extension
        - Name: NameModifier
        - Name: ContainerSettings
    
    """
    
    Extension_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html#cfn-medialive-channel-archiveoutputsettings-extension""", alias="Extension")
    NameModifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html#cfn-medialive-channel-archiveoutputsettings-namemodifier""", alias="NameModifier")
    ContainerSettings_: Optional['ArchiveContainerSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html#cfn-medialive-channel-archiveoutputsettings-containersettings""", alias="ContainerSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.ArchiveOutputSettings:
        from troposphere.medialive import ArchiveOutputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ArchiveS3Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archives3settings.html
    Properties:
        - Name: CannedAcl
    
    """
    
    CannedAcl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archives3settings.html#cfn-medialive-channel-archives3settings-cannedacl""", alias="CannedAcl")
    


    @property
    def tropo_type(self) -> troposphere.medialive.ArchiveS3Settings:
        from troposphere.medialive import ArchiveS3Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AribDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribdestinationsettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.AribDestinationSettings:
        from troposphere.medialive import AribDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AribSourceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribsourcesettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.AribSourceSettings:
        from troposphere.medialive import AribSourceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioChannelMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html
    Properties:
        - Name: OutputChannel
        - Name: InputChannelLevels
    
    """
    
    OutputChannel_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html#cfn-medialive-channel-audiochannelmapping-outputchannel""", alias="OutputChannel")
    InputChannelLevels_: Optional[List['InputChannelLevel']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html#cfn-medialive-channel-audiochannelmapping-inputchannellevels""", alias="InputChannelLevels")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioChannelMapping:
        from troposphere.medialive import AudioChannelMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioCodecSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html
    Properties:
        - Name: Eac3Settings
        - Name: Ac3Settings
        - Name: Mp2Settings
        - Name: Eac3AtmosSettings
        - Name: PassThroughSettings
        - Name: WavSettings
        - Name: AacSettings
    
    """
    
    Eac3Settings_: Optional['Eac3Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-eac3settings""", alias="Eac3Settings")
    Ac3Settings_: Optional['Ac3Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-ac3settings""", alias="Ac3Settings")
    Mp2Settings_: Optional['Mp2Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-mp2settings""", alias="Mp2Settings")
    Eac3AtmosSettings_: Optional['Eac3AtmosSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-eac3atmossettings""", alias="Eac3AtmosSettings")
    PassThroughSettings_: Optional['PassThroughSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-passthroughsettings""", alias="PassThroughSettings")
    WavSettings_: Optional['WavSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-wavsettings""", alias="WavSettings")
    AacSettings_: Optional['AacSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html#cfn-medialive-channel-audiocodecsettings-aacsettings""", alias="AacSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioCodecSettings:
        from troposphere.medialive import AudioCodecSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioDescription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html
    Properties:
        - Name: AudioNormalizationSettings
        - Name: LanguageCode
        - Name: RemixSettings
        - Name: AudioSelectorName
        - Name: StreamName
        - Name: LanguageCodeControl
        - Name: AudioType
        - Name: AudioTypeControl
        - Name: CodecSettings
        - Name: Name
        - Name: AudioWatermarkingSettings
    
    """
    
    AudioNormalizationSettings_: Optional['AudioNormalizationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-audionormalizationsettings""", alias="AudioNormalizationSettings")
    LanguageCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-languagecode""", alias="LanguageCode")
    RemixSettings_: Optional['RemixSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-remixsettings""", alias="RemixSettings")
    AudioSelectorName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-audioselectorname""", alias="AudioSelectorName")
    StreamName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-streamname""", alias="StreamName")
    LanguageCodeControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-languagecodecontrol""", alias="LanguageCodeControl")
    AudioType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-audiotype""", alias="AudioType")
    AudioTypeControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-audiotypecontrol""", alias="AudioTypeControl")
    CodecSettings_: Optional['AudioCodecSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-codecsettings""", alias="CodecSettings")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-name""", alias="Name")
    AudioWatermarkingSettings_: Optional['AudioWatermarkSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html#cfn-medialive-channel-audiodescription-audiowatermarkingsettings""", alias="AudioWatermarkingSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioDescription:
        from troposphere.medialive import AudioDescription as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioDolbyEDecode(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodolbyedecode.html
    Properties:
        - Name: ProgramSelection
    
    """
    
    ProgramSelection_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodolbyedecode.html#cfn-medialive-channel-audiodolbyedecode-programselection""", alias="ProgramSelection")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioDolbyEDecode:
        from troposphere.medialive import AudioDolbyEDecode as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioHlsRenditionSelection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiohlsrenditionselection.html
    Properties:
        - Name: GroupId
        - Name: Name
    
    """
    
    GroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiohlsrenditionselection.html#cfn-medialive-channel-audiohlsrenditionselection-groupid""", alias="GroupId")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiohlsrenditionselection.html#cfn-medialive-channel-audiohlsrenditionselection-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioHlsRenditionSelection:
        from troposphere.medialive import AudioHlsRenditionSelection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioLanguageSelection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiolanguageselection.html
    Properties:
        - Name: LanguageCode
        - Name: LanguageSelectionPolicy
    
    """
    
    LanguageCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiolanguageselection.html#cfn-medialive-channel-audiolanguageselection-languagecode""", alias="LanguageCode")
    LanguageSelectionPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiolanguageselection.html#cfn-medialive-channel-audiolanguageselection-languageselectionpolicy""", alias="LanguageSelectionPolicy")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioLanguageSelection:
        from troposphere.medialive import AudioLanguageSelection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioNormalizationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html
    Properties:
        - Name: TargetLkfs
        - Name: Algorithm
        - Name: AlgorithmControl
    
    """
    
    TargetLkfs_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html#cfn-medialive-channel-audionormalizationsettings-targetlkfs""", alias="TargetLkfs")
    Algorithm_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html#cfn-medialive-channel-audionormalizationsettings-algorithm""", alias="Algorithm")
    AlgorithmControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html#cfn-medialive-channel-audionormalizationsettings-algorithmcontrol""", alias="AlgorithmControl")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioNormalizationSettings:
        from troposphere.medialive import AudioNormalizationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioOnlyHlsSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html
    Properties:
        - Name: SegmentType
        - Name: AudioTrackType
        - Name: AudioOnlyImage
        - Name: AudioGroupId
    
    """
    
    SegmentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html#cfn-medialive-channel-audioonlyhlssettings-segmenttype""", alias="SegmentType")
    AudioTrackType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html#cfn-medialive-channel-audioonlyhlssettings-audiotracktype""", alias="AudioTrackType")
    AudioOnlyImage_: Optional['InputLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html#cfn-medialive-channel-audioonlyhlssettings-audioonlyimage""", alias="AudioOnlyImage")
    AudioGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html#cfn-medialive-channel-audioonlyhlssettings-audiogroupid""", alias="AudioGroupId")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioOnlyHlsSettings:
        from troposphere.medialive import AudioOnlyHlsSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioPidSelection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiopidselection.html
    Properties:
        - Name: Pid
    
    """
    
    Pid_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiopidselection.html#cfn-medialive-channel-audiopidselection-pid""", alias="Pid")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioPidSelection:
        from troposphere.medialive import AudioPidSelection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioSelector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselector.html
    Properties:
        - Name: SelectorSettings
        - Name: Name
    
    """
    
    SelectorSettings_: Optional['AudioSelectorSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselector.html#cfn-medialive-channel-audioselector-selectorsettings""", alias="SelectorSettings")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselector.html#cfn-medialive-channel-audioselector-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioSelector:
        from troposphere.medialive import AudioSelector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioSelectorSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html
    Properties:
        - Name: AudioPidSelection
        - Name: AudioLanguageSelection
        - Name: AudioTrackSelection
        - Name: AudioHlsRenditionSelection
    
    """
    
    AudioPidSelection_: Optional['AudioPidSelection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html#cfn-medialive-channel-audioselectorsettings-audiopidselection""", alias="AudioPidSelection")
    AudioLanguageSelection_: Optional['AudioLanguageSelection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html#cfn-medialive-channel-audioselectorsettings-audiolanguageselection""", alias="AudioLanguageSelection")
    AudioTrackSelection_: Optional['AudioTrackSelection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html#cfn-medialive-channel-audioselectorsettings-audiotrackselection""", alias="AudioTrackSelection")
    AudioHlsRenditionSelection_: Optional['AudioHlsRenditionSelection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html#cfn-medialive-channel-audioselectorsettings-audiohlsrenditionselection""", alias="AudioHlsRenditionSelection")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioSelectorSettings:
        from troposphere.medialive import AudioSelectorSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioSilenceFailoverSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiosilencefailoversettings.html
    Properties:
        - Name: AudioSelectorName
        - Name: AudioSilenceThresholdMsec
    
    """
    
    AudioSelectorName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiosilencefailoversettings.html#cfn-medialive-channel-audiosilencefailoversettings-audioselectorname""", alias="AudioSelectorName")
    AudioSilenceThresholdMsec_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiosilencefailoversettings.html#cfn-medialive-channel-audiosilencefailoversettings-audiosilencethresholdmsec""", alias="AudioSilenceThresholdMsec")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioSilenceFailoverSettings:
        from troposphere.medialive import AudioSilenceFailoverSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioTrack(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrack.html
    Properties:
        - Name: Track
    
    """
    
    Track_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrack.html#cfn-medialive-channel-audiotrack-track""", alias="Track")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioTrack:
        from troposphere.medialive import AudioTrack as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioTrackSelection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrackselection.html
    Properties:
        - Name: DolbyEDecode
        - Name: Tracks
    
    """
    
    DolbyEDecode_: Optional['AudioDolbyEDecode'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrackselection.html#cfn-medialive-channel-audiotrackselection-dolbyedecode""", alias="DolbyEDecode")
    Tracks_: Optional[List['AudioTrack']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrackselection.html#cfn-medialive-channel-audiotrackselection-tracks""", alias="Tracks")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioTrackSelection:
        from troposphere.medialive import AudioTrackSelection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioWatermarkSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiowatermarksettings.html
    Properties:
        - Name: NielsenWatermarksSettings
    
    """
    
    NielsenWatermarksSettings_: Optional['NielsenWatermarksSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiowatermarksettings.html#cfn-medialive-channel-audiowatermarksettings-nielsenwatermarkssettings""", alias="NielsenWatermarksSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AudioWatermarkSettings:
        from troposphere.medialive import AudioWatermarkSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutomaticInputFailoverSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html
    Properties:
        - Name: FailoverConditions
        - Name: InputPreference
        - Name: SecondaryInputId
        - Name: ErrorClearTimeMsec
    
    """
    
    FailoverConditions_: Optional[List['FailoverCondition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html#cfn-medialive-channel-automaticinputfailoversettings-failoverconditions""", alias="FailoverConditions")
    InputPreference_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html#cfn-medialive-channel-automaticinputfailoversettings-inputpreference""", alias="InputPreference")
    SecondaryInputId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html#cfn-medialive-channel-automaticinputfailoversettings-secondaryinputid""", alias="SecondaryInputId")
    ErrorClearTimeMsec_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html#cfn-medialive-channel-automaticinputfailoversettings-errorcleartimemsec""", alias="ErrorClearTimeMsec")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AutomaticInputFailoverSettings:
        from troposphere.medialive import AutomaticInputFailoverSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AvailBlanking(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html
    Properties:
        - Name: State
        - Name: AvailBlankingImage
    
    """
    
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html#cfn-medialive-channel-availblanking-state""", alias="State")
    AvailBlankingImage_: Optional['InputLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html#cfn-medialive-channel-availblanking-availblankingimage""", alias="AvailBlankingImage")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AvailBlanking:
        from troposphere.medialive import AvailBlanking as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AvailConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availconfiguration.html
    Properties:
        - Name: AvailSettings
    
    """
    
    AvailSettings_: Optional['AvailSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availconfiguration.html#cfn-medialive-channel-availconfiguration-availsettings""", alias="AvailSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AvailConfiguration:
        from troposphere.medialive import AvailConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AvailSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html
    Properties:
        - Name: Scte35SpliceInsert
        - Name: Scte35TimeSignalApos
        - Name: Esam
    
    """
    
    Scte35SpliceInsert_: Optional['Scte35SpliceInsert'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html#cfn-medialive-channel-availsettings-scte35spliceinsert""", alias="Scte35SpliceInsert")
    Scte35TimeSignalApos_: Optional['Scte35TimeSignalApos'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html#cfn-medialive-channel-availsettings-scte35timesignalapos""", alias="Scte35TimeSignalApos")
    Esam_: Optional['Esam'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html#cfn-medialive-channel-availsettings-esam""", alias="Esam")
    


    @property
    def tropo_type(self) -> troposphere.medialive.AvailSettings:
        from troposphere.medialive import AvailSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BlackoutSlate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html
    Properties:
        - Name: NetworkEndBlackout
        - Name: State
        - Name: NetworkId
        - Name: NetworkEndBlackoutImage
        - Name: BlackoutSlateImage
    
    """
    
    NetworkEndBlackout_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-networkendblackout""", alias="NetworkEndBlackout")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-state""", alias="State")
    NetworkId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-networkid""", alias="NetworkId")
    NetworkEndBlackoutImage_: Optional['InputLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-networkendblackoutimage""", alias="NetworkEndBlackoutImage")
    BlackoutSlateImage_: Optional['InputLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html#cfn-medialive-channel-blackoutslate-blackoutslateimage""", alias="BlackoutSlateImage")
    


    @property
    def tropo_type(self) -> troposphere.medialive.BlackoutSlate:
        from troposphere.medialive import BlackoutSlate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BurnInDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html
    Properties:
        - Name: BackgroundOpacity
        - Name: FontResolution
        - Name: OutlineColor
        - Name: FontColor
        - Name: ShadowColor
        - Name: ShadowOpacity
        - Name: Font
        - Name: ShadowYOffset
        - Name: Alignment
        - Name: XPosition
        - Name: FontSize
        - Name: YPosition
        - Name: OutlineSize
        - Name: TeletextGridControl
        - Name: FontOpacity
        - Name: ShadowXOffset
        - Name: BackgroundColor
    
    """
    
    BackgroundOpacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-backgroundopacity""", alias="BackgroundOpacity")
    FontResolution_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-fontresolution""", alias="FontResolution")
    OutlineColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-outlinecolor""", alias="OutlineColor")
    FontColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-fontcolor""", alias="FontColor")
    ShadowColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-shadowcolor""", alias="ShadowColor")
    ShadowOpacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-shadowopacity""", alias="ShadowOpacity")
    Font_: Optional['InputLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-font""", alias="Font")
    ShadowYOffset_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-shadowyoffset""", alias="ShadowYOffset")
    Alignment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-alignment""", alias="Alignment")
    XPosition_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-xposition""", alias="XPosition")
    FontSize_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-fontsize""", alias="FontSize")
    YPosition_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-yposition""", alias="YPosition")
    OutlineSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-outlinesize""", alias="OutlineSize")
    TeletextGridControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-teletextgridcontrol""", alias="TeletextGridControl")
    FontOpacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-fontopacity""", alias="FontOpacity")
    ShadowXOffset_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-shadowxoffset""", alias="ShadowXOffset")
    BackgroundColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html#cfn-medialive-channel-burnindestinationsettings-backgroundcolor""", alias="BackgroundColor")
    


    @property
    def tropo_type(self) -> troposphere.medialive.BurnInDestinationSettings:
        from troposphere.medialive import BurnInDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CaptionDescription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html
    Properties:
        - Name: DestinationSettings
        - Name: LanguageCode
        - Name: LanguageDescription
        - Name: Accessibility
        - Name: CaptionSelectorName
        - Name: Name
    
    """
    
    DestinationSettings_: Optional['CaptionDestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-destinationsettings""", alias="DestinationSettings")
    LanguageCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-languagecode""", alias="LanguageCode")
    LanguageDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-languagedescription""", alias="LanguageDescription")
    Accessibility_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-accessibility""", alias="Accessibility")
    CaptionSelectorName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-captionselectorname""", alias="CaptionSelectorName")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html#cfn-medialive-channel-captiondescription-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.medialive.CaptionDescription:
        from troposphere.medialive import CaptionDescription as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CaptionDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html
    Properties:
        - Name: AribDestinationSettings
        - Name: EbuTtDDestinationSettings
        - Name: SmpteTtDestinationSettings
        - Name: EmbeddedPlusScte20DestinationSettings
        - Name: TtmlDestinationSettings
        - Name: Scte20PlusEmbeddedDestinationSettings
        - Name: DvbSubDestinationSettings
        - Name: TeletextDestinationSettings
        - Name: BurnInDestinationSettings
        - Name: WebvttDestinationSettings
        - Name: EmbeddedDestinationSettings
        - Name: RtmpCaptionInfoDestinationSettings
        - Name: Scte27DestinationSettings
    
    """
    
    AribDestinationSettings_: Optional['AribDestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-aribdestinationsettings""", alias="AribDestinationSettings")
    EbuTtDDestinationSettings_: Optional['EbuTtDDestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-ebuttddestinationsettings""", alias="EbuTtDDestinationSettings")
    SmpteTtDestinationSettings_: Optional['SmpteTtDestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-smptettdestinationsettings""", alias="SmpteTtDestinationSettings")
    EmbeddedPlusScte20DestinationSettings_: Optional['EmbeddedPlusScte20DestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-embeddedplusscte20destinationsettings""", alias="EmbeddedPlusScte20DestinationSettings")
    TtmlDestinationSettings_: Optional['TtmlDestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-ttmldestinationsettings""", alias="TtmlDestinationSettings")
    Scte20PlusEmbeddedDestinationSettings_: Optional['Scte20PlusEmbeddedDestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-scte20plusembeddeddestinationsettings""", alias="Scte20PlusEmbeddedDestinationSettings")
    DvbSubDestinationSettings_: Optional['DvbSubDestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-dvbsubdestinationsettings""", alias="DvbSubDestinationSettings")
    TeletextDestinationSettings_: Optional['TeletextDestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-teletextdestinationsettings""", alias="TeletextDestinationSettings")
    BurnInDestinationSettings_: Optional['BurnInDestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-burnindestinationsettings""", alias="BurnInDestinationSettings")
    WebvttDestinationSettings_: Optional['WebvttDestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-webvttdestinationsettings""", alias="WebvttDestinationSettings")
    EmbeddedDestinationSettings_: Optional['EmbeddedDestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-embeddeddestinationsettings""", alias="EmbeddedDestinationSettings")
    RtmpCaptionInfoDestinationSettings_: Optional['RtmpCaptionInfoDestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-rtmpcaptioninfodestinationsettings""", alias="RtmpCaptionInfoDestinationSettings")
    Scte27DestinationSettings_: Optional['Scte27DestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html#cfn-medialive-channel-captiondestinationsettings-scte27destinationsettings""", alias="Scte27DestinationSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.CaptionDestinationSettings:
        from troposphere.medialive import CaptionDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CaptionLanguageMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html
    Properties:
        - Name: LanguageCode
        - Name: LanguageDescription
        - Name: CaptionChannel
    
    """
    
    LanguageCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html#cfn-medialive-channel-captionlanguagemapping-languagecode""", alias="LanguageCode")
    LanguageDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html#cfn-medialive-channel-captionlanguagemapping-languagedescription""", alias="LanguageDescription")
    CaptionChannel_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html#cfn-medialive-channel-captionlanguagemapping-captionchannel""", alias="CaptionChannel")
    


    @property
    def tropo_type(self) -> troposphere.medialive.CaptionLanguageMapping:
        from troposphere.medialive import CaptionLanguageMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CaptionRectangle(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html
    Properties:
        - Name: TopOffset
        - Name: Height
        - Name: Width
        - Name: LeftOffset
    
    """
    
    TopOffset_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html#cfn-medialive-channel-captionrectangle-topoffset""", alias="TopOffset")
    Height_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html#cfn-medialive-channel-captionrectangle-height""", alias="Height")
    Width_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html#cfn-medialive-channel-captionrectangle-width""", alias="Width")
    LeftOffset_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html#cfn-medialive-channel-captionrectangle-leftoffset""", alias="LeftOffset")
    


    @property
    def tropo_type(self) -> troposphere.medialive.CaptionRectangle:
        from troposphere.medialive import CaptionRectangle as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CaptionSelector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html
    Properties:
        - Name: LanguageCode
        - Name: SelectorSettings
        - Name: Name
    
    """
    
    LanguageCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html#cfn-medialive-channel-captionselector-languagecode""", alias="LanguageCode")
    SelectorSettings_: Optional['CaptionSelectorSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html#cfn-medialive-channel-captionselector-selectorsettings""", alias="SelectorSettings")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html#cfn-medialive-channel-captionselector-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.medialive.CaptionSelector:
        from troposphere.medialive import CaptionSelector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CaptionSelectorSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html
    Properties:
        - Name: DvbSubSourceSettings
        - Name: Scte27SourceSettings
        - Name: AribSourceSettings
        - Name: EmbeddedSourceSettings
        - Name: Scte20SourceSettings
        - Name: TeletextSourceSettings
        - Name: AncillarySourceSettings
    
    """
    
    DvbSubSourceSettings_: Optional['DvbSubSourceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-dvbsubsourcesettings""", alias="DvbSubSourceSettings")
    Scte27SourceSettings_: Optional['Scte27SourceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-scte27sourcesettings""", alias="Scte27SourceSettings")
    AribSourceSettings_: Optional['AribSourceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-aribsourcesettings""", alias="AribSourceSettings")
    EmbeddedSourceSettings_: Optional['EmbeddedSourceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-embeddedsourcesettings""", alias="EmbeddedSourceSettings")
    Scte20SourceSettings_: Optional['Scte20SourceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-scte20sourcesettings""", alias="Scte20SourceSettings")
    TeletextSourceSettings_: Optional['TeletextSourceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-teletextsourcesettings""", alias="TeletextSourceSettings")
    AncillarySourceSettings_: Optional['AncillarySourceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html#cfn-medialive-channel-captionselectorsettings-ancillarysourcesettings""", alias="AncillarySourceSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.CaptionSelectorSettings:
        from troposphere.medialive import CaptionSelectorSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CdiInputSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-cdiinputspecification.html
    Properties:
        - Name: Resolution
    
    """
    
    Resolution_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-cdiinputspecification.html#cfn-medialive-channel-cdiinputspecification-resolution""", alias="Resolution")
    


    @property
    def tropo_type(self) -> troposphere.medialive.CdiInputSpecification:
        from troposphere.medialive import CdiInputSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ColorSpacePassthroughSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-colorspacepassthroughsettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.ColorSpacePassthroughSettings:
        from troposphere.medialive import ColorSpacePassthroughSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DolbyVision81Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dolbyvision81settings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.DolbyVision81Settings:
        from troposphere.medialive import DolbyVision81Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DvbNitSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html
    Properties:
        - Name: NetworkName
        - Name: RepInterval
        - Name: NetworkId
    
    """
    
    NetworkName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html#cfn-medialive-channel-dvbnitsettings-networkname""", alias="NetworkName")
    RepInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html#cfn-medialive-channel-dvbnitsettings-repinterval""", alias="RepInterval")
    NetworkId_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html#cfn-medialive-channel-dvbnitsettings-networkid""", alias="NetworkId")
    


    @property
    def tropo_type(self) -> troposphere.medialive.DvbNitSettings:
        from troposphere.medialive import DvbNitSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DvbSdtSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html
    Properties:
        - Name: ServiceProviderName
        - Name: OutputSdt
        - Name: ServiceName
        - Name: RepInterval
    
    """
    
    ServiceProviderName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html#cfn-medialive-channel-dvbsdtsettings-serviceprovidername""", alias="ServiceProviderName")
    OutputSdt_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html#cfn-medialive-channel-dvbsdtsettings-outputsdt""", alias="OutputSdt")
    ServiceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html#cfn-medialive-channel-dvbsdtsettings-servicename""", alias="ServiceName")
    RepInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html#cfn-medialive-channel-dvbsdtsettings-repinterval""", alias="RepInterval")
    


    @property
    def tropo_type(self) -> troposphere.medialive.DvbSdtSettings:
        from troposphere.medialive import DvbSdtSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DvbSubDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html
    Properties:
        - Name: BackgroundOpacity
        - Name: FontResolution
        - Name: OutlineColor
        - Name: FontColor
        - Name: ShadowColor
        - Name: ShadowOpacity
        - Name: Font
        - Name: ShadowYOffset
        - Name: Alignment
        - Name: XPosition
        - Name: FontSize
        - Name: YPosition
        - Name: OutlineSize
        - Name: TeletextGridControl
        - Name: FontOpacity
        - Name: ShadowXOffset
        - Name: BackgroundColor
    
    """
    
    BackgroundOpacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-backgroundopacity""", alias="BackgroundOpacity")
    FontResolution_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-fontresolution""", alias="FontResolution")
    OutlineColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-outlinecolor""", alias="OutlineColor")
    FontColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-fontcolor""", alias="FontColor")
    ShadowColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-shadowcolor""", alias="ShadowColor")
    ShadowOpacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-shadowopacity""", alias="ShadowOpacity")
    Font_: Optional['InputLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-font""", alias="Font")
    ShadowYOffset_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-shadowyoffset""", alias="ShadowYOffset")
    Alignment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-alignment""", alias="Alignment")
    XPosition_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-xposition""", alias="XPosition")
    FontSize_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-fontsize""", alias="FontSize")
    YPosition_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-yposition""", alias="YPosition")
    OutlineSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-outlinesize""", alias="OutlineSize")
    TeletextGridControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-teletextgridcontrol""", alias="TeletextGridControl")
    FontOpacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-fontopacity""", alias="FontOpacity")
    ShadowXOffset_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-shadowxoffset""", alias="ShadowXOffset")
    BackgroundColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html#cfn-medialive-channel-dvbsubdestinationsettings-backgroundcolor""", alias="BackgroundColor")
    


    @property
    def tropo_type(self) -> troposphere.medialive.DvbSubDestinationSettings:
        from troposphere.medialive import DvbSubDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DvbSubSourceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubsourcesettings.html
    Properties:
        - Name: OcrLanguage
        - Name: Pid
    
    """
    
    OcrLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubsourcesettings.html#cfn-medialive-channel-dvbsubsourcesettings-ocrlanguage""", alias="OcrLanguage")
    Pid_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubsourcesettings.html#cfn-medialive-channel-dvbsubsourcesettings-pid""", alias="Pid")
    


    @property
    def tropo_type(self) -> troposphere.medialive.DvbSubSourceSettings:
        from troposphere.medialive import DvbSubSourceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DvbTdtSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbtdtsettings.html
    Properties:
        - Name: RepInterval
    
    """
    
    RepInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbtdtsettings.html#cfn-medialive-channel-dvbtdtsettings-repinterval""", alias="RepInterval")
    


    @property
    def tropo_type(self) -> troposphere.medialive.DvbTdtSettings:
        from troposphere.medialive import DvbTdtSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Eac3AtmosSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3atmossettings.html
    Properties:
        - Name: CodingMode
        - Name: Dialnorm
        - Name: SurroundTrim
        - Name: DrcRf
        - Name: Bitrate
        - Name: DrcLine
        - Name: HeightTrim
    
    """
    
    CodingMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3atmossettings.html#cfn-medialive-channel-eac3atmossettings-codingmode""", alias="CodingMode")
    Dialnorm_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3atmossettings.html#cfn-medialive-channel-eac3atmossettings-dialnorm""", alias="Dialnorm")
    SurroundTrim_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3atmossettings.html#cfn-medialive-channel-eac3atmossettings-surroundtrim""", alias="SurroundTrim")
    DrcRf_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3atmossettings.html#cfn-medialive-channel-eac3atmossettings-drcrf""", alias="DrcRf")
    Bitrate_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3atmossettings.html#cfn-medialive-channel-eac3atmossettings-bitrate""", alias="Bitrate")
    DrcLine_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3atmossettings.html#cfn-medialive-channel-eac3atmossettings-drcline""", alias="DrcLine")
    HeightTrim_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3atmossettings.html#cfn-medialive-channel-eac3atmossettings-heighttrim""", alias="HeightTrim")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Eac3AtmosSettings:
        from troposphere.medialive import Eac3AtmosSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Eac3Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html
    Properties:
        - Name: CodingMode
        - Name: SurroundMode
        - Name: PassthroughControl
        - Name: Dialnorm
        - Name: LoRoSurroundMixLevel
        - Name: PhaseControl
        - Name: LtRtCenterMixLevel
        - Name: LfeFilter
        - Name: LfeControl
        - Name: Bitrate
        - Name: DrcLine
        - Name: DcFilter
        - Name: MetadataControl
        - Name: LtRtSurroundMixLevel
        - Name: LoRoCenterMixLevel
        - Name: DrcRf
        - Name: AttenuationControl
        - Name: BitstreamMode
        - Name: SurroundExMode
        - Name: StereoDownmix
    
    """
    
    CodingMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-codingmode""", alias="CodingMode")
    SurroundMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-surroundmode""", alias="SurroundMode")
    PassthroughControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-passthroughcontrol""", alias="PassthroughControl")
    Dialnorm_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-dialnorm""", alias="Dialnorm")
    LoRoSurroundMixLevel_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-lorosurroundmixlevel""", alias="LoRoSurroundMixLevel")
    PhaseControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-phasecontrol""", alias="PhaseControl")
    LtRtCenterMixLevel_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-ltrtcentermixlevel""", alias="LtRtCenterMixLevel")
    LfeFilter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-lfefilter""", alias="LfeFilter")
    LfeControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-lfecontrol""", alias="LfeControl")
    Bitrate_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-bitrate""", alias="Bitrate")
    DrcLine_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-drcline""", alias="DrcLine")
    DcFilter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-dcfilter""", alias="DcFilter")
    MetadataControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-metadatacontrol""", alias="MetadataControl")
    LtRtSurroundMixLevel_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-ltrtsurroundmixlevel""", alias="LtRtSurroundMixLevel")
    LoRoCenterMixLevel_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-lorocentermixlevel""", alias="LoRoCenterMixLevel")
    DrcRf_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-drcrf""", alias="DrcRf")
    AttenuationControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-attenuationcontrol""", alias="AttenuationControl")
    BitstreamMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-bitstreammode""", alias="BitstreamMode")
    SurroundExMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-surroundexmode""", alias="SurroundExMode")
    StereoDownmix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html#cfn-medialive-channel-eac3settings-stereodownmix""", alias="StereoDownmix")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Eac3Settings:
        from troposphere.medialive import Eac3Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EbuTtDDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html
    Properties:
        - Name: FontFamily
        - Name: FillLineGap
        - Name: StyleControl
        - Name: CopyrightHolder
    
    """
    
    FontFamily_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html#cfn-medialive-channel-ebuttddestinationsettings-fontfamily""", alias="FontFamily")
    FillLineGap_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html#cfn-medialive-channel-ebuttddestinationsettings-filllinegap""", alias="FillLineGap")
    StyleControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html#cfn-medialive-channel-ebuttddestinationsettings-stylecontrol""", alias="StyleControl")
    CopyrightHolder_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html#cfn-medialive-channel-ebuttddestinationsettings-copyrightholder""", alias="CopyrightHolder")
    


    @property
    def tropo_type(self) -> troposphere.medialive.EbuTtDDestinationSettings:
        from troposphere.medialive import EbuTtDDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EmbeddedDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddeddestinationsettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.EmbeddedDestinationSettings:
        from troposphere.medialive import EmbeddedDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EmbeddedPlusScte20DestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedplusscte20destinationsettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.EmbeddedPlusScte20DestinationSettings:
        from troposphere.medialive import EmbeddedPlusScte20DestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EmbeddedSourceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html
    Properties:
        - Name: Source608ChannelNumber
        - Name: Scte20Detection
        - Name: Source608TrackNumber
        - Name: Convert608To708
    
    """
    
    Source608ChannelNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html#cfn-medialive-channel-embeddedsourcesettings-source608channelnumber""", alias="Source608ChannelNumber")
    Scte20Detection_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html#cfn-medialive-channel-embeddedsourcesettings-scte20detection""", alias="Scte20Detection")
    Source608TrackNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html#cfn-medialive-channel-embeddedsourcesettings-source608tracknumber""", alias="Source608TrackNumber")
    Convert608To708_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html#cfn-medialive-channel-embeddedsourcesettings-convert608to708""", alias="Convert608To708")
    


    @property
    def tropo_type(self) -> troposphere.medialive.EmbeddedSourceSettings:
        from troposphere.medialive import EmbeddedSourceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncoderSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html
    Properties:
        - Name: AudioDescriptions
        - Name: VideoDescriptions
        - Name: GlobalConfiguration
        - Name: MotionGraphicsConfiguration
        - Name: ThumbnailConfiguration
        - Name: FeatureActivations
        - Name: CaptionDescriptions
        - Name: AvailConfiguration
        - Name: OutputGroups
        - Name: AvailBlanking
        - Name: NielsenConfiguration
        - Name: BlackoutSlate
        - Name: TimecodeConfig
    
    """
    
    AudioDescriptions_: Optional[List['AudioDescription']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-audiodescriptions""", alias="AudioDescriptions")
    VideoDescriptions_: Optional[List['VideoDescription']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-videodescriptions""", alias="VideoDescriptions")
    GlobalConfiguration_: Optional['GlobalConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-globalconfiguration""", alias="GlobalConfiguration")
    MotionGraphicsConfiguration_: Optional['MotionGraphicsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-motiongraphicsconfiguration""", alias="MotionGraphicsConfiguration")
    ThumbnailConfiguration_: Optional['ThumbnailConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-thumbnailconfiguration""", alias="ThumbnailConfiguration")
    FeatureActivations_: Optional['FeatureActivations'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-featureactivations""", alias="FeatureActivations")
    CaptionDescriptions_: Optional[List['CaptionDescription']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-captiondescriptions""", alias="CaptionDescriptions")
    AvailConfiguration_: Optional['AvailConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-availconfiguration""", alias="AvailConfiguration")
    OutputGroups_: Optional[List['OutputGroup']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-outputgroups""", alias="OutputGroups")
    AvailBlanking_: Optional['AvailBlanking'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-availblanking""", alias="AvailBlanking")
    NielsenConfiguration_: Optional['NielsenConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-nielsenconfiguration""", alias="NielsenConfiguration")
    BlackoutSlate_: Optional['BlackoutSlate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-blackoutslate""", alias="BlackoutSlate")
    TimecodeConfig_: Optional['TimecodeConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html#cfn-medialive-channel-encodersettings-timecodeconfig""", alias="TimecodeConfig")
    


    @property
    def tropo_type(self) -> troposphere.medialive.EncoderSettings:
        from troposphere.medialive import EncoderSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Esam(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-esam.html
    Properties:
        - Name: AdAvailOffset
        - Name: ZoneIdentity
        - Name: AcquisitionPointId
        - Name: PoisEndpoint
        - Name: Username
        - Name: PasswordParam
    
    """
    
    AdAvailOffset_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-esam.html#cfn-medialive-channel-esam-adavailoffset""", alias="AdAvailOffset")
    ZoneIdentity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-esam.html#cfn-medialive-channel-esam-zoneidentity""", alias="ZoneIdentity")
    AcquisitionPointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-esam.html#cfn-medialive-channel-esam-acquisitionpointid""", alias="AcquisitionPointId")
    PoisEndpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-esam.html#cfn-medialive-channel-esam-poisendpoint""", alias="PoisEndpoint")
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-esam.html#cfn-medialive-channel-esam-username""", alias="Username")
    PasswordParam_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-esam.html#cfn-medialive-channel-esam-passwordparam""", alias="PasswordParam")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Esam:
        from troposphere.medialive import Esam as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FailoverCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failovercondition.html
    Properties:
        - Name: FailoverConditionSettings
    
    """
    
    FailoverConditionSettings_: Optional['FailoverConditionSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failovercondition.html#cfn-medialive-channel-failovercondition-failoverconditionsettings""", alias="FailoverConditionSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.FailoverCondition:
        from troposphere.medialive import FailoverCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FailoverConditionSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failoverconditionsettings.html
    Properties:
        - Name: AudioSilenceSettings
        - Name: VideoBlackSettings
        - Name: InputLossSettings
    
    """
    
    AudioSilenceSettings_: Optional['AudioSilenceFailoverSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failoverconditionsettings.html#cfn-medialive-channel-failoverconditionsettings-audiosilencesettings""", alias="AudioSilenceSettings")
    VideoBlackSettings_: Optional['VideoBlackFailoverSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failoverconditionsettings.html#cfn-medialive-channel-failoverconditionsettings-videoblacksettings""", alias="VideoBlackSettings")
    InputLossSettings_: Optional['InputLossFailoverSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failoverconditionsettings.html#cfn-medialive-channel-failoverconditionsettings-inputlosssettings""", alias="InputLossSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.FailoverConditionSettings:
        from troposphere.medialive import FailoverConditionSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FeatureActivations(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-featureactivations.html
    Properties:
        - Name: InputPrepareScheduleActions
    
    """
    
    InputPrepareScheduleActions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-featureactivations.html#cfn-medialive-channel-featureactivations-inputpreparescheduleactions""", alias="InputPrepareScheduleActions")
    


    @property
    def tropo_type(self) -> troposphere.medialive.FeatureActivations:
        from troposphere.medialive import FeatureActivations as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FecOutputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html
    Properties:
        - Name: RowLength
        - Name: ColumnDepth
        - Name: IncludeFec
    
    """
    
    RowLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html#cfn-medialive-channel-fecoutputsettings-rowlength""", alias="RowLength")
    ColumnDepth_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html#cfn-medialive-channel-fecoutputsettings-columndepth""", alias="ColumnDepth")
    IncludeFec_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html#cfn-medialive-channel-fecoutputsettings-includefec""", alias="IncludeFec")
    


    @property
    def tropo_type(self) -> troposphere.medialive.FecOutputSettings:
        from troposphere.medialive import FecOutputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Fmp4HlsSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html
    Properties:
        - Name: AudioRenditionSets
        - Name: NielsenId3Behavior
        - Name: TimedMetadataBehavior
    
    """
    
    AudioRenditionSets_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html#cfn-medialive-channel-fmp4hlssettings-audiorenditionsets""", alias="AudioRenditionSets")
    NielsenId3Behavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html#cfn-medialive-channel-fmp4hlssettings-nielsenid3behavior""", alias="NielsenId3Behavior")
    TimedMetadataBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html#cfn-medialive-channel-fmp4hlssettings-timedmetadatabehavior""", alias="TimedMetadataBehavior")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Fmp4HlsSettings:
        from troposphere.medialive import Fmp4HlsSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FrameCaptureCdnSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturecdnsettings.html
    Properties:
        - Name: FrameCaptureS3Settings
    
    """
    
    FrameCaptureS3Settings_: Optional['FrameCaptureS3Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturecdnsettings.html#cfn-medialive-channel-framecapturecdnsettings-framecaptures3settings""", alias="FrameCaptureS3Settings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.FrameCaptureCdnSettings:
        from troposphere.medialive import FrameCaptureCdnSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FrameCaptureGroupSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html
    Properties:
        - Name: FrameCaptureCdnSettings
        - Name: Destination
    
    """
    
    FrameCaptureCdnSettings_: Optional['FrameCaptureCdnSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html#cfn-medialive-channel-framecapturegroupsettings-framecapturecdnsettings""", alias="FrameCaptureCdnSettings")
    Destination_: Optional['OutputLocationRef'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html#cfn-medialive-channel-framecapturegroupsettings-destination""", alias="Destination")
    


    @property
    def tropo_type(self) -> troposphere.medialive.FrameCaptureGroupSettings:
        from troposphere.medialive import FrameCaptureGroupSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FrameCaptureHlsSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturehlssettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.FrameCaptureHlsSettings:
        from troposphere.medialive import FrameCaptureHlsSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FrameCaptureOutputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptureoutputsettings.html
    Properties:
        - Name: NameModifier
    
    """
    
    NameModifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptureoutputsettings.html#cfn-medialive-channel-framecaptureoutputsettings-namemodifier""", alias="NameModifier")
    


    @property
    def tropo_type(self) -> troposphere.medialive.FrameCaptureOutputSettings:
        from troposphere.medialive import FrameCaptureOutputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FrameCaptureS3Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptures3settings.html
    Properties:
        - Name: CannedAcl
    
    """
    
    CannedAcl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptures3settings.html#cfn-medialive-channel-framecaptures3settings-cannedacl""", alias="CannedAcl")
    


    @property
    def tropo_type(self) -> troposphere.medialive.FrameCaptureS3Settings:
        from troposphere.medialive import FrameCaptureS3Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FrameCaptureSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html
    Properties:
        - Name: TimecodeBurninSettings
        - Name: CaptureInterval
        - Name: CaptureIntervalUnits
    
    """
    
    TimecodeBurninSettings_: Optional['TimecodeBurninSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html#cfn-medialive-channel-framecapturesettings-timecodeburninsettings""", alias="TimecodeBurninSettings")
    CaptureInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html#cfn-medialive-channel-framecapturesettings-captureinterval""", alias="CaptureInterval")
    CaptureIntervalUnits_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html#cfn-medialive-channel-framecapturesettings-captureintervalunits""", alias="CaptureIntervalUnits")
    


    @property
    def tropo_type(self) -> troposphere.medialive.FrameCaptureSettings:
        from troposphere.medialive import FrameCaptureSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GlobalConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html
    Properties:
        - Name: InputEndAction
        - Name: OutputTimingSource
        - Name: OutputLockingMode
        - Name: SupportLowFramerateInputs
        - Name: InitialAudioGain
        - Name: InputLossBehavior
    
    """
    
    InputEndAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-inputendaction""", alias="InputEndAction")
    OutputTimingSource_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-outputtimingsource""", alias="OutputTimingSource")
    OutputLockingMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-outputlockingmode""", alias="OutputLockingMode")
    SupportLowFramerateInputs_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-supportlowframerateinputs""", alias="SupportLowFramerateInputs")
    InitialAudioGain_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-initialaudiogain""", alias="InitialAudioGain")
    InputLossBehavior_: Optional['InputLossBehavior'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html#cfn-medialive-channel-globalconfiguration-inputlossbehavior""", alias="InputLossBehavior")
    


    @property
    def tropo_type(self) -> troposphere.medialive.GlobalConfiguration:
        from troposphere.medialive import GlobalConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class H264ColorSpaceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html
    Properties:
        - Name: Rec601Settings
        - Name: Rec709Settings
        - Name: ColorSpacePassthroughSettings
    
    """
    
    Rec601Settings_: Optional['Rec601Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html#cfn-medialive-channel-h264colorspacesettings-rec601settings""", alias="Rec601Settings")
    Rec709Settings_: Optional['Rec709Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html#cfn-medialive-channel-h264colorspacesettings-rec709settings""", alias="Rec709Settings")
    ColorSpacePassthroughSettings_: Optional['ColorSpacePassthroughSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html#cfn-medialive-channel-h264colorspacesettings-colorspacepassthroughsettings""", alias="ColorSpacePassthroughSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.H264ColorSpaceSettings:
        from troposphere.medialive import H264ColorSpaceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class H264FilterSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264filtersettings.html
    Properties:
        - Name: TemporalFilterSettings
    
    """
    
    TemporalFilterSettings_: Optional['TemporalFilterSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264filtersettings.html#cfn-medialive-channel-h264filtersettings-temporalfiltersettings""", alias="TemporalFilterSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.H264FilterSettings:
        from troposphere.medialive import H264FilterSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class H264Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html
    Properties:
        - Name: TimecodeBurninSettings
        - Name: NumRefFrames
        - Name: TemporalAq
        - Name: Slices
        - Name: FramerateControl
        - Name: QvbrQualityLevel
        - Name: FramerateNumerator
        - Name: ParControl
        - Name: GopClosedCadence
        - Name: FlickerAq
        - Name: Profile
        - Name: QualityLevel
        - Name: MinIInterval
        - Name: SceneChangeDetect
        - Name: ForceFieldPictures
        - Name: FramerateDenominator
        - Name: Softness
        - Name: GopSize
        - Name: AdaptiveQuantization
        - Name: FilterSettings
        - Name: ColorSpaceSettings
        - Name: EntropyEncoding
        - Name: SpatialAq
        - Name: ParDenominator
        - Name: FixedAfd
        - Name: GopSizeUnits
        - Name: AfdSignaling
        - Name: Bitrate
        - Name: ParNumerator
        - Name: RateControlMode
        - Name: ScanType
        - Name: BufSize
        - Name: TimecodeInsertion
        - Name: ColorMetadata
        - Name: BufFillPct
        - Name: GopBReference
        - Name: LookAheadRateControl
        - Name: Level
        - Name: MaxBitrate
        - Name: Syntax
        - Name: SubgopLength
        - Name: GopNumBFrames
    
    """
    
    TimecodeBurninSettings_: Optional['TimecodeBurninSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-timecodeburninsettings""", alias="TimecodeBurninSettings")
    NumRefFrames_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-numrefframes""", alias="NumRefFrames")
    TemporalAq_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-temporalaq""", alias="TemporalAq")
    Slices_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-slices""", alias="Slices")
    FramerateControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-frameratecontrol""", alias="FramerateControl")
    QvbrQualityLevel_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-qvbrqualitylevel""", alias="QvbrQualityLevel")
    FramerateNumerator_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-frameratenumerator""", alias="FramerateNumerator")
    ParControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-parcontrol""", alias="ParControl")
    GopClosedCadence_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopclosedcadence""", alias="GopClosedCadence")
    FlickerAq_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-flickeraq""", alias="FlickerAq")
    Profile_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-profile""", alias="Profile")
    QualityLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-qualitylevel""", alias="QualityLevel")
    MinIInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-miniinterval""", alias="MinIInterval")
    SceneChangeDetect_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-scenechangedetect""", alias="SceneChangeDetect")
    ForceFieldPictures_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-forcefieldpictures""", alias="ForceFieldPictures")
    FramerateDenominator_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-frameratedenominator""", alias="FramerateDenominator")
    Softness_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-softness""", alias="Softness")
    GopSize_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopsize""", alias="GopSize")
    AdaptiveQuantization_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-adaptivequantization""", alias="AdaptiveQuantization")
    FilterSettings_: Optional['H264FilterSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-filtersettings""", alias="FilterSettings")
    ColorSpaceSettings_: Optional['H264ColorSpaceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-colorspacesettings""", alias="ColorSpaceSettings")
    EntropyEncoding_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-entropyencoding""", alias="EntropyEncoding")
    SpatialAq_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-spatialaq""", alias="SpatialAq")
    ParDenominator_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-pardenominator""", alias="ParDenominator")
    FixedAfd_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-fixedafd""", alias="FixedAfd")
    GopSizeUnits_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopsizeunits""", alias="GopSizeUnits")
    AfdSignaling_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-afdsignaling""", alias="AfdSignaling")
    Bitrate_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-bitrate""", alias="Bitrate")
    ParNumerator_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-parnumerator""", alias="ParNumerator")
    RateControlMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-ratecontrolmode""", alias="RateControlMode")
    ScanType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-scantype""", alias="ScanType")
    BufSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-bufsize""", alias="BufSize")
    TimecodeInsertion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-timecodeinsertion""", alias="TimecodeInsertion")
    ColorMetadata_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-colormetadata""", alias="ColorMetadata")
    BufFillPct_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-buffillpct""", alias="BufFillPct")
    GopBReference_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopbreference""", alias="GopBReference")
    LookAheadRateControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-lookaheadratecontrol""", alias="LookAheadRateControl")
    Level_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-level""", alias="Level")
    MaxBitrate_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-maxbitrate""", alias="MaxBitrate")
    Syntax_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-syntax""", alias="Syntax")
    SubgopLength_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-subgoplength""", alias="SubgopLength")
    GopNumBFrames_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html#cfn-medialive-channel-h264settings-gopnumbframes""", alias="GopNumBFrames")
    


    @property
    def tropo_type(self) -> troposphere.medialive.H264Settings:
        from troposphere.medialive import H264Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class H265ColorSpaceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html
    Properties:
        - Name: Rec601Settings
        - Name: Rec709Settings
        - Name: ColorSpacePassthroughSettings
        - Name: DolbyVision81Settings
        - Name: Hdr10Settings
    
    """
    
    Rec601Settings_: Optional['Rec601Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html#cfn-medialive-channel-h265colorspacesettings-rec601settings""", alias="Rec601Settings")
    Rec709Settings_: Optional['Rec709Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html#cfn-medialive-channel-h265colorspacesettings-rec709settings""", alias="Rec709Settings")
    ColorSpacePassthroughSettings_: Optional['ColorSpacePassthroughSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html#cfn-medialive-channel-h265colorspacesettings-colorspacepassthroughsettings""", alias="ColorSpacePassthroughSettings")
    DolbyVision81Settings_: Optional['DolbyVision81Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html#cfn-medialive-channel-h265colorspacesettings-dolbyvision81settings""", alias="DolbyVision81Settings")
    Hdr10Settings_: Optional['Hdr10Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html#cfn-medialive-channel-h265colorspacesettings-hdr10settings""", alias="Hdr10Settings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.H265ColorSpaceSettings:
        from troposphere.medialive import H265ColorSpaceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class H265FilterSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265filtersettings.html
    Properties:
        - Name: TemporalFilterSettings
    
    """
    
    TemporalFilterSettings_: Optional['TemporalFilterSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265filtersettings.html#cfn-medialive-channel-h265filtersettings-temporalfiltersettings""", alias="TemporalFilterSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.H265FilterSettings:
        from troposphere.medialive import H265FilterSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class H265Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html
    Properties:
        - Name: TimecodeBurninSettings
        - Name: Slices
        - Name: QvbrQualityLevel
        - Name: FramerateNumerator
        - Name: GopClosedCadence
        - Name: FlickerAq
        - Name: Profile
        - Name: MinIInterval
        - Name: SceneChangeDetect
        - Name: FramerateDenominator
        - Name: GopSize
        - Name: AdaptiveQuantization
        - Name: FilterSettings
        - Name: AlternativeTransferFunction
        - Name: ColorSpaceSettings
        - Name: Tier
        - Name: ParDenominator
        - Name: FixedAfd
        - Name: GopSizeUnits
        - Name: AfdSignaling
        - Name: Bitrate
        - Name: ParNumerator
        - Name: RateControlMode
        - Name: ScanType
        - Name: BufSize
        - Name: TimecodeInsertion
        - Name: ColorMetadata
        - Name: LookAheadRateControl
        - Name: Level
        - Name: MaxBitrate
    
    """
    
    TimecodeBurninSettings_: Optional['TimecodeBurninSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-timecodeburninsettings""", alias="TimecodeBurninSettings")
    Slices_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-slices""", alias="Slices")
    QvbrQualityLevel_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-qvbrqualitylevel""", alias="QvbrQualityLevel")
    FramerateNumerator_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-frameratenumerator""", alias="FramerateNumerator")
    GopClosedCadence_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-gopclosedcadence""", alias="GopClosedCadence")
    FlickerAq_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-flickeraq""", alias="FlickerAq")
    Profile_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-profile""", alias="Profile")
    MinIInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-miniinterval""", alias="MinIInterval")
    SceneChangeDetect_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-scenechangedetect""", alias="SceneChangeDetect")
    FramerateDenominator_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-frameratedenominator""", alias="FramerateDenominator")
    GopSize_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-gopsize""", alias="GopSize")
    AdaptiveQuantization_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-adaptivequantization""", alias="AdaptiveQuantization")
    FilterSettings_: Optional['H265FilterSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-filtersettings""", alias="FilterSettings")
    AlternativeTransferFunction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-alternativetransferfunction""", alias="AlternativeTransferFunction")
    ColorSpaceSettings_: Optional['H265ColorSpaceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-colorspacesettings""", alias="ColorSpaceSettings")
    Tier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-tier""", alias="Tier")
    ParDenominator_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-pardenominator""", alias="ParDenominator")
    FixedAfd_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-fixedafd""", alias="FixedAfd")
    GopSizeUnits_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-gopsizeunits""", alias="GopSizeUnits")
    AfdSignaling_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-afdsignaling""", alias="AfdSignaling")
    Bitrate_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-bitrate""", alias="Bitrate")
    ParNumerator_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-parnumerator""", alias="ParNumerator")
    RateControlMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-ratecontrolmode""", alias="RateControlMode")
    ScanType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-scantype""", alias="ScanType")
    BufSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-bufsize""", alias="BufSize")
    TimecodeInsertion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-timecodeinsertion""", alias="TimecodeInsertion")
    ColorMetadata_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-colormetadata""", alias="ColorMetadata")
    LookAheadRateControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-lookaheadratecontrol""", alias="LookAheadRateControl")
    Level_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-level""", alias="Level")
    MaxBitrate_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html#cfn-medialive-channel-h265settings-maxbitrate""", alias="MaxBitrate")
    


    @property
    def tropo_type(self) -> troposphere.medialive.H265Settings:
        from troposphere.medialive import H265Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Hdr10Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html
    Properties:
        - Name: MaxCll
        - Name: MaxFall
    
    """
    
    MaxCll_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html#cfn-medialive-channel-hdr10settings-maxcll""", alias="MaxCll")
    MaxFall_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html#cfn-medialive-channel-hdr10settings-maxfall""", alias="MaxFall")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Hdr10Settings:
        from troposphere.medialive import Hdr10Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsAkamaiSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html
    Properties:
        - Name: Salt
        - Name: FilecacheDuration
        - Name: NumRetries
        - Name: Token
        - Name: RestartDelay
        - Name: ConnectionRetryInterval
        - Name: HttpTransferMode
    
    """
    
    Salt_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-salt""", alias="Salt")
    FilecacheDuration_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-filecacheduration""", alias="FilecacheDuration")
    NumRetries_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-numretries""", alias="NumRetries")
    Token_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-token""", alias="Token")
    RestartDelay_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-restartdelay""", alias="RestartDelay")
    ConnectionRetryInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-connectionretryinterval""", alias="ConnectionRetryInterval")
    HttpTransferMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html#cfn-medialive-channel-hlsakamaisettings-httptransfermode""", alias="HttpTransferMode")
    


    @property
    def tropo_type(self) -> troposphere.medialive.HlsAkamaiSettings:
        from troposphere.medialive import HlsAkamaiSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsBasicPutSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html
    Properties:
        - Name: FilecacheDuration
        - Name: NumRetries
        - Name: RestartDelay
        - Name: ConnectionRetryInterval
    
    """
    
    FilecacheDuration_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html#cfn-medialive-channel-hlsbasicputsettings-filecacheduration""", alias="FilecacheDuration")
    NumRetries_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html#cfn-medialive-channel-hlsbasicputsettings-numretries""", alias="NumRetries")
    RestartDelay_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html#cfn-medialive-channel-hlsbasicputsettings-restartdelay""", alias="RestartDelay")
    ConnectionRetryInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html#cfn-medialive-channel-hlsbasicputsettings-connectionretryinterval""", alias="ConnectionRetryInterval")
    


    @property
    def tropo_type(self) -> troposphere.medialive.HlsBasicPutSettings:
        from troposphere.medialive import HlsBasicPutSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsCdnSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html
    Properties:
        - Name: HlsWebdavSettings
        - Name: HlsS3Settings
        - Name: HlsAkamaiSettings
        - Name: HlsBasicPutSettings
        - Name: HlsMediaStoreSettings
    
    """
    
    HlsWebdavSettings_: Optional['HlsWebdavSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlswebdavsettings""", alias="HlsWebdavSettings")
    HlsS3Settings_: Optional['HlsS3Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlss3settings""", alias="HlsS3Settings")
    HlsAkamaiSettings_: Optional['HlsAkamaiSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlsakamaisettings""", alias="HlsAkamaiSettings")
    HlsBasicPutSettings_: Optional['HlsBasicPutSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlsbasicputsettings""", alias="HlsBasicPutSettings")
    HlsMediaStoreSettings_: Optional['HlsMediaStoreSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html#cfn-medialive-channel-hlscdnsettings-hlsmediastoresettings""", alias="HlsMediaStoreSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.HlsCdnSettings:
        from troposphere.medialive import HlsCdnSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsGroupSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html
    Properties:
        - Name: SegmentationMode
        - Name: Destination
        - Name: CodecSpecification
        - Name: IvSource
        - Name: TimedMetadataId3Frame
        - Name: KeyFormatVersions
        - Name: RedundantManifest
        - Name: OutputSelection
        - Name: KeyProviderSettings
        - Name: StreamInfResolution
        - Name: CaptionLanguageMappings
        - Name: HlsId3SegmentTagging
        - Name: IFrameOnlyPlaylists
        - Name: CaptionLanguageSetting
        - Name: KeepSegments
        - Name: ConstantIv
        - Name: DirectoryStructure
        - Name: EncryptionType
        - Name: AdMarkers
        - Name: HlsCdnSettings
        - Name: IndexNSegments
        - Name: DiscontinuityTags
        - Name: InputLossAction
        - Name: Mode
        - Name: TsFileMode
        - Name: BaseUrlManifest1
        - Name: ClientCache
        - Name: MinSegmentLength
        - Name: KeyFormat
        - Name: IvInManifest
        - Name: BaseUrlContent1
        - Name: ProgramDateTimeClock
        - Name: ManifestCompression
        - Name: ManifestDurationFormat
        - Name: TimedMetadataId3Period
        - Name: IncompleteSegmentBehavior
        - Name: ProgramDateTimePeriod
        - Name: SegmentLength
        - Name: TimestampDeltaMilliseconds
        - Name: ProgramDateTime
        - Name: SegmentsPerSubdirectory
        - Name: BaseUrlContent
        - Name: BaseUrlManifest
    
    """
    
    SegmentationMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-segmentationmode""", alias="SegmentationMode")
    Destination_: Optional['OutputLocationRef'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-destination""", alias="Destination")
    CodecSpecification_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-codecspecification""", alias="CodecSpecification")
    IvSource_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-ivsource""", alias="IvSource")
    TimedMetadataId3Frame_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-timedmetadataid3frame""", alias="TimedMetadataId3Frame")
    KeyFormatVersions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-keyformatversions""", alias="KeyFormatVersions")
    RedundantManifest_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-redundantmanifest""", alias="RedundantManifest")
    OutputSelection_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-outputselection""", alias="OutputSelection")
    KeyProviderSettings_: Optional['KeyProviderSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-keyprovidersettings""", alias="KeyProviderSettings")
    StreamInfResolution_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-streaminfresolution""", alias="StreamInfResolution")
    CaptionLanguageMappings_: Optional[List['CaptionLanguageMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-captionlanguagemappings""", alias="CaptionLanguageMappings")
    HlsId3SegmentTagging_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-hlsid3segmenttagging""", alias="HlsId3SegmentTagging")
    IFrameOnlyPlaylists_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-iframeonlyplaylists""", alias="IFrameOnlyPlaylists")
    CaptionLanguageSetting_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-captionlanguagesetting""", alias="CaptionLanguageSetting")
    KeepSegments_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-keepsegments""", alias="KeepSegments")
    ConstantIv_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-constantiv""", alias="ConstantIv")
    DirectoryStructure_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-directorystructure""", alias="DirectoryStructure")
    EncryptionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-encryptiontype""", alias="EncryptionType")
    AdMarkers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-admarkers""", alias="AdMarkers")
    HlsCdnSettings_: Optional['HlsCdnSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-hlscdnsettings""", alias="HlsCdnSettings")
    IndexNSegments_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-indexnsegments""", alias="IndexNSegments")
    DiscontinuityTags_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-discontinuitytags""", alias="DiscontinuityTags")
    InputLossAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-inputlossaction""", alias="InputLossAction")
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-mode""", alias="Mode")
    TsFileMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-tsfilemode""", alias="TsFileMode")
    BaseUrlManifest1_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-baseurlmanifest1""", alias="BaseUrlManifest1")
    ClientCache_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-clientcache""", alias="ClientCache")
    MinSegmentLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-minsegmentlength""", alias="MinSegmentLength")
    KeyFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-keyformat""", alias="KeyFormat")
    IvInManifest_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-ivinmanifest""", alias="IvInManifest")
    BaseUrlContent1_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-baseurlcontent1""", alias="BaseUrlContent1")
    ProgramDateTimeClock_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-programdatetimeclock""", alias="ProgramDateTimeClock")
    ManifestCompression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-manifestcompression""", alias="ManifestCompression")
    ManifestDurationFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-manifestdurationformat""", alias="ManifestDurationFormat")
    TimedMetadataId3Period_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-timedmetadataid3period""", alias="TimedMetadataId3Period")
    IncompleteSegmentBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-incompletesegmentbehavior""", alias="IncompleteSegmentBehavior")
    ProgramDateTimePeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-programdatetimeperiod""", alias="ProgramDateTimePeriod")
    SegmentLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-segmentlength""", alias="SegmentLength")
    TimestampDeltaMilliseconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-timestampdeltamilliseconds""", alias="TimestampDeltaMilliseconds")
    ProgramDateTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-programdatetime""", alias="ProgramDateTime")
    SegmentsPerSubdirectory_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-segmentspersubdirectory""", alias="SegmentsPerSubdirectory")
    BaseUrlContent_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-baseurlcontent""", alias="BaseUrlContent")
    BaseUrlManifest_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html#cfn-medialive-channel-hlsgroupsettings-baseurlmanifest""", alias="BaseUrlManifest")
    


    @property
    def tropo_type(self) -> troposphere.medialive.HlsGroupSettings:
        from troposphere.medialive import HlsGroupSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsInputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html
    Properties:
        - Name: Scte35Source
        - Name: BufferSegments
        - Name: Retries
        - Name: Bandwidth
        - Name: RetryInterval
    
    """
    
    Scte35Source_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html#cfn-medialive-channel-hlsinputsettings-scte35source""", alias="Scte35Source")
    BufferSegments_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html#cfn-medialive-channel-hlsinputsettings-buffersegments""", alias="BufferSegments")
    Retries_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html#cfn-medialive-channel-hlsinputsettings-retries""", alias="Retries")
    Bandwidth_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html#cfn-medialive-channel-hlsinputsettings-bandwidth""", alias="Bandwidth")
    RetryInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html#cfn-medialive-channel-hlsinputsettings-retryinterval""", alias="RetryInterval")
    


    @property
    def tropo_type(self) -> troposphere.medialive.HlsInputSettings:
        from troposphere.medialive import HlsInputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsMediaStoreSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html
    Properties:
        - Name: FilecacheDuration
        - Name: NumRetries
        - Name: MediaStoreStorageClass
        - Name: RestartDelay
        - Name: ConnectionRetryInterval
    
    """
    
    FilecacheDuration_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-filecacheduration""", alias="FilecacheDuration")
    NumRetries_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-numretries""", alias="NumRetries")
    MediaStoreStorageClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-mediastorestorageclass""", alias="MediaStoreStorageClass")
    RestartDelay_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-restartdelay""", alias="RestartDelay")
    ConnectionRetryInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html#cfn-medialive-channel-hlsmediastoresettings-connectionretryinterval""", alias="ConnectionRetryInterval")
    


    @property
    def tropo_type(self) -> troposphere.medialive.HlsMediaStoreSettings:
        from troposphere.medialive import HlsMediaStoreSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsOutputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html
    Properties:
        - Name: NameModifier
        - Name: HlsSettings
        - Name: H265PackagingType
        - Name: SegmentModifier
    
    """
    
    NameModifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html#cfn-medialive-channel-hlsoutputsettings-namemodifier""", alias="NameModifier")
    HlsSettings_: Optional['HlsSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html#cfn-medialive-channel-hlsoutputsettings-hlssettings""", alias="HlsSettings")
    H265PackagingType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html#cfn-medialive-channel-hlsoutputsettings-h265packagingtype""", alias="H265PackagingType")
    SegmentModifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html#cfn-medialive-channel-hlsoutputsettings-segmentmodifier""", alias="SegmentModifier")
    


    @property
    def tropo_type(self) -> troposphere.medialive.HlsOutputSettings:
        from troposphere.medialive import HlsOutputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsS3Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlss3settings.html
    Properties:
        - Name: CannedAcl
    
    """
    
    CannedAcl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlss3settings.html#cfn-medialive-channel-hlss3settings-cannedacl""", alias="CannedAcl")
    


    @property
    def tropo_type(self) -> troposphere.medialive.HlsS3Settings:
        from troposphere.medialive import HlsS3Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html
    Properties:
        - Name: StandardHlsSettings
        - Name: AudioOnlyHlsSettings
        - Name: Fmp4HlsSettings
        - Name: FrameCaptureHlsSettings
    
    """
    
    StandardHlsSettings_: Optional['StandardHlsSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html#cfn-medialive-channel-hlssettings-standardhlssettings""", alias="StandardHlsSettings")
    AudioOnlyHlsSettings_: Optional['AudioOnlyHlsSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html#cfn-medialive-channel-hlssettings-audioonlyhlssettings""", alias="AudioOnlyHlsSettings")
    Fmp4HlsSettings_: Optional['Fmp4HlsSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html#cfn-medialive-channel-hlssettings-fmp4hlssettings""", alias="Fmp4HlsSettings")
    FrameCaptureHlsSettings_: Optional['FrameCaptureHlsSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html#cfn-medialive-channel-hlssettings-framecapturehlssettings""", alias="FrameCaptureHlsSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.HlsSettings:
        from troposphere.medialive import HlsSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HlsWebdavSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html
    Properties:
        - Name: FilecacheDuration
        - Name: NumRetries
        - Name: RestartDelay
        - Name: ConnectionRetryInterval
        - Name: HttpTransferMode
    
    """
    
    FilecacheDuration_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-filecacheduration""", alias="FilecacheDuration")
    NumRetries_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-numretries""", alias="NumRetries")
    RestartDelay_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-restartdelay""", alias="RestartDelay")
    ConnectionRetryInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-connectionretryinterval""", alias="ConnectionRetryInterval")
    HttpTransferMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html#cfn-medialive-channel-hlswebdavsettings-httptransfermode""", alias="HttpTransferMode")
    


    @property
    def tropo_type(self) -> troposphere.medialive.HlsWebdavSettings:
        from troposphere.medialive import HlsWebdavSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HtmlMotionGraphicsSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-htmlmotiongraphicssettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.HtmlMotionGraphicsSettings:
        from troposphere.medialive import HtmlMotionGraphicsSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html
    Properties:
        - Name: InputAttachmentName
        - Name: InputId
        - Name: AutomaticInputFailoverSettings
        - Name: InputSettings
    
    """
    
    InputAttachmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html#cfn-medialive-channel-inputattachment-inputattachmentname""", alias="InputAttachmentName")
    InputId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html#cfn-medialive-channel-inputattachment-inputid""", alias="InputId")
    AutomaticInputFailoverSettings_: Optional['AutomaticInputFailoverSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html#cfn-medialive-channel-inputattachment-automaticinputfailoversettings""", alias="AutomaticInputFailoverSettings")
    InputSettings_: Optional['InputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html#cfn-medialive-channel-inputattachment-inputsettings""", alias="InputSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.InputAttachment:
        from troposphere.medialive import InputAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputChannelLevel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html
    Properties:
        - Name: InputChannel
        - Name: Gain
    
    """
    
    InputChannel_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html#cfn-medialive-channel-inputchannellevel-inputchannel""", alias="InputChannel")
    Gain_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html#cfn-medialive-channel-inputchannellevel-gain""", alias="Gain")
    


    @property
    def tropo_type(self) -> troposphere.medialive.InputChannelLevel:
        from troposphere.medialive import InputChannelLevel as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html
    Properties:
        - Name: Username
        - Name: PasswordParam
        - Name: Uri
    
    """
    
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html#cfn-medialive-channel-inputlocation-username""", alias="Username")
    PasswordParam_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html#cfn-medialive-channel-inputlocation-passwordparam""", alias="PasswordParam")
    Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html#cfn-medialive-channel-inputlocation-uri""", alias="Uri")
    


    @property
    def tropo_type(self) -> troposphere.medialive.InputLocation:
        from troposphere.medialive import InputLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputLossBehavior(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html
    Properties:
        - Name: InputLossImageColor
        - Name: BlackFrameMsec
        - Name: InputLossImageType
        - Name: InputLossImageSlate
        - Name: RepeatFrameMsec
    
    """
    
    InputLossImageColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-inputlossimagecolor""", alias="InputLossImageColor")
    BlackFrameMsec_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-blackframemsec""", alias="BlackFrameMsec")
    InputLossImageType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-inputlossimagetype""", alias="InputLossImageType")
    InputLossImageSlate_: Optional['InputLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-inputlossimageslate""", alias="InputLossImageSlate")
    RepeatFrameMsec_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html#cfn-medialive-channel-inputlossbehavior-repeatframemsec""", alias="RepeatFrameMsec")
    


    @property
    def tropo_type(self) -> troposphere.medialive.InputLossBehavior:
        from troposphere.medialive import InputLossBehavior as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputLossFailoverSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossfailoversettings.html
    Properties:
        - Name: InputLossThresholdMsec
    
    """
    
    InputLossThresholdMsec_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossfailoversettings.html#cfn-medialive-channel-inputlossfailoversettings-inputlossthresholdmsec""", alias="InputLossThresholdMsec")
    


    @property
    def tropo_type(self) -> troposphere.medialive.InputLossFailoverSettings:
        from troposphere.medialive import InputLossFailoverSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html
    Properties:
        - Name: Scte35Pid
        - Name: DeblockFilter
        - Name: FilterStrength
        - Name: InputFilter
        - Name: SourceEndBehavior
        - Name: VideoSelector
        - Name: Smpte2038DataPreference
        - Name: AudioSelectors
        - Name: CaptionSelectors
        - Name: DenoiseFilter
        - Name: NetworkInputSettings
    
    """
    
    Scte35Pid_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-scte35pid""", alias="Scte35Pid")
    DeblockFilter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-deblockfilter""", alias="DeblockFilter")
    FilterStrength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-filterstrength""", alias="FilterStrength")
    InputFilter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-inputfilter""", alias="InputFilter")
    SourceEndBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-sourceendbehavior""", alias="SourceEndBehavior")
    VideoSelector_: Optional['VideoSelector'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-videoselector""", alias="VideoSelector")
    Smpte2038DataPreference_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-smpte2038datapreference""", alias="Smpte2038DataPreference")
    AudioSelectors_: Optional[List['AudioSelector']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-audioselectors""", alias="AudioSelectors")
    CaptionSelectors_: Optional[List['CaptionSelector']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-captionselectors""", alias="CaptionSelectors")
    DenoiseFilter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-denoisefilter""", alias="DenoiseFilter")
    NetworkInputSettings_: Optional['NetworkInputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html#cfn-medialive-channel-inputsettings-networkinputsettings""", alias="NetworkInputSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.InputSettings:
        from troposphere.medialive import InputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html
    Properties:
        - Name: Codec
        - Name: MaximumBitrate
        - Name: Resolution
    
    """
    
    Codec_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html#cfn-medialive-channel-inputspecification-codec""", alias="Codec")
    MaximumBitrate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html#cfn-medialive-channel-inputspecification-maximumbitrate""", alias="MaximumBitrate")
    Resolution_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html#cfn-medialive-channel-inputspecification-resolution""", alias="Resolution")
    


    @property
    def tropo_type(self) -> troposphere.medialive.InputSpecification:
        from troposphere.medialive import InputSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeyProviderSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-keyprovidersettings.html
    Properties:
        - Name: StaticKeySettings
    
    """
    
    StaticKeySettings_: Optional['StaticKeySettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-keyprovidersettings.html#cfn-medialive-channel-keyprovidersettings-statickeysettings""", alias="StaticKeySettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.KeyProviderSettings:
        from troposphere.medialive import KeyProviderSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class M2tsSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html
    Properties:
        - Name: EtvPlatformPid
        - Name: PatInterval
        - Name: ProgramNum
        - Name: RateMode
        - Name: KlvDataPids
        - Name: NullPacketBitrate
        - Name: PmtInterval
        - Name: AribCaptionsPid
        - Name: EsRateInPes
        - Name: VideoPid
        - Name: TransportStreamId
        - Name: EbpPlacement
        - Name: DvbSubPids
        - Name: SegmentationStyle
        - Name: Scte35Pid
        - Name: AudioStreamType
        - Name: Klv
        - Name: EbpLookaheadMs
        - Name: Scte35PrerollPullupMilliseconds
        - Name: DvbTdtSettings
        - Name: TimedMetadataBehavior
        - Name: EbpAudioInterval
        - Name: FragmentTime
        - Name: DvbTeletextPid
        - Name: Scte35Control
        - Name: PcrPeriod
        - Name: NielsenId3Behavior
        - Name: PcrPid
        - Name: SegmentationTime
        - Name: CcDescriptor
        - Name: AudioFramesPerPes
        - Name: AbsentInputAudioBehavior
        - Name: Bitrate
        - Name: PmtPid
        - Name: Scte27Pids
        - Name: SegmentationMarkers
        - Name: DvbNitSettings
        - Name: DvbSdtSettings
        - Name: EtvSignalPid
        - Name: Arib
        - Name: BufferModel
        - Name: EcmPid
        - Name: TimedMetadataPid
        - Name: AudioPids
        - Name: AudioBufferModel
        - Name: Ebif
        - Name: AribCaptionsPidControl
        - Name: PcrControl
    
    """
    
    EtvPlatformPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-etvplatformpid""", alias="EtvPlatformPid")
    PatInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-patinterval""", alias="PatInterval")
    ProgramNum_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-programnum""", alias="ProgramNum")
    RateMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ratemode""", alias="RateMode")
    KlvDataPids_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-klvdatapids""", alias="KlvDataPids")
    NullPacketBitrate_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-nullpacketbitrate""", alias="NullPacketBitrate")
    PmtInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pmtinterval""", alias="PmtInterval")
    AribCaptionsPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-aribcaptionspid""", alias="AribCaptionsPid")
    EsRateInPes_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-esrateinpes""", alias="EsRateInPes")
    VideoPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-videopid""", alias="VideoPid")
    TransportStreamId_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-transportstreamid""", alias="TransportStreamId")
    EbpPlacement_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ebpplacement""", alias="EbpPlacement")
    DvbSubPids_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbsubpids""", alias="DvbSubPids")
    SegmentationStyle_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-segmentationstyle""", alias="SegmentationStyle")
    Scte35Pid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-scte35pid""", alias="Scte35Pid")
    AudioStreamType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-audiostreamtype""", alias="AudioStreamType")
    Klv_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-klv""", alias="Klv")
    EbpLookaheadMs_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ebplookaheadms""", alias="EbpLookaheadMs")
    Scte35PrerollPullupMilliseconds_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-scte35prerollpullupmilliseconds""", alias="Scte35PrerollPullupMilliseconds")
    DvbTdtSettings_: Optional['DvbTdtSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbtdtsettings""", alias="DvbTdtSettings")
    TimedMetadataBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-timedmetadatabehavior""", alias="TimedMetadataBehavior")
    EbpAudioInterval_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ebpaudiointerval""", alias="EbpAudioInterval")
    FragmentTime_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-fragmenttime""", alias="FragmentTime")
    DvbTeletextPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbteletextpid""", alias="DvbTeletextPid")
    Scte35Control_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-scte35control""", alias="Scte35Control")
    PcrPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pcrperiod""", alias="PcrPeriod")
    NielsenId3Behavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-nielsenid3behavior""", alias="NielsenId3Behavior")
    PcrPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pcrpid""", alias="PcrPid")
    SegmentationTime_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-segmentationtime""", alias="SegmentationTime")
    CcDescriptor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ccdescriptor""", alias="CcDescriptor")
    AudioFramesPerPes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-audioframesperpes""", alias="AudioFramesPerPes")
    AbsentInputAudioBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-absentinputaudiobehavior""", alias="AbsentInputAudioBehavior")
    Bitrate_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-bitrate""", alias="Bitrate")
    PmtPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pmtpid""", alias="PmtPid")
    Scte27Pids_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-scte27pids""", alias="Scte27Pids")
    SegmentationMarkers_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-segmentationmarkers""", alias="SegmentationMarkers")
    DvbNitSettings_: Optional['DvbNitSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbnitsettings""", alias="DvbNitSettings")
    DvbSdtSettings_: Optional['DvbSdtSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-dvbsdtsettings""", alias="DvbSdtSettings")
    EtvSignalPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-etvsignalpid""", alias="EtvSignalPid")
    Arib_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-arib""", alias="Arib")
    BufferModel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-buffermodel""", alias="BufferModel")
    EcmPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ecmpid""", alias="EcmPid")
    TimedMetadataPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-timedmetadatapid""", alias="TimedMetadataPid")
    AudioPids_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-audiopids""", alias="AudioPids")
    AudioBufferModel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-audiobuffermodel""", alias="AudioBufferModel")
    Ebif_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-ebif""", alias="Ebif")
    AribCaptionsPidControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-aribcaptionspidcontrol""", alias="AribCaptionsPidControl")
    PcrControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html#cfn-medialive-channel-m2tssettings-pcrcontrol""", alias="PcrControl")
    


    @property
    def tropo_type(self) -> troposphere.medialive.M2tsSettings:
        from troposphere.medialive import M2tsSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class M3u8Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html
    Properties:
        - Name: PatInterval
        - Name: ProgramNum
        - Name: PcrPeriod
        - Name: PmtInterval
        - Name: KlvDataPids
        - Name: NielsenId3Behavior
        - Name: PcrPid
        - Name: VideoPid
        - Name: AudioFramesPerPes
        - Name: TransportStreamId
        - Name: PmtPid
        - Name: Scte35Pid
        - Name: Scte35Behavior
        - Name: KlvBehavior
        - Name: EcmPid
        - Name: TimedMetadataPid
        - Name: AudioPids
        - Name: PcrControl
        - Name: TimedMetadataBehavior
    
    """
    
    PatInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-patinterval""", alias="PatInterval")
    ProgramNum_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-programnum""", alias="ProgramNum")
    PcrPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pcrperiod""", alias="PcrPeriod")
    PmtInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pmtinterval""", alias="PmtInterval")
    KlvDataPids_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-klvdatapids""", alias="KlvDataPids")
    NielsenId3Behavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-nielsenid3behavior""", alias="NielsenId3Behavior")
    PcrPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pcrpid""", alias="PcrPid")
    VideoPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-videopid""", alias="VideoPid")
    AudioFramesPerPes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-audioframesperpes""", alias="AudioFramesPerPes")
    TransportStreamId_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-transportstreamid""", alias="TransportStreamId")
    PmtPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pmtpid""", alias="PmtPid")
    Scte35Pid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-scte35pid""", alias="Scte35Pid")
    Scte35Behavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-scte35behavior""", alias="Scte35Behavior")
    KlvBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-klvbehavior""", alias="KlvBehavior")
    EcmPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-ecmpid""", alias="EcmPid")
    TimedMetadataPid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-timedmetadatapid""", alias="TimedMetadataPid")
    AudioPids_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-audiopids""", alias="AudioPids")
    PcrControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-pcrcontrol""", alias="PcrControl")
    TimedMetadataBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html#cfn-medialive-channel-m3u8settings-timedmetadatabehavior""", alias="TimedMetadataBehavior")
    


    @property
    def tropo_type(self) -> troposphere.medialive.M3u8Settings:
        from troposphere.medialive import M3u8Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MaintenanceCreateSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-maintenancecreatesettings.html
    Properties:
        - Name: MaintenanceDay
        - Name: MaintenanceStartTime
    
    """
    
    MaintenanceDay_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-maintenancecreatesettings.html#cfn-medialive-channel-maintenancecreatesettings-maintenanceday""", alias="MaintenanceDay")
    MaintenanceStartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-maintenancecreatesettings.html#cfn-medialive-channel-maintenancecreatesettings-maintenancestarttime""", alias="MaintenanceStartTime")
    


    @property
    def tropo_type(self) -> troposphere.medialive.MaintenanceCreateSettings:
        from troposphere.medialive import MaintenanceCreateSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MaintenanceUpdateSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-maintenanceupdatesettings.html
    Properties:
        - Name: MaintenanceDay
        - Name: MaintenanceScheduledDate
        - Name: MaintenanceStartTime
    
    """
    
    MaintenanceDay_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-maintenanceupdatesettings.html#cfn-medialive-channel-maintenanceupdatesettings-maintenanceday""", alias="MaintenanceDay")
    MaintenanceScheduledDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-maintenanceupdatesettings.html#cfn-medialive-channel-maintenanceupdatesettings-maintenancescheduleddate""", alias="MaintenanceScheduledDate")
    MaintenanceStartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-maintenanceupdatesettings.html#cfn-medialive-channel-maintenanceupdatesettings-maintenancestarttime""", alias="MaintenanceStartTime")
    


    @property
    def tropo_type(self) -> troposphere.medialive.MaintenanceUpdateSettings:
        from troposphere.medialive import MaintenanceUpdateSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MediaPackageGroupSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackagegroupsettings.html
    Properties:
        - Name: Destination
    
    """
    
    Destination_: Optional['OutputLocationRef'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackagegroupsettings.html#cfn-medialive-channel-mediapackagegroupsettings-destination""", alias="Destination")
    


    @property
    def tropo_type(self) -> troposphere.medialive.MediaPackageGroupSettings:
        from troposphere.medialive import MediaPackageGroupSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MediaPackageOutputDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputdestinationsettings.html
    Properties:
        - Name: ChannelId
    
    """
    
    ChannelId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputdestinationsettings.html#cfn-medialive-channel-mediapackageoutputdestinationsettings-channelid""", alias="ChannelId")
    


    @property
    def tropo_type(self) -> troposphere.medialive.MediaPackageOutputDestinationSettings:
        from troposphere.medialive import MediaPackageOutputDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MediaPackageOutputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputsettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.MediaPackageOutputSettings:
        from troposphere.medialive import MediaPackageOutputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MotionGraphicsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicsconfiguration.html
    Properties:
        - Name: MotionGraphicsSettings
        - Name: MotionGraphicsInsertion
    
    """
    
    MotionGraphicsSettings_: Optional['MotionGraphicsSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicsconfiguration.html#cfn-medialive-channel-motiongraphicsconfiguration-motiongraphicssettings""", alias="MotionGraphicsSettings")
    MotionGraphicsInsertion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicsconfiguration.html#cfn-medialive-channel-motiongraphicsconfiguration-motiongraphicsinsertion""", alias="MotionGraphicsInsertion")
    


    @property
    def tropo_type(self) -> troposphere.medialive.MotionGraphicsConfiguration:
        from troposphere.medialive import MotionGraphicsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MotionGraphicsSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicssettings.html
    Properties:
        - Name: HtmlMotionGraphicsSettings
    
    """
    
    HtmlMotionGraphicsSettings_: Optional['HtmlMotionGraphicsSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicssettings.html#cfn-medialive-channel-motiongraphicssettings-htmlmotiongraphicssettings""", alias="HtmlMotionGraphicsSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.MotionGraphicsSettings:
        from troposphere.medialive import MotionGraphicsSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Mp2Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html
    Properties:
        - Name: CodingMode
        - Name: SampleRate
        - Name: Bitrate
    
    """
    
    CodingMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html#cfn-medialive-channel-mp2settings-codingmode""", alias="CodingMode")
    SampleRate_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html#cfn-medialive-channel-mp2settings-samplerate""", alias="SampleRate")
    Bitrate_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html#cfn-medialive-channel-mp2settings-bitrate""", alias="Bitrate")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Mp2Settings:
        from troposphere.medialive import Mp2Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Mpeg2FilterSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2filtersettings.html
    Properties:
        - Name: TemporalFilterSettings
    
    """
    
    TemporalFilterSettings_: Optional['TemporalFilterSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2filtersettings.html#cfn-medialive-channel-mpeg2filtersettings-temporalfiltersettings""", alias="TemporalFilterSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Mpeg2FilterSettings:
        from troposphere.medialive import Mpeg2FilterSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Mpeg2Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html
    Properties:
        - Name: TimecodeBurninSettings
        - Name: ColorSpace
        - Name: FixedAfd
        - Name: GopSizeUnits
        - Name: FramerateNumerator
        - Name: GopClosedCadence
        - Name: AfdSignaling
        - Name: DisplayAspectRatio
        - Name: ScanType
        - Name: TimecodeInsertion
        - Name: ColorMetadata
        - Name: FramerateDenominator
        - Name: GopSize
        - Name: AdaptiveQuantization
        - Name: SubgopLength
        - Name: FilterSettings
        - Name: GopNumBFrames
    
    """
    
    TimecodeBurninSettings_: Optional['TimecodeBurninSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-timecodeburninsettings""", alias="TimecodeBurninSettings")
    ColorSpace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-colorspace""", alias="ColorSpace")
    FixedAfd_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-fixedafd""", alias="FixedAfd")
    GopSizeUnits_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-gopsizeunits""", alias="GopSizeUnits")
    FramerateNumerator_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-frameratenumerator""", alias="FramerateNumerator")
    GopClosedCadence_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-gopclosedcadence""", alias="GopClosedCadence")
    AfdSignaling_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-afdsignaling""", alias="AfdSignaling")
    DisplayAspectRatio_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-displayaspectratio""", alias="DisplayAspectRatio")
    ScanType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-scantype""", alias="ScanType")
    TimecodeInsertion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-timecodeinsertion""", alias="TimecodeInsertion")
    ColorMetadata_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-colormetadata""", alias="ColorMetadata")
    FramerateDenominator_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-frameratedenominator""", alias="FramerateDenominator")
    GopSize_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-gopsize""", alias="GopSize")
    AdaptiveQuantization_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-adaptivequantization""", alias="AdaptiveQuantization")
    SubgopLength_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-subgoplength""", alias="SubgopLength")
    FilterSettings_: Optional['Mpeg2FilterSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-filtersettings""", alias="FilterSettings")
    GopNumBFrames_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html#cfn-medialive-channel-mpeg2settings-gopnumbframes""", alias="GopNumBFrames")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Mpeg2Settings:
        from troposphere.medialive import Mpeg2Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MsSmoothGroupSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html
    Properties:
        - Name: SegmentationMode
        - Name: Destination
        - Name: EventStopBehavior
        - Name: FilecacheDuration
        - Name: CertificateMode
        - Name: AcquisitionPointId
        - Name: StreamManifestBehavior
        - Name: InputLossAction
        - Name: FragmentLength
        - Name: RestartDelay
        - Name: SparseTrackType
        - Name: EventIdMode
        - Name: TimestampOffsetMode
        - Name: AudioOnlyTimecodeControl
        - Name: NumRetries
        - Name: TimestampOffset
        - Name: EventId
        - Name: SendDelayMs
        - Name: ConnectionRetryInterval
    
    """
    
    SegmentationMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-segmentationmode""", alias="SegmentationMode")
    Destination_: Optional['OutputLocationRef'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-destination""", alias="Destination")
    EventStopBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-eventstopbehavior""", alias="EventStopBehavior")
    FilecacheDuration_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-filecacheduration""", alias="FilecacheDuration")
    CertificateMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-certificatemode""", alias="CertificateMode")
    AcquisitionPointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-acquisitionpointid""", alias="AcquisitionPointId")
    StreamManifestBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-streammanifestbehavior""", alias="StreamManifestBehavior")
    InputLossAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-inputlossaction""", alias="InputLossAction")
    FragmentLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-fragmentlength""", alias="FragmentLength")
    RestartDelay_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-restartdelay""", alias="RestartDelay")
    SparseTrackType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-sparsetracktype""", alias="SparseTrackType")
    EventIdMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-eventidmode""", alias="EventIdMode")
    TimestampOffsetMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-timestampoffsetmode""", alias="TimestampOffsetMode")
    AudioOnlyTimecodeControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-audioonlytimecodecontrol""", alias="AudioOnlyTimecodeControl")
    NumRetries_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-numretries""", alias="NumRetries")
    TimestampOffset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-timestampoffset""", alias="TimestampOffset")
    EventId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-eventid""", alias="EventId")
    SendDelayMs_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-senddelayms""", alias="SendDelayMs")
    ConnectionRetryInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html#cfn-medialive-channel-mssmoothgroupsettings-connectionretryinterval""", alias="ConnectionRetryInterval")
    


    @property
    def tropo_type(self) -> troposphere.medialive.MsSmoothGroupSettings:
        from troposphere.medialive import MsSmoothGroupSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MsSmoothOutputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html
    Properties:
        - Name: NameModifier
        - Name: H265PackagingType
    
    """
    
    NameModifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html#cfn-medialive-channel-mssmoothoutputsettings-namemodifier""", alias="NameModifier")
    H265PackagingType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html#cfn-medialive-channel-mssmoothoutputsettings-h265packagingtype""", alias="H265PackagingType")
    


    @property
    def tropo_type(self) -> troposphere.medialive.MsSmoothOutputSettings:
        from troposphere.medialive import MsSmoothOutputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MultiplexGroupSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexgroupsettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.MultiplexGroupSettings:
        from troposphere.medialive import MultiplexGroupSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MultiplexOutputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexoutputsettings.html
    Properties:
        - Name: Destination
    
    """
    
    Destination_: Optional['OutputLocationRef'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexoutputsettings.html#cfn-medialive-channel-multiplexoutputsettings-destination""", alias="Destination")
    


    @property
    def tropo_type(self) -> troposphere.medialive.MultiplexOutputSettings:
        from troposphere.medialive import MultiplexOutputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MultiplexProgramChannelDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html
    Properties:
        - Name: MultiplexId
        - Name: ProgramName
    
    """
    
    MultiplexId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html#cfn-medialive-channel-multiplexprogramchanneldestinationsettings-multiplexid""", alias="MultiplexId")
    ProgramName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html#cfn-medialive-channel-multiplexprogramchanneldestinationsettings-programname""", alias="ProgramName")
    


    @property
    def tropo_type(self) -> troposphere.medialive.MultiplexProgramChannelDestinationSettings:
        from troposphere.medialive import MultiplexProgramChannelDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkInputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-networkinputsettings.html
    Properties:
        - Name: ServerValidation
        - Name: HlsInputSettings
    
    """
    
    ServerValidation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-networkinputsettings.html#cfn-medialive-channel-networkinputsettings-servervalidation""", alias="ServerValidation")
    HlsInputSettings_: Optional['HlsInputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-networkinputsettings.html#cfn-medialive-channel-networkinputsettings-hlsinputsettings""", alias="HlsInputSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.NetworkInputSettings:
        from troposphere.medialive import NetworkInputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NielsenCBET(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsencbet.html
    Properties:
        - Name: CbetCheckDigitString
        - Name: CbetStepaside
        - Name: Csid
    
    """
    
    CbetCheckDigitString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsencbet.html#cfn-medialive-channel-nielsencbet-cbetcheckdigitstring""", alias="CbetCheckDigitString")
    CbetStepaside_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsencbet.html#cfn-medialive-channel-nielsencbet-cbetstepaside""", alias="CbetStepaside")
    Csid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsencbet.html#cfn-medialive-channel-nielsencbet-csid""", alias="Csid")
    


    @property
    def tropo_type(self) -> troposphere.medialive.NielsenCBET:
        from troposphere.medialive import NielsenCBET as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NielsenConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html
    Properties:
        - Name: DistributorId
        - Name: NielsenPcmToId3Tagging
    
    """
    
    DistributorId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html#cfn-medialive-channel-nielsenconfiguration-distributorid""", alias="DistributorId")
    NielsenPcmToId3Tagging_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html#cfn-medialive-channel-nielsenconfiguration-nielsenpcmtoid3tagging""", alias="NielsenPcmToId3Tagging")
    


    @property
    def tropo_type(self) -> troposphere.medialive.NielsenConfiguration:
        from troposphere.medialive import NielsenConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NielsenNaesIiNw(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsennaesiinw.html
    Properties:
        - Name: Timezone
        - Name: CheckDigitString
        - Name: Sid
    
    """
    
    Timezone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsennaesiinw.html#cfn-medialive-channel-nielsennaesiinw-timezone""", alias="Timezone")
    CheckDigitString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsennaesiinw.html#cfn-medialive-channel-nielsennaesiinw-checkdigitstring""", alias="CheckDigitString")
    Sid_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsennaesiinw.html#cfn-medialive-channel-nielsennaesiinw-sid""", alias="Sid")
    


    @property
    def tropo_type(self) -> troposphere.medialive.NielsenNaesIiNw:
        from troposphere.medialive import NielsenNaesIiNw as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NielsenWatermarksSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenwatermarkssettings.html
    Properties:
        - Name: NielsenDistributionType
        - Name: NielsenCbetSettings
        - Name: NielsenNaesIiNwSettings
    
    """
    
    NielsenDistributionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenwatermarkssettings.html#cfn-medialive-channel-nielsenwatermarkssettings-nielsendistributiontype""", alias="NielsenDistributionType")
    NielsenCbetSettings_: Optional['NielsenCBET'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenwatermarkssettings.html#cfn-medialive-channel-nielsenwatermarkssettings-nielsencbetsettings""", alias="NielsenCbetSettings")
    NielsenNaesIiNwSettings_: Optional['NielsenNaesIiNw'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenwatermarkssettings.html#cfn-medialive-channel-nielsenwatermarkssettings-nielsennaesiinwsettings""", alias="NielsenNaesIiNwSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.NielsenWatermarksSettings:
        from troposphere.medialive import NielsenWatermarksSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Output(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html
    Properties:
        - Name: OutputSettings
        - Name: CaptionDescriptionNames
        - Name: AudioDescriptionNames
        - Name: OutputName
        - Name: VideoDescriptionName
    
    """
    
    OutputSettings_: Optional['OutputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-outputsettings""", alias="OutputSettings")
    CaptionDescriptionNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-captiondescriptionnames""", alias="CaptionDescriptionNames")
    AudioDescriptionNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-audiodescriptionnames""", alias="AudioDescriptionNames")
    OutputName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-outputname""", alias="OutputName")
    VideoDescriptionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html#cfn-medialive-channel-output-videodescriptionname""", alias="VideoDescriptionName")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Output:
        from troposphere.medialive import Output as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html
    Properties:
        - Name: MultiplexSettings
        - Name: Id
        - Name: Settings
        - Name: MediaPackageSettings
    
    """
    
    MultiplexSettings_: Optional['MultiplexProgramChannelDestinationSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html#cfn-medialive-channel-outputdestination-multiplexsettings""", alias="MultiplexSettings")
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html#cfn-medialive-channel-outputdestination-id""", alias="Id")
    Settings_: Optional[List['OutputDestinationSettings']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html#cfn-medialive-channel-outputdestination-settings""", alias="Settings")
    MediaPackageSettings_: Optional[List['MediaPackageOutputDestinationSettings']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html#cfn-medialive-channel-outputdestination-mediapackagesettings""", alias="MediaPackageSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.OutputDestination:
        from troposphere.medialive import OutputDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html
    Properties:
        - Name: StreamName
        - Name: Username
        - Name: PasswordParam
        - Name: Url
    
    """
    
    StreamName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html#cfn-medialive-channel-outputdestinationsettings-streamname""", alias="StreamName")
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html#cfn-medialive-channel-outputdestinationsettings-username""", alias="Username")
    PasswordParam_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html#cfn-medialive-channel-outputdestinationsettings-passwordparam""", alias="PasswordParam")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html#cfn-medialive-channel-outputdestinationsettings-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.medialive.OutputDestinationSettings:
        from troposphere.medialive import OutputDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html
    Properties:
        - Name: Outputs
        - Name: OutputGroupSettings
        - Name: Name
    
    """
    
    Outputs_: Optional[List['Output']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html#cfn-medialive-channel-outputgroup-outputs""", alias="Outputs")
    OutputGroupSettings_: Optional['OutputGroupSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html#cfn-medialive-channel-outputgroup-outputgroupsettings""", alias="OutputGroupSettings")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html#cfn-medialive-channel-outputgroup-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.medialive.OutputGroup:
        from troposphere.medialive import OutputGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputGroupSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html
    Properties:
        - Name: HlsGroupSettings
        - Name: FrameCaptureGroupSettings
        - Name: MultiplexGroupSettings
        - Name: ArchiveGroupSettings
        - Name: MediaPackageGroupSettings
        - Name: UdpGroupSettings
        - Name: MsSmoothGroupSettings
        - Name: RtmpGroupSettings
    
    """
    
    HlsGroupSettings_: Optional['HlsGroupSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-hlsgroupsettings""", alias="HlsGroupSettings")
    FrameCaptureGroupSettings_: Optional['FrameCaptureGroupSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-framecapturegroupsettings""", alias="FrameCaptureGroupSettings")
    MultiplexGroupSettings_: Optional['MultiplexGroupSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-multiplexgroupsettings""", alias="MultiplexGroupSettings")
    ArchiveGroupSettings_: Optional['ArchiveGroupSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-archivegroupsettings""", alias="ArchiveGroupSettings")
    MediaPackageGroupSettings_: Optional['MediaPackageGroupSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-mediapackagegroupsettings""", alias="MediaPackageGroupSettings")
    UdpGroupSettings_: Optional['UdpGroupSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-udpgroupsettings""", alias="UdpGroupSettings")
    MsSmoothGroupSettings_: Optional['MsSmoothGroupSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-mssmoothgroupsettings""", alias="MsSmoothGroupSettings")
    RtmpGroupSettings_: Optional['RtmpGroupSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html#cfn-medialive-channel-outputgroupsettings-rtmpgroupsettings""", alias="RtmpGroupSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.OutputGroupSettings:
        from troposphere.medialive import OutputGroupSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputLocationRef(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputlocationref.html
    Properties:
        - Name: DestinationRefId
    
    """
    
    DestinationRefId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputlocationref.html#cfn-medialive-channel-outputlocationref-destinationrefid""", alias="DestinationRefId")
    


    @property
    def tropo_type(self) -> troposphere.medialive.OutputLocationRef:
        from troposphere.medialive import OutputLocationRef as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html
    Properties:
        - Name: MediaPackageOutputSettings
        - Name: MsSmoothOutputSettings
        - Name: FrameCaptureOutputSettings
        - Name: HlsOutputSettings
        - Name: RtmpOutputSettings
        - Name: UdpOutputSettings
        - Name: MultiplexOutputSettings
        - Name: ArchiveOutputSettings
    
    """
    
    MediaPackageOutputSettings_: Optional['MediaPackageOutputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-mediapackageoutputsettings""", alias="MediaPackageOutputSettings")
    MsSmoothOutputSettings_: Optional['MsSmoothOutputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-mssmoothoutputsettings""", alias="MsSmoothOutputSettings")
    FrameCaptureOutputSettings_: Optional['FrameCaptureOutputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-framecaptureoutputsettings""", alias="FrameCaptureOutputSettings")
    HlsOutputSettings_: Optional['HlsOutputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-hlsoutputsettings""", alias="HlsOutputSettings")
    RtmpOutputSettings_: Optional['RtmpOutputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-rtmpoutputsettings""", alias="RtmpOutputSettings")
    UdpOutputSettings_: Optional['UdpOutputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-udpoutputsettings""", alias="UdpOutputSettings")
    MultiplexOutputSettings_: Optional['MultiplexOutputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-multiplexoutputsettings""", alias="MultiplexOutputSettings")
    ArchiveOutputSettings_: Optional['ArchiveOutputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html#cfn-medialive-channel-outputsettings-archiveoutputsettings""", alias="ArchiveOutputSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.OutputSettings:
        from troposphere.medialive import OutputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PassThroughSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-passthroughsettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.PassThroughSettings:
        from troposphere.medialive import PassThroughSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RawSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rawsettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.RawSettings:
        from troposphere.medialive import RawSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Rec601Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec601settings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.Rec601Settings:
        from troposphere.medialive import Rec601Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Rec709Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec709settings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.Rec709Settings:
        from troposphere.medialive import Rec709Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RemixSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html
    Properties:
        - Name: ChannelsOut
        - Name: ChannelMappings
        - Name: ChannelsIn
    
    """
    
    ChannelsOut_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html#cfn-medialive-channel-remixsettings-channelsout""", alias="ChannelsOut")
    ChannelMappings_: Optional[List['AudioChannelMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html#cfn-medialive-channel-remixsettings-channelmappings""", alias="ChannelMappings")
    ChannelsIn_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html#cfn-medialive-channel-remixsettings-channelsin""", alias="ChannelsIn")
    


    @property
    def tropo_type(self) -> troposphere.medialive.RemixSettings:
        from troposphere.medialive import RemixSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RtmpCaptionInfoDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpcaptioninfodestinationsettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.RtmpCaptionInfoDestinationSettings:
        from troposphere.medialive import RtmpCaptionInfoDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RtmpGroupSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html
    Properties:
        - Name: AuthenticationScheme
        - Name: CacheLength
        - Name: AdMarkers
        - Name: IncludeFillerNalUnits
        - Name: InputLossAction
        - Name: RestartDelay
        - Name: CaptionData
        - Name: CacheFullBehavior
    
    """
    
    AuthenticationScheme_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-authenticationscheme""", alias="AuthenticationScheme")
    CacheLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-cachelength""", alias="CacheLength")
    AdMarkers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-admarkers""", alias="AdMarkers")
    IncludeFillerNalUnits_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-includefillernalunits""", alias="IncludeFillerNalUnits")
    InputLossAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-inputlossaction""", alias="InputLossAction")
    RestartDelay_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-restartdelay""", alias="RestartDelay")
    CaptionData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-captiondata""", alias="CaptionData")
    CacheFullBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html#cfn-medialive-channel-rtmpgroupsettings-cachefullbehavior""", alias="CacheFullBehavior")
    


    @property
    def tropo_type(self) -> troposphere.medialive.RtmpGroupSettings:
        from troposphere.medialive import RtmpGroupSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RtmpOutputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html
    Properties:
        - Name: Destination
        - Name: CertificateMode
        - Name: NumRetries
        - Name: ConnectionRetryInterval
    
    """
    
    Destination_: Optional['OutputLocationRef'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html#cfn-medialive-channel-rtmpoutputsettings-destination""", alias="Destination")
    CertificateMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html#cfn-medialive-channel-rtmpoutputsettings-certificatemode""", alias="CertificateMode")
    NumRetries_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html#cfn-medialive-channel-rtmpoutputsettings-numretries""", alias="NumRetries")
    ConnectionRetryInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html#cfn-medialive-channel-rtmpoutputsettings-connectionretryinterval""", alias="ConnectionRetryInterval")
    


    @property
    def tropo_type(self) -> troposphere.medialive.RtmpOutputSettings:
        from troposphere.medialive import RtmpOutputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Scte20PlusEmbeddedDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20plusembeddeddestinationsettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.Scte20PlusEmbeddedDestinationSettings:
        from troposphere.medialive import Scte20PlusEmbeddedDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Scte20SourceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20sourcesettings.html
    Properties:
        - Name: Source608ChannelNumber
        - Name: Convert608To708
    
    """
    
    Source608ChannelNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20sourcesettings.html#cfn-medialive-channel-scte20sourcesettings-source608channelnumber""", alias="Source608ChannelNumber")
    Convert608To708_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20sourcesettings.html#cfn-medialive-channel-scte20sourcesettings-convert608to708""", alias="Convert608To708")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Scte20SourceSettings:
        from troposphere.medialive import Scte20SourceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Scte27DestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27destinationsettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.Scte27DestinationSettings:
        from troposphere.medialive import Scte27DestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Scte27SourceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27sourcesettings.html
    Properties:
        - Name: OcrLanguage
        - Name: Pid
    
    """
    
    OcrLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27sourcesettings.html#cfn-medialive-channel-scte27sourcesettings-ocrlanguage""", alias="OcrLanguage")
    Pid_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27sourcesettings.html#cfn-medialive-channel-scte27sourcesettings-pid""", alias="Pid")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Scte27SourceSettings:
        from troposphere.medialive import Scte27SourceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Scte35SpliceInsert(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html
    Properties:
        - Name: AdAvailOffset
        - Name: WebDeliveryAllowedFlag
        - Name: NoRegionalBlackoutFlag
    
    """
    
    AdAvailOffset_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html#cfn-medialive-channel-scte35spliceinsert-adavailoffset""", alias="AdAvailOffset")
    WebDeliveryAllowedFlag_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html#cfn-medialive-channel-scte35spliceinsert-webdeliveryallowedflag""", alias="WebDeliveryAllowedFlag")
    NoRegionalBlackoutFlag_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html#cfn-medialive-channel-scte35spliceinsert-noregionalblackoutflag""", alias="NoRegionalBlackoutFlag")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Scte35SpliceInsert:
        from troposphere.medialive import Scte35SpliceInsert as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Scte35TimeSignalApos(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html
    Properties:
        - Name: AdAvailOffset
        - Name: WebDeliveryAllowedFlag
        - Name: NoRegionalBlackoutFlag
    
    """
    
    AdAvailOffset_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html#cfn-medialive-channel-scte35timesignalapos-adavailoffset""", alias="AdAvailOffset")
    WebDeliveryAllowedFlag_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html#cfn-medialive-channel-scte35timesignalapos-webdeliveryallowedflag""", alias="WebDeliveryAllowedFlag")
    NoRegionalBlackoutFlag_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html#cfn-medialive-channel-scte35timesignalapos-noregionalblackoutflag""", alias="NoRegionalBlackoutFlag")
    


    @property
    def tropo_type(self) -> troposphere.medialive.Scte35TimeSignalApos:
        from troposphere.medialive import Scte35TimeSignalApos as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SmpteTtDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-smptettdestinationsettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.SmpteTtDestinationSettings:
        from troposphere.medialive import SmpteTtDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StandardHlsSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html
    Properties:
        - Name: AudioRenditionSets
        - Name: M3u8Settings
    
    """
    
    AudioRenditionSets_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html#cfn-medialive-channel-standardhlssettings-audiorenditionsets""", alias="AudioRenditionSets")
    M3u8Settings_: Optional['M3u8Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html#cfn-medialive-channel-standardhlssettings-m3u8settings""", alias="M3u8Settings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.StandardHlsSettings:
        from troposphere.medialive import StandardHlsSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StaticKeySettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html
    Properties:
        - Name: KeyProviderServer
        - Name: StaticKeyValue
    
    """
    
    KeyProviderServer_: Optional['InputLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html#cfn-medialive-channel-statickeysettings-keyproviderserver""", alias="KeyProviderServer")
    StaticKeyValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html#cfn-medialive-channel-statickeysettings-statickeyvalue""", alias="StaticKeyValue")
    


    @property
    def tropo_type(self) -> troposphere.medialive.StaticKeySettings:
        from troposphere.medialive import StaticKeySettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TeletextDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextdestinationsettings.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.medialive.TeletextDestinationSettings:
        from troposphere.medialive import TeletextDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TeletextSourceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextsourcesettings.html
    Properties:
        - Name: OutputRectangle
        - Name: PageNumber
    
    """
    
    OutputRectangle_: Optional['CaptionRectangle'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextsourcesettings.html#cfn-medialive-channel-teletextsourcesettings-outputrectangle""", alias="OutputRectangle")
    PageNumber_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextsourcesettings.html#cfn-medialive-channel-teletextsourcesettings-pagenumber""", alias="PageNumber")
    


    @property
    def tropo_type(self) -> troposphere.medialive.TeletextSourceSettings:
        from troposphere.medialive import TeletextSourceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TemporalFilterSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html
    Properties:
        - Name: PostFilterSharpening
        - Name: Strength
    
    """
    
    PostFilterSharpening_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html#cfn-medialive-channel-temporalfiltersettings-postfiltersharpening""", alias="PostFilterSharpening")
    Strength_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html#cfn-medialive-channel-temporalfiltersettings-strength""", alias="Strength")
    


    @property
    def tropo_type(self) -> troposphere.medialive.TemporalFilterSettings:
        from troposphere.medialive import TemporalFilterSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ThumbnailConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-thumbnailconfiguration.html
    Properties:
        - Name: State
    
    """
    
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-thumbnailconfiguration.html#cfn-medialive-channel-thumbnailconfiguration-state""", alias="State")
    


    @property
    def tropo_type(self) -> troposphere.medialive.ThumbnailConfiguration:
        from troposphere.medialive import ThumbnailConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimecodeBurninSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeburninsettings.html
    Properties:
        - Name: FontSize
        - Name: Position
        - Name: Prefix
    
    """
    
    FontSize_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeburninsettings.html#cfn-medialive-channel-timecodeburninsettings-fontsize""", alias="FontSize")
    Position_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeburninsettings.html#cfn-medialive-channel-timecodeburninsettings-position""", alias="Position")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeburninsettings.html#cfn-medialive-channel-timecodeburninsettings-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.medialive.TimecodeBurninSettings:
        from troposphere.medialive import TimecodeBurninSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimecodeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html
    Properties:
        - Name: SyncThreshold
        - Name: Source
    
    """
    
    SyncThreshold_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html#cfn-medialive-channel-timecodeconfig-syncthreshold""", alias="SyncThreshold")
    Source_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html#cfn-medialive-channel-timecodeconfig-source""", alias="Source")
    


    @property
    def tropo_type(self) -> troposphere.medialive.TimecodeConfig:
        from troposphere.medialive import TimecodeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TtmlDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ttmldestinationsettings.html
    Properties:
        - Name: StyleControl
    
    """
    
    StyleControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ttmldestinationsettings.html#cfn-medialive-channel-ttmldestinationsettings-stylecontrol""", alias="StyleControl")
    


    @property
    def tropo_type(self) -> troposphere.medialive.TtmlDestinationSettings:
        from troposphere.medialive import TtmlDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UdpContainerSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpcontainersettings.html
    Properties:
        - Name: M2tsSettings
    
    """
    
    M2tsSettings_: Optional['M2tsSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpcontainersettings.html#cfn-medialive-channel-udpcontainersettings-m2tssettings""", alias="M2tsSettings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.UdpContainerSettings:
        from troposphere.medialive import UdpContainerSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UdpGroupSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html
    Properties:
        - Name: TimedMetadataId3Frame
        - Name: TimedMetadataId3Period
        - Name: InputLossAction
    
    """
    
    TimedMetadataId3Frame_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html#cfn-medialive-channel-udpgroupsettings-timedmetadataid3frame""", alias="TimedMetadataId3Frame")
    TimedMetadataId3Period_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html#cfn-medialive-channel-udpgroupsettings-timedmetadataid3period""", alias="TimedMetadataId3Period")
    InputLossAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html#cfn-medialive-channel-udpgroupsettings-inputlossaction""", alias="InputLossAction")
    


    @property
    def tropo_type(self) -> troposphere.medialive.UdpGroupSettings:
        from troposphere.medialive import UdpGroupSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UdpOutputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html
    Properties:
        - Name: Destination
        - Name: FecOutputSettings
        - Name: ContainerSettings
        - Name: BufferMsec
    
    """
    
    Destination_: Optional['OutputLocationRef'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html#cfn-medialive-channel-udpoutputsettings-destination""", alias="Destination")
    FecOutputSettings_: Optional['FecOutputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html#cfn-medialive-channel-udpoutputsettings-fecoutputsettings""", alias="FecOutputSettings")
    ContainerSettings_: Optional['UdpContainerSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html#cfn-medialive-channel-udpoutputsettings-containersettings""", alias="ContainerSettings")
    BufferMsec_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html#cfn-medialive-channel-udpoutputsettings-buffermsec""", alias="BufferMsec")
    


    @property
    def tropo_type(self) -> troposphere.medialive.UdpOutputSettings:
        from troposphere.medialive import UdpOutputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VideoBlackFailoverSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoblackfailoversettings.html
    Properties:
        - Name: VideoBlackThresholdMsec
        - Name: BlackDetectThreshold
    
    """
    
    VideoBlackThresholdMsec_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoblackfailoversettings.html#cfn-medialive-channel-videoblackfailoversettings-videoblackthresholdmsec""", alias="VideoBlackThresholdMsec")
    BlackDetectThreshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoblackfailoversettings.html#cfn-medialive-channel-videoblackfailoversettings-blackdetectthreshold""", alias="BlackDetectThreshold")
    


    @property
    def tropo_type(self) -> troposphere.medialive.VideoBlackFailoverSettings:
        from troposphere.medialive import VideoBlackFailoverSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VideoCodecSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html
    Properties:
        - Name: Mpeg2Settings
        - Name: FrameCaptureSettings
        - Name: H264Settings
        - Name: H265Settings
    
    """
    
    Mpeg2Settings_: Optional['Mpeg2Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html#cfn-medialive-channel-videocodecsettings-mpeg2settings""", alias="Mpeg2Settings")
    FrameCaptureSettings_: Optional['FrameCaptureSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html#cfn-medialive-channel-videocodecsettings-framecapturesettings""", alias="FrameCaptureSettings")
    H264Settings_: Optional['H264Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html#cfn-medialive-channel-videocodecsettings-h264settings""", alias="H264Settings")
    H265Settings_: Optional['H265Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html#cfn-medialive-channel-videocodecsettings-h265settings""", alias="H265Settings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.VideoCodecSettings:
        from troposphere.medialive import VideoCodecSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VideoDescription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html
    Properties:
        - Name: ScalingBehavior
        - Name: RespondToAfd
        - Name: Height
        - Name: Sharpness
        - Name: Width
        - Name: CodecSettings
        - Name: Name
    
    """
    
    ScalingBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-scalingbehavior""", alias="ScalingBehavior")
    RespondToAfd_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-respondtoafd""", alias="RespondToAfd")
    Height_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-height""", alias="Height")
    Sharpness_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-sharpness""", alias="Sharpness")
    Width_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-width""", alias="Width")
    CodecSettings_: Optional['VideoCodecSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-codecsettings""", alias="CodecSettings")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html#cfn-medialive-channel-videodescription-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.medialive.VideoDescription:
        from troposphere.medialive import VideoDescription as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VideoSelector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html
    Properties:
        - Name: ColorSpaceSettings
        - Name: SelectorSettings
        - Name: ColorSpace
        - Name: ColorSpaceUsage
    
    """
    
    ColorSpaceSettings_: Optional['VideoSelectorColorSpaceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html#cfn-medialive-channel-videoselector-colorspacesettings""", alias="ColorSpaceSettings")
    SelectorSettings_: Optional['VideoSelectorSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html#cfn-medialive-channel-videoselector-selectorsettings""", alias="SelectorSettings")
    ColorSpace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html#cfn-medialive-channel-videoselector-colorspace""", alias="ColorSpace")
    ColorSpaceUsage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html#cfn-medialive-channel-videoselector-colorspaceusage""", alias="ColorSpaceUsage")
    


    @property
    def tropo_type(self) -> troposphere.medialive.VideoSelector:
        from troposphere.medialive import VideoSelector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VideoSelectorColorSpaceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorcolorspacesettings.html
    Properties:
        - Name: Hdr10Settings
    
    """
    
    Hdr10Settings_: Optional['Hdr10Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorcolorspacesettings.html#cfn-medialive-channel-videoselectorcolorspacesettings-hdr10settings""", alias="Hdr10Settings")
    


    @property
    def tropo_type(self) -> troposphere.medialive.VideoSelectorColorSpaceSettings:
        from troposphere.medialive import VideoSelectorColorSpaceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VideoSelectorPid(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorpid.html
    Properties:
        - Name: Pid
    
    """
    
    Pid_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorpid.html#cfn-medialive-channel-videoselectorpid-pid""", alias="Pid")
    


    @property
    def tropo_type(self) -> troposphere.medialive.VideoSelectorPid:
        from troposphere.medialive import VideoSelectorPid as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VideoSelectorProgramId(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorprogramid.html
    Properties:
        - Name: ProgramId
    
    """
    
    ProgramId_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorprogramid.html#cfn-medialive-channel-videoselectorprogramid-programid""", alias="ProgramId")
    


    @property
    def tropo_type(self) -> troposphere.medialive.VideoSelectorProgramId:
        from troposphere.medialive import VideoSelectorProgramId as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VideoSelectorSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorsettings.html
    Properties:
        - Name: VideoSelectorProgramId
        - Name: VideoSelectorPid
    
    """
    
    VideoSelectorProgramId_: Optional['VideoSelectorProgramId'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorsettings.html#cfn-medialive-channel-videoselectorsettings-videoselectorprogramid""", alias="VideoSelectorProgramId")
    VideoSelectorPid_: Optional['VideoSelectorPid'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorsettings.html#cfn-medialive-channel-videoselectorsettings-videoselectorpid""", alias="VideoSelectorPid")
    


    @property
    def tropo_type(self) -> troposphere.medialive.VideoSelectorSettings:
        from troposphere.medialive import VideoSelectorSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcOutputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-vpcoutputsettings.html
    Properties:
        - Name: PublicAddressAllocationIds
        - Name: SecurityGroupIds
        - Name: SubnetIds
    
    """
    
    PublicAddressAllocationIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-vpcoutputsettings.html#cfn-medialive-channel-vpcoutputsettings-publicaddressallocationids""", alias="PublicAddressAllocationIds")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-vpcoutputsettings.html#cfn-medialive-channel-vpcoutputsettings-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-vpcoutputsettings.html#cfn-medialive-channel-vpcoutputsettings-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.medialive.VpcOutputSettings:
        from troposphere.medialive import VpcOutputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WavSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-wavsettings.html
    Properties:
        - Name: CodingMode
        - Name: SampleRate
        - Name: BitDepth
    
    """
    
    CodingMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-wavsettings.html#cfn-medialive-channel-wavsettings-codingmode""", alias="CodingMode")
    SampleRate_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-wavsettings.html#cfn-medialive-channel-wavsettings-samplerate""", alias="SampleRate")
    BitDepth_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-wavsettings.html#cfn-medialive-channel-wavsettings-bitdepth""", alias="BitDepth")
    


    @property
    def tropo_type(self) -> troposphere.medialive.WavSettings:
        from troposphere.medialive import WavSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WebvttDestinationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-webvttdestinationsettings.html
    Properties:
        - Name: StyleControl
    
    """
    
    StyleControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-webvttdestinationsettings.html#cfn-medialive-channel-webvttdestinationsettings-stylecontrol""", alias="StyleControl")
    


    @property
    def tropo_type(self) -> troposphere.medialive.WebvttDestinationSettings:
        from troposphere.medialive import WebvttDestinationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputDestinationRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdestinationrequest.html
    Properties:
        - Name: StreamName
    
    """
    
    StreamName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdestinationrequest.html#cfn-medialive-input-inputdestinationrequest-streamname""", alias="StreamName")
    


    @property
    def tropo_type(self) -> troposphere.medialive.InputDestinationRequest:
        from troposphere.medialive import InputDestinationRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputDeviceRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicerequest.html
    Properties:
        - Name: Id
    
    """
    
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicerequest.html#cfn-medialive-input-inputdevicerequest-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.medialive.InputDeviceRequest:
        from troposphere.medialive import InputDeviceRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputDeviceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicesettings.html
    Properties:
        - Name: Id
    
    """
    
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicesettings.html#cfn-medialive-input-inputdevicesettings-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.medialive.InputDeviceSettings:
        from troposphere.medialive import InputDeviceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputSourceRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputsourcerequest.html
    Properties:
        - Name: Username
        - Name: PasswordParam
        - Name: Url
    
    """
    
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputsourcerequest.html#cfn-medialive-input-inputsourcerequest-username""", alias="Username")
    PasswordParam_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputsourcerequest.html#cfn-medialive-input-inputsourcerequest-passwordparam""", alias="PasswordParam")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputsourcerequest.html#cfn-medialive-input-inputsourcerequest-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.medialive.InputSourceRequest:
        from troposphere.medialive import InputSourceRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputVpcRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputvpcrequest.html
    Properties:
        - Name: SecurityGroupIds
        - Name: SubnetIds
    
    """
    
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputvpcrequest.html#cfn-medialive-input-inputvpcrequest-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputvpcrequest.html#cfn-medialive-input-inputvpcrequest-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.medialive.InputVpcRequest:
        from troposphere.medialive import InputVpcRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MediaConnectFlowRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-mediaconnectflowrequest.html
    Properties:
        - Name: FlowArn
    
    """
    
    FlowArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-mediaconnectflowrequest.html#cfn-medialive-input-mediaconnectflowrequest-flowarn""", alias="FlowArn")
    


    @property
    def tropo_type(self) -> troposphere.medialive.MediaConnectFlowRequest:
        from troposphere.medialive import MediaConnectFlowRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputWhitelistRuleCidr(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr.html
    Properties:
        - Name: Cidr
    
    """
    
    Cidr_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr.html#cfn-medialive-inputsecuritygroup-inputwhitelistrulecidr-cidr""", alias="Cidr")
    


    @property
    def tropo_type(self) -> troposphere.medialive.InputWhitelistRuleCidr:
        from troposphere.medialive import InputWhitelistRuleCidr as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Channel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html
    Properties:
        - Name: InputAttachments
        - Name: InputSpecification
        - Name: ChannelClass
        - Name: EncoderSettings
        - Name: Destinations
        - Name: Vpc
        - Name: CdiInputSpecification
        - Name: Maintenance
        - Name: LogLevel
        - Name: RoleArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
        - Name: Inputs
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InputAttachments_: Optional[List['InputAttachment']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-inputattachments""", alias="InputAttachments")
    InputSpecification_: Optional['InputSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-inputspecification""", alias="InputSpecification")
    ChannelClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-channelclass""", alias="ChannelClass")
    EncoderSettings_: Optional['EncoderSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-encodersettings""", alias="EncoderSettings")
    Destinations_: Optional[List['OutputDestination']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-destinations""", alias="Destinations")
    Vpc_: Optional['VpcOutputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-vpc""", alias="Vpc")
    CdiInputSpecification_: Optional['CdiInputSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-cdiinputspecification""", alias="CdiInputSpecification")
    Maintenance_: Optional['MaintenanceCreateSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-maintenance""", alias="Maintenance")
    LogLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-loglevel""", alias="LogLevel")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-rolearn""", alias="RoleArn")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html#cfn-medialive-channel-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.medialive.Channel:
        from troposphere.medialive import Channel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.medialive import Channel as TropoT
        return resource_to_troposphere(self, TropoT)


class Input(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html
    Properties:
        - Name: Type
        - Name: Destinations
        - Name: Vpc
        - Name: MediaConnectFlows
        - Name: InputSecurityGroups
        - Name: InputDevices
        - Name: Sources
        - Name: RoleArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Destinations
        - Name: Arn
        - Name: Sources
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-type""", alias="Type")
    Destinations_: Optional[List['InputDestinationRequest']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-destinations""", alias="Destinations")
    Vpc_: Optional['InputVpcRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-vpc""", alias="Vpc")
    MediaConnectFlows_: Optional[List['MediaConnectFlowRequest']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-mediaconnectflows""", alias="MediaConnectFlows")
    InputSecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-inputsecuritygroups""", alias="InputSecurityGroups")
    InputDevices_: Optional[List['InputDeviceSettings']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-inputdevices""", alias="InputDevices")
    Sources_: Optional[List['InputSourceRequest']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-sources""", alias="Sources")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-rolearn""", alias="RoleArn")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html#cfn-medialive-input-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.medialive.Input:
        from troposphere.medialive import Input as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.medialive import Input as TropoT
        return resource_to_troposphere(self, TropoT)


class InputSecurityGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html
    Properties:
        - Name: WhitelistRules
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    WhitelistRules_: Optional[List['InputWhitelistRuleCidr']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html#cfn-medialive-inputsecuritygroup-whitelistrules""", alias="WhitelistRules")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html#cfn-medialive-inputsecuritygroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.medialive.InputSecurityGroup:
        from troposphere.medialive import InputSecurityGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.medialive import InputSecurityGroup as TropoT
        return resource_to_troposphere(self, TropoT)

