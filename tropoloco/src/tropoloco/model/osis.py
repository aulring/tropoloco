from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CloudWatchLogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-cloudwatchlogdestination.html
    Properties:
        - Name: LogGroup
    
    """
    
    LogGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-cloudwatchlogdestination.html#cfn-osis-pipeline-cloudwatchlogdestination-loggroup""", alias="LogGroup")
    


    @property
    def tropo_type(self) -> troposphere.osis.CloudWatchLogDestination:
        from troposphere.osis import CloudWatchLogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogPublishingOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-logpublishingoptions.html
    Properties:
        - Name: CloudWatchLogDestination
        - Name: IsLoggingEnabled
    
    """
    
    CloudWatchLogDestination_: Optional['CloudWatchLogDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-logpublishingoptions.html#cfn-osis-pipeline-logpublishingoptions-cloudwatchlogdestination""", alias="CloudWatchLogDestination")
    IsLoggingEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-logpublishingoptions.html#cfn-osis-pipeline-logpublishingoptions-isloggingenabled""", alias="IsLoggingEnabled")
    


    @property
    def tropo_type(self) -> troposphere.osis.LogPublishingOptions:
        from troposphere.osis import LogPublishingOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcendpoint.html
    Properties:
        - Name: VpcId
        - Name: VpcOptions
        - Name: VpcEndpointId
    
    """
    
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcendpoint.html#cfn-osis-pipeline-vpcendpoint-vpcid""", alias="VpcId")
    VpcOptions_: Optional['VpcOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcendpoint.html#cfn-osis-pipeline-vpcendpoint-vpcoptions""", alias="VpcOptions")
    VpcEndpointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcendpoint.html#cfn-osis-pipeline-vpcendpoint-vpcendpointid""", alias="VpcEndpointId")
    


    @property
    def tropo_type(self) -> troposphere.osis.VpcEndpoint:
        from troposphere.osis import VpcEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcoptions.html
    Properties:
        - Name: SecurityGroupIds
        - Name: SubnetIds
    
    """
    
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcoptions.html#cfn-osis-pipeline-vpcoptions-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcoptions.html#cfn-osis-pipeline-vpcoptions-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.osis.VpcOptions:
        from troposphere.osis import VpcOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Pipeline(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html
    Properties:
        - Name: PipelineConfigurationBody
        - Name: MinUnits
        - Name: PipelineName
        - Name: VpcOptions
        - Name: MaxUnits
        - Name: LogPublishingOptions
        - Name: Tags
    Attributes:
        - Name: PipelineArn
        - Name: VpcEndpoints
        - Name: IngestEndpointUrls
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PipelineConfigurationBody_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-pipelineconfigurationbody""", alias="PipelineConfigurationBody")
    MinUnits_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-minunits""", alias="MinUnits")
    PipelineName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-pipelinename""", alias="PipelineName")
    VpcOptions_: Optional['VpcOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-vpcoptions""", alias="VpcOptions")
    MaxUnits_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-maxunits""", alias="MaxUnits")
    LogPublishingOptions_: Optional['LogPublishingOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-logpublishingoptions""", alias="LogPublishingOptions")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.osis.Pipeline:
        from troposphere.osis import Pipeline as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.osis import Pipeline as TropoT
        return resource_to_troposphere(self, TropoT)

