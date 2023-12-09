from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class MaintenanceWindow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html
    Properties:
        - Name: EndTimeMinute
        - Name: Type
        - Name: DaysOfTheWeek
        - Name: ApplyTimeOf
        - Name: StartTimeMinute
        - Name: StartTimeHour
        - Name: EndTimeHour
    
    """
    
    EndTimeMinute_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-endtimeminute""", alias="EndTimeMinute")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-type""", alias="Type")
    DaysOfTheWeek_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-daysoftheweek""", alias="DaysOfTheWeek")
    ApplyTimeOf_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-applytimeof""", alias="ApplyTimeOf")
    StartTimeMinute_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-starttimeminute""", alias="StartTimeMinute")
    StartTimeHour_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-starttimehour""", alias="StartTimeHour")
    EndTimeHour_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-endtimehour""", alias="EndTimeHour")
    


    @property
    def tropo_type(self) -> troposphere.workspacesthinclient.MaintenanceWindow:
        from troposphere.workspacesthinclient import MaintenanceWindow as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Environment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html
    Properties:
        - Name: DesiredSoftwareSetId
        - Name: KmsKeyArn
        - Name: DesktopArn
        - Name: SoftwareSetUpdateMode
        - Name: SoftwareSetUpdateSchedule
        - Name: MaintenanceWindow
        - Name: DesktopEndpoint
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: DesktopType
        - Name: RegisteredDevicesCount
        - Name: PendingSoftwareSetId
        - Name: CreatedAt
        - Name: PendingSoftwareSetVersion
        - Name: Id
        - Name: Arn
        - Name: UpdatedAt
        - Name: ActivationCode
        - Name: SoftwareSetComplianceStatus
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DesiredSoftwareSetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-desiredsoftwaresetid""", alias="DesiredSoftwareSetId")
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-kmskeyarn""", alias="KmsKeyArn")
    DesktopArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-desktoparn""", alias="DesktopArn")
    SoftwareSetUpdateMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-softwaresetupdatemode""", alias="SoftwareSetUpdateMode")
    SoftwareSetUpdateSchedule_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-softwaresetupdateschedule""", alias="SoftwareSetUpdateSchedule")
    MaintenanceWindow_: Optional['MaintenanceWindow'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-maintenancewindow""", alias="MaintenanceWindow")
    DesktopEndpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-desktopendpoint""", alias="DesktopEndpoint")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.workspacesthinclient.Environment:
        from troposphere.workspacesthinclient import Environment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.workspacesthinclient import Environment as TropoT
        return resource_to_troposphere(self, TropoT)

