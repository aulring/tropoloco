from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DBClusterRole(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptune-dbcluster-dbclusterrole.html
    Properties:
        - Name: RoleArn
        - Name: FeatureName
    
    """
    
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptune-dbcluster-dbclusterrole.html#cfn-neptune-dbcluster-dbclusterrole-rolearn""", alias="RoleArn")
    FeatureName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptune-dbcluster-dbclusterrole.html#cfn-neptune-dbcluster-dbclusterrole-featurename""", alias="FeatureName")
    


    @property
    def tropo_type(self) -> troposphere.neptune.DBClusterRole:
        from troposphere.neptune import DBClusterRole as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServerlessScalingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptune-dbcluster-serverlessscalingconfiguration.html
    Properties:
        - Name: MinCapacity
        - Name: MaxCapacity
    
    """
    
    MinCapacity_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptune-dbcluster-serverlessscalingconfiguration.html#cfn-neptune-dbcluster-serverlessscalingconfiguration-mincapacity""", alias="MinCapacity")
    MaxCapacity_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptune-dbcluster-serverlessscalingconfiguration.html#cfn-neptune-dbcluster-serverlessscalingconfiguration-maxcapacity""", alias="MaxCapacity")
    


    @property
    def tropo_type(self) -> troposphere.neptune.ServerlessScalingConfiguration:
        from troposphere.neptune import ServerlessScalingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class DBCluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html
    Properties:
        - Name: StorageEncrypted
        - Name: RestoreToTime
        - Name: AssociatedRoles
        - Name: SnapshotIdentifier
        - Name: DBClusterIdentifier
        - Name: PreferredBackupWindow
        - Name: DBPort
        - Name: VpcSecurityGroupIds
        - Name: CopyTagsToSnapshot
        - Name: RestoreType
        - Name: Tags
        - Name: EngineVersion
        - Name: KmsKeyId
        - Name: AvailabilityZones
        - Name: ServerlessScalingConfiguration
        - Name: PreferredMaintenanceWindow
        - Name: IamAuthEnabled
        - Name: DBSubnetGroupName
        - Name: DeletionProtection
        - Name: UseLatestRestorableTime
        - Name: SourceDBClusterIdentifier
        - Name: DBClusterParameterGroupName
        - Name: BackupRetentionPeriod
        - Name: DBInstanceParameterGroupName
        - Name: EnableCloudwatchLogsExports
    Attributes:
        - Name: ClusterResourceId
        - Name: Endpoint
        - Name: Port
        - Name: ReadEndpoint
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StorageEncrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-storageencrypted""", alias="StorageEncrypted")
    RestoreToTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-restoretotime""", alias="RestoreToTime")
    AssociatedRoles_: Optional[List['DBClusterRole']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-associatedroles""", alias="AssociatedRoles")
    SnapshotIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-snapshotidentifier""", alias="SnapshotIdentifier")
    DBClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-dbclusteridentifier""", alias="DBClusterIdentifier")
    PreferredBackupWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-preferredbackupwindow""", alias="PreferredBackupWindow")
    DBPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-dbport""", alias="DBPort")
    VpcSecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-vpcsecuritygroupids""", alias="VpcSecurityGroupIds")
    CopyTagsToSnapshot_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-copytagstosnapshot""", alias="CopyTagsToSnapshot")
    RestoreType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-restoretype""", alias="RestoreType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-tags""", alias="Tags")
    EngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-engineversion""", alias="EngineVersion")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-kmskeyid""", alias="KmsKeyId")
    AvailabilityZones_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-availabilityzones""", alias="AvailabilityZones")
    ServerlessScalingConfiguration_: Optional['ServerlessScalingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-serverlessscalingconfiguration""", alias="ServerlessScalingConfiguration")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    IamAuthEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-iamauthenabled""", alias="IamAuthEnabled")
    DBSubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-dbsubnetgroupname""", alias="DBSubnetGroupName")
    DeletionProtection_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-deletionprotection""", alias="DeletionProtection")
    UseLatestRestorableTime_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-uselatestrestorabletime""", alias="UseLatestRestorableTime")
    SourceDBClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-sourcedbclusteridentifier""", alias="SourceDBClusterIdentifier")
    DBClusterParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-dbclusterparametergroupname""", alias="DBClusterParameterGroupName")
    BackupRetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-backupretentionperiod""", alias="BackupRetentionPeriod")
    DBInstanceParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-dbinstanceparametergroupname""", alias="DBInstanceParameterGroupName")
    EnableCloudwatchLogsExports_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-enablecloudwatchlogsexports""", alias="EnableCloudwatchLogsExports")
    

    @property
    def tropo_type(self) -> troposphere.neptune.DBCluster:
        from troposphere.neptune import DBCluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.neptune import DBCluster as TropoT
        return resource_to_troposphere(self, TropoT)


class DBClusterParameterGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html
    Properties:
        - Name: Description
        - Name: Parameters
        - Name: Family
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-description""", alias="Description")
    Parameters_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-parameters""", alias="Parameters")
    Family_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-family""", alias="Family")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html#cfn-neptune-dbclusterparametergroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.neptune.DBClusterParameterGroup:
        from troposphere.neptune import DBClusterParameterGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.neptune import DBClusterParameterGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class DBInstance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html
    Properties:
        - Name: DBParameterGroupName
        - Name: DBInstanceClass
        - Name: AllowMajorVersionUpgrade
        - Name: DBClusterIdentifier
        - Name: AvailabilityZone
        - Name: PreferredMaintenanceWindow
        - Name: AutoMinorVersionUpgrade
        - Name: DBSubnetGroupName
        - Name: DBInstanceIdentifier
        - Name: DBSnapshotIdentifier
        - Name: Tags
    Attributes:
        - Name: Endpoint
        - Name: Port
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DBParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbparametergroupname""", alias="DBParameterGroupName")
    DBInstanceClass_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbinstanceclass""", alias="DBInstanceClass")
    AllowMajorVersionUpgrade_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-allowmajorversionupgrade""", alias="AllowMajorVersionUpgrade")
    DBClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbclusteridentifier""", alias="DBClusterIdentifier")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-availabilityzone""", alias="AvailabilityZone")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    AutoMinorVersionUpgrade_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-autominorversionupgrade""", alias="AutoMinorVersionUpgrade")
    DBSubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbsubnetgroupname""", alias="DBSubnetGroupName")
    DBInstanceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbinstanceidentifier""", alias="DBInstanceIdentifier")
    DBSnapshotIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-dbsnapshotidentifier""", alias="DBSnapshotIdentifier")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html#cfn-neptune-dbinstance-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.neptune.DBInstance:
        from troposphere.neptune import DBInstance as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.neptune import DBInstance as TropoT
        return resource_to_troposphere(self, TropoT)


class DBParameterGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html
    Properties:
        - Name: Description
        - Name: Parameters
        - Name: Family
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-description""", alias="Description")
    Parameters_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-parameters""", alias="Parameters")
    Family_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-family""", alias="Family")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html#cfn-neptune-dbparametergroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.neptune.DBParameterGroup:
        from troposphere.neptune import DBParameterGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.neptune import DBParameterGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class DBSubnetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html
    Properties:
        - Name: DBSubnetGroupName
        - Name: DBSubnetGroupDescription
        - Name: SubnetIds
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DBSubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html#cfn-neptune-dbsubnetgroup-dbsubnetgroupname""", alias="DBSubnetGroupName")
    DBSubnetGroupDescription_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html#cfn-neptune-dbsubnetgroup-dbsubnetgroupdescription""", alias="DBSubnetGroupDescription")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html#cfn-neptune-dbsubnetgroup-subnetids""", alias="SubnetIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html#cfn-neptune-dbsubnetgroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.neptune.DBSubnetGroup:
        from troposphere.neptune import DBSubnetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.neptune import DBSubnetGroup as TropoT
        return resource_to_troposphere(self, TropoT)

