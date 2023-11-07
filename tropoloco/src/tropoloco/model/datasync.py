from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AzureBlobSasConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationazureblob-azureblobsasconfiguration.html
    Properties:
        - Name: AzureBlobSasToken
    
    """
    
    AzureBlobSasToken_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationazureblob-azureblobsasconfiguration.html#cfn-datasync-locationazureblob-azureblobsasconfiguration-azureblobsastoken""", alias="AzureBlobSasToken")
    


    @property
    def tropo_type(self) -> troposphere.datasync.AzureBlobSasConfiguration:
        from troposphere.datasync import AzureBlobSasConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ec2Config(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html
    Properties:
        - Name: SubnetArn
        - Name: SecurityGroupArns
    
    """
    
    SubnetArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html#cfn-datasync-locationefs-ec2config-subnetarn""", alias="SubnetArn")
    SecurityGroupArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html#cfn-datasync-locationefs-ec2config-securitygrouparns""", alias="SecurityGroupArns")
    


    @property
    def tropo_type(self) -> troposphere.datasync.Ec2Config:
        from troposphere.datasync import Ec2Config as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NFS(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-nfs.html
    Properties:
        - Name: MountOptions
    
    """
    
    MountOptions_: 'NfsMountOptions' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-nfs.html#cfn-datasync-locationfsxontap-nfs-mountoptions""", alias="MountOptions")
    


    @property
    def tropo_type(self) -> troposphere.datasync.NFS:
        from troposphere.datasync import NFS as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NfsMountOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-nfsmountoptions.html
    Properties:
        - Name: Version
    
    """
    
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-nfsmountoptions.html#cfn-datasync-locationfsxontap-nfsmountoptions-version""", alias="Version")
    


    @property
    def tropo_type(self) -> troposphere.datasync.NfsMountOptions:
        from troposphere.datasync import NfsMountOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Protocol(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-protocol.html
    Properties:
        - Name: SMB
        - Name: NFS
    
    """
    
    SMB_: Optional['SMB'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-protocol.html#cfn-datasync-locationfsxontap-protocol-smb""", alias="SMB")
    NFS_: Optional['NFS'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-protocol.html#cfn-datasync-locationfsxontap-protocol-nfs""", alias="NFS")
    


    @property
    def tropo_type(self) -> troposphere.datasync.Protocol:
        from troposphere.datasync import Protocol as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SMB(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smb.html
    Properties:
        - Name: User
        - Name: Domain
        - Name: MountOptions
        - Name: Password
    
    """
    
    User_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smb.html#cfn-datasync-locationfsxontap-smb-user""", alias="User")
    Domain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smb.html#cfn-datasync-locationfsxontap-smb-domain""", alias="Domain")
    MountOptions_: 'SmbMountOptions' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smb.html#cfn-datasync-locationfsxontap-smb-mountoptions""", alias="MountOptions")
    Password_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smb.html#cfn-datasync-locationfsxontap-smb-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.datasync.SMB:
        from troposphere.datasync import SMB as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SmbMountOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smbmountoptions.html
    Properties:
        - Name: Version
    
    """
    
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smbmountoptions.html#cfn-datasync-locationfsxontap-smbmountoptions-version""", alias="Version")
    


    @property
    def tropo_type(self) -> troposphere.datasync.SmbMountOptions:
        from troposphere.datasync import SmbMountOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MountOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-mountoptions.html
    Properties:
        - Name: Version
    
    """
    
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-mountoptions.html#cfn-datasync-locationfsxopenzfs-mountoptions-version""", alias="Version")
    


    @property
    def tropo_type(self) -> troposphere.datasync.MountOptions:
        from troposphere.datasync import MountOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NFS(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-nfs.html
    Properties:
        - Name: MountOptions
    
    """
    
    MountOptions_: 'MountOptions' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-nfs.html#cfn-datasync-locationfsxopenzfs-nfs-mountoptions""", alias="MountOptions")
    


    @property
    def tropo_type(self) -> troposphere.datasync.NFS:
        from troposphere.datasync import NFS as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Protocol(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-protocol.html
    Properties:
        - Name: NFS
    
    """
    
    NFS_: Optional['NFS'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxopenzfs-protocol.html#cfn-datasync-locationfsxopenzfs-protocol-nfs""", alias="NFS")
    


    @property
    def tropo_type(self) -> troposphere.datasync.Protocol:
        from troposphere.datasync import Protocol as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NameNode(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-namenode.html
    Properties:
        - Name: Port
        - Name: Hostname
    
    """
    
    Port_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-namenode.html#cfn-datasync-locationhdfs-namenode-port""", alias="Port")
    Hostname_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-namenode.html#cfn-datasync-locationhdfs-namenode-hostname""", alias="Hostname")
    


    @property
    def tropo_type(self) -> troposphere.datasync.NameNode:
        from troposphere.datasync import NameNode as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QopConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-qopconfiguration.html
    Properties:
        - Name: RpcProtection
        - Name: DataTransferProtection
    
    """
    
    RpcProtection_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-qopconfiguration.html#cfn-datasync-locationhdfs-qopconfiguration-rpcprotection""", alias="RpcProtection")
    DataTransferProtection_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-qopconfiguration.html#cfn-datasync-locationhdfs-qopconfiguration-datatransferprotection""", alias="DataTransferProtection")
    


    @property
    def tropo_type(self) -> troposphere.datasync.QopConfiguration:
        from troposphere.datasync import QopConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MountOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-mountoptions.html
    Properties:
        - Name: Version
    
    """
    
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-mountoptions.html#cfn-datasync-locationnfs-mountoptions-version""", alias="Version")
    


    @property
    def tropo_type(self) -> troposphere.datasync.MountOptions:
        from troposphere.datasync import MountOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnPremConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-onpremconfig.html
    Properties:
        - Name: AgentArns
    
    """
    
    AgentArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-onpremconfig.html#cfn-datasync-locationnfs-onpremconfig-agentarns""", alias="AgentArns")
    


    @property
    def tropo_type(self) -> troposphere.datasync.OnPremConfig:
        from troposphere.datasync import OnPremConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Config(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locations3-s3config.html
    Properties:
        - Name: BucketAccessRoleArn
    
    """
    
    BucketAccessRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locations3-s3config.html#cfn-datasync-locations3-s3config-bucketaccessrolearn""", alias="BucketAccessRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.datasync.S3Config:
        from troposphere.datasync import S3Config as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MountOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationsmb-mountoptions.html
    Properties:
        - Name: Version
    
    """
    
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationsmb-mountoptions.html#cfn-datasync-locationsmb-mountoptions-version""", alias="Version")
    


    @property
    def tropo_type(self) -> troposphere.datasync.MountOptions:
        from troposphere.datasync import MountOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServerConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-serverconfiguration.html
    Properties:
        - Name: ServerHostname
        - Name: ServerPort
    
    """
    
    ServerHostname_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-serverconfiguration.html#cfn-datasync-storagesystem-serverconfiguration-serverhostname""", alias="ServerHostname")
    ServerPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-serverconfiguration.html#cfn-datasync-storagesystem-serverconfiguration-serverport""", alias="ServerPort")
    


    @property
    def tropo_type(self) -> troposphere.datasync.ServerConfiguration:
        from troposphere.datasync import ServerConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServerCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-servercredentials.html
    Properties:
        - Name: Username
        - Name: Password
    
    """
    
    Username_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-servercredentials.html#cfn-datasync-storagesystem-servercredentials-username""", alias="Username")
    Password_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-storagesystem-servercredentials.html#cfn-datasync-storagesystem-servercredentials-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.datasync.ServerCredentials:
        from troposphere.datasync import ServerCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Deleted(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-deleted.html
    Properties:
        - Name: ReportLevel
    
    """
    
    ReportLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-deleted.html#cfn-datasync-task-deleted-reportlevel""", alias="ReportLevel")
    


    @property
    def tropo_type(self) -> troposphere.datasync.Deleted:
        from troposphere.datasync import Deleted as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Destination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-destination.html
    Properties:
        - Name: S3
    
    """
    
    S3_: Optional['S3'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-destination.html#cfn-datasync-task-destination-s3""", alias="S3")
    


    @property
    def tropo_type(self) -> troposphere.datasync.Destination:
        from troposphere.datasync import Destination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FilterRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html
    Properties:
        - Name: FilterType
        - Name: Value
    
    """
    
    FilterType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html#cfn-datasync-task-filterrule-filtertype""", alias="FilterType")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html#cfn-datasync-task-filterrule-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.datasync.FilterRule:
        from troposphere.datasync import FilterRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Options(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html
    Properties:
        - Name: VerifyMode
        - Name: Gid
        - Name: Atime
        - Name: OverwriteMode
        - Name: PreserveDevices
        - Name: Mtime
        - Name: TaskQueueing
        - Name: TransferMode
        - Name: LogLevel
        - Name: ObjectTags
        - Name: Uid
        - Name: BytesPerSecond
        - Name: PosixPermissions
        - Name: PreserveDeletedFiles
        - Name: SecurityDescriptorCopyFlags
    
    """
    
    VerifyMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-verifymode""", alias="VerifyMode")
    Gid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-gid""", alias="Gid")
    Atime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-atime""", alias="Atime")
    OverwriteMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-overwritemode""", alias="OverwriteMode")
    PreserveDevices_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-preservedevices""", alias="PreserveDevices")
    Mtime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-mtime""", alias="Mtime")
    TaskQueueing_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-taskqueueing""", alias="TaskQueueing")
    TransferMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-transfermode""", alias="TransferMode")
    LogLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-loglevel""", alias="LogLevel")
    ObjectTags_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-objecttags""", alias="ObjectTags")
    Uid_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-uid""", alias="Uid")
    BytesPerSecond_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-bytespersecond""", alias="BytesPerSecond")
    PosixPermissions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-posixpermissions""", alias="PosixPermissions")
    PreserveDeletedFiles_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-preservedeletedfiles""", alias="PreserveDeletedFiles")
    SecurityDescriptorCopyFlags_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-securitydescriptorcopyflags""", alias="SecurityDescriptorCopyFlags")
    


    @property
    def tropo_type(self) -> troposphere.datasync.Options:
        from troposphere.datasync import Options as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Overrides(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-overrides.html
    Properties:
        - Name: Verified
        - Name: Skipped
        - Name: Transferred
        - Name: Deleted
    
    """
    
    Verified_: Optional['Verified'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-overrides.html#cfn-datasync-task-overrides-verified""", alias="Verified")
    Skipped_: Optional['Skipped'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-overrides.html#cfn-datasync-task-overrides-skipped""", alias="Skipped")
    Transferred_: Optional['Transferred'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-overrides.html#cfn-datasync-task-overrides-transferred""", alias="Transferred")
    Deleted_: Optional['Deleted'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-overrides.html#cfn-datasync-task-overrides-deleted""", alias="Deleted")
    


    @property
    def tropo_type(self) -> troposphere.datasync.Overrides:
        from troposphere.datasync import Overrides as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-s3.html
    Properties:
        - Name: Subdirectory
        - Name: S3BucketArn
        - Name: BucketAccessRoleArn
    
    """
    
    Subdirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-s3.html#cfn-datasync-task-s3-subdirectory""", alias="Subdirectory")
    S3BucketArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-s3.html#cfn-datasync-task-s3-s3bucketarn""", alias="S3BucketArn")
    BucketAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-s3.html#cfn-datasync-task-s3-bucketaccessrolearn""", alias="BucketAccessRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.datasync.S3:
        from troposphere.datasync import S3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Skipped(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-skipped.html
    Properties:
        - Name: ReportLevel
    
    """
    
    ReportLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-skipped.html#cfn-datasync-task-skipped-reportlevel""", alias="ReportLevel")
    


    @property
    def tropo_type(self) -> troposphere.datasync.Skipped:
        from troposphere.datasync import Skipped as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TaskReportConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfig.html
    Properties:
        - Name: Destination
        - Name: ReportLevel
        - Name: ObjectVersionIds
        - Name: Overrides
        - Name: OutputType
    
    """
    
    Destination_: 'Destination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfig.html#cfn-datasync-task-taskreportconfig-destination""", alias="Destination")
    ReportLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfig.html#cfn-datasync-task-taskreportconfig-reportlevel""", alias="ReportLevel")
    ObjectVersionIds_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfig.html#cfn-datasync-task-taskreportconfig-objectversionids""", alias="ObjectVersionIds")
    Overrides_: Optional['Overrides'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfig.html#cfn-datasync-task-taskreportconfig-overrides""", alias="Overrides")
    OutputType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskreportconfig.html#cfn-datasync-task-taskreportconfig-outputtype""", alias="OutputType")
    


    @property
    def tropo_type(self) -> troposphere.datasync.TaskReportConfig:
        from troposphere.datasync import TaskReportConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TaskSchedule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskschedule.html
    Properties:
        - Name: ScheduleExpression
    
    """
    
    ScheduleExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskschedule.html#cfn-datasync-task-taskschedule-scheduleexpression""", alias="ScheduleExpression")
    


    @property
    def tropo_type(self) -> troposphere.datasync.TaskSchedule:
        from troposphere.datasync import TaskSchedule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Transferred(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-transferred.html
    Properties:
        - Name: ReportLevel
    
    """
    
    ReportLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-transferred.html#cfn-datasync-task-transferred-reportlevel""", alias="ReportLevel")
    


    @property
    def tropo_type(self) -> troposphere.datasync.Transferred:
        from troposphere.datasync import Transferred as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Verified(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-verified.html
    Properties:
        - Name: ReportLevel
    
    """
    
    ReportLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-verified.html#cfn-datasync-task-verified-reportlevel""", alias="ReportLevel")
    


    @property
    def tropo_type(self) -> troposphere.datasync.Verified:
        from troposphere.datasync import Verified as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Agent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html
    Properties:
        - Name: SubnetArns
        - Name: AgentName
        - Name: VpcEndpointId
        - Name: ActivationKey
        - Name: SecurityGroupArns
        - Name: Tags
    Attributes:
        - Name: AgentArn
        - Name: EndpointType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SubnetArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-subnetarns""", alias="SubnetArns")
    AgentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-agentname""", alias="AgentName")
    VpcEndpointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-vpcendpointid""", alias="VpcEndpointId")
    ActivationKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-activationkey""", alias="ActivationKey")
    SecurityGroupArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-securitygrouparns""", alias="SecurityGroupArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.datasync.Agent:
        from troposphere.datasync import Agent as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import Agent as TropoT
        return resource_to_troposphere(self, TropoT)


class LocationAzureBlob(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html
    Properties:
        - Name: AzureAccessTier
        - Name: Subdirectory
        - Name: AzureBlobSasConfiguration
        - Name: AzureBlobType
        - Name: AzureBlobContainerUrl
        - Name: AgentArns
        - Name: Tags
        - Name: AzureBlobAuthenticationType
    Attributes:
        - Name: LocationUri
        - Name: LocationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AzureAccessTier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-azureaccesstier""", alias="AzureAccessTier")
    Subdirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-subdirectory""", alias="Subdirectory")
    AzureBlobSasConfiguration_: Optional['AzureBlobSasConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-azureblobsasconfiguration""", alias="AzureBlobSasConfiguration")
    AzureBlobType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-azureblobtype""", alias="AzureBlobType")
    AzureBlobContainerUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-azureblobcontainerurl""", alias="AzureBlobContainerUrl")
    AgentArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-agentarns""", alias="AgentArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-tags""", alias="Tags")
    AzureBlobAuthenticationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationazureblob.html#cfn-datasync-locationazureblob-azureblobauthenticationtype""", alias="AzureBlobAuthenticationType")
    

    @property
    def tropo_type(self) -> troposphere.datasync.LocationAzureBlob:
        from troposphere.datasync import LocationAzureBlob as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import LocationAzureBlob as TropoT
        return resource_to_troposphere(self, TropoT)


class LocationEFS(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html
    Properties:
        - Name: EfsFilesystemArn
        - Name: Ec2Config
        - Name: AccessPointArn
        - Name: Subdirectory
        - Name: InTransitEncryption
        - Name: FileSystemAccessRoleArn
        - Name: Tags
    Attributes:
        - Name: LocationUri
        - Name: LocationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EfsFilesystemArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-efsfilesystemarn""", alias="EfsFilesystemArn")
    Ec2Config_: 'Ec2Config' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-ec2config""", alias="Ec2Config")
    AccessPointArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-accesspointarn""", alias="AccessPointArn")
    Subdirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-subdirectory""", alias="Subdirectory")
    InTransitEncryption_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-intransitencryption""", alias="InTransitEncryption")
    FileSystemAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-filesystemaccessrolearn""", alias="FileSystemAccessRoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.datasync.LocationEFS:
        from troposphere.datasync import LocationEFS as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import LocationEFS as TropoT
        return resource_to_troposphere(self, TropoT)


class LocationFSxLustre(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html
    Properties:
        - Name: Subdirectory
        - Name: FsxFilesystemArn
        - Name: SecurityGroupArns
        - Name: Tags
    Attributes:
        - Name: LocationUri
        - Name: LocationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Subdirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html#cfn-datasync-locationfsxlustre-subdirectory""", alias="Subdirectory")
    FsxFilesystemArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html#cfn-datasync-locationfsxlustre-fsxfilesystemarn""", alias="FsxFilesystemArn")
    SecurityGroupArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html#cfn-datasync-locationfsxlustre-securitygrouparns""", alias="SecurityGroupArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html#cfn-datasync-locationfsxlustre-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.datasync.LocationFSxLustre:
        from troposphere.datasync import LocationFSxLustre as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import LocationFSxLustre as TropoT
        return resource_to_troposphere(self, TropoT)


class LocationFSxONTAP(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html
    Properties:
        - Name: StorageVirtualMachineArn
        - Name: Subdirectory
        - Name: Protocol
        - Name: SecurityGroupArns
        - Name: Tags
    Attributes:
        - Name: LocationUri
        - Name: FsxFilesystemArn
        - Name: LocationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StorageVirtualMachineArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html#cfn-datasync-locationfsxontap-storagevirtualmachinearn""", alias="StorageVirtualMachineArn")
    Subdirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html#cfn-datasync-locationfsxontap-subdirectory""", alias="Subdirectory")
    Protocol_: Optional['Protocol'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html#cfn-datasync-locationfsxontap-protocol""", alias="Protocol")
    SecurityGroupArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html#cfn-datasync-locationfsxontap-securitygrouparns""", alias="SecurityGroupArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html#cfn-datasync-locationfsxontap-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.datasync.LocationFSxONTAP:
        from troposphere.datasync import LocationFSxONTAP as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import LocationFSxONTAP as TropoT
        return resource_to_troposphere(self, TropoT)


class LocationFSxOpenZFS(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html
    Properties:
        - Name: Subdirectory
        - Name: FsxFilesystemArn
        - Name: Protocol
        - Name: SecurityGroupArns
        - Name: Tags
    Attributes:
        - Name: LocationUri
        - Name: LocationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Subdirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html#cfn-datasync-locationfsxopenzfs-subdirectory""", alias="Subdirectory")
    FsxFilesystemArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html#cfn-datasync-locationfsxopenzfs-fsxfilesystemarn""", alias="FsxFilesystemArn")
    Protocol_: 'Protocol' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html#cfn-datasync-locationfsxopenzfs-protocol""", alias="Protocol")
    SecurityGroupArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html#cfn-datasync-locationfsxopenzfs-securitygrouparns""", alias="SecurityGroupArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxopenzfs.html#cfn-datasync-locationfsxopenzfs-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.datasync.LocationFSxOpenZFS:
        from troposphere.datasync import LocationFSxOpenZFS as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import LocationFSxOpenZFS as TropoT
        return resource_to_troposphere(self, TropoT)


class LocationFSxWindows(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html
    Properties:
        - Name: User
        - Name: Subdirectory
        - Name: FsxFilesystemArn
        - Name: Domain
        - Name: SecurityGroupArns
        - Name: Tags
        - Name: Password
    Attributes:
        - Name: LocationUri
        - Name: LocationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    User_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-user""", alias="User")
    Subdirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-subdirectory""", alias="Subdirectory")
    FsxFilesystemArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-fsxfilesystemarn""", alias="FsxFilesystemArn")
    Domain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-domain""", alias="Domain")
    SecurityGroupArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-securitygrouparns""", alias="SecurityGroupArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-tags""", alias="Tags")
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-password""", alias="Password")
    

    @property
    def tropo_type(self) -> troposphere.datasync.LocationFSxWindows:
        from troposphere.datasync import LocationFSxWindows as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import LocationFSxWindows as TropoT
        return resource_to_troposphere(self, TropoT)


class LocationHDFS(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html
    Properties:
        - Name: KmsKeyProviderUri
        - Name: QopConfiguration
        - Name: KerberosPrincipal
        - Name: SimpleUser
        - Name: ReplicationFactor
        - Name: KerberosKeytab
        - Name: NameNodes
        - Name: Subdirectory
        - Name: KerberosKrb5Conf
        - Name: BlockSize
        - Name: Tags
        - Name: AgentArns
        - Name: AuthenticationType
    Attributes:
        - Name: LocationUri
        - Name: LocationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KmsKeyProviderUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-kmskeyprovideruri""", alias="KmsKeyProviderUri")
    QopConfiguration_: Optional['QopConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-qopconfiguration""", alias="QopConfiguration")
    KerberosPrincipal_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-kerberosprincipal""", alias="KerberosPrincipal")
    SimpleUser_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-simpleuser""", alias="SimpleUser")
    ReplicationFactor_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-replicationfactor""", alias="ReplicationFactor")
    KerberosKeytab_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-kerberoskeytab""", alias="KerberosKeytab")
    NameNodes_: List['NameNode'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-namenodes""", alias="NameNodes")
    Subdirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-subdirectory""", alias="Subdirectory")
    KerberosKrb5Conf_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-kerberoskrb5conf""", alias="KerberosKrb5Conf")
    BlockSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-blocksize""", alias="BlockSize")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-tags""", alias="Tags")
    AgentArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-agentarns""", alias="AgentArns")
    AuthenticationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html#cfn-datasync-locationhdfs-authenticationtype""", alias="AuthenticationType")
    

    @property
    def tropo_type(self) -> troposphere.datasync.LocationHDFS:
        from troposphere.datasync import LocationHDFS as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import LocationHDFS as TropoT
        return resource_to_troposphere(self, TropoT)


class LocationNFS(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html
    Properties:
        - Name: Subdirectory
        - Name: ServerHostname
        - Name: MountOptions
        - Name: OnPremConfig
        - Name: Tags
    Attributes:
        - Name: LocationUri
        - Name: LocationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Subdirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-subdirectory""", alias="Subdirectory")
    ServerHostname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-serverhostname""", alias="ServerHostname")
    MountOptions_: Optional['MountOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-mountoptions""", alias="MountOptions")
    OnPremConfig_: 'OnPremConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-onpremconfig""", alias="OnPremConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.datasync.LocationNFS:
        from troposphere.datasync import LocationNFS as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import LocationNFS as TropoT
        return resource_to_troposphere(self, TropoT)


class LocationObjectStorage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html
    Properties:
        - Name: ServerCertificate
        - Name: SecretKey
        - Name: BucketName
        - Name: Subdirectory
        - Name: ServerHostname
        - Name: AccessKey
        - Name: ServerProtocol
        - Name: AgentArns
        - Name: ServerPort
        - Name: Tags
    Attributes:
        - Name: LocationUri
        - Name: LocationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ServerCertificate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-servercertificate""", alias="ServerCertificate")
    SecretKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-secretkey""", alias="SecretKey")
    BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-bucketname""", alias="BucketName")
    Subdirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-subdirectory""", alias="Subdirectory")
    ServerHostname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverhostname""", alias="ServerHostname")
    AccessKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-accesskey""", alias="AccessKey")
    ServerProtocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverprotocol""", alias="ServerProtocol")
    AgentArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-agentarns""", alias="AgentArns")
    ServerPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverport""", alias="ServerPort")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.datasync.LocationObjectStorage:
        from troposphere.datasync import LocationObjectStorage as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import LocationObjectStorage as TropoT
        return resource_to_troposphere(self, TropoT)


class LocationS3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html
    Properties:
        - Name: S3StorageClass
        - Name: S3Config
        - Name: Subdirectory
        - Name: S3BucketArn
        - Name: Tags
    Attributes:
        - Name: LocationUri
        - Name: LocationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    S3StorageClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3storageclass""", alias="S3StorageClass")
    S3Config_: 'S3Config' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3config""", alias="S3Config")
    Subdirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-subdirectory""", alias="Subdirectory")
    S3BucketArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3bucketarn""", alias="S3BucketArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.datasync.LocationS3:
        from troposphere.datasync import LocationS3 as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import LocationS3 as TropoT
        return resource_to_troposphere(self, TropoT)


class LocationSMB(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html
    Properties:
        - Name: User
        - Name: Subdirectory
        - Name: ServerHostname
        - Name: Domain
        - Name: MountOptions
        - Name: AgentArns
        - Name: Tags
        - Name: Password
    Attributes:
        - Name: LocationUri
        - Name: LocationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    User_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-user""", alias="User")
    Subdirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-subdirectory""", alias="Subdirectory")
    ServerHostname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-serverhostname""", alias="ServerHostname")
    Domain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-domain""", alias="Domain")
    MountOptions_: Optional['MountOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-mountoptions""", alias="MountOptions")
    AgentArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-agentarns""", alias="AgentArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-tags""", alias="Tags")
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-password""", alias="Password")
    

    @property
    def tropo_type(self) -> troposphere.datasync.LocationSMB:
        from troposphere.datasync import LocationSMB as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import LocationSMB as TropoT
        return resource_to_troposphere(self, TropoT)


class StorageSystem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html
    Properties:
        - Name: ServerCredentials
        - Name: ServerConfiguration
        - Name: CloudWatchLogGroupArn
        - Name: SystemType
        - Name: AgentArns
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ConnectivityStatus
        - Name: StorageSystemArn
        - Name: SecretsManagerArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ServerCredentials_: Optional['ServerCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-servercredentials""", alias="ServerCredentials")
    ServerConfiguration_: 'ServerConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-serverconfiguration""", alias="ServerConfiguration")
    CloudWatchLogGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-cloudwatchloggrouparn""", alias="CloudWatchLogGroupArn")
    SystemType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-systemtype""", alias="SystemType")
    AgentArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-agentarns""", alias="AgentArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-storagesystem.html#cfn-datasync-storagesystem-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.datasync.StorageSystem:
        from troposphere.datasync import StorageSystem as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import StorageSystem as TropoT
        return resource_to_troposphere(self, TropoT)


class Task(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html
    Properties:
        - Name: Includes
        - Name: DestinationLocationArn
        - Name: Options
        - Name: Schedule
        - Name: CloudWatchLogGroupArn
        - Name: SourceLocationArn
        - Name: TaskReportConfig
        - Name: Excludes
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: SourceNetworkInterfaceArns
        - Name: DestinationNetworkInterfaceArns
        - Name: TaskArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Includes_: Optional[List['FilterRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-includes""", alias="Includes")
    DestinationLocationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-destinationlocationarn""", alias="DestinationLocationArn")
    Options_: Optional['Options'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-options""", alias="Options")
    Schedule_: Optional['TaskSchedule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-schedule""", alias="Schedule")
    CloudWatchLogGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-cloudwatchloggrouparn""", alias="CloudWatchLogGroupArn")
    SourceLocationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-sourcelocationarn""", alias="SourceLocationArn")
    TaskReportConfig_: Optional['TaskReportConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-taskreportconfig""", alias="TaskReportConfig")
    Excludes_: Optional[List['FilterRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-excludes""", alias="Excludes")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.datasync.Task:
        from troposphere.datasync import Task as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datasync import Task as TropoT
        return resource_to_troposphere(self, TropoT)

