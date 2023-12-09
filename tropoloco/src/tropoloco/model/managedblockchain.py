from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ApprovalThresholdPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-approvalthresholdpolicy.html
    Properties:
        - Name: ThresholdComparator
        - Name: ThresholdPercentage
        - Name: ProposalDurationInHours
    
    """
    
    ThresholdComparator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-approvalthresholdpolicy.html#cfn-managedblockchain-member-approvalthresholdpolicy-thresholdcomparator""", alias="ThresholdComparator")
    ThresholdPercentage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-approvalthresholdpolicy.html#cfn-managedblockchain-member-approvalthresholdpolicy-thresholdpercentage""", alias="ThresholdPercentage")
    ProposalDurationInHours_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-approvalthresholdpolicy.html#cfn-managedblockchain-member-approvalthresholdpolicy-proposaldurationinhours""", alias="ProposalDurationInHours")
    


    @property
    def tropo_type(self) -> troposphere.managedblockchain.ApprovalThresholdPolicy:
        from troposphere.managedblockchain import ApprovalThresholdPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MemberConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberconfiguration.html
    Properties:
        - Name: Description
        - Name: MemberFrameworkConfiguration
        - Name: Name
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberconfiguration.html#cfn-managedblockchain-member-memberconfiguration-description""", alias="Description")
    MemberFrameworkConfiguration_: Optional['MemberFrameworkConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberconfiguration.html#cfn-managedblockchain-member-memberconfiguration-memberframeworkconfiguration""", alias="MemberFrameworkConfiguration")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberconfiguration.html#cfn-managedblockchain-member-memberconfiguration-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.managedblockchain.MemberConfiguration:
        from troposphere.managedblockchain import MemberConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MemberFabricConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberfabricconfiguration.html
    Properties:
        - Name: AdminUsername
        - Name: AdminPassword
    
    """
    
    AdminUsername_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberfabricconfiguration.html#cfn-managedblockchain-member-memberfabricconfiguration-adminusername""", alias="AdminUsername")
    AdminPassword_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberfabricconfiguration.html#cfn-managedblockchain-member-memberfabricconfiguration-adminpassword""", alias="AdminPassword")
    


    @property
    def tropo_type(self) -> troposphere.managedblockchain.MemberFabricConfiguration:
        from troposphere.managedblockchain import MemberFabricConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MemberFrameworkConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberframeworkconfiguration.html
    Properties:
        - Name: MemberFabricConfiguration
    
    """
    
    MemberFabricConfiguration_: Optional['MemberFabricConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberframeworkconfiguration.html#cfn-managedblockchain-member-memberframeworkconfiguration-memberfabricconfiguration""", alias="MemberFabricConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.managedblockchain.MemberFrameworkConfiguration:
        from troposphere.managedblockchain import MemberFrameworkConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html
    Properties:
        - Name: Description
        - Name: FrameworkVersion
        - Name: VotingPolicy
        - Name: Framework
        - Name: Name
        - Name: NetworkFrameworkConfiguration
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html#cfn-managedblockchain-member-networkconfiguration-description""", alias="Description")
    FrameworkVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html#cfn-managedblockchain-member-networkconfiguration-frameworkversion""", alias="FrameworkVersion")
    VotingPolicy_: 'VotingPolicy' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html#cfn-managedblockchain-member-networkconfiguration-votingpolicy""", alias="VotingPolicy")
    Framework_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html#cfn-managedblockchain-member-networkconfiguration-framework""", alias="Framework")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html#cfn-managedblockchain-member-networkconfiguration-name""", alias="Name")
    NetworkFrameworkConfiguration_: Optional['NetworkFrameworkConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html#cfn-managedblockchain-member-networkconfiguration-networkframeworkconfiguration""", alias="NetworkFrameworkConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.managedblockchain.NetworkConfiguration:
        from troposphere.managedblockchain import NetworkConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkFabricConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkfabricconfiguration.html
    Properties:
        - Name: Edition
    
    """
    
    Edition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkfabricconfiguration.html#cfn-managedblockchain-member-networkfabricconfiguration-edition""", alias="Edition")
    


    @property
    def tropo_type(self) -> troposphere.managedblockchain.NetworkFabricConfiguration:
        from troposphere.managedblockchain import NetworkFabricConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkFrameworkConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkframeworkconfiguration.html
    Properties:
        - Name: NetworkFabricConfiguration
    
    """
    
    NetworkFabricConfiguration_: Optional['NetworkFabricConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkframeworkconfiguration.html#cfn-managedblockchain-member-networkframeworkconfiguration-networkfabricconfiguration""", alias="NetworkFabricConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.managedblockchain.NetworkFrameworkConfiguration:
        from troposphere.managedblockchain import NetworkFrameworkConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VotingPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-votingpolicy.html
    Properties:
        - Name: ApprovalThresholdPolicy
    
    """
    
    ApprovalThresholdPolicy_: Optional['ApprovalThresholdPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-votingpolicy.html#cfn-managedblockchain-member-votingpolicy-approvalthresholdpolicy""", alias="ApprovalThresholdPolicy")
    


    @property
    def tropo_type(self) -> troposphere.managedblockchain.VotingPolicy:
        from troposphere.managedblockchain import VotingPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NodeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-node-nodeconfiguration.html
    Properties:
        - Name: AvailabilityZone
        - Name: InstanceType
    
    """
    
    AvailabilityZone_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-node-nodeconfiguration.html#cfn-managedblockchain-node-nodeconfiguration-availabilityzone""", alias="AvailabilityZone")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-node-nodeconfiguration.html#cfn-managedblockchain-node-nodeconfiguration-instancetype""", alias="InstanceType")
    


    @property
    def tropo_type(self) -> troposphere.managedblockchain.NodeConfiguration:
        from troposphere.managedblockchain import NodeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Accessor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-accessor.html
    Properties:
        - Name: NetworkType
        - Name: Tags
        - Name: AccessorType
    Attributes:
        - Name: Status
        - Name: CreationDate
        - Name: BillingToken
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NetworkType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-accessor.html#cfn-managedblockchain-accessor-networktype""", alias="NetworkType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-accessor.html#cfn-managedblockchain-accessor-tags""", alias="Tags")
    AccessorType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-accessor.html#cfn-managedblockchain-accessor-accessortype""", alias="AccessorType")
    

    @property
    def tropo_type(self) -> troposphere.managedblockchain.Accessor:
        from troposphere.managedblockchain import Accessor as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.managedblockchain import Accessor as TropoT
        return resource_to_troposphere(self, TropoT)


class Member(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html
    Properties:
        - Name: MemberConfiguration
        - Name: NetworkConfiguration
        - Name: NetworkId
        - Name: InvitationId
    Attributes:
        - Name: MemberId
        - Name: NetworkId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MemberConfiguration_: 'MemberConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html#cfn-managedblockchain-member-memberconfiguration""", alias="MemberConfiguration")
    NetworkConfiguration_: Optional['NetworkConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html#cfn-managedblockchain-member-networkconfiguration""", alias="NetworkConfiguration")
    NetworkId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html#cfn-managedblockchain-member-networkid""", alias="NetworkId")
    InvitationId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html#cfn-managedblockchain-member-invitationid""", alias="InvitationId")
    

    @property
    def tropo_type(self) -> troposphere.managedblockchain.Member:
        from troposphere.managedblockchain import Member as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.managedblockchain import Member as TropoT
        return resource_to_troposphere(self, TropoT)


class Node(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html
    Properties:
        - Name: MemberId
        - Name: NetworkId
        - Name: NodeConfiguration
    Attributes:
        - Name: MemberId
        - Name: NodeId
        - Name: Arn
        - Name: NetworkId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MemberId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html#cfn-managedblockchain-node-memberid""", alias="MemberId")
    NetworkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html#cfn-managedblockchain-node-networkid""", alias="NetworkId")
    NodeConfiguration_: 'NodeConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html#cfn-managedblockchain-node-nodeconfiguration""", alias="NodeConfiguration")
    

    @property
    def tropo_type(self) -> troposphere.managedblockchain.Node:
        from troposphere.managedblockchain import Node as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.managedblockchain import Node as TropoT
        return resource_to_troposphere(self, TropoT)

