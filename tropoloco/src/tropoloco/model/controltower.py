from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class EnabledControlParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-controltower-enabledcontrol-enabledcontrolparameter.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-controltower-enabledcontrol-enabledcontrolparameter.html#cfn-controltower-enabledcontrol-enabledcontrolparameter-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-controltower-enabledcontrol-enabledcontrolparameter.html#cfn-controltower-enabledcontrol-enabledcontrolparameter-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.controltower.EnabledControlParameter:
        from troposphere.controltower import EnabledControlParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class EnabledControl(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html
    Properties:
        - Name: Parameters
        - Name: ControlIdentifier
        - Name: TargetIdentifier
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Parameters_: Optional[List['EnabledControlParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html#cfn-controltower-enabledcontrol-parameters""", alias="Parameters")
    ControlIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html#cfn-controltower-enabledcontrol-controlidentifier""", alias="ControlIdentifier")
    TargetIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html#cfn-controltower-enabledcontrol-targetidentifier""", alias="TargetIdentifier")
    

    @property
    def tropo_type(self) -> troposphere.controltower.EnabledControl:
        from troposphere.controltower import EnabledControl as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.controltower import EnabledControl as TropoT
        return resource_to_troposphere(self, TropoT)


class LandingZone(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html
    Properties:
        - Name: Version
        - Name: Manifest
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: LatestAvailableVersion
        - Name: DriftStatus
        - Name: Arn
        - Name: LandingZoneIdentifier
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Version_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html#cfn-controltower-landingzone-version""", alias="Version")
    Manifest_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html#cfn-controltower-landingzone-manifest""", alias="Manifest")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html#cfn-controltower-landingzone-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.controltower.LandingZone:
        from troposphere.controltower import LandingZone as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.controltower import LandingZone as TropoT
        return resource_to_troposphere(self, TropoT)

