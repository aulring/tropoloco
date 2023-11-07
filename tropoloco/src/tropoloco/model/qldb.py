from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class KinesisConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html
    Properties:
        - Name: AggregationEnabled
        - Name: StreamArn
    
    """
    
    AggregationEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html#cfn-qldb-stream-kinesisconfiguration-aggregationenabled""", alias="AggregationEnabled")
    StreamArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html#cfn-qldb-stream-kinesisconfiguration-streamarn""", alias="StreamArn")
    


    @property
    def tropo_type(self) -> troposphere.qldb.KinesisConfiguration:
        from troposphere.qldb import KinesisConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Ledger(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html
    Properties:
        - Name: PermissionsMode
        - Name: DeletionProtection
        - Name: KmsKey
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PermissionsMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-permissionsmode""", alias="PermissionsMode")
    DeletionProtection_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-deletionprotection""", alias="DeletionProtection")
    KmsKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-kmskey""", alias="KmsKey")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.qldb.Ledger:
        from troposphere.qldb import Ledger as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.qldb import Ledger as TropoT
        return resource_to_troposphere(self, TropoT)


class Stream(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html
    Properties:
        - Name: InclusiveStartTime
        - Name: StreamName
        - Name: KinesisConfiguration
        - Name: ExclusiveEndTime
        - Name: LedgerName
        - Name: RoleArn
        - Name: Tags
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InclusiveStartTime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-inclusivestarttime""", alias="InclusiveStartTime")
    StreamName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-streamname""", alias="StreamName")
    KinesisConfiguration_: 'KinesisConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-kinesisconfiguration""", alias="KinesisConfiguration")
    ExclusiveEndTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-exclusiveendtime""", alias="ExclusiveEndTime")
    LedgerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-ledgername""", alias="LedgerName")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.qldb.Stream:
        from troposphere.qldb import Stream as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.qldb import Stream as TropoT
        return resource_to_troposphere(self, TropoT)

