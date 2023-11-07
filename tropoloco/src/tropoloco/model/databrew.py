from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CsvOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-csvoptions.html
    Properties:
        - Name: Delimiter
        - Name: HeaderRow
    
    """
    
    Delimiter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-csvoptions.html#cfn-databrew-dataset-csvoptions-delimiter""", alias="Delimiter")
    HeaderRow_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-csvoptions.html#cfn-databrew-dataset-csvoptions-headerrow""", alias="HeaderRow")
    


    @property
    def tropo_type(self) -> troposphere.databrew.CsvOptions:
        from troposphere.databrew import CsvOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataCatalogInputDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html
    Properties:
        - Name: TableName
        - Name: TempDirectory
        - Name: DatabaseName
        - Name: CatalogId
    
    """
    
    TableName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html#cfn-databrew-dataset-datacataloginputdefinition-tablename""", alias="TableName")
    TempDirectory_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html#cfn-databrew-dataset-datacataloginputdefinition-tempdirectory""", alias="TempDirectory")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html#cfn-databrew-dataset-datacataloginputdefinition-databasename""", alias="DatabaseName")
    CatalogId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html#cfn-databrew-dataset-datacataloginputdefinition-catalogid""", alias="CatalogId")
    


    @property
    def tropo_type(self) -> troposphere.databrew.DataCatalogInputDefinition:
        from troposphere.databrew import DataCatalogInputDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatabaseInputDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html
    Properties:
        - Name: TempDirectory
        - Name: QueryString
        - Name: GlueConnectionName
        - Name: DatabaseTableName
    
    """
    
    TempDirectory_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html#cfn-databrew-dataset-databaseinputdefinition-tempdirectory""", alias="TempDirectory")
    QueryString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html#cfn-databrew-dataset-databaseinputdefinition-querystring""", alias="QueryString")
    GlueConnectionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html#cfn-databrew-dataset-databaseinputdefinition-glueconnectionname""", alias="GlueConnectionName")
    DatabaseTableName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html#cfn-databrew-dataset-databaseinputdefinition-databasetablename""", alias="DatabaseTableName")
    


    @property
    def tropo_type(self) -> troposphere.databrew.DatabaseInputDefinition:
        from troposphere.databrew import DatabaseInputDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatasetParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html
    Properties:
        - Name: Type
        - Name: DatetimeOptions
        - Name: Filter
        - Name: CreateColumn
        - Name: Name
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html#cfn-databrew-dataset-datasetparameter-type""", alias="Type")
    DatetimeOptions_: Optional['DatetimeOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html#cfn-databrew-dataset-datasetparameter-datetimeoptions""", alias="DatetimeOptions")
    Filter_: Optional['FilterExpression'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html#cfn-databrew-dataset-datasetparameter-filter""", alias="Filter")
    CreateColumn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html#cfn-databrew-dataset-datasetparameter-createcolumn""", alias="CreateColumn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html#cfn-databrew-dataset-datasetparameter-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.databrew.DatasetParameter:
        from troposphere.databrew import DatasetParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatetimeOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html
    Properties:
        - Name: LocaleCode
        - Name: Format
        - Name: TimezoneOffset
    
    """
    
    LocaleCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html#cfn-databrew-dataset-datetimeoptions-localecode""", alias="LocaleCode")
    Format_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html#cfn-databrew-dataset-datetimeoptions-format""", alias="Format")
    TimezoneOffset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html#cfn-databrew-dataset-datetimeoptions-timezoneoffset""", alias="TimezoneOffset")
    


    @property
    def tropo_type(self) -> troposphere.databrew.DatetimeOptions:
        from troposphere.databrew import DatetimeOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExcelOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html
    Properties:
        - Name: HeaderRow
        - Name: SheetNames
        - Name: SheetIndexes
    
    """
    
    HeaderRow_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html#cfn-databrew-dataset-exceloptions-headerrow""", alias="HeaderRow")
    SheetNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html#cfn-databrew-dataset-exceloptions-sheetnames""", alias="SheetNames")
    SheetIndexes_: Optional[List[int]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html#cfn-databrew-dataset-exceloptions-sheetindexes""", alias="SheetIndexes")
    


    @property
    def tropo_type(self) -> troposphere.databrew.ExcelOptions:
        from troposphere.databrew import ExcelOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FilesLimit(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html
    Properties:
        - Name: Order
        - Name: OrderedBy
        - Name: MaxFiles
    
    """
    
    Order_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html#cfn-databrew-dataset-fileslimit-order""", alias="Order")
    OrderedBy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html#cfn-databrew-dataset-fileslimit-orderedby""", alias="OrderedBy")
    MaxFiles_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html#cfn-databrew-dataset-fileslimit-maxfiles""", alias="MaxFiles")
    


    @property
    def tropo_type(self) -> troposphere.databrew.FilesLimit:
        from troposphere.databrew import FilesLimit as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FilterExpression(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filterexpression.html
    Properties:
        - Name: Expression
        - Name: ValuesMap
    
    """
    
    Expression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filterexpression.html#cfn-databrew-dataset-filterexpression-expression""", alias="Expression")
    ValuesMap_: List['FilterValue'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filterexpression.html#cfn-databrew-dataset-filterexpression-valuesmap""", alias="ValuesMap")
    


    @property
    def tropo_type(self) -> troposphere.databrew.FilterExpression:
        from troposphere.databrew import FilterExpression as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FilterValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filtervalue.html
    Properties:
        - Name: Value
        - Name: ValueReference
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filtervalue.html#cfn-databrew-dataset-filtervalue-value""", alias="Value")
    ValueReference_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filtervalue.html#cfn-databrew-dataset-filtervalue-valuereference""", alias="ValueReference")
    


    @property
    def tropo_type(self) -> troposphere.databrew.FilterValue:
        from troposphere.databrew import FilterValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FormatOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html
    Properties:
        - Name: Excel
        - Name: Csv
        - Name: Json
    
    """
    
    Excel_: Optional['ExcelOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html#cfn-databrew-dataset-formatoptions-excel""", alias="Excel")
    Csv_: Optional['CsvOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html#cfn-databrew-dataset-formatoptions-csv""", alias="Csv")
    Json_: Optional['JsonOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html#cfn-databrew-dataset-formatoptions-json""", alias="Json")
    


    @property
    def tropo_type(self) -> troposphere.databrew.FormatOptions:
        from troposphere.databrew import FormatOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Input(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html
    Properties:
        - Name: DatabaseInputDefinition
        - Name: S3InputDefinition
        - Name: Metadata
        - Name: DataCatalogInputDefinition
    
    """
    
    DatabaseInputDefinition_: Optional['DatabaseInputDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html#cfn-databrew-dataset-input-databaseinputdefinition""", alias="DatabaseInputDefinition")
    S3InputDefinition_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html#cfn-databrew-dataset-input-s3inputdefinition""", alias="S3InputDefinition")
    Metadata_: Optional['Metadata'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html#cfn-databrew-dataset-input-metadata""", alias="Metadata")
    DataCatalogInputDefinition_: Optional['DataCatalogInputDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html#cfn-databrew-dataset-input-datacataloginputdefinition""", alias="DataCatalogInputDefinition")
    


    @property
    def tropo_type(self) -> troposphere.databrew.Input:
        from troposphere.databrew import Input as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JsonOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-jsonoptions.html
    Properties:
        - Name: MultiLine
    
    """
    
    MultiLine_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-jsonoptions.html#cfn-databrew-dataset-jsonoptions-multiline""", alias="MultiLine")
    


    @property
    def tropo_type(self) -> troposphere.databrew.JsonOptions:
        from troposphere.databrew import JsonOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Metadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-metadata.html
    Properties:
        - Name: SourceArn
    
    """
    
    SourceArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-metadata.html#cfn-databrew-dataset-metadata-sourcearn""", alias="SourceArn")
    


    @property
    def tropo_type(self) -> troposphere.databrew.Metadata:
        from troposphere.databrew import Metadata as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PathOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html
    Properties:
        - Name: Parameters
        - Name: LastModifiedDateCondition
        - Name: FilesLimit
    
    """
    
    Parameters_: Optional[List['PathParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html#cfn-databrew-dataset-pathoptions-parameters""", alias="Parameters")
    LastModifiedDateCondition_: Optional['FilterExpression'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html#cfn-databrew-dataset-pathoptions-lastmodifieddatecondition""", alias="LastModifiedDateCondition")
    FilesLimit_: Optional['FilesLimit'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html#cfn-databrew-dataset-pathoptions-fileslimit""", alias="FilesLimit")
    


    @property
    def tropo_type(self) -> troposphere.databrew.PathOptions:
        from troposphere.databrew import PathOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PathParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathparameter.html
    Properties:
        - Name: PathParameterName
        - Name: DatasetParameter
    
    """
    
    PathParameterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathparameter.html#cfn-databrew-dataset-pathparameter-pathparametername""", alias="PathParameterName")
    DatasetParameter_: 'DatasetParameter' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathparameter.html#cfn-databrew-dataset-pathparameter-datasetparameter""", alias="DatasetParameter")
    


    @property
    def tropo_type(self) -> troposphere.databrew.PathParameter:
        from troposphere.databrew import PathParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-s3location.html
    Properties:
        - Name: Bucket
        - Name: Key
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-s3location.html#cfn-databrew-dataset-s3location-bucket""", alias="Bucket")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-s3location.html#cfn-databrew-dataset-s3location-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.databrew.S3Location:
        from troposphere.databrew import S3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AllowedStatistics(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-allowedstatistics.html
    Properties:
        - Name: Statistics
    
    """
    
    Statistics_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-allowedstatistics.html#cfn-databrew-job-allowedstatistics-statistics""", alias="Statistics")
    


    @property
    def tropo_type(self) -> troposphere.databrew.AllowedStatistics:
        from troposphere.databrew import AllowedStatistics as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ColumnSelector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnselector.html
    Properties:
        - Name: Regex
        - Name: Name
    
    """
    
    Regex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnselector.html#cfn-databrew-job-columnselector-regex""", alias="Regex")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnselector.html#cfn-databrew-job-columnselector-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.databrew.ColumnSelector:
        from troposphere.databrew import ColumnSelector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ColumnStatisticsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnstatisticsconfiguration.html
    Properties:
        - Name: Statistics
        - Name: Selectors
    
    """
    
    Statistics_: 'StatisticsConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnstatisticsconfiguration.html#cfn-databrew-job-columnstatisticsconfiguration-statistics""", alias="Statistics")
    Selectors_: Optional[List['ColumnSelector']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnstatisticsconfiguration.html#cfn-databrew-job-columnstatisticsconfiguration-selectors""", alias="Selectors")
    


    @property
    def tropo_type(self) -> troposphere.databrew.ColumnStatisticsConfiguration:
        from troposphere.databrew import ColumnStatisticsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CsvOutputOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-csvoutputoptions.html
    Properties:
        - Name: Delimiter
    
    """
    
    Delimiter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-csvoutputoptions.html#cfn-databrew-job-csvoutputoptions-delimiter""", alias="Delimiter")
    


    @property
    def tropo_type(self) -> troposphere.databrew.CsvOutputOptions:
        from troposphere.databrew import CsvOutputOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataCatalogOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html
    Properties:
        - Name: TableName
        - Name: Overwrite
        - Name: S3Options
        - Name: DatabaseOptions
        - Name: DatabaseName
        - Name: CatalogId
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html#cfn-databrew-job-datacatalogoutput-tablename""", alias="TableName")
    Overwrite_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html#cfn-databrew-job-datacatalogoutput-overwrite""", alias="Overwrite")
    S3Options_: Optional['S3TableOutputOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html#cfn-databrew-job-datacatalogoutput-s3options""", alias="S3Options")
    DatabaseOptions_: Optional['DatabaseTableOutputOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html#cfn-databrew-job-datacatalogoutput-databaseoptions""", alias="DatabaseOptions")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html#cfn-databrew-job-datacatalogoutput-databasename""", alias="DatabaseName")
    CatalogId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html#cfn-databrew-job-datacatalogoutput-catalogid""", alias="CatalogId")
    


    @property
    def tropo_type(self) -> troposphere.databrew.DataCatalogOutput:
        from troposphere.databrew import DataCatalogOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatabaseOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databaseoutput.html
    Properties:
        - Name: DatabaseOutputMode
        - Name: DatabaseOptions
        - Name: GlueConnectionName
    
    """
    
    DatabaseOutputMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databaseoutput.html#cfn-databrew-job-databaseoutput-databaseoutputmode""", alias="DatabaseOutputMode")
    DatabaseOptions_: 'DatabaseTableOutputOptions' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databaseoutput.html#cfn-databrew-job-databaseoutput-databaseoptions""", alias="DatabaseOptions")
    GlueConnectionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databaseoutput.html#cfn-databrew-job-databaseoutput-glueconnectionname""", alias="GlueConnectionName")
    


    @property
    def tropo_type(self) -> troposphere.databrew.DatabaseOutput:
        from troposphere.databrew import DatabaseOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatabaseTableOutputOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databasetableoutputoptions.html
    Properties:
        - Name: TempDirectory
        - Name: TableName
    
    """
    
    TempDirectory_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databasetableoutputoptions.html#cfn-databrew-job-databasetableoutputoptions-tempdirectory""", alias="TempDirectory")
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databasetableoutputoptions.html#cfn-databrew-job-databasetableoutputoptions-tablename""", alias="TableName")
    


    @property
    def tropo_type(self) -> troposphere.databrew.DatabaseTableOutputOptions:
        from troposphere.databrew import DatabaseTableOutputOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EntityDetectorConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-entitydetectorconfiguration.html
    Properties:
        - Name: EntityTypes
        - Name: AllowedStatistics
    
    """
    
    EntityTypes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-entitydetectorconfiguration.html#cfn-databrew-job-entitydetectorconfiguration-entitytypes""", alias="EntityTypes")
    AllowedStatistics_: Optional['AllowedStatistics'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-entitydetectorconfiguration.html#cfn-databrew-job-entitydetectorconfiguration-allowedstatistics""", alias="AllowedStatistics")
    


    @property
    def tropo_type(self) -> troposphere.databrew.EntityDetectorConfiguration:
        from troposphere.databrew import EntityDetectorConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JobSample(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-jobsample.html
    Properties:
        - Name: Size
        - Name: Mode
    
    """
    
    Size_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-jobsample.html#cfn-databrew-job-jobsample-size""", alias="Size")
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-jobsample.html#cfn-databrew-job-jobsample-mode""", alias="Mode")
    


    @property
    def tropo_type(self) -> troposphere.databrew.JobSample:
        from troposphere.databrew import JobSample as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Output(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html
    Properties:
        - Name: Overwrite
        - Name: Format
        - Name: MaxOutputFiles
        - Name: CompressionFormat
        - Name: PartitionColumns
        - Name: FormatOptions
        - Name: Location
    
    """
    
    Overwrite_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-overwrite""", alias="Overwrite")
    Format_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-format""", alias="Format")
    MaxOutputFiles_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-maxoutputfiles""", alias="MaxOutputFiles")
    CompressionFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-compressionformat""", alias="CompressionFormat")
    PartitionColumns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-partitioncolumns""", alias="PartitionColumns")
    FormatOptions_: Optional['OutputFormatOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-formatoptions""", alias="FormatOptions")
    Location_: 'S3Location' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html#cfn-databrew-job-output-location""", alias="Location")
    


    @property
    def tropo_type(self) -> troposphere.databrew.Output:
        from troposphere.databrew import Output as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputFormatOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputformatoptions.html
    Properties:
        - Name: Csv
    
    """
    
    Csv_: Optional['CsvOutputOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputformatoptions.html#cfn-databrew-job-outputformatoptions-csv""", alias="Csv")
    


    @property
    def tropo_type(self) -> troposphere.databrew.OutputFormatOptions:
        from troposphere.databrew import OutputFormatOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html
    Properties:
        - Name: Bucket
        - Name: BucketOwner
        - Name: Key
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html#cfn-databrew-job-outputlocation-bucket""", alias="Bucket")
    BucketOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html#cfn-databrew-job-outputlocation-bucketowner""", alias="BucketOwner")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html#cfn-databrew-job-outputlocation-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.databrew.OutputLocation:
        from troposphere.databrew import OutputLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProfileConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html
    Properties:
        - Name: ProfileColumns
        - Name: DatasetStatisticsConfiguration
        - Name: ColumnStatisticsConfigurations
        - Name: EntityDetectorConfiguration
    
    """
    
    ProfileColumns_: Optional[List['ColumnSelector']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html#cfn-databrew-job-profileconfiguration-profilecolumns""", alias="ProfileColumns")
    DatasetStatisticsConfiguration_: Optional['StatisticsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html#cfn-databrew-job-profileconfiguration-datasetstatisticsconfiguration""", alias="DatasetStatisticsConfiguration")
    ColumnStatisticsConfigurations_: Optional[List['ColumnStatisticsConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html#cfn-databrew-job-profileconfiguration-columnstatisticsconfigurations""", alias="ColumnStatisticsConfigurations")
    EntityDetectorConfiguration_: Optional['EntityDetectorConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html#cfn-databrew-job-profileconfiguration-entitydetectorconfiguration""", alias="EntityDetectorConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.databrew.ProfileConfiguration:
        from troposphere.databrew import ProfileConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Recipe(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-recipe.html
    Properties:
        - Name: Version
        - Name: Name
    
    """
    
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-recipe.html#cfn-databrew-job-recipe-version""", alias="Version")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-recipe.html#cfn-databrew-job-recipe-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.databrew.Recipe:
        from troposphere.databrew import Recipe as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html
    Properties:
        - Name: Bucket
        - Name: BucketOwner
        - Name: Key
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html#cfn-databrew-job-s3location-bucket""", alias="Bucket")
    BucketOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html#cfn-databrew-job-s3location-bucketowner""", alias="BucketOwner")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html#cfn-databrew-job-s3location-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.databrew.S3Location:
        from troposphere.databrew import S3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3TableOutputOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3tableoutputoptions.html
    Properties:
        - Name: Location
    
    """
    
    Location_: 'S3Location' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3tableoutputoptions.html#cfn-databrew-job-s3tableoutputoptions-location""", alias="Location")
    


    @property
    def tropo_type(self) -> troposphere.databrew.S3TableOutputOptions:
        from troposphere.databrew import S3TableOutputOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatisticOverride(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticoverride.html
    Properties:
        - Name: Parameters
        - Name: Statistic
    
    """
    
    Parameters_: Dict[str, str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticoverride.html#cfn-databrew-job-statisticoverride-parameters""", alias="Parameters")
    Statistic_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticoverride.html#cfn-databrew-job-statisticoverride-statistic""", alias="Statistic")
    


    @property
    def tropo_type(self) -> troposphere.databrew.StatisticOverride:
        from troposphere.databrew import StatisticOverride as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatisticsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticsconfiguration.html
    Properties:
        - Name: IncludedStatistics
        - Name: Overrides
    
    """
    
    IncludedStatistics_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticsconfiguration.html#cfn-databrew-job-statisticsconfiguration-includedstatistics""", alias="IncludedStatistics")
    Overrides_: Optional[List['StatisticOverride']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticsconfiguration.html#cfn-databrew-job-statisticsconfiguration-overrides""", alias="Overrides")
    


    @property
    def tropo_type(self) -> troposphere.databrew.StatisticsConfiguration:
        from troposphere.databrew import StatisticsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ValidationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-validationconfiguration.html
    Properties:
        - Name: RulesetArn
        - Name: ValidationMode
    
    """
    
    RulesetArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-validationconfiguration.html#cfn-databrew-job-validationconfiguration-rulesetarn""", alias="RulesetArn")
    ValidationMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-validationconfiguration.html#cfn-databrew-job-validationconfiguration-validationmode""", alias="ValidationMode")
    


    @property
    def tropo_type(self) -> troposphere.databrew.ValidationConfiguration:
        from troposphere.databrew import ValidationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Sample(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-project-sample.html
    Properties:
        - Name: Type
        - Name: Size
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-project-sample.html#cfn-databrew-project-sample-type""", alias="Type")
    Size_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-project-sample.html#cfn-databrew-project-sample-size""", alias="Size")
    


    @property
    def tropo_type(self) -> troposphere.databrew.Sample:
        from troposphere.databrew import Sample as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html
    Properties:
        - Name: Parameters
        - Name: Operation
    
    """
    
    Parameters_: Optional['RecipeParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html#cfn-databrew-recipe-action-parameters""", alias="Parameters")
    Operation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html#cfn-databrew-recipe-action-operation""", alias="Operation")
    


    @property
    def tropo_type(self) -> troposphere.databrew.Action:
        from troposphere.databrew import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConditionExpression(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html
    Properties:
        - Name: Condition
        - Name: Value
        - Name: TargetColumn
    
    """
    
    Condition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html#cfn-databrew-recipe-conditionexpression-condition""", alias="Condition")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html#cfn-databrew-recipe-conditionexpression-value""", alias="Value")
    TargetColumn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html#cfn-databrew-recipe-conditionexpression-targetcolumn""", alias="TargetColumn")
    


    @property
    def tropo_type(self) -> troposphere.databrew.ConditionExpression:
        from troposphere.databrew import ConditionExpression as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataCatalogInputDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html
    Properties:
        - Name: TableName
        - Name: TempDirectory
        - Name: DatabaseName
        - Name: CatalogId
    
    """
    
    TableName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html#cfn-databrew-recipe-datacataloginputdefinition-tablename""", alias="TableName")
    TempDirectory_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html#cfn-databrew-recipe-datacataloginputdefinition-tempdirectory""", alias="TempDirectory")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html#cfn-databrew-recipe-datacataloginputdefinition-databasename""", alias="DatabaseName")
    CatalogId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html#cfn-databrew-recipe-datacataloginputdefinition-catalogid""", alias="CatalogId")
    


    @property
    def tropo_type(self) -> troposphere.databrew.DataCatalogInputDefinition:
        from troposphere.databrew import DataCatalogInputDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Input(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-input.html
    Properties:
        - Name: S3InputDefinition
        - Name: DataCatalogInputDefinition
    
    """
    
    S3InputDefinition_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-input.html#cfn-databrew-recipe-input-s3inputdefinition""", alias="S3InputDefinition")
    DataCatalogInputDefinition_: Optional['DataCatalogInputDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-input.html#cfn-databrew-recipe-input-datacataloginputdefinition""", alias="DataCatalogInputDefinition")
    


    @property
    def tropo_type(self) -> troposphere.databrew.Input:
        from troposphere.databrew import Input as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecipeParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html
    Properties:
        - Name: IgnoreCase
        - Name: PatternOptions
        - Name: Count
        - Name: OrderByColumn
        - Name: UpperBound
        - Name: JoinKeys
        - Name: RemoveLeadingAndTrailingPunctuation
        - Name: StepIndex
        - Name: GroupByAggFunctionOptions
        - Name: Position
        - Name: StopWordsMode
        - Name: SourceColumn
        - Name: CustomCharacters
        - Name: TimeZone
        - Name: RemoveLeadingAndTrailingQuotes
        - Name: SourceColumn2
        - Name: CollapseConsecutiveWhitespace
        - Name: NumRowsAfter
        - Name: RemoveLetters
        - Name: SourceColumn1
        - Name: UseNewDataFrame
        - Name: Interval
        - Name: LowerBound
        - Name: TokenizerPattern
        - Name: LeftColumns
        - Name: CharsToRemove
        - Name: Value1
        - Name: DeleteOtherRows
        - Name: Value2
        - Name: CategoryMap
        - Name: StartPattern
        - Name: StartPosition
        - Name: SheetIndexes
        - Name: TargetIndex
        - Name: RemoveSourceColumn
        - Name: DateTimeParameters
        - Name: EndValue
        - Name: RemoveCustomCharacters
        - Name: EndPosition
        - Name: Pattern
        - Name: Delimiter
        - Name: RemoveSpecialCharacters
        - Name: RemoveAllQuotes
        - Name: EndPattern
        - Name: StartColumnIndex
        - Name: ModeType
        - Name: SecondaryInputs
        - Name: SampleType
        - Name: DateTimeFormat
        - Name: Other
        - Name: CaseStatement
        - Name: FalseString
        - Name: RemoveAllPunctuation
        - Name: CustomStopWords
        - Name: MapType
        - Name: ColumnRange
        - Name: CustomValue
        - Name: Input
        - Name: StepCount
        - Name: TargetDateFormat
        - Name: SecondInput
        - Name: GroupByColumns
        - Name: NumRowsBefore
        - Name: IsText
        - Name: TargetColumn
        - Name: RemoveNumbers
        - Name: Period
        - Name: NumRows
        - Name: RightColumns
        - Name: StemmingMode
        - Name: Units
        - Name: SampleSize
        - Name: IncludeInSplit
        - Name: AggregateFunction
        - Name: Value
        - Name: Exponent
        - Name: StartValue
        - Name: PatternOption2
        - Name: RemoveCustomValue
        - Name: PatternOption1
        - Name: MultiLine
        - Name: TrueString
        - Name: RemoveLeadingAndTrailingWhitespace
        - Name: HiddenColumns
        - Name: RemoveAllWhitespace
        - Name: ViewFrame
        - Name: ColumnDataType
        - Name: JoinType
        - Name: Base
        - Name: ValueColumn
        - Name: DatasetsColumns
        - Name: UdfLang
        - Name: TargetColumnNames
        - Name: DateAddValue
        - Name: ExpandContractions
        - Name: UnpivotColumn
        - Name: Strategy
        - Name: SheetNames
        - Name: Limit
        - Name: OrderByColumns
        - Name: SourceColumns
    
    """
    
    IgnoreCase_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-ignorecase""", alias="IgnoreCase")
    PatternOptions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-patternoptions""", alias="PatternOptions")
    Count_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-count""", alias="Count")
    OrderByColumn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-orderbycolumn""", alias="OrderByColumn")
    UpperBound_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-upperbound""", alias="UpperBound")
    JoinKeys_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-joinkeys""", alias="JoinKeys")
    RemoveLeadingAndTrailingPunctuation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeleadingandtrailingpunctuation""", alias="RemoveLeadingAndTrailingPunctuation")
    StepIndex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-stepindex""", alias="StepIndex")
    GroupByAggFunctionOptions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-groupbyaggfunctionoptions""", alias="GroupByAggFunctionOptions")
    Position_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-position""", alias="Position")
    StopWordsMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-stopwordsmode""", alias="StopWordsMode")
    SourceColumn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sourcecolumn""", alias="SourceColumn")
    CustomCharacters_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-customcharacters""", alias="CustomCharacters")
    TimeZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-timezone""", alias="TimeZone")
    RemoveLeadingAndTrailingQuotes_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeleadingandtrailingquotes""", alias="RemoveLeadingAndTrailingQuotes")
    SourceColumn2_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sourcecolumn2""", alias="SourceColumn2")
    CollapseConsecutiveWhitespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-collapseconsecutivewhitespace""", alias="CollapseConsecutiveWhitespace")
    NumRowsAfter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-numrowsafter""", alias="NumRowsAfter")
    RemoveLetters_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeletters""", alias="RemoveLetters")
    SourceColumn1_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sourcecolumn1""", alias="SourceColumn1")
    UseNewDataFrame_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-usenewdataframe""", alias="UseNewDataFrame")
    Interval_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-interval""", alias="Interval")
    LowerBound_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-lowerbound""", alias="LowerBound")
    TokenizerPattern_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-tokenizerpattern""", alias="TokenizerPattern")
    LeftColumns_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-leftcolumns""", alias="LeftColumns")
    CharsToRemove_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-charstoremove""", alias="CharsToRemove")
    Value1_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-value1""", alias="Value1")
    DeleteOtherRows_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-deleteotherrows""", alias="DeleteOtherRows")
    Value2_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-value2""", alias="Value2")
    CategoryMap_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-categorymap""", alias="CategoryMap")
    StartPattern_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-startpattern""", alias="StartPattern")
    StartPosition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-startposition""", alias="StartPosition")
    SheetIndexes_: Optional[List[int]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sheetindexes""", alias="SheetIndexes")
    TargetIndex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-targetindex""", alias="TargetIndex")
    RemoveSourceColumn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removesourcecolumn""", alias="RemoveSourceColumn")
    DateTimeParameters_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-datetimeparameters""", alias="DateTimeParameters")
    EndValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-endvalue""", alias="EndValue")
    RemoveCustomCharacters_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removecustomcharacters""", alias="RemoveCustomCharacters")
    EndPosition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-endposition""", alias="EndPosition")
    Pattern_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-pattern""", alias="Pattern")
    Delimiter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-delimiter""", alias="Delimiter")
    RemoveSpecialCharacters_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removespecialcharacters""", alias="RemoveSpecialCharacters")
    RemoveAllQuotes_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeallquotes""", alias="RemoveAllQuotes")
    EndPattern_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-endpattern""", alias="EndPattern")
    StartColumnIndex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-startcolumnindex""", alias="StartColumnIndex")
    ModeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-modetype""", alias="ModeType")
    SecondaryInputs_: Optional[List['SecondaryInput']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-secondaryinputs""", alias="SecondaryInputs")
    SampleType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sampletype""", alias="SampleType")
    DateTimeFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-datetimeformat""", alias="DateTimeFormat")
    Other_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-other""", alias="Other")
    CaseStatement_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-casestatement""", alias="CaseStatement")
    FalseString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-falsestring""", alias="FalseString")
    RemoveAllPunctuation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeallpunctuation""", alias="RemoveAllPunctuation")
    CustomStopWords_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-customstopwords""", alias="CustomStopWords")
    MapType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-maptype""", alias="MapType")
    ColumnRange_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-columnrange""", alias="ColumnRange")
    CustomValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-customvalue""", alias="CustomValue")
    Input_: Optional['Input'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-input""", alias="Input")
    StepCount_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-stepcount""", alias="StepCount")
    TargetDateFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-targetdateformat""", alias="TargetDateFormat")
    SecondInput_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-secondinput""", alias="SecondInput")
    GroupByColumns_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-groupbycolumns""", alias="GroupByColumns")
    NumRowsBefore_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-numrowsbefore""", alias="NumRowsBefore")
    IsText_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-istext""", alias="IsText")
    TargetColumn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-targetcolumn""", alias="TargetColumn")
    RemoveNumbers_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removenumbers""", alias="RemoveNumbers")
    Period_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-period""", alias="Period")
    NumRows_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-numrows""", alias="NumRows")
    RightColumns_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-rightcolumns""", alias="RightColumns")
    StemmingMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-stemmingmode""", alias="StemmingMode")
    Units_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-units""", alias="Units")
    SampleSize_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-samplesize""", alias="SampleSize")
    IncludeInSplit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-includeinsplit""", alias="IncludeInSplit")
    AggregateFunction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-aggregatefunction""", alias="AggregateFunction")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-value""", alias="Value")
    Exponent_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-exponent""", alias="Exponent")
    StartValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-startvalue""", alias="StartValue")
    PatternOption2_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-patternoption2""", alias="PatternOption2")
    RemoveCustomValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removecustomvalue""", alias="RemoveCustomValue")
    PatternOption1_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-patternoption1""", alias="PatternOption1")
    MultiLine_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-multiline""", alias="MultiLine")
    TrueString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-truestring""", alias="TrueString")
    RemoveLeadingAndTrailingWhitespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeleadingandtrailingwhitespace""", alias="RemoveLeadingAndTrailingWhitespace")
    HiddenColumns_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-hiddencolumns""", alias="HiddenColumns")
    RemoveAllWhitespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-removeallwhitespace""", alias="RemoveAllWhitespace")
    ViewFrame_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-viewframe""", alias="ViewFrame")
    ColumnDataType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-columndatatype""", alias="ColumnDataType")
    JoinType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-jointype""", alias="JoinType")
    Base_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-base""", alias="Base")
    ValueColumn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-valuecolumn""", alias="ValueColumn")
    DatasetsColumns_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-datasetscolumns""", alias="DatasetsColumns")
    UdfLang_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-udflang""", alias="UdfLang")
    TargetColumnNames_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-targetcolumnnames""", alias="TargetColumnNames")
    DateAddValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-dateaddvalue""", alias="DateAddValue")
    ExpandContractions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-expandcontractions""", alias="ExpandContractions")
    UnpivotColumn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-unpivotcolumn""", alias="UnpivotColumn")
    Strategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-strategy""", alias="Strategy")
    SheetNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sheetnames""", alias="SheetNames")
    Limit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-limit""", alias="Limit")
    OrderByColumns_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-orderbycolumns""", alias="OrderByColumns")
    SourceColumns_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html#cfn-databrew-recipe-recipeparameters-sourcecolumns""", alias="SourceColumns")
    


    @property
    def tropo_type(self) -> troposphere.databrew.RecipeParameters:
        from troposphere.databrew import RecipeParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecipeStep(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html
    Properties:
        - Name: Action
        - Name: ConditionExpressions
    
    """
    
    Action_: 'Action' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html#cfn-databrew-recipe-recipestep-action""", alias="Action")
    ConditionExpressions_: Optional[List['ConditionExpression']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html#cfn-databrew-recipe-recipestep-conditionexpressions""", alias="ConditionExpressions")
    


    @property
    def tropo_type(self) -> troposphere.databrew.RecipeStep:
        from troposphere.databrew import RecipeStep as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html
    Properties:
        - Name: Bucket
        - Name: Key
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html#cfn-databrew-recipe-s3location-bucket""", alias="Bucket")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html#cfn-databrew-recipe-s3location-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.databrew.S3Location:
        from troposphere.databrew import S3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SecondaryInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html
    Properties:
        - Name: S3InputDefinition
        - Name: DataCatalogInputDefinition
    
    """
    
    S3InputDefinition_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html#cfn-databrew-recipe-secondaryinput-s3inputdefinition""", alias="S3InputDefinition")
    DataCatalogInputDefinition_: Optional['DataCatalogInputDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html#cfn-databrew-recipe-secondaryinput-datacataloginputdefinition""", alias="DataCatalogInputDefinition")
    


    @property
    def tropo_type(self) -> troposphere.databrew.SecondaryInput:
        from troposphere.databrew import SecondaryInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ColumnSelector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-columnselector.html
    Properties:
        - Name: Regex
        - Name: Name
    
    """
    
    Regex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-columnselector.html#cfn-databrew-ruleset-columnselector-regex""", alias="Regex")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-columnselector.html#cfn-databrew-ruleset-columnselector-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.databrew.ColumnSelector:
        from troposphere.databrew import ColumnSelector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html
    Properties:
        - Name: ColumnSelectors
        - Name: Disabled
        - Name: SubstitutionMap
        - Name: Name
        - Name: CheckExpression
        - Name: Threshold
    
    """
    
    ColumnSelectors_: Optional[List['ColumnSelector']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html#cfn-databrew-ruleset-rule-columnselectors""", alias="ColumnSelectors")
    Disabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html#cfn-databrew-ruleset-rule-disabled""", alias="Disabled")
    SubstitutionMap_: Optional[List['SubstitutionValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html#cfn-databrew-ruleset-rule-substitutionmap""", alias="SubstitutionMap")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html#cfn-databrew-ruleset-rule-name""", alias="Name")
    CheckExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html#cfn-databrew-ruleset-rule-checkexpression""", alias="CheckExpression")
    Threshold_: Optional['Threshold'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-rule.html#cfn-databrew-ruleset-rule-threshold""", alias="Threshold")
    


    @property
    def tropo_type(self) -> troposphere.databrew.Rule:
        from troposphere.databrew import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SubstitutionValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-substitutionvalue.html
    Properties:
        - Name: Value
        - Name: ValueReference
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-substitutionvalue.html#cfn-databrew-ruleset-substitutionvalue-value""", alias="Value")
    ValueReference_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-substitutionvalue.html#cfn-databrew-ruleset-substitutionvalue-valuereference""", alias="ValueReference")
    


    @property
    def tropo_type(self) -> troposphere.databrew.SubstitutionValue:
        from troposphere.databrew import SubstitutionValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Threshold(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-threshold.html
    Properties:
        - Name: Type
        - Name: Value
        - Name: Unit
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-threshold.html#cfn-databrew-ruleset-threshold-type""", alias="Type")
    Value_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-threshold.html#cfn-databrew-ruleset-threshold-value""", alias="Value")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-ruleset-threshold.html#cfn-databrew-ruleset-threshold-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.databrew.Threshold:
        from troposphere.databrew import Threshold as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Dataset(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html
    Properties:
        - Name: Input
        - Name: Format
        - Name: FormatOptions
        - Name: PathOptions
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Input_: 'Input' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-input""", alias="Input")
    Format_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-format""", alias="Format")
    FormatOptions_: Optional['FormatOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-formatoptions""", alias="FormatOptions")
    PathOptions_: Optional['PathOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-pathoptions""", alias="PathOptions")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html#cfn-databrew-dataset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.databrew.Dataset:
        from troposphere.databrew import Dataset as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.databrew import Dataset as TropoT
        return resource_to_troposphere(self, TropoT)


class Job(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html
    Properties:
        - Name: MaxRetries
        - Name: ProjectName
        - Name: Recipe
        - Name: EncryptionKeyArn
        - Name: LogSubscription
        - Name: Timeout
        - Name: DatabaseOutputs
        - Name: OutputLocation
        - Name: RoleArn
        - Name: Name
        - Name: Type
        - Name: DatasetName
        - Name: ProfileConfiguration
        - Name: Outputs
        - Name: ValidationConfigurations
        - Name: Tags
        - Name: JobSample
        - Name: EncryptionMode
        - Name: MaxCapacity
        - Name: DataCatalogOutputs
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MaxRetries_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-maxretries""", alias="MaxRetries")
    ProjectName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-projectname""", alias="ProjectName")
    Recipe_: Optional['Recipe'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-recipe""", alias="Recipe")
    EncryptionKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-encryptionkeyarn""", alias="EncryptionKeyArn")
    LogSubscription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-logsubscription""", alias="LogSubscription")
    Timeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-timeout""", alias="Timeout")
    DatabaseOutputs_: Optional[List['DatabaseOutput']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-databaseoutputs""", alias="DatabaseOutputs")
    OutputLocation_: Optional['OutputLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-outputlocation""", alias="OutputLocation")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-rolearn""", alias="RoleArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-name""", alias="Name")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-type""", alias="Type")
    DatasetName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-datasetname""", alias="DatasetName")
    ProfileConfiguration_: Optional['ProfileConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-profileconfiguration""", alias="ProfileConfiguration")
    Outputs_: Optional[List['Output']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-outputs""", alias="Outputs")
    ValidationConfigurations_: Optional[List['ValidationConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-validationconfigurations""", alias="ValidationConfigurations")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-tags""", alias="Tags")
    JobSample_: Optional['JobSample'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-jobsample""", alias="JobSample")
    EncryptionMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-encryptionmode""", alias="EncryptionMode")
    MaxCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-maxcapacity""", alias="MaxCapacity")
    DataCatalogOutputs_: Optional[List['DataCatalogOutput']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html#cfn-databrew-job-datacatalogoutputs""", alias="DataCatalogOutputs")
    

    @property
    def tropo_type(self) -> troposphere.databrew.Job:
        from troposphere.databrew import Job as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.databrew import Job as TropoT
        return resource_to_troposphere(self, TropoT)


class Project(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html
    Properties:
        - Name: RecipeName
        - Name: DatasetName
        - Name: Sample
        - Name: RoleArn
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RecipeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-recipename""", alias="RecipeName")
    DatasetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-datasetname""", alias="DatasetName")
    Sample_: Optional['Sample'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-sample""", alias="Sample")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html#cfn-databrew-project-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.databrew.Project:
        from troposphere.databrew import Project as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.databrew import Project as TropoT
        return resource_to_troposphere(self, TropoT)


class Recipe(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html
    Properties:
        - Name: Steps
        - Name: Description
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Steps_: List['RecipeStep'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html#cfn-databrew-recipe-steps""", alias="Steps")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html#cfn-databrew-recipe-description""", alias="Description")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html#cfn-databrew-recipe-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html#cfn-databrew-recipe-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.databrew.Recipe:
        from troposphere.databrew import Recipe as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.databrew import Recipe as TropoT
        return resource_to_troposphere(self, TropoT)


class Ruleset(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html
    Properties:
        - Name: Description
        - Name: TargetArn
        - Name: Rules
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-description""", alias="Description")
    TargetArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-targetarn""", alias="TargetArn")
    Rules_: List['Rule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-rules""", alias="Rules")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-ruleset.html#cfn-databrew-ruleset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.databrew.Ruleset:
        from troposphere.databrew import Ruleset as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.databrew import Ruleset as TropoT
        return resource_to_troposphere(self, TropoT)


class Schedule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html
    Properties:
        - Name: JobNames
        - Name: CronExpression
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    JobNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html#cfn-databrew-schedule-jobnames""", alias="JobNames")
    CronExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html#cfn-databrew-schedule-cronexpression""", alias="CronExpression")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html#cfn-databrew-schedule-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html#cfn-databrew-schedule-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.databrew.Schedule:
        from troposphere.databrew import Schedule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.databrew import Schedule as TropoT
        return resource_to_troposphere(self, TropoT)

