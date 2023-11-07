from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Field(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-field.html
    Properties:
        - Name: RefValue
        - Name: StringValue
        - Name: Key
    
    """
    
    RefValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-field.html#cfn-datapipeline-pipeline-field-refvalue""", alias="RefValue")
    StringValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-field.html#cfn-datapipeline-pipeline-field-stringvalue""", alias="StringValue")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-field.html#cfn-datapipeline-pipeline-field-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.datapipeline.Field:
        from troposphere.datapipeline import Field as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ParameterAttribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parameterattribute.html
    Properties:
        - Name: StringValue
        - Name: Key
    
    """
    
    StringValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parameterattribute.html#cfn-datapipeline-pipeline-parameterattribute-stringvalue""", alias="StringValue")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parameterattribute.html#cfn-datapipeline-pipeline-parameterattribute-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.datapipeline.ParameterAttribute:
        from troposphere.datapipeline import ParameterAttribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ParameterObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parameterobject.html
    Properties:
        - Name: Attributes
        - Name: Id
    
    """
    
    Attributes_: List['ParameterAttribute'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parameterobject.html#cfn-datapipeline-pipeline-parameterobject-attributes""", alias="Attributes")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parameterobject.html#cfn-datapipeline-pipeline-parameterobject-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.datapipeline.ParameterObject:
        from troposphere.datapipeline import ParameterObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ParameterValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parametervalue.html
    Properties:
        - Name: Id
        - Name: StringValue
    
    """
    
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parametervalue.html#cfn-datapipeline-pipeline-parametervalue-id""", alias="Id")
    StringValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-parametervalue.html#cfn-datapipeline-pipeline-parametervalue-stringvalue""", alias="StringValue")
    


    @property
    def tropo_type(self) -> troposphere.datapipeline.ParameterValue:
        from troposphere.datapipeline import ParameterValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipelineObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelineobject.html
    Properties:
        - Name: Fields
        - Name: Id
        - Name: Name
    
    """
    
    Fields_: List['Field'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelineobject.html#cfn-datapipeline-pipeline-pipelineobject-fields""", alias="Fields")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelineobject.html#cfn-datapipeline-pipeline-pipelineobject-id""", alias="Id")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelineobject.html#cfn-datapipeline-pipeline-pipelineobject-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.datapipeline.PipelineObject:
        from troposphere.datapipeline import PipelineObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipelineTag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelinetag.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelinetag.html#cfn-datapipeline-pipeline-pipelinetag-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datapipeline-pipeline-pipelinetag.html#cfn-datapipeline-pipeline-pipelinetag-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.datapipeline.PipelineTag:
        from troposphere.datapipeline import PipelineTag as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Pipeline(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html
    Properties:
        - Name: PipelineTags
        - Name: ParameterObjects
        - Name: Description
        - Name: Activate
        - Name: PipelineObjects
        - Name: ParameterValues
        - Name: Name
    Attributes:
        - Name: PipelineId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PipelineTags_: Optional[List['PipelineTag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-pipelinetags""", alias="PipelineTags")
    ParameterObjects_: Optional[List['ParameterObject']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-parameterobjects""", alias="ParameterObjects")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-description""", alias="Description")
    Activate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-activate""", alias="Activate")
    PipelineObjects_: Optional[List['PipelineObject']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-pipelineobjects""", alias="PipelineObjects")
    ParameterValues_: Optional[List['ParameterValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-parametervalues""", alias="ParameterValues")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html#cfn-datapipeline-pipeline-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.datapipeline.Pipeline:
        from troposphere.datapipeline import Pipeline as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.datapipeline import Pipeline as TropoT
        return resource_to_troposphere(self, TropoT)

