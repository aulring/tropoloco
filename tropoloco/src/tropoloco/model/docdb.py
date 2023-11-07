from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################




######################################################################
# AWS Resource
######################################################################


class DBCluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html
    Properties:
        - Name: StorageEncrypted
        - Name: RestoreToTime
        - Name: EngineVersion
        - Name: KmsKeyId
        - Name: AvailabilityZones
        - Name: SnapshotIdentifier
        - Name: Port
        - Name: DBClusterIdentifier
        - Name: PreferredMaintenanceWindow
        - Name: DBSubnetGroupName
        - Name: DeletionProtection
        - Name: PreferredBackupWindow
        - Name: UseLatestRestorableTime
        - Name: MasterUserPassword
        - Name: VpcSecurityGroupIds
        - Name: SourceDBClusterIdentifier
        - Name: MasterUsername
        - Name: DBClusterParameterGroupName
        - Name: CopyTagsToSnapshot
        - Name: BackupRetentionPeriod
        - Name: RestoreType
        - Name: Tags
        - Name: EnableCloudwatchLogsExports
    Attributes:
        - Name: ClusterResourceId
        - Name: Endpoint
        - Name: Port
        - Name: ReadEndpoint
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StorageEncrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-storageencrypted""", alias="StorageEncrypted")
    RestoreToTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-restoretotime""", alias="RestoreToTime")
    EngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-engineversion""", alias="EngineVersion")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-kmskeyid""", alias="KmsKeyId")
    AvailabilityZones_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-availabilityzones""", alias="AvailabilityZones")
    SnapshotIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-snapshotidentifier""", alias="SnapshotIdentifier")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-port""", alias="Port")
    DBClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbclusteridentifier""", alias="DBClusterIdentifier")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    DBSubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbsubnetgroupname""", alias="DBSubnetGroupName")
    DeletionProtection_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-deletionprotection""", alias="DeletionProtection")
    PreferredBackupWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-preferredbackupwindow""", alias="PreferredBackupWindow")
    UseLatestRestorableTime_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-uselatestrestorabletime""", alias="UseLatestRestorableTime")
    MasterUserPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-masteruserpassword""", alias="MasterUserPassword")
    VpcSecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-vpcsecuritygroupids""", alias="VpcSecurityGroupIds")
    SourceDBClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-sourcedbclusteridentifier""", alias="SourceDBClusterIdentifier")
    MasterUsername_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-masterusername""", alias="MasterUsername")
    DBClusterParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbclusterparametergroupname""", alias="DBClusterParameterGroupName")
    CopyTagsToSnapshot_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-copytagstosnapshot""", alias="CopyTagsToSnapshot")
    BackupRetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-backupretentionperiod""", alias="BackupRetentionPeriod")
    RestoreType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-restoretype""", alias="RestoreType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-tags""", alias="Tags")
    EnableCloudwatchLogsExports_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-enablecloudwatchlogsexports""", alias="EnableCloudwatchLogsExports")
    

    @property
    def tropo_type(self) -> troposphere.docdb.DBCluster:
        from troposphere.docdb import DBCluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.docdb import DBCluster as TropoT
        return resource_to_troposphere(self, TropoT)


class DBClusterParameterGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html
    Properties:
        - Name: Description
        - Name: Parameters
        - Name: Family
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-description""", alias="Description")
    Parameters_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-parameters""", alias="Parameters")
    Family_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-family""", alias="Family")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.docdb.DBClusterParameterGroup:
        from troposphere.docdb import DBClusterParameterGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.docdb import DBClusterParameterGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class DBInstance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html
    Properties:
        - Name: DBInstanceClass
        - Name: DBClusterIdentifier
        - Name: AvailabilityZone
        - Name: PreferredMaintenanceWindow
        - Name: EnablePerformanceInsights
        - Name: AutoMinorVersionUpgrade
        - Name: DBInstanceIdentifier
        - Name: Tags
    Attributes:
        - Name: Endpoint
        - Name: Port
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DBInstanceClass_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbinstanceclass""", alias="DBInstanceClass")
    DBClusterIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbclusteridentifier""", alias="DBClusterIdentifier")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-availabilityzone""", alias="AvailabilityZone")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    EnablePerformanceInsights_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-enableperformanceinsights""", alias="EnablePerformanceInsights")
    AutoMinorVersionUpgrade_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-autominorversionupgrade""", alias="AutoMinorVersionUpgrade")
    DBInstanceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbinstanceidentifier""", alias="DBInstanceIdentifier")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.docdb.DBInstance:
        from troposphere.docdb import DBInstance as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.docdb import DBInstance as TropoT
        return resource_to_troposphere(self, TropoT)


class DBSubnetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html
    Properties:
        - Name: DBSubnetGroupName
        - Name: DBSubnetGroupDescription
        - Name: SubnetIds
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DBSubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-dbsubnetgroupname""", alias="DBSubnetGroupName")
    DBSubnetGroupDescription_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-dbsubnetgroupdescription""", alias="DBSubnetGroupDescription")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-subnetids""", alias="SubnetIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.docdb.DBSubnetGroup:
        from troposphere.docdb import DBSubnetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.docdb import DBSubnetGroup as TropoT
        return resource_to_troposphere(self, TropoT)

