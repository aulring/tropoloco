from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html
    Properties:
        - Name: CrossRegionCopy
        - Name: Name
    
    """
    
    CrossRegionCopy_: List['CrossRegionCopyAction'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html#cfn-dlm-lifecyclepolicy-action-crossregioncopy""", alias="CrossRegionCopy")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html#cfn-dlm-lifecyclepolicy-action-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.dlm.Action:
        from troposphere.dlm import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ArchiveRetainRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-archiveretainrule.html
    Properties:
        - Name: RetentionArchiveTier
    
    """
    
    RetentionArchiveTier_: 'RetentionArchiveTier' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-archiveretainrule.html#cfn-dlm-lifecyclepolicy-archiveretainrule-retentionarchivetier""", alias="RetentionArchiveTier")
    


    @property
    def tropo_type(self) -> troposphere.dlm.ArchiveRetainRule:
        from troposphere.dlm import ArchiveRetainRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ArchiveRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-archiverule.html
    Properties:
        - Name: RetainRule
    
    """
    
    RetainRule_: 'ArchiveRetainRule' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-archiverule.html#cfn-dlm-lifecyclepolicy-archiverule-retainrule""", alias="RetainRule")
    


    @property
    def tropo_type(self) -> troposphere.dlm.ArchiveRule:
        from troposphere.dlm import ArchiveRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CreateRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html
    Properties:
        - Name: IntervalUnit
        - Name: Scripts
        - Name: Times
        - Name: CronExpression
        - Name: Interval
        - Name: Location
    
    """
    
    IntervalUnit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-intervalunit""", alias="IntervalUnit")
    Scripts_: Optional[List['Script']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-scripts""", alias="Scripts")
    Times_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-times""", alias="Times")
    CronExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-cronexpression""", alias="CronExpression")
    Interval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-interval""", alias="Interval")
    Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-location""", alias="Location")
    


    @property
    def tropo_type(self) -> troposphere.dlm.CreateRule:
        from troposphere.dlm import CreateRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CrossRegionCopyAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html
    Properties:
        - Name: Target
        - Name: EncryptionConfiguration
        - Name: RetainRule
    
    """
    
    Target_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-target""", alias="Target")
    EncryptionConfiguration_: 'EncryptionConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-encryptionconfiguration""", alias="EncryptionConfiguration")
    RetainRule_: Optional['CrossRegionCopyRetainRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-retainrule""", alias="RetainRule")
    


    @property
    def tropo_type(self) -> troposphere.dlm.CrossRegionCopyAction:
        from troposphere.dlm import CrossRegionCopyAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CrossRegionCopyDeprecateRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html
    Properties:
        - Name: IntervalUnit
        - Name: Interval
    
    """
    
    IntervalUnit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-intervalunit""", alias="IntervalUnit")
    Interval_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-interval""", alias="Interval")
    


    @property
    def tropo_type(self) -> troposphere.dlm.CrossRegionCopyDeprecateRule:
        from troposphere.dlm import CrossRegionCopyDeprecateRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CrossRegionCopyRetainRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html
    Properties:
        - Name: IntervalUnit
        - Name: Interval
    
    """
    
    IntervalUnit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyretainrule-intervalunit""", alias="IntervalUnit")
    Interval_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyretainrule-interval""", alias="Interval")
    


    @property
    def tropo_type(self) -> troposphere.dlm.CrossRegionCopyRetainRule:
        from troposphere.dlm import CrossRegionCopyRetainRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CrossRegionCopyRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html
    Properties:
        - Name: TargetRegion
        - Name: Target
        - Name: DeprecateRule
        - Name: Encrypted
        - Name: CmkArn
        - Name: RetainRule
        - Name: CopyTags
    
    """
    
    TargetRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-targetregion""", alias="TargetRegion")
    Target_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-target""", alias="Target")
    DeprecateRule_: Optional['CrossRegionCopyDeprecateRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-deprecaterule""", alias="DeprecateRule")
    Encrypted_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-encrypted""", alias="Encrypted")
    CmkArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-cmkarn""", alias="CmkArn")
    RetainRule_: Optional['CrossRegionCopyRetainRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-retainrule""", alias="RetainRule")
    CopyTags_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-copytags""", alias="CopyTags")
    


    @property
    def tropo_type(self) -> troposphere.dlm.CrossRegionCopyRule:
        from troposphere.dlm import CrossRegionCopyRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeprecateRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html
    Properties:
        - Name: IntervalUnit
        - Name: Count
        - Name: Interval
    
    """
    
    IntervalUnit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-intervalunit""", alias="IntervalUnit")
    Count_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-count""", alias="Count")
    Interval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-interval""", alias="Interval")
    


    @property
    def tropo_type(self) -> troposphere.dlm.DeprecateRule:
        from troposphere.dlm import DeprecateRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html
    Properties:
        - Name: Encrypted
        - Name: CmkArn
    
    """
    
    Encrypted_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html#cfn-dlm-lifecyclepolicy-encryptionconfiguration-encrypted""", alias="Encrypted")
    CmkArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html#cfn-dlm-lifecyclepolicy-encryptionconfiguration-cmkarn""", alias="CmkArn")
    


    @property
    def tropo_type(self) -> troposphere.dlm.EncryptionConfiguration:
        from troposphere.dlm import EncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EventParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html
    Properties:
        - Name: EventType
        - Name: SnapshotOwner
        - Name: DescriptionRegex
    
    """
    
    EventType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-eventtype""", alias="EventType")
    SnapshotOwner_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-snapshotowner""", alias="SnapshotOwner")
    DescriptionRegex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-descriptionregex""", alias="DescriptionRegex")
    


    @property
    def tropo_type(self) -> troposphere.dlm.EventParameters:
        from troposphere.dlm import EventParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EventSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html
    Properties:
        - Name: Type
        - Name: Parameters
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html#cfn-dlm-lifecyclepolicy-eventsource-type""", alias="Type")
    Parameters_: Optional['EventParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html#cfn-dlm-lifecyclepolicy-eventsource-parameters""", alias="Parameters")
    


    @property
    def tropo_type(self) -> troposphere.dlm.EventSource:
        from troposphere.dlm import EventSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FastRestoreRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html
    Properties:
        - Name: IntervalUnit
        - Name: AvailabilityZones
        - Name: Count
        - Name: Interval
    
    """
    
    IntervalUnit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-intervalunit""", alias="IntervalUnit")
    AvailabilityZones_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-availabilityzones""", alias="AvailabilityZones")
    Count_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-count""", alias="Count")
    Interval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-interval""", alias="Interval")
    


    @property
    def tropo_type(self) -> troposphere.dlm.FastRestoreRule:
        from troposphere.dlm import FastRestoreRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Parameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html
    Properties:
        - Name: ExcludeBootVolume
        - Name: ExcludeDataVolumeTags
        - Name: NoReboot
    
    """
    
    ExcludeBootVolume_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html#cfn-dlm-lifecyclepolicy-parameters-excludebootvolume""", alias="ExcludeBootVolume")
    ExcludeDataVolumeTags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html#cfn-dlm-lifecyclepolicy-parameters-excludedatavolumetags""", alias="ExcludeDataVolumeTags")
    NoReboot_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html#cfn-dlm-lifecyclepolicy-parameters-noreboot""", alias="NoReboot")
    


    @property
    def tropo_type(self) -> troposphere.dlm.Parameters:
        from troposphere.dlm import Parameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PolicyDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html
    Properties:
        - Name: ResourceTypes
        - Name: Schedules
        - Name: PolicyType
        - Name: EventSource
        - Name: Parameters
        - Name: Actions
        - Name: TargetTags
        - Name: ResourceLocations
    
    """
    
    ResourceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-resourcetypes""", alias="ResourceTypes")
    Schedules_: Optional[List['Schedule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-schedules""", alias="Schedules")
    PolicyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-policytype""", alias="PolicyType")
    EventSource_: Optional['EventSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-eventsource""", alias="EventSource")
    Parameters_: Optional['Parameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-parameters""", alias="Parameters")
    Actions_: Optional[List['Action']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-actions""", alias="Actions")
    TargetTags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-targettags""", alias="TargetTags")
    ResourceLocations_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-resourcelocations""", alias="ResourceLocations")
    


    @property
    def tropo_type(self) -> troposphere.dlm.PolicyDetails:
        from troposphere.dlm import PolicyDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RetainRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html
    Properties:
        - Name: IntervalUnit
        - Name: Count
        - Name: Interval
    
    """
    
    IntervalUnit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-intervalunit""", alias="IntervalUnit")
    Count_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-count""", alias="Count")
    Interval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-interval""", alias="Interval")
    


    @property
    def tropo_type(self) -> troposphere.dlm.RetainRule:
        from troposphere.dlm import RetainRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RetentionArchiveTier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retentionarchivetier.html
    Properties:
        - Name: IntervalUnit
        - Name: Count
        - Name: Interval
    
    """
    
    IntervalUnit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retentionarchivetier.html#cfn-dlm-lifecyclepolicy-retentionarchivetier-intervalunit""", alias="IntervalUnit")
    Count_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retentionarchivetier.html#cfn-dlm-lifecyclepolicy-retentionarchivetier-count""", alias="Count")
    Interval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retentionarchivetier.html#cfn-dlm-lifecyclepolicy-retentionarchivetier-interval""", alias="Interval")
    


    @property
    def tropo_type(self) -> troposphere.dlm.RetentionArchiveTier:
        from troposphere.dlm import RetentionArchiveTier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Schedule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html
    Properties:
        - Name: ShareRules
        - Name: DeprecateRule
        - Name: TagsToAdd
        - Name: CreateRule
        - Name: VariableTags
        - Name: FastRestoreRule
        - Name: ArchiveRule
        - Name: RetainRule
        - Name: CrossRegionCopyRules
        - Name: Name
        - Name: CopyTags
    
    """
    
    ShareRules_: Optional[List['ShareRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-sharerules""", alias="ShareRules")
    DeprecateRule_: Optional['DeprecateRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-deprecaterule""", alias="DeprecateRule")
    TagsToAdd_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-tagstoadd""", alias="TagsToAdd")
    CreateRule_: Optional['CreateRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-createrule""", alias="CreateRule")
    VariableTags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-variabletags""", alias="VariableTags")
    FastRestoreRule_: Optional['FastRestoreRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-fastrestorerule""", alias="FastRestoreRule")
    ArchiveRule_: Optional['ArchiveRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-archiverule""", alias="ArchiveRule")
    RetainRule_: Optional['RetainRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-retainrule""", alias="RetainRule")
    CrossRegionCopyRules_: Optional[List['CrossRegionCopyRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-crossregioncopyrules""", alias="CrossRegionCopyRules")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-name""", alias="Name")
    CopyTags_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-copytags""", alias="CopyTags")
    


    @property
    def tropo_type(self) -> troposphere.dlm.Schedule:
        from troposphere.dlm import Schedule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Script(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html
    Properties:
        - Name: ExecutionHandlerService
        - Name: ExecutionTimeout
        - Name: Stages
        - Name: ExecutionHandler
        - Name: MaximumRetryCount
        - Name: ExecuteOperationOnScriptFailure
    
    """
    
    ExecutionHandlerService_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html#cfn-dlm-lifecyclepolicy-script-executionhandlerservice""", alias="ExecutionHandlerService")
    ExecutionTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html#cfn-dlm-lifecyclepolicy-script-executiontimeout""", alias="ExecutionTimeout")
    Stages_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html#cfn-dlm-lifecyclepolicy-script-stages""", alias="Stages")
    ExecutionHandler_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html#cfn-dlm-lifecyclepolicy-script-executionhandler""", alias="ExecutionHandler")
    MaximumRetryCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html#cfn-dlm-lifecyclepolicy-script-maximumretrycount""", alias="MaximumRetryCount")
    ExecuteOperationOnScriptFailure_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html#cfn-dlm-lifecyclepolicy-script-executeoperationonscriptfailure""", alias="ExecuteOperationOnScriptFailure")
    


    @property
    def tropo_type(self) -> troposphere.dlm.Script:
        from troposphere.dlm import Script as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ShareRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html
    Properties:
        - Name: TargetAccounts
        - Name: UnshareIntervalUnit
        - Name: UnshareInterval
    
    """
    
    TargetAccounts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-targetaccounts""", alias="TargetAccounts")
    UnshareIntervalUnit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-unshareintervalunit""", alias="UnshareIntervalUnit")
    UnshareInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-unshareinterval""", alias="UnshareInterval")
    


    @property
    def tropo_type(self) -> troposphere.dlm.ShareRule:
        from troposphere.dlm import ShareRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class LifecyclePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html
    Properties:
        - Name: ExecutionRoleArn
        - Name: Description
        - Name: State
        - Name: PolicyDetails
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ExecutionRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-executionrolearn""", alias="ExecutionRoleArn")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-description""", alias="Description")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-state""", alias="State")
    PolicyDetails_: Optional['PolicyDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-policydetails""", alias="PolicyDetails")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.dlm.LifecyclePolicy:
        from troposphere.dlm import LifecyclePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.dlm import LifecyclePolicy as TropoT
        return resource_to_troposphere(self, TropoT)

