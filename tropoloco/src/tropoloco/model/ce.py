from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ResourceTag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalymonitor-resourcetag.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalymonitor-resourcetag.html#cfn-ce-anomalymonitor-resourcetag-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalymonitor-resourcetag.html#cfn-ce-anomalymonitor-resourcetag-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.ce.ResourceTag:
        from troposphere.ce import ResourceTag as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceTag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-resourcetag.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-resourcetag.html#cfn-ce-anomalysubscription-resourcetag-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-resourcetag.html#cfn-ce-anomalysubscription-resourcetag-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.ce.ResourceTag:
        from troposphere.ce import ResourceTag as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Subscriber(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html
    Properties:
        - Name: Status
        - Name: Type
        - Name: Address
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html#cfn-ce-anomalysubscription-subscriber-status""", alias="Status")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html#cfn-ce-anomalysubscription-subscriber-type""", alias="Type")
    Address_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html#cfn-ce-anomalysubscription-subscriber-address""", alias="Address")
    


    @property
    def tropo_type(self) -> troposphere.ce.Subscriber:
        from troposphere.ce import Subscriber as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AnomalyMonitor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html
    Properties:
        - Name: MonitorType
        - Name: ResourceTags
        - Name: MonitorName
        - Name: MonitorSpecification
        - Name: MonitorDimension
    Attributes:
        - Name: LastUpdatedDate
        - Name: CreationDate
        - Name: LastEvaluatedDate
        - Name: MonitorArn
        - Name: DimensionalValueCount
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MonitorType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitortype""", alias="MonitorType")
    ResourceTags_: Optional[List['ResourceTag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-resourcetags""", alias="ResourceTags")
    MonitorName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitorname""", alias="MonitorName")
    MonitorSpecification_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitorspecification""", alias="MonitorSpecification")
    MonitorDimension_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitordimension""", alias="MonitorDimension")
    

    @property
    def tropo_type(self) -> troposphere.ce.AnomalyMonitor:
        from troposphere.ce import AnomalyMonitor as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ce import AnomalyMonitor as TropoT
        return resource_to_troposphere(self, TropoT)


class AnomalySubscription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html
    Properties:
        - Name: MonitorArnList
        - Name: ResourceTags
        - Name: Frequency
        - Name: SubscriptionName
        - Name: Subscribers
        - Name: Threshold
        - Name: ThresholdExpression
    Attributes:
        - Name: AccountId
        - Name: SubscriptionArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MonitorArnList_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-monitorarnlist""", alias="MonitorArnList")
    ResourceTags_: Optional[List['ResourceTag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-resourcetags""", alias="ResourceTags")
    Frequency_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-frequency""", alias="Frequency")
    SubscriptionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-subscriptionname""", alias="SubscriptionName")
    Subscribers_: List['Subscriber'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-subscribers""", alias="Subscribers")
    Threshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-threshold""", alias="Threshold")
    ThresholdExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-thresholdexpression""", alias="ThresholdExpression")
    

    @property
    def tropo_type(self) -> troposphere.ce.AnomalySubscription:
        from troposphere.ce import AnomalySubscription as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ce import AnomalySubscription as TropoT
        return resource_to_troposphere(self, TropoT)


class CostCategory(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html
    Properties:
        - Name: DefaultValue
        - Name: SplitChargeRules
        - Name: RuleVersion
        - Name: Rules
        - Name: Name
    Attributes:
        - Name: EffectiveStart
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DefaultValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-defaultvalue""", alias="DefaultValue")
    SplitChargeRules_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-splitchargerules""", alias="SplitChargeRules")
    RuleVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-ruleversion""", alias="RuleVersion")
    Rules_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-rules""", alias="Rules")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ce.CostCategory:
        from troposphere.ce import CostCategory as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ce import CostCategory as TropoT
        return resource_to_troposphere(self, TropoT)

