from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class LoggingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingconfiguration.html
    Properties:
        - Name: LogGroupArn
    
    """
    
    LogGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingconfiguration.html#cfn-aps-workspace-loggingconfiguration-loggrouparn""", alias="LogGroupArn")
    


    @property
    def tropo_type(self) -> troposphere.aps.LoggingConfiguration:
        from troposphere.aps import LoggingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class RuleGroupsNamespace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html
    Properties:
        - Name: Data
        - Name: Tags
        - Name: Workspace
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Data_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-data""", alias="Data")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-tags""", alias="Tags")
    Workspace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-workspace""", alias="Workspace")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.aps.RuleGroupsNamespace:
        from troposphere.aps import RuleGroupsNamespace as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.aps import RuleGroupsNamespace as TropoT
        return resource_to_troposphere(self, TropoT)


class Workspace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html
    Properties:
        - Name: Alias
        - Name: LoggingConfiguration
        - Name: AlertManagerDefinition
        - Name: Tags
    Attributes:
        - Name: PrometheusEndpoint
        - Name: WorkspaceId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Alias_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-alias""", alias="Alias")
    LoggingConfiguration_: Optional['LoggingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-loggingconfiguration""", alias="LoggingConfiguration")
    AlertManagerDefinition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-alertmanagerdefinition""", alias="AlertManagerDefinition")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.aps.Workspace:
        from troposphere.aps import Workspace as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.aps import Workspace as TropoT
        return resource_to_troposphere(self, TropoT)

