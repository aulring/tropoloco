from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AccessPointTag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-accesspointtag.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-accesspointtag.html#cfn-efs-accesspoint-accesspointtag-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-accesspointtag.html#cfn-efs-accesspoint-accesspointtag-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.efs.AccessPointTag:
        from troposphere.efs import AccessPointTag as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CreationInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html
    Properties:
        - Name: OwnerGid
        - Name: OwnerUid
        - Name: Permissions
    
    """
    
    OwnerGid_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html#cfn-efs-accesspoint-creationinfo-ownergid""", alias="OwnerGid")
    OwnerUid_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html#cfn-efs-accesspoint-creationinfo-owneruid""", alias="OwnerUid")
    Permissions_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html#cfn-efs-accesspoint-creationinfo-permissions""", alias="Permissions")
    


    @property
    def tropo_type(self) -> troposphere.efs.CreationInfo:
        from troposphere.efs import CreationInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PosixUser(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html
    Properties:
        - Name: Uid
        - Name: SecondaryGids
        - Name: Gid
    
    """
    
    Uid_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html#cfn-efs-accesspoint-posixuser-uid""", alias="Uid")
    SecondaryGids_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html#cfn-efs-accesspoint-posixuser-secondarygids""", alias="SecondaryGids")
    Gid_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html#cfn-efs-accesspoint-posixuser-gid""", alias="Gid")
    


    @property
    def tropo_type(self) -> troposphere.efs.PosixUser:
        from troposphere.efs import PosixUser as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RootDirectory(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html
    Properties:
        - Name: Path
        - Name: CreationInfo
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html#cfn-efs-accesspoint-rootdirectory-path""", alias="Path")
    CreationInfo_: Optional['CreationInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html#cfn-efs-accesspoint-rootdirectory-creationinfo""", alias="CreationInfo")
    


    @property
    def tropo_type(self) -> troposphere.efs.RootDirectory:
        from troposphere.efs import RootDirectory as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BackupPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-backuppolicy.html
    Properties:
        - Name: Status
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-backuppolicy.html#cfn-efs-filesystem-backuppolicy-status""", alias="Status")
    


    @property
    def tropo_type(self) -> troposphere.efs.BackupPolicy:
        from troposphere.efs import BackupPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ElasticFileSystemTag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-elasticfilesystemtag.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-elasticfilesystemtag.html#cfn-efs-filesystem-elasticfilesystemtag-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-elasticfilesystemtag.html#cfn-efs-filesystem-elasticfilesystemtag-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.efs.ElasticFileSystemTag:
        from troposphere.efs import ElasticFileSystemTag as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LifecyclePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-lifecyclepolicy.html
    Properties:
        - Name: TransitionToIA
        - Name: TransitionToPrimaryStorageClass
    
    """
    
    TransitionToIA_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-lifecyclepolicy.html#cfn-efs-filesystem-lifecyclepolicy-transitiontoia""", alias="TransitionToIA")
    TransitionToPrimaryStorageClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-lifecyclepolicy.html#cfn-efs-filesystem-lifecyclepolicy-transitiontoprimarystorageclass""", alias="TransitionToPrimaryStorageClass")
    


    @property
    def tropo_type(self) -> troposphere.efs.LifecyclePolicy:
        from troposphere.efs import LifecyclePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-replicationconfiguration.html
    Properties:
        - Name: Destinations
    
    """
    
    Destinations_: Optional[List['ReplicationDestination']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-replicationconfiguration.html#cfn-efs-filesystem-replicationconfiguration-destinations""", alias="Destinations")
    


    @property
    def tropo_type(self) -> troposphere.efs.ReplicationConfiguration:
        from troposphere.efs import ReplicationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-replicationdestination.html
    Properties:
        - Name: KmsKeyId
        - Name: AvailabilityZoneName
        - Name: FileSystemId
        - Name: Region
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-replicationdestination.html#cfn-efs-filesystem-replicationdestination-kmskeyid""", alias="KmsKeyId")
    AvailabilityZoneName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-replicationdestination.html#cfn-efs-filesystem-replicationdestination-availabilityzonename""", alias="AvailabilityZoneName")
    FileSystemId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-replicationdestination.html#cfn-efs-filesystem-replicationdestination-filesystemid""", alias="FileSystemId")
    Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-replicationdestination.html#cfn-efs-filesystem-replicationdestination-region""", alias="Region")
    


    @property
    def tropo_type(self) -> troposphere.efs.ReplicationDestination:
        from troposphere.efs import ReplicationDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AccessPoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html
    Properties:
        - Name: FileSystemId
        - Name: RootDirectory
        - Name: ClientToken
        - Name: AccessPointTags
        - Name: PosixUser
    Attributes:
        - Name: AccessPointId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FileSystemId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-filesystemid""", alias="FileSystemId")
    RootDirectory_: Optional['RootDirectory'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-rootdirectory""", alias="RootDirectory")
    ClientToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-clienttoken""", alias="ClientToken")
    AccessPointTags_: Optional[List['AccessPointTag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-accesspointtags""", alias="AccessPointTags")
    PosixUser_: Optional['PosixUser'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-posixuser""", alias="PosixUser")
    

    @property
    def tropo_type(self) -> troposphere.efs.AccessPoint:
        from troposphere.efs import AccessPoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.efs import AccessPoint as TropoT
        return resource_to_troposphere(self, TropoT)


class FileSystem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html
    Properties:
        - Name: KmsKeyId
        - Name: PerformanceMode
        - Name: Encrypted
        - Name: BypassPolicyLockoutSafetyCheck
        - Name: FileSystemTags
        - Name: ProvisionedThroughputInMibps
        - Name: FileSystemPolicy
        - Name: AvailabilityZoneName
        - Name: LifecyclePolicies
        - Name: ThroughputMode
        - Name: ReplicationConfiguration
        - Name: BackupPolicy
    Attributes:
        - Name: FileSystemId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-kmskeyid""", alias="KmsKeyId")
    PerformanceMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-performancemode""", alias="PerformanceMode")
    Encrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-encrypted""", alias="Encrypted")
    BypassPolicyLockoutSafetyCheck_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-bypasspolicylockoutsafetycheck""", alias="BypassPolicyLockoutSafetyCheck")
    FileSystemTags_: Optional[List['ElasticFileSystemTag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-filesystemtags""", alias="FileSystemTags")
    ProvisionedThroughputInMibps_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-provisionedthroughputinmibps""", alias="ProvisionedThroughputInMibps")
    FileSystemPolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-filesystempolicy""", alias="FileSystemPolicy")
    AvailabilityZoneName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-availabilityzonename""", alias="AvailabilityZoneName")
    LifecyclePolicies_: Optional[List['LifecyclePolicy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-lifecyclepolicies""", alias="LifecyclePolicies")
    ThroughputMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-throughputmode""", alias="ThroughputMode")
    ReplicationConfiguration_: Optional['ReplicationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-replicationconfiguration""", alias="ReplicationConfiguration")
    BackupPolicy_: Optional['BackupPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-backuppolicy""", alias="BackupPolicy")
    

    @property
    def tropo_type(self) -> troposphere.efs.FileSystem:
        from troposphere.efs import FileSystem as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.efs import FileSystem as TropoT
        return resource_to_troposphere(self, TropoT)


class MountTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html
    Properties:
        - Name: SecurityGroups
        - Name: FileSystemId
        - Name: IpAddress
        - Name: SubnetId
    Attributes:
        - Name: IpAddress
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SecurityGroups_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-securitygroups""", alias="SecurityGroups")
    FileSystemId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-filesystemid""", alias="FileSystemId")
    IpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-ipaddress""", alias="IpAddress")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-subnetid""", alias="SubnetId")
    

    @property
    def tropo_type(self) -> troposphere.efs.MountTarget:
        from troposphere.efs import MountTarget as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.efs import MountTarget as TropoT
        return resource_to_troposphere(self, TropoT)

