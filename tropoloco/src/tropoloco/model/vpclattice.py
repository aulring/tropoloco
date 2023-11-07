from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DefaultAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-defaultaction.html
    Properties:
        - Name: Forward
        - Name: FixedResponse
    
    """
    
    Forward_: Optional['Forward'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-defaultaction.html#cfn-vpclattice-listener-defaultaction-forward""", alias="Forward")
    FixedResponse_: Optional['FixedResponse'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-defaultaction.html#cfn-vpclattice-listener-defaultaction-fixedresponse""", alias="FixedResponse")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.DefaultAction:
        from troposphere.vpclattice import DefaultAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FixedResponse(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-fixedresponse.html
    Properties:
        - Name: StatusCode
    
    """
    
    StatusCode_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-fixedresponse.html#cfn-vpclattice-listener-fixedresponse-statuscode""", alias="StatusCode")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.FixedResponse:
        from troposphere.vpclattice import FixedResponse as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Forward(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-forward.html
    Properties:
        - Name: TargetGroups
    
    """
    
    TargetGroups_: List['WeightedTargetGroup'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-forward.html#cfn-vpclattice-listener-forward-targetgroups""", alias="TargetGroups")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.Forward:
        from troposphere.vpclattice import Forward as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WeightedTargetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-weightedtargetgroup.html
    Properties:
        - Name: Weight
        - Name: TargetGroupIdentifier
    
    """
    
    Weight_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-weightedtargetgroup.html#cfn-vpclattice-listener-weightedtargetgroup-weight""", alias="Weight")
    TargetGroupIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-listener-weightedtargetgroup.html#cfn-vpclattice-listener-weightedtargetgroup-targetgroupidentifier""", alias="TargetGroupIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.WeightedTargetGroup:
        from troposphere.vpclattice import WeightedTargetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-action.html
    Properties:
        - Name: Forward
        - Name: FixedResponse
    
    """
    
    Forward_: Optional['Forward'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-action.html#cfn-vpclattice-rule-action-forward""", alias="Forward")
    FixedResponse_: Optional['FixedResponse'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-action.html#cfn-vpclattice-rule-action-fixedresponse""", alias="FixedResponse")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.Action:
        from troposphere.vpclattice import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FixedResponse(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-fixedresponse.html
    Properties:
        - Name: StatusCode
    
    """
    
    StatusCode_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-fixedresponse.html#cfn-vpclattice-rule-fixedresponse-statuscode""", alias="StatusCode")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.FixedResponse:
        from troposphere.vpclattice import FixedResponse as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Forward(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-forward.html
    Properties:
        - Name: TargetGroups
    
    """
    
    TargetGroups_: List['WeightedTargetGroup'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-forward.html#cfn-vpclattice-rule-forward-targetgroups""", alias="TargetGroups")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.Forward:
        from troposphere.vpclattice import Forward as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HeaderMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatch.html
    Properties:
        - Name: CaseSensitive
        - Name: Name
        - Name: Match
    
    """
    
    CaseSensitive_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatch.html#cfn-vpclattice-rule-headermatch-casesensitive""", alias="CaseSensitive")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatch.html#cfn-vpclattice-rule-headermatch-name""", alias="Name")
    Match_: 'HeaderMatchType' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatch.html#cfn-vpclattice-rule-headermatch-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.HeaderMatch:
        from troposphere.vpclattice import HeaderMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HeaderMatchType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatchtype.html
    Properties:
        - Name: Contains
        - Name: Exact
        - Name: Prefix
    
    """
    
    Contains_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatchtype.html#cfn-vpclattice-rule-headermatchtype-contains""", alias="Contains")
    Exact_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatchtype.html#cfn-vpclattice-rule-headermatchtype-exact""", alias="Exact")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-headermatchtype.html#cfn-vpclattice-rule-headermatchtype-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.HeaderMatchType:
        from troposphere.vpclattice import HeaderMatchType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-httpmatch.html
    Properties:
        - Name: HeaderMatches
        - Name: PathMatch
        - Name: Method
    
    """
    
    HeaderMatches_: Optional[List['HeaderMatch']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-httpmatch.html#cfn-vpclattice-rule-httpmatch-headermatches""", alias="HeaderMatches")
    PathMatch_: Optional['PathMatch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-httpmatch.html#cfn-vpclattice-rule-httpmatch-pathmatch""", alias="PathMatch")
    Method_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-httpmatch.html#cfn-vpclattice-rule-httpmatch-method""", alias="Method")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.HttpMatch:
        from troposphere.vpclattice import HttpMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Match(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-match.html
    Properties:
        - Name: HttpMatch
    
    """
    
    HttpMatch_: 'HttpMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-match.html#cfn-vpclattice-rule-match-httpmatch""", alias="HttpMatch")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.Match:
        from troposphere.vpclattice import Match as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PathMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatch.html
    Properties:
        - Name: CaseSensitive
        - Name: Match
    
    """
    
    CaseSensitive_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatch.html#cfn-vpclattice-rule-pathmatch-casesensitive""", alias="CaseSensitive")
    Match_: 'PathMatchType' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatch.html#cfn-vpclattice-rule-pathmatch-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.PathMatch:
        from troposphere.vpclattice import PathMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PathMatchType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatchtype.html
    Properties:
        - Name: Exact
        - Name: Prefix
    
    """
    
    Exact_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatchtype.html#cfn-vpclattice-rule-pathmatchtype-exact""", alias="Exact")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-pathmatchtype.html#cfn-vpclattice-rule-pathmatchtype-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.PathMatchType:
        from troposphere.vpclattice import PathMatchType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WeightedTargetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-weightedtargetgroup.html
    Properties:
        - Name: Weight
        - Name: TargetGroupIdentifier
    
    """
    
    Weight_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-weightedtargetgroup.html#cfn-vpclattice-rule-weightedtargetgroup-weight""", alias="Weight")
    TargetGroupIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-rule-weightedtargetgroup.html#cfn-vpclattice-rule-weightedtargetgroup-targetgroupidentifier""", alias="TargetGroupIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.WeightedTargetGroup:
        from troposphere.vpclattice import WeightedTargetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DnsEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-service-dnsentry.html
    Properties:
        - Name: DomainName
        - Name: HostedZoneId
    
    """
    
    DomainName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-service-dnsentry.html#cfn-vpclattice-service-dnsentry-domainname""", alias="DomainName")
    HostedZoneId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-service-dnsentry.html#cfn-vpclattice-service-dnsentry-hostedzoneid""", alias="HostedZoneId")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.DnsEntry:
        from troposphere.vpclattice import DnsEntry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DnsEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-servicenetworkserviceassociation-dnsentry.html
    Properties:
        - Name: DomainName
        - Name: HostedZoneId
    
    """
    
    DomainName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-servicenetworkserviceassociation-dnsentry.html#cfn-vpclattice-servicenetworkserviceassociation-dnsentry-domainname""", alias="DomainName")
    HostedZoneId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-servicenetworkserviceassociation-dnsentry.html#cfn-vpclattice-servicenetworkserviceassociation-dnsentry-hostedzoneid""", alias="HostedZoneId")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.DnsEntry:
        from troposphere.vpclattice import DnsEntry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HealthCheckConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html
    Properties:
        - Name: Path
        - Name: HealthCheckIntervalSeconds
        - Name: Matcher
        - Name: HealthyThresholdCount
        - Name: Port
        - Name: Enabled
        - Name: Protocol
        - Name: ProtocolVersion
        - Name: UnhealthyThresholdCount
        - Name: HealthCheckTimeoutSeconds
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-path""", alias="Path")
    HealthCheckIntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-healthcheckintervalseconds""", alias="HealthCheckIntervalSeconds")
    Matcher_: Optional['Matcher'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-matcher""", alias="Matcher")
    HealthyThresholdCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-healthythresholdcount""", alias="HealthyThresholdCount")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-port""", alias="Port")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-enabled""", alias="Enabled")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-protocol""", alias="Protocol")
    ProtocolVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-protocolversion""", alias="ProtocolVersion")
    UnhealthyThresholdCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-unhealthythresholdcount""", alias="UnhealthyThresholdCount")
    HealthCheckTimeoutSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-healthcheckconfig.html#cfn-vpclattice-targetgroup-healthcheckconfig-healthchecktimeoutseconds""", alias="HealthCheckTimeoutSeconds")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.HealthCheckConfig:
        from troposphere.vpclattice import HealthCheckConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Matcher(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-matcher.html
    Properties:
        - Name: HttpCode
    
    """
    
    HttpCode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-matcher.html#cfn-vpclattice-targetgroup-matcher-httpcode""", alias="HttpCode")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.Matcher:
        from troposphere.vpclattice import Matcher as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Target(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-target.html
    Properties:
        - Name: Port
        - Name: Id
    
    """
    
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-target.html#cfn-vpclattice-targetgroup-target-port""", alias="Port")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-target.html#cfn-vpclattice-targetgroup-target-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.Target:
        from troposphere.vpclattice import Target as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetGroupConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html
    Properties:
        - Name: IpAddressType
        - Name: Port
        - Name: HealthCheck
        - Name: LambdaEventStructureVersion
        - Name: VpcIdentifier
        - Name: Protocol
        - Name: ProtocolVersion
    
    """
    
    IpAddressType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-ipaddresstype""", alias="IpAddressType")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-port""", alias="Port")
    HealthCheck_: Optional['HealthCheckConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-healthcheck""", alias="HealthCheck")
    LambdaEventStructureVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-lambdaeventstructureversion""", alias="LambdaEventStructureVersion")
    VpcIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-vpcidentifier""", alias="VpcIdentifier")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-protocol""", alias="Protocol")
    ProtocolVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-vpclattice-targetgroup-targetgroupconfig.html#cfn-vpclattice-targetgroup-targetgroupconfig-protocolversion""", alias="ProtocolVersion")
    


    @property
    def tropo_type(self) -> troposphere.vpclattice.TargetGroupConfig:
        from troposphere.vpclattice import TargetGroupConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AccessLogSubscription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-accesslogsubscription.html
    Properties:
        - Name: ResourceIdentifier
        - Name: DestinationArn
        - Name: Tags
    Attributes:
        - Name: ResourceArn
        - Name: ResourceId
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-accesslogsubscription.html#cfn-vpclattice-accesslogsubscription-resourceidentifier""", alias="ResourceIdentifier")
    DestinationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-accesslogsubscription.html#cfn-vpclattice-accesslogsubscription-destinationarn""", alias="DestinationArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-accesslogsubscription.html#cfn-vpclattice-accesslogsubscription-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.vpclattice.AccessLogSubscription:
        from troposphere.vpclattice import AccessLogSubscription as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.vpclattice import AccessLogSubscription as TropoT
        return resource_to_troposphere(self, TropoT)


class AuthPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-authpolicy.html
    Properties:
        - Name: Policy
        - Name: ResourceIdentifier
    Attributes:
        - Name: State
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-authpolicy.html#cfn-vpclattice-authpolicy-policy""", alias="Policy")
    ResourceIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-authpolicy.html#cfn-vpclattice-authpolicy-resourceidentifier""", alias="ResourceIdentifier")
    

    @property
    def tropo_type(self) -> troposphere.vpclattice.AuthPolicy:
        from troposphere.vpclattice import AuthPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.vpclattice import AuthPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class Listener(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html
    Properties:
        - Name: DefaultAction
        - Name: Port
        - Name: ServiceIdentifier
        - Name: Protocol
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: ServiceArn
        - Name: Arn
        - Name: ServiceId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DefaultAction_: 'DefaultAction' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html#cfn-vpclattice-listener-defaultaction""", alias="DefaultAction")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html#cfn-vpclattice-listener-port""", alias="Port")
    ServiceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html#cfn-vpclattice-listener-serviceidentifier""", alias="ServiceIdentifier")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html#cfn-vpclattice-listener-protocol""", alias="Protocol")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html#cfn-vpclattice-listener-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-listener.html#cfn-vpclattice-listener-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.vpclattice.Listener:
        from troposphere.vpclattice import Listener as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.vpclattice import Listener as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourcePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-resourcepolicy.html
    Properties:
        - Name: Policy
        - Name: ResourceArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-resourcepolicy.html#cfn-vpclattice-resourcepolicy-policy""", alias="Policy")
    ResourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-resourcepolicy.html#cfn-vpclattice-resourcepolicy-resourcearn""", alias="ResourceArn")
    

    @property
    def tropo_type(self) -> troposphere.vpclattice.ResourcePolicy:
        from troposphere.vpclattice import ResourcePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.vpclattice import ResourcePolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html
    Properties:
        - Name: Action
        - Name: Priority
        - Name: ServiceIdentifier
        - Name: ListenerIdentifier
        - Name: Tags
        - Name: Match
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Action_: 'Action' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-action""", alias="Action")
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-priority""", alias="Priority")
    ServiceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-serviceidentifier""", alias="ServiceIdentifier")
    ListenerIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-listeneridentifier""", alias="ListenerIdentifier")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-tags""", alias="Tags")
    Match_: 'Match' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-match""", alias="Match")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html#cfn-vpclattice-rule-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.vpclattice.Rule:
        from troposphere.vpclattice import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.vpclattice import Rule as TropoT
        return resource_to_troposphere(self, TropoT)


class Service(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html
    Properties:
        - Name: DnsEntry
        - Name: CustomDomainName
        - Name: AuthType
        - Name: Tags
        - Name: Name
        - Name: CertificateArn
    Attributes:
        - Name: Status
        - Name: LastUpdatedAt
        - Name: CreatedAt
        - Name: DnsEntry.HostedZoneId
        - Name: Id
        - Name: Arn
        - Name: DnsEntry.DomainName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DnsEntry_: Optional['DnsEntry'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html#cfn-vpclattice-service-dnsentry""", alias="DnsEntry")
    CustomDomainName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html#cfn-vpclattice-service-customdomainname""", alias="CustomDomainName")
    AuthType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html#cfn-vpclattice-service-authtype""", alias="AuthType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html#cfn-vpclattice-service-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html#cfn-vpclattice-service-name""", alias="Name")
    CertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-service.html#cfn-vpclattice-service-certificatearn""", alias="CertificateArn")
    

    @property
    def tropo_type(self) -> troposphere.vpclattice.Service:
        from troposphere.vpclattice import Service as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.vpclattice import Service as TropoT
        return resource_to_troposphere(self, TropoT)


class ServiceNetwork(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetwork.html
    Properties:
        - Name: AuthType
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LastUpdatedAt
        - Name: CreatedAt
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AuthType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetwork.html#cfn-vpclattice-servicenetwork-authtype""", alias="AuthType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetwork.html#cfn-vpclattice-servicenetwork-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetwork.html#cfn-vpclattice-servicenetwork-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.vpclattice.ServiceNetwork:
        from troposphere.vpclattice import ServiceNetwork as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.vpclattice import ServiceNetwork as TropoT
        return resource_to_troposphere(self, TropoT)


class ServiceNetworkServiceAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkserviceassociation.html
    Properties:
        - Name: ServiceNetworkIdentifier
        - Name: DnsEntry
        - Name: ServiceIdentifier
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: ServiceNetworkId
        - Name: ServiceName
        - Name: CreatedAt
        - Name: DnsEntry.HostedZoneId
        - Name: ServiceNetworkName
        - Name: ServiceArn
        - Name: Id
        - Name: Arn
        - Name: DnsEntry.DomainName
        - Name: ServiceNetworkArn
        - Name: ServiceId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ServiceNetworkIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkserviceassociation.html#cfn-vpclattice-servicenetworkserviceassociation-servicenetworkidentifier""", alias="ServiceNetworkIdentifier")
    DnsEntry_: Optional['DnsEntry'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkserviceassociation.html#cfn-vpclattice-servicenetworkserviceassociation-dnsentry""", alias="DnsEntry")
    ServiceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkserviceassociation.html#cfn-vpclattice-servicenetworkserviceassociation-serviceidentifier""", alias="ServiceIdentifier")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkserviceassociation.html#cfn-vpclattice-servicenetworkserviceassociation-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.vpclattice.ServiceNetworkServiceAssociation:
        from troposphere.vpclattice import ServiceNetworkServiceAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.vpclattice import ServiceNetworkServiceAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class ServiceNetworkVpcAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkvpcassociation.html
    Properties:
        - Name: ServiceNetworkIdentifier
        - Name: VpcIdentifier
        - Name: SecurityGroupIds
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: VpcId
        - Name: ServiceNetworkId
        - Name: CreatedAt
        - Name: ServiceNetworkName
        - Name: Id
        - Name: Arn
        - Name: ServiceNetworkArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ServiceNetworkIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkvpcassociation.html#cfn-vpclattice-servicenetworkvpcassociation-servicenetworkidentifier""", alias="ServiceNetworkIdentifier")
    VpcIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkvpcassociation.html#cfn-vpclattice-servicenetworkvpcassociation-vpcidentifier""", alias="VpcIdentifier")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkvpcassociation.html#cfn-vpclattice-servicenetworkvpcassociation-securitygroupids""", alias="SecurityGroupIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkvpcassociation.html#cfn-vpclattice-servicenetworkvpcassociation-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.vpclattice.ServiceNetworkVpcAssociation:
        from troposphere.vpclattice import ServiceNetworkVpcAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.vpclattice import ServiceNetworkVpcAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class TargetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html
    Properties:
        - Name: Type
        - Name: Config
        - Name: Targets
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: LastUpdatedAt
        - Name: CreatedAt
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html#cfn-vpclattice-targetgroup-type""", alias="Type")
    Config_: Optional['TargetGroupConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html#cfn-vpclattice-targetgroup-config""", alias="Config")
    Targets_: Optional[List['Target']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html#cfn-vpclattice-targetgroup-targets""", alias="Targets")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html#cfn-vpclattice-targetgroup-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html#cfn-vpclattice-targetgroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.vpclattice.TargetGroup:
        from troposphere.vpclattice import TargetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.vpclattice import TargetGroup as TropoT
        return resource_to_troposphere(self, TropoT)

