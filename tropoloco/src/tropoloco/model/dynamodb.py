from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AttributeDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-attributedefinition.html
    Properties:
        - Name: AttributeType
        - Name: AttributeName
    
    """
    
    AttributeType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-attributedefinition.html#cfn-dynamodb-globaltable-attributedefinition-attributetype""", alias="AttributeType")
    AttributeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-attributedefinition.html#cfn-dynamodb-globaltable-attributedefinition-attributename""", alias="AttributeName")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.AttributeDefinition:
        from troposphere.dynamodb import AttributeDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacityAutoScalingSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html
    Properties:
        - Name: MinCapacity
        - Name: SeedCapacity
        - Name: TargetTrackingScalingPolicyConfiguration
        - Name: MaxCapacity
    
    """
    
    MinCapacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-mincapacity""", alias="MinCapacity")
    SeedCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-seedcapacity""", alias="SeedCapacity")
    TargetTrackingScalingPolicyConfiguration_: 'TargetTrackingScalingPolicyConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-targettrackingscalingpolicyconfiguration""", alias="TargetTrackingScalingPolicyConfiguration")
    MaxCapacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-maxcapacity""", alias="MaxCapacity")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.CapacityAutoScalingSettings:
        from troposphere.dynamodb import CapacityAutoScalingSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContributorInsightsSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-contributorinsightsspecification.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-contributorinsightsspecification.html#cfn-dynamodb-globaltable-contributorinsightsspecification-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.ContributorInsightsSpecification:
        from troposphere.dynamodb import ContributorInsightsSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GlobalSecondaryIndex(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html
    Properties:
        - Name: IndexName
        - Name: Projection
        - Name: KeySchema
        - Name: WriteProvisionedThroughputSettings
    
    """
    
    IndexName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-indexname""", alias="IndexName")
    Projection_: 'Projection' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-projection""", alias="Projection")
    KeySchema_: List['KeySchema'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-keyschema""", alias="KeySchema")
    WriteProvisionedThroughputSettings_: Optional['WriteProvisionedThroughputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-writeprovisionedthroughputsettings""", alias="WriteProvisionedThroughputSettings")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.GlobalSecondaryIndex:
        from troposphere.dynamodb import GlobalSecondaryIndex as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeySchema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-keyschema.html
    Properties:
        - Name: KeyType
        - Name: AttributeName
    
    """
    
    KeyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-keyschema.html#cfn-dynamodb-globaltable-keyschema-keytype""", alias="KeyType")
    AttributeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-keyschema.html#cfn-dynamodb-globaltable-keyschema-attributename""", alias="AttributeName")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.KeySchema:
        from troposphere.dynamodb import KeySchema as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisStreamSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-kinesisstreamspecification.html
    Properties:
        - Name: StreamArn
    
    """
    
    StreamArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-kinesisstreamspecification.html#cfn-dynamodb-globaltable-kinesisstreamspecification-streamarn""", alias="StreamArn")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.KinesisStreamSpecification:
        from troposphere.dynamodb import KinesisStreamSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LocalSecondaryIndex(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html
    Properties:
        - Name: IndexName
        - Name: Projection
        - Name: KeySchema
    
    """
    
    IndexName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html#cfn-dynamodb-globaltable-localsecondaryindex-indexname""", alias="IndexName")
    Projection_: 'Projection' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html#cfn-dynamodb-globaltable-localsecondaryindex-projection""", alias="Projection")
    KeySchema_: List['KeySchema'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html#cfn-dynamodb-globaltable-localsecondaryindex-keyschema""", alias="KeySchema")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.LocalSecondaryIndex:
        from troposphere.dynamodb import LocalSecondaryIndex as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PointInTimeRecoverySpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-pointintimerecoveryspecification.html
    Properties:
        - Name: PointInTimeRecoveryEnabled
    
    """
    
    PointInTimeRecoveryEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-pointintimerecoveryspecification.html#cfn-dynamodb-globaltable-pointintimerecoveryspecification-pointintimerecoveryenabled""", alias="PointInTimeRecoveryEnabled")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.PointInTimeRecoverySpecification:
        from troposphere.dynamodb import PointInTimeRecoverySpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Projection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-projection.html
    Properties:
        - Name: ProjectionType
        - Name: NonKeyAttributes
    
    """
    
    ProjectionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-projection.html#cfn-dynamodb-globaltable-projection-projectiontype""", alias="ProjectionType")
    NonKeyAttributes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-projection.html#cfn-dynamodb-globaltable-projection-nonkeyattributes""", alias="NonKeyAttributes")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.Projection:
        from troposphere.dynamodb import Projection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReadProvisionedThroughputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html
    Properties:
        - Name: ReadCapacityUnits
        - Name: ReadCapacityAutoScalingSettings
    
    """
    
    ReadCapacityUnits_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html#cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityunits""", alias="ReadCapacityUnits")
    ReadCapacityAutoScalingSettings_: Optional['CapacityAutoScalingSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html#cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityautoscalingsettings""", alias="ReadCapacityAutoScalingSettings")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.ReadProvisionedThroughputSettings:
        from troposphere.dynamodb import ReadProvisionedThroughputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicaGlobalSecondaryIndexSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html
    Properties:
        - Name: IndexName
        - Name: ContributorInsightsSpecification
        - Name: ReadProvisionedThroughputSettings
    
    """
    
    IndexName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-indexname""", alias="IndexName")
    ContributorInsightsSpecification_: Optional['ContributorInsightsSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-contributorinsightsspecification""", alias="ContributorInsightsSpecification")
    ReadProvisionedThroughputSettings_: Optional['ReadProvisionedThroughputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-readprovisionedthroughputsettings""", alias="ReadProvisionedThroughputSettings")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.ReplicaGlobalSecondaryIndexSpecification:
        from troposphere.dynamodb import ReplicaGlobalSecondaryIndexSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicaSSESpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicassespecification.html
    Properties:
        - Name: KMSMasterKeyId
    
    """
    
    KMSMasterKeyId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicassespecification.html#cfn-dynamodb-globaltable-replicassespecification-kmsmasterkeyid""", alias="KMSMasterKeyId")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.ReplicaSSESpecification:
        from troposphere.dynamodb import ReplicaSSESpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicaSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html
    Properties:
        - Name: SSESpecification
        - Name: KinesisStreamSpecification
        - Name: ContributorInsightsSpecification
        - Name: GlobalSecondaryIndexes
        - Name: Region
        - Name: PointInTimeRecoverySpecification
        - Name: ReadProvisionedThroughputSettings
        - Name: TableClass
        - Name: DeletionProtectionEnabled
        - Name: Tags
    
    """
    
    SSESpecification_: Optional['ReplicaSSESpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-ssespecification""", alias="SSESpecification")
    KinesisStreamSpecification_: Optional['KinesisStreamSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-kinesisstreamspecification""", alias="KinesisStreamSpecification")
    ContributorInsightsSpecification_: Optional['ContributorInsightsSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-contributorinsightsspecification""", alias="ContributorInsightsSpecification")
    GlobalSecondaryIndexes_: Optional[List['ReplicaGlobalSecondaryIndexSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-globalsecondaryindexes""", alias="GlobalSecondaryIndexes")
    Region_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-region""", alias="Region")
    PointInTimeRecoverySpecification_: Optional['PointInTimeRecoverySpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-pointintimerecoveryspecification""", alias="PointInTimeRecoverySpecification")
    ReadProvisionedThroughputSettings_: Optional['ReadProvisionedThroughputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-readprovisionedthroughputsettings""", alias="ReadProvisionedThroughputSettings")
    TableClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-tableclass""", alias="TableClass")
    DeletionProtectionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-deletionprotectionenabled""", alias="DeletionProtectionEnabled")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-tags""", alias="Tags")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.ReplicaSpecification:
        from troposphere.dynamodb import ReplicaSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SSESpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html
    Properties:
        - Name: SSEEnabled
        - Name: SSEType
    
    """
    
    SSEEnabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html#cfn-dynamodb-globaltable-ssespecification-sseenabled""", alias="SSEEnabled")
    SSEType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html#cfn-dynamodb-globaltable-ssespecification-ssetype""", alias="SSEType")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.SSESpecification:
        from troposphere.dynamodb import SSESpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StreamSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-streamspecification.html
    Properties:
        - Name: StreamViewType
    
    """
    
    StreamViewType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-streamspecification.html#cfn-dynamodb-globaltable-streamspecification-streamviewtype""", alias="StreamViewType")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.StreamSpecification:
        from troposphere.dynamodb import StreamSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetTrackingScalingPolicyConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html
    Properties:
        - Name: ScaleOutCooldown
        - Name: TargetValue
        - Name: DisableScaleIn
        - Name: ScaleInCooldown
    
    """
    
    ScaleOutCooldown_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleoutcooldown""", alias="ScaleOutCooldown")
    TargetValue_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-targetvalue""", alias="TargetValue")
    DisableScaleIn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-disablescalein""", alias="DisableScaleIn")
    ScaleInCooldown_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleincooldown""", alias="ScaleInCooldown")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.TargetTrackingScalingPolicyConfiguration:
        from troposphere.dynamodb import TargetTrackingScalingPolicyConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimeToLiveSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-timetolivespecification.html
    Properties:
        - Name: Enabled
        - Name: AttributeName
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-timetolivespecification.html#cfn-dynamodb-globaltable-timetolivespecification-enabled""", alias="Enabled")
    AttributeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-timetolivespecification.html#cfn-dynamodb-globaltable-timetolivespecification-attributename""", alias="AttributeName")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.TimeToLiveSpecification:
        from troposphere.dynamodb import TimeToLiveSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WriteProvisionedThroughputSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings.html
    Properties:
        - Name: WriteCapacityAutoScalingSettings
    
    """
    
    WriteCapacityAutoScalingSettings_: Optional['CapacityAutoScalingSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings.html#cfn-dynamodb-globaltable-writeprovisionedthroughputsettings-writecapacityautoscalingsettings""", alias="WriteCapacityAutoScalingSettings")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.WriteProvisionedThroughputSettings:
        from troposphere.dynamodb import WriteProvisionedThroughputSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AttributeDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-attributedefinition.html
    Properties:
        - Name: AttributeType
        - Name: AttributeName
    
    """
    
    AttributeType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-attributedefinition.html#cfn-dynamodb-table-attributedefinition-attributetype""", alias="AttributeType")
    AttributeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-attributedefinition.html#cfn-dynamodb-table-attributedefinition-attributename""", alias="AttributeName")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.AttributeDefinition:
        from troposphere.dynamodb import AttributeDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContributorInsightsSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-contributorinsightsspecification.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-contributorinsightsspecification.html#cfn-dynamodb-table-contributorinsightsspecification-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.ContributorInsightsSpecification:
        from troposphere.dynamodb import ContributorInsightsSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Csv(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-csv.html
    Properties:
        - Name: Delimiter
        - Name: HeaderList
    
    """
    
    Delimiter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-csv.html#cfn-dynamodb-table-csv-delimiter""", alias="Delimiter")
    HeaderList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-csv.html#cfn-dynamodb-table-csv-headerlist""", alias="HeaderList")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.Csv:
        from troposphere.dynamodb import Csv as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GlobalSecondaryIndex(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-globalsecondaryindex.html
    Properties:
        - Name: IndexName
        - Name: ContributorInsightsSpecification
        - Name: Projection
        - Name: ProvisionedThroughput
        - Name: KeySchema
    
    """
    
    IndexName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-globalsecondaryindex.html#cfn-dynamodb-table-globalsecondaryindex-indexname""", alias="IndexName")
    ContributorInsightsSpecification_: Optional['ContributorInsightsSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-globalsecondaryindex.html#cfn-dynamodb-table-globalsecondaryindex-contributorinsightsspecification""", alias="ContributorInsightsSpecification")
    Projection_: 'Projection' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-globalsecondaryindex.html#cfn-dynamodb-table-globalsecondaryindex-projection""", alias="Projection")
    ProvisionedThroughput_: Optional['ProvisionedThroughput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-globalsecondaryindex.html#cfn-dynamodb-table-globalsecondaryindex-provisionedthroughput""", alias="ProvisionedThroughput")
    KeySchema_: List['KeySchema'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-globalsecondaryindex.html#cfn-dynamodb-table-globalsecondaryindex-keyschema""", alias="KeySchema")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.GlobalSecondaryIndex:
        from troposphere.dynamodb import GlobalSecondaryIndex as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImportSourceSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-importsourcespecification.html
    Properties:
        - Name: S3BucketSource
        - Name: InputFormat
        - Name: InputFormatOptions
        - Name: InputCompressionType
    
    """
    
    S3BucketSource_: 'S3BucketSource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-importsourcespecification.html#cfn-dynamodb-table-importsourcespecification-s3bucketsource""", alias="S3BucketSource")
    InputFormat_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-importsourcespecification.html#cfn-dynamodb-table-importsourcespecification-inputformat""", alias="InputFormat")
    InputFormatOptions_: Optional['InputFormatOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-importsourcespecification.html#cfn-dynamodb-table-importsourcespecification-inputformatoptions""", alias="InputFormatOptions")
    InputCompressionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-importsourcespecification.html#cfn-dynamodb-table-importsourcespecification-inputcompressiontype""", alias="InputCompressionType")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.ImportSourceSpecification:
        from troposphere.dynamodb import ImportSourceSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputFormatOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-inputformatoptions.html
    Properties:
        - Name: Csv
    
    """
    
    Csv_: Optional['Csv'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-inputformatoptions.html#cfn-dynamodb-table-inputformatoptions-csv""", alias="Csv")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.InputFormatOptions:
        from troposphere.dynamodb import InputFormatOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeySchema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-keyschema.html
    Properties:
        - Name: KeyType
        - Name: AttributeName
    
    """
    
    KeyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-keyschema.html#cfn-dynamodb-table-keyschema-keytype""", alias="KeyType")
    AttributeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-keyschema.html#cfn-dynamodb-table-keyschema-attributename""", alias="AttributeName")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.KeySchema:
        from troposphere.dynamodb import KeySchema as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisStreamSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-kinesisstreamspecification.html
    Properties:
        - Name: StreamArn
    
    """
    
    StreamArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-kinesisstreamspecification.html#cfn-dynamodb-table-kinesisstreamspecification-streamarn""", alias="StreamArn")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.KinesisStreamSpecification:
        from troposphere.dynamodb import KinesisStreamSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LocalSecondaryIndex(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-localsecondaryindex.html
    Properties:
        - Name: IndexName
        - Name: Projection
        - Name: KeySchema
    
    """
    
    IndexName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-localsecondaryindex.html#cfn-dynamodb-table-localsecondaryindex-indexname""", alias="IndexName")
    Projection_: 'Projection' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-localsecondaryindex.html#cfn-dynamodb-table-localsecondaryindex-projection""", alias="Projection")
    KeySchema_: List['KeySchema'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-localsecondaryindex.html#cfn-dynamodb-table-localsecondaryindex-keyschema""", alias="KeySchema")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.LocalSecondaryIndex:
        from troposphere.dynamodb import LocalSecondaryIndex as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PointInTimeRecoverySpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.html
    Properties:
        - Name: PointInTimeRecoveryEnabled
    
    """
    
    PointInTimeRecoveryEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.html#cfn-dynamodb-table-pointintimerecoveryspecification-pointintimerecoveryenabled""", alias="PointInTimeRecoveryEnabled")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.PointInTimeRecoverySpecification:
        from troposphere.dynamodb import PointInTimeRecoverySpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Projection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-projection.html
    Properties:
        - Name: NonKeyAttributes
        - Name: ProjectionType
    
    """
    
    NonKeyAttributes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-projection.html#cfn-dynamodb-table-projection-nonkeyattributes""", alias="NonKeyAttributes")
    ProjectionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-projection.html#cfn-dynamodb-table-projection-projectiontype""", alias="ProjectionType")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.Projection:
        from troposphere.dynamodb import Projection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProvisionedThroughput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-provisionedthroughput.html
    Properties:
        - Name: WriteCapacityUnits
        - Name: ReadCapacityUnits
    
    """
    
    WriteCapacityUnits_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-provisionedthroughput.html#cfn-dynamodb-table-provisionedthroughput-writecapacityunits""", alias="WriteCapacityUnits")
    ReadCapacityUnits_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-provisionedthroughput.html#cfn-dynamodb-table-provisionedthroughput-readcapacityunits""", alias="ReadCapacityUnits")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.ProvisionedThroughput:
        from troposphere.dynamodb import ProvisionedThroughput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3BucketSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-s3bucketsource.html
    Properties:
        - Name: S3Bucket
        - Name: S3KeyPrefix
        - Name: S3BucketOwner
    
    """
    
    S3Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-s3bucketsource.html#cfn-dynamodb-table-s3bucketsource-s3bucket""", alias="S3Bucket")
    S3KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-s3bucketsource.html#cfn-dynamodb-table-s3bucketsource-s3keyprefix""", alias="S3KeyPrefix")
    S3BucketOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-s3bucketsource.html#cfn-dynamodb-table-s3bucketsource-s3bucketowner""", alias="S3BucketOwner")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.S3BucketSource:
        from troposphere.dynamodb import S3BucketSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SSESpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html
    Properties:
        - Name: SSEEnabled
        - Name: SSEType
        - Name: KMSMasterKeyId
    
    """
    
    SSEEnabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-sseenabled""", alias="SSEEnabled")
    SSEType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-ssetype""", alias="SSEType")
    KMSMasterKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-kmsmasterkeyid""", alias="KMSMasterKeyId")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.SSESpecification:
        from troposphere.dynamodb import SSESpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StreamSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-streamspecification.html
    Properties:
        - Name: StreamViewType
    
    """
    
    StreamViewType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-streamspecification.html#cfn-dynamodb-table-streamspecification-streamviewtype""", alias="StreamViewType")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.StreamSpecification:
        from troposphere.dynamodb import StreamSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimeToLiveSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-timetolivespecification.html
    Properties:
        - Name: Enabled
        - Name: AttributeName
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-timetolivespecification.html#cfn-dynamodb-table-timetolivespecification-enabled""", alias="Enabled")
    AttributeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-timetolivespecification.html#cfn-dynamodb-table-timetolivespecification-attributename""", alias="AttributeName")
    


    @property
    def tropo_type(self) -> troposphere.dynamodb.TimeToLiveSpecification:
        from troposphere.dynamodb import TimeToLiveSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class GlobalTable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html
    Properties:
        - Name: SSESpecification
        - Name: TableName
        - Name: AttributeDefinitions
        - Name: StreamSpecification
        - Name: BillingMode
        - Name: GlobalSecondaryIndexes
        - Name: KeySchema
        - Name: LocalSecondaryIndexes
        - Name: Replicas
        - Name: WriteProvisionedThroughputSettings
        - Name: TimeToLiveSpecification
    Attributes:
        - Name: TableId
        - Name: Arn
        - Name: StreamArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SSESpecification_: Optional['SSESpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-ssespecification""", alias="SSESpecification")
    TableName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-tablename""", alias="TableName")
    AttributeDefinitions_: List['AttributeDefinition'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-attributedefinitions""", alias="AttributeDefinitions")
    StreamSpecification_: Optional['StreamSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-streamspecification""", alias="StreamSpecification")
    BillingMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-billingmode""", alias="BillingMode")
    GlobalSecondaryIndexes_: Optional[List['GlobalSecondaryIndex']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-globalsecondaryindexes""", alias="GlobalSecondaryIndexes")
    KeySchema_: List['KeySchema'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-keyschema""", alias="KeySchema")
    LocalSecondaryIndexes_: Optional[List['LocalSecondaryIndex']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-localsecondaryindexes""", alias="LocalSecondaryIndexes")
    Replicas_: List['ReplicaSpecification'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-replicas""", alias="Replicas")
    WriteProvisionedThroughputSettings_: Optional['WriteProvisionedThroughputSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-writeprovisionedthroughputsettings""", alias="WriteProvisionedThroughputSettings")
    TimeToLiveSpecification_: Optional['TimeToLiveSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-timetolivespecification""", alias="TimeToLiveSpecification")
    

    @property
    def tropo_type(self) -> troposphere.dynamodb.GlobalTable:
        from troposphere.dynamodb import GlobalTable as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.dynamodb import GlobalTable as TropoT
        return resource_to_troposphere(self, TropoT)


class Table(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html
    Properties:
        - Name: SSESpecification
        - Name: KinesisStreamSpecification
        - Name: StreamSpecification
        - Name: ContributorInsightsSpecification
        - Name: ImportSourceSpecification
        - Name: PointInTimeRecoverySpecification
        - Name: ProvisionedThroughput
        - Name: TableName
        - Name: AttributeDefinitions
        - Name: BillingMode
        - Name: GlobalSecondaryIndexes
        - Name: KeySchema
        - Name: LocalSecondaryIndexes
        - Name: DeletionProtectionEnabled
        - Name: TableClass
        - Name: Tags
        - Name: TimeToLiveSpecification
    Attributes:
        - Name: Arn
        - Name: StreamArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SSESpecification_: Optional['SSESpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-ssespecification""", alias="SSESpecification")
    KinesisStreamSpecification_: Optional['KinesisStreamSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-kinesisstreamspecification""", alias="KinesisStreamSpecification")
    StreamSpecification_: Optional['StreamSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-streamspecification""", alias="StreamSpecification")
    ContributorInsightsSpecification_: Optional['ContributorInsightsSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-contributorinsightsspecification""", alias="ContributorInsightsSpecification")
    ImportSourceSpecification_: Optional['ImportSourceSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-importsourcespecification""", alias="ImportSourceSpecification")
    PointInTimeRecoverySpecification_: Optional['PointInTimeRecoverySpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-pointintimerecoveryspecification""", alias="PointInTimeRecoverySpecification")
    ProvisionedThroughput_: Optional['ProvisionedThroughput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-provisionedthroughput""", alias="ProvisionedThroughput")
    TableName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tablename""", alias="TableName")
    AttributeDefinitions_: Optional[List['AttributeDefinition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-attributedefinitions""", alias="AttributeDefinitions")
    BillingMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-billingmode""", alias="BillingMode")
    GlobalSecondaryIndexes_: Optional[List['GlobalSecondaryIndex']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-globalsecondaryindexes""", alias="GlobalSecondaryIndexes")
    KeySchema_: List['KeySchema'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-keyschema""", alias="KeySchema")
    LocalSecondaryIndexes_: Optional[List['LocalSecondaryIndex']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-localsecondaryindexes""", alias="LocalSecondaryIndexes")
    DeletionProtectionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-deletionprotectionenabled""", alias="DeletionProtectionEnabled")
    TableClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tableclass""", alias="TableClass")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tags""", alias="Tags")
    TimeToLiveSpecification_: Optional['TimeToLiveSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-timetolivespecification""", alias="TimeToLiveSpecification")
    

    @property
    def tropo_type(self) -> troposphere.dynamodb.Table:
        from troposphere.dynamodb import Table as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.dynamodb import Table as TropoT
        return resource_to_troposphere(self, TropoT)

