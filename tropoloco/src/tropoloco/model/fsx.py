from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AutoExportPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-datarepositoryassociation-autoexportpolicy.html
    Properties:
        - Name: Events
    
    """
    
    Events_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-datarepositoryassociation-autoexportpolicy.html#cfn-fsx-datarepositoryassociation-autoexportpolicy-events""", alias="Events")
    


    @property
    def tropo_type(self) -> troposphere.fsx.AutoExportPolicy:
        from troposphere.fsx import AutoExportPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoImportPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-datarepositoryassociation-autoimportpolicy.html
    Properties:
        - Name: Events
    
    """
    
    Events_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-datarepositoryassociation-autoimportpolicy.html#cfn-fsx-datarepositoryassociation-autoimportpolicy-events""", alias="Events")
    


    @property
    def tropo_type(self) -> troposphere.fsx.AutoImportPolicy:
        from troposphere.fsx import AutoImportPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-datarepositoryassociation-s3.html
    Properties:
        - Name: AutoImportPolicy
        - Name: AutoExportPolicy
    
    """
    
    AutoImportPolicy_: Optional['AutoImportPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-datarepositoryassociation-s3.html#cfn-fsx-datarepositoryassociation-s3-autoimportpolicy""", alias="AutoImportPolicy")
    AutoExportPolicy_: Optional['AutoExportPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-datarepositoryassociation-s3.html#cfn-fsx-datarepositoryassociation-s3-autoexportpolicy""", alias="AutoExportPolicy")
    


    @property
    def tropo_type(self) -> troposphere.fsx.S3:
        from troposphere.fsx import S3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuditLogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-auditlogconfiguration.html
    Properties:
        - Name: FileAccessAuditLogLevel
        - Name: FileShareAccessAuditLogLevel
        - Name: AuditLogDestination
    
    """
    
    FileAccessAuditLogLevel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-auditlogconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-auditlogconfiguration-fileaccessauditloglevel""", alias="FileAccessAuditLogLevel")
    FileShareAccessAuditLogLevel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-auditlogconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-auditlogconfiguration-fileshareaccessauditloglevel""", alias="FileShareAccessAuditLogLevel")
    AuditLogDestination_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-auditlogconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-auditlogconfiguration-auditlogdestination""", alias="AuditLogDestination")
    


    @property
    def tropo_type(self) -> troposphere.fsx.AuditLogConfiguration:
        from troposphere.fsx import AuditLogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClientConfigurations(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations.html
    Properties:
        - Name: Options
        - Name: Clients
    
    """
    
    Options_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations-options""", alias="Options")
    Clients_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations-clients""", alias="Clients")
    


    @property
    def tropo_type(self) -> troposphere.fsx.ClientConfigurations:
        from troposphere.fsx import ClientConfigurations as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DiskIopsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-diskiopsconfiguration.html
    Properties:
        - Name: Mode
        - Name: Iops
    
    """
    
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-diskiopsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-diskiopsconfiguration-mode""", alias="Mode")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-diskiopsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-diskiopsconfiguration-iops""", alias="Iops")
    


    @property
    def tropo_type(self) -> troposphere.fsx.DiskIopsConfiguration:
        from troposphere.fsx import DiskIopsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LustreConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html
    Properties:
        - Name: DataCompressionType
        - Name: DriveCacheType
        - Name: ImportPath
        - Name: WeeklyMaintenanceStartTime
        - Name: AutoImportPolicy
        - Name: ImportedFileChunkSize
        - Name: DeploymentType
        - Name: DailyAutomaticBackupStartTime
        - Name: CopyTagsToBackups
        - Name: ExportPath
        - Name: PerUnitStorageThroughput
        - Name: AutomaticBackupRetentionDays
    
    """
    
    DataCompressionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-datacompressiontype""", alias="DataCompressionType")
    DriveCacheType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-drivecachetype""", alias="DriveCacheType")
    ImportPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-importpath""", alias="ImportPath")
    WeeklyMaintenanceStartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-weeklymaintenancestarttime""", alias="WeeklyMaintenanceStartTime")
    AutoImportPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-autoimportpolicy""", alias="AutoImportPolicy")
    ImportedFileChunkSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-importedfilechunksize""", alias="ImportedFileChunkSize")
    DeploymentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-deploymenttype""", alias="DeploymentType")
    DailyAutomaticBackupStartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-dailyautomaticbackupstarttime""", alias="DailyAutomaticBackupStartTime")
    CopyTagsToBackups_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-copytagstobackups""", alias="CopyTagsToBackups")
    ExportPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-exportpath""", alias="ExportPath")
    PerUnitStorageThroughput_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-perunitstoragethroughput""", alias="PerUnitStorageThroughput")
    AutomaticBackupRetentionDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html#cfn-fsx-filesystem-lustreconfiguration-automaticbackupretentiondays""", alias="AutomaticBackupRetentionDays")
    


    @property
    def tropo_type(self) -> troposphere.fsx.LustreConfiguration:
        from troposphere.fsx import LustreConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NfsExports(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports.html
    Properties:
        - Name: ClientConfigurations
    
    """
    
    ClientConfigurations_: Optional[List['ClientConfigurations']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations""", alias="ClientConfigurations")
    


    @property
    def tropo_type(self) -> troposphere.fsx.NfsExports:
        from troposphere.fsx import NfsExports as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OntapConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html
    Properties:
        - Name: HAPairs
        - Name: FsxAdminPassword
        - Name: ThroughputCapacityPerHAPair
        - Name: RouteTableIds
        - Name: WeeklyMaintenanceStartTime
        - Name: DiskIopsConfiguration
        - Name: DeploymentType
        - Name: DailyAutomaticBackupStartTime
        - Name: ThroughputCapacity
        - Name: AutomaticBackupRetentionDays
        - Name: EndpointIpAddressRange
        - Name: PreferredSubnetId
    
    """
    
    HAPairs_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-hapairs""", alias="HAPairs")
    FsxAdminPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-fsxadminpassword""", alias="FsxAdminPassword")
    ThroughputCapacityPerHAPair_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-throughputcapacityperhapair""", alias="ThroughputCapacityPerHAPair")
    RouteTableIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-routetableids""", alias="RouteTableIds")
    WeeklyMaintenanceStartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-weeklymaintenancestarttime""", alias="WeeklyMaintenanceStartTime")
    DiskIopsConfiguration_: Optional['DiskIopsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-diskiopsconfiguration""", alias="DiskIopsConfiguration")
    DeploymentType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-deploymenttype""", alias="DeploymentType")
    DailyAutomaticBackupStartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-dailyautomaticbackupstarttime""", alias="DailyAutomaticBackupStartTime")
    ThroughputCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-throughputcapacity""", alias="ThroughputCapacity")
    AutomaticBackupRetentionDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-automaticbackupretentiondays""", alias="AutomaticBackupRetentionDays")
    EndpointIpAddressRange_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-endpointipaddressrange""", alias="EndpointIpAddressRange")
    PreferredSubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html#cfn-fsx-filesystem-ontapconfiguration-preferredsubnetid""", alias="PreferredSubnetId")
    


    @property
    def tropo_type(self) -> troposphere.fsx.OntapConfiguration:
        from troposphere.fsx import OntapConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OpenZFSConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html
    Properties:
        - Name: Options
        - Name: CopyTagsToVolumes
        - Name: DeploymentType
        - Name: ThroughputCapacity
        - Name: RootVolumeConfiguration
        - Name: EndpointIpAddressRange
        - Name: RouteTableIds
        - Name: WeeklyMaintenanceStartTime
        - Name: DiskIopsConfiguration
        - Name: DailyAutomaticBackupStartTime
        - Name: CopyTagsToBackups
        - Name: AutomaticBackupRetentionDays
        - Name: PreferredSubnetId
    
    """
    
    Options_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-options""", alias="Options")
    CopyTagsToVolumes_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-copytagstovolumes""", alias="CopyTagsToVolumes")
    DeploymentType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-deploymenttype""", alias="DeploymentType")
    ThroughputCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-throughputcapacity""", alias="ThroughputCapacity")
    RootVolumeConfiguration_: Optional['RootVolumeConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration""", alias="RootVolumeConfiguration")
    EndpointIpAddressRange_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-endpointipaddressrange""", alias="EndpointIpAddressRange")
    RouteTableIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-routetableids""", alias="RouteTableIds")
    WeeklyMaintenanceStartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-weeklymaintenancestarttime""", alias="WeeklyMaintenanceStartTime")
    DiskIopsConfiguration_: Optional['DiskIopsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-diskiopsconfiguration""", alias="DiskIopsConfiguration")
    DailyAutomaticBackupStartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-dailyautomaticbackupstarttime""", alias="DailyAutomaticBackupStartTime")
    CopyTagsToBackups_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-copytagstobackups""", alias="CopyTagsToBackups")
    AutomaticBackupRetentionDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-automaticbackupretentiondays""", alias="AutomaticBackupRetentionDays")
    PreferredSubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-preferredsubnetid""", alias="PreferredSubnetId")
    


    @property
    def tropo_type(self) -> troposphere.fsx.OpenZFSConfiguration:
        from troposphere.fsx import OpenZFSConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RootVolumeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html
    Properties:
        - Name: ReadOnly
        - Name: DataCompressionType
        - Name: NfsExports
        - Name: CopyTagsToSnapshots
        - Name: RecordSizeKiB
        - Name: UserAndGroupQuotas
    
    """
    
    ReadOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-readonly""", alias="ReadOnly")
    DataCompressionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-datacompressiontype""", alias="DataCompressionType")
    NfsExports_: Optional[List['NfsExports']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports""", alias="NfsExports")
    CopyTagsToSnapshots_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-copytagstosnapshots""", alias="CopyTagsToSnapshots")
    RecordSizeKiB_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-recordsizekib""", alias="RecordSizeKiB")
    UserAndGroupQuotas_: Optional[List['UserAndGroupQuotas']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas""", alias="UserAndGroupQuotas")
    


    @property
    def tropo_type(self) -> troposphere.fsx.RootVolumeConfiguration:
        from troposphere.fsx import RootVolumeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SelfManagedActiveDirectoryConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html
    Properties:
        - Name: FileSystemAdministratorsGroup
        - Name: UserName
        - Name: DomainName
        - Name: OrganizationalUnitDistinguishedName
        - Name: DnsIps
        - Name: Password
    
    """
    
    FileSystemAdministratorsGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-filesystemadministratorsgroup""", alias="FileSystemAdministratorsGroup")
    UserName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-username""", alias="UserName")
    DomainName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-domainname""", alias="DomainName")
    OrganizationalUnitDistinguishedName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-organizationalunitdistinguishedname""", alias="OrganizationalUnitDistinguishedName")
    DnsIps_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-dnsips""", alias="DnsIps")
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.fsx.SelfManagedActiveDirectoryConfiguration:
        from troposphere.fsx import SelfManagedActiveDirectoryConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserAndGroupQuotas(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas.html
    Properties:
        - Name: Type
        - Name: Id
        - Name: StorageCapacityQuotaGiB
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas-type""", alias="Type")
    Id_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas-id""", alias="Id")
    StorageCapacityQuotaGiB_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas.html#cfn-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas-storagecapacityquotagib""", alias="StorageCapacityQuotaGiB")
    


    @property
    def tropo_type(self) -> troposphere.fsx.UserAndGroupQuotas:
        from troposphere.fsx import UserAndGroupQuotas as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WindowsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html
    Properties:
        - Name: SelfManagedActiveDirectoryConfiguration
        - Name: AuditLogConfiguration
        - Name: WeeklyMaintenanceStartTime
        - Name: ActiveDirectoryId
        - Name: DiskIopsConfiguration
        - Name: DeploymentType
        - Name: Aliases
        - Name: ThroughputCapacity
        - Name: CopyTagsToBackups
        - Name: DailyAutomaticBackupStartTime
        - Name: AutomaticBackupRetentionDays
        - Name: PreferredSubnetId
    
    """
    
    SelfManagedActiveDirectoryConfiguration_: Optional['SelfManagedActiveDirectoryConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration""", alias="SelfManagedActiveDirectoryConfiguration")
    AuditLogConfiguration_: Optional['AuditLogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-auditlogconfiguration""", alias="AuditLogConfiguration")
    WeeklyMaintenanceStartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-weeklymaintenancestarttime""", alias="WeeklyMaintenanceStartTime")
    ActiveDirectoryId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-activedirectoryid""", alias="ActiveDirectoryId")
    DiskIopsConfiguration_: Optional['DiskIopsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-diskiopsconfiguration""", alias="DiskIopsConfiguration")
    DeploymentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-deploymenttype""", alias="DeploymentType")
    Aliases_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-aliases""", alias="Aliases")
    ThroughputCapacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-throughputcapacity""", alias="ThroughputCapacity")
    CopyTagsToBackups_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-copytagstobackups""", alias="CopyTagsToBackups")
    DailyAutomaticBackupStartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-dailyautomaticbackupstarttime""", alias="DailyAutomaticBackupStartTime")
    AutomaticBackupRetentionDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-automaticbackupretentiondays""", alias="AutomaticBackupRetentionDays")
    PreferredSubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html#cfn-fsx-filesystem-windowsconfiguration-preferredsubnetid""", alias="PreferredSubnetId")
    


    @property
    def tropo_type(self) -> troposphere.fsx.WindowsConfiguration:
        from troposphere.fsx import WindowsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ActiveDirectoryConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration.html
    Properties:
        - Name: SelfManagedActiveDirectoryConfiguration
        - Name: NetBiosName
    
    """
    
    SelfManagedActiveDirectoryConfiguration_: Optional['SelfManagedActiveDirectoryConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration""", alias="SelfManagedActiveDirectoryConfiguration")
    NetBiosName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-netbiosname""", alias="NetBiosName")
    


    @property
    def tropo_type(self) -> troposphere.fsx.ActiveDirectoryConfiguration:
        from troposphere.fsx import ActiveDirectoryConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SelfManagedActiveDirectoryConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html
    Properties:
        - Name: FileSystemAdministratorsGroup
        - Name: UserName
        - Name: DomainName
        - Name: OrganizationalUnitDistinguishedName
        - Name: DnsIps
        - Name: Password
    
    """
    
    FileSystemAdministratorsGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration-filesystemadministratorsgroup""", alias="FileSystemAdministratorsGroup")
    UserName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration-username""", alias="UserName")
    DomainName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration-domainname""", alias="DomainName")
    OrganizationalUnitDistinguishedName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration-organizationalunitdistinguishedname""", alias="OrganizationalUnitDistinguishedName")
    DnsIps_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration-dnsips""", alias="DnsIps")
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.fsx.SelfManagedActiveDirectoryConfiguration:
        from troposphere.fsx import SelfManagedActiveDirectoryConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AggregateConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-aggregateconfiguration.html
    Properties:
        - Name: Aggregates
        - Name: ConstituentsPerAggregate
    
    """
    
    Aggregates_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-aggregateconfiguration.html#cfn-fsx-volume-ontapconfiguration-aggregateconfiguration-aggregates""", alias="Aggregates")
    ConstituentsPerAggregate_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-aggregateconfiguration.html#cfn-fsx-volume-ontapconfiguration-aggregateconfiguration-constituentsperaggregate""", alias="ConstituentsPerAggregate")
    


    @property
    def tropo_type(self) -> troposphere.fsx.AggregateConfiguration:
        from troposphere.fsx import AggregateConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutocommitPeriod(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-snaplockconfiguration-autocommitperiod.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-snaplockconfiguration-autocommitperiod.html#cfn-fsx-volume-ontapconfiguration-snaplockconfiguration-autocommitperiod-type""", alias="Type")
    Value_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-snaplockconfiguration-autocommitperiod.html#cfn-fsx-volume-ontapconfiguration-snaplockconfiguration-autocommitperiod-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.fsx.AutocommitPeriod:
        from troposphere.fsx import AutocommitPeriod as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClientConfigurations(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-nfsexports-clientconfigurations.html
    Properties:
        - Name: Options
        - Name: Clients
    
    """
    
    Options_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-nfsexports-clientconfigurations.html#cfn-fsx-volume-openzfsconfiguration-nfsexports-clientconfigurations-options""", alias="Options")
    Clients_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-nfsexports-clientconfigurations.html#cfn-fsx-volume-openzfsconfiguration-nfsexports-clientconfigurations-clients""", alias="Clients")
    


    @property
    def tropo_type(self) -> troposphere.fsx.ClientConfigurations:
        from troposphere.fsx import ClientConfigurations as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NfsExports(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-nfsexports.html
    Properties:
        - Name: ClientConfigurations
    
    """
    
    ClientConfigurations_: List['ClientConfigurations'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-nfsexports.html#cfn-fsx-volume-openzfsconfiguration-nfsexports-clientconfigurations""", alias="ClientConfigurations")
    


    @property
    def tropo_type(self) -> troposphere.fsx.NfsExports:
        from troposphere.fsx import NfsExports as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OntapConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html
    Properties:
        - Name: JunctionPath
        - Name: StorageVirtualMachineId
        - Name: TieringPolicy
        - Name: SizeInMegabytes
        - Name: VolumeStyle
        - Name: SizeInBytes
        - Name: SecurityStyle
        - Name: SnaplockConfiguration
        - Name: AggregateConfiguration
        - Name: SnapshotPolicy
        - Name: StorageEfficiencyEnabled
        - Name: CopyTagsToBackups
        - Name: OntapVolumeType
    
    """
    
    JunctionPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-junctionpath""", alias="JunctionPath")
    StorageVirtualMachineId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-storagevirtualmachineid""", alias="StorageVirtualMachineId")
    TieringPolicy_: Optional['TieringPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-tieringpolicy""", alias="TieringPolicy")
    SizeInMegabytes_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-sizeinmegabytes""", alias="SizeInMegabytes")
    VolumeStyle_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-volumestyle""", alias="VolumeStyle")
    SizeInBytes_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-sizeinbytes""", alias="SizeInBytes")
    SecurityStyle_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-securitystyle""", alias="SecurityStyle")
    SnaplockConfiguration_: Optional['SnaplockConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-snaplockconfiguration""", alias="SnaplockConfiguration")
    AggregateConfiguration_: Optional['AggregateConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-aggregateconfiguration""", alias="AggregateConfiguration")
    SnapshotPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-snapshotpolicy""", alias="SnapshotPolicy")
    StorageEfficiencyEnabled_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-storageefficiencyenabled""", alias="StorageEfficiencyEnabled")
    CopyTagsToBackups_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-copytagstobackups""", alias="CopyTagsToBackups")
    OntapVolumeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html#cfn-fsx-volume-ontapconfiguration-ontapvolumetype""", alias="OntapVolumeType")
    


    @property
    def tropo_type(self) -> troposphere.fsx.OntapConfiguration:
        from troposphere.fsx import OntapConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OpenZFSConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html
    Properties:
        - Name: ReadOnly
        - Name: Options
        - Name: DataCompressionType
        - Name: NfsExports
        - Name: StorageCapacityQuotaGiB
        - Name: CopyTagsToSnapshots
        - Name: ParentVolumeId
        - Name: StorageCapacityReservationGiB
        - Name: RecordSizeKiB
        - Name: OriginSnapshot
        - Name: UserAndGroupQuotas
    
    """
    
    ReadOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-readonly""", alias="ReadOnly")
    Options_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-options""", alias="Options")
    DataCompressionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-datacompressiontype""", alias="DataCompressionType")
    NfsExports_: Optional[List['NfsExports']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-nfsexports""", alias="NfsExports")
    StorageCapacityQuotaGiB_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-storagecapacityquotagib""", alias="StorageCapacityQuotaGiB")
    CopyTagsToSnapshots_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-copytagstosnapshots""", alias="CopyTagsToSnapshots")
    ParentVolumeId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-parentvolumeid""", alias="ParentVolumeId")
    StorageCapacityReservationGiB_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-storagecapacityreservationgib""", alias="StorageCapacityReservationGiB")
    RecordSizeKiB_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-recordsizekib""", alias="RecordSizeKiB")
    OriginSnapshot_: Optional['OriginSnapshot'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-originsnapshot""", alias="OriginSnapshot")
    UserAndGroupQuotas_: Optional[List['UserAndGroupQuotas']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html#cfn-fsx-volume-openzfsconfiguration-userandgroupquotas""", alias="UserAndGroupQuotas")
    


    @property
    def tropo_type(self) -> troposphere.fsx.OpenZFSConfiguration:
        from troposphere.fsx import OpenZFSConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OriginSnapshot(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-originsnapshot.html
    Properties:
        - Name: CopyStrategy
        - Name: SnapshotARN
    
    """
    
    CopyStrategy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-originsnapshot.html#cfn-fsx-volume-openzfsconfiguration-originsnapshot-copystrategy""", alias="CopyStrategy")
    SnapshotARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-originsnapshot.html#cfn-fsx-volume-openzfsconfiguration-originsnapshot-snapshotarn""", alias="SnapshotARN")
    


    @property
    def tropo_type(self) -> troposphere.fsx.OriginSnapshot:
        from troposphere.fsx import OriginSnapshot as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RetentionPeriod(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-retentionperiod.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-retentionperiod.html#cfn-fsx-volume-retentionperiod-type""", alias="Type")
    Value_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-retentionperiod.html#cfn-fsx-volume-retentionperiod-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.fsx.RetentionPeriod:
        from troposphere.fsx import RetentionPeriod as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnaplockConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-snaplockconfiguration.html
    Properties:
        - Name: AuditLogVolume
        - Name: VolumeAppendModeEnabled
        - Name: AutocommitPeriod
        - Name: RetentionPeriod
        - Name: PrivilegedDelete
        - Name: SnaplockType
    
    """
    
    AuditLogVolume_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-snaplockconfiguration.html#cfn-fsx-volume-ontapconfiguration-snaplockconfiguration-auditlogvolume""", alias="AuditLogVolume")
    VolumeAppendModeEnabled_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-snaplockconfiguration.html#cfn-fsx-volume-ontapconfiguration-snaplockconfiguration-volumeappendmodeenabled""", alias="VolumeAppendModeEnabled")
    AutocommitPeriod_: Optional['AutocommitPeriod'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-snaplockconfiguration.html#cfn-fsx-volume-ontapconfiguration-snaplockconfiguration-autocommitperiod""", alias="AutocommitPeriod")
    RetentionPeriod_: Optional['SnaplockRetentionPeriod'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-snaplockconfiguration.html#cfn-fsx-volume-ontapconfiguration-snaplockconfiguration-retentionperiod""", alias="RetentionPeriod")
    PrivilegedDelete_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-snaplockconfiguration.html#cfn-fsx-volume-ontapconfiguration-snaplockconfiguration-privilegeddelete""", alias="PrivilegedDelete")
    SnaplockType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-snaplockconfiguration.html#cfn-fsx-volume-ontapconfiguration-snaplockconfiguration-snaplocktype""", alias="SnaplockType")
    


    @property
    def tropo_type(self) -> troposphere.fsx.SnaplockConfiguration:
        from troposphere.fsx import SnaplockConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnaplockRetentionPeriod(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-snaplockretentionperiod.html
    Properties:
        - Name: DefaultRetention
        - Name: MaximumRetention
        - Name: MinimumRetention
    
    """
    
    DefaultRetention_: 'RetentionPeriod' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-snaplockretentionperiod.html#cfn-fsx-volume-snaplockretentionperiod-defaultretention""", alias="DefaultRetention")
    MaximumRetention_: 'RetentionPeriod' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-snaplockretentionperiod.html#cfn-fsx-volume-snaplockretentionperiod-maximumretention""", alias="MaximumRetention")
    MinimumRetention_: 'RetentionPeriod' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-snaplockretentionperiod.html#cfn-fsx-volume-snaplockretentionperiod-minimumretention""", alias="MinimumRetention")
    


    @property
    def tropo_type(self) -> troposphere.fsx.SnaplockRetentionPeriod:
        from troposphere.fsx import SnaplockRetentionPeriod as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TieringPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-tieringpolicy.html
    Properties:
        - Name: CoolingPeriod
        - Name: Name
    
    """
    
    CoolingPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-tieringpolicy.html#cfn-fsx-volume-ontapconfiguration-tieringpolicy-coolingperiod""", alias="CoolingPeriod")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-tieringpolicy.html#cfn-fsx-volume-ontapconfiguration-tieringpolicy-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.fsx.TieringPolicy:
        from troposphere.fsx import TieringPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserAndGroupQuotas(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-userandgroupquotas.html
    Properties:
        - Name: Type
        - Name: Id
        - Name: StorageCapacityQuotaGiB
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-userandgroupquotas.html#cfn-fsx-volume-openzfsconfiguration-userandgroupquotas-type""", alias="Type")
    Id_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-userandgroupquotas.html#cfn-fsx-volume-openzfsconfiguration-userandgroupquotas-id""", alias="Id")
    StorageCapacityQuotaGiB_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-userandgroupquotas.html#cfn-fsx-volume-openzfsconfiguration-userandgroupquotas-storagecapacityquotagib""", alias="StorageCapacityQuotaGiB")
    


    @property
    def tropo_type(self) -> troposphere.fsx.UserAndGroupQuotas:
        from troposphere.fsx import UserAndGroupQuotas as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class DataRepositoryAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-datarepositoryassociation.html
    Properties:
        - Name: FileSystemPath
        - Name: DataRepositoryPath
        - Name: BatchImportMetaDataOnCreate
        - Name: S3
        - Name: FileSystemId
        - Name: ImportedFileChunkSize
        - Name: Tags
    Attributes:
        - Name: ResourceARN
        - Name: AssociationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FileSystemPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-datarepositoryassociation.html#cfn-fsx-datarepositoryassociation-filesystempath""", alias="FileSystemPath")
    DataRepositoryPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-datarepositoryassociation.html#cfn-fsx-datarepositoryassociation-datarepositorypath""", alias="DataRepositoryPath")
    BatchImportMetaDataOnCreate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-datarepositoryassociation.html#cfn-fsx-datarepositoryassociation-batchimportmetadataoncreate""", alias="BatchImportMetaDataOnCreate")
    S3_: Optional['S3'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-datarepositoryassociation.html#cfn-fsx-datarepositoryassociation-s3""", alias="S3")
    FileSystemId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-datarepositoryassociation.html#cfn-fsx-datarepositoryassociation-filesystemid""", alias="FileSystemId")
    ImportedFileChunkSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-datarepositoryassociation.html#cfn-fsx-datarepositoryassociation-importedfilechunksize""", alias="ImportedFileChunkSize")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-datarepositoryassociation.html#cfn-fsx-datarepositoryassociation-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.fsx.DataRepositoryAssociation:
        from troposphere.fsx import DataRepositoryAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.fsx import DataRepositoryAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class FileSystem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html
    Properties:
        - Name: StorageType
        - Name: KmsKeyId
        - Name: StorageCapacity
        - Name: LustreConfiguration
        - Name: BackupId
        - Name: OntapConfiguration
        - Name: SubnetIds
        - Name: SecurityGroupIds
        - Name: WindowsConfiguration
        - Name: FileSystemTypeVersion
        - Name: OpenZFSConfiguration
        - Name: FileSystemType
        - Name: Tags
    Attributes:
        - Name: ResourceARN
        - Name: RootVolumeId
        - Name: DNSName
        - Name: LustreMountName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StorageType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-storagetype""", alias="StorageType")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-kmskeyid""", alias="KmsKeyId")
    StorageCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-storagecapacity""", alias="StorageCapacity")
    LustreConfiguration_: Optional['LustreConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-lustreconfiguration""", alias="LustreConfiguration")
    BackupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-backupid""", alias="BackupId")
    OntapConfiguration_: Optional['OntapConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-ontapconfiguration""", alias="OntapConfiguration")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-subnetids""", alias="SubnetIds")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-securitygroupids""", alias="SecurityGroupIds")
    WindowsConfiguration_: Optional['WindowsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-windowsconfiguration""", alias="WindowsConfiguration")
    FileSystemTypeVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-filesystemtypeversion""", alias="FileSystemTypeVersion")
    OpenZFSConfiguration_: Optional['OpenZFSConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-openzfsconfiguration""", alias="OpenZFSConfiguration")
    FileSystemType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-filesystemtype""", alias="FileSystemType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html#cfn-fsx-filesystem-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.fsx.FileSystem:
        from troposphere.fsx import FileSystem as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.fsx import FileSystem as TropoT
        return resource_to_troposphere(self, TropoT)


class Snapshot(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-snapshot.html
    Properties:
        - Name: VolumeId
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ResourceARN
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VolumeId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-snapshot.html#cfn-fsx-snapshot-volumeid""", alias="VolumeId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-snapshot.html#cfn-fsx-snapshot-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-snapshot.html#cfn-fsx-snapshot-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.fsx.Snapshot:
        from troposphere.fsx import Snapshot as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.fsx import Snapshot as TropoT
        return resource_to_troposphere(self, TropoT)


class StorageVirtualMachine(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html
    Properties:
        - Name: SvmAdminPassword
        - Name: ActiveDirectoryConfiguration
        - Name: RootVolumeSecurityStyle
        - Name: FileSystemId
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ResourceARN
        - Name: StorageVirtualMachineId
        - Name: UUID
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SvmAdminPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-svmadminpassword""", alias="SvmAdminPassword")
    ActiveDirectoryConfiguration_: Optional['ActiveDirectoryConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-activedirectoryconfiguration""", alias="ActiveDirectoryConfiguration")
    RootVolumeSecurityStyle_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-rootvolumesecuritystyle""", alias="RootVolumeSecurityStyle")
    FileSystemId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-filesystemid""", alias="FileSystemId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html#cfn-fsx-storagevirtualmachine-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.fsx.StorageVirtualMachine:
        from troposphere.fsx import StorageVirtualMachine as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.fsx import StorageVirtualMachine as TropoT
        return resource_to_troposphere(self, TropoT)


class Volume(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html
    Properties:
        - Name: OpenZFSConfiguration
        - Name: VolumeType
        - Name: BackupId
        - Name: OntapConfiguration
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ResourceARN
        - Name: VolumeId
        - Name: UUID
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OpenZFSConfiguration_: Optional['OpenZFSConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-openzfsconfiguration""", alias="OpenZFSConfiguration")
    VolumeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-volumetype""", alias="VolumeType")
    BackupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-backupid""", alias="BackupId")
    OntapConfiguration_: Optional['OntapConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-ontapconfiguration""", alias="OntapConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html#cfn-fsx-volume-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.fsx.Volume:
        from troposphere.fsx import Volume as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.fsx import Volume as TropoT
        return resource_to_troposphere(self, TropoT)

