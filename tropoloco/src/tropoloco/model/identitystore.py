from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class MemberId(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-groupmembership-memberid.html
    Properties:
        - Name: UserId
    
    """
    
    UserId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-groupmembership-memberid.html#cfn-identitystore-groupmembership-memberid-userid""", alias="UserId")
    


    @property
    def tropo_type(self) -> troposphere.identitystore.MemberId:
        from troposphere.identitystore import MemberId as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Group(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html
    Properties:
        - Name: Description
        - Name: DisplayName
        - Name: IdentityStoreId
    Attributes:
        - Name: GroupId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-description""", alias="Description")
    DisplayName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-displayname""", alias="DisplayName")
    IdentityStoreId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-identitystoreid""", alias="IdentityStoreId")
    

    @property
    def tropo_type(self) -> troposphere.identitystore.Group:
        from troposphere.identitystore import Group as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.identitystore import Group as TropoT
        return resource_to_troposphere(self, TropoT)


class GroupMembership(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html
    Properties:
        - Name: MemberId
        - Name: IdentityStoreId
        - Name: GroupId
    Attributes:
        - Name: MembershipId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MemberId_: 'MemberId' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-memberid""", alias="MemberId")
    IdentityStoreId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-identitystoreid""", alias="IdentityStoreId")
    GroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-groupid""", alias="GroupId")
    

    @property
    def tropo_type(self) -> troposphere.identitystore.GroupMembership:
        from troposphere.identitystore import GroupMembership as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.identitystore import GroupMembership as TropoT
        return resource_to_troposphere(self, TropoT)

