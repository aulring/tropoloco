from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DefinitionDocument(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html
    Properties:
        - Name: Language
        - Name: Text
    
    """
    
    Language_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html#cfn-iotthingsgraph-flowtemplate-definitiondocument-language""", alias="Language")
    Text_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html#cfn-iotthingsgraph-flowtemplate-definitiondocument-text""", alias="Text")
    


    @property
    def tropo_type(self) -> troposphere.iotthingsgraph.DefinitionDocument:
        from troposphere.iotthingsgraph import DefinitionDocument as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class FlowTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html
    Properties:
        - Name: CompatibleNamespaceVersion
        - Name: Definition
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CompatibleNamespaceVersion_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-compatiblenamespaceversion""", alias="CompatibleNamespaceVersion")
    Definition_: 'DefinitionDocument' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-definition""", alias="Definition")
    

    @property
    def tropo_type(self) -> troposphere.iotthingsgraph.FlowTemplate:
        from troposphere.iotthingsgraph import FlowTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotthingsgraph import FlowTemplate as TropoT
        return resource_to_troposphere(self, TropoT)

