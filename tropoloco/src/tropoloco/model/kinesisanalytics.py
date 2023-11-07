from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CSVMappingParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html
    Properties:
        - Name: RecordRowDelimiter
        - Name: RecordColumnDelimiter
    
    """
    
    RecordRowDelimiter_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html#cfn-kinesisanalytics-application-csvmappingparameters-recordrowdelimiter""", alias="RecordRowDelimiter")
    RecordColumnDelimiter_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html#cfn-kinesisanalytics-application-csvmappingparameters-recordcolumndelimiter""", alias="RecordColumnDelimiter")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.CSVMappingParameters:
        from troposphere.kinesisanalytics import CSVMappingParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Input(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html
    Properties:
        - Name: NamePrefix
        - Name: InputSchema
        - Name: KinesisStreamsInput
        - Name: KinesisFirehoseInput
        - Name: InputProcessingConfiguration
        - Name: InputParallelism
    
    """
    
    NamePrefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-nameprefix""", alias="NamePrefix")
    InputSchema_: 'InputSchema' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputschema""", alias="InputSchema")
    KinesisStreamsInput_: Optional['KinesisStreamsInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-kinesisstreamsinput""", alias="KinesisStreamsInput")
    KinesisFirehoseInput_: Optional['KinesisFirehoseInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-kinesisfirehoseinput""", alias="KinesisFirehoseInput")
    InputProcessingConfiguration_: Optional['InputProcessingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputprocessingconfiguration""", alias="InputProcessingConfiguration")
    InputParallelism_: Optional['InputParallelism'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputparallelism""", alias="InputParallelism")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.Input:
        from troposphere.kinesisanalytics import Input as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputLambdaProcessor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html
    Properties:
        - Name: ResourceARN
        - Name: RoleARN
    
    """
    
    ResourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html#cfn-kinesisanalytics-application-inputlambdaprocessor-resourcearn""", alias="ResourceARN")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html#cfn-kinesisanalytics-application-inputlambdaprocessor-rolearn""", alias="RoleARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.InputLambdaProcessor:
        from troposphere.kinesisanalytics import InputLambdaProcessor as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputParallelism(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputparallelism.html
    Properties:
        - Name: Count
    
    """
    
    Count_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputparallelism.html#cfn-kinesisanalytics-application-inputparallelism-count""", alias="Count")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.InputParallelism:
        from troposphere.kinesisanalytics import InputParallelism as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputProcessingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html
    Properties:
        - Name: InputLambdaProcessor
    
    """
    
    InputLambdaProcessor_: Optional['InputLambdaProcessor'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html#cfn-kinesisanalytics-application-inputprocessingconfiguration-inputlambdaprocessor""", alias="InputLambdaProcessor")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.InputProcessingConfiguration:
        from troposphere.kinesisanalytics import InputProcessingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputSchema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html
    Properties:
        - Name: RecordEncoding
        - Name: RecordColumns
        - Name: RecordFormat
    
    """
    
    RecordEncoding_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordencoding""", alias="RecordEncoding")
    RecordColumns_: List['RecordColumn'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordcolumns""", alias="RecordColumns")
    RecordFormat_: 'RecordFormat' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordformat""", alias="RecordFormat")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.InputSchema:
        from troposphere.kinesisanalytics import InputSchema as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JSONMappingParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-jsonmappingparameters.html
    Properties:
        - Name: RecordRowPath
    
    """
    
    RecordRowPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-jsonmappingparameters.html#cfn-kinesisanalytics-application-jsonmappingparameters-recordrowpath""", alias="RecordRowPath")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.JSONMappingParameters:
        from troposphere.kinesisanalytics import JSONMappingParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisFirehoseInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html
    Properties:
        - Name: ResourceARN
        - Name: RoleARN
    
    """
    
    ResourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html#cfn-kinesisanalytics-application-kinesisfirehoseinput-resourcearn""", alias="ResourceARN")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html#cfn-kinesisanalytics-application-kinesisfirehoseinput-rolearn""", alias="RoleARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.KinesisFirehoseInput:
        from troposphere.kinesisanalytics import KinesisFirehoseInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisStreamsInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html
    Properties:
        - Name: ResourceARN
        - Name: RoleARN
    
    """
    
    ResourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html#cfn-kinesisanalytics-application-kinesisstreamsinput-resourcearn""", alias="ResourceARN")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html#cfn-kinesisanalytics-application-kinesisstreamsinput-rolearn""", alias="RoleARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.KinesisStreamsInput:
        from troposphere.kinesisanalytics import KinesisStreamsInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MappingParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html
    Properties:
        - Name: JSONMappingParameters
        - Name: CSVMappingParameters
    
    """
    
    JSONMappingParameters_: Optional['JSONMappingParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html#cfn-kinesisanalytics-application-mappingparameters-jsonmappingparameters""", alias="JSONMappingParameters")
    CSVMappingParameters_: Optional['CSVMappingParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html#cfn-kinesisanalytics-application-mappingparameters-csvmappingparameters""", alias="CSVMappingParameters")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.MappingParameters:
        from troposphere.kinesisanalytics import MappingParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecordColumn(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html
    Properties:
        - Name: Mapping
        - Name: SqlType
        - Name: Name
    
    """
    
    Mapping_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-mapping""", alias="Mapping")
    SqlType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-sqltype""", alias="SqlType")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.RecordColumn:
        from troposphere.kinesisanalytics import RecordColumn as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecordFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html
    Properties:
        - Name: MappingParameters
        - Name: RecordFormatType
    
    """
    
    MappingParameters_: Optional['MappingParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html#cfn-kinesisanalytics-application-recordformat-mappingparameters""", alias="MappingParameters")
    RecordFormatType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html#cfn-kinesisanalytics-application-recordformat-recordformattype""", alias="RecordFormatType")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.RecordFormat:
        from troposphere.kinesisanalytics import RecordFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DestinationSchema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-destinationschema.html
    Properties:
        - Name: RecordFormatType
    
    """
    
    RecordFormatType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-destinationschema.html#cfn-kinesisanalytics-applicationoutput-destinationschema-recordformattype""", alias="RecordFormatType")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.DestinationSchema:
        from troposphere.kinesisanalytics import DestinationSchema as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisFirehoseOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html
    Properties:
        - Name: ResourceARN
        - Name: RoleARN
    
    """
    
    ResourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-resourcearn""", alias="ResourceARN")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-rolearn""", alias="RoleARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.KinesisFirehoseOutput:
        from troposphere.kinesisanalytics import KinesisFirehoseOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisStreamsOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html
    Properties:
        - Name: ResourceARN
        - Name: RoleARN
    
    """
    
    ResourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-resourcearn""", alias="ResourceARN")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-rolearn""", alias="RoleARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.KinesisStreamsOutput:
        from troposphere.kinesisanalytics import KinesisStreamsOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html
    Properties:
        - Name: ResourceARN
        - Name: RoleARN
    
    """
    
    ResourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html#cfn-kinesisanalytics-applicationoutput-lambdaoutput-resourcearn""", alias="ResourceARN")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html#cfn-kinesisanalytics-applicationoutput-lambdaoutput-rolearn""", alias="RoleARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.LambdaOutput:
        from troposphere.kinesisanalytics import LambdaOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Output(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html
    Properties:
        - Name: DestinationSchema
        - Name: LambdaOutput
        - Name: KinesisFirehoseOutput
        - Name: KinesisStreamsOutput
        - Name: Name
    
    """
    
    DestinationSchema_: 'DestinationSchema' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-destinationschema""", alias="DestinationSchema")
    LambdaOutput_: Optional['LambdaOutput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-lambdaoutput""", alias="LambdaOutput")
    KinesisFirehoseOutput_: Optional['KinesisFirehoseOutput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-kinesisfirehoseoutput""", alias="KinesisFirehoseOutput")
    KinesisStreamsOutput_: Optional['KinesisStreamsOutput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-kinesisstreamsoutput""", alias="KinesisStreamsOutput")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.Output:
        from troposphere.kinesisanalytics import Output as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CSVMappingParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html
    Properties:
        - Name: RecordRowDelimiter
        - Name: RecordColumnDelimiter
    
    """
    
    RecordRowDelimiter_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter""", alias="RecordRowDelimiter")
    RecordColumnDelimiter_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter""", alias="RecordColumnDelimiter")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.CSVMappingParameters:
        from troposphere.kinesisanalytics import CSVMappingParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JSONMappingParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters.html
    Properties:
        - Name: RecordRowPath
    
    """
    
    RecordRowPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters-recordrowpath""", alias="RecordRowPath")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.JSONMappingParameters:
        from troposphere.kinesisanalytics import JSONMappingParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MappingParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html
    Properties:
        - Name: JSONMappingParameters
        - Name: CSVMappingParameters
    
    """
    
    JSONMappingParameters_: Optional['JSONMappingParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-mappingparameters-jsonmappingparameters""", alias="JSONMappingParameters")
    CSVMappingParameters_: Optional['CSVMappingParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-mappingparameters-csvmappingparameters""", alias="CSVMappingParameters")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.MappingParameters:
        from troposphere.kinesisanalytics import MappingParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecordColumn(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html
    Properties:
        - Name: Mapping
        - Name: SqlType
        - Name: Name
    
    """
    
    Mapping_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-mapping""", alias="Mapping")
    SqlType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-sqltype""", alias="SqlType")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.RecordColumn:
        from troposphere.kinesisanalytics import RecordColumn as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecordFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html
    Properties:
        - Name: MappingParameters
        - Name: RecordFormatType
    
    """
    
    MappingParameters_: Optional['MappingParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html#cfn-kinesisanalytics-applicationreferencedatasource-recordformat-mappingparameters""", alias="MappingParameters")
    RecordFormatType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html#cfn-kinesisanalytics-applicationreferencedatasource-recordformat-recordformattype""", alias="RecordFormatType")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.RecordFormat:
        from troposphere.kinesisanalytics import RecordFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReferenceDataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html
    Properties:
        - Name: ReferenceSchema
        - Name: TableName
        - Name: S3ReferenceDataSource
    
    """
    
    ReferenceSchema_: 'ReferenceSchema' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-referenceschema""", alias="ReferenceSchema")
    TableName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-tablename""", alias="TableName")
    S3ReferenceDataSource_: Optional['S3ReferenceDataSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-s3referencedatasource""", alias="S3ReferenceDataSource")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.ReferenceDataSource:
        from troposphere.kinesisanalytics import ReferenceDataSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReferenceSchema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html
    Properties:
        - Name: RecordEncoding
        - Name: RecordColumns
        - Name: RecordFormat
    
    """
    
    RecordEncoding_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordencoding""", alias="RecordEncoding")
    RecordColumns_: List['RecordColumn'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordcolumns""", alias="RecordColumns")
    RecordFormat_: 'RecordFormat' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordformat""", alias="RecordFormat")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.ReferenceSchema:
        from troposphere.kinesisanalytics import ReferenceSchema as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3ReferenceDataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html
    Properties:
        - Name: BucketARN
        - Name: FileKey
        - Name: ReferenceRoleARN
    
    """
    
    BucketARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-bucketarn""", alias="BucketARN")
    FileKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-filekey""", alias="FileKey")
    ReferenceRoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-referencerolearn""", alias="ReferenceRoleARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.S3ReferenceDataSource:
        from troposphere.kinesisanalytics import S3ReferenceDataSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Application(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html
    Properties:
        - Name: ApplicationName
        - Name: Inputs
        - Name: ApplicationDescription
        - Name: ApplicationCode
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApplicationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationname""", alias="ApplicationName")
    Inputs_: List['Input'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-inputs""", alias="Inputs")
    ApplicationDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationdescription""", alias="ApplicationDescription")
    ApplicationCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationcode""", alias="ApplicationCode")
    

    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.Application:
        from troposphere.kinesisanalytics import Application as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kinesisanalytics import Application as TropoT
        return resource_to_troposphere(self, TropoT)


class ApplicationOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html
    Properties:
        - Name: ApplicationName
        - Name: Output
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApplicationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-applicationname""", alias="ApplicationName")
    Output_: 'Output' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-output""", alias="Output")
    

    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.ApplicationOutput:
        from troposphere.kinesisanalytics import ApplicationOutput as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kinesisanalytics import ApplicationOutput as TropoT
        return resource_to_troposphere(self, TropoT)


class ApplicationReferenceDataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html
    Properties:
        - Name: ApplicationName
        - Name: ReferenceDataSource
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApplicationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-applicationname""", alias="ApplicationName")
    ReferenceDataSource_: 'ReferenceDataSource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource""", alias="ReferenceDataSource")
    

    @property
    def tropo_type(self) -> troposphere.kinesisanalytics.ApplicationReferenceDataSource:
        from troposphere.kinesisanalytics import ApplicationReferenceDataSource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kinesisanalytics import ApplicationReferenceDataSource as TropoT
        return resource_to_troposphere(self, TropoT)

