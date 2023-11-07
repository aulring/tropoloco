from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ReplicationSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-keyspace-replicationspecification.html
    Properties:
        - Name: ReplicationStrategy
        - Name: RegionList
    
    """
    
    ReplicationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-keyspace-replicationspecification.html#cfn-cassandra-keyspace-replicationspecification-replicationstrategy""", alias="ReplicationStrategy")
    RegionList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-keyspace-replicationspecification.html#cfn-cassandra-keyspace-replicationspecification-regionlist""", alias="RegionList")
    


    @property
    def tropo_type(self) -> troposphere.cassandra.ReplicationSpecification:
        from troposphere.cassandra import ReplicationSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BillingMode(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html
    Properties:
        - Name: Mode
        - Name: ProvisionedThroughput
    
    """
    
    Mode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html#cfn-cassandra-table-billingmode-mode""", alias="Mode")
    ProvisionedThroughput_: Optional['ProvisionedThroughput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html#cfn-cassandra-table-billingmode-provisionedthroughput""", alias="ProvisionedThroughput")
    


    @property
    def tropo_type(self) -> troposphere.cassandra.BillingMode:
        from troposphere.cassandra import BillingMode as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClusteringKeyColumn(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html
    Properties:
        - Name: OrderBy
        - Name: Column
    
    """
    
    OrderBy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html#cfn-cassandra-table-clusteringkeycolumn-orderby""", alias="OrderBy")
    Column_: 'Column' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html#cfn-cassandra-table-clusteringkeycolumn-column""", alias="Column")
    


    @property
    def tropo_type(self) -> troposphere.cassandra.ClusteringKeyColumn:
        from troposphere.cassandra import ClusteringKeyColumn as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Column(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html
    Properties:
        - Name: ColumnName
        - Name: ColumnType
    
    """
    
    ColumnName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html#cfn-cassandra-table-column-columnname""", alias="ColumnName")
    ColumnType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html#cfn-cassandra-table-column-columntype""", alias="ColumnType")
    


    @property
    def tropo_type(self) -> troposphere.cassandra.Column:
        from troposphere.cassandra import Column as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html
    Properties:
        - Name: EncryptionType
        - Name: KmsKeyIdentifier
    
    """
    
    EncryptionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html#cfn-cassandra-table-encryptionspecification-encryptiontype""", alias="EncryptionType")
    KmsKeyIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html#cfn-cassandra-table-encryptionspecification-kmskeyidentifier""", alias="KmsKeyIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.cassandra.EncryptionSpecification:
        from troposphere.cassandra import EncryptionSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProvisionedThroughput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html
    Properties:
        - Name: WriteCapacityUnits
        - Name: ReadCapacityUnits
    
    """
    
    WriteCapacityUnits_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html#cfn-cassandra-table-provisionedthroughput-writecapacityunits""", alias="WriteCapacityUnits")
    ReadCapacityUnits_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html#cfn-cassandra-table-provisionedthroughput-readcapacityunits""", alias="ReadCapacityUnits")
    


    @property
    def tropo_type(self) -> troposphere.cassandra.ProvisionedThroughput:
        from troposphere.cassandra import ProvisionedThroughput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Keyspace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html
    Properties:
        - Name: KeyspaceName
        - Name: ReplicationSpecification
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KeyspaceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-keyspacename""", alias="KeyspaceName")
    ReplicationSpecification_: Optional['ReplicationSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-replicationspecification""", alias="ReplicationSpecification")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.cassandra.Keyspace:
        from troposphere.cassandra import Keyspace as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cassandra import Keyspace as TropoT
        return resource_to_troposphere(self, TropoT)


class Table(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html
    Properties:
        - Name: TableName
        - Name: PointInTimeRecoveryEnabled
        - Name: ClusteringKeyColumns
        - Name: ClientSideTimestampsEnabled
        - Name: PartitionKeyColumns
        - Name: BillingMode
        - Name: DefaultTimeToLive
        - Name: KeyspaceName
        - Name: EncryptionSpecification
        - Name: RegularColumns
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TableName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-tablename""", alias="TableName")
    PointInTimeRecoveryEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-pointintimerecoveryenabled""", alias="PointInTimeRecoveryEnabled")
    ClusteringKeyColumns_: Optional[List['ClusteringKeyColumn']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-clusteringkeycolumns""", alias="ClusteringKeyColumns")
    ClientSideTimestampsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-clientsidetimestampsenabled""", alias="ClientSideTimestampsEnabled")
    PartitionKeyColumns_: List['Column'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-partitionkeycolumns""", alias="PartitionKeyColumns")
    BillingMode_: Optional['BillingMode'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-billingmode""", alias="BillingMode")
    DefaultTimeToLive_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-defaulttimetolive""", alias="DefaultTimeToLive")
    KeyspaceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-keyspacename""", alias="KeyspaceName")
    EncryptionSpecification_: Optional['EncryptionSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-encryptionspecification""", alias="EncryptionSpecification")
    RegularColumns_: Optional[List['Column']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-regularcolumns""", alias="RegularColumns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.cassandra.Table:
        from troposphere.cassandra import Table as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cassandra import Table as TropoT
        return resource_to_troposphere(self, TropoT)

