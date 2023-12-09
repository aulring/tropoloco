from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ControlCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition.html
    Properties:
        - Name: Type
        - Name: AlarmIdentifier
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition.html#cfn-arczonalshift-zonalautoshiftconfiguration-controlcondition-type""", alias="Type")
    AlarmIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition.html#cfn-arczonalshift-zonalautoshiftconfiguration-controlcondition-alarmidentifier""", alias="AlarmIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.arczonalshift.ControlCondition:
        from troposphere.arczonalshift import ControlCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PracticeRunConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.html
    Properties:
        - Name: BlockedDates
        - Name: OutcomeAlarms
        - Name: BlockingAlarms
        - Name: BlockedWindows
    
    """
    
    BlockedDates_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockeddates""", alias="BlockedDates")
    OutcomeAlarms_: List['ControlCondition'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-outcomealarms""", alias="OutcomeAlarms")
    BlockingAlarms_: Optional[List['ControlCondition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockingalarms""", alias="BlockingAlarms")
    BlockedWindows_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockedwindows""", alias="BlockedWindows")
    


    @property
    def tropo_type(self) -> troposphere.arczonalshift.PracticeRunConfiguration:
        from troposphere.arczonalshift import PracticeRunConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ZonalAutoshiftConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arczonalshift-zonalautoshiftconfiguration.html
    Properties:
        - Name: ResourceIdentifier
        - Name: ZonalAutoshiftStatus
        - Name: PracticeRunConfiguration
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arczonalshift-zonalautoshiftconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-resourceidentifier""", alias="ResourceIdentifier")
    ZonalAutoshiftStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arczonalshift-zonalautoshiftconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-zonalautoshiftstatus""", alias="ZonalAutoshiftStatus")
    PracticeRunConfiguration_: Optional['PracticeRunConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arczonalshift-zonalautoshiftconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration""", alias="PracticeRunConfiguration")
    

    @property
    def tropo_type(self) -> troposphere.arczonalshift.ZonalAutoshiftConfiguration:
        from troposphere.arczonalshift import ZonalAutoshiftConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.arczonalshift import ZonalAutoshiftConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)

