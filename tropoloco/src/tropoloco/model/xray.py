from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class InsightsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-group-insightsconfiguration.html
    Properties:
        - Name: NotificationsEnabled
        - Name: InsightsEnabled
    
    """
    
    NotificationsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-group-insightsconfiguration.html#cfn-xray-group-insightsconfiguration-notificationsenabled""", alias="NotificationsEnabled")
    InsightsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-group-insightsconfiguration.html#cfn-xray-group-insightsconfiguration-insightsenabled""", alias="InsightsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.xray.InsightsConfiguration:
        from troposphere.xray import InsightsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SamplingRuleProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html
    Properties:
        - Name: Priority
        - Name: ReservoirSize
        - Name: RuleARN
        - Name: URLPath
        - Name: Attributes
        - Name: FixedRate
        - Name: Host
        - Name: ResourceARN
        - Name: HTTPMethod
        - Name: ServiceName
        - Name: Version
        - Name: ServiceType
        - Name: RuleName
    
    """
    
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-priority""", alias="Priority")
    ReservoirSize_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-reservoirsize""", alias="ReservoirSize")
    RuleARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-rulearn""", alias="RuleARN")
    URLPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-urlpath""", alias="URLPath")
    Attributes_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-attributes""", alias="Attributes")
    FixedRate_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-fixedrate""", alias="FixedRate")
    Host_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-host""", alias="Host")
    ResourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-resourcearn""", alias="ResourceARN")
    HTTPMethod_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-httpmethod""", alias="HTTPMethod")
    ServiceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-servicename""", alias="ServiceName")
    Version_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-version""", alias="Version")
    ServiceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-servicetype""", alias="ServiceType")
    RuleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html#cfn-xray-samplingrule-samplingrule-rulename""", alias="RuleName")
    


    @property
    def tropo_type(self) -> troposphere.xray.SamplingRuleProperty:
        from troposphere.xray import SamplingRuleProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Group(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html
    Properties:
        - Name: GroupName
        - Name: InsightsConfiguration
        - Name: FilterExpression
        - Name: Tags
    Attributes:
        - Name: GroupARN
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-groupname""", alias="GroupName")
    InsightsConfiguration_: Optional['InsightsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-insightsconfiguration""", alias="InsightsConfiguration")
    FilterExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-filterexpression""", alias="FilterExpression")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html#cfn-xray-group-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.xray.Group:
        from troposphere.xray import Group as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.xray import Group as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourcePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html
    Properties:
        - Name: BypassPolicyLockoutCheck
        - Name: PolicyName
        - Name: PolicyDocument
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BypassPolicyLockoutCheck_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html#cfn-xray-resourcepolicy-bypasspolicylockoutcheck""", alias="BypassPolicyLockoutCheck")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html#cfn-xray-resourcepolicy-policyname""", alias="PolicyName")
    PolicyDocument_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html#cfn-xray-resourcepolicy-policydocument""", alias="PolicyDocument")
    

    @property
    def tropo_type(self) -> troposphere.xray.ResourcePolicy:
        from troposphere.xray import ResourcePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.xray import ResourcePolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class SamplingRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html
    Properties:
        - Name: SamplingRule
        - Name: Tags
    Attributes:
        - Name: RuleARN
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SamplingRule_: Optional['SamplingRuleProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-samplingrule""", alias="SamplingRule")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html#cfn-xray-samplingrule-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.xray.SamplingRule:
        from troposphere.xray import SamplingRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.xray import SamplingRule as TropoT
        return resource_to_troposphere(self, TropoT)

