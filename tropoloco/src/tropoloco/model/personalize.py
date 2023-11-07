from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasource.html
    Properties:
        - Name: DataLocation
    
    """
    
    DataLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasource.html#cfn-personalize-dataset-datasource-datalocation""", alias="DataLocation")
    


    @property
    def tropo_type(self) -> troposphere.personalize.DataSource:
        from troposphere.personalize import DataSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatasetImportJob(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html
    Properties:
        - Name: DatasetArn
        - Name: JobName
        - Name: DatasetImportJobArn
        - Name: RoleArn
        - Name: DataSource
    
    """
    
    DatasetArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-datasetarn""", alias="DatasetArn")
    JobName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-jobname""", alias="JobName")
    DatasetImportJobArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-datasetimportjobarn""", alias="DatasetImportJobArn")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-rolearn""", alias="RoleArn")
    DataSource_: Optional['DataSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-datasource""", alias="DataSource")
    


    @property
    def tropo_type(self) -> troposphere.personalize.DatasetImportJob:
        from troposphere.personalize import DatasetImportJob as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AlgorithmHyperParameterRanges(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-algorithmhyperparameterranges.html
    Properties:
        - Name: IntegerHyperParameterRanges
        - Name: CategoricalHyperParameterRanges
        - Name: ContinuousHyperParameterRanges
    
    """
    
    IntegerHyperParameterRanges_: Optional[List['IntegerHyperParameterRange']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-algorithmhyperparameterranges.html#cfn-personalize-solution-algorithmhyperparameterranges-integerhyperparameterranges""", alias="IntegerHyperParameterRanges")
    CategoricalHyperParameterRanges_: Optional[List['CategoricalHyperParameterRange']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-algorithmhyperparameterranges.html#cfn-personalize-solution-algorithmhyperparameterranges-categoricalhyperparameterranges""", alias="CategoricalHyperParameterRanges")
    ContinuousHyperParameterRanges_: Optional[List['ContinuousHyperParameterRange']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-algorithmhyperparameterranges.html#cfn-personalize-solution-algorithmhyperparameterranges-continuoushyperparameterranges""", alias="ContinuousHyperParameterRanges")
    


    @property
    def tropo_type(self) -> troposphere.personalize.AlgorithmHyperParameterRanges:
        from troposphere.personalize import AlgorithmHyperParameterRanges as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoMLConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-automlconfig.html
    Properties:
        - Name: MetricName
        - Name: RecipeList
    
    """
    
    MetricName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-automlconfig.html#cfn-personalize-solution-automlconfig-metricname""", alias="MetricName")
    RecipeList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-automlconfig.html#cfn-personalize-solution-automlconfig-recipelist""", alias="RecipeList")
    


    @property
    def tropo_type(self) -> troposphere.personalize.AutoMLConfig:
        from troposphere.personalize import AutoMLConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CategoricalHyperParameterRange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-categoricalhyperparameterrange.html
    Properties:
        - Name: Values
        - Name: Name
    
    """
    
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-categoricalhyperparameterrange.html#cfn-personalize-solution-categoricalhyperparameterrange-values""", alias="Values")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-categoricalhyperparameterrange.html#cfn-personalize-solution-categoricalhyperparameterrange-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.personalize.CategoricalHyperParameterRange:
        from troposphere.personalize import CategoricalHyperParameterRange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContinuousHyperParameterRange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-continuoushyperparameterrange.html
    Properties:
        - Name: MinValue
        - Name: MaxValue
        - Name: Name
    
    """
    
    MinValue_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-continuoushyperparameterrange.html#cfn-personalize-solution-continuoushyperparameterrange-minvalue""", alias="MinValue")
    MaxValue_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-continuoushyperparameterrange.html#cfn-personalize-solution-continuoushyperparameterrange-maxvalue""", alias="MaxValue")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-continuoushyperparameterrange.html#cfn-personalize-solution-continuoushyperparameterrange-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.personalize.ContinuousHyperParameterRange:
        from troposphere.personalize import ContinuousHyperParameterRange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HpoConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoconfig.html
    Properties:
        - Name: HpoResourceConfig
        - Name: AlgorithmHyperParameterRanges
        - Name: HpoObjective
    
    """
    
    HpoResourceConfig_: Optional['HpoResourceConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoconfig.html#cfn-personalize-solution-hpoconfig-hporesourceconfig""", alias="HpoResourceConfig")
    AlgorithmHyperParameterRanges_: Optional['AlgorithmHyperParameterRanges'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoconfig.html#cfn-personalize-solution-hpoconfig-algorithmhyperparameterranges""", alias="AlgorithmHyperParameterRanges")
    HpoObjective_: Optional['HpoObjective'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoconfig.html#cfn-personalize-solution-hpoconfig-hpoobjective""", alias="HpoObjective")
    


    @property
    def tropo_type(self) -> troposphere.personalize.HpoConfig:
        from troposphere.personalize import HpoConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HpoObjective(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoobjective.html
    Properties:
        - Name: MetricName
        - Name: Type
        - Name: MetricRegex
    
    """
    
    MetricName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoobjective.html#cfn-personalize-solution-hpoobjective-metricname""", alias="MetricName")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoobjective.html#cfn-personalize-solution-hpoobjective-type""", alias="Type")
    MetricRegex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoobjective.html#cfn-personalize-solution-hpoobjective-metricregex""", alias="MetricRegex")
    


    @property
    def tropo_type(self) -> troposphere.personalize.HpoObjective:
        from troposphere.personalize import HpoObjective as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HpoResourceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hporesourceconfig.html
    Properties:
        - Name: MaxParallelTrainingJobs
        - Name: MaxNumberOfTrainingJobs
    
    """
    
    MaxParallelTrainingJobs_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hporesourceconfig.html#cfn-personalize-solution-hporesourceconfig-maxparalleltrainingjobs""", alias="MaxParallelTrainingJobs")
    MaxNumberOfTrainingJobs_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hporesourceconfig.html#cfn-personalize-solution-hporesourceconfig-maxnumberoftrainingjobs""", alias="MaxNumberOfTrainingJobs")
    


    @property
    def tropo_type(self) -> troposphere.personalize.HpoResourceConfig:
        from troposphere.personalize import HpoResourceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IntegerHyperParameterRange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-integerhyperparameterrange.html
    Properties:
        - Name: MinValue
        - Name: MaxValue
        - Name: Name
    
    """
    
    MinValue_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-integerhyperparameterrange.html#cfn-personalize-solution-integerhyperparameterrange-minvalue""", alias="MinValue")
    MaxValue_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-integerhyperparameterrange.html#cfn-personalize-solution-integerhyperparameterrange-maxvalue""", alias="MaxValue")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-integerhyperparameterrange.html#cfn-personalize-solution-integerhyperparameterrange-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.personalize.IntegerHyperParameterRange:
        from troposphere.personalize import IntegerHyperParameterRange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SolutionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html
    Properties:
        - Name: EventValueThreshold
        - Name: HpoConfig
        - Name: AlgorithmHyperParameters
        - Name: FeatureTransformationParameters
        - Name: AutoMLConfig
    
    """
    
    EventValueThreshold_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-eventvaluethreshold""", alias="EventValueThreshold")
    HpoConfig_: Optional['HpoConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-hpoconfig""", alias="HpoConfig")
    AlgorithmHyperParameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-algorithmhyperparameters""", alias="AlgorithmHyperParameters")
    FeatureTransformationParameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-featuretransformationparameters""", alias="FeatureTransformationParameters")
    AutoMLConfig_: Optional['AutoMLConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-automlconfig""", alias="AutoMLConfig")
    


    @property
    def tropo_type(self) -> troposphere.personalize.SolutionConfig:
        from troposphere.personalize import SolutionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Dataset(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html
    Properties:
        - Name: DatasetGroupArn
        - Name: DatasetType
        - Name: DatasetImportJob
        - Name: SchemaArn
        - Name: Name
    Attributes:
        - Name: DatasetArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DatasetGroupArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-datasetgrouparn""", alias="DatasetGroupArn")
    DatasetType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-datasettype""", alias="DatasetType")
    DatasetImportJob_: Optional['DatasetImportJob'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-datasetimportjob""", alias="DatasetImportJob")
    SchemaArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-schemaarn""", alias="SchemaArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.personalize.Dataset:
        from troposphere.personalize import Dataset as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.personalize import Dataset as TropoT
        return resource_to_troposphere(self, TropoT)


class DatasetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html
    Properties:
        - Name: KmsKeyArn
        - Name: Domain
        - Name: RoleArn
        - Name: Name
    Attributes:
        - Name: DatasetGroupArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-kmskeyarn""", alias="KmsKeyArn")
    Domain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-domain""", alias="Domain")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-rolearn""", alias="RoleArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.personalize.DatasetGroup:
        from troposphere.personalize import DatasetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.personalize import DatasetGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class Schema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html
    Properties:
        - Name: Schema
        - Name: Domain
        - Name: Name
    Attributes:
        - Name: SchemaArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Schema_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html#cfn-personalize-schema-schema""", alias="Schema")
    Domain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html#cfn-personalize-schema-domain""", alias="Domain")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html#cfn-personalize-schema-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.personalize.Schema:
        from troposphere.personalize import Schema as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.personalize import Schema as TropoT
        return resource_to_troposphere(self, TropoT)


class Solution(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html
    Properties:
        - Name: PerformAutoML
        - Name: PerformHPO
        - Name: EventType
        - Name: DatasetGroupArn
        - Name: SolutionConfig
        - Name: RecipeArn
        - Name: Name
    Attributes:
        - Name: SolutionArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PerformAutoML_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-performautoml""", alias="PerformAutoML")
    PerformHPO_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-performhpo""", alias="PerformHPO")
    EventType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-eventtype""", alias="EventType")
    DatasetGroupArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-datasetgrouparn""", alias="DatasetGroupArn")
    SolutionConfig_: Optional['SolutionConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-solutionconfig""", alias="SolutionConfig")
    RecipeArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-recipearn""", alias="RecipeArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.personalize.Solution:
        from troposphere.personalize import Solution as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.personalize import Solution as TropoT
        return resource_to_troposphere(self, TropoT)

