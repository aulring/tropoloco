from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AttributesItems(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-forecast-dataset-attributesitems.html
    Properties:
        - Name: AttributeType
        - Name: AttributeName
    
    """
    
    AttributeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-forecast-dataset-attributesitems.html#cfn-forecast-dataset-attributesitems-attributetype""", alias="AttributeType")
    AttributeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-forecast-dataset-attributesitems.html#cfn-forecast-dataset-attributesitems-attributename""", alias="AttributeName")
    


    @property
    def tropo_type(self) -> troposphere.forecast.AttributesItems:
        from troposphere.forecast import AttributesItems as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-forecast-dataset-encryptionconfig.html
    Properties:
        - Name: KmsKeyArn
        - Name: RoleArn
    
    """
    
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-forecast-dataset-encryptionconfig.html#cfn-forecast-dataset-encryptionconfig-kmskeyarn""", alias="KmsKeyArn")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-forecast-dataset-encryptionconfig.html#cfn-forecast-dataset-encryptionconfig-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.forecast.EncryptionConfig:
        from troposphere.forecast import EncryptionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Schema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-forecast-dataset-schema.html
    Properties:
        - Name: Attributes
    
    """
    
    Attributes_: Optional[List['AttributesItems']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-forecast-dataset-schema.html#cfn-forecast-dataset-schema-attributes""", alias="Attributes")
    


    @property
    def tropo_type(self) -> troposphere.forecast.Schema:
        from troposphere.forecast import Schema as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagsItems(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-forecast-dataset-tagsitems.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-forecast-dataset-tagsitems.html#cfn-forecast-dataset-tagsitems-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-forecast-dataset-tagsitems.html#cfn-forecast-dataset-tagsitems-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.forecast.TagsItems:
        from troposphere.forecast import TagsItems as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Dataset(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html
    Properties:
        - Name: DataFrequency
        - Name: DatasetName
        - Name: Schema
        - Name: DatasetType
        - Name: Domain
        - Name: EncryptionConfig
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DataFrequency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-datafrequency""", alias="DataFrequency")
    DatasetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-datasetname""", alias="DatasetName")
    Schema_: 'Schema' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-schema""", alias="Schema")
    DatasetType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-datasettype""", alias="DatasetType")
    Domain_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-domain""", alias="Domain")
    EncryptionConfig_: Optional['EncryptionConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-encryptionconfig""", alias="EncryptionConfig")
    Tags_: Optional[List['TagsItems']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html#cfn-forecast-dataset-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.forecast.Dataset:
        from troposphere.forecast import Dataset as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.forecast import Dataset as TropoT
        return resource_to_troposphere(self, TropoT)


class DatasetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html
    Properties:
        - Name: DatasetArns
        - Name: DatasetGroupName
        - Name: Domain
        - Name: Tags
    Attributes:
        - Name: DatasetGroupArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DatasetArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html#cfn-forecast-datasetgroup-datasetarns""", alias="DatasetArns")
    DatasetGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html#cfn-forecast-datasetgroup-datasetgroupname""", alias="DatasetGroupName")
    Domain_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html#cfn-forecast-datasetgroup-domain""", alias="Domain")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html#cfn-forecast-datasetgroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.forecast.DatasetGroup:
        from troposphere.forecast import DatasetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.forecast import DatasetGroup as TropoT
        return resource_to_troposphere(self, TropoT)

