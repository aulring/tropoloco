from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DeviceUnderTest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest.html
    Properties:
        - Name: ThingArn
        - Name: CertificateArn
    
    """
    
    ThingArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest.html#cfn-iotcoredeviceadvisor-suitedefinition-deviceundertest-thingarn""", alias="ThingArn")
    CertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-deviceundertest.html#cfn-iotcoredeviceadvisor-suitedefinition-deviceundertest-certificatearn""", alias="CertificateArn")
    


    @property
    def tropo_type(self) -> troposphere.iotcoredeviceadvisor.DeviceUnderTest:
        from troposphere.iotcoredeviceadvisor import DeviceUnderTest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SuiteDefinitionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html
    Properties:
        - Name: DevicePermissionRoleArn
        - Name: SuiteDefinitionName
        - Name: IntendedForQualification
        - Name: Devices
        - Name: RootGroup
    
    """
    
    DevicePermissionRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-devicepermissionrolearn""", alias="DevicePermissionRoleArn")
    SuiteDefinitionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-suitedefinitionname""", alias="SuiteDefinitionName")
    IntendedForQualification_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-intendedforqualification""", alias="IntendedForQualification")
    Devices_: Optional[List['DeviceUnderTest']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-devices""", alias="Devices")
    RootGroup_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration-rootgroup""", alias="RootGroup")
    


    @property
    def tropo_type(self) -> troposphere.iotcoredeviceadvisor.SuiteDefinitionConfiguration:
        from troposphere.iotcoredeviceadvisor import SuiteDefinitionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class SuiteDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html
    Properties:
        - Name: SuiteDefinitionConfiguration
        - Name: Tags
    Attributes:
        - Name: SuiteDefinitionArn
        - Name: SuiteDefinitionVersion
        - Name: SuiteDefinitionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SuiteDefinitionConfiguration_: 'SuiteDefinitionConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration""", alias="SuiteDefinitionConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotcoredeviceadvisor.SuiteDefinition:
        from troposphere.iotcoredeviceadvisor import SuiteDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotcoredeviceadvisor import SuiteDefinition as TropoT
        return resource_to_troposphere(self, TropoT)

