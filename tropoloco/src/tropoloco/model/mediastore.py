from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CorsRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html
    Properties:
        - Name: AllowedMethods
        - Name: AllowedOrigins
        - Name: ExposeHeaders
        - Name: MaxAgeSeconds
        - Name: AllowedHeaders
    
    """
    
    AllowedMethods_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-allowedmethods""", alias="AllowedMethods")
    AllowedOrigins_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-allowedorigins""", alias="AllowedOrigins")
    ExposeHeaders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-exposeheaders""", alias="ExposeHeaders")
    MaxAgeSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-maxageseconds""", alias="MaxAgeSeconds")
    AllowedHeaders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html#cfn-mediastore-container-corsrule-allowedheaders""", alias="AllowedHeaders")
    


    @property
    def tropo_type(self) -> troposphere.mediastore.CorsRule:
        from troposphere.mediastore import CorsRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicy.html
    Properties:
        - Name: ContainerLevelMetrics
        - Name: MetricPolicyRules
    
    """
    
    ContainerLevelMetrics_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicy.html#cfn-mediastore-container-metricpolicy-containerlevelmetrics""", alias="ContainerLevelMetrics")
    MetricPolicyRules_: Optional[List['MetricPolicyRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicy.html#cfn-mediastore-container-metricpolicy-metricpolicyrules""", alias="MetricPolicyRules")
    


    @property
    def tropo_type(self) -> troposphere.mediastore.MetricPolicy:
        from troposphere.mediastore import MetricPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricPolicyRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicyrule.html
    Properties:
        - Name: ObjectGroup
        - Name: ObjectGroupName
    
    """
    
    ObjectGroup_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicyrule.html#cfn-mediastore-container-metricpolicyrule-objectgroup""", alias="ObjectGroup")
    ObjectGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicyrule.html#cfn-mediastore-container-metricpolicyrule-objectgroupname""", alias="ObjectGroupName")
    


    @property
    def tropo_type(self) -> troposphere.mediastore.MetricPolicyRule:
        from troposphere.mediastore import MetricPolicyRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Container(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html
    Properties:
        - Name: Policy
        - Name: MetricPolicy
        - Name: ContainerName
        - Name: CorsPolicy
        - Name: LifecyclePolicy
        - Name: AccessLoggingEnabled
        - Name: Tags
    Attributes:
        - Name: Endpoint
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-policy""", alias="Policy")
    MetricPolicy_: Optional['MetricPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-metricpolicy""", alias="MetricPolicy")
    ContainerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-containername""", alias="ContainerName")
    CorsPolicy_: Optional[List['CorsRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-corspolicy""", alias="CorsPolicy")
    LifecyclePolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-lifecyclepolicy""", alias="LifecyclePolicy")
    AccessLoggingEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-accessloggingenabled""", alias="AccessLoggingEnabled")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html#cfn-mediastore-container-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.mediastore.Container:
        from troposphere.mediastore import Container as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediastore import Container as TropoT
        return resource_to_troposphere(self, TropoT)

