from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ClusterEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html
    Properties:
        - Name: Endpoint
        - Name: Region
    
    """
    
    Endpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html#cfn-route53recoverycontrol-cluster-clusterendpoint-endpoint""", alias="Endpoint")
    Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html#cfn-route53recoverycontrol-cluster-clusterendpoint-region""", alias="Region")
    


    @property
    def tropo_type(self) -> troposphere.route53recoverycontrol.ClusterEndpoint:
        from troposphere.route53recoverycontrol import ClusterEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssertionRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html
    Properties:
        - Name: AssertedControls
        - Name: WaitPeriodMs
    
    """
    
    AssertedControls_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule-assertedcontrols""", alias="AssertedControls")
    WaitPeriodMs_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule-waitperiodms""", alias="WaitPeriodMs")
    


    @property
    def tropo_type(self) -> troposphere.route53recoverycontrol.AssertionRule:
        from troposphere.route53recoverycontrol import AssertionRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GatingRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html
    Properties:
        - Name: TargetControls
        - Name: GatingControls
        - Name: WaitPeriodMs
    
    """
    
    TargetControls_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-targetcontrols""", alias="TargetControls")
    GatingControls_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-gatingcontrols""", alias="GatingControls")
    WaitPeriodMs_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-waitperiodms""", alias="WaitPeriodMs")
    


    @property
    def tropo_type(self) -> troposphere.route53recoverycontrol.GatingRule:
        from troposphere.route53recoverycontrol import GatingRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html
    Properties:
        - Name: Type
        - Name: Inverted
        - Name: Threshold
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-type""", alias="Type")
    Inverted_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-inverted""", alias="Inverted")
    Threshold_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-threshold""", alias="Threshold")
    


    @property
    def tropo_type(self) -> troposphere.route53recoverycontrol.RuleConfig:
        from troposphere.route53recoverycontrol import RuleConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Cluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html
    Properties:
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ClusterArn
        - Name: Status
        - Name: ClusterEndpoints
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html#cfn-route53recoverycontrol-cluster-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html#cfn-route53recoverycontrol-cluster-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53recoverycontrol.Cluster:
        from troposphere.route53recoverycontrol import Cluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53recoverycontrol import Cluster as TropoT
        return resource_to_troposphere(self, TropoT)


class ControlPanel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html
    Properties:
        - Name: ClusterArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: ControlPanelArn
        - Name: DefaultControlPanel
        - Name: RoutingControlCount
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ClusterArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-clusterarn""", alias="ClusterArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53recoverycontrol.ControlPanel:
        from troposphere.route53recoverycontrol import ControlPanel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53recoverycontrol import ControlPanel as TropoT
        return resource_to_troposphere(self, TropoT)


class RoutingControl(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html
    Properties:
        - Name: ClusterArn
        - Name: ControlPanelArn
        - Name: Name
    Attributes:
        - Name: Status
        - Name: RoutingControlArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ClusterArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-clusterarn""", alias="ClusterArn")
    ControlPanelArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-controlpanelarn""", alias="ControlPanelArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53recoverycontrol.RoutingControl:
        from troposphere.route53recoverycontrol import RoutingControl as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53recoverycontrol import RoutingControl as TropoT
        return resource_to_troposphere(self, TropoT)


class SafetyRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html
    Properties:
        - Name: ControlPanelArn
        - Name: AssertionRule
        - Name: RuleConfig
        - Name: GatingRule
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: SafetyRuleArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ControlPanelArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-controlpanelarn""", alias="ControlPanelArn")
    AssertionRule_: Optional['AssertionRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule""", alias="AssertionRule")
    RuleConfig_: 'RuleConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-ruleconfig""", alias="RuleConfig")
    GatingRule_: Optional['GatingRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule""", alias="GatingRule")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53recoverycontrol.SafetyRule:
        from troposphere.route53recoverycontrol import SafetyRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53recoverycontrol import SafetyRule as TropoT
        return resource_to_troposphere(self, TropoT)

