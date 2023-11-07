from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AccessLoggingPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-accessloggingpolicy.html
    Properties:
        - Name: EmitInterval
        - Name: Enabled
        - Name: S3BucketName
        - Name: S3BucketPrefix
    
    """
    
    EmitInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-accessloggingpolicy.html#cfn-elb-accessloggingpolicy-emitinterval""", alias="EmitInterval")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-accessloggingpolicy.html#cfn-elb-accessloggingpolicy-enabled""", alias="Enabled")
    S3BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-accessloggingpolicy.html#cfn-elb-accessloggingpolicy-s3bucketname""", alias="S3BucketName")
    S3BucketPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-accessloggingpolicy.html#cfn-elb-accessloggingpolicy-s3bucketprefix""", alias="S3BucketPrefix")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancing.AccessLoggingPolicy:
        from troposphere.elasticloadbalancing import AccessLoggingPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AppCookieStickinessPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-AppCookieStickinessPolicy.html
    Properties:
        - Name: CookieName
        - Name: PolicyName
    
    """
    
    CookieName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-AppCookieStickinessPolicy.html#cfn-elb-appcookiestickinesspolicy-cookiename""", alias="CookieName")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-AppCookieStickinessPolicy.html#cfn-elb-appcookiestickinesspolicy-policyname""", alias="PolicyName")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancing.AppCookieStickinessPolicy:
        from troposphere.elasticloadbalancing import AppCookieStickinessPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectionDrainingPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-connectiondrainingpolicy.html
    Properties:
        - Name: Enabled
        - Name: Timeout
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-connectiondrainingpolicy.html#cfn-elb-connectiondrainingpolicy-enabled""", alias="Enabled")
    Timeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-connectiondrainingpolicy.html#cfn-elb-connectiondrainingpolicy-timeout""", alias="Timeout")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancing.ConnectionDrainingPolicy:
        from troposphere.elasticloadbalancing import ConnectionDrainingPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectionSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-connectionsettings.html
    Properties:
        - Name: IdleTimeout
    
    """
    
    IdleTimeout_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-connectionsettings.html#cfn-elb-connectionsettings-idletimeout""", alias="IdleTimeout")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancing.ConnectionSettings:
        from troposphere.elasticloadbalancing import ConnectionSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HealthCheck(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-health-check.html
    Properties:
        - Name: HealthyThreshold
        - Name: Interval
        - Name: Target
        - Name: Timeout
        - Name: UnhealthyThreshold
    
    """
    
    HealthyThreshold_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-health-check.html#cfn-elb-healthcheck-healthythreshold""", alias="HealthyThreshold")
    Interval_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-health-check.html#cfn-elb-healthcheck-interval""", alias="Interval")
    Target_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-health-check.html#cfn-elb-healthcheck-target""", alias="Target")
    Timeout_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-health-check.html#cfn-elb-healthcheck-timeout""", alias="Timeout")
    UnhealthyThreshold_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-health-check.html#cfn-elb-healthcheck-unhealthythreshold""", alias="UnhealthyThreshold")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancing.HealthCheck:
        from troposphere.elasticloadbalancing import HealthCheck as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LBCookieStickinessPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-LBCookieStickinessPolicy.html
    Properties:
        - Name: CookieExpirationPeriod
        - Name: PolicyName
    
    """
    
    CookieExpirationPeriod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-LBCookieStickinessPolicy.html#cfn-elb-lbcookiestickinesspolicy-cookieexpirationperiod""", alias="CookieExpirationPeriod")
    PolicyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-LBCookieStickinessPolicy.html#cfn-elb-lbcookiestickinesspolicy-policyname""", alias="PolicyName")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancing.LBCookieStickinessPolicy:
        from troposphere.elasticloadbalancing import LBCookieStickinessPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Listeners(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html
    Properties:
        - Name: InstancePort
        - Name: InstanceProtocol
        - Name: LoadBalancerPort
        - Name: PolicyNames
        - Name: Protocol
        - Name: SSLCertificateId
    
    """
    
    InstancePort_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-instanceport""", alias="InstancePort")
    InstanceProtocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-instanceprotocol""", alias="InstanceProtocol")
    LoadBalancerPort_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-loadbalancerport""", alias="LoadBalancerPort")
    PolicyNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-policynames""", alias="PolicyNames")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-protocol""", alias="Protocol")
    SSLCertificateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-sslcertificateid""", alias="SSLCertificateId")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancing.Listeners:
        from troposphere.elasticloadbalancing import Listeners as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Policies(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-policy.html
    Properties:
        - Name: Attributes
        - Name: InstancePorts
        - Name: LoadBalancerPorts
        - Name: PolicyName
        - Name: PolicyType
    
    """
    
    Attributes_: List[Dict] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-policy.html#cfn-ec2-elb-policy-attributes""", alias="Attributes")
    InstancePorts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-policy.html#cfn-ec2-elb-policy-instanceports""", alias="InstancePorts")
    LoadBalancerPorts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-policy.html#cfn-ec2-elb-policy-loadbalancerports""", alias="LoadBalancerPorts")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-policy.html#cfn-ec2-elb-policy-policyname""", alias="PolicyName")
    PolicyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-policy.html#cfn-ec2-elb-policy-policytype""", alias="PolicyType")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancing.Policies:
        from troposphere.elasticloadbalancing import Policies as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class LoadBalancer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html
    Properties:
        - Name: AccessLoggingPolicy
        - Name: AppCookieStickinessPolicy
        - Name: AvailabilityZones
        - Name: ConnectionDrainingPolicy
        - Name: ConnectionSettings
        - Name: CrossZone
        - Name: HealthCheck
        - Name: Instances
        - Name: LBCookieStickinessPolicy
        - Name: Listeners
        - Name: LoadBalancerName
        - Name: Policies
        - Name: Scheme
        - Name: SecurityGroups
        - Name: Subnets
        - Name: Tags
    Attributes:
        - Name: CanonicalHostedZoneName
        - Name: CanonicalHostedZoneNameID
        - Name: DNSName
        - Name: SourceSecurityGroup.GroupName
        - Name: SourceSecurityGroup.OwnerAlias
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AccessLoggingPolicy_: Optional['AccessLoggingPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-accessloggingpolicy""", alias="AccessLoggingPolicy")
    AppCookieStickinessPolicy_: Optional[List['AppCookieStickinessPolicy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-appcookiestickinesspolicy""", alias="AppCookieStickinessPolicy")
    AvailabilityZones_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-availabilityzones""", alias="AvailabilityZones")
    ConnectionDrainingPolicy_: Optional['ConnectionDrainingPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-connectiondrainingpolicy""", alias="ConnectionDrainingPolicy")
    ConnectionSettings_: Optional['ConnectionSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-connectionsettings""", alias="ConnectionSettings")
    CrossZone_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-crosszone""", alias="CrossZone")
    HealthCheck_: Optional['HealthCheck'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-healthcheck""", alias="HealthCheck")
    Instances_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-instances""", alias="Instances")
    LBCookieStickinessPolicy_: Optional[List['LBCookieStickinessPolicy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-lbcookiestickinesspolicy""", alias="LBCookieStickinessPolicy")
    Listeners_: List['Listeners'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-listeners""", alias="Listeners")
    LoadBalancerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-elbname""", alias="LoadBalancerName")
    Policies_: Optional[List['Policies']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-policies""", alias="Policies")
    Scheme_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-scheme""", alias="Scheme")
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-securitygroups""", alias="SecurityGroups")
    Subnets_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-subnets""", alias="Subnets")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-elasticloadbalancing-loadbalancer-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.elasticloadbalancing.LoadBalancer:
        from troposphere.elasticloadbalancing import LoadBalancer as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticloadbalancing import LoadBalancer as TropoT
        return resource_to_troposphere(self, TropoT)

