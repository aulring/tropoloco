from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AmazonOpenSearchServerlessBufferingHints(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints.html
    Properties:
        - Name: IntervalInSeconds
        - Name: SizeInMBs
    
    """
    
    IntervalInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints-intervalinseconds""", alias="IntervalInSeconds")
    SizeInMBs_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints-sizeinmbs""", alias="SizeInMBs")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.AmazonOpenSearchServerlessBufferingHints:
        from troposphere.kinesisfirehose import AmazonOpenSearchServerlessBufferingHints as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AmazonOpenSearchServerlessDestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html
    Properties:
        - Name: IndexName
        - Name: S3Configuration
        - Name: BufferingHints
        - Name: RetryOptions
        - Name: CollectionEndpoint
        - Name: VpcConfiguration
        - Name: ProcessingConfiguration
        - Name: CloudWatchLoggingOptions
        - Name: RoleARN
        - Name: S3BackupMode
    
    """
    
    IndexName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-indexname""", alias="IndexName")
    S3Configuration_: 'S3DestinationConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-s3configuration""", alias="S3Configuration")
    BufferingHints_: Optional['AmazonOpenSearchServerlessBufferingHints'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-bufferinghints""", alias="BufferingHints")
    RetryOptions_: Optional['AmazonOpenSearchServerlessRetryOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-retryoptions""", alias="RetryOptions")
    CollectionEndpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-collectionendpoint""", alias="CollectionEndpoint")
    VpcConfiguration_: Optional['VpcConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-vpcconfiguration""", alias="VpcConfiguration")
    ProcessingConfiguration_: Optional['ProcessingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-processingconfiguration""", alias="ProcessingConfiguration")
    CloudWatchLoggingOptions_: Optional['CloudWatchLoggingOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-cloudwatchloggingoptions""", alias="CloudWatchLoggingOptions")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-rolearn""", alias="RoleARN")
    S3BackupMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-s3backupmode""", alias="S3BackupMode")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.AmazonOpenSearchServerlessDestinationConfiguration:
        from troposphere.kinesisfirehose import AmazonOpenSearchServerlessDestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AmazonOpenSearchServerlessRetryOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessretryoptions.html
    Properties:
        - Name: DurationInSeconds
    
    """
    
    DurationInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessretryoptions.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessretryoptions-durationinseconds""", alias="DurationInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.AmazonOpenSearchServerlessRetryOptions:
        from troposphere.kinesisfirehose import AmazonOpenSearchServerlessRetryOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AmazonopensearchserviceBufferingHints(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html
    Properties:
        - Name: IntervalInSeconds
        - Name: SizeInMBs
    
    """
    
    IntervalInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints-intervalinseconds""", alias="IntervalInSeconds")
    SizeInMBs_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints-sizeinmbs""", alias="SizeInMBs")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.AmazonopensearchserviceBufferingHints:
        from troposphere.kinesisfirehose import AmazonopensearchserviceBufferingHints as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AmazonopensearchserviceDestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html
    Properties:
        - Name: TypeName
        - Name: IndexRotationPeriod
        - Name: ProcessingConfiguration
        - Name: ClusterEndpoint
        - Name: DomainARN
        - Name: RoleARN
        - Name: S3BackupMode
        - Name: IndexName
        - Name: DocumentIdOptions
        - Name: S3Configuration
        - Name: BufferingHints
        - Name: RetryOptions
        - Name: VpcConfiguration
        - Name: CloudWatchLoggingOptions
    
    """
    
    TypeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-typename""", alias="TypeName")
    IndexRotationPeriod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-indexrotationperiod""", alias="IndexRotationPeriod")
    ProcessingConfiguration_: Optional['ProcessingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-processingconfiguration""", alias="ProcessingConfiguration")
    ClusterEndpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-clusterendpoint""", alias="ClusterEndpoint")
    DomainARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-domainarn""", alias="DomainARN")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-rolearn""", alias="RoleARN")
    S3BackupMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-s3backupmode""", alias="S3BackupMode")
    IndexName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-indexname""", alias="IndexName")
    DocumentIdOptions_: Optional['DocumentIdOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-documentidoptions""", alias="DocumentIdOptions")
    S3Configuration_: 'S3DestinationConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-s3configuration""", alias="S3Configuration")
    BufferingHints_: Optional['AmazonopensearchserviceBufferingHints'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-bufferinghints""", alias="BufferingHints")
    RetryOptions_: Optional['AmazonopensearchserviceRetryOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-retryoptions""", alias="RetryOptions")
    VpcConfiguration_: Optional['VpcConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-vpcconfiguration""", alias="VpcConfiguration")
    CloudWatchLoggingOptions_: Optional['CloudWatchLoggingOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-cloudwatchloggingoptions""", alias="CloudWatchLoggingOptions")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.AmazonopensearchserviceDestinationConfiguration:
        from troposphere.kinesisfirehose import AmazonopensearchserviceDestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AmazonopensearchserviceRetryOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions.html
    Properties:
        - Name: DurationInSeconds
    
    """
    
    DurationInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions-durationinseconds""", alias="DurationInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.AmazonopensearchserviceRetryOptions:
        from troposphere.kinesisfirehose import AmazonopensearchserviceRetryOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuthenticationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration.html
    Properties:
        - Name: Connectivity
        - Name: RoleARN
    
    """
    
    Connectivity_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration.html#cfn-kinesisfirehose-deliverystream-authenticationconfiguration-connectivity""", alias="Connectivity")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration.html#cfn-kinesisfirehose-deliverystream-authenticationconfiguration-rolearn""", alias="RoleARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.AuthenticationConfiguration:
        from troposphere.kinesisfirehose import AuthenticationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BufferingHints(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html
    Properties:
        - Name: IntervalInSeconds
        - Name: SizeInMBs
    
    """
    
    IntervalInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html#cfn-kinesisfirehose-deliverystream-bufferinghints-intervalinseconds""", alias="IntervalInSeconds")
    SizeInMBs_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html#cfn-kinesisfirehose-deliverystream-bufferinghints-sizeinmbs""", alias="SizeInMBs")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.BufferingHints:
        from troposphere.kinesisfirehose import BufferingHints as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchLoggingOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html
    Properties:
        - Name: LogStreamName
        - Name: Enabled
        - Name: LogGroupName
    
    """
    
    LogStreamName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-logstreamname""", alias="LogStreamName")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-enabled""", alias="Enabled")
    LogGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-loggroupname""", alias="LogGroupName")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.CloudWatchLoggingOptions:
        from troposphere.kinesisfirehose import CloudWatchLoggingOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CopyCommand(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html
    Properties:
        - Name: DataTableName
        - Name: CopyOptions
        - Name: DataTableColumns
    
    """
    
    DataTableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-datatablename""", alias="DataTableName")
    CopyOptions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-copyoptions""", alias="CopyOptions")
    DataTableColumns_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-datatablecolumns""", alias="DataTableColumns")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.CopyCommand:
        from troposphere.kinesisfirehose import CopyCommand as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataFormatConversionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html
    Properties:
        - Name: InputFormatConfiguration
        - Name: Enabled
        - Name: SchemaConfiguration
        - Name: OutputFormatConfiguration
    
    """
    
    InputFormatConfiguration_: Optional['InputFormatConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-inputformatconfiguration""", alias="InputFormatConfiguration")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-enabled""", alias="Enabled")
    SchemaConfiguration_: Optional['SchemaConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-schemaconfiguration""", alias="SchemaConfiguration")
    OutputFormatConfiguration_: Optional['OutputFormatConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-outputformatconfiguration""", alias="OutputFormatConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.DataFormatConversionConfiguration:
        from troposphere.kinesisfirehose import DataFormatConversionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeliveryStreamEncryptionConfigurationInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html
    Properties:
        - Name: KeyType
        - Name: KeyARN
    
    """
    
    KeyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keytype""", alias="KeyType")
    KeyARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keyarn""", alias="KeyARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.DeliveryStreamEncryptionConfigurationInput:
        from troposphere.kinesisfirehose import DeliveryStreamEncryptionConfigurationInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Deserializer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html
    Properties:
        - Name: HiveJsonSerDe
        - Name: OpenXJsonSerDe
    
    """
    
    HiveJsonSerDe_: Optional['HiveJsonSerDe'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html#cfn-kinesisfirehose-deliverystream-deserializer-hivejsonserde""", alias="HiveJsonSerDe")
    OpenXJsonSerDe_: Optional['OpenXJsonSerDe'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html#cfn-kinesisfirehose-deliverystream-deserializer-openxjsonserde""", alias="OpenXJsonSerDe")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.Deserializer:
        from troposphere.kinesisfirehose import Deserializer as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DocumentIdOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-documentidoptions.html
    Properties:
        - Name: DefaultDocumentIdFormat
    
    """
    
    DefaultDocumentIdFormat_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-documentidoptions.html#cfn-kinesisfirehose-deliverystream-documentidoptions-defaultdocumentidformat""", alias="DefaultDocumentIdFormat")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.DocumentIdOptions:
        from troposphere.kinesisfirehose import DocumentIdOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynamicPartitioningConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html
    Properties:
        - Name: Enabled
        - Name: RetryOptions
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html#cfn-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration-enabled""", alias="Enabled")
    RetryOptions_: Optional['RetryOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html#cfn-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration-retryoptions""", alias="RetryOptions")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.DynamicPartitioningConfiguration:
        from troposphere.kinesisfirehose import DynamicPartitioningConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ElasticsearchBufferingHints(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html
    Properties:
        - Name: IntervalInSeconds
        - Name: SizeInMBs
    
    """
    
    IntervalInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html#cfn-kinesisfirehose-deliverystream-elasticsearchbufferinghints-intervalinseconds""", alias="IntervalInSeconds")
    SizeInMBs_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html#cfn-kinesisfirehose-deliverystream-elasticsearchbufferinghints-sizeinmbs""", alias="SizeInMBs")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.ElasticsearchBufferingHints:
        from troposphere.kinesisfirehose import ElasticsearchBufferingHints as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ElasticsearchDestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html
    Properties:
        - Name: TypeName
        - Name: IndexRotationPeriod
        - Name: ProcessingConfiguration
        - Name: ClusterEndpoint
        - Name: DomainARN
        - Name: RoleARN
        - Name: S3BackupMode
        - Name: IndexName
        - Name: DocumentIdOptions
        - Name: S3Configuration
        - Name: BufferingHints
        - Name: RetryOptions
        - Name: VpcConfiguration
        - Name: CloudWatchLoggingOptions
    
    """
    
    TypeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-typename""", alias="TypeName")
    IndexRotationPeriod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-indexrotationperiod""", alias="IndexRotationPeriod")
    ProcessingConfiguration_: Optional['ProcessingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-processingconfiguration""", alias="ProcessingConfiguration")
    ClusterEndpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-clusterendpoint""", alias="ClusterEndpoint")
    DomainARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-domainarn""", alias="DomainARN")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-rolearn""", alias="RoleARN")
    S3BackupMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-s3backupmode""", alias="S3BackupMode")
    IndexName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-indexname""", alias="IndexName")
    DocumentIdOptions_: Optional['DocumentIdOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-documentidoptions""", alias="DocumentIdOptions")
    S3Configuration_: 'S3DestinationConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-s3configuration""", alias="S3Configuration")
    BufferingHints_: Optional['ElasticsearchBufferingHints'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-bufferinghints""", alias="BufferingHints")
    RetryOptions_: Optional['ElasticsearchRetryOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-retryoptions""", alias="RetryOptions")
    VpcConfiguration_: Optional['VpcConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-vpcconfiguration""", alias="VpcConfiguration")
    CloudWatchLoggingOptions_: Optional['CloudWatchLoggingOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-cloudwatchloggingoptions""", alias="CloudWatchLoggingOptions")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.ElasticsearchDestinationConfiguration:
        from troposphere.kinesisfirehose import ElasticsearchDestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ElasticsearchRetryOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchretryoptions.html
    Properties:
        - Name: DurationInSeconds
    
    """
    
    DurationInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchretryoptions.html#cfn-kinesisfirehose-deliverystream-elasticsearchretryoptions-durationinseconds""", alias="DurationInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.ElasticsearchRetryOptions:
        from troposphere.kinesisfirehose import ElasticsearchRetryOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html
    Properties:
        - Name: KMSEncryptionConfig
        - Name: NoEncryptionConfig
    
    """
    
    KMSEncryptionConfig_: Optional['KMSEncryptionConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html#cfn-kinesisfirehose-deliverystream-encryptionconfiguration-kmsencryptionconfig""", alias="KMSEncryptionConfig")
    NoEncryptionConfig_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html#cfn-kinesisfirehose-deliverystream-encryptionconfiguration-noencryptionconfig""", alias="NoEncryptionConfig")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.EncryptionConfiguration:
        from troposphere.kinesisfirehose import EncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExtendedS3DestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html
    Properties:
        - Name: ErrorOutputPrefix
        - Name: S3BackupConfiguration
        - Name: BucketARN
        - Name: CompressionFormat
        - Name: DataFormatConversionConfiguration
        - Name: EncryptionConfiguration
        - Name: DynamicPartitioningConfiguration
        - Name: Prefix
        - Name: ProcessingConfiguration
        - Name: RoleARN
        - Name: S3BackupMode
        - Name: BufferingHints
        - Name: CloudWatchLoggingOptions
    
    """
    
    ErrorOutputPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-erroroutputprefix""", alias="ErrorOutputPrefix")
    S3BackupConfiguration_: Optional['S3DestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-s3backupconfiguration""", alias="S3BackupConfiguration")
    BucketARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-bucketarn""", alias="BucketARN")
    CompressionFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-compressionformat""", alias="CompressionFormat")
    DataFormatConversionConfiguration_: Optional['DataFormatConversionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-dataformatconversionconfiguration""", alias="DataFormatConversionConfiguration")
    EncryptionConfiguration_: Optional['EncryptionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-encryptionconfiguration""", alias="EncryptionConfiguration")
    DynamicPartitioningConfiguration_: Optional['DynamicPartitioningConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-dynamicpartitioningconfiguration""", alias="DynamicPartitioningConfiguration")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-prefix""", alias="Prefix")
    ProcessingConfiguration_: Optional['ProcessingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-processingconfiguration""", alias="ProcessingConfiguration")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-rolearn""", alias="RoleARN")
    S3BackupMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-s3backupmode""", alias="S3BackupMode")
    BufferingHints_: Optional['BufferingHints'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-bufferinghints""", alias="BufferingHints")
    CloudWatchLoggingOptions_: Optional['CloudWatchLoggingOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-cloudwatchloggingoptions""", alias="CloudWatchLoggingOptions")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.ExtendedS3DestinationConfiguration:
        from troposphere.kinesisfirehose import ExtendedS3DestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HiveJsonSerDe(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-hivejsonserde.html
    Properties:
        - Name: TimestampFormats
    
    """
    
    TimestampFormats_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-hivejsonserde.html#cfn-kinesisfirehose-deliverystream-hivejsonserde-timestampformats""", alias="TimestampFormats")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.HiveJsonSerDe:
        from troposphere.kinesisfirehose import HiveJsonSerDe as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpEndpointCommonAttribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html
    Properties:
        - Name: AttributeValue
        - Name: AttributeName
    
    """
    
    AttributeValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html#cfn-kinesisfirehose-deliverystream-httpendpointcommonattribute-attributevalue""", alias="AttributeValue")
    AttributeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html#cfn-kinesisfirehose-deliverystream-httpendpointcommonattribute-attributename""", alias="AttributeName")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.HttpEndpointCommonAttribute:
        from troposphere.kinesisfirehose import HttpEndpointCommonAttribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpEndpointConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html
    Properties:
        - Name: AccessKey
        - Name: Url
        - Name: Name
    
    """
    
    AccessKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-accesskey""", alias="AccessKey")
    Url_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-url""", alias="Url")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.HttpEndpointConfiguration:
        from troposphere.kinesisfirehose import HttpEndpointConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpEndpointDestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html
    Properties:
        - Name: RequestConfiguration
        - Name: S3Configuration
        - Name: BufferingHints
        - Name: RetryOptions
        - Name: EndpointConfiguration
        - Name: ProcessingConfiguration
        - Name: RoleARN
        - Name: CloudWatchLoggingOptions
        - Name: S3BackupMode
    
    """
    
    RequestConfiguration_: Optional['HttpEndpointRequestConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-requestconfiguration""", alias="RequestConfiguration")
    S3Configuration_: 'S3DestinationConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-s3configuration""", alias="S3Configuration")
    BufferingHints_: Optional['BufferingHints'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-bufferinghints""", alias="BufferingHints")
    RetryOptions_: Optional['RetryOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-retryoptions""", alias="RetryOptions")
    EndpointConfiguration_: 'HttpEndpointConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-endpointconfiguration""", alias="EndpointConfiguration")
    ProcessingConfiguration_: Optional['ProcessingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-processingconfiguration""", alias="ProcessingConfiguration")
    RoleARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-rolearn""", alias="RoleARN")
    CloudWatchLoggingOptions_: Optional['CloudWatchLoggingOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-cloudwatchloggingoptions""", alias="CloudWatchLoggingOptions")
    S3BackupMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-s3backupmode""", alias="S3BackupMode")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.HttpEndpointDestinationConfiguration:
        from troposphere.kinesisfirehose import HttpEndpointDestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpEndpointRequestConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html
    Properties:
        - Name: CommonAttributes
        - Name: ContentEncoding
    
    """
    
    CommonAttributes_: Optional[List['HttpEndpointCommonAttribute']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointrequestconfiguration-commonattributes""", alias="CommonAttributes")
    ContentEncoding_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointrequestconfiguration-contentencoding""", alias="ContentEncoding")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.HttpEndpointRequestConfiguration:
        from troposphere.kinesisfirehose import HttpEndpointRequestConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputFormatConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration.html
    Properties:
        - Name: Deserializer
    
    """
    
    Deserializer_: Optional['Deserializer'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration.html#cfn-kinesisfirehose-deliverystream-inputformatconfiguration-deserializer""", alias="Deserializer")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.InputFormatConfiguration:
        from troposphere.kinesisfirehose import InputFormatConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KMSEncryptionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig.html
    Properties:
        - Name: AWSKMSKeyARN
    
    """
    
    AWSKMSKeyARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig.html#cfn-kinesisfirehose-deliverystream-kmsencryptionconfig-awskmskeyarn""", alias="AWSKMSKeyARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.KMSEncryptionConfig:
        from troposphere.kinesisfirehose import KMSEncryptionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisStreamSourceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html
    Properties:
        - Name: KinesisStreamARN
        - Name: RoleARN
    
    """
    
    KinesisStreamARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-kinesisstreamarn""", alias="KinesisStreamARN")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-rolearn""", alias="RoleARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.KinesisStreamSourceConfiguration:
        from troposphere.kinesisfirehose import KinesisStreamSourceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MSKSourceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html
    Properties:
        - Name: AuthenticationConfiguration
        - Name: MSKClusterARN
        - Name: TopicName
    
    """
    
    AuthenticationConfiguration_: 'AuthenticationConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-authenticationconfiguration""", alias="AuthenticationConfiguration")
    MSKClusterARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-mskclusterarn""", alias="MSKClusterARN")
    TopicName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-topicname""", alias="TopicName")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.MSKSourceConfiguration:
        from troposphere.kinesisfirehose import MSKSourceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OpenXJsonSerDe(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html
    Properties:
        - Name: ConvertDotsInJsonKeysToUnderscores
        - Name: ColumnToJsonKeyMappings
        - Name: CaseInsensitive
    
    """
    
    ConvertDotsInJsonKeysToUnderscores_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-convertdotsinjsonkeystounderscores""", alias="ConvertDotsInJsonKeysToUnderscores")
    ColumnToJsonKeyMappings_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-columntojsonkeymappings""", alias="ColumnToJsonKeyMappings")
    CaseInsensitive_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-caseinsensitive""", alias="CaseInsensitive")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.OpenXJsonSerDe:
        from troposphere.kinesisfirehose import OpenXJsonSerDe as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OrcSerDe(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html
    Properties:
        - Name: PaddingTolerance
        - Name: Compression
        - Name: StripeSizeBytes
        - Name: BloomFilterColumns
        - Name: BloomFilterFalsePositiveProbability
        - Name: EnablePadding
        - Name: FormatVersion
        - Name: RowIndexStride
        - Name: BlockSizeBytes
        - Name: DictionaryKeyThreshold
    
    """
    
    PaddingTolerance_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-paddingtolerance""", alias="PaddingTolerance")
    Compression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-compression""", alias="Compression")
    StripeSizeBytes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-stripesizebytes""", alias="StripeSizeBytes")
    BloomFilterColumns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-bloomfiltercolumns""", alias="BloomFilterColumns")
    BloomFilterFalsePositiveProbability_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-bloomfilterfalsepositiveprobability""", alias="BloomFilterFalsePositiveProbability")
    EnablePadding_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-enablepadding""", alias="EnablePadding")
    FormatVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-formatversion""", alias="FormatVersion")
    RowIndexStride_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-rowindexstride""", alias="RowIndexStride")
    BlockSizeBytes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-blocksizebytes""", alias="BlockSizeBytes")
    DictionaryKeyThreshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-dictionarykeythreshold""", alias="DictionaryKeyThreshold")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.OrcSerDe:
        from troposphere.kinesisfirehose import OrcSerDe as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputFormatConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-outputformatconfiguration.html
    Properties:
        - Name: Serializer
    
    """
    
    Serializer_: Optional['Serializer'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-outputformatconfiguration.html#cfn-kinesisfirehose-deliverystream-outputformatconfiguration-serializer""", alias="Serializer")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.OutputFormatConfiguration:
        from troposphere.kinesisfirehose import OutputFormatConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ParquetSerDe(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html
    Properties:
        - Name: Compression
        - Name: BlockSizeBytes
        - Name: EnableDictionaryCompression
        - Name: PageSizeBytes
        - Name: MaxPaddingBytes
        - Name: WriterVersion
    
    """
    
    Compression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-compression""", alias="Compression")
    BlockSizeBytes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-blocksizebytes""", alias="BlockSizeBytes")
    EnableDictionaryCompression_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-enabledictionarycompression""", alias="EnableDictionaryCompression")
    PageSizeBytes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-pagesizebytes""", alias="PageSizeBytes")
    MaxPaddingBytes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-maxpaddingbytes""", alias="MaxPaddingBytes")
    WriterVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-writerversion""", alias="WriterVersion")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.ParquetSerDe:
        from troposphere.kinesisfirehose import ParquetSerDe as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProcessingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html
    Properties:
        - Name: Enabled
        - Name: Processors
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html#cfn-kinesisfirehose-deliverystream-processingconfiguration-enabled""", alias="Enabled")
    Processors_: Optional[List['Processor']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html#cfn-kinesisfirehose-deliverystream-processingconfiguration-processors""", alias="Processors")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.ProcessingConfiguration:
        from troposphere.kinesisfirehose import ProcessingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Processor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html
    Properties:
        - Name: Type
        - Name: Parameters
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-type""", alias="Type")
    Parameters_: Optional[List['ProcessorParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-parameters""", alias="Parameters")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.Processor:
        from troposphere.kinesisfirehose import Processor as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProcessorParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html
    Properties:
        - Name: ParameterValue
        - Name: ParameterName
    
    """
    
    ParameterValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html#cfn-kinesisfirehose-deliverystream-processorparameter-parametervalue""", alias="ParameterValue")
    ParameterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html#cfn-kinesisfirehose-deliverystream-processorparameter-parametername""", alias="ParameterName")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.ProcessorParameter:
        from troposphere.kinesisfirehose import ProcessorParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RedshiftDestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html
    Properties:
        - Name: S3BackupConfiguration
        - Name: S3Configuration
        - Name: Username
        - Name: CopyCommand
        - Name: RetryOptions
        - Name: ProcessingConfiguration
        - Name: CloudWatchLoggingOptions
        - Name: ClusterJDBCURL
        - Name: RoleARN
        - Name: Password
        - Name: S3BackupMode
    
    """
    
    S3BackupConfiguration_: Optional['S3DestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3backupconfiguration""", alias="S3BackupConfiguration")
    S3Configuration_: 'S3DestinationConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3configuration""", alias="S3Configuration")
    Username_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-username""", alias="Username")
    CopyCommand_: 'CopyCommand' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-copycommand""", alias="CopyCommand")
    RetryOptions_: Optional['RedshiftRetryOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-retryoptions""", alias="RetryOptions")
    ProcessingConfiguration_: Optional['ProcessingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-processingconfiguration""", alias="ProcessingConfiguration")
    CloudWatchLoggingOptions_: Optional['CloudWatchLoggingOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-cloudwatchloggingoptions""", alias="CloudWatchLoggingOptions")
    ClusterJDBCURL_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-clusterjdbcurl""", alias="ClusterJDBCURL")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-rolearn""", alias="RoleARN")
    Password_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-password""", alias="Password")
    S3BackupMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3backupmode""", alias="S3BackupMode")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.RedshiftDestinationConfiguration:
        from troposphere.kinesisfirehose import RedshiftDestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RedshiftRetryOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions.html
    Properties:
        - Name: DurationInSeconds
    
    """
    
    DurationInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions.html#cfn-kinesisfirehose-deliverystream-redshiftretryoptions-durationinseconds""", alias="DurationInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.RedshiftRetryOptions:
        from troposphere.kinesisfirehose import RedshiftRetryOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RetryOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html
    Properties:
        - Name: DurationInSeconds
    
    """
    
    DurationInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html#cfn-kinesisfirehose-deliverystream-retryoptions-durationinseconds""", alias="DurationInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.RetryOptions:
        from troposphere.kinesisfirehose import RetryOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3DestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html
    Properties:
        - Name: ErrorOutputPrefix
        - Name: BucketARN
        - Name: BufferingHints
        - Name: CompressionFormat
        - Name: EncryptionConfiguration
        - Name: Prefix
        - Name: CloudWatchLoggingOptions
        - Name: RoleARN
    
    """
    
    ErrorOutputPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-erroroutputprefix""", alias="ErrorOutputPrefix")
    BucketARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-bucketarn""", alias="BucketARN")
    BufferingHints_: Optional['BufferingHints'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-bufferinghints""", alias="BufferingHints")
    CompressionFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-compressionformat""", alias="CompressionFormat")
    EncryptionConfiguration_: Optional['EncryptionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-encryptionconfiguration""", alias="EncryptionConfiguration")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-prefix""", alias="Prefix")
    CloudWatchLoggingOptions_: Optional['CloudWatchLoggingOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-cloudwatchloggingoptions""", alias="CloudWatchLoggingOptions")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-rolearn""", alias="RoleARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.S3DestinationConfiguration:
        from troposphere.kinesisfirehose import S3DestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SchemaConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html
    Properties:
        - Name: VersionId
        - Name: TableName
        - Name: DatabaseName
        - Name: Region
        - Name: CatalogId
        - Name: RoleARN
    
    """
    
    VersionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-versionid""", alias="VersionId")
    TableName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-tablename""", alias="TableName")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-databasename""", alias="DatabaseName")
    Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-region""", alias="Region")
    CatalogId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-catalogid""", alias="CatalogId")
    RoleARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-rolearn""", alias="RoleARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.SchemaConfiguration:
        from troposphere.kinesisfirehose import SchemaConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Serializer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html
    Properties:
        - Name: OrcSerDe
        - Name: ParquetSerDe
    
    """
    
    OrcSerDe_: Optional['OrcSerDe'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-orcserde""", alias="OrcSerDe")
    ParquetSerDe_: Optional['ParquetSerDe'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-parquetserde""", alias="ParquetSerDe")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.Serializer:
        from troposphere.kinesisfirehose import Serializer as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SplunkDestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html
    Properties:
        - Name: HECEndpoint
        - Name: S3Configuration
        - Name: HECToken
        - Name: RetryOptions
        - Name: HECEndpointType
        - Name: HECAcknowledgmentTimeoutInSeconds
        - Name: ProcessingConfiguration
        - Name: CloudWatchLoggingOptions
        - Name: S3BackupMode
    
    """
    
    HECEndpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecendpoint""", alias="HECEndpoint")
    S3Configuration_: 'S3DestinationConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-s3configuration""", alias="S3Configuration")
    HECToken_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hectoken""", alias="HECToken")
    RetryOptions_: Optional['SplunkRetryOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-retryoptions""", alias="RetryOptions")
    HECEndpointType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecendpointtype""", alias="HECEndpointType")
    HECAcknowledgmentTimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecacknowledgmenttimeoutinseconds""", alias="HECAcknowledgmentTimeoutInSeconds")
    ProcessingConfiguration_: Optional['ProcessingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-processingconfiguration""", alias="ProcessingConfiguration")
    CloudWatchLoggingOptions_: Optional['CloudWatchLoggingOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-cloudwatchloggingoptions""", alias="CloudWatchLoggingOptions")
    S3BackupMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-s3backupmode""", alias="S3BackupMode")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.SplunkDestinationConfiguration:
        from troposphere.kinesisfirehose import SplunkDestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SplunkRetryOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkretryoptions.html
    Properties:
        - Name: DurationInSeconds
    
    """
    
    DurationInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkretryoptions.html#cfn-kinesisfirehose-deliverystream-splunkretryoptions-durationinseconds""", alias="DurationInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.SplunkRetryOptions:
        from troposphere.kinesisfirehose import SplunkRetryOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html
    Properties:
        - Name: SubnetIds
        - Name: SecurityGroupIds
        - Name: RoleARN
    
    """
    
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-subnetids""", alias="SubnetIds")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-securitygroupids""", alias="SecurityGroupIds")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-rolearn""", alias="RoleARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.VpcConfiguration:
        from troposphere.kinesisfirehose import VpcConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class DeliveryStream(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html
    Properties:
        - Name: DeliveryStreamEncryptionConfigurationInput
        - Name: HttpEndpointDestinationConfiguration
        - Name: KinesisStreamSourceConfiguration
        - Name: DeliveryStreamType
        - Name: RedshiftDestinationConfiguration
        - Name: AmazonopensearchserviceDestinationConfiguration
        - Name: MSKSourceConfiguration
        - Name: SplunkDestinationConfiguration
        - Name: ExtendedS3DestinationConfiguration
        - Name: AmazonOpenSearchServerlessDestinationConfiguration
        - Name: ElasticsearchDestinationConfiguration
        - Name: S3DestinationConfiguration
        - Name: DeliveryStreamName
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DeliveryStreamEncryptionConfigurationInput_: Optional['DeliveryStreamEncryptionConfigurationInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput""", alias="DeliveryStreamEncryptionConfigurationInput")
    HttpEndpointDestinationConfiguration_: Optional['HttpEndpointDestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration""", alias="HttpEndpointDestinationConfiguration")
    KinesisStreamSourceConfiguration_: Optional['KinesisStreamSourceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration""", alias="KinesisStreamSourceConfiguration")
    DeliveryStreamType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamtype""", alias="DeliveryStreamType")
    RedshiftDestinationConfiguration_: Optional['RedshiftDestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration""", alias="RedshiftDestinationConfiguration")
    AmazonopensearchserviceDestinationConfiguration_: Optional['AmazonopensearchserviceDestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration""", alias="AmazonopensearchserviceDestinationConfiguration")
    MSKSourceConfiguration_: Optional['MSKSourceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-msksourceconfiguration""", alias="MSKSourceConfiguration")
    SplunkDestinationConfiguration_: Optional['SplunkDestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration""", alias="SplunkDestinationConfiguration")
    ExtendedS3DestinationConfiguration_: Optional['ExtendedS3DestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration""", alias="ExtendedS3DestinationConfiguration")
    AmazonOpenSearchServerlessDestinationConfiguration_: Optional['AmazonOpenSearchServerlessDestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration""", alias="AmazonOpenSearchServerlessDestinationConfiguration")
    ElasticsearchDestinationConfiguration_: Optional['ElasticsearchDestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration""", alias="ElasticsearchDestinationConfiguration")
    S3DestinationConfiguration_: Optional['S3DestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration""", alias="S3DestinationConfiguration")
    DeliveryStreamName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamname""", alias="DeliveryStreamName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.kinesisfirehose.DeliveryStream:
        from troposphere.kinesisfirehose import DeliveryStream as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kinesisfirehose import DeliveryStream as TropoT
        return resource_to_troposphere(self, TropoT)

