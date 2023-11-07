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


class EnabledControl(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html
    Properties:
        - Name: ControlIdentifier
        - Name: TargetIdentifier
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ControlIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html#cfn-controltower-enabledcontrol-controlidentifier""", alias="ControlIdentifier")
    TargetIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html#cfn-controltower-enabledcontrol-targetidentifier""", alias="TargetIdentifier")
    

    @property
    def tropo_type(self) -> troposphere.controltower.EnabledControl:
        from troposphere.controltower import EnabledControl as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.controltower import EnabledControl as TropoT
        return resource_to_troposphere(self, TropoT)

