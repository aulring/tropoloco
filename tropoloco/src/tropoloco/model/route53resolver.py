from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class FirewallRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html
    Properties:
        - Name: Action
        - Name: Priority
        - Name: BlockOverrideDomain
        - Name: FirewallDomainListId
        - Name: BlockResponse
        - Name: BlockOverrideTtl
        - Name: BlockOverrideDnsType
    
    """
    
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-action""", alias="Action")
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-priority""", alias="Priority")
    BlockOverrideDomain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridedomain""", alias="BlockOverrideDomain")
    FirewallDomainListId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-firewalldomainlistid""", alias="FirewallDomainListId")
    BlockResponse_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockresponse""", alias="BlockResponse")
    BlockOverrideTtl_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridettl""", alias="BlockOverrideTtl")
    BlockOverrideDnsType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridednstype""", alias="BlockOverrideDnsType")
    


    @property
    def tropo_type(self) -> troposphere.route53resolver.FirewallRule:
        from troposphere.route53resolver import FirewallRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IpAddressRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html
    Properties:
        - Name: Ipv6
        - Name: Ip
        - Name: SubnetId
    
    """
    
    Ipv6_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-ipv6""", alias="Ipv6")
    Ip_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-ip""", alias="Ip")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-subnetid""", alias="SubnetId")
    


    @property
    def tropo_type(self) -> troposphere.route53resolver.IpAddressRequest:
        from troposphere.route53resolver import IpAddressRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetAddress(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html
    Properties:
        - Name: Ipv6
        - Name: Ip
        - Name: Port
        - Name: Protocol
    
    """
    
    Ipv6_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-ipv6""", alias="Ipv6")
    Ip_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-ip""", alias="Ip")
    Port_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-port""", alias="Port")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.route53resolver.TargetAddress:
        from troposphere.route53resolver import TargetAddress as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class FirewallDomainList(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html
    Properties:
        - Name: Domains
        - Name: DomainFileUrl
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: CreationTime
        - Name: ManagedOwnerName
        - Name: ModificationTime
        - Name: Id
        - Name: Arn
        - Name: CreatorRequestId
        - Name: StatusMessage
        - Name: DomainCount
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Domains_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-domains""", alias="Domains")
    DomainFileUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-domainfileurl""", alias="DomainFileUrl")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53resolver.FirewallDomainList:
        from troposphere.route53resolver import FirewallDomainList as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53resolver import FirewallDomainList as TropoT
        return resource_to_troposphere(self, TropoT)


class FirewallRuleGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html
    Properties:
        - Name: FirewallRules
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: RuleCount
        - Name: Status
        - Name: OwnerId
        - Name: CreationTime
        - Name: ShareStatus
        - Name: ModificationTime
        - Name: Id
        - Name: Arn
        - Name: CreatorRequestId
        - Name: StatusMessage
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FirewallRules_: Optional[List['FirewallRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-firewallrules""", alias="FirewallRules")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53resolver.FirewallRuleGroup:
        from troposphere.route53resolver import FirewallRuleGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53resolver import FirewallRuleGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class FirewallRuleGroupAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html
    Properties:
        - Name: VpcId
        - Name: FirewallRuleGroupId
        - Name: Priority
        - Name: MutationProtection
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: CreationTime
        - Name: ManagedOwnerName
        - Name: ModificationTime
        - Name: Id
        - Name: Arn
        - Name: CreatorRequestId
        - Name: StatusMessage
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-vpcid""", alias="VpcId")
    FirewallRuleGroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-firewallrulegroupid""", alias="FirewallRuleGroupId")
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-priority""", alias="Priority")
    MutationProtection_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-mutationprotection""", alias="MutationProtection")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53resolver.FirewallRuleGroupAssociation:
        from troposphere.route53resolver import FirewallRuleGroupAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53resolver import FirewallRuleGroupAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class OutpostResolver(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-outpostresolver.html
    Properties:
        - Name: InstanceCount
        - Name: OutpostArn
        - Name: PreferredInstanceType
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: CreationTime
        - Name: ModificationTime
        - Name: Id
        - Name: Arn
        - Name: CreatorRequestId
        - Name: StatusMessage
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InstanceCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-outpostresolver.html#cfn-route53resolver-outpostresolver-instancecount""", alias="InstanceCount")
    OutpostArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-outpostresolver.html#cfn-route53resolver-outpostresolver-outpostarn""", alias="OutpostArn")
    PreferredInstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-outpostresolver.html#cfn-route53resolver-outpostresolver-preferredinstancetype""", alias="PreferredInstanceType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-outpostresolver.html#cfn-route53resolver-outpostresolver-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-outpostresolver.html#cfn-route53resolver-outpostresolver-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53resolver.OutpostResolver:
        from troposphere.route53resolver import OutpostResolver as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53resolver import OutpostResolver as TropoT
        return resource_to_troposphere(self, TropoT)


class ResolverConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html
    Properties:
        - Name: ResourceId
        - Name: AutodefinedReverseFlag
    Attributes:
        - Name: OwnerId
        - Name: AutodefinedReverse
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html#cfn-route53resolver-resolverconfig-resourceid""", alias="ResourceId")
    AutodefinedReverseFlag_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html#cfn-route53resolver-resolverconfig-autodefinedreverseflag""", alias="AutodefinedReverseFlag")
    

    @property
    def tropo_type(self) -> troposphere.route53resolver.ResolverConfig:
        from troposphere.route53resolver import ResolverConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53resolver import ResolverConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class ResolverDNSSECConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html
    Properties:
        - Name: ResourceId
    Attributes:
        - Name: ValidationStatus
        - Name: OwnerId
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html#cfn-route53resolver-resolverdnssecconfig-resourceid""", alias="ResourceId")
    

    @property
    def tropo_type(self) -> troposphere.route53resolver.ResolverDNSSECConfig:
        from troposphere.route53resolver import ResolverDNSSECConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53resolver import ResolverDNSSECConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class ResolverEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html
    Properties:
        - Name: IpAddresses
        - Name: Protocols
        - Name: OutpostArn
        - Name: PreferredInstanceType
        - Name: ResolverEndpointType
        - Name: Direction
        - Name: SecurityGroupIds
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ResolverEndpointId
        - Name: IpAddressCount
        - Name: OutpostArn
        - Name: PreferredInstanceType
        - Name: ResolverEndpointType
        - Name: Arn
        - Name: Direction
        - Name: HostVPCId
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IpAddresses_: List['IpAddressRequest'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-ipaddresses""", alias="IpAddresses")
    Protocols_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-protocols""", alias="Protocols")
    OutpostArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-outpostarn""", alias="OutpostArn")
    PreferredInstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-preferredinstancetype""", alias="PreferredInstanceType")
    ResolverEndpointType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-resolverendpointtype""", alias="ResolverEndpointType")
    Direction_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-direction""", alias="Direction")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-securitygroupids""", alias="SecurityGroupIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53resolver.ResolverEndpoint:
        from troposphere.route53resolver import ResolverEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53resolver import ResolverEndpoint as TropoT
        return resource_to_troposphere(self, TropoT)


class ResolverQueryLoggingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html
    Properties:
        - Name: DestinationArn
        - Name: Name
    Attributes:
        - Name: Status
        - Name: OwnerId
        - Name: AssociationCount
        - Name: CreationTime
        - Name: ShareStatus
        - Name: Id
        - Name: Arn
        - Name: CreatorRequestId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DestinationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#cfn-route53resolver-resolverqueryloggingconfig-destinationarn""", alias="DestinationArn")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#cfn-route53resolver-resolverqueryloggingconfig-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53resolver.ResolverQueryLoggingConfig:
        from troposphere.route53resolver import ResolverQueryLoggingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53resolver import ResolverQueryLoggingConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class ResolverQueryLoggingConfigAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html
    Properties:
        - Name: ResourceId
        - Name: ResolverQueryLogConfigId
    Attributes:
        - Name: Status
        - Name: CreationTime
        - Name: Error
        - Name: Id
        - Name: ErrorMessage
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#cfn-route53resolver-resolverqueryloggingconfigassociation-resourceid""", alias="ResourceId")
    ResolverQueryLogConfigId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#cfn-route53resolver-resolverqueryloggingconfigassociation-resolverquerylogconfigid""", alias="ResolverQueryLogConfigId")
    

    @property
    def tropo_type(self) -> troposphere.route53resolver.ResolverQueryLoggingConfigAssociation:
        from troposphere.route53resolver import ResolverQueryLoggingConfigAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53resolver import ResolverQueryLoggingConfigAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class ResolverRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html
    Properties:
        - Name: ResolverEndpointId
        - Name: DomainName
        - Name: RuleType
        - Name: Tags
        - Name: TargetIps
        - Name: Name
    Attributes:
        - Name: ResolverEndpointId
        - Name: DomainName
        - Name: ResolverRuleId
        - Name: Arn
        - Name: TargetIps
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResolverEndpointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-resolverendpointid""", alias="ResolverEndpointId")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-domainname""", alias="DomainName")
    RuleType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-ruletype""", alias="RuleType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-tags""", alias="Tags")
    TargetIps_: Optional[List['TargetAddress']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-targetips""", alias="TargetIps")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53resolver.ResolverRule:
        from troposphere.route53resolver import ResolverRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53resolver import ResolverRule as TropoT
        return resource_to_troposphere(self, TropoT)


class ResolverRuleAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html
    Properties:
        - Name: VPCId
        - Name: ResolverRuleId
        - Name: Name
    Attributes:
        - Name: VPCId
        - Name: ResolverRuleId
        - Name: ResolverRuleAssociationId
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VPCId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-vpcid""", alias="VPCId")
    ResolverRuleId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-resolverruleid""", alias="ResolverRuleId")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53resolver.ResolverRuleAssociation:
        from troposphere.route53resolver import ResolverRuleAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53resolver import ResolverRuleAssociation as TropoT
        return resource_to_troposphere(self, TropoT)

