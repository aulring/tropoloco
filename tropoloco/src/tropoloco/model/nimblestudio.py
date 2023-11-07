from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class StreamConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html
    Properties:
        - Name: MaxSessionLengthInMinutes
        - Name: ClipboardMode
        - Name: StreamingImageIds
        - Name: MaxStoppedSessionLengthInMinutes
        - Name: SessionPersistenceMode
        - Name: AutomaticTerminationMode
        - Name: SessionBackup
        - Name: Ec2InstanceTypes
        - Name: SessionStorage
        - Name: VolumeConfiguration
    
    """
    
    MaxSessionLengthInMinutes_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-maxsessionlengthinminutes""", alias="MaxSessionLengthInMinutes")
    ClipboardMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-clipboardmode""", alias="ClipboardMode")
    StreamingImageIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-streamingimageids""", alias="StreamingImageIds")
    MaxStoppedSessionLengthInMinutes_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-maxstoppedsessionlengthinminutes""", alias="MaxStoppedSessionLengthInMinutes")
    SessionPersistenceMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-sessionpersistencemode""", alias="SessionPersistenceMode")
    AutomaticTerminationMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-automaticterminationmode""", alias="AutomaticTerminationMode")
    SessionBackup_: Optional['StreamConfigurationSessionBackup'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-sessionbackup""", alias="SessionBackup")
    Ec2InstanceTypes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-ec2instancetypes""", alias="Ec2InstanceTypes")
    SessionStorage_: Optional['StreamConfigurationSessionStorage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-sessionstorage""", alias="SessionStorage")
    VolumeConfiguration_: Optional['VolumeConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-volumeconfiguration""", alias="VolumeConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.StreamConfiguration:
        from troposphere.nimblestudio import StreamConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StreamConfigurationSessionBackup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfigurationsessionbackup.html
    Properties:
        - Name: Mode
        - Name: MaxBackupsToRetain
    
    """
    
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfigurationsessionbackup.html#cfn-nimblestudio-launchprofile-streamconfigurationsessionbackup-mode""", alias="Mode")
    MaxBackupsToRetain_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfigurationsessionbackup.html#cfn-nimblestudio-launchprofile-streamconfigurationsessionbackup-maxbackupstoretain""", alias="MaxBackupsToRetain")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.StreamConfigurationSessionBackup:
        from troposphere.nimblestudio import StreamConfigurationSessionBackup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StreamConfigurationSessionStorage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfigurationsessionstorage.html
    Properties:
        - Name: Root
        - Name: Mode
    
    """
    
    Root_: Optional['StreamingSessionStorageRoot'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfigurationsessionstorage.html#cfn-nimblestudio-launchprofile-streamconfigurationsessionstorage-root""", alias="Root")
    Mode_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfigurationsessionstorage.html#cfn-nimblestudio-launchprofile-streamconfigurationsessionstorage-mode""", alias="Mode")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.StreamConfigurationSessionStorage:
        from troposphere.nimblestudio import StreamConfigurationSessionStorage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StreamingSessionStorageRoot(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamingsessionstorageroot.html
    Properties:
        - Name: Linux
        - Name: Windows
    
    """
    
    Linux_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamingsessionstorageroot.html#cfn-nimblestudio-launchprofile-streamingsessionstorageroot-linux""", alias="Linux")
    Windows_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamingsessionstorageroot.html#cfn-nimblestudio-launchprofile-streamingsessionstorageroot-windows""", alias="Windows")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.StreamingSessionStorageRoot:
        from troposphere.nimblestudio import StreamingSessionStorageRoot as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VolumeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-volumeconfiguration.html
    Properties:
        - Name: Size
        - Name: Throughput
        - Name: Iops
    
    """
    
    Size_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-volumeconfiguration.html#cfn-nimblestudio-launchprofile-volumeconfiguration-size""", alias="Size")
    Throughput_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-volumeconfiguration.html#cfn-nimblestudio-launchprofile-volumeconfiguration-throughput""", alias="Throughput")
    Iops_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-volumeconfiguration.html#cfn-nimblestudio-launchprofile-volumeconfiguration-iops""", alias="Iops")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.VolumeConfiguration:
        from troposphere.nimblestudio import VolumeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StreamingImageEncryptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-streamingimage-streamingimageencryptionconfiguration.html
    Properties:
        - Name: KeyType
        - Name: KeyArn
    
    """
    
    KeyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-streamingimage-streamingimageencryptionconfiguration.html#cfn-nimblestudio-streamingimage-streamingimageencryptionconfiguration-keytype""", alias="KeyType")
    KeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-streamingimage-streamingimageencryptionconfiguration.html#cfn-nimblestudio-streamingimage-streamingimageencryptionconfiguration-keyarn""", alias="KeyArn")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.StreamingImageEncryptionConfiguration:
        from troposphere.nimblestudio import StreamingImageEncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StudioEncryptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studio-studioencryptionconfiguration.html
    Properties:
        - Name: KeyType
        - Name: KeyArn
    
    """
    
    KeyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studio-studioencryptionconfiguration.html#cfn-nimblestudio-studio-studioencryptionconfiguration-keytype""", alias="KeyType")
    KeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studio-studioencryptionconfiguration.html#cfn-nimblestudio-studio-studioencryptionconfiguration-keyarn""", alias="KeyArn")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.StudioEncryptionConfiguration:
        from troposphere.nimblestudio import StudioEncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ActiveDirectoryComputerAttribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectorycomputerattribute.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectorycomputerattribute.html#cfn-nimblestudio-studiocomponent-activedirectorycomputerattribute-value""", alias="Value")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectorycomputerattribute.html#cfn-nimblestudio-studiocomponent-activedirectorycomputerattribute-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.ActiveDirectoryComputerAttribute:
        from troposphere.nimblestudio import ActiveDirectoryComputerAttribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ActiveDirectoryConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectoryconfiguration.html
    Properties:
        - Name: DirectoryId
        - Name: OrganizationalUnitDistinguishedName
        - Name: ComputerAttributes
    
    """
    
    DirectoryId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectoryconfiguration.html#cfn-nimblestudio-studiocomponent-activedirectoryconfiguration-directoryid""", alias="DirectoryId")
    OrganizationalUnitDistinguishedName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectoryconfiguration.html#cfn-nimblestudio-studiocomponent-activedirectoryconfiguration-organizationalunitdistinguishedname""", alias="OrganizationalUnitDistinguishedName")
    ComputerAttributes_: Optional[List['ActiveDirectoryComputerAttribute']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectoryconfiguration.html#cfn-nimblestudio-studiocomponent-activedirectoryconfiguration-computerattributes""", alias="ComputerAttributes")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.ActiveDirectoryConfiguration:
        from troposphere.nimblestudio import ActiveDirectoryConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComputeFarmConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-computefarmconfiguration.html
    Properties:
        - Name: ActiveDirectoryUser
        - Name: Endpoint
    
    """
    
    ActiveDirectoryUser_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-computefarmconfiguration.html#cfn-nimblestudio-studiocomponent-computefarmconfiguration-activedirectoryuser""", alias="ActiveDirectoryUser")
    Endpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-computefarmconfiguration.html#cfn-nimblestudio-studiocomponent-computefarmconfiguration-endpoint""", alias="Endpoint")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.ComputeFarmConfiguration:
        from troposphere.nimblestudio import ComputeFarmConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LicenseServiceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-licenseserviceconfiguration.html
    Properties:
        - Name: Endpoint
    
    """
    
    Endpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-licenseserviceconfiguration.html#cfn-nimblestudio-studiocomponent-licenseserviceconfiguration-endpoint""", alias="Endpoint")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.LicenseServiceConfiguration:
        from troposphere.nimblestudio import LicenseServiceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScriptParameterKeyValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-scriptparameterkeyvalue.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-scriptparameterkeyvalue.html#cfn-nimblestudio-studiocomponent-scriptparameterkeyvalue-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-scriptparameterkeyvalue.html#cfn-nimblestudio-studiocomponent-scriptparameterkeyvalue-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.ScriptParameterKeyValue:
        from troposphere.nimblestudio import ScriptParameterKeyValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SharedFileSystemConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html
    Properties:
        - Name: Endpoint
        - Name: FileSystemId
        - Name: ShareName
        - Name: WindowsMountDrive
        - Name: LinuxMountPoint
    
    """
    
    Endpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-endpoint""", alias="Endpoint")
    FileSystemId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-filesystemid""", alias="FileSystemId")
    ShareName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-sharename""", alias="ShareName")
    WindowsMountDrive_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-windowsmountdrive""", alias="WindowsMountDrive")
    LinuxMountPoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-linuxmountpoint""", alias="LinuxMountPoint")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.SharedFileSystemConfiguration:
        from troposphere.nimblestudio import SharedFileSystemConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StudioComponentConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html
    Properties:
        - Name: LicenseServiceConfiguration
        - Name: ComputeFarmConfiguration
        - Name: ActiveDirectoryConfiguration
        - Name: SharedFileSystemConfiguration
    
    """
    
    LicenseServiceConfiguration_: Optional['LicenseServiceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html#cfn-nimblestudio-studiocomponent-studiocomponentconfiguration-licenseserviceconfiguration""", alias="LicenseServiceConfiguration")
    ComputeFarmConfiguration_: Optional['ComputeFarmConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html#cfn-nimblestudio-studiocomponent-studiocomponentconfiguration-computefarmconfiguration""", alias="ComputeFarmConfiguration")
    ActiveDirectoryConfiguration_: Optional['ActiveDirectoryConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html#cfn-nimblestudio-studiocomponent-studiocomponentconfiguration-activedirectoryconfiguration""", alias="ActiveDirectoryConfiguration")
    SharedFileSystemConfiguration_: Optional['SharedFileSystemConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html#cfn-nimblestudio-studiocomponent-studiocomponentconfiguration-sharedfilesystemconfiguration""", alias="SharedFileSystemConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.StudioComponentConfiguration:
        from troposphere.nimblestudio import StudioComponentConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StudioComponentInitializationScript(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html
    Properties:
        - Name: Script
        - Name: LaunchProfileProtocolVersion
        - Name: Platform
        - Name: RunContext
    
    """
    
    Script_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html#cfn-nimblestudio-studiocomponent-studiocomponentinitializationscript-script""", alias="Script")
    LaunchProfileProtocolVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html#cfn-nimblestudio-studiocomponent-studiocomponentinitializationscript-launchprofileprotocolversion""", alias="LaunchProfileProtocolVersion")
    Platform_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html#cfn-nimblestudio-studiocomponent-studiocomponentinitializationscript-platform""", alias="Platform")
    RunContext_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html#cfn-nimblestudio-studiocomponent-studiocomponentinitializationscript-runcontext""", alias="RunContext")
    


    @property
    def tropo_type(self) -> troposphere.nimblestudio.StudioComponentInitializationScript:
        from troposphere.nimblestudio import StudioComponentInitializationScript as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class LaunchProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html
    Properties:
        - Name: Description
        - Name: Ec2SubnetIds
        - Name: StudioComponentIds
        - Name: StreamConfiguration
        - Name: LaunchProfileProtocolVersions
        - Name: StudioId
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LaunchProfileId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-description""", alias="Description")
    Ec2SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-ec2subnetids""", alias="Ec2SubnetIds")
    StudioComponentIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-studiocomponentids""", alias="StudioComponentIds")
    StreamConfiguration_: 'StreamConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-streamconfiguration""", alias="StreamConfiguration")
    LaunchProfileProtocolVersions_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-launchprofileprotocolversions""", alias="LaunchProfileProtocolVersions")
    StudioId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-studioid""", alias="StudioId")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.nimblestudio.LaunchProfile:
        from troposphere.nimblestudio import LaunchProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.nimblestudio import LaunchProfile as TropoT
        return resource_to_troposphere(self, TropoT)


class StreamingImage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html
    Properties:
        - Name: Description
        - Name: Ec2ImageId
        - Name: StudioId
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Owner
        - Name: Platform
        - Name: EncryptionConfiguration
        - Name: EulaIds
        - Name: EncryptionConfiguration.KeyArn
        - Name: EncryptionConfiguration.KeyType
        - Name: StreamingImageId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-description""", alias="Description")
    Ec2ImageId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-ec2imageid""", alias="Ec2ImageId")
    StudioId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-studioid""", alias="StudioId")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.nimblestudio.StreamingImage:
        from troposphere.nimblestudio import StreamingImage as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.nimblestudio import StreamingImage as TropoT
        return resource_to_troposphere(self, TropoT)


class Studio(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html
    Properties:
        - Name: UserRoleArn
        - Name: DisplayName
        - Name: StudioName
        - Name: AdminRoleArn
        - Name: StudioEncryptionConfiguration
        - Name: Tags
    Attributes:
        - Name: HomeRegion
        - Name: StudioUrl
        - Name: SsoClientId
        - Name: StudioId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UserRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-userrolearn""", alias="UserRoleArn")
    DisplayName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-displayname""", alias="DisplayName")
    StudioName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-studioname""", alias="StudioName")
    AdminRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-adminrolearn""", alias="AdminRoleArn")
    StudioEncryptionConfiguration_: Optional['StudioEncryptionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-studioencryptionconfiguration""", alias="StudioEncryptionConfiguration")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.nimblestudio.Studio:
        from troposphere.nimblestudio import Studio as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.nimblestudio import Studio as TropoT
        return resource_to_troposphere(self, TropoT)


class StudioComponent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html
    Properties:
        - Name: Configuration
        - Name: Description
        - Name: Ec2SecurityGroupIds
        - Name: InitializationScripts
        - Name: Name
        - Name: ScriptParameters
        - Name: StudioId
        - Name: Subtype
        - Name: Tags
        - Name: Type
    Attributes:
        - Name: StudioComponentId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Configuration_: Optional['StudioComponentConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-configuration""", alias="Configuration")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-description""", alias="Description")
    Ec2SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-ec2securitygroupids""", alias="Ec2SecurityGroupIds")
    InitializationScripts_: Optional[List['StudioComponentInitializationScript']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-initializationscripts""", alias="InitializationScripts")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-name""", alias="Name")
    ScriptParameters_: Optional[List['ScriptParameterKeyValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-scriptparameters""", alias="ScriptParameters")
    StudioId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-studioid""", alias="StudioId")
    Subtype_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-subtype""", alias="Subtype")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-tags""", alias="Tags")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-type""", alias="Type")
    

    @property
    def tropo_type(self) -> troposphere.nimblestudio.StudioComponent:
        from troposphere.nimblestudio import StudioComponent as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.nimblestudio import StudioComponent as TropoT
        return resource_to_troposphere(self, TropoT)

