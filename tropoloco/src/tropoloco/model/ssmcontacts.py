from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ChannelTargetInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-channeltargetinfo.html
    Properties:
        - Name: RetryIntervalInMinutes
        - Name: ChannelId
    
    """
    
    RetryIntervalInMinutes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-channeltargetinfo.html#cfn-ssmcontacts-contact-channeltargetinfo-retryintervalinminutes""", alias="RetryIntervalInMinutes")
    ChannelId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-channeltargetinfo.html#cfn-ssmcontacts-contact-channeltargetinfo-channelid""", alias="ChannelId")
    


    @property
    def tropo_type(self) -> troposphere.ssmcontacts.ChannelTargetInfo:
        from troposphere.ssmcontacts import ChannelTargetInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContactTargetInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-contacttargetinfo.html
    Properties:
        - Name: ContactId
        - Name: IsEssential
    
    """
    
    ContactId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-contacttargetinfo.html#cfn-ssmcontacts-contact-contacttargetinfo-contactid""", alias="ContactId")
    IsEssential_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-contacttargetinfo.html#cfn-ssmcontacts-contact-contacttargetinfo-isessential""", alias="IsEssential")
    


    @property
    def tropo_type(self) -> troposphere.ssmcontacts.ContactTargetInfo:
        from troposphere.ssmcontacts import ContactTargetInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Stage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-stage.html
    Properties:
        - Name: DurationInMinutes
        - Name: RotationIds
        - Name: Targets
    
    """
    
    DurationInMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-stage.html#cfn-ssmcontacts-contact-stage-durationinminutes""", alias="DurationInMinutes")
    RotationIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-stage.html#cfn-ssmcontacts-contact-stage-rotationids""", alias="RotationIds")
    Targets_: Optional[List['Targets']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-stage.html#cfn-ssmcontacts-contact-stage-targets""", alias="Targets")
    


    @property
    def tropo_type(self) -> troposphere.ssmcontacts.Stage:
        from troposphere.ssmcontacts import Stage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Targets(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-targets.html
    Properties:
        - Name: ChannelTargetInfo
        - Name: ContactTargetInfo
    
    """
    
    ChannelTargetInfo_: Optional['ChannelTargetInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-targets.html#cfn-ssmcontacts-contact-targets-channeltargetinfo""", alias="ChannelTargetInfo")
    ContactTargetInfo_: Optional['ContactTargetInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-targets.html#cfn-ssmcontacts-contact-targets-contacttargetinfo""", alias="ContactTargetInfo")
    


    @property
    def tropo_type(self) -> troposphere.ssmcontacts.Targets:
        from troposphere.ssmcontacts import Targets as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ChannelTargetInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-channeltargetinfo.html
    Properties:
        - Name: RetryIntervalInMinutes
        - Name: ChannelId
    
    """
    
    RetryIntervalInMinutes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-channeltargetinfo.html#cfn-ssmcontacts-plan-channeltargetinfo-retryintervalinminutes""", alias="RetryIntervalInMinutes")
    ChannelId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-channeltargetinfo.html#cfn-ssmcontacts-plan-channeltargetinfo-channelid""", alias="ChannelId")
    


    @property
    def tropo_type(self) -> troposphere.ssmcontacts.ChannelTargetInfo:
        from troposphere.ssmcontacts import ChannelTargetInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContactTargetInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-contacttargetinfo.html
    Properties:
        - Name: ContactId
        - Name: IsEssential
    
    """
    
    ContactId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-contacttargetinfo.html#cfn-ssmcontacts-plan-contacttargetinfo-contactid""", alias="ContactId")
    IsEssential_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-contacttargetinfo.html#cfn-ssmcontacts-plan-contacttargetinfo-isessential""", alias="IsEssential")
    


    @property
    def tropo_type(self) -> troposphere.ssmcontacts.ContactTargetInfo:
        from troposphere.ssmcontacts import ContactTargetInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Stage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-stage.html
    Properties:
        - Name: DurationInMinutes
        - Name: Targets
    
    """
    
    DurationInMinutes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-stage.html#cfn-ssmcontacts-plan-stage-durationinminutes""", alias="DurationInMinutes")
    Targets_: Optional[List['Targets']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-stage.html#cfn-ssmcontacts-plan-stage-targets""", alias="Targets")
    


    @property
    def tropo_type(self) -> troposphere.ssmcontacts.Stage:
        from troposphere.ssmcontacts import Stage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Targets(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-targets.html
    Properties:
        - Name: ChannelTargetInfo
        - Name: ContactTargetInfo
    
    """
    
    ChannelTargetInfo_: Optional['ChannelTargetInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-targets.html#cfn-ssmcontacts-plan-targets-channeltargetinfo""", alias="ChannelTargetInfo")
    ContactTargetInfo_: Optional['ContactTargetInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-targets.html#cfn-ssmcontacts-plan-targets-contacttargetinfo""", alias="ContactTargetInfo")
    


    @property
    def tropo_type(self) -> troposphere.ssmcontacts.Targets:
        from troposphere.ssmcontacts import Targets as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CoverageTime(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-coveragetime.html
    Properties:
        - Name: EndTime
        - Name: StartTime
    
    """
    
    EndTime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-coveragetime.html#cfn-ssmcontacts-rotation-coveragetime-endtime""", alias="EndTime")
    StartTime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-coveragetime.html#cfn-ssmcontacts-rotation-coveragetime-starttime""", alias="StartTime")
    


    @property
    def tropo_type(self) -> troposphere.ssmcontacts.CoverageTime:
        from troposphere.ssmcontacts import CoverageTime as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonthlySetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-monthlysetting.html
    Properties:
        - Name: DayOfMonth
        - Name: HandOffTime
    
    """
    
    DayOfMonth_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-monthlysetting.html#cfn-ssmcontacts-rotation-monthlysetting-dayofmonth""", alias="DayOfMonth")
    HandOffTime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-monthlysetting.html#cfn-ssmcontacts-rotation-monthlysetting-handofftime""", alias="HandOffTime")
    


    @property
    def tropo_type(self) -> troposphere.ssmcontacts.MonthlySetting:
        from troposphere.ssmcontacts import MonthlySetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecurrenceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html
    Properties:
        - Name: DailySettings
        - Name: NumberOfOnCalls
        - Name: ShiftCoverages
        - Name: WeeklySettings
        - Name: RecurrenceMultiplier
        - Name: MonthlySettings
    
    """
    
    DailySettings_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html#cfn-ssmcontacts-rotation-recurrencesettings-dailysettings""", alias="DailySettings")
    NumberOfOnCalls_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html#cfn-ssmcontacts-rotation-recurrencesettings-numberofoncalls""", alias="NumberOfOnCalls")
    ShiftCoverages_: Optional[List['ShiftCoverage']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html#cfn-ssmcontacts-rotation-recurrencesettings-shiftcoverages""", alias="ShiftCoverages")
    WeeklySettings_: Optional[List['WeeklySetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html#cfn-ssmcontacts-rotation-recurrencesettings-weeklysettings""", alias="WeeklySettings")
    RecurrenceMultiplier_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html#cfn-ssmcontacts-rotation-recurrencesettings-recurrencemultiplier""", alias="RecurrenceMultiplier")
    MonthlySettings_: Optional[List['MonthlySetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html#cfn-ssmcontacts-rotation-recurrencesettings-monthlysettings""", alias="MonthlySettings")
    


    @property
    def tropo_type(self) -> troposphere.ssmcontacts.RecurrenceSettings:
        from troposphere.ssmcontacts import RecurrenceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ShiftCoverage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-shiftcoverage.html
    Properties:
        - Name: DayOfWeek
        - Name: CoverageTimes
    
    """
    
    DayOfWeek_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-shiftcoverage.html#cfn-ssmcontacts-rotation-shiftcoverage-dayofweek""", alias="DayOfWeek")
    CoverageTimes_: List['CoverageTime'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-shiftcoverage.html#cfn-ssmcontacts-rotation-shiftcoverage-coveragetimes""", alias="CoverageTimes")
    


    @property
    def tropo_type(self) -> troposphere.ssmcontacts.ShiftCoverage:
        from troposphere.ssmcontacts import ShiftCoverage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WeeklySetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-weeklysetting.html
    Properties:
        - Name: DayOfWeek
        - Name: HandOffTime
    
    """
    
    DayOfWeek_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-weeklysetting.html#cfn-ssmcontacts-rotation-weeklysetting-dayofweek""", alias="DayOfWeek")
    HandOffTime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-weeklysetting.html#cfn-ssmcontacts-rotation-weeklysetting-handofftime""", alias="HandOffTime")
    


    @property
    def tropo_type(self) -> troposphere.ssmcontacts.WeeklySetting:
        from troposphere.ssmcontacts import WeeklySetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Contact(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html
    Properties:
        - Name: Type
        - Name: Alias
        - Name: DisplayName
        - Name: Plan
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-type""", alias="Type")
    Alias_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-alias""", alias="Alias")
    DisplayName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-displayname""", alias="DisplayName")
    Plan_: Optional[List['Stage']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-plan""", alias="Plan")
    

    @property
    def tropo_type(self) -> troposphere.ssmcontacts.Contact:
        from troposphere.ssmcontacts import Contact as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssmcontacts import Contact as TropoT
        return resource_to_troposphere(self, TropoT)


class ContactChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html
    Properties:
        - Name: ChannelName
        - Name: ChannelAddress
        - Name: ContactId
        - Name: ChannelType
        - Name: DeferActivation
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ChannelName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channelname""", alias="ChannelName")
    ChannelAddress_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channeladdress""", alias="ChannelAddress")
    ContactId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-contactid""", alias="ContactId")
    ChannelType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channeltype""", alias="ChannelType")
    DeferActivation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-deferactivation""", alias="DeferActivation")
    

    @property
    def tropo_type(self) -> troposphere.ssmcontacts.ContactChannel:
        from troposphere.ssmcontacts import ContactChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssmcontacts import ContactChannel as TropoT
        return resource_to_troposphere(self, TropoT)


class Plan(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-plan.html
    Properties:
        - Name: RotationIds
        - Name: Stages
        - Name: ContactId
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RotationIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-plan.html#cfn-ssmcontacts-plan-rotationids""", alias="RotationIds")
    Stages_: Optional[List['Stage']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-plan.html#cfn-ssmcontacts-plan-stages""", alias="Stages")
    ContactId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-plan.html#cfn-ssmcontacts-plan-contactid""", alias="ContactId")
    

    @property
    def tropo_type(self) -> troposphere.ssmcontacts.Plan:
        from troposphere.ssmcontacts import Plan as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssmcontacts import Plan as TropoT
        return resource_to_troposphere(self, TropoT)


class Rotation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html
    Properties:
        - Name: Recurrence
        - Name: TimeZoneId
        - Name: StartTime
        - Name: Tags
        - Name: Name
        - Name: ContactIds
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Recurrence_: 'RecurrenceSettings' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html#cfn-ssmcontacts-rotation-recurrence""", alias="Recurrence")
    TimeZoneId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html#cfn-ssmcontacts-rotation-timezoneid""", alias="TimeZoneId")
    StartTime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html#cfn-ssmcontacts-rotation-starttime""", alias="StartTime")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html#cfn-ssmcontacts-rotation-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html#cfn-ssmcontacts-rotation-name""", alias="Name")
    ContactIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html#cfn-ssmcontacts-rotation-contactids""", alias="ContactIds")
    

    @property
    def tropo_type(self) -> troposphere.ssmcontacts.Rotation:
        from troposphere.ssmcontacts import Rotation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssmcontacts import Rotation as TropoT
        return resource_to_troposphere(self, TropoT)

