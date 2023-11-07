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


class MicrosoftTeamsChannelConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html
    Properties:
        - Name: UserRoleRequired
        - Name: LoggingLevel
        - Name: SnsTopicArns
        - Name: GuardrailPolicies
        - Name: IamRoleArn
        - Name: TeamId
        - Name: ConfigurationName
        - Name: TeamsTenantId
        - Name: TeamsChannelId
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UserRoleRequired_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-userrolerequired""", alias="UserRoleRequired")
    LoggingLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-logginglevel""", alias="LoggingLevel")
    SnsTopicArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-snstopicarns""", alias="SnsTopicArns")
    GuardrailPolicies_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-guardrailpolicies""", alias="GuardrailPolicies")
    IamRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-iamrolearn""", alias="IamRoleArn")
    TeamId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-teamid""", alias="TeamId")
    ConfigurationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-configurationname""", alias="ConfigurationName")
    TeamsTenantId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-teamstenantid""", alias="TeamsTenantId")
    TeamsChannelId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-teamschannelid""", alias="TeamsChannelId")
    

    @property
    def tropo_type(self) -> troposphere.chatbot.MicrosoftTeamsChannelConfiguration:
        from troposphere.chatbot import MicrosoftTeamsChannelConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.chatbot import MicrosoftTeamsChannelConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class SlackChannelConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html
    Properties:
        - Name: UserRoleRequired
        - Name: LoggingLevel
        - Name: SnsTopicArns
        - Name: GuardrailPolicies
        - Name: SlackWorkspaceId
        - Name: SlackChannelId
        - Name: IamRoleArn
        - Name: ConfigurationName
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UserRoleRequired_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-userrolerequired""", alias="UserRoleRequired")
    LoggingLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-logginglevel""", alias="LoggingLevel")
    SnsTopicArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-snstopicarns""", alias="SnsTopicArns")
    GuardrailPolicies_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-guardrailpolicies""", alias="GuardrailPolicies")
    SlackWorkspaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackworkspaceid""", alias="SlackWorkspaceId")
    SlackChannelId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackchannelid""", alias="SlackChannelId")
    IamRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-iamrolearn""", alias="IamRoleArn")
    ConfigurationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-configurationname""", alias="ConfigurationName")
    

    @property
    def tropo_type(self) -> troposphere.chatbot.SlackChannelConfiguration:
        from troposphere.chatbot import SlackChannelConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.chatbot import SlackChannelConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)

