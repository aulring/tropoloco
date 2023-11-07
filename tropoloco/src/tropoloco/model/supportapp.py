from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################




######################################################################
# AWS Resource
######################################################################


class AccountAlias(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-accountalias.html
    Properties:
        - Name: AccountAlias
    Attributes:
        - Name: AccountAliasResourceId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AccountAlias_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-accountalias.html#cfn-supportapp-accountalias-accountalias""", alias="AccountAlias")
    

    @property
    def tropo_type(self) -> troposphere.supportapp.AccountAlias:
        from troposphere.supportapp import AccountAlias as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.supportapp import AccountAlias as TropoT
        return resource_to_troposphere(self, TropoT)


class SlackChannelConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html
    Properties:
        - Name: ChannelName
        - Name: NotifyOnAddCorrespondenceToCase
        - Name: ChannelRoleArn
        - Name: NotifyOnResolveCase
        - Name: NotifyOnCaseSeverity
        - Name: TeamId
        - Name: ChannelId
        - Name: NotifyOnCreateOrReopenCase
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ChannelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-channelname""", alias="ChannelName")
    NotifyOnAddCorrespondenceToCase_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-notifyonaddcorrespondencetocase""", alias="NotifyOnAddCorrespondenceToCase")
    ChannelRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-channelrolearn""", alias="ChannelRoleArn")
    NotifyOnResolveCase_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-notifyonresolvecase""", alias="NotifyOnResolveCase")
    NotifyOnCaseSeverity_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-notifyoncaseseverity""", alias="NotifyOnCaseSeverity")
    TeamId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-teamid""", alias="TeamId")
    ChannelId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-channelid""", alias="ChannelId")
    NotifyOnCreateOrReopenCase_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html#cfn-supportapp-slackchannelconfiguration-notifyoncreateorreopencase""", alias="NotifyOnCreateOrReopenCase")
    

    @property
    def tropo_type(self) -> troposphere.supportapp.SlackChannelConfiguration:
        from troposphere.supportapp import SlackChannelConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.supportapp import SlackChannelConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class SlackWorkspaceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackworkspaceconfiguration.html
    Properties:
        - Name: VersionId
        - Name: TeamId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VersionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackworkspaceconfiguration.html#cfn-supportapp-slackworkspaceconfiguration-versionid""", alias="VersionId")
    TeamId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackworkspaceconfiguration.html#cfn-supportapp-slackworkspaceconfiguration-teamid""", alias="TeamId")
    

    @property
    def tropo_type(self) -> troposphere.supportapp.SlackWorkspaceConfiguration:
        from troposphere.supportapp import SlackWorkspaceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.supportapp import SlackWorkspaceConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)

