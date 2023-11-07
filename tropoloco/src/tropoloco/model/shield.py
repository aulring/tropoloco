from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class EmergencyContact(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-proactiveengagement-emergencycontact.html
    Properties:
        - Name: ContactNotes
        - Name: PhoneNumber
        - Name: EmailAddress
    
    """
    
    ContactNotes_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-proactiveengagement-emergencycontact.html#cfn-shield-proactiveengagement-emergencycontact-contactnotes""", alias="ContactNotes")
    PhoneNumber_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-proactiveengagement-emergencycontact.html#cfn-shield-proactiveengagement-emergencycontact-phonenumber""", alias="PhoneNumber")
    EmailAddress_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-proactiveengagement-emergencycontact.html#cfn-shield-proactiveengagement-emergencycontact-emailaddress""", alias="EmailAddress")
    


    @property
    def tropo_type(self) -> troposphere.shield.EmergencyContact:
        from troposphere.shield import EmergencyContact as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-protection-action.html
    Properties:
        - Name: Block
        - Name: Count
    
    """
    
    Block_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-protection-action.html#cfn-shield-protection-action-block""", alias="Block")
    Count_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-protection-action.html#cfn-shield-protection-action-count""", alias="Count")
    


    @property
    def tropo_type(self) -> troposphere.shield.Action:
        from troposphere.shield import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ApplicationLayerAutomaticResponseConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-protection-applicationlayerautomaticresponseconfiguration.html
    Properties:
        - Name: Status
        - Name: Action
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-protection-applicationlayerautomaticresponseconfiguration.html#cfn-shield-protection-applicationlayerautomaticresponseconfiguration-status""", alias="Status")
    Action_: 'Action' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-protection-applicationlayerautomaticresponseconfiguration.html#cfn-shield-protection-applicationlayerautomaticresponseconfiguration-action""", alias="Action")
    


    @property
    def tropo_type(self) -> troposphere.shield.ApplicationLayerAutomaticResponseConfiguration:
        from troposphere.shield import ApplicationLayerAutomaticResponseConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class DRTAccess(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-drtaccess.html
    Properties:
        - Name: LogBucketList
        - Name: RoleArn
    Attributes:
        - Name: AccountId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LogBucketList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-drtaccess.html#cfn-shield-drtaccess-logbucketlist""", alias="LogBucketList")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-drtaccess.html#cfn-shield-drtaccess-rolearn""", alias="RoleArn")
    

    @property
    def tropo_type(self) -> troposphere.shield.DRTAccess:
        from troposphere.shield import DRTAccess as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.shield import DRTAccess as TropoT
        return resource_to_troposphere(self, TropoT)


class ProactiveEngagement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-proactiveengagement.html
    Properties:
        - Name: ProactiveEngagementStatus
        - Name: EmergencyContactList
    Attributes:
        - Name: AccountId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ProactiveEngagementStatus_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-proactiveengagement.html#cfn-shield-proactiveengagement-proactiveengagementstatus""", alias="ProactiveEngagementStatus")
    EmergencyContactList_: List['EmergencyContact'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-proactiveengagement.html#cfn-shield-proactiveengagement-emergencycontactlist""", alias="EmergencyContactList")
    

    @property
    def tropo_type(self) -> troposphere.shield.ProactiveEngagement:
        from troposphere.shield import ProactiveEngagement as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.shield import ProactiveEngagement as TropoT
        return resource_to_troposphere(self, TropoT)


class Protection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.html
    Properties:
        - Name: ResourceArn
        - Name: HealthCheckArns
        - Name: ApplicationLayerAutomaticResponseConfiguration
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ProtectionArn
        - Name: ProtectionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.html#cfn-shield-protection-resourcearn""", alias="ResourceArn")
    HealthCheckArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.html#cfn-shield-protection-healthcheckarns""", alias="HealthCheckArns")
    ApplicationLayerAutomaticResponseConfiguration_: Optional['ApplicationLayerAutomaticResponseConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.html#cfn-shield-protection-applicationlayerautomaticresponseconfiguration""", alias="ApplicationLayerAutomaticResponseConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.html#cfn-shield-protection-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.html#cfn-shield-protection-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.shield.Protection:
        from troposphere.shield import Protection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.shield import Protection as TropoT
        return resource_to_troposphere(self, TropoT)


class ProtectionGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html
    Properties:
        - Name: Aggregation
        - Name: Pattern
        - Name: ProtectionGroupId
        - Name: ResourceType
        - Name: Members
        - Name: Tags
    Attributes:
        - Name: ProtectionGroupArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Aggregation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html#cfn-shield-protectiongroup-aggregation""", alias="Aggregation")
    Pattern_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html#cfn-shield-protectiongroup-pattern""", alias="Pattern")
    ProtectionGroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html#cfn-shield-protectiongroup-protectiongroupid""", alias="ProtectionGroupId")
    ResourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html#cfn-shield-protectiongroup-resourcetype""", alias="ResourceType")
    Members_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html#cfn-shield-protectiongroup-members""", alias="Members")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html#cfn-shield-protectiongroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.shield.ProtectionGroup:
        from troposphere.shield import ProtectionGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.shield import ProtectionGroup as TropoT
        return resource_to_troposphere(self, TropoT)

