from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AugmentedManifestsListItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-augmentedmanifestslistitem.html
    Properties:
        - Name: S3Uri
        - Name: AttributeNames
        - Name: Split
    
    """
    
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-augmentedmanifestslistitem.html#cfn-comprehend-documentclassifier-augmentedmanifestslistitem-s3uri""", alias="S3Uri")
    AttributeNames_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-augmentedmanifestslistitem.html#cfn-comprehend-documentclassifier-augmentedmanifestslistitem-attributenames""", alias="AttributeNames")
    Split_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-augmentedmanifestslistitem.html#cfn-comprehend-documentclassifier-augmentedmanifestslistitem-split""", alias="Split")
    


    @property
    def tropo_type(self) -> troposphere.comprehend.AugmentedManifestsListItem:
        from troposphere.comprehend import AugmentedManifestsListItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DocumentClassifierDocuments(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierdocuments.html
    Properties:
        - Name: S3Uri
        - Name: TestS3Uri
    
    """
    
    S3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierdocuments.html#cfn-comprehend-documentclassifier-documentclassifierdocuments-s3uri""", alias="S3Uri")
    TestS3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierdocuments.html#cfn-comprehend-documentclassifier-documentclassifierdocuments-tests3uri""", alias="TestS3Uri")
    


    @property
    def tropo_type(self) -> troposphere.comprehend.DocumentClassifierDocuments:
        from troposphere.comprehend import DocumentClassifierDocuments as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DocumentClassifierInputDataConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html
    Properties:
        - Name: DocumentReaderConfig
        - Name: S3Uri
        - Name: Documents
        - Name: DataFormat
        - Name: DocumentType
        - Name: AugmentedManifests
        - Name: LabelDelimiter
        - Name: TestS3Uri
    
    """
    
    DocumentReaderConfig_: Optional['DocumentReaderConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-documentreaderconfig""", alias="DocumentReaderConfig")
    S3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-s3uri""", alias="S3Uri")
    Documents_: Optional['DocumentClassifierDocuments'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-documents""", alias="Documents")
    DataFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-dataformat""", alias="DataFormat")
    DocumentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-documenttype""", alias="DocumentType")
    AugmentedManifests_: Optional[List['AugmentedManifestsListItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-augmentedmanifests""", alias="AugmentedManifests")
    LabelDelimiter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-labeldelimiter""", alias="LabelDelimiter")
    TestS3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-tests3uri""", alias="TestS3Uri")
    


    @property
    def tropo_type(self) -> troposphere.comprehend.DocumentClassifierInputDataConfig:
        from troposphere.comprehend import DocumentClassifierInputDataConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DocumentClassifierOutputDataConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifieroutputdataconfig.html
    Properties:
        - Name: KmsKeyId
        - Name: S3Uri
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifieroutputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifieroutputdataconfig-kmskeyid""", alias="KmsKeyId")
    S3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifieroutputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifieroutputdataconfig-s3uri""", alias="S3Uri")
    


    @property
    def tropo_type(self) -> troposphere.comprehend.DocumentClassifierOutputDataConfig:
        from troposphere.comprehend import DocumentClassifierOutputDataConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DocumentReaderConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentreaderconfig.html
    Properties:
        - Name: FeatureTypes
        - Name: DocumentReadMode
        - Name: DocumentReadAction
    
    """
    
    FeatureTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentreaderconfig.html#cfn-comprehend-documentclassifier-documentreaderconfig-featuretypes""", alias="FeatureTypes")
    DocumentReadMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentreaderconfig.html#cfn-comprehend-documentclassifier-documentreaderconfig-documentreadmode""", alias="DocumentReadMode")
    DocumentReadAction_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentreaderconfig.html#cfn-comprehend-documentclassifier-documentreaderconfig-documentreadaction""", alias="DocumentReadAction")
    


    @property
    def tropo_type(self) -> troposphere.comprehend.DocumentReaderConfig:
        from troposphere.comprehend import DocumentReaderConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-vpcconfig.html
    Properties:
        - Name: Subnets
        - Name: SecurityGroupIds
    
    """
    
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-vpcconfig.html#cfn-comprehend-documentclassifier-vpcconfig-subnets""", alias="Subnets")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-vpcconfig.html#cfn-comprehend-documentclassifier-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.comprehend.VpcConfig:
        from troposphere.comprehend import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataSecurityConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html
    Properties:
        - Name: VpcConfig
        - Name: VolumeKmsKeyId
        - Name: ModelKmsKeyId
        - Name: DataLakeKmsKeyId
    
    """
    
    VpcConfig_: Optional['VpcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html#cfn-comprehend-flywheel-datasecurityconfig-vpcconfig""", alias="VpcConfig")
    VolumeKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html#cfn-comprehend-flywheel-datasecurityconfig-volumekmskeyid""", alias="VolumeKmsKeyId")
    ModelKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html#cfn-comprehend-flywheel-datasecurityconfig-modelkmskeyid""", alias="ModelKmsKeyId")
    DataLakeKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html#cfn-comprehend-flywheel-datasecurityconfig-datalakekmskeyid""", alias="DataLakeKmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.comprehend.DataSecurityConfig:
        from troposphere.comprehend import DataSecurityConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DocumentClassificationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-documentclassificationconfig.html
    Properties:
        - Name: Mode
        - Name: Labels
    
    """
    
    Mode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-documentclassificationconfig.html#cfn-comprehend-flywheel-documentclassificationconfig-mode""", alias="Mode")
    Labels_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-documentclassificationconfig.html#cfn-comprehend-flywheel-documentclassificationconfig-labels""", alias="Labels")
    


    @property
    def tropo_type(self) -> troposphere.comprehend.DocumentClassificationConfig:
        from troposphere.comprehend import DocumentClassificationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EntityRecognitionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entityrecognitionconfig.html
    Properties:
        - Name: EntityTypes
    
    """
    
    EntityTypes_: Optional[List['EntityTypesListItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entityrecognitionconfig.html#cfn-comprehend-flywheel-entityrecognitionconfig-entitytypes""", alias="EntityTypes")
    


    @property
    def tropo_type(self) -> troposphere.comprehend.EntityRecognitionConfig:
        from troposphere.comprehend import EntityRecognitionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EntityTypesListItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entitytypeslistitem.html
    Properties:
        - Name: Type
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entitytypeslistitem.html#cfn-comprehend-flywheel-entitytypeslistitem-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.comprehend.EntityTypesListItem:
        from troposphere.comprehend import EntityTypesListItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TaskConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html
    Properties:
        - Name: LanguageCode
        - Name: DocumentClassificationConfig
        - Name: EntityRecognitionConfig
    
    """
    
    LanguageCode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html#cfn-comprehend-flywheel-taskconfig-languagecode""", alias="LanguageCode")
    DocumentClassificationConfig_: Optional['DocumentClassificationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html#cfn-comprehend-flywheel-taskconfig-documentclassificationconfig""", alias="DocumentClassificationConfig")
    EntityRecognitionConfig_: Optional['EntityRecognitionConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html#cfn-comprehend-flywheel-taskconfig-entityrecognitionconfig""", alias="EntityRecognitionConfig")
    


    @property
    def tropo_type(self) -> troposphere.comprehend.TaskConfig:
        from troposphere.comprehend import TaskConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-vpcconfig.html
    Properties:
        - Name: Subnets
        - Name: SecurityGroupIds
    
    """
    
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-vpcconfig.html#cfn-comprehend-flywheel-vpcconfig-subnets""", alias="Subnets")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-vpcconfig.html#cfn-comprehend-flywheel-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.comprehend.VpcConfig:
        from troposphere.comprehend import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class DocumentClassifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html
    Properties:
        - Name: LanguageCode
        - Name: DataAccessRoleArn
        - Name: OutputDataConfig
        - Name: VpcConfig
        - Name: DocumentClassifierName
        - Name: Mode
        - Name: VolumeKmsKeyId
        - Name: ModelKmsKeyId
        - Name: VersionName
        - Name: ModelPolicy
        - Name: InputDataConfig
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LanguageCode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-languagecode""", alias="LanguageCode")
    DataAccessRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-dataaccessrolearn""", alias="DataAccessRoleArn")
    OutputDataConfig_: Optional['DocumentClassifierOutputDataConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-outputdataconfig""", alias="OutputDataConfig")
    VpcConfig_: Optional['VpcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-vpcconfig""", alias="VpcConfig")
    DocumentClassifierName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-documentclassifiername""", alias="DocumentClassifierName")
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-mode""", alias="Mode")
    VolumeKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-volumekmskeyid""", alias="VolumeKmsKeyId")
    ModelKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-modelkmskeyid""", alias="ModelKmsKeyId")
    VersionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-versionname""", alias="VersionName")
    ModelPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-modelpolicy""", alias="ModelPolicy")
    InputDataConfig_: 'DocumentClassifierInputDataConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-inputdataconfig""", alias="InputDataConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.comprehend.DocumentClassifier:
        from troposphere.comprehend import DocumentClassifier as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.comprehend import DocumentClassifier as TropoT
        return resource_to_troposphere(self, TropoT)


class Flywheel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html
    Properties:
        - Name: DataLakeS3Uri
        - Name: DataAccessRoleArn
        - Name: FlywheelName
        - Name: ModelType
        - Name: TaskConfig
        - Name: ActiveModelArn
        - Name: DataSecurityConfig
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DataLakeS3Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-datalakes3uri""", alias="DataLakeS3Uri")
    DataAccessRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-dataaccessrolearn""", alias="DataAccessRoleArn")
    FlywheelName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-flywheelname""", alias="FlywheelName")
    ModelType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-modeltype""", alias="ModelType")
    TaskConfig_: Optional['TaskConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-taskconfig""", alias="TaskConfig")
    ActiveModelArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-activemodelarn""", alias="ActiveModelArn")
    DataSecurityConfig_: Optional['DataSecurityConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-datasecurityconfig""", alias="DataSecurityConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.comprehend.Flywheel:
        from troposphere.comprehend import Flywheel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.comprehend import Flywheel as TropoT
        return resource_to_troposphere(self, TropoT)

