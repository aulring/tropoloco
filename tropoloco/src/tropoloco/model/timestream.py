from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DimensionMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-dimensionmapping.html
    Properties:
        - Name: DimensionValueType
        - Name: Name
    
    """
    
    DimensionValueType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-dimensionmapping.html#cfn-timestream-scheduledquery-dimensionmapping-dimensionvaluetype""", alias="DimensionValueType")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-dimensionmapping.html#cfn-timestream-scheduledquery-dimensionmapping-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.timestream.DimensionMapping:
        from troposphere.timestream import DimensionMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ErrorReportConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-errorreportconfiguration.html
    Properties:
        - Name: S3Configuration
    
    """
    
    S3Configuration_: 'S3Configuration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-errorreportconfiguration.html#cfn-timestream-scheduledquery-errorreportconfiguration-s3configuration""", alias="S3Configuration")
    


    @property
    def tropo_type(self) -> troposphere.timestream.ErrorReportConfiguration:
        from troposphere.timestream import ErrorReportConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MixedMeasureMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html
    Properties:
        - Name: MeasureName
        - Name: SourceColumn
        - Name: TargetMeasureName
        - Name: MeasureValueType
        - Name: MultiMeasureAttributeMappings
    
    """
    
    MeasureName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html#cfn-timestream-scheduledquery-mixedmeasuremapping-measurename""", alias="MeasureName")
    SourceColumn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html#cfn-timestream-scheduledquery-mixedmeasuremapping-sourcecolumn""", alias="SourceColumn")
    TargetMeasureName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html#cfn-timestream-scheduledquery-mixedmeasuremapping-targetmeasurename""", alias="TargetMeasureName")
    MeasureValueType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html#cfn-timestream-scheduledquery-mixedmeasuremapping-measurevaluetype""", alias="MeasureValueType")
    MultiMeasureAttributeMappings_: Optional[List['MultiMeasureAttributeMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html#cfn-timestream-scheduledquery-mixedmeasuremapping-multimeasureattributemappings""", alias="MultiMeasureAttributeMappings")
    


    @property
    def tropo_type(self) -> troposphere.timestream.MixedMeasureMapping:
        from troposphere.timestream import MixedMeasureMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MultiMeasureAttributeMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasureattributemapping.html
    Properties:
        - Name: SourceColumn
        - Name: TargetMultiMeasureAttributeName
        - Name: MeasureValueType
    
    """
    
    SourceColumn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasureattributemapping.html#cfn-timestream-scheduledquery-multimeasureattributemapping-sourcecolumn""", alias="SourceColumn")
    TargetMultiMeasureAttributeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasureattributemapping.html#cfn-timestream-scheduledquery-multimeasureattributemapping-targetmultimeasureattributename""", alias="TargetMultiMeasureAttributeName")
    MeasureValueType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasureattributemapping.html#cfn-timestream-scheduledquery-multimeasureattributemapping-measurevaluetype""", alias="MeasureValueType")
    


    @property
    def tropo_type(self) -> troposphere.timestream.MultiMeasureAttributeMapping:
        from troposphere.timestream import MultiMeasureAttributeMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MultiMeasureMappings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasuremappings.html
    Properties:
        - Name: TargetMultiMeasureName
        - Name: MultiMeasureAttributeMappings
    
    """
    
    TargetMultiMeasureName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasuremappings.html#cfn-timestream-scheduledquery-multimeasuremappings-targetmultimeasurename""", alias="TargetMultiMeasureName")
    MultiMeasureAttributeMappings_: List['MultiMeasureAttributeMapping'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasuremappings.html#cfn-timestream-scheduledquery-multimeasuremappings-multimeasureattributemappings""", alias="MultiMeasureAttributeMappings")
    


    @property
    def tropo_type(self) -> troposphere.timestream.MultiMeasureMappings:
        from troposphere.timestream import MultiMeasureMappings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-notificationconfiguration.html
    Properties:
        - Name: SnsConfiguration
    
    """
    
    SnsConfiguration_: 'SnsConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-notificationconfiguration.html#cfn-timestream-scheduledquery-notificationconfiguration-snsconfiguration""", alias="SnsConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.timestream.NotificationConfiguration:
        from troposphere.timestream import NotificationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Configuration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-s3configuration.html
    Properties:
        - Name: BucketName
        - Name: ObjectKeyPrefix
        - Name: EncryptionOption
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-s3configuration.html#cfn-timestream-scheduledquery-s3configuration-bucketname""", alias="BucketName")
    ObjectKeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-s3configuration.html#cfn-timestream-scheduledquery-s3configuration-objectkeyprefix""", alias="ObjectKeyPrefix")
    EncryptionOption_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-s3configuration.html#cfn-timestream-scheduledquery-s3configuration-encryptionoption""", alias="EncryptionOption")
    


    @property
    def tropo_type(self) -> troposphere.timestream.S3Configuration:
        from troposphere.timestream import S3Configuration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScheduleConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-scheduleconfiguration.html
    Properties:
        - Name: ScheduleExpression
    
    """
    
    ScheduleExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-scheduleconfiguration.html#cfn-timestream-scheduledquery-scheduleconfiguration-scheduleexpression""", alias="ScheduleExpression")
    


    @property
    def tropo_type(self) -> troposphere.timestream.ScheduleConfiguration:
        from troposphere.timestream import ScheduleConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-snsconfiguration.html
    Properties:
        - Name: TopicArn
    
    """
    
    TopicArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-snsconfiguration.html#cfn-timestream-scheduledquery-snsconfiguration-topicarn""", alias="TopicArn")
    


    @property
    def tropo_type(self) -> troposphere.timestream.SnsConfiguration:
        from troposphere.timestream import SnsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-targetconfiguration.html
    Properties:
        - Name: TimestreamConfiguration
    
    """
    
    TimestreamConfiguration_: 'TimestreamConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-targetconfiguration.html#cfn-timestream-scheduledquery-targetconfiguration-timestreamconfiguration""", alias="TimestreamConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.timestream.TargetConfiguration:
        from troposphere.timestream import TargetConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimestreamConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html
    Properties:
        - Name: TimeColumn
        - Name: TableName
        - Name: DimensionMappings
        - Name: MixedMeasureMappings
        - Name: MeasureNameColumn
        - Name: DatabaseName
        - Name: MultiMeasureMappings
    
    """
    
    TimeColumn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-timecolumn""", alias="TimeColumn")
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-tablename""", alias="TableName")
    DimensionMappings_: List['DimensionMapping'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-dimensionmappings""", alias="DimensionMappings")
    MixedMeasureMappings_: Optional[List['MixedMeasureMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-mixedmeasuremappings""", alias="MixedMeasureMappings")
    MeasureNameColumn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-measurenamecolumn""", alias="MeasureNameColumn")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-databasename""", alias="DatabaseName")
    MultiMeasureMappings_: Optional['MultiMeasureMappings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-multimeasuremappings""", alias="MultiMeasureMappings")
    


    @property
    def tropo_type(self) -> troposphere.timestream.TimestreamConfiguration:
        from troposphere.timestream import TimestreamConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MagneticStoreRejectedDataLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-magneticstorerejecteddatalocation.html
    Properties:
        - Name: S3Configuration
    
    """
    
    S3Configuration_: Optional['S3Configuration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-magneticstorerejecteddatalocation.html#cfn-timestream-table-magneticstorerejecteddatalocation-s3configuration""", alias="S3Configuration")
    


    @property
    def tropo_type(self) -> troposphere.timestream.MagneticStoreRejectedDataLocation:
        from troposphere.timestream import MagneticStoreRejectedDataLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MagneticStoreWriteProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-magneticstorewriteproperties.html
    Properties:
        - Name: EnableMagneticStoreWrites
        - Name: MagneticStoreRejectedDataLocation
    
    """
    
    EnableMagneticStoreWrites_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-magneticstorewriteproperties.html#cfn-timestream-table-magneticstorewriteproperties-enablemagneticstorewrites""", alias="EnableMagneticStoreWrites")
    MagneticStoreRejectedDataLocation_: Optional['MagneticStoreRejectedDataLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-magneticstorewriteproperties.html#cfn-timestream-table-magneticstorewriteproperties-magneticstorerejecteddatalocation""", alias="MagneticStoreRejectedDataLocation")
    


    @property
    def tropo_type(self) -> troposphere.timestream.MagneticStoreWriteProperties:
        from troposphere.timestream import MagneticStoreWriteProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PartitionKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-partitionkey.html
    Properties:
        - Name: Type
        - Name: EnforcementInRecord
        - Name: Name
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-partitionkey.html#cfn-timestream-table-partitionkey-type""", alias="Type")
    EnforcementInRecord_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-partitionkey.html#cfn-timestream-table-partitionkey-enforcementinrecord""", alias="EnforcementInRecord")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-partitionkey.html#cfn-timestream-table-partitionkey-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.timestream.PartitionKey:
        from troposphere.timestream import PartitionKey as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RetentionProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-retentionproperties.html
    Properties:
        - Name: MagneticStoreRetentionPeriodInDays
        - Name: MemoryStoreRetentionPeriodInHours
    
    """
    
    MagneticStoreRetentionPeriodInDays_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-retentionproperties.html#cfn-timestream-table-retentionproperties-magneticstoreretentionperiodindays""", alias="MagneticStoreRetentionPeriodInDays")
    MemoryStoreRetentionPeriodInHours_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-retentionproperties.html#cfn-timestream-table-retentionproperties-memorystoreretentionperiodinhours""", alias="MemoryStoreRetentionPeriodInHours")
    


    @property
    def tropo_type(self) -> troposphere.timestream.RetentionProperties:
        from troposphere.timestream import RetentionProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Configuration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-s3configuration.html
    Properties:
        - Name: BucketName
        - Name: KmsKeyId
        - Name: ObjectKeyPrefix
        - Name: EncryptionOption
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-s3configuration.html#cfn-timestream-table-s3configuration-bucketname""", alias="BucketName")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-s3configuration.html#cfn-timestream-table-s3configuration-kmskeyid""", alias="KmsKeyId")
    ObjectKeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-s3configuration.html#cfn-timestream-table-s3configuration-objectkeyprefix""", alias="ObjectKeyPrefix")
    EncryptionOption_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-s3configuration.html#cfn-timestream-table-s3configuration-encryptionoption""", alias="EncryptionOption")
    


    @property
    def tropo_type(self) -> troposphere.timestream.S3Configuration:
        from troposphere.timestream import S3Configuration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Schema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-schema.html
    Properties:
        - Name: CompositePartitionKey
    
    """
    
    CompositePartitionKey_: Optional[List['PartitionKey']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-schema.html#cfn-timestream-table-schema-compositepartitionkey""", alias="CompositePartitionKey")
    


    @property
    def tropo_type(self) -> troposphere.timestream.Schema:
        from troposphere.timestream import Schema as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Database(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html
    Properties:
        - Name: KmsKeyId
        - Name: DatabaseName
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html#cfn-timestream-database-kmskeyid""", alias="KmsKeyId")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html#cfn-timestream-database-databasename""", alias="DatabaseName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html#cfn-timestream-database-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.timestream.Database:
        from troposphere.timestream import Database as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.timestream import Database as TropoT
        return resource_to_troposphere(self, TropoT)


class ScheduledQuery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html
    Properties:
        - Name: ScheduledQueryExecutionRoleArn
        - Name: ErrorReportConfiguration
        - Name: ScheduleConfiguration
        - Name: TargetConfiguration
        - Name: KmsKeyId
        - Name: QueryString
        - Name: NotificationConfiguration
        - Name: ScheduledQueryName
        - Name: ClientToken
        - Name: Tags
    Attributes:
        - Name: SQScheduleConfiguration
        - Name: SQNotificationConfiguration
        - Name: SQErrorReportConfiguration
        - Name: SQKmsKeyId
        - Name: SQQueryString
        - Name: SQTargetConfiguration
        - Name: SQName
        - Name: Arn
        - Name: SQScheduledQueryExecutionRoleArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ScheduledQueryExecutionRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-scheduledqueryexecutionrolearn""", alias="ScheduledQueryExecutionRoleArn")
    ErrorReportConfiguration_: 'ErrorReportConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-errorreportconfiguration""", alias="ErrorReportConfiguration")
    ScheduleConfiguration_: 'ScheduleConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-scheduleconfiguration""", alias="ScheduleConfiguration")
    TargetConfiguration_: Optional['TargetConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-targetconfiguration""", alias="TargetConfiguration")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-kmskeyid""", alias="KmsKeyId")
    QueryString_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-querystring""", alias="QueryString")
    NotificationConfiguration_: 'NotificationConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-notificationconfiguration""", alias="NotificationConfiguration")
    ScheduledQueryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-scheduledqueryname""", alias="ScheduledQueryName")
    ClientToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-clienttoken""", alias="ClientToken")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.timestream.ScheduledQuery:
        from troposphere.timestream import ScheduledQuery as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.timestream import ScheduledQuery as TropoT
        return resource_to_troposphere(self, TropoT)


class Table(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html
    Properties:
        - Name: TableName
        - Name: RetentionProperties
        - Name: Schema
        - Name: DatabaseName
        - Name: Tags
        - Name: MagneticStoreWriteProperties
    Attributes:
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TableName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-tablename""", alias="TableName")
    RetentionProperties_: Optional['RetentionProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-retentionproperties""", alias="RetentionProperties")
    Schema_: Optional['Schema'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-schema""", alias="Schema")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-databasename""", alias="DatabaseName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-tags""", alias="Tags")
    MagneticStoreWriteProperties_: Optional['MagneticStoreWriteProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-magneticstorewriteproperties""", alias="MagneticStoreWriteProperties")
    

    @property
    def tropo_type(self) -> troposphere.timestream.Table:
        from troposphere.timestream import Table as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.timestream import Table as TropoT
        return resource_to_troposphere(self, TropoT)

