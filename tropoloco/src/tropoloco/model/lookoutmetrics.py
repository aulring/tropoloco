from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html
    Properties:
        - Name: LambdaConfiguration
        - Name: SNSConfiguration
    
    """
    
    LambdaConfiguration_: Optional['LambdaConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html#cfn-lookoutmetrics-alert-action-lambdaconfiguration""", alias="LambdaConfiguration")
    SNSConfiguration_: Optional['SNSConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html#cfn-lookoutmetrics-alert-action-snsconfiguration""", alias="SNSConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.Action:
        from troposphere.lookoutmetrics import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html
    Properties:
        - Name: LambdaArn
        - Name: RoleArn
    
    """
    
    LambdaArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html#cfn-lookoutmetrics-alert-lambdaconfiguration-lambdaarn""", alias="LambdaArn")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html#cfn-lookoutmetrics-alert-lambdaconfiguration-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.LambdaConfiguration:
        from troposphere.lookoutmetrics import LambdaConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SNSConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html
    Properties:
        - Name: SnsTopicArn
        - Name: RoleArn
    
    """
    
    SnsTopicArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html#cfn-lookoutmetrics-alert-snsconfiguration-snstopicarn""", alias="SnsTopicArn")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html#cfn-lookoutmetrics-alert-snsconfiguration-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.SNSConfiguration:
        from troposphere.lookoutmetrics import SNSConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnomalyDetectorConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-anomalydetectorconfig.html
    Properties:
        - Name: AnomalyDetectorFrequency
    
    """
    
    AnomalyDetectorFrequency_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-anomalydetectorconfig.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorconfig-anomalydetectorfrequency""", alias="AnomalyDetectorFrequency")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.AnomalyDetectorConfig:
        from troposphere.lookoutmetrics import AnomalyDetectorConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AppFlowConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html
    Properties:
        - Name: FlowName
        - Name: RoleArn
    
    """
    
    FlowName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html#cfn-lookoutmetrics-anomalydetector-appflowconfig-flowname""", alias="FlowName")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html#cfn-lookoutmetrics-anomalydetector-appflowconfig-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.AppFlowConfig:
        from troposphere.lookoutmetrics import AppFlowConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudwatchConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-cloudwatchconfig.html
    Properties:
        - Name: RoleArn
    
    """
    
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-cloudwatchconfig.html#cfn-lookoutmetrics-anomalydetector-cloudwatchconfig-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.CloudwatchConfig:
        from troposphere.lookoutmetrics import CloudwatchConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CsvFormatDescriptor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html
    Properties:
        - Name: QuoteSymbol
        - Name: ContainsHeader
        - Name: Delimiter
        - Name: HeaderList
        - Name: Charset
        - Name: FileCompression
    
    """
    
    QuoteSymbol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-quotesymbol""", alias="QuoteSymbol")
    ContainsHeader_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-containsheader""", alias="ContainsHeader")
    Delimiter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-delimiter""", alias="Delimiter")
    HeaderList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-headerlist""", alias="HeaderList")
    Charset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-charset""", alias="Charset")
    FileCompression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-filecompression""", alias="FileCompression")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.CsvFormatDescriptor:
        from troposphere.lookoutmetrics import CsvFormatDescriptor as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FileFormatDescriptor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html
    Properties:
        - Name: JsonFormatDescriptor
        - Name: CsvFormatDescriptor
    
    """
    
    JsonFormatDescriptor_: Optional['JsonFormatDescriptor'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-fileformatdescriptor-jsonformatdescriptor""", alias="JsonFormatDescriptor")
    CsvFormatDescriptor_: Optional['CsvFormatDescriptor'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-fileformatdescriptor-csvformatdescriptor""", alias="CsvFormatDescriptor")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.FileFormatDescriptor:
        from troposphere.lookoutmetrics import FileFormatDescriptor as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JsonFormatDescriptor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html
    Properties:
        - Name: Charset
        - Name: FileCompression
    
    """
    
    Charset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-jsonformatdescriptor-charset""", alias="Charset")
    FileCompression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-jsonformatdescriptor-filecompression""", alias="FileCompression")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.JsonFormatDescriptor:
        from troposphere.lookoutmetrics import JsonFormatDescriptor as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Metric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html
    Properties:
        - Name: AggregationFunction
        - Name: MetricName
        - Name: Namespace
    
    """
    
    AggregationFunction_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-aggregationfunction""", alias="AggregationFunction")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-metricname""", alias="MetricName")
    Namespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.Metric:
        from troposphere.lookoutmetrics import Metric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html
    Properties:
        - Name: Timezone
        - Name: MetricSetDescription
        - Name: MetricList
        - Name: MetricSource
        - Name: TimestampColumn
        - Name: DimensionList
        - Name: MetricSetFrequency
        - Name: MetricSetName
        - Name: Offset
    
    """
    
    Timezone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-timezone""", alias="Timezone")
    MetricSetDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetdescription""", alias="MetricSetDescription")
    MetricList_: List['Metric'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metriclist""", alias="MetricList")
    MetricSource_: 'MetricSource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsource""", alias="MetricSource")
    TimestampColumn_: Optional['TimestampColumn'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-timestampcolumn""", alias="TimestampColumn")
    DimensionList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-dimensionlist""", alias="DimensionList")
    MetricSetFrequency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetfrequency""", alias="MetricSetFrequency")
    MetricSetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetname""", alias="MetricSetName")
    Offset_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-offset""", alias="Offset")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.MetricSet:
        from troposphere.lookoutmetrics import MetricSet as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html
    Properties:
        - Name: S3SourceConfig
        - Name: CloudwatchConfig
        - Name: RDSSourceConfig
        - Name: AppFlowConfig
        - Name: RedshiftSourceConfig
    
    """
    
    S3SourceConfig_: Optional['S3SourceConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-s3sourceconfig""", alias="S3SourceConfig")
    CloudwatchConfig_: Optional['CloudwatchConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-cloudwatchconfig""", alias="CloudwatchConfig")
    RDSSourceConfig_: Optional['RDSSourceConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-rdssourceconfig""", alias="RDSSourceConfig")
    AppFlowConfig_: Optional['AppFlowConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-appflowconfig""", alias="AppFlowConfig")
    RedshiftSourceConfig_: Optional['RedshiftSourceConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-redshiftsourceconfig""", alias="RedshiftSourceConfig")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.MetricSource:
        from troposphere.lookoutmetrics import MetricSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RDSSourceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html
    Properties:
        - Name: TableName
        - Name: DatabasePort
        - Name: DatabaseHost
        - Name: DatabaseName
        - Name: SecretManagerArn
        - Name: VpcConfiguration
        - Name: DBInstanceIdentifier
        - Name: RoleArn
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-tablename""", alias="TableName")
    DatabasePort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databaseport""", alias="DatabasePort")
    DatabaseHost_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databasehost""", alias="DatabaseHost")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databasename""", alias="DatabaseName")
    SecretManagerArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-secretmanagerarn""", alias="SecretManagerArn")
    VpcConfiguration_: 'VpcConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-vpcconfiguration""", alias="VpcConfiguration")
    DBInstanceIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-dbinstanceidentifier""", alias="DBInstanceIdentifier")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.RDSSourceConfig:
        from troposphere.lookoutmetrics import RDSSourceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RedshiftSourceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html
    Properties:
        - Name: TableName
        - Name: DatabasePort
        - Name: DatabaseHost
        - Name: DatabaseName
        - Name: SecretManagerArn
        - Name: VpcConfiguration
        - Name: ClusterIdentifier
        - Name: RoleArn
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-tablename""", alias="TableName")
    DatabasePort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databaseport""", alias="DatabasePort")
    DatabaseHost_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databasehost""", alias="DatabaseHost")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databasename""", alias="DatabaseName")
    SecretManagerArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-secretmanagerarn""", alias="SecretManagerArn")
    VpcConfiguration_: 'VpcConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-vpcconfiguration""", alias="VpcConfiguration")
    ClusterIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-clusteridentifier""", alias="ClusterIdentifier")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.RedshiftSourceConfig:
        from troposphere.lookoutmetrics import RedshiftSourceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3SourceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html
    Properties:
        - Name: TemplatedPathList
        - Name: HistoricalDataPathList
        - Name: RoleArn
        - Name: FileFormatDescriptor
    
    """
    
    TemplatedPathList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-templatedpathlist""", alias="TemplatedPathList")
    HistoricalDataPathList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-historicaldatapathlist""", alias="HistoricalDataPathList")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-rolearn""", alias="RoleArn")
    FileFormatDescriptor_: 'FileFormatDescriptor' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-fileformatdescriptor""", alias="FileFormatDescriptor")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.S3SourceConfig:
        from troposphere.lookoutmetrics import S3SourceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimestampColumn(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html
    Properties:
        - Name: ColumnName
        - Name: ColumnFormat
    
    """
    
    ColumnName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html#cfn-lookoutmetrics-anomalydetector-timestampcolumn-columnname""", alias="ColumnName")
    ColumnFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html#cfn-lookoutmetrics-anomalydetector-timestampcolumn-columnformat""", alias="ColumnFormat")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.TimestampColumn:
        from troposphere.lookoutmetrics import TimestampColumn as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html
    Properties:
        - Name: SubnetIdList
        - Name: SecurityGroupIdList
    
    """
    
    SubnetIdList_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html#cfn-lookoutmetrics-anomalydetector-vpcconfiguration-subnetidlist""", alias="SubnetIdList")
    SecurityGroupIdList_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html#cfn-lookoutmetrics-anomalydetector-vpcconfiguration-securitygroupidlist""", alias="SecurityGroupIdList")
    


    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.VpcConfiguration:
        from troposphere.lookoutmetrics import VpcConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Alert(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html
    Properties:
        - Name: AlertDescription
        - Name: Action
        - Name: AlertName
        - Name: AlertSensitivityThreshold
        - Name: AnomalyDetectorArn
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AlertDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertdescription""", alias="AlertDescription")
    Action_: 'Action' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-action""", alias="Action")
    AlertName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertname""", alias="AlertName")
    AlertSensitivityThreshold_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertsensitivitythreshold""", alias="AlertSensitivityThreshold")
    AnomalyDetectorArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-anomalydetectorarn""", alias="AnomalyDetectorArn")
    

    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.Alert:
        from troposphere.lookoutmetrics import Alert as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lookoutmetrics import Alert as TropoT
        return resource_to_troposphere(self, TropoT)


class AnomalyDetector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html
    Properties:
        - Name: AnomalyDetectorName
        - Name: KmsKeyArn
        - Name: AnomalyDetectorDescription
        - Name: AnomalyDetectorConfig
        - Name: MetricSetList
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AnomalyDetectorName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorname""", alias="AnomalyDetectorName")
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-kmskeyarn""", alias="KmsKeyArn")
    AnomalyDetectorDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectordescription""", alias="AnomalyDetectorDescription")
    AnomalyDetectorConfig_: 'AnomalyDetectorConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorconfig""", alias="AnomalyDetectorConfig")
    MetricSetList_: List['MetricSet'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-metricsetlist""", alias="MetricSetList")
    

    @property
    def tropo_type(self) -> troposphere.lookoutmetrics.AnomalyDetector:
        from troposphere.lookoutmetrics import AnomalyDetector as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lookoutmetrics import AnomalyDetector as TropoT
        return resource_to_troposphere(self, TropoT)

