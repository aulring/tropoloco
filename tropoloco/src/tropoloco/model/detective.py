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


class Graph(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html
    Properties:
        - Name: AutoEnableMembers
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AutoEnableMembers_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html#cfn-detective-graph-autoenablemembers""", alias="AutoEnableMembers")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html#cfn-detective-graph-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.detective.Graph:
        from troposphere.detective import Graph as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.detective import Graph as TropoT
        return resource_to_troposphere(self, TropoT)


class MemberInvitation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html
    Properties:
        - Name: MemberId
        - Name: Message
        - Name: GraphArn
        - Name: DisableEmailNotification
        - Name: MemberEmailAddress
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MemberId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-memberid""", alias="MemberId")
    Message_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-message""", alias="Message")
    GraphArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-grapharn""", alias="GraphArn")
    DisableEmailNotification_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-disableemailnotification""", alias="DisableEmailNotification")
    MemberEmailAddress_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-memberemailaddress""", alias="MemberEmailAddress")
    

    @property
    def tropo_type(self) -> troposphere.detective.MemberInvitation:
        from troposphere.detective import MemberInvitation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.detective import MemberInvitation as TropoT
        return resource_to_troposphere(self, TropoT)


class OrganizationAdmin(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-organizationadmin.html
    Properties:
        - Name: AccountId
    Attributes:
        - Name: GraphArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AccountId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-organizationadmin.html#cfn-detective-organizationadmin-accountid""", alias="AccountId")
    

    @property
    def tropo_type(self) -> troposphere.detective.OrganizationAdmin:
        from troposphere.detective import OrganizationAdmin as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.detective import OrganizationAdmin as TropoT
        return resource_to_troposphere(self, TropoT)

