from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AliasRoutingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-aliasroutingconfiguration.html
    Properties:
        - Name: AdditionalVersionWeights
    
    """
    
    AdditionalVersionWeights_: List['VersionWeight'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-aliasroutingconfiguration.html#cfn-lambda-alias-aliasroutingconfiguration-additionalversionweights""", alias="AdditionalVersionWeights")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.AliasRoutingConfiguration:
        from troposphere.awslambda import AliasRoutingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProvisionedConcurrencyConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-provisionedconcurrencyconfiguration.html
    Properties:
        - Name: ProvisionedConcurrentExecutions
    
    """
    
    ProvisionedConcurrentExecutions_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-provisionedconcurrencyconfiguration.html#cfn-lambda-alias-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions""", alias="ProvisionedConcurrentExecutions")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.ProvisionedConcurrencyConfiguration:
        from troposphere.awslambda import ProvisionedConcurrencyConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VersionWeight(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-versionweight.html
    Properties:
        - Name: FunctionVersion
        - Name: FunctionWeight
    
    """
    
    FunctionVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-versionweight.html#cfn-lambda-alias-versionweight-functionversion""", alias="FunctionVersion")
    FunctionWeight_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-versionweight.html#cfn-lambda-alias-versionweight-functionweight""", alias="FunctionWeight")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.VersionWeight:
        from troposphere.awslambda import VersionWeight as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AllowedPublishers(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-allowedpublishers.html
    Properties:
        - Name: SigningProfileVersionArns
    
    """
    
    SigningProfileVersionArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-allowedpublishers.html#cfn-lambda-codesigningconfig-allowedpublishers-signingprofileversionarns""", alias="SigningProfileVersionArns")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.AllowedPublishers:
        from troposphere.awslambda import AllowedPublishers as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CodeSigningPolicies(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-codesigningpolicies.html
    Properties:
        - Name: UntrustedArtifactOnDeployment
    
    """
    
    UntrustedArtifactOnDeployment_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-codesigningpolicies.html#cfn-lambda-codesigningconfig-codesigningpolicies-untrustedartifactondeployment""", alias="UntrustedArtifactOnDeployment")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.CodeSigningPolicies:
        from troposphere.awslambda import CodeSigningPolicies as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DestinationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html
    Properties:
        - Name: OnSuccess
        - Name: OnFailure
    
    """
    
    OnSuccess_: Optional['OnSuccess'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html#cfn-lambda-eventinvokeconfig-destinationconfig-onsuccess""", alias="OnSuccess")
    OnFailure_: Optional['OnFailure'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html#cfn-lambda-eventinvokeconfig-destinationconfig-onfailure""", alias="OnFailure")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.DestinationConfig:
        from troposphere.awslambda import DestinationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnFailure(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onfailure.html
    Properties:
        - Name: Destination
    
    """
    
    Destination_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onfailure.html#cfn-lambda-eventinvokeconfig-destinationconfig-onfailure-destination""", alias="Destination")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.OnFailure:
        from troposphere.awslambda import OnFailure as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnSuccess(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onsuccess.html
    Properties:
        - Name: Destination
    
    """
    
    Destination_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onsuccess.html#cfn-lambda-eventinvokeconfig-destinationconfig-onsuccess-destination""", alias="Destination")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.OnSuccess:
        from troposphere.awslambda import OnSuccess as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AmazonManagedKafkaEventSourceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig.html
    Properties:
        - Name: ConsumerGroupId
    
    """
    
    ConsumerGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig.html#cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig-consumergroupid""", alias="ConsumerGroupId")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.AmazonManagedKafkaEventSourceConfig:
        from troposphere.awslambda import AmazonManagedKafkaEventSourceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DestinationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-destinationconfig.html
    Properties:
        - Name: OnFailure
    
    """
    
    OnFailure_: Optional['OnFailure'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-destinationconfig.html#cfn-lambda-eventsourcemapping-destinationconfig-onfailure""", alias="OnFailure")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.DestinationConfig:
        from troposphere.awslambda import DestinationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DocumentDBEventSourceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-documentdbeventsourceconfig.html
    Properties:
        - Name: FullDocument
        - Name: CollectionName
        - Name: DatabaseName
    
    """
    
    FullDocument_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-documentdbeventsourceconfig.html#cfn-lambda-eventsourcemapping-documentdbeventsourceconfig-fulldocument""", alias="FullDocument")
    CollectionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-documentdbeventsourceconfig.html#cfn-lambda-eventsourcemapping-documentdbeventsourceconfig-collectionname""", alias="CollectionName")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-documentdbeventsourceconfig.html#cfn-lambda-eventsourcemapping-documentdbeventsourceconfig-databasename""", alias="DatabaseName")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.DocumentDBEventSourceConfig:
        from troposphere.awslambda import DocumentDBEventSourceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Endpoints(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-endpoints.html
    Properties:
        - Name: KafkaBootstrapServers
    
    """
    
    KafkaBootstrapServers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-endpoints.html#cfn-lambda-eventsourcemapping-endpoints-kafkabootstrapservers""", alias="KafkaBootstrapServers")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.Endpoints:
        from troposphere.awslambda import Endpoints as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Filter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filter.html
    Properties:
        - Name: Pattern
    
    """
    
    Pattern_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filter.html#cfn-lambda-eventsourcemapping-filter-pattern""", alias="Pattern")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.Filter:
        from troposphere.awslambda import Filter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FilterCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html
    Properties:
        - Name: Filters
    
    """
    
    Filters_: Optional[List['Filter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html#cfn-lambda-eventsourcemapping-filtercriteria-filters""", alias="Filters")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.FilterCriteria:
        from troposphere.awslambda import FilterCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnFailure(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-onfailure.html
    Properties:
        - Name: Destination
    
    """
    
    Destination_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-onfailure.html#cfn-lambda-eventsourcemapping-onfailure-destination""", alias="Destination")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.OnFailure:
        from troposphere.awslambda import OnFailure as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScalingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-scalingconfig.html
    Properties:
        - Name: MaximumConcurrency
    
    """
    
    MaximumConcurrency_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-scalingconfig.html#cfn-lambda-eventsourcemapping-scalingconfig-maximumconcurrency""", alias="MaximumConcurrency")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.ScalingConfig:
        from troposphere.awslambda import ScalingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SelfManagedEventSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedeventsource.html
    Properties:
        - Name: Endpoints
    
    """
    
    Endpoints_: Optional['Endpoints'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedeventsource.html#cfn-lambda-eventsourcemapping-selfmanagedeventsource-endpoints""", alias="Endpoints")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.SelfManagedEventSource:
        from troposphere.awslambda import SelfManagedEventSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SelfManagedKafkaEventSourceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig.html
    Properties:
        - Name: ConsumerGroupId
    
    """
    
    ConsumerGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig.html#cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig-consumergroupid""", alias="ConsumerGroupId")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.SelfManagedKafkaEventSourceConfig:
        from troposphere.awslambda import SelfManagedKafkaEventSourceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceAccessConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.html
    Properties:
        - Name: Type
        - Name: URI
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.html#cfn-lambda-eventsourcemapping-sourceaccessconfiguration-type""", alias="Type")
    URI_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.html#cfn-lambda-eventsourcemapping-sourceaccessconfiguration-uri""", alias="URI")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.SourceAccessConfiguration:
        from troposphere.awslambda import SourceAccessConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Code(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html
    Properties:
        - Name: S3ObjectVersion
        - Name: S3Bucket
        - Name: ZipFile
        - Name: S3Key
        - Name: ImageUri
    
    """
    
    S3ObjectVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3objectversion""", alias="S3ObjectVersion")
    S3Bucket_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3bucket""", alias="S3Bucket")
    ZipFile_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-zipfile""", alias="ZipFile")
    S3Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3key""", alias="S3Key")
    ImageUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-imageuri""", alias="ImageUri")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.Code:
        from troposphere.awslambda import Code as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeadLetterConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-deadletterconfig.html
    Properties:
        - Name: TargetArn
    
    """
    
    TargetArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-deadletterconfig.html#cfn-lambda-function-deadletterconfig-targetarn""", alias="TargetArn")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.DeadLetterConfig:
        from troposphere.awslambda import DeadLetterConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Environment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-environment.html
    Properties:
        - Name: Variables
    
    """
    
    Variables_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-environment.html#cfn-lambda-function-environment-variables""", alias="Variables")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.Environment:
        from troposphere.awslambda import Environment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EphemeralStorage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-ephemeralstorage.html
    Properties:
        - Name: Size
    
    """
    
    Size_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-ephemeralstorage.html#cfn-lambda-function-ephemeralstorage-size""", alias="Size")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.EphemeralStorage:
        from troposphere.awslambda import EphemeralStorage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FileSystemConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.html
    Properties:
        - Name: Arn
        - Name: LocalMountPath
    
    """
    
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.html#cfn-lambda-function-filesystemconfig-arn""", alias="Arn")
    LocalMountPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.html#cfn-lambda-function-filesystemconfig-localmountpath""", alias="LocalMountPath")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.FileSystemConfig:
        from troposphere.awslambda import FileSystemConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImageConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html
    Properties:
        - Name: WorkingDirectory
        - Name: Command
        - Name: EntryPoint
    
    """
    
    WorkingDirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html#cfn-lambda-function-imageconfig-workingdirectory""", alias="WorkingDirectory")
    Command_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html#cfn-lambda-function-imageconfig-command""", alias="Command")
    EntryPoint_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html#cfn-lambda-function-imageconfig-entrypoint""", alias="EntryPoint")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.ImageConfig:
        from troposphere.awslambda import ImageConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuntimeManagementConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-runtimemanagementconfig.html
    Properties:
        - Name: UpdateRuntimeOn
        - Name: RuntimeVersionArn
    
    """
    
    UpdateRuntimeOn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-runtimemanagementconfig.html#cfn-lambda-function-runtimemanagementconfig-updateruntimeon""", alias="UpdateRuntimeOn")
    RuntimeVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-runtimemanagementconfig.html#cfn-lambda-function-runtimemanagementconfig-runtimeversionarn""", alias="RuntimeVersionArn")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.RuntimeManagementConfig:
        from troposphere.awslambda import RuntimeManagementConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnapStart(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstart.html
    Properties:
        - Name: ApplyOn
    
    """
    
    ApplyOn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstart.html#cfn-lambda-function-snapstart-applyon""", alias="ApplyOn")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.SnapStart:
        from troposphere.awslambda import SnapStart as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnapStartResponse(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstartresponse.html
    Properties:
        - Name: OptimizationStatus
        - Name: ApplyOn
    
    """
    
    OptimizationStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstartresponse.html#cfn-lambda-function-snapstartresponse-optimizationstatus""", alias="OptimizationStatus")
    ApplyOn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstartresponse.html#cfn-lambda-function-snapstartresponse-applyon""", alias="ApplyOn")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.SnapStartResponse:
        from troposphere.awslambda import SnapStartResponse as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TracingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-tracingconfig.html
    Properties:
        - Name: Mode
    
    """
    
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-tracingconfig.html#cfn-lambda-function-tracingconfig-mode""", alias="Mode")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.TracingConfig:
        from troposphere.awslambda import TracingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VPCConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html
    Properties:
        - Name: Ipv6AllowedForDualStack
        - Name: SecurityGroupIds
        - Name: SubnetIds
    
    """
    
    Ipv6AllowedForDualStack_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html#cfn-lambda-function-vpcconfig-ipv6allowedfordualstack""", alias="Ipv6AllowedForDualStack")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html#cfn-lambda-function-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html#cfn-lambda-function-vpcconfig-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.VPCConfig:
        from troposphere.awslambda import VPCConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Content(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html
    Properties:
        - Name: S3ObjectVersion
        - Name: S3Bucket
        - Name: S3Key
    
    """
    
    S3ObjectVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3objectversion""", alias="S3ObjectVersion")
    S3Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3bucket""", alias="S3Bucket")
    S3Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3key""", alias="S3Key")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.Content:
        from troposphere.awslambda import Content as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Cors(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html
    Properties:
        - Name: AllowCredentials
        - Name: AllowOrigins
        - Name: ExposeHeaders
        - Name: AllowHeaders
        - Name: MaxAge
        - Name: AllowMethods
    
    """
    
    AllowCredentials_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-allowcredentials""", alias="AllowCredentials")
    AllowOrigins_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-alloworigins""", alias="AllowOrigins")
    ExposeHeaders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-exposeheaders""", alias="ExposeHeaders")
    AllowHeaders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-allowheaders""", alias="AllowHeaders")
    MaxAge_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-maxage""", alias="MaxAge")
    AllowMethods_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-allowmethods""", alias="AllowMethods")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.Cors:
        from troposphere.awslambda import Cors as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProvisionedConcurrencyConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-provisionedconcurrencyconfiguration.html
    Properties:
        - Name: ProvisionedConcurrentExecutions
    
    """
    
    ProvisionedConcurrentExecutions_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-provisionedconcurrencyconfiguration.html#cfn-lambda-version-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions""", alias="ProvisionedConcurrentExecutions")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.ProvisionedConcurrencyConfiguration:
        from troposphere.awslambda import ProvisionedConcurrencyConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuntimePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-runtimepolicy.html
    Properties:
        - Name: UpdateRuntimeOn
        - Name: RuntimeVersionArn
    
    """
    
    UpdateRuntimeOn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-runtimepolicy.html#cfn-lambda-version-runtimepolicy-updateruntimeon""", alias="UpdateRuntimeOn")
    RuntimeVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-runtimepolicy.html#cfn-lambda-version-runtimepolicy-runtimeversionarn""", alias="RuntimeVersionArn")
    


    @property
    def tropo_type(self) -> troposphere.awslambda.RuntimePolicy:
        from troposphere.awslambda import RuntimePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Alias(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html
    Properties:
        - Name: Description
        - Name: FunctionName
        - Name: FunctionVersion
        - Name: Name
        - Name: ProvisionedConcurrencyConfig
        - Name: RoutingConfig
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-description""", alias="Description")
    FunctionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-functionname""", alias="FunctionName")
    FunctionVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-functionversion""", alias="FunctionVersion")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-name""", alias="Name")
    ProvisionedConcurrencyConfig_: Optional['ProvisionedConcurrencyConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-provisionedconcurrencyconfig""", alias="ProvisionedConcurrencyConfig")
    RoutingConfig_: Optional['AliasRoutingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-routingconfig""", alias="RoutingConfig")
    

    @property
    def tropo_type(self) -> troposphere.awslambda.Alias:
        from troposphere.awslambda import Alias as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.awslambda import Alias as TropoT
        return resource_to_troposphere(self, TropoT)


class CodeSigningConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html
    Properties:
        - Name: Description
        - Name: AllowedPublishers
        - Name: CodeSigningPolicies
    Attributes:
        - Name: CodeSigningConfigId
        - Name: CodeSigningConfigArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-description""", alias="Description")
    AllowedPublishers_: 'AllowedPublishers' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-allowedpublishers""", alias="AllowedPublishers")
    CodeSigningPolicies_: Optional['CodeSigningPolicies'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-codesigningpolicies""", alias="CodeSigningPolicies")
    

    @property
    def tropo_type(self) -> troposphere.awslambda.CodeSigningConfig:
        from troposphere.awslambda import CodeSigningConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.awslambda import CodeSigningConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class EventInvokeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html
    Properties:
        - Name: FunctionName
        - Name: MaximumRetryAttempts
        - Name: DestinationConfig
        - Name: Qualifier
        - Name: MaximumEventAgeInSeconds
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FunctionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-functionname""", alias="FunctionName")
    MaximumRetryAttempts_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-maximumretryattempts""", alias="MaximumRetryAttempts")
    DestinationConfig_: Optional['DestinationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-destinationconfig""", alias="DestinationConfig")
    Qualifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-qualifier""", alias="Qualifier")
    MaximumEventAgeInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-maximumeventageinseconds""", alias="MaximumEventAgeInSeconds")
    

    @property
    def tropo_type(self) -> troposphere.awslambda.EventInvokeConfig:
        from troposphere.awslambda import EventInvokeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.awslambda import EventInvokeConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class EventSourceMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html
    Properties:
        - Name: StartingPosition
        - Name: BatchSize
        - Name: MaximumRetryAttempts
        - Name: Topics
        - Name: ScalingConfig
        - Name: SelfManagedEventSource
        - Name: ParallelizationFactor
        - Name: Enabled
        - Name: FilterCriteria
        - Name: EventSourceArn
        - Name: SelfManagedKafkaEventSourceConfig
        - Name: DocumentDBEventSourceConfig
        - Name: FunctionName
        - Name: TumblingWindowInSeconds
        - Name: BisectBatchOnFunctionError
        - Name: DestinationConfig
        - Name: AmazonManagedKafkaEventSourceConfig
        - Name: MaximumRecordAgeInSeconds
        - Name: StartingPositionTimestamp
        - Name: Queues
        - Name: SourceAccessConfigurations
        - Name: FunctionResponseTypes
        - Name: MaximumBatchingWindowInSeconds
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StartingPosition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingposition""", alias="StartingPosition")
    BatchSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-batchsize""", alias="BatchSize")
    MaximumRetryAttempts_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumretryattempts""", alias="MaximumRetryAttempts")
    Topics_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-topics""", alias="Topics")
    ScalingConfig_: Optional['ScalingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-scalingconfig""", alias="ScalingConfig")
    SelfManagedEventSource_: Optional['SelfManagedEventSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-selfmanagedeventsource""", alias="SelfManagedEventSource")
    ParallelizationFactor_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-parallelizationfactor""", alias="ParallelizationFactor")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-enabled""", alias="Enabled")
    FilterCriteria_: Optional['FilterCriteria'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-filtercriteria""", alias="FilterCriteria")
    EventSourceArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-eventsourcearn""", alias="EventSourceArn")
    SelfManagedKafkaEventSourceConfig_: Optional['SelfManagedKafkaEventSourceConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig""", alias="SelfManagedKafkaEventSourceConfig")
    DocumentDBEventSourceConfig_: Optional['DocumentDBEventSourceConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-documentdbeventsourceconfig""", alias="DocumentDBEventSourceConfig")
    FunctionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionname""", alias="FunctionName")
    TumblingWindowInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-tumblingwindowinseconds""", alias="TumblingWindowInSeconds")
    BisectBatchOnFunctionError_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror""", alias="BisectBatchOnFunctionError")
    DestinationConfig_: Optional['DestinationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-destinationconfig""", alias="DestinationConfig")
    AmazonManagedKafkaEventSourceConfig_: Optional['AmazonManagedKafkaEventSourceConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig""", alias="AmazonManagedKafkaEventSourceConfig")
    MaximumRecordAgeInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumrecordageinseconds""", alias="MaximumRecordAgeInSeconds")
    StartingPositionTimestamp_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingpositiontimestamp""", alias="StartingPositionTimestamp")
    Queues_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-queues""", alias="Queues")
    SourceAccessConfigurations_: Optional[List['SourceAccessConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-sourceaccessconfigurations""", alias="SourceAccessConfigurations")
    FunctionResponseTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionresponsetypes""", alias="FunctionResponseTypes")
    MaximumBatchingWindowInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds""", alias="MaximumBatchingWindowInSeconds")
    

    @property
    def tropo_type(self) -> troposphere.awslambda.EventSourceMapping:
        from troposphere.awslambda import EventSourceMapping as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.awslambda import EventSourceMapping as TropoT
        return resource_to_troposphere(self, TropoT)


class Function(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html
    Properties:
        - Name: Policy
        - Name: Description
        - Name: TracingConfig
        - Name: VpcConfig
        - Name: RuntimeManagementConfig
        - Name: ReservedConcurrentExecutions
        - Name: SnapStart
        - Name: FileSystemConfigs
        - Name: FunctionName
        - Name: Runtime
        - Name: KmsKeyArn
        - Name: PackageType
        - Name: CodeSigningConfigArn
        - Name: Layers
        - Name: Tags
        - Name: ImageConfig
        - Name: MemorySize
        - Name: DeadLetterConfig
        - Name: Timeout
        - Name: Handler
        - Name: Code
        - Name: Role
        - Name: Environment
        - Name: EphemeralStorage
        - Name: Architectures
    Attributes:
        - Name: SnapStartResponse.OptimizationStatus
        - Name: SnapStartResponse.ApplyOn
        - Name: SnapStartResponse
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-policy""", alias="Policy")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-description""", alias="Description")
    TracingConfig_: Optional['TracingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-tracingconfig""", alias="TracingConfig")
    VpcConfig_: Optional['VPCConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-vpcconfig""", alias="VpcConfig")
    RuntimeManagementConfig_: Optional['RuntimeManagementConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-runtimemanagementconfig""", alias="RuntimeManagementConfig")
    ReservedConcurrentExecutions_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-reservedconcurrentexecutions""", alias="ReservedConcurrentExecutions")
    SnapStart_: Optional['SnapStart'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-snapstart""", alias="SnapStart")
    FileSystemConfigs_: Optional[List['FileSystemConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-filesystemconfigs""", alias="FileSystemConfigs")
    FunctionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-functionname""", alias="FunctionName")
    Runtime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-runtime""", alias="Runtime")
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-kmskeyarn""", alias="KmsKeyArn")
    PackageType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-packagetype""", alias="PackageType")
    CodeSigningConfigArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-codesigningconfigarn""", alias="CodeSigningConfigArn")
    Layers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-layers""", alias="Layers")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-tags""", alias="Tags")
    ImageConfig_: Optional['ImageConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-imageconfig""", alias="ImageConfig")
    MemorySize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-memorysize""", alias="MemorySize")
    DeadLetterConfig_: Optional['DeadLetterConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-deadletterconfig""", alias="DeadLetterConfig")
    Timeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-timeout""", alias="Timeout")
    Handler_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-handler""", alias="Handler")
    Code_: 'Code' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-code""", alias="Code")
    Role_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-role""", alias="Role")
    Environment_: Optional['Environment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-environment""", alias="Environment")
    EphemeralStorage_: Optional['EphemeralStorage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-ephemeralstorage""", alias="EphemeralStorage")
    Architectures_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-architectures""", alias="Architectures")
    

    @property
    def tropo_type(self) -> troposphere.awslambda.Function:
        from troposphere.awslambda import Function as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.awslambda import Function as TropoT
        return resource_to_troposphere(self, TropoT)


class LayerVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html
    Properties:
        - Name: CompatibleRuntimes
        - Name: LicenseInfo
        - Name: Description
        - Name: LayerName
        - Name: Content
        - Name: CompatibleArchitectures
    Attributes:
        - Name: LayerVersionArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CompatibleRuntimes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-compatibleruntimes""", alias="CompatibleRuntimes")
    LicenseInfo_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-licenseinfo""", alias="LicenseInfo")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-description""", alias="Description")
    LayerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-layername""", alias="LayerName")
    Content_: 'Content' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-content""", alias="Content")
    CompatibleArchitectures_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-compatiblearchitectures""", alias="CompatibleArchitectures")
    

    @property
    def tropo_type(self) -> troposphere.awslambda.LayerVersion:
        from troposphere.awslambda import LayerVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.awslambda import LayerVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class LayerVersionPermission(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html
    Properties:
        - Name: Action
        - Name: LayerVersionArn
        - Name: OrganizationId
        - Name: Principal
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-action""", alias="Action")
    LayerVersionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-layerversionarn""", alias="LayerVersionArn")
    OrganizationId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-organizationid""", alias="OrganizationId")
    Principal_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-principal""", alias="Principal")
    

    @property
    def tropo_type(self) -> troposphere.awslambda.LayerVersionPermission:
        from troposphere.awslambda import LayerVersionPermission as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.awslambda import LayerVersionPermission as TropoT
        return resource_to_troposphere(self, TropoT)


class Permission(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html
    Properties:
        - Name: FunctionName
        - Name: Action
        - Name: EventSourceToken
        - Name: FunctionUrlAuthType
        - Name: SourceArn
        - Name: SourceAccount
        - Name: PrincipalOrgID
        - Name: Principal
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FunctionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-functionname""", alias="FunctionName")
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-action""", alias="Action")
    EventSourceToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-eventsourcetoken""", alias="EventSourceToken")
    FunctionUrlAuthType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-functionurlauthtype""", alias="FunctionUrlAuthType")
    SourceArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-sourcearn""", alias="SourceArn")
    SourceAccount_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-sourceaccount""", alias="SourceAccount")
    PrincipalOrgID_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-principalorgid""", alias="PrincipalOrgID")
    Principal_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-principal""", alias="Principal")
    

    @property
    def tropo_type(self) -> troposphere.awslambda.Permission:
        from troposphere.awslambda import Permission as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.awslambda import Permission as TropoT
        return resource_to_troposphere(self, TropoT)


class Url(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html
    Properties:
        - Name: Qualifier
        - Name: InvokeMode
        - Name: AuthType
        - Name: TargetFunctionArn
        - Name: Cors
    Attributes:
        - Name: FunctionArn
        - Name: FunctionUrl
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Qualifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-qualifier""", alias="Qualifier")
    InvokeMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-invokemode""", alias="InvokeMode")
    AuthType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-authtype""", alias="AuthType")
    TargetFunctionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-targetfunctionarn""", alias="TargetFunctionArn")
    Cors_: Optional['Cors'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-cors""", alias="Cors")
    

    @property
    def tropo_type(self) -> troposphere.awslambda.Url:
        from troposphere.awslambda import Url as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.awslambda import Url as TropoT
        return resource_to_troposphere(self, TropoT)


class Version(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html
    Properties:
        - Name: FunctionName
        - Name: ProvisionedConcurrencyConfig
        - Name: Description
        - Name: RuntimePolicy
        - Name: CodeSha256
    Attributes:
        - Name: FunctionArn
        - Name: Version
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FunctionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-functionname""", alias="FunctionName")
    ProvisionedConcurrencyConfig_: Optional['ProvisionedConcurrencyConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-provisionedconcurrencyconfig""", alias="ProvisionedConcurrencyConfig")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-description""", alias="Description")
    RuntimePolicy_: Optional['RuntimePolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-runtimepolicy""", alias="RuntimePolicy")
    CodeSha256_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-codesha256""", alias="CodeSha256")
    

    @property
    def tropo_type(self) -> troposphere.awslambda.Version:
        from troposphere.awslambda import Version as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.awslambda import Version as TropoT
        return resource_to_troposphere(self, TropoT)

