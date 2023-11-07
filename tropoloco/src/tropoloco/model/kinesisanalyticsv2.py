from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ApplicationCodeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html
    Properties:
        - Name: CodeContentType
        - Name: CodeContent
    
    """
    
    CodeContentType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontenttype""", alias="CodeContentType")
    CodeContent_: 'CodeContent' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontent""", alias="CodeContent")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.ApplicationCodeConfiguration:
        from troposphere.kinesisanalyticsv2 import ApplicationCodeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ApplicationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html
    Properties:
        - Name: ApplicationCodeConfiguration
        - Name: EnvironmentProperties
        - Name: FlinkApplicationConfiguration
        - Name: SqlApplicationConfiguration
        - Name: ZeppelinApplicationConfiguration
        - Name: VpcConfigurations
        - Name: ApplicationSnapshotConfiguration
    
    """
    
    ApplicationCodeConfiguration_: Optional['ApplicationCodeConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationcodeconfiguration""", alias="ApplicationCodeConfiguration")
    EnvironmentProperties_: Optional['EnvironmentProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-environmentproperties""", alias="EnvironmentProperties")
    FlinkApplicationConfiguration_: Optional['FlinkApplicationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-flinkapplicationconfiguration""", alias="FlinkApplicationConfiguration")
    SqlApplicationConfiguration_: Optional['SqlApplicationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-sqlapplicationconfiguration""", alias="SqlApplicationConfiguration")
    ZeppelinApplicationConfiguration_: Optional['ZeppelinApplicationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-zeppelinapplicationconfiguration""", alias="ZeppelinApplicationConfiguration")
    VpcConfigurations_: Optional[List['VpcConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-vpcconfigurations""", alias="VpcConfigurations")
    ApplicationSnapshotConfiguration_: Optional['ApplicationSnapshotConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationsnapshotconfiguration""", alias="ApplicationSnapshotConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.ApplicationConfiguration:
        from troposphere.kinesisanalyticsv2 import ApplicationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ApplicationMaintenanceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration.html
    Properties:
        - Name: ApplicationMaintenanceWindowStartTime
    
    """
    
    ApplicationMaintenanceWindowStartTime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration.html#cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration-applicationmaintenancewindowstarttime""", alias="ApplicationMaintenanceWindowStartTime")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.ApplicationMaintenanceConfiguration:
        from troposphere.kinesisanalyticsv2 import ApplicationMaintenanceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ApplicationRestoreConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationrestoreconfiguration.html
    Properties:
        - Name: SnapshotName
        - Name: ApplicationRestoreType
    
    """
    
    SnapshotName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationrestoreconfiguration.html#cfn-kinesisanalyticsv2-application-applicationrestoreconfiguration-snapshotname""", alias="SnapshotName")
    ApplicationRestoreType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationrestoreconfiguration.html#cfn-kinesisanalyticsv2-application-applicationrestoreconfiguration-applicationrestoretype""", alias="ApplicationRestoreType")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.ApplicationRestoreConfiguration:
        from troposphere.kinesisanalyticsv2 import ApplicationRestoreConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ApplicationSnapshotConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html
    Properties:
        - Name: SnapshotsEnabled
    
    """
    
    SnapshotsEnabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html#cfn-kinesisanalyticsv2-application-applicationsnapshotconfiguration-snapshotsenabled""", alias="SnapshotsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.ApplicationSnapshotConfiguration:
        from troposphere.kinesisanalyticsv2 import ApplicationSnapshotConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CSVMappingParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html
    Properties:
        - Name: RecordRowDelimiter
        - Name: RecordColumnDelimiter
    
    """
    
    RecordRowDelimiter_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html#cfn-kinesisanalyticsv2-application-csvmappingparameters-recordrowdelimiter""", alias="RecordRowDelimiter")
    RecordColumnDelimiter_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html#cfn-kinesisanalyticsv2-application-csvmappingparameters-recordcolumndelimiter""", alias="RecordColumnDelimiter")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.CSVMappingParameters:
        from troposphere.kinesisanalyticsv2 import CSVMappingParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CatalogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html
    Properties:
        - Name: GlueDataCatalogConfiguration
    
    """
    
    GlueDataCatalogConfiguration_: Optional['GlueDataCatalogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html#cfn-kinesisanalyticsv2-application-catalogconfiguration-gluedatacatalogconfiguration""", alias="GlueDataCatalogConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.CatalogConfiguration:
        from troposphere.kinesisanalyticsv2 import CatalogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CheckpointConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html
    Properties:
        - Name: ConfigurationType
        - Name: CheckpointInterval
        - Name: MinPauseBetweenCheckpoints
        - Name: CheckpointingEnabled
    
    """
    
    ConfigurationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-configurationtype""", alias="ConfigurationType")
    CheckpointInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointinterval""", alias="CheckpointInterval")
    MinPauseBetweenCheckpoints_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-minpausebetweencheckpoints""", alias="MinPauseBetweenCheckpoints")
    CheckpointingEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointingenabled""", alias="CheckpointingEnabled")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.CheckpointConfiguration:
        from troposphere.kinesisanalyticsv2 import CheckpointConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CodeContent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html
    Properties:
        - Name: ZipFileContent
        - Name: S3ContentLocation
        - Name: TextContent
    
    """
    
    ZipFileContent_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-zipfilecontent""", alias="ZipFileContent")
    S3ContentLocation_: Optional['S3ContentLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-s3contentlocation""", alias="S3ContentLocation")
    TextContent_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-textcontent""", alias="TextContent")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.CodeContent:
        from troposphere.kinesisanalyticsv2 import CodeContent as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomArtifactConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html
    Properties:
        - Name: MavenReference
        - Name: S3ContentLocation
        - Name: ArtifactType
    
    """
    
    MavenReference_: Optional['MavenReference'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-mavenreference""", alias="MavenReference")
    S3ContentLocation_: Optional['S3ContentLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-s3contentlocation""", alias="S3ContentLocation")
    ArtifactType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-artifacttype""", alias="ArtifactType")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.CustomArtifactConfiguration:
        from troposphere.kinesisanalyticsv2 import CustomArtifactConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeployAsApplicationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html
    Properties:
        - Name: S3ContentLocation
    
    """
    
    S3ContentLocation_: 'S3ContentBaseLocation' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-deployasapplicationconfiguration-s3contentlocation""", alias="S3ContentLocation")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.DeployAsApplicationConfiguration:
        from troposphere.kinesisanalyticsv2 import DeployAsApplicationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnvironmentProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html
    Properties:
        - Name: PropertyGroups
    
    """
    
    PropertyGroups_: Optional[List['PropertyGroup']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html#cfn-kinesisanalyticsv2-application-environmentproperties-propertygroups""", alias="PropertyGroups")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.EnvironmentProperties:
        from troposphere.kinesisanalyticsv2 import EnvironmentProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FlinkApplicationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html
    Properties:
        - Name: CheckpointConfiguration
        - Name: ParallelismConfiguration
        - Name: MonitoringConfiguration
    
    """
    
    CheckpointConfiguration_: Optional['CheckpointConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-checkpointconfiguration""", alias="CheckpointConfiguration")
    ParallelismConfiguration_: Optional['ParallelismConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-parallelismconfiguration""", alias="ParallelismConfiguration")
    MonitoringConfiguration_: Optional['MonitoringConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-monitoringconfiguration""", alias="MonitoringConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.FlinkApplicationConfiguration:
        from troposphere.kinesisanalyticsv2 import FlinkApplicationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FlinkRunConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration.html
    Properties:
        - Name: AllowNonRestoredState
    
    """
    
    AllowNonRestoredState_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration.html#cfn-kinesisanalyticsv2-application-flinkrunconfiguration-allownonrestoredstate""", alias="AllowNonRestoredState")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.FlinkRunConfiguration:
        from troposphere.kinesisanalyticsv2 import FlinkRunConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GlueDataCatalogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.html
    Properties:
        - Name: DatabaseARN
    
    """
    
    DatabaseARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.html#cfn-kinesisanalyticsv2-application-gluedatacatalogconfiguration-databasearn""", alias="DatabaseARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.GlueDataCatalogConfiguration:
        from troposphere.kinesisanalyticsv2 import GlueDataCatalogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Input(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html
    Properties:
        - Name: NamePrefix
        - Name: InputSchema
        - Name: KinesisStreamsInput
        - Name: KinesisFirehoseInput
        - Name: InputProcessingConfiguration
        - Name: InputParallelism
    
    """
    
    NamePrefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-nameprefix""", alias="NamePrefix")
    InputSchema_: 'InputSchema' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputschema""", alias="InputSchema")
    KinesisStreamsInput_: Optional['KinesisStreamsInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisstreamsinput""", alias="KinesisStreamsInput")
    KinesisFirehoseInput_: Optional['KinesisFirehoseInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisfirehoseinput""", alias="KinesisFirehoseInput")
    InputProcessingConfiguration_: Optional['InputProcessingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputprocessingconfiguration""", alias="InputProcessingConfiguration")
    InputParallelism_: Optional['InputParallelism'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputparallelism""", alias="InputParallelism")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.Input:
        from troposphere.kinesisanalyticsv2 import Input as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputLambdaProcessor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html
    Properties:
        - Name: ResourceARN
    
    """
    
    ResourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html#cfn-kinesisanalyticsv2-application-inputlambdaprocessor-resourcearn""", alias="ResourceARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.InputLambdaProcessor:
        from troposphere.kinesisanalyticsv2 import InputLambdaProcessor as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputParallelism(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html
    Properties:
        - Name: Count
    
    """
    
    Count_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html#cfn-kinesisanalyticsv2-application-inputparallelism-count""", alias="Count")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.InputParallelism:
        from troposphere.kinesisanalyticsv2 import InputParallelism as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputProcessingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html
    Properties:
        - Name: InputLambdaProcessor
    
    """
    
    InputLambdaProcessor_: Optional['InputLambdaProcessor'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html#cfn-kinesisanalyticsv2-application-inputprocessingconfiguration-inputlambdaprocessor""", alias="InputLambdaProcessor")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.InputProcessingConfiguration:
        from troposphere.kinesisanalyticsv2 import InputProcessingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputSchema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html
    Properties:
        - Name: RecordEncoding
        - Name: RecordColumns
        - Name: RecordFormat
    
    """
    
    RecordEncoding_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordencoding""", alias="RecordEncoding")
    RecordColumns_: List['RecordColumn'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordcolumns""", alias="RecordColumns")
    RecordFormat_: 'RecordFormat' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordformat""", alias="RecordFormat")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.InputSchema:
        from troposphere.kinesisanalyticsv2 import InputSchema as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JSONMappingParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html
    Properties:
        - Name: RecordRowPath
    
    """
    
    RecordRowPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html#cfn-kinesisanalyticsv2-application-jsonmappingparameters-recordrowpath""", alias="RecordRowPath")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.JSONMappingParameters:
        from troposphere.kinesisanalyticsv2 import JSONMappingParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisFirehoseInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html
    Properties:
        - Name: ResourceARN
    
    """
    
    ResourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html#cfn-kinesisanalyticsv2-application-kinesisfirehoseinput-resourcearn""", alias="ResourceARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.KinesisFirehoseInput:
        from troposphere.kinesisanalyticsv2 import KinesisFirehoseInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisStreamsInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html
    Properties:
        - Name: ResourceARN
    
    """
    
    ResourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html#cfn-kinesisanalyticsv2-application-kinesisstreamsinput-resourcearn""", alias="ResourceARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.KinesisStreamsInput:
        from troposphere.kinesisanalyticsv2 import KinesisStreamsInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MappingParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html
    Properties:
        - Name: JSONMappingParameters
        - Name: CSVMappingParameters
    
    """
    
    JSONMappingParameters_: Optional['JSONMappingParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-jsonmappingparameters""", alias="JSONMappingParameters")
    CSVMappingParameters_: Optional['CSVMappingParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-csvmappingparameters""", alias="CSVMappingParameters")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.MappingParameters:
        from troposphere.kinesisanalyticsv2 import MappingParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MavenReference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html
    Properties:
        - Name: ArtifactId
        - Name: Version
        - Name: GroupId
    
    """
    
    ArtifactId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-artifactid""", alias="ArtifactId")
    Version_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-version""", alias="Version")
    GroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-groupid""", alias="GroupId")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.MavenReference:
        from troposphere.kinesisanalyticsv2 import MavenReference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html
    Properties:
        - Name: ConfigurationType
        - Name: MetricsLevel
        - Name: LogLevel
    
    """
    
    ConfigurationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-configurationtype""", alias="ConfigurationType")
    MetricsLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-metricslevel""", alias="MetricsLevel")
    LogLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-loglevel""", alias="LogLevel")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.MonitoringConfiguration:
        from troposphere.kinesisanalyticsv2 import MonitoringConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ParallelismConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html
    Properties:
        - Name: ConfigurationType
        - Name: ParallelismPerKPU
        - Name: AutoScalingEnabled
        - Name: Parallelism
    
    """
    
    ConfigurationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-configurationtype""", alias="ConfigurationType")
    ParallelismPerKPU_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-parallelismperkpu""", alias="ParallelismPerKPU")
    AutoScalingEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-autoscalingenabled""", alias="AutoScalingEnabled")
    Parallelism_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-parallelism""", alias="Parallelism")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.ParallelismConfiguration:
        from troposphere.kinesisanalyticsv2 import ParallelismConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PropertyGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html
    Properties:
        - Name: PropertyMap
        - Name: PropertyGroupId
    
    """
    
    PropertyMap_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html#cfn-kinesisanalyticsv2-application-propertygroup-propertymap""", alias="PropertyMap")
    PropertyGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html#cfn-kinesisanalyticsv2-application-propertygroup-propertygroupid""", alias="PropertyGroupId")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.PropertyGroup:
        from troposphere.kinesisanalyticsv2 import PropertyGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecordColumn(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html
    Properties:
        - Name: Mapping
        - Name: SqlType
        - Name: Name
    
    """
    
    Mapping_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-mapping""", alias="Mapping")
    SqlType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-sqltype""", alias="SqlType")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.RecordColumn:
        from troposphere.kinesisanalyticsv2 import RecordColumn as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecordFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html
    Properties:
        - Name: MappingParameters
        - Name: RecordFormatType
    
    """
    
    MappingParameters_: Optional['MappingParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html#cfn-kinesisanalyticsv2-application-recordformat-mappingparameters""", alias="MappingParameters")
    RecordFormatType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html#cfn-kinesisanalyticsv2-application-recordformat-recordformattype""", alias="RecordFormatType")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.RecordFormat:
        from troposphere.kinesisanalyticsv2 import RecordFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RunConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-runconfiguration.html
    Properties:
        - Name: FlinkRunConfiguration
        - Name: ApplicationRestoreConfiguration
    
    """
    
    FlinkRunConfiguration_: Optional['FlinkRunConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-runconfiguration.html#cfn-kinesisanalyticsv2-application-runconfiguration-flinkrunconfiguration""", alias="FlinkRunConfiguration")
    ApplicationRestoreConfiguration_: Optional['ApplicationRestoreConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-runconfiguration.html#cfn-kinesisanalyticsv2-application-runconfiguration-applicationrestoreconfiguration""", alias="ApplicationRestoreConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.RunConfiguration:
        from troposphere.kinesisanalyticsv2 import RunConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3ContentBaseLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html
    Properties:
        - Name: BucketARN
        - Name: BasePath
    
    """
    
    BucketARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html#cfn-kinesisanalyticsv2-application-s3contentbaselocation-bucketarn""", alias="BucketARN")
    BasePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html#cfn-kinesisanalyticsv2-application-s3contentbaselocation-basepath""", alias="BasePath")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.S3ContentBaseLocation:
        from troposphere.kinesisanalyticsv2 import S3ContentBaseLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3ContentLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html
    Properties:
        - Name: BucketARN
        - Name: FileKey
        - Name: ObjectVersion
    
    """
    
    BucketARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-bucketarn""", alias="BucketARN")
    FileKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-filekey""", alias="FileKey")
    ObjectVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-objectversion""", alias="ObjectVersion")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.S3ContentLocation:
        from troposphere.kinesisanalyticsv2 import S3ContentLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SqlApplicationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html
    Properties:
        - Name: Inputs
    
    """
    
    Inputs_: Optional[List['Input']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-sqlapplicationconfiguration-inputs""", alias="Inputs")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.SqlApplicationConfiguration:
        from troposphere.kinesisanalyticsv2 import SqlApplicationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-vpcconfiguration.html
    Properties:
        - Name: SecurityGroupIds
        - Name: SubnetIds
    
    """
    
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-vpcconfiguration.html#cfn-kinesisanalyticsv2-application-vpcconfiguration-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-vpcconfiguration.html#cfn-kinesisanalyticsv2-application-vpcconfiguration-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.VpcConfiguration:
        from troposphere.kinesisanalyticsv2 import VpcConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ZeppelinApplicationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html
    Properties:
        - Name: CatalogConfiguration
        - Name: MonitoringConfiguration
        - Name: DeployAsApplicationConfiguration
        - Name: CustomArtifactsConfiguration
    
    """
    
    CatalogConfiguration_: Optional['CatalogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-catalogconfiguration""", alias="CatalogConfiguration")
    MonitoringConfiguration_: Optional['ZeppelinMonitoringConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-monitoringconfiguration""", alias="MonitoringConfiguration")
    DeployAsApplicationConfiguration_: Optional['DeployAsApplicationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-deployasapplicationconfiguration""", alias="DeployAsApplicationConfiguration")
    CustomArtifactsConfiguration_: Optional[List['CustomArtifactConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-customartifactsconfiguration""", alias="CustomArtifactsConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.ZeppelinApplicationConfiguration:
        from troposphere.kinesisanalyticsv2 import ZeppelinApplicationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ZeppelinMonitoringConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration.html
    Properties:
        - Name: LogLevel
    
    """
    
    LogLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration-loglevel""", alias="LogLevel")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.ZeppelinMonitoringConfiguration:
        from troposphere.kinesisanalyticsv2 import ZeppelinMonitoringConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchLoggingOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html
    Properties:
        - Name: LogStreamARN
    
    """
    
    LogStreamARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption-logstreamarn""", alias="LogStreamARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.CloudWatchLoggingOption:
        from troposphere.kinesisanalyticsv2 import CloudWatchLoggingOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DestinationSchema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-destinationschema.html
    Properties:
        - Name: RecordFormatType
    
    """
    
    RecordFormatType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-destinationschema.html#cfn-kinesisanalyticsv2-applicationoutput-destinationschema-recordformattype""", alias="RecordFormatType")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.DestinationSchema:
        from troposphere.kinesisanalyticsv2 import DestinationSchema as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisFirehoseOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput.html
    Properties:
        - Name: ResourceARN
    
    """
    
    ResourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput-resourcearn""", alias="ResourceARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.KinesisFirehoseOutput:
        from troposphere.kinesisanalyticsv2 import KinesisFirehoseOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisStreamsOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html
    Properties:
        - Name: ResourceARN
    
    """
    
    ResourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput-resourcearn""", alias="ResourceARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.KinesisStreamsOutput:
        from troposphere.kinesisanalyticsv2 import KinesisStreamsOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-lambdaoutput.html
    Properties:
        - Name: ResourceARN
    
    """
    
    ResourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-lambdaoutput.html#cfn-kinesisanalyticsv2-applicationoutput-lambdaoutput-resourcearn""", alias="ResourceARN")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.LambdaOutput:
        from troposphere.kinesisanalyticsv2 import LambdaOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Output(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html
    Properties:
        - Name: DestinationSchema
        - Name: LambdaOutput
        - Name: KinesisFirehoseOutput
        - Name: KinesisStreamsOutput
        - Name: Name
    
    """
    
    DestinationSchema_: 'DestinationSchema' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-destinationschema""", alias="DestinationSchema")
    LambdaOutput_: Optional['LambdaOutput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-lambdaoutput""", alias="LambdaOutput")
    KinesisFirehoseOutput_: Optional['KinesisFirehoseOutput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisfirehoseoutput""", alias="KinesisFirehoseOutput")
    KinesisStreamsOutput_: Optional['KinesisStreamsOutput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisstreamsoutput""", alias="KinesisStreamsOutput")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.Output:
        from troposphere.kinesisanalyticsv2 import Output as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CSVMappingParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html
    Properties:
        - Name: RecordRowDelimiter
        - Name: RecordColumnDelimiter
    
    """
    
    RecordRowDelimiter_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter""", alias="RecordRowDelimiter")
    RecordColumnDelimiter_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter""", alias="RecordColumnDelimiter")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.CSVMappingParameters:
        from troposphere.kinesisanalyticsv2 import CSVMappingParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JSONMappingParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html
    Properties:
        - Name: RecordRowPath
    
    """
    
    RecordRowPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters-recordrowpath""", alias="RecordRowPath")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.JSONMappingParameters:
        from troposphere.kinesisanalyticsv2 import JSONMappingParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MappingParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html
    Properties:
        - Name: JSONMappingParameters
        - Name: CSVMappingParameters
    
    """
    
    JSONMappingParameters_: Optional['JSONMappingParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-jsonmappingparameters""", alias="JSONMappingParameters")
    CSVMappingParameters_: Optional['CSVMappingParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-csvmappingparameters""", alias="CSVMappingParameters")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.MappingParameters:
        from troposphere.kinesisanalyticsv2 import MappingParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecordColumn(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html
    Properties:
        - Name: Mapping
        - Name: SqlType
        - Name: Name
    
    """
    
    Mapping_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-mapping""", alias="Mapping")
    SqlType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-sqltype""", alias="SqlType")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.RecordColumn:
        from troposphere.kinesisanalyticsv2 import RecordColumn as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecordFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html
    Properties:
        - Name: MappingParameters
        - Name: RecordFormatType
    
    """
    
    MappingParameters_: Optional['MappingParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordformat-mappingparameters""", alias="MappingParameters")
    RecordFormatType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordformat-recordformattype""", alias="RecordFormatType")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.RecordFormat:
        from troposphere.kinesisanalyticsv2 import RecordFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReferenceDataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html
    Properties:
        - Name: ReferenceSchema
        - Name: TableName
        - Name: S3ReferenceDataSource
    
    """
    
    ReferenceSchema_: 'ReferenceSchema' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-referenceschema""", alias="ReferenceSchema")
    TableName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-tablename""", alias="TableName")
    S3ReferenceDataSource_: Optional['S3ReferenceDataSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-s3referencedatasource""", alias="S3ReferenceDataSource")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.ReferenceDataSource:
        from troposphere.kinesisanalyticsv2 import ReferenceDataSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReferenceSchema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html
    Properties:
        - Name: RecordEncoding
        - Name: RecordColumns
        - Name: RecordFormat
    
    """
    
    RecordEncoding_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordencoding""", alias="RecordEncoding")
    RecordColumns_: List['RecordColumn'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordcolumns""", alias="RecordColumns")
    RecordFormat_: 'RecordFormat' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordformat""", alias="RecordFormat")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.ReferenceSchema:
        from troposphere.kinesisanalyticsv2 import ReferenceSchema as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3ReferenceDataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html
    Properties:
        - Name: BucketARN
        - Name: FileKey
    
    """
    
    BucketARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-bucketarn""", alias="BucketARN")
    FileKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-filekey""", alias="FileKey")
    


    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.S3ReferenceDataSource:
        from troposphere.kinesisanalyticsv2 import S3ReferenceDataSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Application(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html
    Properties:
        - Name: ApplicationName
        - Name: RuntimeEnvironment
        - Name: RunConfiguration
        - Name: ApplicationMode
        - Name: ApplicationMaintenanceConfiguration
        - Name: ApplicationConfiguration
        - Name: ApplicationDescription
        - Name: Tags
        - Name: ServiceExecutionRole
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApplicationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationname""", alias="ApplicationName")
    RuntimeEnvironment_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runtimeenvironment""", alias="RuntimeEnvironment")
    RunConfiguration_: Optional['RunConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runconfiguration""", alias="RunConfiguration")
    ApplicationMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationmode""", alias="ApplicationMode")
    ApplicationMaintenanceConfiguration_: Optional['ApplicationMaintenanceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration""", alias="ApplicationMaintenanceConfiguration")
    ApplicationConfiguration_: Optional['ApplicationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationconfiguration""", alias="ApplicationConfiguration")
    ApplicationDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationdescription""", alias="ApplicationDescription")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-tags""", alias="Tags")
    ServiceExecutionRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-serviceexecutionrole""", alias="ServiceExecutionRole")
    

    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.Application:
        from troposphere.kinesisanalyticsv2 import Application as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kinesisanalyticsv2 import Application as TropoT
        return resource_to_troposphere(self, TropoT)


class ApplicationCloudWatchLoggingOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html
    Properties:
        - Name: ApplicationName
        - Name: CloudWatchLoggingOption
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApplicationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-applicationname""", alias="ApplicationName")
    CloudWatchLoggingOption_: 'CloudWatchLoggingOption' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption""", alias="CloudWatchLoggingOption")
    

    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.ApplicationCloudWatchLoggingOption:
        from troposphere.kinesisanalyticsv2 import ApplicationCloudWatchLoggingOption as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kinesisanalyticsv2 import ApplicationCloudWatchLoggingOption as TropoT
        return resource_to_troposphere(self, TropoT)


class ApplicationOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html
    Properties:
        - Name: ApplicationName
        - Name: Output
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApplicationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-applicationname""", alias="ApplicationName")
    Output_: 'Output' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-output""", alias="Output")
    

    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.ApplicationOutput:
        from troposphere.kinesisanalyticsv2 import ApplicationOutput as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kinesisanalyticsv2 import ApplicationOutput as TropoT
        return resource_to_troposphere(self, TropoT)


class ApplicationReferenceDataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html
    Properties:
        - Name: ApplicationName
        - Name: ReferenceDataSource
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApplicationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-applicationname""", alias="ApplicationName")
    ReferenceDataSource_: 'ReferenceDataSource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource""", alias="ReferenceDataSource")
    

    @property
    def tropo_type(self) -> troposphere.kinesisanalyticsv2.ApplicationReferenceDataSource:
        from troposphere.kinesisanalyticsv2 import ApplicationReferenceDataSource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kinesisanalyticsv2 import ApplicationReferenceDataSource as TropoT
        return resource_to_troposphere(self, TropoT)

