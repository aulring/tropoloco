from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ResourceSpec(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-app-resourcespec.html
    Properties:
        - Name: SageMakerImageArn
        - Name: InstanceType
        - Name: SageMakerImageVersionArn
    
    """
    
    SageMakerImageArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-app-resourcespec.html#cfn-sagemaker-app-resourcespec-sagemakerimagearn""", alias="SageMakerImageArn")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-app-resourcespec.html#cfn-sagemaker-app-resourcespec-instancetype""", alias="InstanceType")
    SageMakerImageVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-app-resourcespec.html#cfn-sagemaker-app-resourcespec-sagemakerimageversionarn""", alias="SageMakerImageVersionArn")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ResourceSpec:
        from troposphere.sagemaker import ResourceSpec as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FileSystemConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-filesystemconfig.html
    Properties:
        - Name: MountPath
        - Name: DefaultGid
        - Name: DefaultUid
    
    """
    
    MountPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-filesystemconfig.html#cfn-sagemaker-appimageconfig-filesystemconfig-mountpath""", alias="MountPath")
    DefaultGid_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-filesystemconfig.html#cfn-sagemaker-appimageconfig-filesystemconfig-defaultgid""", alias="DefaultGid")
    DefaultUid_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-filesystemconfig.html#cfn-sagemaker-appimageconfig-filesystemconfig-defaultuid""", alias="DefaultUid")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.FileSystemConfig:
        from troposphere.sagemaker import FileSystemConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KernelGatewayImageConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig.html
    Properties:
        - Name: KernelSpecs
        - Name: FileSystemConfig
    
    """
    
    KernelSpecs_: List['KernelSpec'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig.html#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig-kernelspecs""", alias="KernelSpecs")
    FileSystemConfig_: Optional['FileSystemConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig.html#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig-filesystemconfig""", alias="FileSystemConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.KernelGatewayImageConfig:
        from troposphere.sagemaker import KernelGatewayImageConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KernelSpec(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelspec.html
    Properties:
        - Name: DisplayName
        - Name: Name
    
    """
    
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelspec.html#cfn-sagemaker-appimageconfig-kernelspec-displayname""", alias="DisplayName")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelspec.html#cfn-sagemaker-appimageconfig-kernelspec-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.KernelSpec:
        from troposphere.sagemaker import KernelSpec as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GitConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html
    Properties:
        - Name: SecretArn
        - Name: Branch
        - Name: RepositoryUrl
    
    """
    
    SecretArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html#cfn-sagemaker-coderepository-gitconfig-secretarn""", alias="SecretArn")
    Branch_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html#cfn-sagemaker-coderepository-gitconfig-branch""", alias="Branch")
    RepositoryUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html#cfn-sagemaker-coderepository-gitconfig-repositoryurl""", alias="RepositoryUrl")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.GitConfig:
        from troposphere.sagemaker import GitConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchTransformInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-batchtransforminput.html
    Properties:
        - Name: DatasetFormat
        - Name: S3DataDistributionType
        - Name: DataCapturedDestinationS3Uri
        - Name: S3InputMode
        - Name: LocalPath
        - Name: ExcludeFeaturesAttribute
    
    """
    
    DatasetFormat_: 'DatasetFormat' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-dataqualityjobdefinition-batchtransforminput-datasetformat""", alias="DatasetFormat")
    S3DataDistributionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-dataqualityjobdefinition-batchtransforminput-s3datadistributiontype""", alias="S3DataDistributionType")
    DataCapturedDestinationS3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-dataqualityjobdefinition-batchtransforminput-datacaptureddestinations3uri""", alias="DataCapturedDestinationS3Uri")
    S3InputMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-dataqualityjobdefinition-batchtransforminput-s3inputmode""", alias="S3InputMode")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-dataqualityjobdefinition-batchtransforminput-localpath""", alias="LocalPath")
    ExcludeFeaturesAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-dataqualityjobdefinition-batchtransforminput-excludefeaturesattribute""", alias="ExcludeFeaturesAttribute")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.BatchTransformInput:
        from troposphere.sagemaker import BatchTransformInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClusterConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html
    Properties:
        - Name: InstanceCount
        - Name: VolumeSizeInGB
        - Name: VolumeKmsKeyId
        - Name: InstanceType
    
    """
    
    InstanceCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-instancecount""", alias="InstanceCount")
    VolumeSizeInGB_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-volumesizeingb""", alias="VolumeSizeInGB")
    VolumeKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-volumekmskeyid""", alias="VolumeKmsKeyId")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-instancetype""", alias="InstanceType")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ClusterConfig:
        from troposphere.sagemaker import ClusterConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConstraintsResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource.html
    Properties:
        - Name: S3Uri
    
    """
    
    S3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource.html#cfn-sagemaker-dataqualityjobdefinition-constraintsresource-s3uri""", alias="S3Uri")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ConstraintsResource:
        from troposphere.sagemaker import ConstraintsResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Csv(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-csv.html
    Properties:
        - Name: Header
    
    """
    
    Header_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-csv.html#cfn-sagemaker-dataqualityjobdefinition-csv-header""", alias="Header")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Csv:
        from troposphere.sagemaker import Csv as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataQualityAppSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html
    Properties:
        - Name: ContainerEntrypoint
        - Name: PostAnalyticsProcessorSourceUri
        - Name: RecordPreprocessorSourceUri
        - Name: Environment
        - Name: ImageUri
        - Name: ContainerArguments
    
    """
    
    ContainerEntrypoint_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-containerentrypoint""", alias="ContainerEntrypoint")
    PostAnalyticsProcessorSourceUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-postanalyticsprocessorsourceuri""", alias="PostAnalyticsProcessorSourceUri")
    RecordPreprocessorSourceUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-recordpreprocessorsourceuri""", alias="RecordPreprocessorSourceUri")
    Environment_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-environment""", alias="Environment")
    ImageUri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-imageuri""", alias="ImageUri")
    ContainerArguments_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-containerarguments""", alias="ContainerArguments")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DataQualityAppSpecification:
        from troposphere.sagemaker import DataQualityAppSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataQualityBaselineConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html
    Properties:
        - Name: StatisticsResource
        - Name: ConstraintsResource
        - Name: BaseliningJobName
    
    """
    
    StatisticsResource_: Optional['StatisticsResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig-statisticsresource""", alias="StatisticsResource")
    ConstraintsResource_: Optional['ConstraintsResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig-constraintsresource""", alias="ConstraintsResource")
    BaseliningJobName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig-baseliningjobname""", alias="BaseliningJobName")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DataQualityBaselineConfig:
        from troposphere.sagemaker import DataQualityBaselineConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataQualityJobInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput.html
    Properties:
        - Name: BatchTransformInput
        - Name: EndpointInput
    
    """
    
    BatchTransformInput_: Optional['BatchTransformInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput-batchtransforminput""", alias="BatchTransformInput")
    EndpointInput_: Optional['EndpointInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput-endpointinput""", alias="EndpointInput")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DataQualityJobInput:
        from troposphere.sagemaker import DataQualityJobInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatasetFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-datasetformat.html
    Properties:
        - Name: Parquet
        - Name: Csv
        - Name: Json
    
    """
    
    Parquet_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-datasetformat.html#cfn-sagemaker-dataqualityjobdefinition-datasetformat-parquet""", alias="Parquet")
    Csv_: Optional['Csv'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-datasetformat.html#cfn-sagemaker-dataqualityjobdefinition-datasetformat-csv""", alias="Csv")
    Json_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-datasetformat.html#cfn-sagemaker-dataqualityjobdefinition-datasetformat-json""", alias="Json")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DatasetFormat:
        from troposphere.sagemaker import DatasetFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EndpointInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html
    Properties:
        - Name: S3DataDistributionType
        - Name: EndpointName
        - Name: S3InputMode
        - Name: LocalPath
        - Name: ExcludeFeaturesAttribute
    
    """
    
    S3DataDistributionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3datadistributiontype""", alias="S3DataDistributionType")
    EndpointName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-endpointname""", alias="EndpointName")
    S3InputMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3inputmode""", alias="S3InputMode")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-localpath""", alias="LocalPath")
    ExcludeFeaturesAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-excludefeaturesattribute""", alias="ExcludeFeaturesAttribute")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.EndpointInput:
        from troposphere.sagemaker import EndpointInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Json(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-json.html
    Properties:
        - Name: Line
    
    """
    
    Line_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-json.html#cfn-sagemaker-dataqualityjobdefinition-json-line""", alias="Line")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Json:
        from troposphere.sagemaker import Json as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutput.html
    Properties:
        - Name: S3Output
    
    """
    
    S3Output_: 'S3Output' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutput.html#cfn-sagemaker-dataqualityjobdefinition-monitoringoutput-s3output""", alias="S3Output")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringOutput:
        from troposphere.sagemaker import MonitoringOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringOutputConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.html
    Properties:
        - Name: KmsKeyId
        - Name: MonitoringOutputs
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-dataqualityjobdefinition-monitoringoutputconfig-kmskeyid""", alias="KmsKeyId")
    MonitoringOutputs_: List['MonitoringOutput'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-dataqualityjobdefinition-monitoringoutputconfig-monitoringoutputs""", alias="MonitoringOutputs")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringOutputConfig:
        from troposphere.sagemaker import MonitoringOutputConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringResources(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringresources.html
    Properties:
        - Name: ClusterConfig
    
    """
    
    ClusterConfig_: 'ClusterConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringresources.html#cfn-sagemaker-dataqualityjobdefinition-monitoringresources-clusterconfig""", alias="ClusterConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringResources:
        from troposphere.sagemaker import MonitoringResources as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html
    Properties:
        - Name: EnableNetworkIsolation
        - Name: EnableInterContainerTrafficEncryption
        - Name: VpcConfig
    
    """
    
    EnableNetworkIsolation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig-enablenetworkisolation""", alias="EnableNetworkIsolation")
    EnableInterContainerTrafficEncryption_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig-enableintercontainertrafficencryption""", alias="EnableInterContainerTrafficEncryption")
    VpcConfig_: Optional['VpcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig-vpcconfig""", alias="VpcConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.NetworkConfig:
        from troposphere.sagemaker import NetworkConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Output(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html
    Properties:
        - Name: S3Uri
        - Name: LocalPath
        - Name: S3UploadMode
    
    """
    
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html#cfn-sagemaker-dataqualityjobdefinition-s3output-s3uri""", alias="S3Uri")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html#cfn-sagemaker-dataqualityjobdefinition-s3output-localpath""", alias="LocalPath")
    S3UploadMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html#cfn-sagemaker-dataqualityjobdefinition-s3output-s3uploadmode""", alias="S3UploadMode")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.S3Output:
        from troposphere.sagemaker import S3Output as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatisticsResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource.html
    Properties:
        - Name: S3Uri
    
    """
    
    S3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource.html#cfn-sagemaker-dataqualityjobdefinition-statisticsresource-s3uri""", alias="S3Uri")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.StatisticsResource:
        from troposphere.sagemaker import StatisticsResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StoppingCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-stoppingcondition.html
    Properties:
        - Name: MaxRuntimeInSeconds
    
    """
    
    MaxRuntimeInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-stoppingcondition.html#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition-maxruntimeinseconds""", alias="MaxRuntimeInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.StoppingCondition:
        from troposphere.sagemaker import StoppingCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-vpcconfig.html
    Properties:
        - Name: Subnets
        - Name: SecurityGroupIds
    
    """
    
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-vpcconfig.html#cfn-sagemaker-dataqualityjobdefinition-vpcconfig-subnets""", alias="Subnets")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-vpcconfig.html#cfn-sagemaker-dataqualityjobdefinition-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.VpcConfig:
        from troposphere.sagemaker import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Device(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html
    Properties:
        - Name: IotThingName
        - Name: Description
        - Name: DeviceName
    
    """
    
    IotThingName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html#cfn-sagemaker-device-device-iotthingname""", alias="IotThingName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html#cfn-sagemaker-device-device-description""", alias="Description")
    DeviceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html#cfn-sagemaker-device-device-devicename""", alias="DeviceName")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Device:
        from troposphere.sagemaker import Device as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EdgeOutputConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html
    Properties:
        - Name: KmsKeyId
        - Name: S3OutputLocation
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html#cfn-sagemaker-devicefleet-edgeoutputconfig-kmskeyid""", alias="KmsKeyId")
    S3OutputLocation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html#cfn-sagemaker-devicefleet-edgeoutputconfig-s3outputlocation""", alias="S3OutputLocation")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.EdgeOutputConfig:
        from troposphere.sagemaker import EdgeOutputConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomImage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-customimage.html
    Properties:
        - Name: ImageName
        - Name: AppImageConfigName
        - Name: ImageVersionNumber
    
    """
    
    ImageName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-customimage.html#cfn-sagemaker-domain-customimage-imagename""", alias="ImageName")
    AppImageConfigName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-customimage.html#cfn-sagemaker-domain-customimage-appimageconfigname""", alias="AppImageConfigName")
    ImageVersionNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-customimage.html#cfn-sagemaker-domain-customimage-imageversionnumber""", alias="ImageVersionNumber")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.CustomImage:
        from troposphere.sagemaker import CustomImage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefaultSpaceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-defaultspacesettings.html
    Properties:
        - Name: SecurityGroups
        - Name: KernelGatewayAppSettings
        - Name: JupyterServerAppSettings
        - Name: ExecutionRole
    
    """
    
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-defaultspacesettings.html#cfn-sagemaker-domain-defaultspacesettings-securitygroups""", alias="SecurityGroups")
    KernelGatewayAppSettings_: Optional['KernelGatewayAppSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-defaultspacesettings.html#cfn-sagemaker-domain-defaultspacesettings-kernelgatewayappsettings""", alias="KernelGatewayAppSettings")
    JupyterServerAppSettings_: Optional['JupyterServerAppSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-defaultspacesettings.html#cfn-sagemaker-domain-defaultspacesettings-jupyterserverappsettings""", alias="JupyterServerAppSettings")
    ExecutionRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-defaultspacesettings.html#cfn-sagemaker-domain-defaultspacesettings-executionrole""", alias="ExecutionRole")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DefaultSpaceSettings:
        from troposphere.sagemaker import DefaultSpaceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DomainSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-domainsettings.html
    Properties:
        - Name: RStudioServerProDomainSettings
        - Name: SecurityGroupIds
    
    """
    
    RStudioServerProDomainSettings_: Optional['RStudioServerProDomainSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-domainsettings.html#cfn-sagemaker-domain-domainsettings-rstudioserverprodomainsettings""", alias="RStudioServerProDomainSettings")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-domainsettings.html#cfn-sagemaker-domain-domainsettings-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DomainSettings:
        from troposphere.sagemaker import DomainSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JupyterServerAppSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-jupyterserverappsettings.html
    Properties:
        - Name: DefaultResourceSpec
    
    """
    
    DefaultResourceSpec_: Optional['ResourceSpec'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-jupyterserverappsettings.html#cfn-sagemaker-domain-jupyterserverappsettings-defaultresourcespec""", alias="DefaultResourceSpec")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.JupyterServerAppSettings:
        from troposphere.sagemaker import JupyterServerAppSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KernelGatewayAppSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-kernelgatewayappsettings.html
    Properties:
        - Name: CustomImages
        - Name: DefaultResourceSpec
    
    """
    
    CustomImages_: Optional[List['CustomImage']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-kernelgatewayappsettings.html#cfn-sagemaker-domain-kernelgatewayappsettings-customimages""", alias="CustomImages")
    DefaultResourceSpec_: Optional['ResourceSpec'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-kernelgatewayappsettings.html#cfn-sagemaker-domain-kernelgatewayappsettings-defaultresourcespec""", alias="DefaultResourceSpec")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.KernelGatewayAppSettings:
        from troposphere.sagemaker import KernelGatewayAppSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RSessionAppSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rsessionappsettings.html
    Properties:
        - Name: CustomImages
        - Name: DefaultResourceSpec
    
    """
    
    CustomImages_: Optional[List['CustomImage']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rsessionappsettings.html#cfn-sagemaker-domain-rsessionappsettings-customimages""", alias="CustomImages")
    DefaultResourceSpec_: Optional['ResourceSpec'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rsessionappsettings.html#cfn-sagemaker-domain-rsessionappsettings-defaultresourcespec""", alias="DefaultResourceSpec")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.RSessionAppSettings:
        from troposphere.sagemaker import RSessionAppSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RStudioServerProAppSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rstudioserverproappsettings.html
    Properties:
        - Name: AccessStatus
        - Name: UserGroup
    
    """
    
    AccessStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rstudioserverproappsettings.html#cfn-sagemaker-domain-rstudioserverproappsettings-accessstatus""", alias="AccessStatus")
    UserGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rstudioserverproappsettings.html#cfn-sagemaker-domain-rstudioserverproappsettings-usergroup""", alias="UserGroup")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.RStudioServerProAppSettings:
        from troposphere.sagemaker import RStudioServerProAppSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RStudioServerProDomainSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rstudioserverprodomainsettings.html
    Properties:
        - Name: DomainExecutionRoleArn
        - Name: RStudioConnectUrl
        - Name: DefaultResourceSpec
        - Name: RStudioPackageManagerUrl
    
    """
    
    DomainExecutionRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rstudioserverprodomainsettings.html#cfn-sagemaker-domain-rstudioserverprodomainsettings-domainexecutionrolearn""", alias="DomainExecutionRoleArn")
    RStudioConnectUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rstudioserverprodomainsettings.html#cfn-sagemaker-domain-rstudioserverprodomainsettings-rstudioconnecturl""", alias="RStudioConnectUrl")
    DefaultResourceSpec_: Optional['ResourceSpec'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rstudioserverprodomainsettings.html#cfn-sagemaker-domain-rstudioserverprodomainsettings-defaultresourcespec""", alias="DefaultResourceSpec")
    RStudioPackageManagerUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rstudioserverprodomainsettings.html#cfn-sagemaker-domain-rstudioserverprodomainsettings-rstudiopackagemanagerurl""", alias="RStudioPackageManagerUrl")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.RStudioServerProDomainSettings:
        from troposphere.sagemaker import RStudioServerProDomainSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceSpec(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-resourcespec.html
    Properties:
        - Name: SageMakerImageArn
        - Name: InstanceType
        - Name: LifecycleConfigArn
        - Name: SageMakerImageVersionArn
    
    """
    
    SageMakerImageArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-resourcespec.html#cfn-sagemaker-domain-resourcespec-sagemakerimagearn""", alias="SageMakerImageArn")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-resourcespec.html#cfn-sagemaker-domain-resourcespec-instancetype""", alias="InstanceType")
    LifecycleConfigArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-resourcespec.html#cfn-sagemaker-domain-resourcespec-lifecycleconfigarn""", alias="LifecycleConfigArn")
    SageMakerImageVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-resourcespec.html#cfn-sagemaker-domain-resourcespec-sagemakerimageversionarn""", alias="SageMakerImageVersionArn")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ResourceSpec:
        from troposphere.sagemaker import ResourceSpec as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SharingSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-sharingsettings.html
    Properties:
        - Name: NotebookOutputOption
        - Name: S3KmsKeyId
        - Name: S3OutputPath
    
    """
    
    NotebookOutputOption_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-sharingsettings.html#cfn-sagemaker-domain-sharingsettings-notebookoutputoption""", alias="NotebookOutputOption")
    S3KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-sharingsettings.html#cfn-sagemaker-domain-sharingsettings-s3kmskeyid""", alias="S3KmsKeyId")
    S3OutputPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-sharingsettings.html#cfn-sagemaker-domain-sharingsettings-s3outputpath""", alias="S3OutputPath")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.SharingSettings:
        from troposphere.sagemaker import SharingSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html
    Properties:
        - Name: SecurityGroups
        - Name: KernelGatewayAppSettings
        - Name: RStudioServerProAppSettings
        - Name: RSessionAppSettings
        - Name: JupyterServerAppSettings
        - Name: ExecutionRole
        - Name: SharingSettings
    
    """
    
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-securitygroups""", alias="SecurityGroups")
    KernelGatewayAppSettings_: Optional['KernelGatewayAppSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-kernelgatewayappsettings""", alias="KernelGatewayAppSettings")
    RStudioServerProAppSettings_: Optional['RStudioServerProAppSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-rstudioserverproappsettings""", alias="RStudioServerProAppSettings")
    RSessionAppSettings_: Optional['RSessionAppSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-rsessionappsettings""", alias="RSessionAppSettings")
    JupyterServerAppSettings_: Optional['JupyterServerAppSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-jupyterserverappsettings""", alias="JupyterServerAppSettings")
    ExecutionRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-executionrole""", alias="ExecutionRole")
    SharingSettings_: Optional['SharingSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-sharingsettings""", alias="SharingSettings")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.UserSettings:
        from troposphere.sagemaker import UserSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Alarm(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-alarm.html
    Properties:
        - Name: AlarmName
    
    """
    
    AlarmName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-alarm.html#cfn-sagemaker-endpoint-alarm-alarmname""", alias="AlarmName")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Alarm:
        from troposphere.sagemaker import Alarm as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoRollbackConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-autorollbackconfig.html
    Properties:
        - Name: Alarms
    
    """
    
    Alarms_: List['Alarm'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-autorollbackconfig.html#cfn-sagemaker-endpoint-autorollbackconfig-alarms""", alias="Alarms")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.AutoRollbackConfig:
        from troposphere.sagemaker import AutoRollbackConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BlueGreenUpdatePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html
    Properties:
        - Name: MaximumExecutionTimeoutInSeconds
        - Name: TerminationWaitInSeconds
        - Name: TrafficRoutingConfiguration
    
    """
    
    MaximumExecutionTimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html#cfn-sagemaker-endpoint-bluegreenupdatepolicy-maximumexecutiontimeoutinseconds""", alias="MaximumExecutionTimeoutInSeconds")
    TerminationWaitInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html#cfn-sagemaker-endpoint-bluegreenupdatepolicy-terminationwaitinseconds""", alias="TerminationWaitInSeconds")
    TrafficRoutingConfiguration_: 'TrafficRoutingConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html#cfn-sagemaker-endpoint-bluegreenupdatepolicy-trafficroutingconfiguration""", alias="TrafficRoutingConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.BlueGreenUpdatePolicy:
        from troposphere.sagemaker import BlueGreenUpdatePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacitySize(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html#cfn-sagemaker-endpoint-capacitysize-type""", alias="Type")
    Value_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html#cfn-sagemaker-endpoint-capacitysize-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.CapacitySize:
        from troposphere.sagemaker import CapacitySize as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html
    Properties:
        - Name: AutoRollbackConfiguration
        - Name: RollingUpdatePolicy
        - Name: BlueGreenUpdatePolicy
    
    """
    
    AutoRollbackConfiguration_: Optional['AutoRollbackConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html#cfn-sagemaker-endpoint-deploymentconfig-autorollbackconfiguration""", alias="AutoRollbackConfiguration")
    RollingUpdatePolicy_: Optional['RollingUpdatePolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html#cfn-sagemaker-endpoint-deploymentconfig-rollingupdatepolicy""", alias="RollingUpdatePolicy")
    BlueGreenUpdatePolicy_: Optional['BlueGreenUpdatePolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html#cfn-sagemaker-endpoint-deploymentconfig-bluegreenupdatepolicy""", alias="BlueGreenUpdatePolicy")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DeploymentConfig:
        from troposphere.sagemaker import DeploymentConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RollingUpdatePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-rollingupdatepolicy.html
    Properties:
        - Name: MaximumExecutionTimeoutInSeconds
        - Name: MaximumBatchSize
        - Name: WaitIntervalInSeconds
        - Name: RollbackMaximumBatchSize
    
    """
    
    MaximumExecutionTimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-rollingupdatepolicy.html#cfn-sagemaker-endpoint-rollingupdatepolicy-maximumexecutiontimeoutinseconds""", alias="MaximumExecutionTimeoutInSeconds")
    MaximumBatchSize_: 'CapacitySize' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-rollingupdatepolicy.html#cfn-sagemaker-endpoint-rollingupdatepolicy-maximumbatchsize""", alias="MaximumBatchSize")
    WaitIntervalInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-rollingupdatepolicy.html#cfn-sagemaker-endpoint-rollingupdatepolicy-waitintervalinseconds""", alias="WaitIntervalInSeconds")
    RollbackMaximumBatchSize_: Optional['CapacitySize'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-rollingupdatepolicy.html#cfn-sagemaker-endpoint-rollingupdatepolicy-rollbackmaximumbatchsize""", alias="RollbackMaximumBatchSize")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.RollingUpdatePolicy:
        from troposphere.sagemaker import RollingUpdatePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrafficRoutingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html
    Properties:
        - Name: Type
        - Name: LinearStepSize
        - Name: CanarySize
        - Name: WaitIntervalInSeconds
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-type""", alias="Type")
    LinearStepSize_: Optional['CapacitySize'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-linearstepsize""", alias="LinearStepSize")
    CanarySize_: Optional['CapacitySize'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-canarysize""", alias="CanarySize")
    WaitIntervalInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-waitintervalinseconds""", alias="WaitIntervalInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.TrafficRoutingConfig:
        from troposphere.sagemaker import TrafficRoutingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VariantProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-variantproperty.html
    Properties:
        - Name: VariantPropertyType
    
    """
    
    VariantPropertyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-variantproperty.html#cfn-sagemaker-endpoint-variantproperty-variantpropertytype""", alias="VariantPropertyType")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.VariantProperty:
        from troposphere.sagemaker import VariantProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AsyncInferenceClientConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig.html
    Properties:
        - Name: MaxConcurrentInvocationsPerInstance
    
    """
    
    MaxConcurrentInvocationsPerInstance_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceclientconfig-maxconcurrentinvocationsperinstance""", alias="MaxConcurrentInvocationsPerInstance")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.AsyncInferenceClientConfig:
        from troposphere.sagemaker import AsyncInferenceClientConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AsyncInferenceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceconfig.html
    Properties:
        - Name: OutputConfig
        - Name: ClientConfig
    
    """
    
    OutputConfig_: 'AsyncInferenceOutputConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceconfig-outputconfig""", alias="OutputConfig")
    ClientConfig_: Optional['AsyncInferenceClientConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceconfig-clientconfig""", alias="ClientConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.AsyncInferenceConfig:
        from troposphere.sagemaker import AsyncInferenceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AsyncInferenceNotificationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig.html
    Properties:
        - Name: IncludeInferenceResponseIn
        - Name: SuccessTopic
        - Name: ErrorTopic
    
    """
    
    IncludeInferenceResponseIn_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig.html#cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-includeinferenceresponsein""", alias="IncludeInferenceResponseIn")
    SuccessTopic_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig.html#cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-successtopic""", alias="SuccessTopic")
    ErrorTopic_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig.html#cfn-sagemaker-endpointconfig-asyncinferencenotificationconfig-errortopic""", alias="ErrorTopic")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.AsyncInferenceNotificationConfig:
        from troposphere.sagemaker import AsyncInferenceNotificationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AsyncInferenceOutputConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.html
    Properties:
        - Name: KmsKeyId
        - Name: NotificationConfig
        - Name: S3OutputPath
        - Name: S3FailurePath
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-kmskeyid""", alias="KmsKeyId")
    NotificationConfig_: Optional['AsyncInferenceNotificationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-notificationconfig""", alias="NotificationConfig")
    S3OutputPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-s3outputpath""", alias="S3OutputPath")
    S3FailurePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceoutputconfig-s3failurepath""", alias="S3FailurePath")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.AsyncInferenceOutputConfig:
        from troposphere.sagemaker import AsyncInferenceOutputConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CaptureContentTypeHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html
    Properties:
        - Name: JsonContentTypes
        - Name: CsvContentTypes
    
    """
    
    JsonContentTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader-jsoncontenttypes""", alias="JsonContentTypes")
    CsvContentTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader-csvcontenttypes""", alias="CsvContentTypes")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.CaptureContentTypeHeader:
        from troposphere.sagemaker import CaptureContentTypeHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CaptureOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-captureoption.html
    Properties:
        - Name: CaptureMode
    
    """
    
    CaptureMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-captureoption.html#cfn-sagemaker-endpointconfig-captureoption-capturemode""", alias="CaptureMode")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.CaptureOption:
        from troposphere.sagemaker import CaptureOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClarifyExplainerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig.html
    Properties:
        - Name: InferenceConfig
        - Name: EnableExplanations
        - Name: ShapConfig
    
    """
    
    InferenceConfig_: Optional['ClarifyInferenceConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig.html#cfn-sagemaker-endpointconfig-clarifyexplainerconfig-inferenceconfig""", alias="InferenceConfig")
    EnableExplanations_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig.html#cfn-sagemaker-endpointconfig-clarifyexplainerconfig-enableexplanations""", alias="EnableExplanations")
    ShapConfig_: 'ClarifyShapConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig.html#cfn-sagemaker-endpointconfig-clarifyexplainerconfig-shapconfig""", alias="ShapConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ClarifyExplainerConfig:
        from troposphere.sagemaker import ClarifyExplainerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClarifyFeatureType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyfeaturetype.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.sagemaker.ClarifyFeatureType:
        from troposphere.sagemaker import ClarifyFeatureType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClarifyHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyheader.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.sagemaker.ClarifyHeader:
        from troposphere.sagemaker import ClarifyHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClarifyInferenceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html
    Properties:
        - Name: ContentTemplate
        - Name: LabelHeaders
        - Name: MaxPayloadInMB
        - Name: ProbabilityIndex
        - Name: LabelAttribute
        - Name: FeatureTypes
        - Name: FeatureHeaders
        - Name: LabelIndex
        - Name: ProbabilityAttribute
        - Name: FeaturesAttribute
        - Name: MaxRecordCount
    
    """
    
    ContentTemplate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html#cfn-sagemaker-endpointconfig-clarifyinferenceconfig-contenttemplate""", alias="ContentTemplate")
    LabelHeaders_: Optional[List['ClarifyHeader']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html#cfn-sagemaker-endpointconfig-clarifyinferenceconfig-labelheaders""", alias="LabelHeaders")
    MaxPayloadInMB_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html#cfn-sagemaker-endpointconfig-clarifyinferenceconfig-maxpayloadinmb""", alias="MaxPayloadInMB")
    ProbabilityIndex_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html#cfn-sagemaker-endpointconfig-clarifyinferenceconfig-probabilityindex""", alias="ProbabilityIndex")
    LabelAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html#cfn-sagemaker-endpointconfig-clarifyinferenceconfig-labelattribute""", alias="LabelAttribute")
    FeatureTypes_: Optional[List['ClarifyFeatureType']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html#cfn-sagemaker-endpointconfig-clarifyinferenceconfig-featuretypes""", alias="FeatureTypes")
    FeatureHeaders_: Optional[List['ClarifyHeader']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html#cfn-sagemaker-endpointconfig-clarifyinferenceconfig-featureheaders""", alias="FeatureHeaders")
    LabelIndex_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html#cfn-sagemaker-endpointconfig-clarifyinferenceconfig-labelindex""", alias="LabelIndex")
    ProbabilityAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html#cfn-sagemaker-endpointconfig-clarifyinferenceconfig-probabilityattribute""", alias="ProbabilityAttribute")
    FeaturesAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html#cfn-sagemaker-endpointconfig-clarifyinferenceconfig-featuresattribute""", alias="FeaturesAttribute")
    MaxRecordCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html#cfn-sagemaker-endpointconfig-clarifyinferenceconfig-maxrecordcount""", alias="MaxRecordCount")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ClarifyInferenceConfig:
        from troposphere.sagemaker import ClarifyInferenceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClarifyShapBaselineConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig.html
    Properties:
        - Name: ShapBaseline
        - Name: ShapBaselineUri
        - Name: MimeType
    
    """
    
    ShapBaseline_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig.html#cfn-sagemaker-endpointconfig-clarifyshapbaselineconfig-shapbaseline""", alias="ShapBaseline")
    ShapBaselineUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig.html#cfn-sagemaker-endpointconfig-clarifyshapbaselineconfig-shapbaselineuri""", alias="ShapBaselineUri")
    MimeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig.html#cfn-sagemaker-endpointconfig-clarifyshapbaselineconfig-mimetype""", alias="MimeType")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ClarifyShapBaselineConfig:
        from troposphere.sagemaker import ClarifyShapBaselineConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClarifyShapConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapconfig.html
    Properties:
        - Name: TextConfig
        - Name: UseLogit
        - Name: Seed
        - Name: ShapBaselineConfig
        - Name: NumberOfSamples
    
    """
    
    TextConfig_: Optional['ClarifyTextConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapconfig.html#cfn-sagemaker-endpointconfig-clarifyshapconfig-textconfig""", alias="TextConfig")
    UseLogit_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapconfig.html#cfn-sagemaker-endpointconfig-clarifyshapconfig-uselogit""", alias="UseLogit")
    Seed_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapconfig.html#cfn-sagemaker-endpointconfig-clarifyshapconfig-seed""", alias="Seed")
    ShapBaselineConfig_: 'ClarifyShapBaselineConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapconfig.html#cfn-sagemaker-endpointconfig-clarifyshapconfig-shapbaselineconfig""", alias="ShapBaselineConfig")
    NumberOfSamples_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapconfig.html#cfn-sagemaker-endpointconfig-clarifyshapconfig-numberofsamples""", alias="NumberOfSamples")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ClarifyShapConfig:
        from troposphere.sagemaker import ClarifyShapConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClarifyTextConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifytextconfig.html
    Properties:
        - Name: Language
        - Name: Granularity
    
    """
    
    Language_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifytextconfig.html#cfn-sagemaker-endpointconfig-clarifytextconfig-language""", alias="Language")
    Granularity_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifytextconfig.html#cfn-sagemaker-endpointconfig-clarifytextconfig-granularity""", alias="Granularity")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ClarifyTextConfig:
        from troposphere.sagemaker import ClarifyTextConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataCaptureConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html
    Properties:
        - Name: CaptureOptions
        - Name: KmsKeyId
        - Name: DestinationS3Uri
        - Name: InitialSamplingPercentage
        - Name: CaptureContentTypeHeader
        - Name: EnableCapture
    
    """
    
    CaptureOptions_: List['CaptureOption'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-captureoptions""", alias="CaptureOptions")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-kmskeyid""", alias="KmsKeyId")
    DestinationS3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-destinations3uri""", alias="DestinationS3Uri")
    InitialSamplingPercentage_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-initialsamplingpercentage""", alias="InitialSamplingPercentage")
    CaptureContentTypeHeader_: Optional['CaptureContentTypeHeader'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader""", alias="CaptureContentTypeHeader")
    EnableCapture_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-enablecapture""", alias="EnableCapture")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DataCaptureConfig:
        from troposphere.sagemaker import DataCaptureConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExplainerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-explainerconfig.html
    Properties:
        - Name: ClarifyExplainerConfig
    
    """
    
    ClarifyExplainerConfig_: Optional['ClarifyExplainerConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-explainerconfig.html#cfn-sagemaker-endpointconfig-explainerconfig-clarifyexplainerconfig""", alias="ClarifyExplainerConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ExplainerConfig:
        from troposphere.sagemaker import ExplainerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ManagedInstanceScaling(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-managedinstancescaling.html
    Properties:
        - Name: Status
        - Name: MaxInstanceCount
        - Name: MinInstanceCount
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-managedinstancescaling.html#cfn-sagemaker-endpointconfig-productionvariant-managedinstancescaling-status""", alias="Status")
    MaxInstanceCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-managedinstancescaling.html#cfn-sagemaker-endpointconfig-productionvariant-managedinstancescaling-maxinstancecount""", alias="MaxInstanceCount")
    MinInstanceCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-managedinstancescaling.html#cfn-sagemaker-endpointconfig-productionvariant-managedinstancescaling-mininstancecount""", alias="MinInstanceCount")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ManagedInstanceScaling:
        from troposphere.sagemaker import ManagedInstanceScaling as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProductionVariant(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html
    Properties:
        - Name: ManagedInstanceScaling
        - Name: ModelName
        - Name: VolumeSizeInGB
        - Name: EnableSSMAccess
        - Name: VariantName
        - Name: InitialInstanceCount
        - Name: RoutingConfig
        - Name: AcceleratorType
        - Name: InitialVariantWeight
        - Name: ModelDataDownloadTimeoutInSeconds
        - Name: ContainerStartupHealthCheckTimeoutInSeconds
        - Name: ServerlessConfig
        - Name: InstanceType
    
    """
    
    ManagedInstanceScaling_: Optional['ManagedInstanceScaling'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-managedinstancescaling""", alias="ManagedInstanceScaling")
    ModelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-modelname""", alias="ModelName")
    VolumeSizeInGB_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-volumesizeingb""", alias="VolumeSizeInGB")
    EnableSSMAccess_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-enablessmaccess""", alias="EnableSSMAccess")
    VariantName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-variantname""", alias="VariantName")
    InitialInstanceCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-initialinstancecount""", alias="InitialInstanceCount")
    RoutingConfig_: Optional['RoutingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-routingconfig""", alias="RoutingConfig")
    AcceleratorType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-acceleratortype""", alias="AcceleratorType")
    InitialVariantWeight_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-initialvariantweight""", alias="InitialVariantWeight")
    ModelDataDownloadTimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-modeldatadownloadtimeoutinseconds""", alias="ModelDataDownloadTimeoutInSeconds")
    ContainerStartupHealthCheckTimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-containerstartuphealthchecktimeoutinseconds""", alias="ContainerStartupHealthCheckTimeoutInSeconds")
    ServerlessConfig_: Optional['ServerlessConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-serverlessconfig""", alias="ServerlessConfig")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-instancetype""", alias="InstanceType")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ProductionVariant:
        from troposphere.sagemaker import ProductionVariant as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RoutingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-routingconfig.html
    Properties:
        - Name: RoutingStrategy
    
    """
    
    RoutingStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-routingconfig.html#cfn-sagemaker-endpointconfig-productionvariant-routingconfig-routingstrategy""", alias="RoutingStrategy")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.RoutingConfig:
        from troposphere.sagemaker import RoutingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServerlessConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-serverlessconfig.html
    Properties:
        - Name: MaxConcurrency
        - Name: MemorySizeInMB
        - Name: ProvisionedConcurrency
    
    """
    
    MaxConcurrency_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-serverlessconfig.html#cfn-sagemaker-endpointconfig-productionvariant-serverlessconfig-maxconcurrency""", alias="MaxConcurrency")
    MemorySizeInMB_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-serverlessconfig.html#cfn-sagemaker-endpointconfig-productionvariant-serverlessconfig-memorysizeinmb""", alias="MemorySizeInMB")
    ProvisionedConcurrency_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-serverlessconfig.html#cfn-sagemaker-endpointconfig-productionvariant-serverlessconfig-provisionedconcurrency""", alias="ProvisionedConcurrency")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ServerlessConfig:
        from troposphere.sagemaker import ServerlessConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-vpcconfig.html
    Properties:
        - Name: Subnets
        - Name: SecurityGroupIds
    
    """
    
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-vpcconfig.html#cfn-sagemaker-endpointconfig-vpcconfig-subnets""", alias="Subnets")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-vpcconfig.html#cfn-sagemaker-endpointconfig-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.VpcConfig:
        from troposphere.sagemaker import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataCatalogConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-datacatalogconfig.html
    Properties:
        - Name: TableName
        - Name: Database
        - Name: Catalog
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-datacatalogconfig.html#cfn-sagemaker-featuregroup-datacatalogconfig-tablename""", alias="TableName")
    Database_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-datacatalogconfig.html#cfn-sagemaker-featuregroup-datacatalogconfig-database""", alias="Database")
    Catalog_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-datacatalogconfig.html#cfn-sagemaker-featuregroup-datacatalogconfig-catalog""", alias="Catalog")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DataCatalogConfig:
        from troposphere.sagemaker import DataCatalogConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FeatureDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-featuredefinition.html
    Properties:
        - Name: FeatureType
        - Name: FeatureName
    
    """
    
    FeatureType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-featuredefinition.html#cfn-sagemaker-featuregroup-featuredefinition-featuretype""", alias="FeatureType")
    FeatureName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-featuredefinition.html#cfn-sagemaker-featuregroup-featuredefinition-featurename""", alias="FeatureName")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.FeatureDefinition:
        from troposphere.sagemaker import FeatureDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OfflineStoreConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-offlinestoreconfig.html
    Properties:
        - Name: DataCatalogConfig
        - Name: S3StorageConfig
        - Name: DisableGlueTableCreation
        - Name: TableFormat
    
    """
    
    DataCatalogConfig_: Optional['DataCatalogConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-offlinestoreconfig.html#cfn-sagemaker-featuregroup-offlinestoreconfig-datacatalogconfig""", alias="DataCatalogConfig")
    S3StorageConfig_: 'S3StorageConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-offlinestoreconfig.html#cfn-sagemaker-featuregroup-offlinestoreconfig-s3storageconfig""", alias="S3StorageConfig")
    DisableGlueTableCreation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-offlinestoreconfig.html#cfn-sagemaker-featuregroup-offlinestoreconfig-disablegluetablecreation""", alias="DisableGlueTableCreation")
    TableFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-offlinestoreconfig.html#cfn-sagemaker-featuregroup-offlinestoreconfig-tableformat""", alias="TableFormat")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.OfflineStoreConfig:
        from troposphere.sagemaker import OfflineStoreConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnlineStoreConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-onlinestoreconfig.html
    Properties:
        - Name: EnableOnlineStore
        - Name: SecurityConfig
    
    """
    
    EnableOnlineStore_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-onlinestoreconfig.html#cfn-sagemaker-featuregroup-onlinestoreconfig-enableonlinestore""", alias="EnableOnlineStore")
    SecurityConfig_: Optional['OnlineStoreSecurityConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-onlinestoreconfig.html#cfn-sagemaker-featuregroup-onlinestoreconfig-securityconfig""", alias="SecurityConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.OnlineStoreConfig:
        from troposphere.sagemaker import OnlineStoreConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnlineStoreSecurityConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-onlinestoresecurityconfig.html
    Properties:
        - Name: KmsKeyId
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-onlinestoresecurityconfig.html#cfn-sagemaker-featuregroup-onlinestoresecurityconfig-kmskeyid""", alias="KmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.OnlineStoreSecurityConfig:
        from troposphere.sagemaker import OnlineStoreSecurityConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3StorageConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-s3storageconfig.html
    Properties:
        - Name: KmsKeyId
        - Name: S3Uri
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-s3storageconfig.html#cfn-sagemaker-featuregroup-s3storageconfig-kmskeyid""", alias="KmsKeyId")
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-s3storageconfig.html#cfn-sagemaker-featuregroup-s3storageconfig-s3uri""", alias="S3Uri")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.S3StorageConfig:
        from troposphere.sagemaker import S3StorageConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeployedImage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-deployedimage.html
    Properties:
        - Name: ResolutionTime
        - Name: SpecifiedImage
        - Name: ResolvedImage
    
    """
    
    ResolutionTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-deployedimage.html#cfn-sagemaker-inferencecomponent-deployedimage-resolutiontime""", alias="ResolutionTime")
    SpecifiedImage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-deployedimage.html#cfn-sagemaker-inferencecomponent-deployedimage-specifiedimage""", alias="SpecifiedImage")
    ResolvedImage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-deployedimage.html#cfn-sagemaker-inferencecomponent-deployedimage-resolvedimage""", alias="ResolvedImage")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DeployedImage:
        from troposphere.sagemaker import DeployedImage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InferenceComponentComputeResourceRequirements(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements.html
    Properties:
        - Name: NumberOfAcceleratorDevicesRequired
        - Name: MaxMemoryRequiredInMb
        - Name: MinMemoryRequiredInMb
        - Name: NumberOfCpuCoresRequired
    
    """
    
    NumberOfAcceleratorDevicesRequired_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements.html#cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-numberofacceleratordevicesrequired""", alias="NumberOfAcceleratorDevicesRequired")
    MaxMemoryRequiredInMb_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements.html#cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-maxmemoryrequiredinmb""", alias="MaxMemoryRequiredInMb")
    MinMemoryRequiredInMb_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements.html#cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-minmemoryrequiredinmb""", alias="MinMemoryRequiredInMb")
    NumberOfCpuCoresRequired_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements.html#cfn-sagemaker-inferencecomponent-inferencecomponentcomputeresourcerequirements-numberofcpucoresrequired""", alias="NumberOfCpuCoresRequired")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.InferenceComponentComputeResourceRequirements:
        from troposphere.sagemaker import InferenceComponentComputeResourceRequirements as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InferenceComponentContainerSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecification.html
    Properties:
        - Name: ArtifactUrl
        - Name: Environment
        - Name: DeployedImage
        - Name: Image
    
    """
    
    ArtifactUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecification.html#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-artifacturl""", alias="ArtifactUrl")
    Environment_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecification.html#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-environment""", alias="Environment")
    DeployedImage_: Optional['DeployedImage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecification.html#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-deployedimage""", alias="DeployedImage")
    Image_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentcontainerspecification.html#cfn-sagemaker-inferencecomponent-inferencecomponentcontainerspecification-image""", alias="Image")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.InferenceComponentContainerSpecification:
        from troposphere.sagemaker import InferenceComponentContainerSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InferenceComponentRuntimeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentruntimeconfig.html
    Properties:
        - Name: CurrentCopyCount
        - Name: DesiredCopyCount
        - Name: CopyCount
    
    """
    
    CurrentCopyCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentruntimeconfig.html#cfn-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-currentcopycount""", alias="CurrentCopyCount")
    DesiredCopyCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentruntimeconfig.html#cfn-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-desiredcopycount""", alias="DesiredCopyCount")
    CopyCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentruntimeconfig.html#cfn-sagemaker-inferencecomponent-inferencecomponentruntimeconfig-copycount""", alias="CopyCount")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.InferenceComponentRuntimeConfig:
        from troposphere.sagemaker import InferenceComponentRuntimeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InferenceComponentSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentspecification.html
    Properties:
        - Name: Container
        - Name: ModelName
        - Name: ComputeResourceRequirements
        - Name: StartupParameters
    
    """
    
    Container_: Optional['InferenceComponentContainerSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentspecification.html#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-container""", alias="Container")
    ModelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentspecification.html#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-modelname""", alias="ModelName")
    ComputeResourceRequirements_: 'InferenceComponentComputeResourceRequirements' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentspecification.html#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-computeresourcerequirements""", alias="ComputeResourceRequirements")
    StartupParameters_: Optional['InferenceComponentStartupParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentspecification.html#cfn-sagemaker-inferencecomponent-inferencecomponentspecification-startupparameters""", alias="StartupParameters")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.InferenceComponentSpecification:
        from troposphere.sagemaker import InferenceComponentSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InferenceComponentStartupParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentstartupparameters.html
    Properties:
        - Name: ModelDataDownloadTimeoutInSeconds
        - Name: ContainerStartupHealthCheckTimeoutInSeconds
    
    """
    
    ModelDataDownloadTimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentstartupparameters.html#cfn-sagemaker-inferencecomponent-inferencecomponentstartupparameters-modeldatadownloadtimeoutinseconds""", alias="ModelDataDownloadTimeoutInSeconds")
    ContainerStartupHealthCheckTimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferencecomponent-inferencecomponentstartupparameters.html#cfn-sagemaker-inferencecomponent-inferencecomponentstartupparameters-containerstartuphealthchecktimeoutinseconds""", alias="ContainerStartupHealthCheckTimeoutInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.InferenceComponentStartupParameters:
        from troposphere.sagemaker import InferenceComponentStartupParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CaptureContentTypeHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-capturecontenttypeheader.html
    Properties:
        - Name: JsonContentTypes
        - Name: CsvContentTypes
    
    """
    
    JsonContentTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-capturecontenttypeheader.html#cfn-sagemaker-inferenceexperiment-capturecontenttypeheader-jsoncontenttypes""", alias="JsonContentTypes")
    CsvContentTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-capturecontenttypeheader.html#cfn-sagemaker-inferenceexperiment-capturecontenttypeheader-csvcontenttypes""", alias="CsvContentTypes")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.CaptureContentTypeHeader:
        from troposphere.sagemaker import CaptureContentTypeHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataStorageConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-datastorageconfig.html
    Properties:
        - Name: Destination
        - Name: ContentType
        - Name: KmsKey
    
    """
    
    Destination_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-datastorageconfig.html#cfn-sagemaker-inferenceexperiment-datastorageconfig-destination""", alias="Destination")
    ContentType_: Optional['CaptureContentTypeHeader'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-datastorageconfig.html#cfn-sagemaker-inferenceexperiment-datastorageconfig-contenttype""", alias="ContentType")
    KmsKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-datastorageconfig.html#cfn-sagemaker-inferenceexperiment-datastorageconfig-kmskey""", alias="KmsKey")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DataStorageConfig:
        from troposphere.sagemaker import DataStorageConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EndpointMetadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-endpointmetadata.html
    Properties:
        - Name: EndpointStatus
        - Name: EndpointName
        - Name: EndpointConfigName
    
    """
    
    EndpointStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-endpointmetadata.html#cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointstatus""", alias="EndpointStatus")
    EndpointName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-endpointmetadata.html#cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointname""", alias="EndpointName")
    EndpointConfigName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-endpointmetadata.html#cfn-sagemaker-inferenceexperiment-endpointmetadata-endpointconfigname""", alias="EndpointConfigName")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.EndpointMetadata:
        from troposphere.sagemaker import EndpointMetadata as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InferenceExperimentSchedule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-inferenceexperimentschedule.html
    Properties:
        - Name: EndTime
        - Name: StartTime
    
    """
    
    EndTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-inferenceexperimentschedule.html#cfn-sagemaker-inferenceexperiment-inferenceexperimentschedule-endtime""", alias="EndTime")
    StartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-inferenceexperimentschedule.html#cfn-sagemaker-inferenceexperiment-inferenceexperimentschedule-starttime""", alias="StartTime")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.InferenceExperimentSchedule:
        from troposphere.sagemaker import InferenceExperimentSchedule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelInfrastructureConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-modelinfrastructureconfig.html
    Properties:
        - Name: InfrastructureType
        - Name: RealTimeInferenceConfig
    
    """
    
    InfrastructureType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-modelinfrastructureconfig.html#cfn-sagemaker-inferenceexperiment-modelinfrastructureconfig-infrastructuretype""", alias="InfrastructureType")
    RealTimeInferenceConfig_: 'RealTimeInferenceConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-modelinfrastructureconfig.html#cfn-sagemaker-inferenceexperiment-modelinfrastructureconfig-realtimeinferenceconfig""", alias="RealTimeInferenceConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelInfrastructureConfig:
        from troposphere.sagemaker import ModelInfrastructureConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelVariantConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-modelvariantconfig.html
    Properties:
        - Name: ModelName
        - Name: VariantName
        - Name: InfrastructureConfig
    
    """
    
    ModelName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-modelvariantconfig.html#cfn-sagemaker-inferenceexperiment-modelvariantconfig-modelname""", alias="ModelName")
    VariantName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-modelvariantconfig.html#cfn-sagemaker-inferenceexperiment-modelvariantconfig-variantname""", alias="VariantName")
    InfrastructureConfig_: 'ModelInfrastructureConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-modelvariantconfig.html#cfn-sagemaker-inferenceexperiment-modelvariantconfig-infrastructureconfig""", alias="InfrastructureConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelVariantConfig:
        from troposphere.sagemaker import ModelVariantConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RealTimeInferenceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-realtimeinferenceconfig.html
    Properties:
        - Name: InstanceCount
        - Name: InstanceType
    
    """
    
    InstanceCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-realtimeinferenceconfig.html#cfn-sagemaker-inferenceexperiment-realtimeinferenceconfig-instancecount""", alias="InstanceCount")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-realtimeinferenceconfig.html#cfn-sagemaker-inferenceexperiment-realtimeinferenceconfig-instancetype""", alias="InstanceType")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.RealTimeInferenceConfig:
        from troposphere.sagemaker import RealTimeInferenceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ShadowModeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-shadowmodeconfig.html
    Properties:
        - Name: SourceModelVariantName
        - Name: ShadowModelVariants
    
    """
    
    SourceModelVariantName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-shadowmodeconfig.html#cfn-sagemaker-inferenceexperiment-shadowmodeconfig-sourcemodelvariantname""", alias="SourceModelVariantName")
    ShadowModelVariants_: List['ShadowModelVariantConfig'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-shadowmodeconfig.html#cfn-sagemaker-inferenceexperiment-shadowmodeconfig-shadowmodelvariants""", alias="ShadowModelVariants")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ShadowModeConfig:
        from troposphere.sagemaker import ShadowModeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ShadowModelVariantConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-shadowmodelvariantconfig.html
    Properties:
        - Name: ShadowModelVariantName
        - Name: SamplingPercentage
    
    """
    
    ShadowModelVariantName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-shadowmodelvariantconfig.html#cfn-sagemaker-inferenceexperiment-shadowmodelvariantconfig-shadowmodelvariantname""", alias="ShadowModelVariantName")
    SamplingPercentage_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-inferenceexperiment-shadowmodelvariantconfig.html#cfn-sagemaker-inferenceexperiment-shadowmodelvariantconfig-samplingpercentage""", alias="SamplingPercentage")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ShadowModelVariantConfig:
        from troposphere.sagemaker import ShadowModelVariantConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContainerDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html
    Properties:
        - Name: ImageConfig
        - Name: InferenceSpecificationName
        - Name: ContainerHostname
        - Name: ModelPackageName
        - Name: Mode
        - Name: Environment
        - Name: ModelDataUrl
        - Name: Image
        - Name: ModelDataSource
        - Name: MultiModelConfig
    
    """
    
    ImageConfig_: Optional['ImageConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-imageconfig""", alias="ImageConfig")
    InferenceSpecificationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-inferencespecificationname""", alias="InferenceSpecificationName")
    ContainerHostname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-containerhostname""", alias="ContainerHostname")
    ModelPackageName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-modelpackagename""", alias="ModelPackageName")
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-mode""", alias="Mode")
    Environment_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-environment""", alias="Environment")
    ModelDataUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-modeldataurl""", alias="ModelDataUrl")
    Image_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-image""", alias="Image")
    ModelDataSource_: Optional['ModelDataSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-modeldatasource""", alias="ModelDataSource")
    MultiModelConfig_: Optional['MultiModelConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-multimodelconfig""", alias="MultiModelConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ContainerDefinition:
        from troposphere.sagemaker import ContainerDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImageConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig.html
    Properties:
        - Name: RepositoryAuthConfig
        - Name: RepositoryAccessMode
    
    """
    
    RepositoryAuthConfig_: Optional['RepositoryAuthConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig.html#cfn-sagemaker-model-containerdefinition-imageconfig-repositoryauthconfig""", alias="RepositoryAuthConfig")
    RepositoryAccessMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig.html#cfn-sagemaker-model-containerdefinition-imageconfig-repositoryaccessmode""", alias="RepositoryAccessMode")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ImageConfig:
        from troposphere.sagemaker import ImageConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InferenceExecutionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-inferenceexecutionconfig.html
    Properties:
        - Name: Mode
    
    """
    
    Mode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-inferenceexecutionconfig.html#cfn-sagemaker-model-inferenceexecutionconfig-mode""", alias="Mode")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.InferenceExecutionConfig:
        from troposphere.sagemaker import InferenceExecutionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelDataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-modeldatasource.html
    Properties:
        - Name: S3DataSource
    
    """
    
    S3DataSource_: 'S3DataSource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-modeldatasource.html#cfn-sagemaker-model-containerdefinition-modeldatasource-s3datasource""", alias="S3DataSource")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelDataSource:
        from troposphere.sagemaker import ModelDataSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MultiModelConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-multimodelconfig.html
    Properties:
        - Name: ModelCacheSetting
    
    """
    
    ModelCacheSetting_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-multimodelconfig.html#cfn-sagemaker-model-containerdefinition-multimodelconfig-modelcachesetting""", alias="ModelCacheSetting")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MultiModelConfig:
        from troposphere.sagemaker import MultiModelConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RepositoryAuthConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig-repositoryauthconfig.html
    Properties:
        - Name: RepositoryCredentialsProviderArn
    
    """
    
    RepositoryCredentialsProviderArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig-repositoryauthconfig.html#cfn-sagemaker-model-containerdefinition-imageconfig-repositoryauthconfig-repositorycredentialsproviderarn""", alias="RepositoryCredentialsProviderArn")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.RepositoryAuthConfig:
        from troposphere.sagemaker import RepositoryAuthConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3DataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-modeldatasource-s3datasource.html
    Properties:
        - Name: S3Uri
        - Name: S3DataType
        - Name: CompressionType
    
    """
    
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-modeldatasource-s3datasource.html#cfn-sagemaker-model-containerdefinition-modeldatasource-s3datasource-s3uri""", alias="S3Uri")
    S3DataType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-modeldatasource-s3datasource.html#cfn-sagemaker-model-containerdefinition-modeldatasource-s3datasource-s3datatype""", alias="S3DataType")
    CompressionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-modeldatasource-s3datasource.html#cfn-sagemaker-model-containerdefinition-modeldatasource-s3datasource-compressiontype""", alias="CompressionType")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.S3DataSource:
        from troposphere.sagemaker import S3DataSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html
    Properties:
        - Name: Subnets
        - Name: SecurityGroupIds
    
    """
    
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html#cfn-sagemaker-model-vpcconfig-subnets""", alias="Subnets")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html#cfn-sagemaker-model-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.VpcConfig:
        from troposphere.sagemaker import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchTransformInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html
    Properties:
        - Name: DatasetFormat
        - Name: S3DataDistributionType
        - Name: StartTimeOffset
        - Name: EndTimeOffset
        - Name: ProbabilityThresholdAttribute
        - Name: InferenceAttribute
        - Name: DataCapturedDestinationS3Uri
        - Name: S3InputMode
        - Name: LocalPath
        - Name: ProbabilityAttribute
        - Name: FeaturesAttribute
    
    """
    
    DatasetFormat_: 'DatasetFormat' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html#cfn-sagemaker-modelbiasjobdefinition-batchtransforminput-datasetformat""", alias="DatasetFormat")
    S3DataDistributionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html#cfn-sagemaker-modelbiasjobdefinition-batchtransforminput-s3datadistributiontype""", alias="S3DataDistributionType")
    StartTimeOffset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html#cfn-sagemaker-modelbiasjobdefinition-batchtransforminput-starttimeoffset""", alias="StartTimeOffset")
    EndTimeOffset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html#cfn-sagemaker-modelbiasjobdefinition-batchtransforminput-endtimeoffset""", alias="EndTimeOffset")
    ProbabilityThresholdAttribute_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html#cfn-sagemaker-modelbiasjobdefinition-batchtransforminput-probabilitythresholdattribute""", alias="ProbabilityThresholdAttribute")
    InferenceAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html#cfn-sagemaker-modelbiasjobdefinition-batchtransforminput-inferenceattribute""", alias="InferenceAttribute")
    DataCapturedDestinationS3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html#cfn-sagemaker-modelbiasjobdefinition-batchtransforminput-datacaptureddestinations3uri""", alias="DataCapturedDestinationS3Uri")
    S3InputMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html#cfn-sagemaker-modelbiasjobdefinition-batchtransforminput-s3inputmode""", alias="S3InputMode")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html#cfn-sagemaker-modelbiasjobdefinition-batchtransforminput-localpath""", alias="LocalPath")
    ProbabilityAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html#cfn-sagemaker-modelbiasjobdefinition-batchtransforminput-probabilityattribute""", alias="ProbabilityAttribute")
    FeaturesAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html#cfn-sagemaker-modelbiasjobdefinition-batchtransforminput-featuresattribute""", alias="FeaturesAttribute")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.BatchTransformInput:
        from troposphere.sagemaker import BatchTransformInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClusterConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html
    Properties:
        - Name: InstanceCount
        - Name: VolumeSizeInGB
        - Name: VolumeKmsKeyId
        - Name: InstanceType
    
    """
    
    InstanceCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-instancecount""", alias="InstanceCount")
    VolumeSizeInGB_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-volumesizeingb""", alias="VolumeSizeInGB")
    VolumeKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-volumekmskeyid""", alias="VolumeKmsKeyId")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-instancetype""", alias="InstanceType")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ClusterConfig:
        from troposphere.sagemaker import ClusterConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConstraintsResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-constraintsresource.html
    Properties:
        - Name: S3Uri
    
    """
    
    S3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-constraintsresource.html#cfn-sagemaker-modelbiasjobdefinition-constraintsresource-s3uri""", alias="S3Uri")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ConstraintsResource:
        from troposphere.sagemaker import ConstraintsResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Csv(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-csv.html
    Properties:
        - Name: Header
    
    """
    
    Header_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-csv.html#cfn-sagemaker-modelbiasjobdefinition-csv-header""", alias="Header")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Csv:
        from troposphere.sagemaker import Csv as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatasetFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-datasetformat.html
    Properties:
        - Name: Parquet
        - Name: Csv
        - Name: Json
    
    """
    
    Parquet_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-datasetformat.html#cfn-sagemaker-modelbiasjobdefinition-datasetformat-parquet""", alias="Parquet")
    Csv_: Optional['Csv'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-datasetformat.html#cfn-sagemaker-modelbiasjobdefinition-datasetformat-csv""", alias="Csv")
    Json_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-datasetformat.html#cfn-sagemaker-modelbiasjobdefinition-datasetformat-json""", alias="Json")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DatasetFormat:
        from troposphere.sagemaker import DatasetFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EndpointInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html
    Properties:
        - Name: S3DataDistributionType
        - Name: StartTimeOffset
        - Name: EndTimeOffset
        - Name: ProbabilityThresholdAttribute
        - Name: EndpointName
        - Name: InferenceAttribute
        - Name: S3InputMode
        - Name: LocalPath
        - Name: ProbabilityAttribute
        - Name: FeaturesAttribute
    
    """
    
    S3DataDistributionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-s3datadistributiontype""", alias="S3DataDistributionType")
    StartTimeOffset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-starttimeoffset""", alias="StartTimeOffset")
    EndTimeOffset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-endtimeoffset""", alias="EndTimeOffset")
    ProbabilityThresholdAttribute_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-probabilitythresholdattribute""", alias="ProbabilityThresholdAttribute")
    EndpointName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-endpointname""", alias="EndpointName")
    InferenceAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-inferenceattribute""", alias="InferenceAttribute")
    S3InputMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-s3inputmode""", alias="S3InputMode")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-localpath""", alias="LocalPath")
    ProbabilityAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-probabilityattribute""", alias="ProbabilityAttribute")
    FeaturesAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-featuresattribute""", alias="FeaturesAttribute")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.EndpointInput:
        from troposphere.sagemaker import EndpointInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Json(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-json.html
    Properties:
        - Name: Line
    
    """
    
    Line_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-json.html#cfn-sagemaker-modelbiasjobdefinition-json-line""", alias="Line")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Json:
        from troposphere.sagemaker import Json as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelBiasAppSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html
    Properties:
        - Name: ConfigUri
        - Name: Environment
        - Name: ImageUri
    
    """
    
    ConfigUri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-configuri""", alias="ConfigUri")
    Environment_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-environment""", alias="Environment")
    ImageUri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-imageuri""", alias="ImageUri")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelBiasAppSpecification:
        from troposphere.sagemaker import ModelBiasAppSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelBiasBaselineConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html
    Properties:
        - Name: ConstraintsResource
        - Name: BaseliningJobName
    
    """
    
    ConstraintsResource_: Optional['ConstraintsResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig-constraintsresource""", alias="ConstraintsResource")
    BaseliningJobName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig-baseliningjobname""", alias="BaseliningJobName")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelBiasBaselineConfig:
        from troposphere.sagemaker import ModelBiasBaselineConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelBiasJobInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html
    Properties:
        - Name: GroundTruthS3Input
        - Name: BatchTransformInput
        - Name: EndpointInput
    
    """
    
    GroundTruthS3Input_: 'MonitoringGroundTruthS3Input' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-groundtruths3input""", alias="GroundTruthS3Input")
    BatchTransformInput_: Optional['BatchTransformInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-batchtransforminput""", alias="BatchTransformInput")
    EndpointInput_: Optional['EndpointInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-endpointinput""", alias="EndpointInput")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelBiasJobInput:
        from troposphere.sagemaker import ModelBiasJobInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringGroundTruthS3Input(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input.html
    Properties:
        - Name: S3Uri
    
    """
    
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input.html#cfn-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input-s3uri""", alias="S3Uri")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringGroundTruthS3Input:
        from troposphere.sagemaker import MonitoringGroundTruthS3Input as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutput.html
    Properties:
        - Name: S3Output
    
    """
    
    S3Output_: 'S3Output' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutput.html#cfn-sagemaker-modelbiasjobdefinition-monitoringoutput-s3output""", alias="S3Output")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringOutput:
        from troposphere.sagemaker import MonitoringOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringOutputConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutputconfig.html
    Properties:
        - Name: KmsKeyId
        - Name: MonitoringOutputs
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelbiasjobdefinition-monitoringoutputconfig-kmskeyid""", alias="KmsKeyId")
    MonitoringOutputs_: List['MonitoringOutput'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelbiasjobdefinition-monitoringoutputconfig-monitoringoutputs""", alias="MonitoringOutputs")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringOutputConfig:
        from troposphere.sagemaker import MonitoringOutputConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringResources(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringresources.html
    Properties:
        - Name: ClusterConfig
    
    """
    
    ClusterConfig_: 'ClusterConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringresources.html#cfn-sagemaker-modelbiasjobdefinition-monitoringresources-clusterconfig""", alias="ClusterConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringResources:
        from troposphere.sagemaker import MonitoringResources as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html
    Properties:
        - Name: EnableNetworkIsolation
        - Name: EnableInterContainerTrafficEncryption
        - Name: VpcConfig
    
    """
    
    EnableNetworkIsolation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig-enablenetworkisolation""", alias="EnableNetworkIsolation")
    EnableInterContainerTrafficEncryption_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig-enableintercontainertrafficencryption""", alias="EnableInterContainerTrafficEncryption")
    VpcConfig_: Optional['VpcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig-vpcconfig""", alias="VpcConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.NetworkConfig:
        from troposphere.sagemaker import NetworkConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Output(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html
    Properties:
        - Name: S3Uri
        - Name: LocalPath
        - Name: S3UploadMode
    
    """
    
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html#cfn-sagemaker-modelbiasjobdefinition-s3output-s3uri""", alias="S3Uri")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html#cfn-sagemaker-modelbiasjobdefinition-s3output-localpath""", alias="LocalPath")
    S3UploadMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html#cfn-sagemaker-modelbiasjobdefinition-s3output-s3uploadmode""", alias="S3UploadMode")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.S3Output:
        from troposphere.sagemaker import S3Output as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StoppingCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-stoppingcondition.html
    Properties:
        - Name: MaxRuntimeInSeconds
    
    """
    
    MaxRuntimeInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-stoppingcondition.html#cfn-sagemaker-modelbiasjobdefinition-stoppingcondition-maxruntimeinseconds""", alias="MaxRuntimeInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.StoppingCondition:
        from troposphere.sagemaker import StoppingCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html
    Properties:
        - Name: Subnets
        - Name: SecurityGroupIds
    
    """
    
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html#cfn-sagemaker-modelbiasjobdefinition-vpcconfig-subnets""", alias="Subnets")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html#cfn-sagemaker-modelbiasjobdefinition-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.VpcConfig:
        from troposphere.sagemaker import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AdditionalInformation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-additionalinformation.html
    Properties:
        - Name: EthicalConsiderations
        - Name: CaveatsAndRecommendations
        - Name: CustomDetails
    
    """
    
    EthicalConsiderations_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-additionalinformation.html#cfn-sagemaker-modelcard-additionalinformation-ethicalconsiderations""", alias="EthicalConsiderations")
    CaveatsAndRecommendations_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-additionalinformation.html#cfn-sagemaker-modelcard-additionalinformation-caveatsandrecommendations""", alias="CaveatsAndRecommendations")
    CustomDetails_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-additionalinformation.html#cfn-sagemaker-modelcard-additionalinformation-customdetails""", alias="CustomDetails")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.AdditionalInformation:
        from troposphere.sagemaker import AdditionalInformation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BusinessDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-businessdetails.html
    Properties:
        - Name: BusinessStakeholders
        - Name: LineOfBusiness
        - Name: BusinessProblem
    
    """
    
    BusinessStakeholders_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-businessdetails.html#cfn-sagemaker-modelcard-businessdetails-businessstakeholders""", alias="BusinessStakeholders")
    LineOfBusiness_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-businessdetails.html#cfn-sagemaker-modelcard-businessdetails-lineofbusiness""", alias="LineOfBusiness")
    BusinessProblem_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-businessdetails.html#cfn-sagemaker-modelcard-businessdetails-businessproblem""", alias="BusinessProblem")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.BusinessDetails:
        from troposphere.sagemaker import BusinessDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Container(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-container.html
    Properties:
        - Name: NearestModelName
        - Name: ModelDataUrl
        - Name: Image
    
    """
    
    NearestModelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-container.html#cfn-sagemaker-modelcard-container-nearestmodelname""", alias="NearestModelName")
    ModelDataUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-container.html#cfn-sagemaker-modelcard-container-modeldataurl""", alias="ModelDataUrl")
    Image_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-container.html#cfn-sagemaker-modelcard-container-image""", alias="Image")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Container:
        from troposphere.sagemaker import Container as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Content(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-content.html
    Properties:
        - Name: IntendedUses
        - Name: AdditionalInformation
        - Name: ModelOverview
        - Name: TrainingDetails
        - Name: EvaluationDetails
        - Name: ModelPackageDetails
        - Name: BusinessDetails
    
    """
    
    IntendedUses_: Optional['IntendedUses'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-content.html#cfn-sagemaker-modelcard-content-intendeduses""", alias="IntendedUses")
    AdditionalInformation_: Optional['AdditionalInformation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-content.html#cfn-sagemaker-modelcard-content-additionalinformation""", alias="AdditionalInformation")
    ModelOverview_: Optional['ModelOverview'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-content.html#cfn-sagemaker-modelcard-content-modeloverview""", alias="ModelOverview")
    TrainingDetails_: Optional['TrainingDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-content.html#cfn-sagemaker-modelcard-content-trainingdetails""", alias="TrainingDetails")
    EvaluationDetails_: Optional[List['EvaluationDetail']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-content.html#cfn-sagemaker-modelcard-content-evaluationdetails""", alias="EvaluationDetails")
    ModelPackageDetails_: Optional['ModelPackageDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-content.html#cfn-sagemaker-modelcard-content-modelpackagedetails""", alias="ModelPackageDetails")
    BusinessDetails_: Optional['BusinessDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-content.html#cfn-sagemaker-modelcard-content-businessdetails""", alias="BusinessDetails")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Content:
        from troposphere.sagemaker import Content as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluationDetail(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-evaluationdetail.html
    Properties:
        - Name: Datasets
        - Name: EvaluationObservation
        - Name: MetricGroups
        - Name: Metadata
        - Name: EvaluationJobArn
        - Name: Name
    
    """
    
    Datasets_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-evaluationdetail.html#cfn-sagemaker-modelcard-evaluationdetail-datasets""", alias="Datasets")
    EvaluationObservation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-evaluationdetail.html#cfn-sagemaker-modelcard-evaluationdetail-evaluationobservation""", alias="EvaluationObservation")
    MetricGroups_: Optional[List['MetricGroup']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-evaluationdetail.html#cfn-sagemaker-modelcard-evaluationdetail-metricgroups""", alias="MetricGroups")
    Metadata_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-evaluationdetail.html#cfn-sagemaker-modelcard-evaluationdetail-metadata""", alias="Metadata")
    EvaluationJobArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-evaluationdetail.html#cfn-sagemaker-modelcard-evaluationdetail-evaluationjobarn""", alias="EvaluationJobArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-evaluationdetail.html#cfn-sagemaker-modelcard-evaluationdetail-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.EvaluationDetail:
        from troposphere.sagemaker import EvaluationDetail as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Function(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-function.html
    Properties:
        - Name: Condition
        - Name: Function
        - Name: Facet
    
    """
    
    Condition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-function.html#cfn-sagemaker-modelcard-function-condition""", alias="Condition")
    Function_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-function.html#cfn-sagemaker-modelcard-function-function""", alias="Function")
    Facet_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-function.html#cfn-sagemaker-modelcard-function-facet""", alias="Facet")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Function:
        from troposphere.sagemaker import Function as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InferenceEnvironment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-inferenceenvironment.html
    Properties:
        - Name: ContainerImage
    
    """
    
    ContainerImage_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-inferenceenvironment.html#cfn-sagemaker-modelcard-inferenceenvironment-containerimage""", alias="ContainerImage")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.InferenceEnvironment:
        from troposphere.sagemaker import InferenceEnvironment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InferenceSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-inferencespecification.html
    Properties:
        - Name: Containers
    
    """
    
    Containers_: List['Container'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-inferencespecification.html#cfn-sagemaker-modelcard-inferencespecification-containers""", alias="Containers")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.InferenceSpecification:
        from troposphere.sagemaker import InferenceSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IntendedUses(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-intendeduses.html
    Properties:
        - Name: IntendedUses
        - Name: FactorsAffectingModelEfficiency
        - Name: PurposeOfModel
        - Name: RiskRating
        - Name: ExplanationsForRiskRating
    
    """
    
    IntendedUses_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-intendeduses.html#cfn-sagemaker-modelcard-intendeduses-intendeduses""", alias="IntendedUses")
    FactorsAffectingModelEfficiency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-intendeduses.html#cfn-sagemaker-modelcard-intendeduses-factorsaffectingmodelefficiency""", alias="FactorsAffectingModelEfficiency")
    PurposeOfModel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-intendeduses.html#cfn-sagemaker-modelcard-intendeduses-purposeofmodel""", alias="PurposeOfModel")
    RiskRating_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-intendeduses.html#cfn-sagemaker-modelcard-intendeduses-riskrating""", alias="RiskRating")
    ExplanationsForRiskRating_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-intendeduses.html#cfn-sagemaker-modelcard-intendeduses-explanationsforriskrating""", alias="ExplanationsForRiskRating")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.IntendedUses:
        from troposphere.sagemaker import IntendedUses as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricDataItems(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-metricdataitems.html
    Properties:
        - Name: XAxisName
        - Name: Type
        - Name: Value
        - Name: YAxisName
        - Name: Notes
        - Name: Name
    
    """
    
    XAxisName_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-metricdataitems.html#cfn-sagemaker-modelcard-metricdataitems-xaxisname""", alias="XAxisName")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-metricdataitems.html#cfn-sagemaker-modelcard-metricdataitems-type""", alias="Type")
    Value_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-metricdataitems.html#cfn-sagemaker-modelcard-metricdataitems-value""", alias="Value")
    YAxisName_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-metricdataitems.html#cfn-sagemaker-modelcard-metricdataitems-yaxisname""", alias="YAxisName")
    Notes_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-metricdataitems.html#cfn-sagemaker-modelcard-metricdataitems-notes""", alias="Notes")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-metricdataitems.html#cfn-sagemaker-modelcard-metricdataitems-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MetricDataItems:
        from troposphere.sagemaker import MetricDataItems as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-metricgroup.html
    Properties:
        - Name: Name
        - Name: MetricData
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-metricgroup.html#cfn-sagemaker-modelcard-metricgroup-name""", alias="Name")
    MetricData_: List['MetricDataItems'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-metricgroup.html#cfn-sagemaker-modelcard-metricgroup-metricdata""", alias="MetricData")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MetricGroup:
        from troposphere.sagemaker import MetricGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelOverview(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modeloverview.html
    Properties:
        - Name: ModelOwner
        - Name: ModelArtifact
        - Name: AlgorithmType
        - Name: ModelName
        - Name: InferenceEnvironment
        - Name: ProblemType
        - Name: ModelDescription
        - Name: ModelVersion
        - Name: ModelCreator
        - Name: ModelId
    
    """
    
    ModelOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modeloverview.html#cfn-sagemaker-modelcard-modeloverview-modelowner""", alias="ModelOwner")
    ModelArtifact_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modeloverview.html#cfn-sagemaker-modelcard-modeloverview-modelartifact""", alias="ModelArtifact")
    AlgorithmType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modeloverview.html#cfn-sagemaker-modelcard-modeloverview-algorithmtype""", alias="AlgorithmType")
    ModelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modeloverview.html#cfn-sagemaker-modelcard-modeloverview-modelname""", alias="ModelName")
    InferenceEnvironment_: Optional['InferenceEnvironment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modeloverview.html#cfn-sagemaker-modelcard-modeloverview-inferenceenvironment""", alias="InferenceEnvironment")
    ProblemType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modeloverview.html#cfn-sagemaker-modelcard-modeloverview-problemtype""", alias="ProblemType")
    ModelDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modeloverview.html#cfn-sagemaker-modelcard-modeloverview-modeldescription""", alias="ModelDescription")
    ModelVersion_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modeloverview.html#cfn-sagemaker-modelcard-modeloverview-modelversion""", alias="ModelVersion")
    ModelCreator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modeloverview.html#cfn-sagemaker-modelcard-modeloverview-modelcreator""", alias="ModelCreator")
    ModelId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modeloverview.html#cfn-sagemaker-modelcard-modeloverview-modelid""", alias="ModelId")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelOverview:
        from troposphere.sagemaker import ModelOverview as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelPackageCreator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagecreator.html
    Properties:
        - Name: UserProfileName
    
    """
    
    UserProfileName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagecreator.html#cfn-sagemaker-modelcard-modelpackagecreator-userprofilename""", alias="UserProfileName")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelPackageCreator:
        from troposphere.sagemaker import ModelPackageCreator as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelPackageDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html
    Properties:
        - Name: ModelPackageGroupName
        - Name: Task
        - Name: CreatedBy
        - Name: ApprovalDescription
        - Name: ModelApprovalStatus
        - Name: ModelPackageVersion
        - Name: ModelPackageDescription
        - Name: ModelPackageName
        - Name: ModelPackageStatus
        - Name: SourceAlgorithms
        - Name: InferenceSpecification
        - Name: ModelPackageArn
        - Name: Domain
    
    """
    
    ModelPackageGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagegroupname""", alias="ModelPackageGroupName")
    Task_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html#cfn-sagemaker-modelcard-modelpackagedetails-task""", alias="Task")
    CreatedBy_: Optional['ModelPackageCreator'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html#cfn-sagemaker-modelcard-modelpackagedetails-createdby""", alias="CreatedBy")
    ApprovalDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html#cfn-sagemaker-modelcard-modelpackagedetails-approvaldescription""", alias="ApprovalDescription")
    ModelApprovalStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html#cfn-sagemaker-modelcard-modelpackagedetails-modelapprovalstatus""", alias="ModelApprovalStatus")
    ModelPackageVersion_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html#cfn-sagemaker-modelcard-modelpackagedetails-modelpackageversion""", alias="ModelPackageVersion")
    ModelPackageDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagedescription""", alias="ModelPackageDescription")
    ModelPackageName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagename""", alias="ModelPackageName")
    ModelPackageStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagestatus""", alias="ModelPackageStatus")
    SourceAlgorithms_: Optional[List['SourceAlgorithm']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html#cfn-sagemaker-modelcard-modelpackagedetails-sourcealgorithms""", alias="SourceAlgorithms")
    InferenceSpecification_: Optional['InferenceSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html#cfn-sagemaker-modelcard-modelpackagedetails-inferencespecification""", alias="InferenceSpecification")
    ModelPackageArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html#cfn-sagemaker-modelcard-modelpackagedetails-modelpackagearn""", alias="ModelPackageArn")
    Domain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-modelpackagedetails.html#cfn-sagemaker-modelcard-modelpackagedetails-domain""", alias="Domain")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelPackageDetails:
        from troposphere.sagemaker import ModelPackageDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ObjectiveFunction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-objectivefunction.html
    Properties:
        - Name: Function
        - Name: Notes
    
    """
    
    Function_: Optional['Function'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-objectivefunction.html#cfn-sagemaker-modelcard-objectivefunction-function""", alias="Function")
    Notes_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-objectivefunction.html#cfn-sagemaker-modelcard-objectivefunction-notes""", alias="Notes")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ObjectiveFunction:
        from troposphere.sagemaker import ObjectiveFunction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SecurityConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-securityconfig.html
    Properties:
        - Name: KmsKeyId
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-securityconfig.html#cfn-sagemaker-modelcard-securityconfig-kmskeyid""", alias="KmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.SecurityConfig:
        from troposphere.sagemaker import SecurityConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceAlgorithm(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-sourcealgorithm.html
    Properties:
        - Name: ModelDataUrl
        - Name: AlgorithmName
    
    """
    
    ModelDataUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-sourcealgorithm.html#cfn-sagemaker-modelcard-sourcealgorithm-modeldataurl""", alias="ModelDataUrl")
    AlgorithmName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-sourcealgorithm.html#cfn-sagemaker-modelcard-sourcealgorithm-algorithmname""", alias="AlgorithmName")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.SourceAlgorithm:
        from troposphere.sagemaker import SourceAlgorithm as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrainingDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingdetails.html
    Properties:
        - Name: ObjectiveFunction
        - Name: TrainingObservations
        - Name: TrainingJobDetails
    
    """
    
    ObjectiveFunction_: Optional['ObjectiveFunction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingdetails.html#cfn-sagemaker-modelcard-trainingdetails-objectivefunction""", alias="ObjectiveFunction")
    TrainingObservations_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingdetails.html#cfn-sagemaker-modelcard-trainingdetails-trainingobservations""", alias="TrainingObservations")
    TrainingJobDetails_: Optional['TrainingJobDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingdetails.html#cfn-sagemaker-modelcard-trainingdetails-trainingjobdetails""", alias="TrainingJobDetails")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.TrainingDetails:
        from troposphere.sagemaker import TrainingDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrainingEnvironment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingenvironment.html
    Properties:
        - Name: ContainerImage
    
    """
    
    ContainerImage_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingenvironment.html#cfn-sagemaker-modelcard-trainingenvironment-containerimage""", alias="ContainerImage")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.TrainingEnvironment:
        from troposphere.sagemaker import TrainingEnvironment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrainingHyperParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-traininghyperparameter.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-traininghyperparameter.html#cfn-sagemaker-modelcard-traininghyperparameter-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-traininghyperparameter.html#cfn-sagemaker-modelcard-traininghyperparameter-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.TrainingHyperParameter:
        from troposphere.sagemaker import TrainingHyperParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrainingJobDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingjobdetails.html
    Properties:
        - Name: TrainingMetrics
        - Name: HyperParameters
        - Name: TrainingArn
        - Name: UserProvidedTrainingMetrics
        - Name: TrainingEnvironment
        - Name: TrainingDatasets
        - Name: UserProvidedHyperParameters
    
    """
    
    TrainingMetrics_: Optional[List['TrainingMetric']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingjobdetails.html#cfn-sagemaker-modelcard-trainingjobdetails-trainingmetrics""", alias="TrainingMetrics")
    HyperParameters_: Optional[List['TrainingHyperParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingjobdetails.html#cfn-sagemaker-modelcard-trainingjobdetails-hyperparameters""", alias="HyperParameters")
    TrainingArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingjobdetails.html#cfn-sagemaker-modelcard-trainingjobdetails-trainingarn""", alias="TrainingArn")
    UserProvidedTrainingMetrics_: Optional[List['TrainingMetric']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingjobdetails.html#cfn-sagemaker-modelcard-trainingjobdetails-userprovidedtrainingmetrics""", alias="UserProvidedTrainingMetrics")
    TrainingEnvironment_: Optional['TrainingEnvironment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingjobdetails.html#cfn-sagemaker-modelcard-trainingjobdetails-trainingenvironment""", alias="TrainingEnvironment")
    TrainingDatasets_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingjobdetails.html#cfn-sagemaker-modelcard-trainingjobdetails-trainingdatasets""", alias="TrainingDatasets")
    UserProvidedHyperParameters_: Optional[List['TrainingHyperParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingjobdetails.html#cfn-sagemaker-modelcard-trainingjobdetails-userprovidedhyperparameters""", alias="UserProvidedHyperParameters")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.TrainingJobDetails:
        from troposphere.sagemaker import TrainingJobDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrainingMetric(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingmetric.html
    Properties:
        - Name: Value
        - Name: Notes
        - Name: Name
    
    """
    
    Value_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingmetric.html#cfn-sagemaker-modelcard-trainingmetric-value""", alias="Value")
    Notes_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingmetric.html#cfn-sagemaker-modelcard-trainingmetric-notes""", alias="Notes")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-trainingmetric.html#cfn-sagemaker-modelcard-trainingmetric-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.TrainingMetric:
        from troposphere.sagemaker import TrainingMetric as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserContext(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-usercontext.html
    Properties:
        - Name: DomainId
        - Name: UserProfileArn
        - Name: UserProfileName
    
    """
    
    DomainId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-usercontext.html#cfn-sagemaker-modelcard-usercontext-domainid""", alias="DomainId")
    UserProfileArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-usercontext.html#cfn-sagemaker-modelcard-usercontext-userprofilearn""", alias="UserProfileArn")
    UserProfileName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelcard-usercontext.html#cfn-sagemaker-modelcard-usercontext-userprofilename""", alias="UserProfileName")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.UserContext:
        from troposphere.sagemaker import UserContext as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchTransformInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-batchtransforminput.html
    Properties:
        - Name: DatasetFormat
        - Name: S3DataDistributionType
        - Name: InferenceAttribute
        - Name: DataCapturedDestinationS3Uri
        - Name: S3InputMode
        - Name: LocalPath
        - Name: ProbabilityAttribute
        - Name: FeaturesAttribute
    
    """
    
    DatasetFormat_: 'DatasetFormat' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelexplainabilityjobdefinition-batchtransforminput-datasetformat""", alias="DatasetFormat")
    S3DataDistributionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelexplainabilityjobdefinition-batchtransforminput-s3datadistributiontype""", alias="S3DataDistributionType")
    InferenceAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelexplainabilityjobdefinition-batchtransforminput-inferenceattribute""", alias="InferenceAttribute")
    DataCapturedDestinationS3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelexplainabilityjobdefinition-batchtransforminput-datacaptureddestinations3uri""", alias="DataCapturedDestinationS3Uri")
    S3InputMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelexplainabilityjobdefinition-batchtransforminput-s3inputmode""", alias="S3InputMode")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelexplainabilityjobdefinition-batchtransforminput-localpath""", alias="LocalPath")
    ProbabilityAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelexplainabilityjobdefinition-batchtransforminput-probabilityattribute""", alias="ProbabilityAttribute")
    FeaturesAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelexplainabilityjobdefinition-batchtransforminput-featuresattribute""", alias="FeaturesAttribute")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.BatchTransformInput:
        from troposphere.sagemaker import BatchTransformInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClusterConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html
    Properties:
        - Name: InstanceCount
        - Name: VolumeSizeInGB
        - Name: VolumeKmsKeyId
        - Name: InstanceType
    
    """
    
    InstanceCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-instancecount""", alias="InstanceCount")
    VolumeSizeInGB_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-volumesizeingb""", alias="VolumeSizeInGB")
    VolumeKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-volumekmskeyid""", alias="VolumeKmsKeyId")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-instancetype""", alias="InstanceType")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ClusterConfig:
        from troposphere.sagemaker import ClusterConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConstraintsResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-constraintsresource.html
    Properties:
        - Name: S3Uri
    
    """
    
    S3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-constraintsresource.html#cfn-sagemaker-modelexplainabilityjobdefinition-constraintsresource-s3uri""", alias="S3Uri")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ConstraintsResource:
        from troposphere.sagemaker import ConstraintsResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Csv(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-csv.html
    Properties:
        - Name: Header
    
    """
    
    Header_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-csv.html#cfn-sagemaker-modelexplainabilityjobdefinition-csv-header""", alias="Header")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Csv:
        from troposphere.sagemaker import Csv as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatasetFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-datasetformat.html
    Properties:
        - Name: Parquet
        - Name: Csv
        - Name: Json
    
    """
    
    Parquet_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-datasetformat.html#cfn-sagemaker-modelexplainabilityjobdefinition-datasetformat-parquet""", alias="Parquet")
    Csv_: Optional['Csv'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-datasetformat.html#cfn-sagemaker-modelexplainabilityjobdefinition-datasetformat-csv""", alias="Csv")
    Json_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-datasetformat.html#cfn-sagemaker-modelexplainabilityjobdefinition-datasetformat-json""", alias="Json")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DatasetFormat:
        from troposphere.sagemaker import DatasetFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EndpointInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html
    Properties:
        - Name: S3DataDistributionType
        - Name: EndpointName
        - Name: InferenceAttribute
        - Name: S3InputMode
        - Name: LocalPath
        - Name: ProbabilityAttribute
        - Name: FeaturesAttribute
    
    """
    
    S3DataDistributionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-s3datadistributiontype""", alias="S3DataDistributionType")
    EndpointName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-endpointname""", alias="EndpointName")
    InferenceAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-inferenceattribute""", alias="InferenceAttribute")
    S3InputMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-s3inputmode""", alias="S3InputMode")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-localpath""", alias="LocalPath")
    ProbabilityAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-probabilityattribute""", alias="ProbabilityAttribute")
    FeaturesAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-featuresattribute""", alias="FeaturesAttribute")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.EndpointInput:
        from troposphere.sagemaker import EndpointInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Json(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-json.html
    Properties:
        - Name: Line
    
    """
    
    Line_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-json.html#cfn-sagemaker-modelexplainabilityjobdefinition-json-line""", alias="Line")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Json:
        from troposphere.sagemaker import Json as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelExplainabilityAppSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html
    Properties:
        - Name: ConfigUri
        - Name: Environment
        - Name: ImageUri
    
    """
    
    ConfigUri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-configuri""", alias="ConfigUri")
    Environment_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-environment""", alias="Environment")
    ImageUri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-imageuri""", alias="ImageUri")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelExplainabilityAppSpecification:
        from troposphere.sagemaker import ModelExplainabilityAppSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelExplainabilityBaselineConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html
    Properties:
        - Name: ConstraintsResource
        - Name: BaseliningJobName
    
    """
    
    ConstraintsResource_: Optional['ConstraintsResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig-constraintsresource""", alias="ConstraintsResource")
    BaseliningJobName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig-baseliningjobname""", alias="BaseliningJobName")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelExplainabilityBaselineConfig:
        from troposphere.sagemaker import ModelExplainabilityBaselineConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelExplainabilityJobInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput.html
    Properties:
        - Name: BatchTransformInput
        - Name: EndpointInput
    
    """
    
    BatchTransformInput_: Optional['BatchTransformInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-batchtransforminput""", alias="BatchTransformInput")
    EndpointInput_: Optional['EndpointInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-endpointinput""", alias="EndpointInput")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelExplainabilityJobInput:
        from troposphere.sagemaker import ModelExplainabilityJobInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutput.html
    Properties:
        - Name: S3Output
    
    """
    
    S3Output_: 'S3Output' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutput.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringoutput-s3output""", alias="S3Output")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringOutput:
        from troposphere.sagemaker import MonitoringOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringOutputConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig.html
    Properties:
        - Name: KmsKeyId
        - Name: MonitoringOutputs
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig-kmskeyid""", alias="KmsKeyId")
    MonitoringOutputs_: List['MonitoringOutput'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig-monitoringoutputs""", alias="MonitoringOutputs")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringOutputConfig:
        from troposphere.sagemaker import MonitoringOutputConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringResources(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources.html
    Properties:
        - Name: ClusterConfig
    
    """
    
    ClusterConfig_: 'ClusterConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringresources-clusterconfig""", alias="ClusterConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringResources:
        from troposphere.sagemaker import MonitoringResources as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html
    Properties:
        - Name: EnableNetworkIsolation
        - Name: EnableInterContainerTrafficEncryption
        - Name: VpcConfig
    
    """
    
    EnableNetworkIsolation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig-enablenetworkisolation""", alias="EnableNetworkIsolation")
    EnableInterContainerTrafficEncryption_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig-enableintercontainertrafficencryption""", alias="EnableInterContainerTrafficEncryption")
    VpcConfig_: Optional['VpcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig-vpcconfig""", alias="VpcConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.NetworkConfig:
        from troposphere.sagemaker import NetworkConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Output(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html
    Properties:
        - Name: S3Uri
        - Name: LocalPath
        - Name: S3UploadMode
    
    """
    
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html#cfn-sagemaker-modelexplainabilityjobdefinition-s3output-s3uri""", alias="S3Uri")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html#cfn-sagemaker-modelexplainabilityjobdefinition-s3output-localpath""", alias="LocalPath")
    S3UploadMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html#cfn-sagemaker-modelexplainabilityjobdefinition-s3output-s3uploadmode""", alias="S3UploadMode")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.S3Output:
        from troposphere.sagemaker import S3Output as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StoppingCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition.html
    Properties:
        - Name: MaxRuntimeInSeconds
    
    """
    
    MaxRuntimeInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition-maxruntimeinseconds""", alias="MaxRuntimeInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.StoppingCondition:
        from troposphere.sagemaker import StoppingCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-vpcconfig.html
    Properties:
        - Name: Subnets
        - Name: SecurityGroupIds
    
    """
    
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-vpcconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-vpcconfig-subnets""", alias="Subnets")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-vpcconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.VpcConfig:
        from troposphere.sagemaker import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AdditionalInferenceSpecificationDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.html
    Properties:
        - Name: Description
        - Name: SupportedContentTypes
        - Name: SupportedRealtimeInferenceInstanceTypes
        - Name: Containers
        - Name: SupportedTransformInstanceTypes
        - Name: Name
        - Name: SupportedResponseMIMETypes
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.html#cfn-sagemaker-modelpackage-additionalinferencespecificationdefinition-description""", alias="Description")
    SupportedContentTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.html#cfn-sagemaker-modelpackage-additionalinferencespecificationdefinition-supportedcontenttypes""", alias="SupportedContentTypes")
    SupportedRealtimeInferenceInstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.html#cfn-sagemaker-modelpackage-additionalinferencespecificationdefinition-supportedrealtimeinferenceinstancetypes""", alias="SupportedRealtimeInferenceInstanceTypes")
    Containers_: List['ModelPackageContainerDefinition'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.html#cfn-sagemaker-modelpackage-additionalinferencespecificationdefinition-containers""", alias="Containers")
    SupportedTransformInstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.html#cfn-sagemaker-modelpackage-additionalinferencespecificationdefinition-supportedtransforminstancetypes""", alias="SupportedTransformInstanceTypes")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.html#cfn-sagemaker-modelpackage-additionalinferencespecificationdefinition-name""", alias="Name")
    SupportedResponseMIMETypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.html#cfn-sagemaker-modelpackage-additionalinferencespecificationdefinition-supportedresponsemimetypes""", alias="SupportedResponseMIMETypes")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.AdditionalInferenceSpecificationDefinition:
        from troposphere.sagemaker import AdditionalInferenceSpecificationDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Bias(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-bias.html
    Properties:
        - Name: Report
        - Name: PreTrainingReport
        - Name: PostTrainingReport
    
    """
    
    Report_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-bias.html#cfn-sagemaker-modelpackage-bias-report""", alias="Report")
    PreTrainingReport_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-bias.html#cfn-sagemaker-modelpackage-bias-pretrainingreport""", alias="PreTrainingReport")
    PostTrainingReport_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-bias.html#cfn-sagemaker-modelpackage-bias-posttrainingreport""", alias="PostTrainingReport")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Bias:
        from troposphere.sagemaker import Bias as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-datasource.html
    Properties:
        - Name: S3DataSource
    
    """
    
    S3DataSource_: 'S3DataSource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-datasource.html#cfn-sagemaker-modelpackage-datasource-s3datasource""", alias="S3DataSource")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DataSource:
        from troposphere.sagemaker import DataSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DriftCheckBaselines(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbaselines.html
    Properties:
        - Name: ModelDataQuality
        - Name: Bias
        - Name: ModelQuality
        - Name: Explainability
    
    """
    
    ModelDataQuality_: Optional['DriftCheckModelDataQuality'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbaselines.html#cfn-sagemaker-modelpackage-driftcheckbaselines-modeldataquality""", alias="ModelDataQuality")
    Bias_: Optional['DriftCheckBias'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbaselines.html#cfn-sagemaker-modelpackage-driftcheckbaselines-bias""", alias="Bias")
    ModelQuality_: Optional['DriftCheckModelQuality'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbaselines.html#cfn-sagemaker-modelpackage-driftcheckbaselines-modelquality""", alias="ModelQuality")
    Explainability_: Optional['DriftCheckExplainability'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbaselines.html#cfn-sagemaker-modelpackage-driftcheckbaselines-explainability""", alias="Explainability")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DriftCheckBaselines:
        from troposphere.sagemaker import DriftCheckBaselines as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DriftCheckBias(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbias.html
    Properties:
        - Name: PreTrainingConstraints
        - Name: ConfigFile
        - Name: PostTrainingConstraints
    
    """
    
    PreTrainingConstraints_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbias.html#cfn-sagemaker-modelpackage-driftcheckbias-pretrainingconstraints""", alias="PreTrainingConstraints")
    ConfigFile_: Optional['FileSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbias.html#cfn-sagemaker-modelpackage-driftcheckbias-configfile""", alias="ConfigFile")
    PostTrainingConstraints_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbias.html#cfn-sagemaker-modelpackage-driftcheckbias-posttrainingconstraints""", alias="PostTrainingConstraints")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DriftCheckBias:
        from troposphere.sagemaker import DriftCheckBias as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DriftCheckExplainability(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckexplainability.html
    Properties:
        - Name: Constraints
        - Name: ConfigFile
    
    """
    
    Constraints_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckexplainability.html#cfn-sagemaker-modelpackage-driftcheckexplainability-constraints""", alias="Constraints")
    ConfigFile_: Optional['FileSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckexplainability.html#cfn-sagemaker-modelpackage-driftcheckexplainability-configfile""", alias="ConfigFile")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DriftCheckExplainability:
        from troposphere.sagemaker import DriftCheckExplainability as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DriftCheckModelDataQuality(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodeldataquality.html
    Properties:
        - Name: Constraints
        - Name: Statistics
    
    """
    
    Constraints_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodeldataquality.html#cfn-sagemaker-modelpackage-driftcheckmodeldataquality-constraints""", alias="Constraints")
    Statistics_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodeldataquality.html#cfn-sagemaker-modelpackage-driftcheckmodeldataquality-statistics""", alias="Statistics")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DriftCheckModelDataQuality:
        from troposphere.sagemaker import DriftCheckModelDataQuality as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DriftCheckModelQuality(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodelquality.html
    Properties:
        - Name: Constraints
        - Name: Statistics
    
    """
    
    Constraints_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodelquality.html#cfn-sagemaker-modelpackage-driftcheckmodelquality-constraints""", alias="Constraints")
    Statistics_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodelquality.html#cfn-sagemaker-modelpackage-driftcheckmodelquality-statistics""", alias="Statistics")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DriftCheckModelQuality:
        from troposphere.sagemaker import DriftCheckModelQuality as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Explainability(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-explainability.html
    Properties:
        - Name: Report
    
    """
    
    Report_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-explainability.html#cfn-sagemaker-modelpackage-explainability-report""", alias="Report")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Explainability:
        from troposphere.sagemaker import Explainability as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FileSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-filesource.html
    Properties:
        - Name: ContentType
        - Name: S3Uri
        - Name: ContentDigest
    
    """
    
    ContentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-filesource.html#cfn-sagemaker-modelpackage-filesource-contenttype""", alias="ContentType")
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-filesource.html#cfn-sagemaker-modelpackage-filesource-s3uri""", alias="S3Uri")
    ContentDigest_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-filesource.html#cfn-sagemaker-modelpackage-filesource-contentdigest""", alias="ContentDigest")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.FileSource:
        from troposphere.sagemaker import FileSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InferenceSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-inferencespecification.html
    Properties:
        - Name: SupportedContentTypes
        - Name: SupportedRealtimeInferenceInstanceTypes
        - Name: Containers
        - Name: SupportedTransformInstanceTypes
        - Name: SupportedResponseMIMETypes
    
    """
    
    SupportedContentTypes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-inferencespecification.html#cfn-sagemaker-modelpackage-inferencespecification-supportedcontenttypes""", alias="SupportedContentTypes")
    SupportedRealtimeInferenceInstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-inferencespecification.html#cfn-sagemaker-modelpackage-inferencespecification-supportedrealtimeinferenceinstancetypes""", alias="SupportedRealtimeInferenceInstanceTypes")
    Containers_: List['ModelPackageContainerDefinition'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-inferencespecification.html#cfn-sagemaker-modelpackage-inferencespecification-containers""", alias="Containers")
    SupportedTransformInstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-inferencespecification.html#cfn-sagemaker-modelpackage-inferencespecification-supportedtransforminstancetypes""", alias="SupportedTransformInstanceTypes")
    SupportedResponseMIMETypes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-inferencespecification.html#cfn-sagemaker-modelpackage-inferencespecification-supportedresponsemimetypes""", alias="SupportedResponseMIMETypes")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.InferenceSpecification:
        from troposphere.sagemaker import InferenceSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetadataProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metadataproperties.html
    Properties:
        - Name: GeneratedBy
        - Name: Repository
        - Name: CommitId
        - Name: ProjectId
    
    """
    
    GeneratedBy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metadataproperties.html#cfn-sagemaker-modelpackage-metadataproperties-generatedby""", alias="GeneratedBy")
    Repository_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metadataproperties.html#cfn-sagemaker-modelpackage-metadataproperties-repository""", alias="Repository")
    CommitId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metadataproperties.html#cfn-sagemaker-modelpackage-metadataproperties-commitid""", alias="CommitId")
    ProjectId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metadataproperties.html#cfn-sagemaker-modelpackage-metadataproperties-projectid""", alias="ProjectId")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MetadataProperties:
        from troposphere.sagemaker import MetadataProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricsSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metricssource.html
    Properties:
        - Name: ContentType
        - Name: S3Uri
        - Name: ContentDigest
    
    """
    
    ContentType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metricssource.html#cfn-sagemaker-modelpackage-metricssource-contenttype""", alias="ContentType")
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metricssource.html#cfn-sagemaker-modelpackage-metricssource-s3uri""", alias="S3Uri")
    ContentDigest_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metricssource.html#cfn-sagemaker-modelpackage-metricssource-contentdigest""", alias="ContentDigest")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MetricsSource:
        from troposphere.sagemaker import MetricsSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelDataQuality(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modeldataquality.html
    Properties:
        - Name: Constraints
        - Name: Statistics
    
    """
    
    Constraints_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modeldataquality.html#cfn-sagemaker-modelpackage-modeldataquality-constraints""", alias="Constraints")
    Statistics_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modeldataquality.html#cfn-sagemaker-modelpackage-modeldataquality-statistics""", alias="Statistics")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelDataQuality:
        from troposphere.sagemaker import ModelDataQuality as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelinput.html
    Properties:
        - Name: DataInputConfig
    
    """
    
    DataInputConfig_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelinput.html#cfn-sagemaker-modelpackage-modelinput-datainputconfig""", alias="DataInputConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelInput:
        from troposphere.sagemaker import ModelInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelMetrics(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelmetrics.html
    Properties:
        - Name: ModelDataQuality
        - Name: Bias
        - Name: ModelQuality
        - Name: Explainability
    
    """
    
    ModelDataQuality_: Optional['ModelDataQuality'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelmetrics.html#cfn-sagemaker-modelpackage-modelmetrics-modeldataquality""", alias="ModelDataQuality")
    Bias_: Optional['Bias'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelmetrics.html#cfn-sagemaker-modelpackage-modelmetrics-bias""", alias="Bias")
    ModelQuality_: Optional['ModelQuality'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelmetrics.html#cfn-sagemaker-modelpackage-modelmetrics-modelquality""", alias="ModelQuality")
    Explainability_: Optional['Explainability'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelmetrics.html#cfn-sagemaker-modelpackage-modelmetrics-explainability""", alias="Explainability")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelMetrics:
        from troposphere.sagemaker import ModelMetrics as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelPackageContainerDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html
    Properties:
        - Name: ModelInput
        - Name: NearestModelName
        - Name: ContainerHostname
        - Name: ImageDigest
        - Name: FrameworkVersion
        - Name: Environment
        - Name: ModelDataUrl
        - Name: Image
        - Name: Framework
    
    """
    
    ModelInput_: Optional['ModelInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-modelinput""", alias="ModelInput")
    NearestModelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-nearestmodelname""", alias="NearestModelName")
    ContainerHostname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-containerhostname""", alias="ContainerHostname")
    ImageDigest_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-imagedigest""", alias="ImageDigest")
    FrameworkVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-frameworkversion""", alias="FrameworkVersion")
    Environment_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-environment""", alias="Environment")
    ModelDataUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-modeldataurl""", alias="ModelDataUrl")
    Image_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-image""", alias="Image")
    Framework_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html#cfn-sagemaker-modelpackage-modelpackagecontainerdefinition-framework""", alias="Framework")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelPackageContainerDefinition:
        from troposphere.sagemaker import ModelPackageContainerDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelPackageStatusDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusdetails.html
    Properties:
        - Name: ValidationStatuses
    
    """
    
    ValidationStatuses_: Optional[List['ModelPackageStatusItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusdetails.html#cfn-sagemaker-modelpackage-modelpackagestatusdetails-validationstatuses""", alias="ValidationStatuses")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelPackageStatusDetails:
        from troposphere.sagemaker import ModelPackageStatusDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelPackageStatusItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusitem.html
    Properties:
        - Name: Status
        - Name: FailureReason
        - Name: Name
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusitem.html#cfn-sagemaker-modelpackage-modelpackagestatusitem-status""", alias="Status")
    FailureReason_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusitem.html#cfn-sagemaker-modelpackage-modelpackagestatusitem-failurereason""", alias="FailureReason")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusitem.html#cfn-sagemaker-modelpackage-modelpackagestatusitem-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelPackageStatusItem:
        from troposphere.sagemaker import ModelPackageStatusItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelQuality(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelquality.html
    Properties:
        - Name: Constraints
        - Name: Statistics
    
    """
    
    Constraints_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelquality.html#cfn-sagemaker-modelpackage-modelquality-constraints""", alias="Constraints")
    Statistics_: Optional['MetricsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelquality.html#cfn-sagemaker-modelpackage-modelquality-statistics""", alias="Statistics")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelQuality:
        from troposphere.sagemaker import ModelQuality as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3DataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-s3datasource.html
    Properties:
        - Name: S3Uri
        - Name: S3DataType
    
    """
    
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-s3datasource.html#cfn-sagemaker-modelpackage-s3datasource-s3uri""", alias="S3Uri")
    S3DataType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-s3datasource.html#cfn-sagemaker-modelpackage-s3datasource-s3datatype""", alias="S3DataType")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.S3DataSource:
        from troposphere.sagemaker import S3DataSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceAlgorithm(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-sourcealgorithm.html
    Properties:
        - Name: ModelDataUrl
        - Name: AlgorithmName
    
    """
    
    ModelDataUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-sourcealgorithm.html#cfn-sagemaker-modelpackage-sourcealgorithm-modeldataurl""", alias="ModelDataUrl")
    AlgorithmName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-sourcealgorithm.html#cfn-sagemaker-modelpackage-sourcealgorithm-algorithmname""", alias="AlgorithmName")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.SourceAlgorithm:
        from troposphere.sagemaker import SourceAlgorithm as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceAlgorithmSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-sourcealgorithmspecification.html
    Properties:
        - Name: SourceAlgorithms
    
    """
    
    SourceAlgorithms_: List['SourceAlgorithm'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-sourcealgorithmspecification.html#cfn-sagemaker-modelpackage-sourcealgorithmspecification-sourcealgorithms""", alias="SourceAlgorithms")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.SourceAlgorithmSpecification:
        from troposphere.sagemaker import SourceAlgorithmSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TransformInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transforminput.html
    Properties:
        - Name: ContentType
        - Name: SplitType
        - Name: CompressionType
        - Name: DataSource
    
    """
    
    ContentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transforminput.html#cfn-sagemaker-modelpackage-transforminput-contenttype""", alias="ContentType")
    SplitType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transforminput.html#cfn-sagemaker-modelpackage-transforminput-splittype""", alias="SplitType")
    CompressionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transforminput.html#cfn-sagemaker-modelpackage-transforminput-compressiontype""", alias="CompressionType")
    DataSource_: 'DataSource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transforminput.html#cfn-sagemaker-modelpackage-transforminput-datasource""", alias="DataSource")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.TransformInput:
        from troposphere.sagemaker import TransformInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TransformJobDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformjobdefinition.html
    Properties:
        - Name: TransformResources
        - Name: MaxConcurrentTransforms
        - Name: MaxPayloadInMB
        - Name: TransformOutput
        - Name: Environment
        - Name: TransformInput
        - Name: BatchStrategy
    
    """
    
    TransformResources_: 'TransformResources' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformjobdefinition.html#cfn-sagemaker-modelpackage-transformjobdefinition-transformresources""", alias="TransformResources")
    MaxConcurrentTransforms_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformjobdefinition.html#cfn-sagemaker-modelpackage-transformjobdefinition-maxconcurrenttransforms""", alias="MaxConcurrentTransforms")
    MaxPayloadInMB_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformjobdefinition.html#cfn-sagemaker-modelpackage-transformjobdefinition-maxpayloadinmb""", alias="MaxPayloadInMB")
    TransformOutput_: 'TransformOutput' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformjobdefinition.html#cfn-sagemaker-modelpackage-transformjobdefinition-transformoutput""", alias="TransformOutput")
    Environment_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformjobdefinition.html#cfn-sagemaker-modelpackage-transformjobdefinition-environment""", alias="Environment")
    TransformInput_: 'TransformInput' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformjobdefinition.html#cfn-sagemaker-modelpackage-transformjobdefinition-transforminput""", alias="TransformInput")
    BatchStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformjobdefinition.html#cfn-sagemaker-modelpackage-transformjobdefinition-batchstrategy""", alias="BatchStrategy")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.TransformJobDefinition:
        from troposphere.sagemaker import TransformJobDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TransformOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformoutput.html
    Properties:
        - Name: AssembleWith
        - Name: Accept
        - Name: KmsKeyId
        - Name: S3OutputPath
    
    """
    
    AssembleWith_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformoutput.html#cfn-sagemaker-modelpackage-transformoutput-assemblewith""", alias="AssembleWith")
    Accept_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformoutput.html#cfn-sagemaker-modelpackage-transformoutput-accept""", alias="Accept")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformoutput.html#cfn-sagemaker-modelpackage-transformoutput-kmskeyid""", alias="KmsKeyId")
    S3OutputPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformoutput.html#cfn-sagemaker-modelpackage-transformoutput-s3outputpath""", alias="S3OutputPath")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.TransformOutput:
        from troposphere.sagemaker import TransformOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TransformResources(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformresources.html
    Properties:
        - Name: InstanceCount
        - Name: VolumeKmsKeyId
        - Name: InstanceType
    
    """
    
    InstanceCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformresources.html#cfn-sagemaker-modelpackage-transformresources-instancecount""", alias="InstanceCount")
    VolumeKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformresources.html#cfn-sagemaker-modelpackage-transformresources-volumekmskeyid""", alias="VolumeKmsKeyId")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformresources.html#cfn-sagemaker-modelpackage-transformresources-instancetype""", alias="InstanceType")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.TransformResources:
        from troposphere.sagemaker import TransformResources as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ValidationProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationprofile.html
    Properties:
        - Name: ProfileName
        - Name: TransformJobDefinition
    
    """
    
    ProfileName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationprofile.html#cfn-sagemaker-modelpackage-validationprofile-profilename""", alias="ProfileName")
    TransformJobDefinition_: 'TransformJobDefinition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationprofile.html#cfn-sagemaker-modelpackage-validationprofile-transformjobdefinition""", alias="TransformJobDefinition")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ValidationProfile:
        from troposphere.sagemaker import ValidationProfile as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ValidationSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationspecification.html
    Properties:
        - Name: ValidationRole
        - Name: ValidationProfiles
    
    """
    
    ValidationRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationspecification.html#cfn-sagemaker-modelpackage-validationspecification-validationrole""", alias="ValidationRole")
    ValidationProfiles_: List['ValidationProfile'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationspecification.html#cfn-sagemaker-modelpackage-validationspecification-validationprofiles""", alias="ValidationProfiles")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ValidationSpecification:
        from troposphere.sagemaker import ValidationSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchTransformInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html
    Properties:
        - Name: DatasetFormat
        - Name: S3DataDistributionType
        - Name: StartTimeOffset
        - Name: EndTimeOffset
        - Name: ProbabilityThresholdAttribute
        - Name: InferenceAttribute
        - Name: DataCapturedDestinationS3Uri
        - Name: S3InputMode
        - Name: LocalPath
        - Name: ProbabilityAttribute
    
    """
    
    DatasetFormat_: 'DatasetFormat' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-datasetformat""", alias="DatasetFormat")
    S3DataDistributionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-s3datadistributiontype""", alias="S3DataDistributionType")
    StartTimeOffset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-starttimeoffset""", alias="StartTimeOffset")
    EndTimeOffset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-endtimeoffset""", alias="EndTimeOffset")
    ProbabilityThresholdAttribute_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-probabilitythresholdattribute""", alias="ProbabilityThresholdAttribute")
    InferenceAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-inferenceattribute""", alias="InferenceAttribute")
    DataCapturedDestinationS3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-datacaptureddestinations3uri""", alias="DataCapturedDestinationS3Uri")
    S3InputMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-s3inputmode""", alias="S3InputMode")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-localpath""", alias="LocalPath")
    ProbabilityAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-probabilityattribute""", alias="ProbabilityAttribute")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.BatchTransformInput:
        from troposphere.sagemaker import BatchTransformInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClusterConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html
    Properties:
        - Name: InstanceCount
        - Name: VolumeSizeInGB
        - Name: VolumeKmsKeyId
        - Name: InstanceType
    
    """
    
    InstanceCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancecount""", alias="InstanceCount")
    VolumeSizeInGB_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumesizeingb""", alias="VolumeSizeInGB")
    VolumeKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumekmskeyid""", alias="VolumeKmsKeyId")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancetype""", alias="InstanceType")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ClusterConfig:
        from troposphere.sagemaker import ClusterConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConstraintsResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-constraintsresource.html
    Properties:
        - Name: S3Uri
    
    """
    
    S3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-constraintsresource.html#cfn-sagemaker-modelqualityjobdefinition-constraintsresource-s3uri""", alias="S3Uri")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ConstraintsResource:
        from troposphere.sagemaker import ConstraintsResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Csv(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-csv.html
    Properties:
        - Name: Header
    
    """
    
    Header_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-csv.html#cfn-sagemaker-modelqualityjobdefinition-csv-header""", alias="Header")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Csv:
        from troposphere.sagemaker import Csv as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatasetFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-datasetformat.html
    Properties:
        - Name: Parquet
        - Name: Csv
        - Name: Json
    
    """
    
    Parquet_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-datasetformat.html#cfn-sagemaker-modelqualityjobdefinition-datasetformat-parquet""", alias="Parquet")
    Csv_: Optional['Csv'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-datasetformat.html#cfn-sagemaker-modelqualityjobdefinition-datasetformat-csv""", alias="Csv")
    Json_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-datasetformat.html#cfn-sagemaker-modelqualityjobdefinition-datasetformat-json""", alias="Json")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DatasetFormat:
        from troposphere.sagemaker import DatasetFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EndpointInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html
    Properties:
        - Name: S3DataDistributionType
        - Name: StartTimeOffset
        - Name: EndTimeOffset
        - Name: ProbabilityThresholdAttribute
        - Name: EndpointName
        - Name: InferenceAttribute
        - Name: S3InputMode
        - Name: LocalPath
        - Name: ProbabilityAttribute
    
    """
    
    S3DataDistributionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-s3datadistributiontype""", alias="S3DataDistributionType")
    StartTimeOffset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-starttimeoffset""", alias="StartTimeOffset")
    EndTimeOffset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-endtimeoffset""", alias="EndTimeOffset")
    ProbabilityThresholdAttribute_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-probabilitythresholdattribute""", alias="ProbabilityThresholdAttribute")
    EndpointName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-endpointname""", alias="EndpointName")
    InferenceAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-inferenceattribute""", alias="InferenceAttribute")
    S3InputMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-s3inputmode""", alias="S3InputMode")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-localpath""", alias="LocalPath")
    ProbabilityAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-probabilityattribute""", alias="ProbabilityAttribute")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.EndpointInput:
        from troposphere.sagemaker import EndpointInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Json(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-json.html
    Properties:
        - Name: Line
    
    """
    
    Line_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-json.html#cfn-sagemaker-modelqualityjobdefinition-json-line""", alias="Line")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Json:
        from troposphere.sagemaker import Json as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelQualityAppSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html
    Properties:
        - Name: ContainerEntrypoint
        - Name: ProblemType
        - Name: PostAnalyticsProcessorSourceUri
        - Name: RecordPreprocessorSourceUri
        - Name: Environment
        - Name: ImageUri
        - Name: ContainerArguments
    
    """
    
    ContainerEntrypoint_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-containerentrypoint""", alias="ContainerEntrypoint")
    ProblemType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-problemtype""", alias="ProblemType")
    PostAnalyticsProcessorSourceUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-postanalyticsprocessorsourceuri""", alias="PostAnalyticsProcessorSourceUri")
    RecordPreprocessorSourceUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-recordpreprocessorsourceuri""", alias="RecordPreprocessorSourceUri")
    Environment_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-environment""", alias="Environment")
    ImageUri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-imageuri""", alias="ImageUri")
    ContainerArguments_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-containerarguments""", alias="ContainerArguments")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelQualityAppSpecification:
        from troposphere.sagemaker import ModelQualityAppSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelQualityBaselineConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html
    Properties:
        - Name: ConstraintsResource
        - Name: BaseliningJobName
    
    """
    
    ConstraintsResource_: Optional['ConstraintsResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-constraintsresource""", alias="ConstraintsResource")
    BaseliningJobName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-baseliningjobname""", alias="BaseliningJobName")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelQualityBaselineConfig:
        from troposphere.sagemaker import ModelQualityBaselineConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ModelQualityJobInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html
    Properties:
        - Name: GroundTruthS3Input
        - Name: BatchTransformInput
        - Name: EndpointInput
    
    """
    
    GroundTruthS3Input_: 'MonitoringGroundTruthS3Input' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-groundtruths3input""", alias="GroundTruthS3Input")
    BatchTransformInput_: Optional['BatchTransformInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-batchtransforminput""", alias="BatchTransformInput")
    EndpointInput_: Optional['EndpointInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-endpointinput""", alias="EndpointInput")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelQualityJobInput:
        from troposphere.sagemaker import ModelQualityJobInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringGroundTruthS3Input(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input.html
    Properties:
        - Name: S3Uri
    
    """
    
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input.html#cfn-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input-s3uri""", alias="S3Uri")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringGroundTruthS3Input:
        from troposphere.sagemaker import MonitoringGroundTruthS3Input as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutput.html
    Properties:
        - Name: S3Output
    
    """
    
    S3Output_: 'S3Output' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutput.html#cfn-sagemaker-modelqualityjobdefinition-monitoringoutput-s3output""", alias="S3Output")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringOutput:
        from troposphere.sagemaker import MonitoringOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringOutputConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutputconfig.html
    Properties:
        - Name: KmsKeyId
        - Name: MonitoringOutputs
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelqualityjobdefinition-monitoringoutputconfig-kmskeyid""", alias="KmsKeyId")
    MonitoringOutputs_: List['MonitoringOutput'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelqualityjobdefinition-monitoringoutputconfig-monitoringoutputs""", alias="MonitoringOutputs")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringOutputConfig:
        from troposphere.sagemaker import MonitoringOutputConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringResources(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringresources.html
    Properties:
        - Name: ClusterConfig
    
    """
    
    ClusterConfig_: 'ClusterConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringresources.html#cfn-sagemaker-modelqualityjobdefinition-monitoringresources-clusterconfig""", alias="ClusterConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringResources:
        from troposphere.sagemaker import MonitoringResources as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html
    Properties:
        - Name: EnableNetworkIsolation
        - Name: EnableInterContainerTrafficEncryption
        - Name: VpcConfig
    
    """
    
    EnableNetworkIsolation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig-enablenetworkisolation""", alias="EnableNetworkIsolation")
    EnableInterContainerTrafficEncryption_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig-enableintercontainertrafficencryption""", alias="EnableInterContainerTrafficEncryption")
    VpcConfig_: Optional['VpcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig-vpcconfig""", alias="VpcConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.NetworkConfig:
        from troposphere.sagemaker import NetworkConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Output(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html
    Properties:
        - Name: S3Uri
        - Name: LocalPath
        - Name: S3UploadMode
    
    """
    
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html#cfn-sagemaker-modelqualityjobdefinition-s3output-s3uri""", alias="S3Uri")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html#cfn-sagemaker-modelqualityjobdefinition-s3output-localpath""", alias="LocalPath")
    S3UploadMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html#cfn-sagemaker-modelqualityjobdefinition-s3output-s3uploadmode""", alias="S3UploadMode")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.S3Output:
        from troposphere.sagemaker import S3Output as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StoppingCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-stoppingcondition.html
    Properties:
        - Name: MaxRuntimeInSeconds
    
    """
    
    MaxRuntimeInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-stoppingcondition.html#cfn-sagemaker-modelqualityjobdefinition-stoppingcondition-maxruntimeinseconds""", alias="MaxRuntimeInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.StoppingCondition:
        from troposphere.sagemaker import StoppingCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-vpcconfig.html
    Properties:
        - Name: Subnets
        - Name: SecurityGroupIds
    
    """
    
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-vpcconfig.html#cfn-sagemaker-modelqualityjobdefinition-vpcconfig-subnets""", alias="Subnets")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-vpcconfig.html#cfn-sagemaker-modelqualityjobdefinition-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.VpcConfig:
        from troposphere.sagemaker import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BaselineConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html
    Properties:
        - Name: StatisticsResource
        - Name: ConstraintsResource
    
    """
    
    StatisticsResource_: Optional['StatisticsResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html#cfn-sagemaker-monitoringschedule-baselineconfig-statisticsresource""", alias="StatisticsResource")
    ConstraintsResource_: Optional['ConstraintsResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html#cfn-sagemaker-monitoringschedule-baselineconfig-constraintsresource""", alias="ConstraintsResource")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.BaselineConfig:
        from troposphere.sagemaker import BaselineConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchTransformInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-batchtransforminput.html
    Properties:
        - Name: DatasetFormat
        - Name: S3DataDistributionType
        - Name: DataCapturedDestinationS3Uri
        - Name: S3InputMode
        - Name: LocalPath
        - Name: ExcludeFeaturesAttribute
    
    """
    
    DatasetFormat_: 'DatasetFormat' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-batchtransforminput.html#cfn-sagemaker-monitoringschedule-batchtransforminput-datasetformat""", alias="DatasetFormat")
    S3DataDistributionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-batchtransforminput.html#cfn-sagemaker-monitoringschedule-batchtransforminput-s3datadistributiontype""", alias="S3DataDistributionType")
    DataCapturedDestinationS3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-batchtransforminput.html#cfn-sagemaker-monitoringschedule-batchtransforminput-datacaptureddestinations3uri""", alias="DataCapturedDestinationS3Uri")
    S3InputMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-batchtransforminput.html#cfn-sagemaker-monitoringschedule-batchtransforminput-s3inputmode""", alias="S3InputMode")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-batchtransforminput.html#cfn-sagemaker-monitoringschedule-batchtransforminput-localpath""", alias="LocalPath")
    ExcludeFeaturesAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-batchtransforminput.html#cfn-sagemaker-monitoringschedule-batchtransforminput-excludefeaturesattribute""", alias="ExcludeFeaturesAttribute")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.BatchTransformInput:
        from troposphere.sagemaker import BatchTransformInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClusterConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html
    Properties:
        - Name: InstanceCount
        - Name: VolumeSizeInGB
        - Name: VolumeKmsKeyId
        - Name: InstanceType
    
    """
    
    InstanceCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-instancecount""", alias="InstanceCount")
    VolumeSizeInGB_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-volumesizeingb""", alias="VolumeSizeInGB")
    VolumeKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-volumekmskeyid""", alias="VolumeKmsKeyId")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-instancetype""", alias="InstanceType")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ClusterConfig:
        from troposphere.sagemaker import ClusterConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConstraintsResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-constraintsresource.html
    Properties:
        - Name: S3Uri
    
    """
    
    S3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-constraintsresource.html#cfn-sagemaker-monitoringschedule-constraintsresource-s3uri""", alias="S3Uri")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ConstraintsResource:
        from troposphere.sagemaker import ConstraintsResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Csv(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-csv.html
    Properties:
        - Name: Header
    
    """
    
    Header_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-csv.html#cfn-sagemaker-monitoringschedule-csv-header""", alias="Header")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Csv:
        from troposphere.sagemaker import Csv as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatasetFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-datasetformat.html
    Properties:
        - Name: Parquet
        - Name: Csv
        - Name: Json
    
    """
    
    Parquet_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-datasetformat.html#cfn-sagemaker-monitoringschedule-datasetformat-parquet""", alias="Parquet")
    Csv_: Optional['Csv'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-datasetformat.html#cfn-sagemaker-monitoringschedule-datasetformat-csv""", alias="Csv")
    Json_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-datasetformat.html#cfn-sagemaker-monitoringschedule-datasetformat-json""", alias="Json")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.DatasetFormat:
        from troposphere.sagemaker import DatasetFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EndpointInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html
    Properties:
        - Name: S3DataDistributionType
        - Name: EndpointName
        - Name: S3InputMode
        - Name: LocalPath
        - Name: ExcludeFeaturesAttribute
    
    """
    
    S3DataDistributionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-s3datadistributiontype""", alias="S3DataDistributionType")
    EndpointName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-endpointname""", alias="EndpointName")
    S3InputMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-s3inputmode""", alias="S3InputMode")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-localpath""", alias="LocalPath")
    ExcludeFeaturesAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-excludefeaturesattribute""", alias="ExcludeFeaturesAttribute")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.EndpointInput:
        from troposphere.sagemaker import EndpointInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Json(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-json.html
    Properties:
        - Name: Line
    
    """
    
    Line_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-json.html#cfn-sagemaker-monitoringschedule-json-line""", alias="Line")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.Json:
        from troposphere.sagemaker import Json as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringAppSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html
    Properties:
        - Name: ContainerEntrypoint
        - Name: PostAnalyticsProcessorSourceUri
        - Name: RecordPreprocessorSourceUri
        - Name: ImageUri
        - Name: ContainerArguments
    
    """
    
    ContainerEntrypoint_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-containerentrypoint""", alias="ContainerEntrypoint")
    PostAnalyticsProcessorSourceUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-postanalyticsprocessorsourceuri""", alias="PostAnalyticsProcessorSourceUri")
    RecordPreprocessorSourceUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-recordpreprocessorsourceuri""", alias="RecordPreprocessorSourceUri")
    ImageUri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-imageuri""", alias="ImageUri")
    ContainerArguments_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-containerarguments""", alias="ContainerArguments")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringAppSpecification:
        from troposphere.sagemaker import MonitoringAppSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringExecutionSummary(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html
    Properties:
        - Name: ScheduledTime
        - Name: EndpointName
        - Name: MonitoringScheduleName
        - Name: ProcessingJobArn
        - Name: FailureReason
        - Name: CreationTime
        - Name: LastModifiedTime
        - Name: MonitoringExecutionStatus
    
    """
    
    ScheduledTime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-scheduledtime""", alias="ScheduledTime")
    EndpointName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-endpointname""", alias="EndpointName")
    MonitoringScheduleName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-monitoringschedulename""", alias="MonitoringScheduleName")
    ProcessingJobArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-processingjobarn""", alias="ProcessingJobArn")
    FailureReason_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-failurereason""", alias="FailureReason")
    CreationTime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-creationtime""", alias="CreationTime")
    LastModifiedTime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-lastmodifiedtime""", alias="LastModifiedTime")
    MonitoringExecutionStatus_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-monitoringexecutionstatus""", alias="MonitoringExecutionStatus")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringExecutionSummary:
        from troposphere.sagemaker import MonitoringExecutionSummary as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinput.html
    Properties:
        - Name: BatchTransformInput
        - Name: EndpointInput
    
    """
    
    BatchTransformInput_: Optional['BatchTransformInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinput.html#cfn-sagemaker-monitoringschedule-monitoringinput-batchtransforminput""", alias="BatchTransformInput")
    EndpointInput_: Optional['EndpointInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinput.html#cfn-sagemaker-monitoringschedule-monitoringinput-endpointinput""", alias="EndpointInput")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringInput:
        from troposphere.sagemaker import MonitoringInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringJobDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html
    Properties:
        - Name: MonitoringInputs
        - Name: MonitoringResources
        - Name: BaselineConfig
        - Name: StoppingCondition
        - Name: MonitoringAppSpecification
        - Name: NetworkConfig
        - Name: Environment
        - Name: MonitoringOutputConfig
        - Name: RoleArn
    
    """
    
    MonitoringInputs_: List['MonitoringInput'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringinputs""", alias="MonitoringInputs")
    MonitoringResources_: 'MonitoringResources' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringresources""", alias="MonitoringResources")
    BaselineConfig_: Optional['BaselineConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-baselineconfig""", alias="BaselineConfig")
    StoppingCondition_: Optional['StoppingCondition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-stoppingcondition""", alias="StoppingCondition")
    MonitoringAppSpecification_: 'MonitoringAppSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringappspecification""", alias="MonitoringAppSpecification")
    NetworkConfig_: Optional['NetworkConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-networkconfig""", alias="NetworkConfig")
    Environment_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-environment""", alias="Environment")
    MonitoringOutputConfig_: 'MonitoringOutputConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringoutputconfig""", alias="MonitoringOutputConfig")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringJobDefinition:
        from troposphere.sagemaker import MonitoringJobDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html
    Properties:
        - Name: S3Output
    
    """
    
    S3Output_: 'S3Output' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html#cfn-sagemaker-monitoringschedule-monitoringoutput-s3output""", alias="S3Output")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringOutput:
        from troposphere.sagemaker import MonitoringOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringOutputConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html
    Properties:
        - Name: KmsKeyId
        - Name: MonitoringOutputs
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html#cfn-sagemaker-monitoringschedule-monitoringoutputconfig-kmskeyid""", alias="KmsKeyId")
    MonitoringOutputs_: List['MonitoringOutput'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html#cfn-sagemaker-monitoringschedule-monitoringoutputconfig-monitoringoutputs""", alias="MonitoringOutputs")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringOutputConfig:
        from troposphere.sagemaker import MonitoringOutputConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringResources(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringresources.html
    Properties:
        - Name: ClusterConfig
    
    """
    
    ClusterConfig_: 'ClusterConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringresources.html#cfn-sagemaker-monitoringschedule-monitoringresources-clusterconfig""", alias="ClusterConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringResources:
        from troposphere.sagemaker import MonitoringResources as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringScheduleConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html
    Properties:
        - Name: ScheduleConfig
        - Name: MonitoringJobDefinition
        - Name: MonitoringJobDefinitionName
        - Name: MonitoringType
    
    """
    
    ScheduleConfig_: Optional['ScheduleConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-scheduleconfig""", alias="ScheduleConfig")
    MonitoringJobDefinition_: Optional['MonitoringJobDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinition""", alias="MonitoringJobDefinition")
    MonitoringJobDefinitionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinitionname""", alias="MonitoringJobDefinitionName")
    MonitoringType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringtype""", alias="MonitoringType")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringScheduleConfig:
        from troposphere.sagemaker import MonitoringScheduleConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html
    Properties:
        - Name: EnableNetworkIsolation
        - Name: EnableInterContainerTrafficEncryption
        - Name: VpcConfig
    
    """
    
    EnableNetworkIsolation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-enablenetworkisolation""", alias="EnableNetworkIsolation")
    EnableInterContainerTrafficEncryption_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-enableintercontainertrafficencryption""", alias="EnableInterContainerTrafficEncryption")
    VpcConfig_: Optional['VpcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-vpcconfig""", alias="VpcConfig")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.NetworkConfig:
        from troposphere.sagemaker import NetworkConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Output(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html
    Properties:
        - Name: S3Uri
        - Name: LocalPath
        - Name: S3UploadMode
    
    """
    
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html#cfn-sagemaker-monitoringschedule-s3output-s3uri""", alias="S3Uri")
    LocalPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html#cfn-sagemaker-monitoringschedule-s3output-localpath""", alias="LocalPath")
    S3UploadMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html#cfn-sagemaker-monitoringschedule-s3output-s3uploadmode""", alias="S3UploadMode")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.S3Output:
        from troposphere.sagemaker import S3Output as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScheduleConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html
    Properties:
        - Name: ScheduleExpression
        - Name: DataAnalysisStartTime
        - Name: DataAnalysisEndTime
    
    """
    
    ScheduleExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html#cfn-sagemaker-monitoringschedule-scheduleconfig-scheduleexpression""", alias="ScheduleExpression")
    DataAnalysisStartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html#cfn-sagemaker-monitoringschedule-scheduleconfig-dataanalysisstarttime""", alias="DataAnalysisStartTime")
    DataAnalysisEndTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html#cfn-sagemaker-monitoringschedule-scheduleconfig-dataanalysisendtime""", alias="DataAnalysisEndTime")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ScheduleConfig:
        from troposphere.sagemaker import ScheduleConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatisticsResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-statisticsresource.html
    Properties:
        - Name: S3Uri
    
    """
    
    S3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-statisticsresource.html#cfn-sagemaker-monitoringschedule-statisticsresource-s3uri""", alias="S3Uri")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.StatisticsResource:
        from troposphere.sagemaker import StatisticsResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StoppingCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-stoppingcondition.html
    Properties:
        - Name: MaxRuntimeInSeconds
    
    """
    
    MaxRuntimeInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-stoppingcondition.html#cfn-sagemaker-monitoringschedule-stoppingcondition-maxruntimeinseconds""", alias="MaxRuntimeInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.StoppingCondition:
        from troposphere.sagemaker import StoppingCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html
    Properties:
        - Name: Subnets
        - Name: SecurityGroupIds
    
    """
    
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html#cfn-sagemaker-monitoringschedule-vpcconfig-subnets""", alias="Subnets")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html#cfn-sagemaker-monitoringschedule-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.VpcConfig:
        from troposphere.sagemaker import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceMetadataServiceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstance-instancemetadataserviceconfiguration.html
    Properties:
        - Name: MinimumInstanceMetadataServiceVersion
    
    """
    
    MinimumInstanceMetadataServiceVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstance-instancemetadataserviceconfiguration.html#cfn-sagemaker-notebookinstance-instancemetadataserviceconfiguration-minimuminstancemetadataserviceversion""", alias="MinimumInstanceMetadataServiceVersion")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.InstanceMetadataServiceConfiguration:
        from troposphere.sagemaker import InstanceMetadataServiceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotebookInstanceLifecycleHook(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook.html
    Properties:
        - Name: Content
    
    """
    
    Content_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook.html#cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook-content""", alias="Content")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.NotebookInstanceLifecycleHook:
        from troposphere.sagemaker import NotebookInstanceLifecycleHook as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ParallelismConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-pipeline-parallelismconfiguration.html
    Properties:
        - Name: MaxParallelExecutionSteps
    
    """
    
    MaxParallelExecutionSteps_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-pipeline-parallelismconfiguration.html#cfn-sagemaker-pipeline-parallelismconfiguration-maxparallelexecutionsteps""", alias="MaxParallelExecutionSteps")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ParallelismConfiguration:
        from troposphere.sagemaker import ParallelismConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipelineDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-pipeline-pipelinedefinition.html
    Properties:
        - Name: PipelineDefinitionBody
        - Name: PipelineDefinitionS3Location
    
    """
    
    PipelineDefinitionBody_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-pipeline-pipelinedefinition.html#cfn-sagemaker-pipeline-pipelinedefinition-pipelinedefinitionbody""", alias="PipelineDefinitionBody")
    PipelineDefinitionS3Location_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-pipeline-pipelinedefinition.html#cfn-sagemaker-pipeline-pipelinedefinition-pipelinedefinitions3location""", alias="PipelineDefinitionS3Location")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.PipelineDefinition:
        from troposphere.sagemaker import PipelineDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-pipeline-s3location.html
    Properties:
        - Name: Bucket
        - Name: Version
        - Name: ETag
        - Name: Key
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-pipeline-s3location.html#cfn-sagemaker-pipeline-s3location-bucket""", alias="Bucket")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-pipeline-s3location.html#cfn-sagemaker-pipeline-s3location-version""", alias="Version")
    ETag_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-pipeline-s3location.html#cfn-sagemaker-pipeline-s3location-etag""", alias="ETag")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-pipeline-s3location.html#cfn-sagemaker-pipeline-s3location-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.S3Location:
        from troposphere.sagemaker import S3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProvisioningParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-project-provisioningparameter.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-project-provisioningparameter.html#cfn-sagemaker-project-provisioningparameter-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-project-provisioningparameter.html#cfn-sagemaker-project-provisioningparameter-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ProvisioningParameter:
        from troposphere.sagemaker import ProvisioningParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceCatalogProvisionedProductDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-project-servicecatalogprovisionedproductdetails.html
    Properties:
        - Name: ProvisionedProductStatusMessage
        - Name: ProvisionedProductId
    
    """
    
    ProvisionedProductStatusMessage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-project-servicecatalogprovisionedproductdetails.html#cfn-sagemaker-project-servicecatalogprovisionedproductdetails-provisionedproductstatusmessage""", alias="ProvisionedProductStatusMessage")
    ProvisionedProductId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-project-servicecatalogprovisionedproductdetails.html#cfn-sagemaker-project-servicecatalogprovisionedproductdetails-provisionedproductid""", alias="ProvisionedProductId")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ServiceCatalogProvisionedProductDetails:
        from troposphere.sagemaker import ServiceCatalogProvisionedProductDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceCatalogProvisioningDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-project-servicecatalogprovisioningdetails.html
    Properties:
        - Name: PathId
        - Name: ProvisioningParameters
        - Name: ProductId
        - Name: ProvisioningArtifactId
    
    """
    
    PathId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-project-servicecatalogprovisioningdetails.html#cfn-sagemaker-project-servicecatalogprovisioningdetails-pathid""", alias="PathId")
    ProvisioningParameters_: Optional[List['ProvisioningParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-project-servicecatalogprovisioningdetails.html#cfn-sagemaker-project-servicecatalogprovisioningdetails-provisioningparameters""", alias="ProvisioningParameters")
    ProductId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-project-servicecatalogprovisioningdetails.html#cfn-sagemaker-project-servicecatalogprovisioningdetails-productid""", alias="ProductId")
    ProvisioningArtifactId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-project-servicecatalogprovisioningdetails.html#cfn-sagemaker-project-servicecatalogprovisioningdetails-provisioningartifactid""", alias="ProvisioningArtifactId")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ServiceCatalogProvisioningDetails:
        from troposphere.sagemaker import ServiceCatalogProvisioningDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomImage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-customimage.html
    Properties:
        - Name: ImageName
        - Name: AppImageConfigName
        - Name: ImageVersionNumber
    
    """
    
    ImageName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-customimage.html#cfn-sagemaker-space-customimage-imagename""", alias="ImageName")
    AppImageConfigName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-customimage.html#cfn-sagemaker-space-customimage-appimageconfigname""", alias="AppImageConfigName")
    ImageVersionNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-customimage.html#cfn-sagemaker-space-customimage-imageversionnumber""", alias="ImageVersionNumber")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.CustomImage:
        from troposphere.sagemaker import CustomImage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JupyterServerAppSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-jupyterserverappsettings.html
    Properties:
        - Name: DefaultResourceSpec
    
    """
    
    DefaultResourceSpec_: Optional['ResourceSpec'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-jupyterserverappsettings.html#cfn-sagemaker-space-jupyterserverappsettings-defaultresourcespec""", alias="DefaultResourceSpec")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.JupyterServerAppSettings:
        from troposphere.sagemaker import JupyterServerAppSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KernelGatewayAppSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-kernelgatewayappsettings.html
    Properties:
        - Name: CustomImages
        - Name: DefaultResourceSpec
    
    """
    
    CustomImages_: Optional[List['CustomImage']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-kernelgatewayappsettings.html#cfn-sagemaker-space-kernelgatewayappsettings-customimages""", alias="CustomImages")
    DefaultResourceSpec_: Optional['ResourceSpec'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-kernelgatewayappsettings.html#cfn-sagemaker-space-kernelgatewayappsettings-defaultresourcespec""", alias="DefaultResourceSpec")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.KernelGatewayAppSettings:
        from troposphere.sagemaker import KernelGatewayAppSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceSpec(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-resourcespec.html
    Properties:
        - Name: SageMakerImageArn
        - Name: InstanceType
        - Name: SageMakerImageVersionArn
    
    """
    
    SageMakerImageArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-resourcespec.html#cfn-sagemaker-space-resourcespec-sagemakerimagearn""", alias="SageMakerImageArn")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-resourcespec.html#cfn-sagemaker-space-resourcespec-instancetype""", alias="InstanceType")
    SageMakerImageVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-resourcespec.html#cfn-sagemaker-space-resourcespec-sagemakerimageversionarn""", alias="SageMakerImageVersionArn")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ResourceSpec:
        from troposphere.sagemaker import ResourceSpec as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpaceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-spacesettings.html
    Properties:
        - Name: KernelGatewayAppSettings
        - Name: JupyterServerAppSettings
    
    """
    
    KernelGatewayAppSettings_: Optional['KernelGatewayAppSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-spacesettings.html#cfn-sagemaker-space-spacesettings-kernelgatewayappsettings""", alias="KernelGatewayAppSettings")
    JupyterServerAppSettings_: Optional['JupyterServerAppSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-space-spacesettings.html#cfn-sagemaker-space-spacesettings-jupyterserverappsettings""", alias="JupyterServerAppSettings")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.SpaceSettings:
        from troposphere.sagemaker import SpaceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomImage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-customimage.html
    Properties:
        - Name: ImageName
        - Name: AppImageConfigName
        - Name: ImageVersionNumber
    
    """
    
    ImageName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-customimage.html#cfn-sagemaker-userprofile-customimage-imagename""", alias="ImageName")
    AppImageConfigName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-customimage.html#cfn-sagemaker-userprofile-customimage-appimageconfigname""", alias="AppImageConfigName")
    ImageVersionNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-customimage.html#cfn-sagemaker-userprofile-customimage-imageversionnumber""", alias="ImageVersionNumber")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.CustomImage:
        from troposphere.sagemaker import CustomImage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JupyterServerAppSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-jupyterserverappsettings.html
    Properties:
        - Name: DefaultResourceSpec
    
    """
    
    DefaultResourceSpec_: Optional['ResourceSpec'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-jupyterserverappsettings.html#cfn-sagemaker-userprofile-jupyterserverappsettings-defaultresourcespec""", alias="DefaultResourceSpec")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.JupyterServerAppSettings:
        from troposphere.sagemaker import JupyterServerAppSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KernelGatewayAppSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-kernelgatewayappsettings.html
    Properties:
        - Name: CustomImages
        - Name: DefaultResourceSpec
    
    """
    
    CustomImages_: Optional[List['CustomImage']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-kernelgatewayappsettings.html#cfn-sagemaker-userprofile-kernelgatewayappsettings-customimages""", alias="CustomImages")
    DefaultResourceSpec_: Optional['ResourceSpec'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-kernelgatewayappsettings.html#cfn-sagemaker-userprofile-kernelgatewayappsettings-defaultresourcespec""", alias="DefaultResourceSpec")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.KernelGatewayAppSettings:
        from troposphere.sagemaker import KernelGatewayAppSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RStudioServerProAppSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-rstudioserverproappsettings.html
    Properties:
        - Name: AccessStatus
        - Name: UserGroup
    
    """
    
    AccessStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-rstudioserverproappsettings.html#cfn-sagemaker-userprofile-rstudioserverproappsettings-accessstatus""", alias="AccessStatus")
    UserGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-rstudioserverproappsettings.html#cfn-sagemaker-userprofile-rstudioserverproappsettings-usergroup""", alias="UserGroup")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.RStudioServerProAppSettings:
        from troposphere.sagemaker import RStudioServerProAppSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceSpec(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-resourcespec.html
    Properties:
        - Name: SageMakerImageArn
        - Name: InstanceType
        - Name: SageMakerImageVersionArn
    
    """
    
    SageMakerImageArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-resourcespec.html#cfn-sagemaker-userprofile-resourcespec-sagemakerimagearn""", alias="SageMakerImageArn")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-resourcespec.html#cfn-sagemaker-userprofile-resourcespec-instancetype""", alias="InstanceType")
    SageMakerImageVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-resourcespec.html#cfn-sagemaker-userprofile-resourcespec-sagemakerimageversionarn""", alias="SageMakerImageVersionArn")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.ResourceSpec:
        from troposphere.sagemaker import ResourceSpec as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SharingSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-sharingsettings.html
    Properties:
        - Name: NotebookOutputOption
        - Name: S3KmsKeyId
        - Name: S3OutputPath
    
    """
    
    NotebookOutputOption_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-sharingsettings.html#cfn-sagemaker-userprofile-sharingsettings-notebookoutputoption""", alias="NotebookOutputOption")
    S3KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-sharingsettings.html#cfn-sagemaker-userprofile-sharingsettings-s3kmskeyid""", alias="S3KmsKeyId")
    S3OutputPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-sharingsettings.html#cfn-sagemaker-userprofile-sharingsettings-s3outputpath""", alias="S3OutputPath")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.SharingSettings:
        from troposphere.sagemaker import SharingSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html
    Properties:
        - Name: SecurityGroups
        - Name: KernelGatewayAppSettings
        - Name: RStudioServerProAppSettings
        - Name: JupyterServerAppSettings
        - Name: ExecutionRole
        - Name: SharingSettings
    
    """
    
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-securitygroups""", alias="SecurityGroups")
    KernelGatewayAppSettings_: Optional['KernelGatewayAppSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-kernelgatewayappsettings""", alias="KernelGatewayAppSettings")
    RStudioServerProAppSettings_: Optional['RStudioServerProAppSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-rstudioserverproappsettings""", alias="RStudioServerProAppSettings")
    JupyterServerAppSettings_: Optional['JupyterServerAppSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-jupyterserverappsettings""", alias="JupyterServerAppSettings")
    ExecutionRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-executionrole""", alias="ExecutionRole")
    SharingSettings_: Optional['SharingSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-sharingsettings""", alias="SharingSettings")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.UserSettings:
        from troposphere.sagemaker import UserSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CognitoMemberDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html
    Properties:
        - Name: CognitoUserPool
        - Name: CognitoClientId
        - Name: CognitoUserGroup
    
    """
    
    CognitoUserPool_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html#cfn-sagemaker-workteam-cognitomemberdefinition-cognitouserpool""", alias="CognitoUserPool")
    CognitoClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html#cfn-sagemaker-workteam-cognitomemberdefinition-cognitoclientid""", alias="CognitoClientId")
    CognitoUserGroup_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html#cfn-sagemaker-workteam-cognitomemberdefinition-cognitousergroup""", alias="CognitoUserGroup")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.CognitoMemberDefinition:
        from troposphere.sagemaker import CognitoMemberDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MemberDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-memberdefinition.html
    Properties:
        - Name: OidcMemberDefinition
        - Name: CognitoMemberDefinition
    
    """
    
    OidcMemberDefinition_: Optional['OidcMemberDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-memberdefinition.html#cfn-sagemaker-workteam-memberdefinition-oidcmemberdefinition""", alias="OidcMemberDefinition")
    CognitoMemberDefinition_: Optional['CognitoMemberDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-memberdefinition.html#cfn-sagemaker-workteam-memberdefinition-cognitomemberdefinition""", alias="CognitoMemberDefinition")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.MemberDefinition:
        from troposphere.sagemaker import MemberDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-notificationconfiguration.html
    Properties:
        - Name: NotificationTopicArn
    
    """
    
    NotificationTopicArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-notificationconfiguration.html#cfn-sagemaker-workteam-notificationconfiguration-notificationtopicarn""", alias="NotificationTopicArn")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.NotificationConfiguration:
        from troposphere.sagemaker import NotificationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OidcMemberDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-oidcmemberdefinition.html
    Properties:
        - Name: OidcGroups
    
    """
    
    OidcGroups_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-oidcmemberdefinition.html#cfn-sagemaker-workteam-oidcmemberdefinition-oidcgroups""", alias="OidcGroups")
    


    @property
    def tropo_type(self) -> troposphere.sagemaker.OidcMemberDefinition:
        from troposphere.sagemaker import OidcMemberDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class App(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html
    Properties:
        - Name: DomainId
        - Name: ResourceSpec
        - Name: AppType
        - Name: Tags
        - Name: UserProfileName
        - Name: AppName
    Attributes:
        - Name: AppArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DomainId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-domainid""", alias="DomainId")
    ResourceSpec_: Optional['ResourceSpec'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-resourcespec""", alias="ResourceSpec")
    AppType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-apptype""", alias="AppType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-tags""", alias="Tags")
    UserProfileName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-userprofilename""", alias="UserProfileName")
    AppName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-appname""", alias="AppName")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.App:
        from troposphere.sagemaker import App as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import App as TropoT
        return resource_to_troposphere(self, TropoT)


class AppImageConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html
    Properties:
        - Name: KernelGatewayImageConfig
        - Name: AppImageConfigName
        - Name: Tags
    Attributes:
        - Name: AppImageConfigArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KernelGatewayImageConfig_: Optional['KernelGatewayImageConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig""", alias="KernelGatewayImageConfig")
    AppImageConfigName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-appimageconfigname""", alias="AppImageConfigName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.AppImageConfig:
        from troposphere.sagemaker import AppImageConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import AppImageConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class CodeRepository(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html
    Properties:
        - Name: CodeRepositoryName
        - Name: GitConfig
        - Name: Tags
    Attributes:
        - Name: CodeRepositoryName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CodeRepositoryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-coderepositoryname""", alias="CodeRepositoryName")
    GitConfig_: 'GitConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-gitconfig""", alias="GitConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.CodeRepository:
        from troposphere.sagemaker import CodeRepository as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import CodeRepository as TropoT
        return resource_to_troposphere(self, TropoT)


class DataQualityJobDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html
    Properties:
        - Name: DataQualityJobInput
        - Name: DataQualityAppSpecification
        - Name: EndpointName
        - Name: StoppingCondition
        - Name: JobDefinitionName
        - Name: JobResources
        - Name: NetworkConfig
        - Name: DataQualityJobOutputConfig
        - Name: DataQualityBaselineConfig
        - Name: RoleArn
        - Name: Tags
    Attributes:
        - Name: JobDefinitionArn
        - Name: CreationTime
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DataQualityJobInput_: 'DataQualityJobInput' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput""", alias="DataQualityJobInput")
    DataQualityAppSpecification_: 'DataQualityAppSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification""", alias="DataQualityAppSpecification")
    EndpointName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-endpointname""", alias="EndpointName")
    StoppingCondition_: Optional['StoppingCondition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition""", alias="StoppingCondition")
    JobDefinitionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobdefinitionname""", alias="JobDefinitionName")
    JobResources_: 'MonitoringResources' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobresources""", alias="JobResources")
    NetworkConfig_: Optional['NetworkConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig""", alias="NetworkConfig")
    DataQualityJobOutputConfig_: 'MonitoringOutputConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjoboutputconfig""", alias="DataQualityJobOutputConfig")
    DataQualityBaselineConfig_: Optional['DataQualityBaselineConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig""", alias="DataQualityBaselineConfig")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.DataQualityJobDefinition:
        from troposphere.sagemaker import DataQualityJobDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import DataQualityJobDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class Device(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html
    Properties:
        - Name: DeviceFleetName
        - Name: Device
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DeviceFleetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-devicefleetname""", alias="DeviceFleetName")
    Device_: Optional['Device'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-device""", alias="Device")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.Device:
        from troposphere.sagemaker import Device as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import Device as TropoT
        return resource_to_troposphere(self, TropoT)


class DeviceFleet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html
    Properties:
        - Name: DeviceFleetName
        - Name: Description
        - Name: OutputConfig
        - Name: RoleArn
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DeviceFleetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-devicefleetname""", alias="DeviceFleetName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-description""", alias="Description")
    OutputConfig_: 'EdgeOutputConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-outputconfig""", alias="OutputConfig")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.DeviceFleet:
        from troposphere.sagemaker import DeviceFleet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import DeviceFleet as TropoT
        return resource_to_troposphere(self, TropoT)


class Domain(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html
    Properties:
        - Name: AppNetworkAccessType
        - Name: DefaultSpaceSettings
        - Name: KmsKeyId
        - Name: VpcId
        - Name: DomainName
        - Name: AppSecurityGroupManagement
        - Name: DefaultUserSettings
        - Name: SubnetIds
        - Name: AuthMode
        - Name: Tags
        - Name: DomainSettings
    Attributes:
        - Name: HomeEfsFileSystemId
        - Name: DomainId
        - Name: SecurityGroupIdForDomainBoundary
        - Name: SingleSignOnManagedApplicationInstanceId
        - Name: DomainArn
        - Name: Url
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AppNetworkAccessType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-appnetworkaccesstype""", alias="AppNetworkAccessType")
    DefaultSpaceSettings_: Optional['DefaultSpaceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-defaultspacesettings""", alias="DefaultSpaceSettings")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-kmskeyid""", alias="KmsKeyId")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-vpcid""", alias="VpcId")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-domainname""", alias="DomainName")
    AppSecurityGroupManagement_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-appsecuritygroupmanagement""", alias="AppSecurityGroupManagement")
    DefaultUserSettings_: 'UserSettings' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-defaultusersettings""", alias="DefaultUserSettings")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-subnetids""", alias="SubnetIds")
    AuthMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-authmode""", alias="AuthMode")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-tags""", alias="Tags")
    DomainSettings_: Optional['DomainSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-domainsettings""", alias="DomainSettings")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.Domain:
        from troposphere.sagemaker import Domain as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import Domain as TropoT
        return resource_to_troposphere(self, TropoT)


class Endpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html
    Properties:
        - Name: RetainAllVariantProperties
        - Name: EndpointName
        - Name: ExcludeRetainedVariantProperties
        - Name: EndpointConfigName
        - Name: DeploymentConfig
        - Name: RetainDeploymentConfig
        - Name: Tags
    Attributes:
        - Name: EndpointName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RetainAllVariantProperties_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-retainallvariantproperties""", alias="RetainAllVariantProperties")
    EndpointName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointname""", alias="EndpointName")
    ExcludeRetainedVariantProperties_: Optional[List['VariantProperty']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-excluderetainedvariantproperties""", alias="ExcludeRetainedVariantProperties")
    EndpointConfigName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointconfigname""", alias="EndpointConfigName")
    DeploymentConfig_: Optional['DeploymentConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-deploymentconfig""", alias="DeploymentConfig")
    RetainDeploymentConfig_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-retaindeploymentconfig""", alias="RetainDeploymentConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.Endpoint:
        from troposphere.sagemaker import Endpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import Endpoint as TropoT
        return resource_to_troposphere(self, TropoT)


class EndpointConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html
    Properties:
        - Name: ShadowProductionVariants
        - Name: DataCaptureConfig
        - Name: ExecutionRoleArn
        - Name: EnableNetworkIsolation
        - Name: ProductionVariants
        - Name: KmsKeyId
        - Name: AsyncInferenceConfig
        - Name: VpcConfig
        - Name: EndpointConfigName
        - Name: ExplainerConfig
        - Name: Tags
    Attributes:
        - Name: EndpointConfigName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ShadowProductionVariants_: Optional[List['ProductionVariant']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-shadowproductionvariants""", alias="ShadowProductionVariants")
    DataCaptureConfig_: Optional['DataCaptureConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig""", alias="DataCaptureConfig")
    ExecutionRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-executionrolearn""", alias="ExecutionRoleArn")
    EnableNetworkIsolation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-enablenetworkisolation""", alias="EnableNetworkIsolation")
    ProductionVariants_: List['ProductionVariant'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-productionvariants""", alias="ProductionVariants")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-kmskeyid""", alias="KmsKeyId")
    AsyncInferenceConfig_: Optional['AsyncInferenceConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-asyncinferenceconfig""", alias="AsyncInferenceConfig")
    VpcConfig_: Optional['VpcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-vpcconfig""", alias="VpcConfig")
    EndpointConfigName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-endpointconfigname""", alias="EndpointConfigName")
    ExplainerConfig_: Optional['ExplainerConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-explainerconfig""", alias="ExplainerConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.EndpointConfig:
        from troposphere.sagemaker import EndpointConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import EndpointConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class FeatureGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html
    Properties:
        - Name: Description
        - Name: OfflineStoreConfig
        - Name: FeatureDefinitions
        - Name: RecordIdentifierFeatureName
        - Name: EventTimeFeatureName
        - Name: FeatureGroupName
        - Name: OnlineStoreConfig
        - Name: RoleArn
        - Name: Tags
    Attributes:
        - Name: FeatureGroupStatus
        - Name: CreationTime
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-description""", alias="Description")
    OfflineStoreConfig_: Optional['OfflineStoreConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-offlinestoreconfig""", alias="OfflineStoreConfig")
    FeatureDefinitions_: List['FeatureDefinition'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-featuredefinitions""", alias="FeatureDefinitions")
    RecordIdentifierFeatureName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-recordidentifierfeaturename""", alias="RecordIdentifierFeatureName")
    EventTimeFeatureName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-eventtimefeaturename""", alias="EventTimeFeatureName")
    FeatureGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-featuregroupname""", alias="FeatureGroupName")
    OnlineStoreConfig_: Optional['OnlineStoreConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-onlinestoreconfig""", alias="OnlineStoreConfig")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.FeatureGroup:
        from troposphere.sagemaker import FeatureGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import FeatureGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class Image(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html
    Properties:
        - Name: ImageName
        - Name: ImageDisplayName
        - Name: ImageRoleArn
        - Name: ImageDescription
        - Name: Tags
    Attributes:
        - Name: ImageArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ImageName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagename""", alias="ImageName")
    ImageDisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagedisplayname""", alias="ImageDisplayName")
    ImageRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagerolearn""", alias="ImageRoleArn")
    ImageDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagedescription""", alias="ImageDescription")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.Image:
        from troposphere.sagemaker import Image as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import Image as TropoT
        return resource_to_troposphere(self, TropoT)


class ImageVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html
    Properties:
        - Name: ImageName
        - Name: Horovod
        - Name: Processor
        - Name: JobType
        - Name: Alias
        - Name: ProgrammingLang
        - Name: VendorGuidance
        - Name: MLFramework
        - Name: Aliases
        - Name: ReleaseNotes
        - Name: BaseImage
    Attributes:
        - Name: ImageVersionArn
        - Name: Version
        - Name: ContainerImage
        - Name: ImageArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ImageName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-imagename""", alias="ImageName")
    Horovod_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-horovod""", alias="Horovod")
    Processor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-processor""", alias="Processor")
    JobType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-jobtype""", alias="JobType")
    Alias_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-alias""", alias="Alias")
    ProgrammingLang_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-programminglang""", alias="ProgrammingLang")
    VendorGuidance_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-vendorguidance""", alias="VendorGuidance")
    MLFramework_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-mlframework""", alias="MLFramework")
    Aliases_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-aliases""", alias="Aliases")
    ReleaseNotes_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-releasenotes""", alias="ReleaseNotes")
    BaseImage_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-baseimage""", alias="BaseImage")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.ImageVersion:
        from troposphere.sagemaker import ImageVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import ImageVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class InferenceComponent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferencecomponent.html
    Properties:
        - Name: EndpointName
        - Name: VariantName
        - Name: InferenceComponentName
        - Name: Specification
        - Name: RuntimeConfig
        - Name: EndpointArn
        - Name: Tags
    Attributes:
        - Name: Specification.Container.DeployedImage.ResolutionTime
        - Name: FailureReason
        - Name: InferenceComponentStatus
        - Name: CreationTime
        - Name: LastModifiedTime
        - Name: InferenceComponentArn
        - Name: Specification.Container.DeployedImage.ResolvedImage
        - Name: RuntimeConfig.CurrentCopyCount
        - Name: RuntimeConfig.DesiredCopyCount
        - Name: Specification.Container.DeployedImage
        - Name: Specification.Container.DeployedImage.SpecifiedImage
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EndpointName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferencecomponent.html#cfn-sagemaker-inferencecomponent-endpointname""", alias="EndpointName")
    VariantName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferencecomponent.html#cfn-sagemaker-inferencecomponent-variantname""", alias="VariantName")
    InferenceComponentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferencecomponent.html#cfn-sagemaker-inferencecomponent-inferencecomponentname""", alias="InferenceComponentName")
    Specification_: 'InferenceComponentSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferencecomponent.html#cfn-sagemaker-inferencecomponent-specification""", alias="Specification")
    RuntimeConfig_: 'InferenceComponentRuntimeConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferencecomponent.html#cfn-sagemaker-inferencecomponent-runtimeconfig""", alias="RuntimeConfig")
    EndpointArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferencecomponent.html#cfn-sagemaker-inferencecomponent-endpointarn""", alias="EndpointArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferencecomponent.html#cfn-sagemaker-inferencecomponent-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.InferenceComponent:
        from troposphere.sagemaker import InferenceComponent as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import InferenceComponent as TropoT
        return resource_to_troposphere(self, TropoT)


class InferenceExperiment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html
    Properties:
        - Name: DataStorageConfig
        - Name: Description
        - Name: StatusReason
        - Name: ModelVariants
        - Name: ShadowModeConfig
        - Name: RoleArn
        - Name: Name
        - Name: Type
        - Name: EndpointName
        - Name: DesiredState
        - Name: Schedule
        - Name: KmsKey
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: EndpointMetadata.EndpointConfigName
        - Name: CreationTime
        - Name: LastModifiedTime
        - Name: EndpointMetadata.EndpointName
        - Name: Arn
        - Name: EndpointMetadata.EndpointStatus
        - Name: EndpointMetadata
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DataStorageConfig_: Optional['DataStorageConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html#cfn-sagemaker-inferenceexperiment-datastorageconfig""", alias="DataStorageConfig")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html#cfn-sagemaker-inferenceexperiment-description""", alias="Description")
    StatusReason_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html#cfn-sagemaker-inferenceexperiment-statusreason""", alias="StatusReason")
    ModelVariants_: List['ModelVariantConfig'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html#cfn-sagemaker-inferenceexperiment-modelvariants""", alias="ModelVariants")
    ShadowModeConfig_: Optional['ShadowModeConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html#cfn-sagemaker-inferenceexperiment-shadowmodeconfig""", alias="ShadowModeConfig")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html#cfn-sagemaker-inferenceexperiment-rolearn""", alias="RoleArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html#cfn-sagemaker-inferenceexperiment-name""", alias="Name")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html#cfn-sagemaker-inferenceexperiment-type""", alias="Type")
    EndpointName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html#cfn-sagemaker-inferenceexperiment-endpointname""", alias="EndpointName")
    DesiredState_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html#cfn-sagemaker-inferenceexperiment-desiredstate""", alias="DesiredState")
    Schedule_: Optional['InferenceExperimentSchedule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html#cfn-sagemaker-inferenceexperiment-schedule""", alias="Schedule")
    KmsKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html#cfn-sagemaker-inferenceexperiment-kmskey""", alias="KmsKey")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html#cfn-sagemaker-inferenceexperiment-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.InferenceExperiment:
        from troposphere.sagemaker import InferenceExperiment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import InferenceExperiment as TropoT
        return resource_to_troposphere(self, TropoT)


class Model(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html
    Properties:
        - Name: ExecutionRoleArn
        - Name: EnableNetworkIsolation
        - Name: PrimaryContainer
        - Name: ModelName
        - Name: VpcConfig
        - Name: Containers
        - Name: InferenceExecutionConfig
        - Name: Tags
    Attributes:
        - Name: ModelName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ExecutionRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-executionrolearn""", alias="ExecutionRoleArn")
    EnableNetworkIsolation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-enablenetworkisolation""", alias="EnableNetworkIsolation")
    PrimaryContainer_: Optional['ContainerDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-primarycontainer""", alias="PrimaryContainer")
    ModelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-modelname""", alias="ModelName")
    VpcConfig_: Optional['VpcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-vpcconfig""", alias="VpcConfig")
    Containers_: Optional[List['ContainerDefinition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-containers""", alias="Containers")
    InferenceExecutionConfig_: Optional['InferenceExecutionConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-inferenceexecutionconfig""", alias="InferenceExecutionConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.Model:
        from troposphere.sagemaker import Model as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import Model as TropoT
        return resource_to_troposphere(self, TropoT)


class ModelBiasJobDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html
    Properties:
        - Name: ModelBiasJobInput
        - Name: ModelBiasJobOutputConfig
        - Name: EndpointName
        - Name: StoppingCondition
        - Name: JobDefinitionName
        - Name: JobResources
        - Name: NetworkConfig
        - Name: ModelBiasBaselineConfig
        - Name: ModelBiasAppSpecification
        - Name: RoleArn
        - Name: Tags
    Attributes:
        - Name: JobDefinitionArn
        - Name: CreationTime
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ModelBiasJobInput_: 'ModelBiasJobInput' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput""", alias="ModelBiasJobInput")
    ModelBiasJobOutputConfig_: 'MonitoringOutputConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjoboutputconfig""", alias="ModelBiasJobOutputConfig")
    EndpointName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-endpointname""", alias="EndpointName")
    StoppingCondition_: Optional['StoppingCondition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-stoppingcondition""", alias="StoppingCondition")
    JobDefinitionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobdefinitionname""", alias="JobDefinitionName")
    JobResources_: 'MonitoringResources' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobresources""", alias="JobResources")
    NetworkConfig_: Optional['NetworkConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig""", alias="NetworkConfig")
    ModelBiasBaselineConfig_: Optional['ModelBiasBaselineConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig""", alias="ModelBiasBaselineConfig")
    ModelBiasAppSpecification_: 'ModelBiasAppSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification""", alias="ModelBiasAppSpecification")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelBiasJobDefinition:
        from troposphere.sagemaker import ModelBiasJobDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import ModelBiasJobDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class ModelCard(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelcard.html
    Properties:
        - Name: LastModifiedBy
        - Name: ModelCardName
        - Name: ModelCardStatus
        - Name: CreatedBy
        - Name: SecurityConfig
        - Name: Content
        - Name: Tags
    Attributes:
        - Name: LastModifiedBy.UserProfileArn
        - Name: CreatedBy.DomainId
        - Name: ModelCardArn
        - Name: CreatedBy.UserProfileName
        - Name: CreationTime
        - Name: LastModifiedTime
        - Name: LastModifiedBy.DomainId
        - Name: ModelCardVersion
        - Name: ModelCardProcessingStatus
        - Name: LastModifiedBy.UserProfileName
        - Name: CreatedBy.UserProfileArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LastModifiedBy_: Optional['UserContext'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelcard.html#cfn-sagemaker-modelcard-lastmodifiedby""", alias="LastModifiedBy")
    ModelCardName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelcard.html#cfn-sagemaker-modelcard-modelcardname""", alias="ModelCardName")
    ModelCardStatus_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelcard.html#cfn-sagemaker-modelcard-modelcardstatus""", alias="ModelCardStatus")
    CreatedBy_: Optional['UserContext'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelcard.html#cfn-sagemaker-modelcard-createdby""", alias="CreatedBy")
    SecurityConfig_: Optional['SecurityConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelcard.html#cfn-sagemaker-modelcard-securityconfig""", alias="SecurityConfig")
    Content_: 'Content' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelcard.html#cfn-sagemaker-modelcard-content""", alias="Content")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelcard.html#cfn-sagemaker-modelcard-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelCard:
        from troposphere.sagemaker import ModelCard as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import ModelCard as TropoT
        return resource_to_troposphere(self, TropoT)


class ModelExplainabilityJobDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html
    Properties:
        - Name: ModelExplainabilityJobOutputConfig
        - Name: EndpointName
        - Name: StoppingCondition
        - Name: ModelExplainabilityBaselineConfig
        - Name: JobDefinitionName
        - Name: JobResources
        - Name: NetworkConfig
        - Name: RoleArn
        - Name: ModelExplainabilityJobInput
        - Name: Tags
        - Name: ModelExplainabilityAppSpecification
    Attributes:
        - Name: JobDefinitionArn
        - Name: CreationTime
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ModelExplainabilityJobOutputConfig_: 'MonitoringOutputConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjoboutputconfig""", alias="ModelExplainabilityJobOutputConfig")
    EndpointName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointname""", alias="EndpointName")
    StoppingCondition_: Optional['StoppingCondition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition""", alias="StoppingCondition")
    ModelExplainabilityBaselineConfig_: Optional['ModelExplainabilityBaselineConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig""", alias="ModelExplainabilityBaselineConfig")
    JobDefinitionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobdefinitionname""", alias="JobDefinitionName")
    JobResources_: 'MonitoringResources' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobresources""", alias="JobResources")
    NetworkConfig_: Optional['NetworkConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig""", alias="NetworkConfig")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-rolearn""", alias="RoleArn")
    ModelExplainabilityJobInput_: 'ModelExplainabilityJobInput' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput""", alias="ModelExplainabilityJobInput")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-tags""", alias="Tags")
    ModelExplainabilityAppSpecification_: 'ModelExplainabilityAppSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification""", alias="ModelExplainabilityAppSpecification")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelExplainabilityJobDefinition:
        from troposphere.sagemaker import ModelExplainabilityJobDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import ModelExplainabilityJobDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class ModelPackage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html
    Properties:
        - Name: DriftCheckBaselines
        - Name: ModelPackageGroupName
        - Name: ModelMetrics
        - Name: Task
        - Name: CustomerMetadataProperties
        - Name: ApprovalDescription
        - Name: ModelApprovalStatus
        - Name: ModelPackageVersion
        - Name: MetadataProperties
        - Name: ValidationSpecification
        - Name: SourceAlgorithmSpecification
        - Name: ModelPackageStatusDetails
        - Name: SkipModelValidation
        - Name: ModelPackageDescription
        - Name: AdditionalInferenceSpecificationsToAdd
        - Name: ModelPackageName
        - Name: InferenceSpecification
        - Name: SamplePayloadUrl
        - Name: LastModifiedTime
        - Name: ClientToken
        - Name: Domain
        - Name: Tags
        - Name: CertifyForMarketplace
        - Name: AdditionalInferenceSpecifications
    Attributes:
        - Name: ModelPackageStatus
        - Name: CreationTime
        - Name: ModelPackageArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DriftCheckBaselines_: Optional['DriftCheckBaselines'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-driftcheckbaselines""", alias="DriftCheckBaselines")
    ModelPackageGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-modelpackagegroupname""", alias="ModelPackageGroupName")
    ModelMetrics_: Optional['ModelMetrics'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-modelmetrics""", alias="ModelMetrics")
    Task_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-task""", alias="Task")
    CustomerMetadataProperties_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-customermetadataproperties""", alias="CustomerMetadataProperties")
    ApprovalDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-approvaldescription""", alias="ApprovalDescription")
    ModelApprovalStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-modelapprovalstatus""", alias="ModelApprovalStatus")
    ModelPackageVersion_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-modelpackageversion""", alias="ModelPackageVersion")
    MetadataProperties_: Optional['MetadataProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-metadataproperties""", alias="MetadataProperties")
    ValidationSpecification_: Optional['ValidationSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-validationspecification""", alias="ValidationSpecification")
    SourceAlgorithmSpecification_: Optional['SourceAlgorithmSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-sourcealgorithmspecification""", alias="SourceAlgorithmSpecification")
    ModelPackageStatusDetails_: Optional['ModelPackageStatusDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-modelpackagestatusdetails""", alias="ModelPackageStatusDetails")
    SkipModelValidation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-skipmodelvalidation""", alias="SkipModelValidation")
    ModelPackageDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-modelpackagedescription""", alias="ModelPackageDescription")
    AdditionalInferenceSpecificationsToAdd_: Optional[List['AdditionalInferenceSpecificationDefinition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-additionalinferencespecificationstoadd""", alias="AdditionalInferenceSpecificationsToAdd")
    ModelPackageName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-modelpackagename""", alias="ModelPackageName")
    InferenceSpecification_: Optional['InferenceSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-inferencespecification""", alias="InferenceSpecification")
    SamplePayloadUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-samplepayloadurl""", alias="SamplePayloadUrl")
    LastModifiedTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-lastmodifiedtime""", alias="LastModifiedTime")
    ClientToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-clienttoken""", alias="ClientToken")
    Domain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-domain""", alias="Domain")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-tags""", alias="Tags")
    CertifyForMarketplace_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-certifyformarketplace""", alias="CertifyForMarketplace")
    AdditionalInferenceSpecifications_: Optional[List['AdditionalInferenceSpecificationDefinition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html#cfn-sagemaker-modelpackage-additionalinferencespecifications""", alias="AdditionalInferenceSpecifications")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelPackage:
        from troposphere.sagemaker import ModelPackage as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import ModelPackage as TropoT
        return resource_to_troposphere(self, TropoT)


class ModelPackageGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html
    Properties:
        - Name: ModelPackageGroupName
        - Name: ModelPackageGroupDescription
        - Name: ModelPackageGroupPolicy
        - Name: Tags
    Attributes:
        - Name: ModelPackageGroupArn
        - Name: CreationTime
        - Name: ModelPackageGroupStatus
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ModelPackageGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupname""", alias="ModelPackageGroupName")
    ModelPackageGroupDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupdescription""", alias="ModelPackageGroupDescription")
    ModelPackageGroupPolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegrouppolicy""", alias="ModelPackageGroupPolicy")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelPackageGroup:
        from troposphere.sagemaker import ModelPackageGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import ModelPackageGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class ModelQualityJobDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html
    Properties:
        - Name: ModelQualityAppSpecification
        - Name: EndpointName
        - Name: StoppingCondition
        - Name: ModelQualityBaselineConfig
        - Name: JobDefinitionName
        - Name: ModelQualityJobInput
        - Name: JobResources
        - Name: NetworkConfig
        - Name: ModelQualityJobOutputConfig
        - Name: RoleArn
        - Name: Tags
    Attributes:
        - Name: JobDefinitionArn
        - Name: CreationTime
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ModelQualityAppSpecification_: 'ModelQualityAppSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification""", alias="ModelQualityAppSpecification")
    EndpointName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-endpointname""", alias="EndpointName")
    StoppingCondition_: Optional['StoppingCondition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-stoppingcondition""", alias="StoppingCondition")
    ModelQualityBaselineConfig_: Optional['ModelQualityBaselineConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig""", alias="ModelQualityBaselineConfig")
    JobDefinitionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobdefinitionname""", alias="JobDefinitionName")
    ModelQualityJobInput_: 'ModelQualityJobInput' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput""", alias="ModelQualityJobInput")
    JobResources_: 'MonitoringResources' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobresources""", alias="JobResources")
    NetworkConfig_: Optional['NetworkConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig""", alias="NetworkConfig")
    ModelQualityJobOutputConfig_: 'MonitoringOutputConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjoboutputconfig""", alias="ModelQualityJobOutputConfig")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.ModelQualityJobDefinition:
        from troposphere.sagemaker import ModelQualityJobDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import ModelQualityJobDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class MonitoringSchedule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html
    Properties:
        - Name: MonitoringScheduleStatus
        - Name: MonitoringScheduleConfig
        - Name: MonitoringScheduleName
        - Name: EndpointName
        - Name: FailureReason
        - Name: LastMonitoringExecutionSummary
        - Name: Tags
    Attributes:
        - Name: MonitoringScheduleArn
        - Name: CreationTime
        - Name: LastModifiedTime
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MonitoringScheduleStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulestatus""", alias="MonitoringScheduleStatus")
    MonitoringScheduleConfig_: 'MonitoringScheduleConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig""", alias="MonitoringScheduleConfig")
    MonitoringScheduleName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulename""", alias="MonitoringScheduleName")
    EndpointName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-endpointname""", alias="EndpointName")
    FailureReason_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-failurereason""", alias="FailureReason")
    LastMonitoringExecutionSummary_: Optional['MonitoringExecutionSummary'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-lastmonitoringexecutionsummary""", alias="LastMonitoringExecutionSummary")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.MonitoringSchedule:
        from troposphere.sagemaker import MonitoringSchedule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import MonitoringSchedule as TropoT
        return resource_to_troposphere(self, TropoT)


class NotebookInstance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html
    Properties:
        - Name: KmsKeyId
        - Name: VolumeSizeInGB
        - Name: AdditionalCodeRepositories
        - Name: DefaultCodeRepository
        - Name: DirectInternetAccess
        - Name: PlatformIdentifier
        - Name: AcceleratorTypes
        - Name: SubnetId
        - Name: SecurityGroupIds
        - Name: RoleArn
        - Name: InstanceMetadataServiceConfiguration
        - Name: RootAccess
        - Name: NotebookInstanceName
        - Name: InstanceType
        - Name: LifecycleConfigName
        - Name: Tags
    Attributes:
        - Name: NotebookInstanceName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-kmskeyid""", alias="KmsKeyId")
    VolumeSizeInGB_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-volumesizeingb""", alias="VolumeSizeInGB")
    AdditionalCodeRepositories_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-additionalcoderepositories""", alias="AdditionalCodeRepositories")
    DefaultCodeRepository_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-defaultcoderepository""", alias="DefaultCodeRepository")
    DirectInternetAccess_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-directinternetaccess""", alias="DirectInternetAccess")
    PlatformIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-platformidentifier""", alias="PlatformIdentifier")
    AcceleratorTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-acceleratortypes""", alias="AcceleratorTypes")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-subnetid""", alias="SubnetId")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-securitygroupids""", alias="SecurityGroupIds")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rolearn""", alias="RoleArn")
    InstanceMetadataServiceConfiguration_: Optional['InstanceMetadataServiceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-instancemetadataserviceconfiguration""", alias="InstanceMetadataServiceConfiguration")
    RootAccess_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rootaccess""", alias="RootAccess")
    NotebookInstanceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-notebookinstancename""", alias="NotebookInstanceName")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-instancetype""", alias="InstanceType")
    LifecycleConfigName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-lifecycleconfigname""", alias="LifecycleConfigName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.NotebookInstance:
        from troposphere.sagemaker import NotebookInstance as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import NotebookInstance as TropoT
        return resource_to_troposphere(self, TropoT)


class NotebookInstanceLifecycleConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html
    Properties:
        - Name: OnStart
        - Name: NotebookInstanceLifecycleConfigName
        - Name: OnCreate
    Attributes:
        - Name: NotebookInstanceLifecycleConfigName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OnStart_: Optional[List['NotebookInstanceLifecycleHook']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-onstart""", alias="OnStart")
    NotebookInstanceLifecycleConfigName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecycleconfigname""", alias="NotebookInstanceLifecycleConfigName")
    OnCreate_: Optional[List['NotebookInstanceLifecycleHook']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-oncreate""", alias="OnCreate")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.NotebookInstanceLifecycleConfig:
        from troposphere.sagemaker import NotebookInstanceLifecycleConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import NotebookInstanceLifecycleConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class Pipeline(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html
    Properties:
        - Name: PipelineName
        - Name: ParallelismConfiguration
        - Name: PipelineDescription
        - Name: PipelineDisplayName
        - Name: PipelineDefinition
        - Name: RoleArn
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PipelineName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinename""", alias="PipelineName")
    ParallelismConfiguration_: Optional['ParallelismConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-parallelismconfiguration""", alias="ParallelismConfiguration")
    PipelineDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedescription""", alias="PipelineDescription")
    PipelineDisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedisplayname""", alias="PipelineDisplayName")
    PipelineDefinition_: 'PipelineDefinition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedefinition""", alias="PipelineDefinition")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.Pipeline:
        from troposphere.sagemaker import Pipeline as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import Pipeline as TropoT
        return resource_to_troposphere(self, TropoT)


class Project(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html
    Properties:
        - Name: ProjectName
        - Name: ServiceCatalogProvisionedProductDetails
        - Name: ServiceCatalogProvisioningDetails
        - Name: ProjectDescription
        - Name: Tags
    Attributes:
        - Name: ProjectArn
        - Name: ProjectStatus
        - Name: ProjectId
        - Name: CreationTime
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ProjectName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectname""", alias="ProjectName")
    ServiceCatalogProvisionedProductDetails_: Optional['ServiceCatalogProvisionedProductDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-servicecatalogprovisionedproductdetails""", alias="ServiceCatalogProvisionedProductDetails")
    ServiceCatalogProvisioningDetails_: 'ServiceCatalogProvisioningDetails' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-servicecatalogprovisioningdetails""", alias="ServiceCatalogProvisioningDetails")
    ProjectDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectdescription""", alias="ProjectDescription")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.Project:
        from troposphere.sagemaker import Project as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import Project as TropoT
        return resource_to_troposphere(self, TropoT)


class Space(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-space.html
    Properties:
        - Name: DomainId
        - Name: SpaceName
        - Name: SpaceSettings
        - Name: Tags
    Attributes:
        - Name: SpaceArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DomainId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-space.html#cfn-sagemaker-space-domainid""", alias="DomainId")
    SpaceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-space.html#cfn-sagemaker-space-spacename""", alias="SpaceName")
    SpaceSettings_: Optional['SpaceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-space.html#cfn-sagemaker-space-spacesettings""", alias="SpaceSettings")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-space.html#cfn-sagemaker-space-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.Space:
        from troposphere.sagemaker import Space as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import Space as TropoT
        return resource_to_troposphere(self, TropoT)


class UserProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html
    Properties:
        - Name: DomainId
        - Name: SingleSignOnUserValue
        - Name: UserSettings
        - Name: SingleSignOnUserIdentifier
        - Name: UserProfileName
        - Name: Tags
    Attributes:
        - Name: UserProfileArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DomainId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-domainid""", alias="DomainId")
    SingleSignOnUserValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-singlesignonuservalue""", alias="SingleSignOnUserValue")
    UserSettings_: Optional['UserSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-usersettings""", alias="UserSettings")
    SingleSignOnUserIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-singlesignonuseridentifier""", alias="SingleSignOnUserIdentifier")
    UserProfileName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-userprofilename""", alias="UserProfileName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.UserProfile:
        from troposphere.sagemaker import UserProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import UserProfile as TropoT
        return resource_to_troposphere(self, TropoT)


class Workteam(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html
    Properties:
        - Name: Description
        - Name: NotificationConfiguration
        - Name: WorkteamName
        - Name: MemberDefinitions
        - Name: WorkforceName
        - Name: Tags
    Attributes:
        - Name: WorkteamName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-description""", alias="Description")
    NotificationConfiguration_: Optional['NotificationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-notificationconfiguration""", alias="NotificationConfiguration")
    WorkteamName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-workteamname""", alias="WorkteamName")
    MemberDefinitions_: Optional[List['MemberDefinition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-memberdefinitions""", alias="MemberDefinitions")
    WorkforceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-workforcename""", alias="WorkforceName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sagemaker.Workteam:
        from troposphere.sagemaker import Workteam as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sagemaker import Workteam as TropoT
        return resource_to_troposphere(self, TropoT)

