from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################




######################################################################
# AWS Resource
######################################################################


class Link(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-oam-link.html
    Properties:
        - Name: SinkIdentifier
        - Name: LabelTemplate
        - Name: ResourceTypes
        - Name: Tags
    Attributes:
        - Name: Label
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SinkIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-oam-link.html#cfn-oam-link-sinkidentifier""", alias="SinkIdentifier")
    LabelTemplate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-oam-link.html#cfn-oam-link-labeltemplate""", alias="LabelTemplate")
    ResourceTypes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-oam-link.html#cfn-oam-link-resourcetypes""", alias="ResourceTypes")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-oam-link.html#cfn-oam-link-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.oam.Link:
        from troposphere.oam import Link as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.oam import Link as TropoT
        return resource_to_troposphere(self, TropoT)


class Sink(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-oam-sink.html
    Properties:
        - Name: Policy
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-oam-sink.html#cfn-oam-sink-policy""", alias="Policy")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-oam-sink.html#cfn-oam-sink-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-oam-sink.html#cfn-oam-sink-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.oam.Sink:
        from troposphere.oam import Sink as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.oam import Sink as TropoT
        return resource_to_troposphere(self, TropoT)

