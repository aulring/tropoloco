from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AgentPermissions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeguruprofiler-profilinggroup-agentpermissions.html
    Properties:
        - Name: Principals
    
    """
    
    Principals_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeguruprofiler-profilinggroup-agentpermissions.html#cfn-codeguruprofiler-profilinggroup-agentpermissions-principals""", alias="Principals")
    


    @property
    def tropo_type(self) -> troposphere.codeguruprofiler.AgentPermissions:
        from troposphere.codeguruprofiler import AgentPermissions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Channel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeguruprofiler-profilinggroup-channel.html
    Properties:
        - Name: channelUri
        - Name: channelId
    
    """
    
    channelUri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeguruprofiler-profilinggroup-channel.html#cfn-codeguruprofiler-profilinggroup-channel-channeluri""", alias="channelUri")
    channelId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeguruprofiler-profilinggroup-channel.html#cfn-codeguruprofiler-profilinggroup-channel-channelid""", alias="channelId")
    


    @property
    def tropo_type(self) -> troposphere.codeguruprofiler.Channel:
        from troposphere.codeguruprofiler import Channel as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ProfilingGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html
    Properties:
        - Name: AnomalyDetectionNotificationConfiguration
        - Name: AgentPermissions
        - Name: ComputePlatform
        - Name: ProfilingGroupName
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AnomalyDetectionNotificationConfiguration_: Optional[List['Channel']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html#cfn-codeguruprofiler-profilinggroup-anomalydetectionnotificationconfiguration""", alias="AnomalyDetectionNotificationConfiguration")
    AgentPermissions_: Optional['AgentPermissions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html#cfn-codeguruprofiler-profilinggroup-agentpermissions""", alias="AgentPermissions")
    ComputePlatform_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html#cfn-codeguruprofiler-profilinggroup-computeplatform""", alias="ComputePlatform")
    ProfilingGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html#cfn-codeguruprofiler-profilinggroup-profilinggroupname""", alias="ProfilingGroupName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html#cfn-codeguruprofiler-profilinggroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.codeguruprofiler.ProfilingGroup:
        from troposphere.codeguruprofiler import ProfilingGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codeguruprofiler import ProfilingGroup as TropoT
        return resource_to_troposphere(self, TropoT)

