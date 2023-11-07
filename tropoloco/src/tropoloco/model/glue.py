from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CsvClassifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html
    Properties:
        - Name: ContainsCustomDatatype
        - Name: QuoteSymbol
        - Name: ContainsHeader
        - Name: Delimiter
        - Name: Header
        - Name: AllowSingleColumn
        - Name: CustomDatatypeConfigured
        - Name: DisableValueTrimming
        - Name: Name
    
    """
    
    ContainsCustomDatatype_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-containscustomdatatype""", alias="ContainsCustomDatatype")
    QuoteSymbol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-quotesymbol""", alias="QuoteSymbol")
    ContainsHeader_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-containsheader""", alias="ContainsHeader")
    Delimiter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-delimiter""", alias="Delimiter")
    Header_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-header""", alias="Header")
    AllowSingleColumn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-allowsinglecolumn""", alias="AllowSingleColumn")
    CustomDatatypeConfigured_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-customdatatypeconfigured""", alias="CustomDatatypeConfigured")
    DisableValueTrimming_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-disablevaluetrimming""", alias="DisableValueTrimming")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.CsvClassifier:
        from troposphere.glue import CsvClassifier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrokClassifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html
    Properties:
        - Name: CustomPatterns
        - Name: GrokPattern
        - Name: Classification
        - Name: Name
    
    """
    
    CustomPatterns_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html#cfn-glue-classifier-grokclassifier-custompatterns""", alias="CustomPatterns")
    GrokPattern_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html#cfn-glue-classifier-grokclassifier-grokpattern""", alias="GrokPattern")
    Classification_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html#cfn-glue-classifier-grokclassifier-classification""", alias="Classification")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html#cfn-glue-classifier-grokclassifier-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.GrokClassifier:
        from troposphere.glue import GrokClassifier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JsonClassifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-jsonclassifier.html
    Properties:
        - Name: JsonPath
        - Name: Name
    
    """
    
    JsonPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-jsonclassifier.html#cfn-glue-classifier-jsonclassifier-jsonpath""", alias="JsonPath")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-jsonclassifier.html#cfn-glue-classifier-jsonclassifier-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.JsonClassifier:
        from troposphere.glue import JsonClassifier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class XMLClassifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-xmlclassifier.html
    Properties:
        - Name: RowTag
        - Name: Classification
        - Name: Name
    
    """
    
    RowTag_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-xmlclassifier.html#cfn-glue-classifier-xmlclassifier-rowtag""", alias="RowTag")
    Classification_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-xmlclassifier.html#cfn-glue-classifier-xmlclassifier-classification""", alias="Classification")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-xmlclassifier.html#cfn-glue-classifier-xmlclassifier-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.XMLClassifier:
        from troposphere.glue import XMLClassifier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectionInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html
    Properties:
        - Name: Description
        - Name: ConnectionType
        - Name: MatchCriteria
        - Name: PhysicalConnectionRequirements
        - Name: ConnectionProperties
        - Name: Name
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html#cfn-glue-connection-connectioninput-description""", alias="Description")
    ConnectionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html#cfn-glue-connection-connectioninput-connectiontype""", alias="ConnectionType")
    MatchCriteria_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html#cfn-glue-connection-connectioninput-matchcriteria""", alias="MatchCriteria")
    PhysicalConnectionRequirements_: Optional['PhysicalConnectionRequirements'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html#cfn-glue-connection-connectioninput-physicalconnectionrequirements""", alias="PhysicalConnectionRequirements")
    ConnectionProperties_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html#cfn-glue-connection-connectioninput-connectionproperties""", alias="ConnectionProperties")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html#cfn-glue-connection-connectioninput-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.ConnectionInput:
        from troposphere.glue import ConnectionInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PhysicalConnectionRequirements(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-physicalconnectionrequirements.html
    Properties:
        - Name: AvailabilityZone
        - Name: SecurityGroupIdList
        - Name: SubnetId
    
    """
    
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-physicalconnectionrequirements.html#cfn-glue-connection-physicalconnectionrequirements-availabilityzone""", alias="AvailabilityZone")
    SecurityGroupIdList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-physicalconnectionrequirements.html#cfn-glue-connection-physicalconnectionrequirements-securitygroupidlist""", alias="SecurityGroupIdList")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-physicalconnectionrequirements.html#cfn-glue-connection-physicalconnectionrequirements-subnetid""", alias="SubnetId")
    


    @property
    def tropo_type(self) -> troposphere.glue.PhysicalConnectionRequirements:
        from troposphere.glue import PhysicalConnectionRequirements as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CatalogTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html
    Properties:
        - Name: ConnectionName
        - Name: DatabaseName
        - Name: DlqEventQueueArn
        - Name: Tables
        - Name: EventQueueArn
    
    """
    
    ConnectionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html#cfn-glue-crawler-catalogtarget-connectionname""", alias="ConnectionName")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html#cfn-glue-crawler-catalogtarget-databasename""", alias="DatabaseName")
    DlqEventQueueArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html#cfn-glue-crawler-catalogtarget-dlqeventqueuearn""", alias="DlqEventQueueArn")
    Tables_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html#cfn-glue-crawler-catalogtarget-tables""", alias="Tables")
    EventQueueArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html#cfn-glue-crawler-catalogtarget-eventqueuearn""", alias="EventQueueArn")
    


    @property
    def tropo_type(self) -> troposphere.glue.CatalogTarget:
        from troposphere.glue import CatalogTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeltaTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-deltatarget.html
    Properties:
        - Name: ConnectionName
        - Name: CreateNativeDeltaTable
        - Name: WriteManifest
        - Name: DeltaTables
    
    """
    
    ConnectionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-deltatarget.html#cfn-glue-crawler-deltatarget-connectionname""", alias="ConnectionName")
    CreateNativeDeltaTable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-deltatarget.html#cfn-glue-crawler-deltatarget-createnativedeltatable""", alias="CreateNativeDeltaTable")
    WriteManifest_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-deltatarget.html#cfn-glue-crawler-deltatarget-writemanifest""", alias="WriteManifest")
    DeltaTables_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-deltatarget.html#cfn-glue-crawler-deltatarget-deltatables""", alias="DeltaTables")
    


    @property
    def tropo_type(self) -> troposphere.glue.DeltaTarget:
        from troposphere.glue import DeltaTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynamoDBTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-dynamodbtarget.html
    Properties:
        - Name: Path
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-dynamodbtarget.html#cfn-glue-crawler-dynamodbtarget-path""", alias="Path")
    


    @property
    def tropo_type(self) -> troposphere.glue.DynamoDBTarget:
        from troposphere.glue import DynamoDBTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IcebergTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-icebergtarget.html
    Properties:
        - Name: ConnectionName
        - Name: Exclusions
        - Name: Paths
        - Name: MaximumTraversalDepth
    
    """
    
    ConnectionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-icebergtarget.html#cfn-glue-crawler-icebergtarget-connectionname""", alias="ConnectionName")
    Exclusions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-icebergtarget.html#cfn-glue-crawler-icebergtarget-exclusions""", alias="Exclusions")
    Paths_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-icebergtarget.html#cfn-glue-crawler-icebergtarget-paths""", alias="Paths")
    MaximumTraversalDepth_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-icebergtarget.html#cfn-glue-crawler-icebergtarget-maximumtraversaldepth""", alias="MaximumTraversalDepth")
    


    @property
    def tropo_type(self) -> troposphere.glue.IcebergTarget:
        from troposphere.glue import IcebergTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JdbcTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-jdbctarget.html
    Properties:
        - Name: ConnectionName
        - Name: Path
        - Name: Exclusions
    
    """
    
    ConnectionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-jdbctarget.html#cfn-glue-crawler-jdbctarget-connectionname""", alias="ConnectionName")
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-jdbctarget.html#cfn-glue-crawler-jdbctarget-path""", alias="Path")
    Exclusions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-jdbctarget.html#cfn-glue-crawler-jdbctarget-exclusions""", alias="Exclusions")
    


    @property
    def tropo_type(self) -> troposphere.glue.JdbcTarget:
        from troposphere.glue import JdbcTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MongoDBTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-mongodbtarget.html
    Properties:
        - Name: ConnectionName
        - Name: Path
    
    """
    
    ConnectionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-mongodbtarget.html#cfn-glue-crawler-mongodbtarget-connectionname""", alias="ConnectionName")
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-mongodbtarget.html#cfn-glue-crawler-mongodbtarget-path""", alias="Path")
    


    @property
    def tropo_type(self) -> troposphere.glue.MongoDBTarget:
        from troposphere.glue import MongoDBTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecrawlPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-recrawlpolicy.html
    Properties:
        - Name: RecrawlBehavior
    
    """
    
    RecrawlBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-recrawlpolicy.html#cfn-glue-crawler-recrawlpolicy-recrawlbehavior""", alias="RecrawlBehavior")
    


    @property
    def tropo_type(self) -> troposphere.glue.RecrawlPolicy:
        from troposphere.glue import RecrawlPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Target(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html
    Properties:
        - Name: ConnectionName
        - Name: Path
        - Name: SampleSize
        - Name: Exclusions
        - Name: DlqEventQueueArn
        - Name: EventQueueArn
    
    """
    
    ConnectionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html#cfn-glue-crawler-s3target-connectionname""", alias="ConnectionName")
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html#cfn-glue-crawler-s3target-path""", alias="Path")
    SampleSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html#cfn-glue-crawler-s3target-samplesize""", alias="SampleSize")
    Exclusions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html#cfn-glue-crawler-s3target-exclusions""", alias="Exclusions")
    DlqEventQueueArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html#cfn-glue-crawler-s3target-dlqeventqueuearn""", alias="DlqEventQueueArn")
    EventQueueArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html#cfn-glue-crawler-s3target-eventqueuearn""", alias="EventQueueArn")
    


    @property
    def tropo_type(self) -> troposphere.glue.S3Target:
        from troposphere.glue import S3Target as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Schedule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schedule.html
    Properties:
        - Name: ScheduleExpression
    
    """
    
    ScheduleExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schedule.html#cfn-glue-crawler-schedule-scheduleexpression""", alias="ScheduleExpression")
    


    @property
    def tropo_type(self) -> troposphere.glue.Schedule:
        from troposphere.glue import Schedule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SchemaChangePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schemachangepolicy.html
    Properties:
        - Name: UpdateBehavior
        - Name: DeleteBehavior
    
    """
    
    UpdateBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schemachangepolicy.html#cfn-glue-crawler-schemachangepolicy-updatebehavior""", alias="UpdateBehavior")
    DeleteBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schemachangepolicy.html#cfn-glue-crawler-schemachangepolicy-deletebehavior""", alias="DeleteBehavior")
    


    @property
    def tropo_type(self) -> troposphere.glue.SchemaChangePolicy:
        from troposphere.glue import SchemaChangePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Targets(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html
    Properties:
        - Name: S3Targets
        - Name: CatalogTargets
        - Name: DeltaTargets
        - Name: MongoDBTargets
        - Name: JdbcTargets
        - Name: DynamoDBTargets
        - Name: IcebergTargets
    
    """
    
    S3Targets_: Optional[List['S3Target']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html#cfn-glue-crawler-targets-s3targets""", alias="S3Targets")
    CatalogTargets_: Optional[List['CatalogTarget']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html#cfn-glue-crawler-targets-catalogtargets""", alias="CatalogTargets")
    DeltaTargets_: Optional[List['DeltaTarget']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html#cfn-glue-crawler-targets-deltatargets""", alias="DeltaTargets")
    MongoDBTargets_: Optional[List['MongoDBTarget']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html#cfn-glue-crawler-targets-mongodbtargets""", alias="MongoDBTargets")
    JdbcTargets_: Optional[List['JdbcTarget']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html#cfn-glue-crawler-targets-jdbctargets""", alias="JdbcTargets")
    DynamoDBTargets_: Optional[List['DynamoDBTarget']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html#cfn-glue-crawler-targets-dynamodbtargets""", alias="DynamoDBTargets")
    IcebergTargets_: Optional[List['IcebergTarget']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html#cfn-glue-crawler-targets-icebergtargets""", alias="IcebergTargets")
    


    @property
    def tropo_type(self) -> troposphere.glue.Targets:
        from troposphere.glue import Targets as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectionPasswordEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-connectionpasswordencryption.html
    Properties:
        - Name: ReturnConnectionPasswordEncrypted
        - Name: KmsKeyId
    
    """
    
    ReturnConnectionPasswordEncrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-connectionpasswordencryption.html#cfn-glue-datacatalogencryptionsettings-connectionpasswordencryption-returnconnectionpasswordencrypted""", alias="ReturnConnectionPasswordEncrypted")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-connectionpasswordencryption.html#cfn-glue-datacatalogencryptionsettings-connectionpasswordencryption-kmskeyid""", alias="KmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.glue.ConnectionPasswordEncryption:
        from troposphere.glue import ConnectionPasswordEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataCatalogEncryptionSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings.html
    Properties:
        - Name: ConnectionPasswordEncryption
        - Name: EncryptionAtRest
    
    """
    
    ConnectionPasswordEncryption_: Optional['ConnectionPasswordEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings.html#cfn-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-connectionpasswordencryption""", alias="ConnectionPasswordEncryption")
    EncryptionAtRest_: Optional['EncryptionAtRest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings.html#cfn-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-encryptionatrest""", alias="EncryptionAtRest")
    


    @property
    def tropo_type(self) -> troposphere.glue.DataCatalogEncryptionSettings:
        from troposphere.glue import DataCatalogEncryptionSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionAtRest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-encryptionatrest.html
    Properties:
        - Name: CatalogEncryptionMode
        - Name: SseAwsKmsKeyId
    
    """
    
    CatalogEncryptionMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-encryptionatrest.html#cfn-glue-datacatalogencryptionsettings-encryptionatrest-catalogencryptionmode""", alias="CatalogEncryptionMode")
    SseAwsKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-encryptionatrest.html#cfn-glue-datacatalogencryptionsettings-encryptionatrest-sseawskmskeyid""", alias="SseAwsKmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.glue.EncryptionAtRest:
        from troposphere.glue import EncryptionAtRest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataQualityTargetTable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-dataqualityruleset-dataqualitytargettable.html
    Properties:
        - Name: TableName
        - Name: DatabaseName
    
    """
    
    TableName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-dataqualityruleset-dataqualitytargettable.html#cfn-glue-dataqualityruleset-dataqualitytargettable-tablename""", alias="TableName")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-dataqualityruleset-dataqualitytargettable.html#cfn-glue-dataqualityruleset-dataqualitytargettable-databasename""", alias="DatabaseName")
    


    @property
    def tropo_type(self) -> troposphere.glue.DataQualityTargetTable:
        from troposphere.glue import DataQualityTargetTable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataLakePrincipal(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-datalakeprincipal.html
    Properties:
        - Name: DataLakePrincipalIdentifier
    
    """
    
    DataLakePrincipalIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-datalakeprincipal.html#cfn-glue-database-datalakeprincipal-datalakeprincipalidentifier""", alias="DataLakePrincipalIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.glue.DataLakePrincipal:
        from troposphere.glue import DataLakePrincipal as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatabaseIdentifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html
    Properties:
        - Name: DatabaseName
        - Name: Region
        - Name: CatalogId
    
    """
    
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html#cfn-glue-database-databaseidentifier-databasename""", alias="DatabaseName")
    Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html#cfn-glue-database-databaseidentifier-region""", alias="Region")
    CatalogId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html#cfn-glue-database-databaseidentifier-catalogid""", alias="CatalogId")
    


    @property
    def tropo_type(self) -> troposphere.glue.DatabaseIdentifier:
        from troposphere.glue import DatabaseIdentifier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatabaseInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html
    Properties:
        - Name: LocationUri
        - Name: CreateTableDefaultPermissions
        - Name: Description
        - Name: Parameters
        - Name: TargetDatabase
        - Name: FederatedDatabase
        - Name: Name
    
    """
    
    LocationUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-locationuri""", alias="LocationUri")
    CreateTableDefaultPermissions_: Optional[List['PrincipalPrivileges']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-createtabledefaultpermissions""", alias="CreateTableDefaultPermissions")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-description""", alias="Description")
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-parameters""", alias="Parameters")
    TargetDatabase_: Optional['DatabaseIdentifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-targetdatabase""", alias="TargetDatabase")
    FederatedDatabase_: Optional['FederatedDatabase'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-federateddatabase""", alias="FederatedDatabase")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.DatabaseInput:
        from troposphere.glue import DatabaseInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FederatedDatabase(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput-federateddatabase.html
    Properties:
        - Name: ConnectionName
        - Name: Identifier
    
    """
    
    ConnectionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput-federateddatabase.html#cfn-glue-database-databaseinput-federateddatabase-connectionname""", alias="ConnectionName")
    Identifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput-federateddatabase.html#cfn-glue-database-databaseinput-federateddatabase-identifier""", alias="Identifier")
    


    @property
    def tropo_type(self) -> troposphere.glue.FederatedDatabase:
        from troposphere.glue import FederatedDatabase as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrincipalPrivileges(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html
    Properties:
        - Name: Permissions
        - Name: Principal
    
    """
    
    Permissions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html#cfn-glue-database-principalprivileges-permissions""", alias="Permissions")
    Principal_: Optional['DataLakePrincipal'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html#cfn-glue-database-principalprivileges-principal""", alias="Principal")
    


    @property
    def tropo_type(self) -> troposphere.glue.PrincipalPrivileges:
        from troposphere.glue import PrincipalPrivileges as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectionsList(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-connectionslist.html
    Properties:
        - Name: Connections
    
    """
    
    Connections_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-connectionslist.html#cfn-glue-job-connectionslist-connections""", alias="Connections")
    


    @property
    def tropo_type(self) -> troposphere.glue.ConnectionsList:
        from troposphere.glue import ConnectionsList as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExecutionProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-executionproperty.html
    Properties:
        - Name: MaxConcurrentRuns
    
    """
    
    MaxConcurrentRuns_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-executionproperty.html#cfn-glue-job-executionproperty-maxconcurrentruns""", alias="MaxConcurrentRuns")
    


    @property
    def tropo_type(self) -> troposphere.glue.ExecutionProperty:
        from troposphere.glue import ExecutionProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JobCommand(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html
    Properties:
        - Name: Runtime
        - Name: PythonVersion
        - Name: ScriptLocation
        - Name: Name
    
    """
    
    Runtime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html#cfn-glue-job-jobcommand-runtime""", alias="Runtime")
    PythonVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html#cfn-glue-job-jobcommand-pythonversion""", alias="PythonVersion")
    ScriptLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html#cfn-glue-job-jobcommand-scriptlocation""", alias="ScriptLocation")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html#cfn-glue-job-jobcommand-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.JobCommand:
        from troposphere.glue import JobCommand as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-notificationproperty.html
    Properties:
        - Name: NotifyDelayAfter
    
    """
    
    NotifyDelayAfter_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-notificationproperty.html#cfn-glue-job-notificationproperty-notifydelayafter""", alias="NotifyDelayAfter")
    


    @property
    def tropo_type(self) -> troposphere.glue.NotificationProperty:
        from troposphere.glue import NotificationProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FindMatchesParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters-findmatchesparameters.html
    Properties:
        - Name: PrecisionRecallTradeoff
        - Name: EnforceProvidedLabels
        - Name: PrimaryKeyColumnName
        - Name: AccuracyCostTradeoff
    
    """
    
    PrecisionRecallTradeoff_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters-findmatchesparameters.html#cfn-glue-mltransform-transformparameters-findmatchesparameters-precisionrecalltradeoff""", alias="PrecisionRecallTradeoff")
    EnforceProvidedLabels_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters-findmatchesparameters.html#cfn-glue-mltransform-transformparameters-findmatchesparameters-enforceprovidedlabels""", alias="EnforceProvidedLabels")
    PrimaryKeyColumnName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters-findmatchesparameters.html#cfn-glue-mltransform-transformparameters-findmatchesparameters-primarykeycolumnname""", alias="PrimaryKeyColumnName")
    AccuracyCostTradeoff_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters-findmatchesparameters.html#cfn-glue-mltransform-transformparameters-findmatchesparameters-accuracycosttradeoff""", alias="AccuracyCostTradeoff")
    


    @property
    def tropo_type(self) -> troposphere.glue.FindMatchesParameters:
        from troposphere.glue import FindMatchesParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GlueTables(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables-gluetables.html
    Properties:
        - Name: ConnectionName
        - Name: TableName
        - Name: DatabaseName
        - Name: CatalogId
    
    """
    
    ConnectionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables-gluetables.html#cfn-glue-mltransform-inputrecordtables-gluetables-connectionname""", alias="ConnectionName")
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables-gluetables.html#cfn-glue-mltransform-inputrecordtables-gluetables-tablename""", alias="TableName")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables-gluetables.html#cfn-glue-mltransform-inputrecordtables-gluetables-databasename""", alias="DatabaseName")
    CatalogId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables-gluetables.html#cfn-glue-mltransform-inputrecordtables-gluetables-catalogid""", alias="CatalogId")
    


    @property
    def tropo_type(self) -> troposphere.glue.GlueTables:
        from troposphere.glue import GlueTables as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputRecordTables(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables.html
    Properties:
        - Name: GlueTables
    
    """
    
    GlueTables_: Optional[List['GlueTables']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables.html#cfn-glue-mltransform-inputrecordtables-gluetables""", alias="GlueTables")
    


    @property
    def tropo_type(self) -> troposphere.glue.InputRecordTables:
        from troposphere.glue import InputRecordTables as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MLUserDataEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption-mluserdataencryption.html
    Properties:
        - Name: MLUserDataEncryptionMode
        - Name: KmsKeyId
    
    """
    
    MLUserDataEncryptionMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption-mluserdataencryption.html#cfn-glue-mltransform-transformencryption-mluserdataencryption-mluserdataencryptionmode""", alias="MLUserDataEncryptionMode")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption-mluserdataencryption.html#cfn-glue-mltransform-transformencryption-mluserdataencryption-kmskeyid""", alias="KmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.glue.MLUserDataEncryption:
        from troposphere.glue import MLUserDataEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TransformEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption.html
    Properties:
        - Name: MLUserDataEncryption
        - Name: TaskRunSecurityConfigurationName
    
    """
    
    MLUserDataEncryption_: Optional['MLUserDataEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption.html#cfn-glue-mltransform-transformencryption-mluserdataencryption""", alias="MLUserDataEncryption")
    TaskRunSecurityConfigurationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption.html#cfn-glue-mltransform-transformencryption-taskrunsecurityconfigurationname""", alias="TaskRunSecurityConfigurationName")
    


    @property
    def tropo_type(self) -> troposphere.glue.TransformEncryption:
        from troposphere.glue import TransformEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TransformParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters.html
    Properties:
        - Name: TransformType
        - Name: FindMatchesParameters
    
    """
    
    TransformType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters.html#cfn-glue-mltransform-transformparameters-transformtype""", alias="TransformType")
    FindMatchesParameters_: Optional['FindMatchesParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters.html#cfn-glue-mltransform-transformparameters-findmatchesparameters""", alias="FindMatchesParameters")
    


    @property
    def tropo_type(self) -> troposphere.glue.TransformParameters:
        from troposphere.glue import TransformParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Column(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-column.html
    Properties:
        - Name: Comment
        - Name: Type
        - Name: Name
    
    """
    
    Comment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-column.html#cfn-glue-partition-column-comment""", alias="Comment")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-column.html#cfn-glue-partition-column-type""", alias="Type")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-column.html#cfn-glue-partition-column-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.Column:
        from troposphere.glue import Column as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Order(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-order.html
    Properties:
        - Name: Column
        - Name: SortOrder
    
    """
    
    Column_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-order.html#cfn-glue-partition-order-column""", alias="Column")
    SortOrder_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-order.html#cfn-glue-partition-order-sortorder""", alias="SortOrder")
    


    @property
    def tropo_type(self) -> troposphere.glue.Order:
        from troposphere.glue import Order as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PartitionInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-partitioninput.html
    Properties:
        - Name: Parameters
        - Name: StorageDescriptor
        - Name: Values
    
    """
    
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-partitioninput.html#cfn-glue-partition-partitioninput-parameters""", alias="Parameters")
    StorageDescriptor_: Optional['StorageDescriptor'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-partitioninput.html#cfn-glue-partition-partitioninput-storagedescriptor""", alias="StorageDescriptor")
    Values_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-partitioninput.html#cfn-glue-partition-partitioninput-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.glue.PartitionInput:
        from troposphere.glue import PartitionInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SchemaId(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemaid.html
    Properties:
        - Name: RegistryName
        - Name: SchemaName
        - Name: SchemaArn
    
    """
    
    RegistryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemaid.html#cfn-glue-partition-schemaid-registryname""", alias="RegistryName")
    SchemaName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemaid.html#cfn-glue-partition-schemaid-schemaname""", alias="SchemaName")
    SchemaArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemaid.html#cfn-glue-partition-schemaid-schemaarn""", alias="SchemaArn")
    


    @property
    def tropo_type(self) -> troposphere.glue.SchemaId:
        from troposphere.glue import SchemaId as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SchemaReference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemareference.html
    Properties:
        - Name: SchemaVersionId
        - Name: SchemaId
        - Name: SchemaVersionNumber
    
    """
    
    SchemaVersionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemareference.html#cfn-glue-partition-schemareference-schemaversionid""", alias="SchemaVersionId")
    SchemaId_: Optional['SchemaId'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemareference.html#cfn-glue-partition-schemareference-schemaid""", alias="SchemaId")
    SchemaVersionNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemareference.html#cfn-glue-partition-schemareference-schemaversionnumber""", alias="SchemaVersionNumber")
    


    @property
    def tropo_type(self) -> troposphere.glue.SchemaReference:
        from troposphere.glue import SchemaReference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SerdeInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-serdeinfo.html
    Properties:
        - Name: Parameters
        - Name: SerializationLibrary
        - Name: Name
    
    """
    
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-serdeinfo.html#cfn-glue-partition-serdeinfo-parameters""", alias="Parameters")
    SerializationLibrary_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-serdeinfo.html#cfn-glue-partition-serdeinfo-serializationlibrary""", alias="SerializationLibrary")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-serdeinfo.html#cfn-glue-partition-serdeinfo-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.SerdeInfo:
        from troposphere.glue import SerdeInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SkewedInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-skewedinfo.html
    Properties:
        - Name: SkewedColumnNames
        - Name: SkewedColumnValues
        - Name: SkewedColumnValueLocationMaps
    
    """
    
    SkewedColumnNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-skewedinfo.html#cfn-glue-partition-skewedinfo-skewedcolumnnames""", alias="SkewedColumnNames")
    SkewedColumnValues_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-skewedinfo.html#cfn-glue-partition-skewedinfo-skewedcolumnvalues""", alias="SkewedColumnValues")
    SkewedColumnValueLocationMaps_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-skewedinfo.html#cfn-glue-partition-skewedinfo-skewedcolumnvaluelocationmaps""", alias="SkewedColumnValueLocationMaps")
    


    @property
    def tropo_type(self) -> troposphere.glue.SkewedInfo:
        from troposphere.glue import SkewedInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StorageDescriptor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html
    Properties:
        - Name: StoredAsSubDirectories
        - Name: Parameters
        - Name: BucketColumns
        - Name: NumberOfBuckets
        - Name: OutputFormat
        - Name: Columns
        - Name: SerdeInfo
        - Name: SortColumns
        - Name: Compressed
        - Name: SchemaReference
        - Name: SkewedInfo
        - Name: InputFormat
        - Name: Location
    
    """
    
    StoredAsSubDirectories_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-storedassubdirectories""", alias="StoredAsSubDirectories")
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-parameters""", alias="Parameters")
    BucketColumns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-bucketcolumns""", alias="BucketColumns")
    NumberOfBuckets_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-numberofbuckets""", alias="NumberOfBuckets")
    OutputFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-outputformat""", alias="OutputFormat")
    Columns_: Optional[List['Column']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-columns""", alias="Columns")
    SerdeInfo_: Optional['SerdeInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-serdeinfo""", alias="SerdeInfo")
    SortColumns_: Optional[List['Order']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-sortcolumns""", alias="SortColumns")
    Compressed_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-compressed""", alias="Compressed")
    SchemaReference_: Optional['SchemaReference'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-schemareference""", alias="SchemaReference")
    SkewedInfo_: Optional['SkewedInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-skewedinfo""", alias="SkewedInfo")
    InputFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-inputformat""", alias="InputFormat")
    Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-location""", alias="Location")
    


    @property
    def tropo_type(self) -> troposphere.glue.StorageDescriptor:
        from troposphere.glue import StorageDescriptor as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Registry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-registry.html
    Properties:
        - Name: Arn
        - Name: Name
    
    """
    
    Arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-registry.html#cfn-glue-schema-registry-arn""", alias="Arn")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-registry.html#cfn-glue-schema-registry-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.Registry:
        from troposphere.glue import Registry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SchemaVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-schemaversion.html
    Properties:
        - Name: IsLatest
        - Name: VersionNumber
    
    """
    
    IsLatest_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-schemaversion.html#cfn-glue-schema-schemaversion-islatest""", alias="IsLatest")
    VersionNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-schemaversion.html#cfn-glue-schema-schemaversion-versionnumber""", alias="VersionNumber")
    


    @property
    def tropo_type(self) -> troposphere.glue.SchemaVersion:
        from troposphere.glue import SchemaVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Schema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schemaversion-schema.html
    Properties:
        - Name: RegistryName
        - Name: SchemaArn
        - Name: SchemaName
    
    """
    
    RegistryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schemaversion-schema.html#cfn-glue-schemaversion-schema-registryname""", alias="RegistryName")
    SchemaArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schemaversion-schema.html#cfn-glue-schemaversion-schema-schemaarn""", alias="SchemaArn")
    SchemaName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schemaversion-schema.html#cfn-glue-schemaversion-schema-schemaname""", alias="SchemaName")
    


    @property
    def tropo_type(self) -> troposphere.glue.Schema:
        from troposphere.glue import Schema as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-cloudwatchencryption.html
    Properties:
        - Name: KmsKeyArn
        - Name: CloudWatchEncryptionMode
    
    """
    
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-cloudwatchencryption.html#cfn-glue-securityconfiguration-cloudwatchencryption-kmskeyarn""", alias="KmsKeyArn")
    CloudWatchEncryptionMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-cloudwatchencryption.html#cfn-glue-securityconfiguration-cloudwatchencryption-cloudwatchencryptionmode""", alias="CloudWatchEncryptionMode")
    


    @property
    def tropo_type(self) -> troposphere.glue.CloudWatchEncryption:
        from troposphere.glue import CloudWatchEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-encryptionconfiguration.html
    Properties:
        - Name: S3Encryptions
        - Name: CloudWatchEncryption
        - Name: JobBookmarksEncryption
    
    """
    
    S3Encryptions_: Optional['S3Encryptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-encryptionconfiguration.html#cfn-glue-securityconfiguration-encryptionconfiguration-s3encryptions""", alias="S3Encryptions")
    CloudWatchEncryption_: Optional['CloudWatchEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-encryptionconfiguration.html#cfn-glue-securityconfiguration-encryptionconfiguration-cloudwatchencryption""", alias="CloudWatchEncryption")
    JobBookmarksEncryption_: Optional['JobBookmarksEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-encryptionconfiguration.html#cfn-glue-securityconfiguration-encryptionconfiguration-jobbookmarksencryption""", alias="JobBookmarksEncryption")
    


    @property
    def tropo_type(self) -> troposphere.glue.EncryptionConfiguration:
        from troposphere.glue import EncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JobBookmarksEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-jobbookmarksencryption.html
    Properties:
        - Name: KmsKeyArn
        - Name: JobBookmarksEncryptionMode
    
    """
    
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-jobbookmarksencryption.html#cfn-glue-securityconfiguration-jobbookmarksencryption-kmskeyarn""", alias="KmsKeyArn")
    JobBookmarksEncryptionMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-jobbookmarksencryption.html#cfn-glue-securityconfiguration-jobbookmarksencryption-jobbookmarksencryptionmode""", alias="JobBookmarksEncryptionMode")
    


    @property
    def tropo_type(self) -> troposphere.glue.JobBookmarksEncryption:
        from troposphere.glue import JobBookmarksEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Encryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryption.html
    Properties:
        - Name: KmsKeyArn
        - Name: S3EncryptionMode
    
    """
    
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryption.html#cfn-glue-securityconfiguration-s3encryption-kmskeyarn""", alias="KmsKeyArn")
    S3EncryptionMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryption.html#cfn-glue-securityconfiguration-s3encryption-s3encryptionmode""", alias="S3EncryptionMode")
    


    @property
    def tropo_type(self) -> troposphere.glue.S3Encryption:
        from troposphere.glue import S3Encryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Encryptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryptions.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.glue.S3Encryptions:
        from troposphere.glue import S3Encryptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Column(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-column.html
    Properties:
        - Name: Comment
        - Name: Type
        - Name: Name
    
    """
    
    Comment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-column.html#cfn-glue-table-column-comment""", alias="Comment")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-column.html#cfn-glue-table-column-type""", alias="Type")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-column.html#cfn-glue-table-column-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.Column:
        from troposphere.glue import Column as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IcebergInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-iceberginput.html
    Properties:
        - Name: MetadataOperation
        - Name: Version
    
    """
    
    MetadataOperation_: Optional['MetadataOperation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-iceberginput.html#cfn-glue-table-iceberginput-metadataoperation""", alias="MetadataOperation")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-iceberginput.html#cfn-glue-table-iceberginput-version""", alias="Version")
    


    @property
    def tropo_type(self) -> troposphere.glue.IcebergInput:
        from troposphere.glue import IcebergInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetadataOperation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-metadataoperation.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.glue.MetadataOperation:
        from troposphere.glue import MetadataOperation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OpenTableFormatInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-opentableformatinput.html
    Properties:
        - Name: IcebergInput
    
    """
    
    IcebergInput_: Optional['IcebergInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-opentableformatinput.html#cfn-glue-table-opentableformatinput-iceberginput""", alias="IcebergInput")
    


    @property
    def tropo_type(self) -> troposphere.glue.OpenTableFormatInput:
        from troposphere.glue import OpenTableFormatInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Order(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-order.html
    Properties:
        - Name: Column
        - Name: SortOrder
    
    """
    
    Column_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-order.html#cfn-glue-table-order-column""", alias="Column")
    SortOrder_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-order.html#cfn-glue-table-order-sortorder""", alias="SortOrder")
    


    @property
    def tropo_type(self) -> troposphere.glue.Order:
        from troposphere.glue import Order as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SchemaId(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html
    Properties:
        - Name: RegistryName
        - Name: SchemaName
        - Name: SchemaArn
    
    """
    
    RegistryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html#cfn-glue-table-schemaid-registryname""", alias="RegistryName")
    SchemaName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html#cfn-glue-table-schemaid-schemaname""", alias="SchemaName")
    SchemaArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html#cfn-glue-table-schemaid-schemaarn""", alias="SchemaArn")
    


    @property
    def tropo_type(self) -> troposphere.glue.SchemaId:
        from troposphere.glue import SchemaId as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SchemaReference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html
    Properties:
        - Name: SchemaVersionId
        - Name: SchemaId
        - Name: SchemaVersionNumber
    
    """
    
    SchemaVersionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html#cfn-glue-table-schemareference-schemaversionid""", alias="SchemaVersionId")
    SchemaId_: Optional['SchemaId'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html#cfn-glue-table-schemareference-schemaid""", alias="SchemaId")
    SchemaVersionNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html#cfn-glue-table-schemareference-schemaversionnumber""", alias="SchemaVersionNumber")
    


    @property
    def tropo_type(self) -> troposphere.glue.SchemaReference:
        from troposphere.glue import SchemaReference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SerdeInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-serdeinfo.html
    Properties:
        - Name: Parameters
        - Name: SerializationLibrary
        - Name: Name
    
    """
    
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-serdeinfo.html#cfn-glue-table-serdeinfo-parameters""", alias="Parameters")
    SerializationLibrary_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-serdeinfo.html#cfn-glue-table-serdeinfo-serializationlibrary""", alias="SerializationLibrary")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-serdeinfo.html#cfn-glue-table-serdeinfo-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.SerdeInfo:
        from troposphere.glue import SerdeInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SkewedInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-skewedinfo.html
    Properties:
        - Name: SkewedColumnNames
        - Name: SkewedColumnValues
        - Name: SkewedColumnValueLocationMaps
    
    """
    
    SkewedColumnNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-skewedinfo.html#cfn-glue-table-skewedinfo-skewedcolumnnames""", alias="SkewedColumnNames")
    SkewedColumnValues_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-skewedinfo.html#cfn-glue-table-skewedinfo-skewedcolumnvalues""", alias="SkewedColumnValues")
    SkewedColumnValueLocationMaps_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-skewedinfo.html#cfn-glue-table-skewedinfo-skewedcolumnvaluelocationmaps""", alias="SkewedColumnValueLocationMaps")
    


    @property
    def tropo_type(self) -> troposphere.glue.SkewedInfo:
        from troposphere.glue import SkewedInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StorageDescriptor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html
    Properties:
        - Name: StoredAsSubDirectories
        - Name: Parameters
        - Name: BucketColumns
        - Name: NumberOfBuckets
        - Name: OutputFormat
        - Name: Columns
        - Name: SerdeInfo
        - Name: SortColumns
        - Name: Compressed
        - Name: SchemaReference
        - Name: SkewedInfo
        - Name: InputFormat
        - Name: Location
    
    """
    
    StoredAsSubDirectories_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-storedassubdirectories""", alias="StoredAsSubDirectories")
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-parameters""", alias="Parameters")
    BucketColumns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-bucketcolumns""", alias="BucketColumns")
    NumberOfBuckets_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-numberofbuckets""", alias="NumberOfBuckets")
    OutputFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-outputformat""", alias="OutputFormat")
    Columns_: Optional[List['Column']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-columns""", alias="Columns")
    SerdeInfo_: Optional['SerdeInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-serdeinfo""", alias="SerdeInfo")
    SortColumns_: Optional[List['Order']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-sortcolumns""", alias="SortColumns")
    Compressed_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-compressed""", alias="Compressed")
    SchemaReference_: Optional['SchemaReference'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-schemareference""", alias="SchemaReference")
    SkewedInfo_: Optional['SkewedInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-skewedinfo""", alias="SkewedInfo")
    InputFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-inputformat""", alias="InputFormat")
    Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-location""", alias="Location")
    


    @property
    def tropo_type(self) -> troposphere.glue.StorageDescriptor:
        from troposphere.glue import StorageDescriptor as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TableIdentifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html
    Properties:
        - Name: DatabaseName
        - Name: Region
        - Name: CatalogId
        - Name: Name
    
    """
    
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html#cfn-glue-table-tableidentifier-databasename""", alias="DatabaseName")
    Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html#cfn-glue-table-tableidentifier-region""", alias="Region")
    CatalogId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html#cfn-glue-table-tableidentifier-catalogid""", alias="CatalogId")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html#cfn-glue-table-tableidentifier-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.TableIdentifier:
        from troposphere.glue import TableIdentifier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TableInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html
    Properties:
        - Name: Owner
        - Name: ViewOriginalText
        - Name: Description
        - Name: TableType
        - Name: Parameters
        - Name: ViewExpandedText
        - Name: StorageDescriptor
        - Name: TargetTable
        - Name: PartitionKeys
        - Name: Retention
        - Name: Name
    
    """
    
    Owner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-owner""", alias="Owner")
    ViewOriginalText_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-vieworiginaltext""", alias="ViewOriginalText")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-description""", alias="Description")
    TableType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-tabletype""", alias="TableType")
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-parameters""", alias="Parameters")
    ViewExpandedText_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-viewexpandedtext""", alias="ViewExpandedText")
    StorageDescriptor_: Optional['StorageDescriptor'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-storagedescriptor""", alias="StorageDescriptor")
    TargetTable_: Optional['TableIdentifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-targettable""", alias="TargetTable")
    PartitionKeys_: Optional[List['Column']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-partitionkeys""", alias="PartitionKeys")
    Retention_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-retention""", alias="Retention")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.glue.TableInput:
        from troposphere.glue import TableInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html
    Properties:
        - Name: NotificationProperty
        - Name: CrawlerName
        - Name: Timeout
        - Name: JobName
        - Name: Arguments
        - Name: SecurityConfiguration
    
    """
    
    NotificationProperty_: Optional['NotificationProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html#cfn-glue-trigger-action-notificationproperty""", alias="NotificationProperty")
    CrawlerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html#cfn-glue-trigger-action-crawlername""", alias="CrawlerName")
    Timeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html#cfn-glue-trigger-action-timeout""", alias="Timeout")
    JobName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html#cfn-glue-trigger-action-jobname""", alias="JobName")
    Arguments_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html#cfn-glue-trigger-action-arguments""", alias="Arguments")
    SecurityConfiguration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html#cfn-glue-trigger-action-securityconfiguration""", alias="SecurityConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.glue.Action:
        from troposphere.glue import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Condition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html
    Properties:
        - Name: CrawlerName
        - Name: State
        - Name: CrawlState
        - Name: LogicalOperator
        - Name: JobName
    
    """
    
    CrawlerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html#cfn-glue-trigger-condition-crawlername""", alias="CrawlerName")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html#cfn-glue-trigger-condition-state""", alias="State")
    CrawlState_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html#cfn-glue-trigger-condition-crawlstate""", alias="CrawlState")
    LogicalOperator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html#cfn-glue-trigger-condition-logicaloperator""", alias="LogicalOperator")
    JobName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html#cfn-glue-trigger-condition-jobname""", alias="JobName")
    


    @property
    def tropo_type(self) -> troposphere.glue.Condition:
        from troposphere.glue import Condition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EventBatchingCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-eventbatchingcondition.html
    Properties:
        - Name: BatchSize
        - Name: BatchWindow
    
    """
    
    BatchSize_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-eventbatchingcondition.html#cfn-glue-trigger-eventbatchingcondition-batchsize""", alias="BatchSize")
    BatchWindow_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-eventbatchingcondition.html#cfn-glue-trigger-eventbatchingcondition-batchwindow""", alias="BatchWindow")
    


    @property
    def tropo_type(self) -> troposphere.glue.EventBatchingCondition:
        from troposphere.glue import EventBatchingCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-notificationproperty.html
    Properties:
        - Name: NotifyDelayAfter
    
    """
    
    NotifyDelayAfter_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-notificationproperty.html#cfn-glue-trigger-notificationproperty-notifydelayafter""", alias="NotifyDelayAfter")
    


    @property
    def tropo_type(self) -> troposphere.glue.NotificationProperty:
        from troposphere.glue import NotificationProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Predicate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-predicate.html
    Properties:
        - Name: Logical
        - Name: Conditions
    
    """
    
    Logical_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-predicate.html#cfn-glue-trigger-predicate-logical""", alias="Logical")
    Conditions_: Optional[List['Condition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-predicate.html#cfn-glue-trigger-predicate-conditions""", alias="Conditions")
    


    @property
    def tropo_type(self) -> troposphere.glue.Predicate:
        from troposphere.glue import Predicate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Classifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html
    Properties:
        - Name: XMLClassifier
        - Name: JsonClassifier
        - Name: CsvClassifier
        - Name: GrokClassifier
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    XMLClassifier_: Optional['XMLClassifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html#cfn-glue-classifier-xmlclassifier""", alias="XMLClassifier")
    JsonClassifier_: Optional['JsonClassifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html#cfn-glue-classifier-jsonclassifier""", alias="JsonClassifier")
    CsvClassifier_: Optional['CsvClassifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html#cfn-glue-classifier-csvclassifier""", alias="CsvClassifier")
    GrokClassifier_: Optional['GrokClassifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html#cfn-glue-classifier-grokclassifier""", alias="GrokClassifier")
    

    @property
    def tropo_type(self) -> troposphere.glue.Classifier:
        from troposphere.glue import Classifier as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import Classifier as TropoT
        return resource_to_troposphere(self, TropoT)


class Connection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-connection.html
    Properties:
        - Name: ConnectionInput
        - Name: CatalogId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConnectionInput_: 'ConnectionInput' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-connection.html#cfn-glue-connection-connectioninput""", alias="ConnectionInput")
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-connection.html#cfn-glue-connection-catalogid""", alias="CatalogId")
    

    @property
    def tropo_type(self) -> troposphere.glue.Connection:
        from troposphere.glue import Connection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import Connection as TropoT
        return resource_to_troposphere(self, TropoT)


class Crawler(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html
    Properties:
        - Name: Classifiers
        - Name: Description
        - Name: SchemaChangePolicy
        - Name: Configuration
        - Name: RecrawlPolicy
        - Name: DatabaseName
        - Name: Targets
        - Name: CrawlerSecurityConfiguration
        - Name: Name
        - Name: Role
        - Name: Schedule
        - Name: TablePrefix
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Classifiers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-classifiers""", alias="Classifiers")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-description""", alias="Description")
    SchemaChangePolicy_: Optional['SchemaChangePolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-schemachangepolicy""", alias="SchemaChangePolicy")
    Configuration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-configuration""", alias="Configuration")
    RecrawlPolicy_: Optional['RecrawlPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-recrawlpolicy""", alias="RecrawlPolicy")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-databasename""", alias="DatabaseName")
    Targets_: 'Targets' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-targets""", alias="Targets")
    CrawlerSecurityConfiguration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-crawlersecurityconfiguration""", alias="CrawlerSecurityConfiguration")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-name""", alias="Name")
    Role_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-role""", alias="Role")
    Schedule_: Optional['Schedule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-schedule""", alias="Schedule")
    TablePrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-tableprefix""", alias="TablePrefix")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.glue.Crawler:
        from troposphere.glue import Crawler as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import Crawler as TropoT
        return resource_to_troposphere(self, TropoT)


class DataCatalogEncryptionSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html
    Properties:
        - Name: DataCatalogEncryptionSettings
        - Name: CatalogId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DataCatalogEncryptionSettings_: 'DataCatalogEncryptionSettings' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html#cfn-glue-datacatalogencryptionsettings-datacatalogencryptionsettings""", alias="DataCatalogEncryptionSettings")
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html#cfn-glue-datacatalogencryptionsettings-catalogid""", alias="CatalogId")
    

    @property
    def tropo_type(self) -> troposphere.glue.DataCatalogEncryptionSettings:
        from troposphere.glue import DataCatalogEncryptionSettings as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import DataCatalogEncryptionSettings as TropoT
        return resource_to_troposphere(self, TropoT)


class DataQualityRuleset(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html
    Properties:
        - Name: Ruleset
        - Name: Description
        - Name: TargetTable
        - Name: ClientToken
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Ruleset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html#cfn-glue-dataqualityruleset-ruleset""", alias="Ruleset")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html#cfn-glue-dataqualityruleset-description""", alias="Description")
    TargetTable_: Optional['DataQualityTargetTable'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html#cfn-glue-dataqualityruleset-targettable""", alias="TargetTable")
    ClientToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html#cfn-glue-dataqualityruleset-clienttoken""", alias="ClientToken")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html#cfn-glue-dataqualityruleset-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html#cfn-glue-dataqualityruleset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.glue.DataQualityRuleset:
        from troposphere.glue import DataQualityRuleset as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import DataQualityRuleset as TropoT
        return resource_to_troposphere(self, TropoT)


class Database(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html
    Properties:
        - Name: DatabaseInput
        - Name: CatalogId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DatabaseInput_: 'DatabaseInput' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html#cfn-glue-database-databaseinput""", alias="DatabaseInput")
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html#cfn-glue-database-catalogid""", alias="CatalogId")
    

    @property
    def tropo_type(self) -> troposphere.glue.Database:
        from troposphere.glue import Database as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import Database as TropoT
        return resource_to_troposphere(self, TropoT)


class DevEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html
    Properties:
        - Name: ExtraJarsS3Path
        - Name: PublicKey
        - Name: NumberOfNodes
        - Name: Arguments
        - Name: SubnetId
        - Name: PublicKeys
        - Name: SecurityGroupIds
        - Name: RoleArn
        - Name: WorkerType
        - Name: EndpointName
        - Name: GlueVersion
        - Name: ExtraPythonLibsS3Path
        - Name: SecurityConfiguration
        - Name: NumberOfWorkers
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ExtraJarsS3Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-extrajarss3path""", alias="ExtraJarsS3Path")
    PublicKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-publickey""", alias="PublicKey")
    NumberOfNodes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-numberofnodes""", alias="NumberOfNodes")
    Arguments_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-arguments""", alias="Arguments")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-subnetid""", alias="SubnetId")
    PublicKeys_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-publickeys""", alias="PublicKeys")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-securitygroupids""", alias="SecurityGroupIds")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-rolearn""", alias="RoleArn")
    WorkerType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-workertype""", alias="WorkerType")
    EndpointName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-endpointname""", alias="EndpointName")
    GlueVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-glueversion""", alias="GlueVersion")
    ExtraPythonLibsS3Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-extrapythonlibss3path""", alias="ExtraPythonLibsS3Path")
    SecurityConfiguration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-securityconfiguration""", alias="SecurityConfiguration")
    NumberOfWorkers_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-numberofworkers""", alias="NumberOfWorkers")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.glue.DevEndpoint:
        from troposphere.glue import DevEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import DevEndpoint as TropoT
        return resource_to_troposphere(self, TropoT)


class Job(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html
    Properties:
        - Name: Connections
        - Name: MaxRetries
        - Name: Description
        - Name: Timeout
        - Name: AllocatedCapacity
        - Name: Name
        - Name: Role
        - Name: DefaultArguments
        - Name: NotificationProperty
        - Name: WorkerType
        - Name: ExecutionClass
        - Name: LogUri
        - Name: Command
        - Name: GlueVersion
        - Name: ExecutionProperty
        - Name: SecurityConfiguration
        - Name: NumberOfWorkers
        - Name: Tags
        - Name: MaxCapacity
        - Name: NonOverridableArguments
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Connections_: Optional['ConnectionsList'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-connections""", alias="Connections")
    MaxRetries_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-maxretries""", alias="MaxRetries")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-description""", alias="Description")
    Timeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-timeout""", alias="Timeout")
    AllocatedCapacity_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-allocatedcapacity""", alias="AllocatedCapacity")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-name""", alias="Name")
    Role_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-role""", alias="Role")
    DefaultArguments_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-defaultarguments""", alias="DefaultArguments")
    NotificationProperty_: Optional['NotificationProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-notificationproperty""", alias="NotificationProperty")
    WorkerType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-workertype""", alias="WorkerType")
    ExecutionClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-executionclass""", alias="ExecutionClass")
    LogUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-loguri""", alias="LogUri")
    Command_: 'JobCommand' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-command""", alias="Command")
    GlueVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-glueversion""", alias="GlueVersion")
    ExecutionProperty_: Optional['ExecutionProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-executionproperty""", alias="ExecutionProperty")
    SecurityConfiguration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-securityconfiguration""", alias="SecurityConfiguration")
    NumberOfWorkers_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-numberofworkers""", alias="NumberOfWorkers")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-tags""", alias="Tags")
    MaxCapacity_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-maxcapacity""", alias="MaxCapacity")
    NonOverridableArguments_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-nonoverridablearguments""", alias="NonOverridableArguments")
    

    @property
    def tropo_type(self) -> troposphere.glue.Job:
        from troposphere.glue import Job as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import Job as TropoT
        return resource_to_troposphere(self, TropoT)


class MLTransform(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html
    Properties:
        - Name: MaxRetries
        - Name: Description
        - Name: TransformEncryption
        - Name: Timeout
        - Name: Name
        - Name: Role
        - Name: WorkerType
        - Name: GlueVersion
        - Name: TransformParameters
        - Name: InputRecordTables
        - Name: NumberOfWorkers
        - Name: Tags
        - Name: MaxCapacity
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MaxRetries_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-maxretries""", alias="MaxRetries")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-description""", alias="Description")
    TransformEncryption_: Optional['TransformEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-transformencryption""", alias="TransformEncryption")
    Timeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-timeout""", alias="Timeout")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-name""", alias="Name")
    Role_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-role""", alias="Role")
    WorkerType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-workertype""", alias="WorkerType")
    GlueVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-glueversion""", alias="GlueVersion")
    TransformParameters_: 'TransformParameters' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-transformparameters""", alias="TransformParameters")
    InputRecordTables_: 'InputRecordTables' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-inputrecordtables""", alias="InputRecordTables")
    NumberOfWorkers_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-numberofworkers""", alias="NumberOfWorkers")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-tags""", alias="Tags")
    MaxCapacity_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-maxcapacity""", alias="MaxCapacity")
    

    @property
    def tropo_type(self) -> troposphere.glue.MLTransform:
        from troposphere.glue import MLTransform as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import MLTransform as TropoT
        return resource_to_troposphere(self, TropoT)


class Partition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html
    Properties:
        - Name: TableName
        - Name: DatabaseName
        - Name: CatalogId
        - Name: PartitionInput
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html#cfn-glue-partition-tablename""", alias="TableName")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html#cfn-glue-partition-databasename""", alias="DatabaseName")
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html#cfn-glue-partition-catalogid""", alias="CatalogId")
    PartitionInput_: 'PartitionInput' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html#cfn-glue-partition-partitioninput""", alias="PartitionInput")
    

    @property
    def tropo_type(self) -> troposphere.glue.Partition:
        from troposphere.glue import Partition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import Partition as TropoT
        return resource_to_troposphere(self, TropoT)


class Registry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-registry.html
    Properties:
        - Name: Description
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-registry.html#cfn-glue-registry-description""", alias="Description")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-registry.html#cfn-glue-registry-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-registry.html#cfn-glue-registry-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.glue.Registry:
        from troposphere.glue import Registry as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import Registry as TropoT
        return resource_to_troposphere(self, TropoT)


class Schema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html
    Properties:
        - Name: SchemaDefinition
        - Name: Description
        - Name: DataFormat
        - Name: Registry
        - Name: Compatibility
        - Name: Tags
        - Name: Name
        - Name: CheckpointVersion
    Attributes:
        - Name: InitialSchemaVersionId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SchemaDefinition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-schemadefinition""", alias="SchemaDefinition")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-description""", alias="Description")
    DataFormat_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-dataformat""", alias="DataFormat")
    Registry_: Optional['Registry'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-registry""", alias="Registry")
    Compatibility_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-compatibility""", alias="Compatibility")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-name""", alias="Name")
    CheckpointVersion_: Optional['SchemaVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-checkpointversion""", alias="CheckpointVersion")
    

    @property
    def tropo_type(self) -> troposphere.glue.Schema:
        from troposphere.glue import Schema as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import Schema as TropoT
        return resource_to_troposphere(self, TropoT)


class SchemaVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html
    Properties:
        - Name: SchemaDefinition
        - Name: Schema
    Attributes:
        - Name: VersionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SchemaDefinition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html#cfn-glue-schemaversion-schemadefinition""", alias="SchemaDefinition")
    Schema_: 'Schema' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html#cfn-glue-schemaversion-schema""", alias="Schema")
    

    @property
    def tropo_type(self) -> troposphere.glue.SchemaVersion:
        from troposphere.glue import SchemaVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import SchemaVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class SchemaVersionMetadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html
    Properties:
        - Name: SchemaVersionId
        - Name: Value
        - Name: Key
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SchemaVersionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html#cfn-glue-schemaversionmetadata-schemaversionid""", alias="SchemaVersionId")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html#cfn-glue-schemaversionmetadata-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html#cfn-glue-schemaversionmetadata-key""", alias="Key")
    

    @property
    def tropo_type(self) -> troposphere.glue.SchemaVersionMetadata:
        from troposphere.glue import SchemaVersionMetadata as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import SchemaVersionMetadata as TropoT
        return resource_to_troposphere(self, TropoT)


class SecurityConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-securityconfiguration.html
    Properties:
        - Name: EncryptionConfiguration
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EncryptionConfiguration_: 'EncryptionConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-securityconfiguration.html#cfn-glue-securityconfiguration-encryptionconfiguration""", alias="EncryptionConfiguration")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-securityconfiguration.html#cfn-glue-securityconfiguration-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.glue.SecurityConfiguration:
        from troposphere.glue import SecurityConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import SecurityConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class Table(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html
    Properties:
        - Name: TableInput
        - Name: OpenTableFormatInput
        - Name: DatabaseName
        - Name: CatalogId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TableInput_: 'TableInput' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html#cfn-glue-table-tableinput""", alias="TableInput")
    OpenTableFormatInput_: Optional['OpenTableFormatInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html#cfn-glue-table-opentableformatinput""", alias="OpenTableFormatInput")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html#cfn-glue-table-databasename""", alias="DatabaseName")
    CatalogId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html#cfn-glue-table-catalogid""", alias="CatalogId")
    

    @property
    def tropo_type(self) -> troposphere.glue.Table:
        from troposphere.glue import Table as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import Table as TropoT
        return resource_to_troposphere(self, TropoT)


class Trigger(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html
    Properties:
        - Name: Type
        - Name: StartOnCreation
        - Name: Description
        - Name: Actions
        - Name: EventBatchingCondition
        - Name: WorkflowName
        - Name: Schedule
        - Name: Tags
        - Name: Name
        - Name: Predicate
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-type""", alias="Type")
    StartOnCreation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-startoncreation""", alias="StartOnCreation")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-description""", alias="Description")
    Actions_: List['Action'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-actions""", alias="Actions")
    EventBatchingCondition_: Optional['EventBatchingCondition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-eventbatchingcondition""", alias="EventBatchingCondition")
    WorkflowName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-workflowname""", alias="WorkflowName")
    Schedule_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-schedule""", alias="Schedule")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-name""", alias="Name")
    Predicate_: Optional['Predicate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-predicate""", alias="Predicate")
    

    @property
    def tropo_type(self) -> troposphere.glue.Trigger:
        from troposphere.glue import Trigger as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import Trigger as TropoT
        return resource_to_troposphere(self, TropoT)


class Workflow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html
    Properties:
        - Name: Description
        - Name: DefaultRunProperties
        - Name: Tags
        - Name: Name
        - Name: MaxConcurrentRuns
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html#cfn-glue-workflow-description""", alias="Description")
    DefaultRunProperties_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html#cfn-glue-workflow-defaultrunproperties""", alias="DefaultRunProperties")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html#cfn-glue-workflow-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html#cfn-glue-workflow-name""", alias="Name")
    MaxConcurrentRuns_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html#cfn-glue-workflow-maxconcurrentruns""", alias="MaxConcurrentRuns")
    

    @property
    def tropo_type(self) -> troposphere.glue.Workflow:
        from troposphere.glue import Workflow as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.glue import Workflow as TropoT
        return resource_to_troposphere(self, TropoT)

