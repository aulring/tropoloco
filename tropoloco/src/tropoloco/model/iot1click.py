from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DeviceTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-devicetemplate.html
    Properties:
        - Name: DeviceType
        - Name: CallbackOverrides
    
    """
    
    DeviceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-devicetemplate.html#cfn-iot1click-project-devicetemplate-devicetype""", alias="DeviceType")
    CallbackOverrides_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-devicetemplate.html#cfn-iot1click-project-devicetemplate-callbackoverrides""", alias="CallbackOverrides")
    


    @property
    def tropo_type(self) -> troposphere.iot1click.DeviceTemplate:
        from troposphere.iot1click import DeviceTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PlacementTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-placementtemplate.html
    Properties:
        - Name: DeviceTemplates
        - Name: DefaultAttributes
    
    """
    
    DeviceTemplates_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-placementtemplate.html#cfn-iot1click-project-placementtemplate-devicetemplates""", alias="DeviceTemplates")
    DefaultAttributes_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-placementtemplate.html#cfn-iot1click-project-placementtemplate-defaultattributes""", alias="DefaultAttributes")
    


    @property
    def tropo_type(self) -> troposphere.iot1click.PlacementTemplate:
        from troposphere.iot1click import PlacementTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Device(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html
    Properties:
        - Name: DeviceId
        - Name: Enabled
    Attributes:
        - Name: DeviceId
        - Name: Enabled
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DeviceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html#cfn-iot1click-device-deviceid""", alias="DeviceId")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html#cfn-iot1click-device-enabled""", alias="Enabled")
    

    @property
    def tropo_type(self) -> troposphere.iot1click.Device:
        from troposphere.iot1click import Device as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot1click import Device as TropoT
        return resource_to_troposphere(self, TropoT)


class Placement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html
    Properties:
        - Name: PlacementName
        - Name: ProjectName
        - Name: AssociatedDevices
        - Name: Attributes
    Attributes:
        - Name: PlacementName
        - Name: ProjectName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PlacementName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-placementname""", alias="PlacementName")
    ProjectName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-projectname""", alias="ProjectName")
    AssociatedDevices_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-associateddevices""", alias="AssociatedDevices")
    Attributes_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html#cfn-iot1click-placement-attributes""", alias="Attributes")
    

    @property
    def tropo_type(self) -> troposphere.iot1click.Placement:
        from troposphere.iot1click import Placement as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot1click import Placement as TropoT
        return resource_to_troposphere(self, TropoT)


class Project(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html
    Properties:
        - Name: Description
        - Name: PlacementTemplate
        - Name: ProjectName
    Attributes:
        - Name: ProjectName
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html#cfn-iot1click-project-description""", alias="Description")
    PlacementTemplate_: 'PlacementTemplate' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html#cfn-iot1click-project-placementtemplate""", alias="PlacementTemplate")
    ProjectName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html#cfn-iot1click-project-projectname""", alias="ProjectName")
    

    @property
    def tropo_type(self) -> troposphere.iot1click.Project:
        from troposphere.iot1click import Project as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iot1click import Project as TropoT
        return resource_to_troposphere(self, TropoT)

