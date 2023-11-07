from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AgentlessDialerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-agentlessdialerconfig.html
    Properties:
        - Name: DialingCapacity
    
    """
    
    DialingCapacity_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-agentlessdialerconfig.html#cfn-connectcampaigns-campaign-agentlessdialerconfig-dialingcapacity""", alias="DialingCapacity")
    


    @property
    def tropo_type(self) -> troposphere.connectcampaigns.AgentlessDialerConfig:
        from troposphere.connectcampaigns import AgentlessDialerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnswerMachineDetectionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-answermachinedetectionconfig.html
    Properties:
        - Name: EnableAnswerMachineDetection
    
    """
    
    EnableAnswerMachineDetection_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-answermachinedetectionconfig.html#cfn-connectcampaigns-campaign-answermachinedetectionconfig-enableanswermachinedetection""", alias="EnableAnswerMachineDetection")
    


    @property
    def tropo_type(self) -> troposphere.connectcampaigns.AnswerMachineDetectionConfig:
        from troposphere.connectcampaigns import AnswerMachineDetectionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DialerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-dialerconfig.html
    Properties:
        - Name: AgentlessDialerConfig
        - Name: PredictiveDialerConfig
        - Name: ProgressiveDialerConfig
    
    """
    
    AgentlessDialerConfig_: Optional['AgentlessDialerConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-dialerconfig.html#cfn-connectcampaigns-campaign-dialerconfig-agentlessdialerconfig""", alias="AgentlessDialerConfig")
    PredictiveDialerConfig_: Optional['PredictiveDialerConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-dialerconfig.html#cfn-connectcampaigns-campaign-dialerconfig-predictivedialerconfig""", alias="PredictiveDialerConfig")
    ProgressiveDialerConfig_: Optional['ProgressiveDialerConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-dialerconfig.html#cfn-connectcampaigns-campaign-dialerconfig-progressivedialerconfig""", alias="ProgressiveDialerConfig")
    


    @property
    def tropo_type(self) -> troposphere.connectcampaigns.DialerConfig:
        from troposphere.connectcampaigns import DialerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutboundCallConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-outboundcallconfig.html
    Properties:
        - Name: ConnectContactFlowArn
        - Name: ConnectQueueArn
        - Name: AnswerMachineDetectionConfig
        - Name: ConnectSourcePhoneNumber
    
    """
    
    ConnectContactFlowArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-outboundcallconfig.html#cfn-connectcampaigns-campaign-outboundcallconfig-connectcontactflowarn""", alias="ConnectContactFlowArn")
    ConnectQueueArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-outboundcallconfig.html#cfn-connectcampaigns-campaign-outboundcallconfig-connectqueuearn""", alias="ConnectQueueArn")
    AnswerMachineDetectionConfig_: Optional['AnswerMachineDetectionConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-outboundcallconfig.html#cfn-connectcampaigns-campaign-outboundcallconfig-answermachinedetectionconfig""", alias="AnswerMachineDetectionConfig")
    ConnectSourcePhoneNumber_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-outboundcallconfig.html#cfn-connectcampaigns-campaign-outboundcallconfig-connectsourcephonenumber""", alias="ConnectSourcePhoneNumber")
    


    @property
    def tropo_type(self) -> troposphere.connectcampaigns.OutboundCallConfig:
        from troposphere.connectcampaigns import OutboundCallConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PredictiveDialerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-predictivedialerconfig.html
    Properties:
        - Name: DialingCapacity
        - Name: BandwidthAllocation
    
    """
    
    DialingCapacity_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-predictivedialerconfig.html#cfn-connectcampaigns-campaign-predictivedialerconfig-dialingcapacity""", alias="DialingCapacity")
    BandwidthAllocation_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-predictivedialerconfig.html#cfn-connectcampaigns-campaign-predictivedialerconfig-bandwidthallocation""", alias="BandwidthAllocation")
    


    @property
    def tropo_type(self) -> troposphere.connectcampaigns.PredictiveDialerConfig:
        from troposphere.connectcampaigns import PredictiveDialerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProgressiveDialerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-progressivedialerconfig.html
    Properties:
        - Name: DialingCapacity
        - Name: BandwidthAllocation
    
    """
    
    DialingCapacity_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-progressivedialerconfig.html#cfn-connectcampaigns-campaign-progressivedialerconfig-dialingcapacity""", alias="DialingCapacity")
    BandwidthAllocation_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-progressivedialerconfig.html#cfn-connectcampaigns-campaign-progressivedialerconfig-bandwidthallocation""", alias="BandwidthAllocation")
    


    @property
    def tropo_type(self) -> troposphere.connectcampaigns.ProgressiveDialerConfig:
        from troposphere.connectcampaigns import ProgressiveDialerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Campaign(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html
    Properties:
        - Name: OutboundCallConfig
        - Name: ConnectInstanceArn
        - Name: DialerConfig
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OutboundCallConfig_: 'OutboundCallConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html#cfn-connectcampaigns-campaign-outboundcallconfig""", alias="OutboundCallConfig")
    ConnectInstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html#cfn-connectcampaigns-campaign-connectinstancearn""", alias="ConnectInstanceArn")
    DialerConfig_: 'DialerConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html#cfn-connectcampaigns-campaign-dialerconfig""", alias="DialerConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html#cfn-connectcampaigns-campaign-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html#cfn-connectcampaigns-campaign-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.connectcampaigns.Campaign:
        from troposphere.connectcampaigns import Campaign as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connectcampaigns import Campaign as TropoT
        return resource_to_troposphere(self, TropoT)

