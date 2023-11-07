from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CachePolicyConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html
    Properties:
        - Name: Comment
        - Name: MinTTL
        - Name: MaxTTL
        - Name: ParametersInCacheKeyAndForwardedToOrigin
        - Name: DefaultTTL
        - Name: Name
    
    """
    
    Comment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-comment""", alias="Comment")
    MinTTL_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-minttl""", alias="MinTTL")
    MaxTTL_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-maxttl""", alias="MaxTTL")
    ParametersInCacheKeyAndForwardedToOrigin_: 'ParametersInCacheKeyAndForwardedToOrigin' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-parametersincachekeyandforwardedtoorigin""", alias="ParametersInCacheKeyAndForwardedToOrigin")
    DefaultTTL_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-defaultttl""", alias="DefaultTTL")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.CachePolicyConfig:
        from troposphere.cloudfront import CachePolicyConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CookiesConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cookiesconfig.html
    Properties:
        - Name: Cookies
        - Name: CookieBehavior
    
    """
    
    Cookies_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cookiesconfig.html#cfn-cloudfront-cachepolicy-cookiesconfig-cookies""", alias="Cookies")
    CookieBehavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cookiesconfig.html#cfn-cloudfront-cachepolicy-cookiesconfig-cookiebehavior""", alias="CookieBehavior")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.CookiesConfig:
        from troposphere.cloudfront import CookiesConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HeadersConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-headersconfig.html
    Properties:
        - Name: Headers
        - Name: HeaderBehavior
    
    """
    
    Headers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-headersconfig.html#cfn-cloudfront-cachepolicy-headersconfig-headers""", alias="Headers")
    HeaderBehavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-headersconfig.html#cfn-cloudfront-cachepolicy-headersconfig-headerbehavior""", alias="HeaderBehavior")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.HeadersConfig:
        from troposphere.cloudfront import HeadersConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ParametersInCacheKeyAndForwardedToOrigin(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html
    Properties:
        - Name: EnableAcceptEncodingBrotli
        - Name: HeadersConfig
        - Name: CookiesConfig
        - Name: EnableAcceptEncodingGzip
        - Name: QueryStringsConfig
    
    """
    
    EnableAcceptEncodingBrotli_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-enableacceptencodingbrotli""", alias="EnableAcceptEncodingBrotli")
    HeadersConfig_: 'HeadersConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-headersconfig""", alias="HeadersConfig")
    CookiesConfig_: 'CookiesConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-cookiesconfig""", alias="CookiesConfig")
    EnableAcceptEncodingGzip_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-enableacceptencodinggzip""", alias="EnableAcceptEncodingGzip")
    QueryStringsConfig_: 'QueryStringsConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-querystringsconfig""", alias="QueryStringsConfig")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.ParametersInCacheKeyAndForwardedToOrigin:
        from troposphere.cloudfront import ParametersInCacheKeyAndForwardedToOrigin as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QueryStringsConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-querystringsconfig.html
    Properties:
        - Name: QueryStrings
        - Name: QueryStringBehavior
    
    """
    
    QueryStrings_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-querystringsconfig.html#cfn-cloudfront-cachepolicy-querystringsconfig-querystrings""", alias="QueryStrings")
    QueryStringBehavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-querystringsconfig.html#cfn-cloudfront-cachepolicy-querystringsconfig-querystringbehavior""", alias="QueryStringBehavior")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.QueryStringsConfig:
        from troposphere.cloudfront import QueryStringsConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudFrontOriginAccessIdentityConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig.html
    Properties:
        - Name: Comment
    
    """
    
    Comment_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig.html#cfn-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig-comment""", alias="Comment")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.CloudFrontOriginAccessIdentityConfig:
        from troposphere.cloudfront import CloudFrontOriginAccessIdentityConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContinuousDeploymentPolicyConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig.html
    Properties:
        - Name: Type
        - Name: SingleHeaderPolicyConfig
        - Name: Enabled
        - Name: StagingDistributionDnsNames
        - Name: TrafficConfig
        - Name: SingleWeightPolicyConfig
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig.html#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-type""", alias="Type")
    SingleHeaderPolicyConfig_: Optional['SingleHeaderPolicyConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig.html#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-singleheaderpolicyconfig""", alias="SingleHeaderPolicyConfig")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig.html#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-enabled""", alias="Enabled")
    StagingDistributionDnsNames_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig.html#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-stagingdistributiondnsnames""", alias="StagingDistributionDnsNames")
    TrafficConfig_: Optional['TrafficConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig.html#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-trafficconfig""", alias="TrafficConfig")
    SingleWeightPolicyConfig_: Optional['SingleWeightPolicyConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig.html#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-singleweightpolicyconfig""", alias="SingleWeightPolicyConfig")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.ContinuousDeploymentPolicyConfig:
        from troposphere.cloudfront import ContinuousDeploymentPolicyConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SessionStickinessConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig.html
    Properties:
        - Name: IdleTTL
        - Name: MaximumTTL
    
    """
    
    IdleTTL_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig.html#cfn-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig-idlettl""", alias="IdleTTL")
    MaximumTTL_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig.html#cfn-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig-maximumttl""", alias="MaximumTTL")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.SessionStickinessConfig:
        from troposphere.cloudfront import SessionStickinessConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SingleHeaderConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderconfig.html
    Properties:
        - Name: Header
        - Name: Value
    
    """
    
    Header_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderconfig.html#cfn-cloudfront-continuousdeploymentpolicy-singleheaderconfig-header""", alias="Header")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderconfig.html#cfn-cloudfront-continuousdeploymentpolicy-singleheaderconfig-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.SingleHeaderConfig:
        from troposphere.cloudfront import SingleHeaderConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SingleHeaderPolicyConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig.html
    Properties:
        - Name: Header
        - Name: Value
    
    """
    
    Header_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig.html#cfn-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig-header""", alias="Header")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig.html#cfn-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.SingleHeaderPolicyConfig:
        from troposphere.cloudfront import SingleHeaderPolicyConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SingleWeightConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleweightconfig.html
    Properties:
        - Name: SessionStickinessConfig
        - Name: Weight
    
    """
    
    SessionStickinessConfig_: Optional['SessionStickinessConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleweightconfig.html#cfn-cloudfront-continuousdeploymentpolicy-singleweightconfig-sessionstickinessconfig""", alias="SessionStickinessConfig")
    Weight_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleweightconfig.html#cfn-cloudfront-continuousdeploymentpolicy-singleweightconfig-weight""", alias="Weight")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.SingleWeightConfig:
        from troposphere.cloudfront import SingleWeightConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SingleWeightPolicyConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig.html
    Properties:
        - Name: SessionStickinessConfig
        - Name: Weight
    
    """
    
    SessionStickinessConfig_: Optional['SessionStickinessConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig.html#cfn-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig-sessionstickinessconfig""", alias="SessionStickinessConfig")
    Weight_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig.html#cfn-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig-weight""", alias="Weight")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.SingleWeightPolicyConfig:
        from troposphere.cloudfront import SingleWeightPolicyConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrafficConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-trafficconfig.html
    Properties:
        - Name: SingleWeightConfig
        - Name: Type
        - Name: SingleHeaderConfig
    
    """
    
    SingleWeightConfig_: Optional['SingleWeightConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-trafficconfig.html#cfn-cloudfront-continuousdeploymentpolicy-trafficconfig-singleweightconfig""", alias="SingleWeightConfig")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-trafficconfig.html#cfn-cloudfront-continuousdeploymentpolicy-trafficconfig-type""", alias="Type")
    SingleHeaderConfig_: Optional['SingleHeaderConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-trafficconfig.html#cfn-cloudfront-continuousdeploymentpolicy-trafficconfig-singleheaderconfig""", alias="SingleHeaderConfig")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.TrafficConfig:
        from troposphere.cloudfront import TrafficConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CacheBehavior(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html
    Properties:
        - Name: Compress
        - Name: FunctionAssociations
        - Name: LambdaFunctionAssociations
        - Name: TargetOriginId
        - Name: ViewerProtocolPolicy
        - Name: ResponseHeadersPolicyId
        - Name: RealtimeLogConfigArn
        - Name: TrustedSigners
        - Name: DefaultTTL
        - Name: FieldLevelEncryptionId
        - Name: TrustedKeyGroups
        - Name: AllowedMethods
        - Name: PathPattern
        - Name: CachedMethods
        - Name: SmoothStreaming
        - Name: ForwardedValues
        - Name: OriginRequestPolicyId
        - Name: MinTTL
        - Name: CachePolicyId
        - Name: MaxTTL
    
    """
    
    Compress_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-compress""", alias="Compress")
    FunctionAssociations_: Optional[List['FunctionAssociation']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-functionassociations""", alias="FunctionAssociations")
    LambdaFunctionAssociations_: Optional[List['LambdaFunctionAssociation']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-lambdafunctionassociations""", alias="LambdaFunctionAssociations")
    TargetOriginId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-targetoriginid""", alias="TargetOriginId")
    ViewerProtocolPolicy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-viewerprotocolpolicy""", alias="ViewerProtocolPolicy")
    ResponseHeadersPolicyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-responseheaderspolicyid""", alias="ResponseHeadersPolicyId")
    RealtimeLogConfigArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-realtimelogconfigarn""", alias="RealtimeLogConfigArn")
    TrustedSigners_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-trustedsigners""", alias="TrustedSigners")
    DefaultTTL_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-defaultttl""", alias="DefaultTTL")
    FieldLevelEncryptionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-fieldlevelencryptionid""", alias="FieldLevelEncryptionId")
    TrustedKeyGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-trustedkeygroups""", alias="TrustedKeyGroups")
    AllowedMethods_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-allowedmethods""", alias="AllowedMethods")
    PathPattern_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-pathpattern""", alias="PathPattern")
    CachedMethods_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-cachedmethods""", alias="CachedMethods")
    SmoothStreaming_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-smoothstreaming""", alias="SmoothStreaming")
    ForwardedValues_: Optional['ForwardedValues'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-forwardedvalues""", alias="ForwardedValues")
    OriginRequestPolicyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-originrequestpolicyid""", alias="OriginRequestPolicyId")
    MinTTL_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-minttl""", alias="MinTTL")
    CachePolicyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-cachepolicyid""", alias="CachePolicyId")
    MaxTTL_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-maxttl""", alias="MaxTTL")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.CacheBehavior:
        from troposphere.cloudfront import CacheBehavior as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Cookies(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html
    Properties:
        - Name: WhitelistedNames
        - Name: Forward
    
    """
    
    WhitelistedNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html#cfn-cloudfront-distribution-cookies-whitelistednames""", alias="WhitelistedNames")
    Forward_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html#cfn-cloudfront-distribution-cookies-forward""", alias="Forward")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.Cookies:
        from troposphere.cloudfront import Cookies as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomErrorResponse(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html
    Properties:
        - Name: ResponseCode
        - Name: ErrorCachingMinTTL
        - Name: ErrorCode
        - Name: ResponsePagePath
    
    """
    
    ResponseCode_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-responsecode""", alias="ResponseCode")
    ErrorCachingMinTTL_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-errorcachingminttl""", alias="ErrorCachingMinTTL")
    ErrorCode_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-errorcode""", alias="ErrorCode")
    ResponsePagePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-responsepagepath""", alias="ResponsePagePath")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.CustomErrorResponse:
        from troposphere.cloudfront import CustomErrorResponse as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomOriginConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html
    Properties:
        - Name: OriginReadTimeout
        - Name: HTTPSPort
        - Name: OriginKeepaliveTimeout
        - Name: OriginSSLProtocols
        - Name: HTTPPort
        - Name: OriginProtocolPolicy
    
    """
    
    OriginReadTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originreadtimeout""", alias="OriginReadTimeout")
    HTTPSPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-httpsport""", alias="HTTPSPort")
    OriginKeepaliveTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originkeepalivetimeout""", alias="OriginKeepaliveTimeout")
    OriginSSLProtocols_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originsslprotocols""", alias="OriginSSLProtocols")
    HTTPPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-httpport""", alias="HTTPPort")
    OriginProtocolPolicy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originprotocolpolicy""", alias="OriginProtocolPolicy")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.CustomOriginConfig:
        from troposphere.cloudfront import CustomOriginConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefaultCacheBehavior(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html
    Properties:
        - Name: Compress
        - Name: FunctionAssociations
        - Name: LambdaFunctionAssociations
        - Name: TargetOriginId
        - Name: ViewerProtocolPolicy
        - Name: ResponseHeadersPolicyId
        - Name: RealtimeLogConfigArn
        - Name: TrustedSigners
        - Name: DefaultTTL
        - Name: FieldLevelEncryptionId
        - Name: TrustedKeyGroups
        - Name: AllowedMethods
        - Name: CachedMethods
        - Name: SmoothStreaming
        - Name: ForwardedValues
        - Name: OriginRequestPolicyId
        - Name: MinTTL
        - Name: CachePolicyId
        - Name: MaxTTL
    
    """
    
    Compress_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-compress""", alias="Compress")
    FunctionAssociations_: Optional[List['FunctionAssociation']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-functionassociations""", alias="FunctionAssociations")
    LambdaFunctionAssociations_: Optional[List['LambdaFunctionAssociation']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-lambdafunctionassociations""", alias="LambdaFunctionAssociations")
    TargetOriginId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-targetoriginid""", alias="TargetOriginId")
    ViewerProtocolPolicy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-viewerprotocolpolicy""", alias="ViewerProtocolPolicy")
    ResponseHeadersPolicyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-responseheaderspolicyid""", alias="ResponseHeadersPolicyId")
    RealtimeLogConfigArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-realtimelogconfigarn""", alias="RealtimeLogConfigArn")
    TrustedSigners_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-trustedsigners""", alias="TrustedSigners")
    DefaultTTL_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-defaultttl""", alias="DefaultTTL")
    FieldLevelEncryptionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-fieldlevelencryptionid""", alias="FieldLevelEncryptionId")
    TrustedKeyGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-trustedkeygroups""", alias="TrustedKeyGroups")
    AllowedMethods_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-allowedmethods""", alias="AllowedMethods")
    CachedMethods_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-cachedmethods""", alias="CachedMethods")
    SmoothStreaming_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-smoothstreaming""", alias="SmoothStreaming")
    ForwardedValues_: Optional['ForwardedValues'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-forwardedvalues""", alias="ForwardedValues")
    OriginRequestPolicyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-originrequestpolicyid""", alias="OriginRequestPolicyId")
    MinTTL_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-minttl""", alias="MinTTL")
    CachePolicyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-cachepolicyid""", alias="CachePolicyId")
    MaxTTL_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-maxttl""", alias="MaxTTL")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.DefaultCacheBehavior:
        from troposphere.cloudfront import DefaultCacheBehavior as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DistributionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html
    Properties:
        - Name: Logging
        - Name: Comment
        - Name: DefaultRootObject
        - Name: Origins
        - Name: ViewerCertificate
        - Name: PriceClass
        - Name: CustomOrigin
        - Name: S3Origin
        - Name: DefaultCacheBehavior
        - Name: Staging
        - Name: CustomErrorResponses
        - Name: ContinuousDeploymentPolicyId
        - Name: OriginGroups
        - Name: Enabled
        - Name: Aliases
        - Name: IPV6Enabled
        - Name: CNAMEs
        - Name: WebACLId
        - Name: HttpVersion
        - Name: Restrictions
        - Name: CacheBehaviors
    
    """
    
    Logging_: Optional['Logging'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-logging""", alias="Logging")
    Comment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-comment""", alias="Comment")
    DefaultRootObject_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-defaultrootobject""", alias="DefaultRootObject")
    Origins_: Optional[List['Origin']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-origins""", alias="Origins")
    ViewerCertificate_: Optional['ViewerCertificate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-viewercertificate""", alias="ViewerCertificate")
    PriceClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-priceclass""", alias="PriceClass")
    CustomOrigin_: Optional['LegacyCustomOrigin'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-customorigin""", alias="CustomOrigin")
    S3Origin_: Optional['LegacyS3Origin'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-s3origin""", alias="S3Origin")
    DefaultCacheBehavior_: 'DefaultCacheBehavior' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-defaultcachebehavior""", alias="DefaultCacheBehavior")
    Staging_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-staging""", alias="Staging")
    CustomErrorResponses_: Optional[List['CustomErrorResponse']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-customerrorresponses""", alias="CustomErrorResponses")
    ContinuousDeploymentPolicyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-continuousdeploymentpolicyid""", alias="ContinuousDeploymentPolicyId")
    OriginGroups_: Optional['OriginGroups'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-origingroups""", alias="OriginGroups")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-enabled""", alias="Enabled")
    Aliases_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-aliases""", alias="Aliases")
    IPV6Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-ipv6enabled""", alias="IPV6Enabled")
    CNAMEs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-cnames""", alias="CNAMEs")
    WebACLId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-webaclid""", alias="WebACLId")
    HttpVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-httpversion""", alias="HttpVersion")
    Restrictions_: Optional['Restrictions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-restrictions""", alias="Restrictions")
    CacheBehaviors_: Optional[List['CacheBehavior']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-cachebehaviors""", alias="CacheBehaviors")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.DistributionConfig:
        from troposphere.cloudfront import DistributionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ForwardedValues(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html
    Properties:
        - Name: Cookies
        - Name: Headers
        - Name: QueryString
        - Name: QueryStringCacheKeys
    
    """
    
    Cookies_: Optional['Cookies'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-cookies""", alias="Cookies")
    Headers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-headers""", alias="Headers")
    QueryString_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-querystring""", alias="QueryString")
    QueryStringCacheKeys_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-querystringcachekeys""", alias="QueryStringCacheKeys")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.ForwardedValues:
        from troposphere.cloudfront import ForwardedValues as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FunctionAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-functionassociation.html
    Properties:
        - Name: FunctionARN
        - Name: EventType
    
    """
    
    FunctionARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-functionassociation.html#cfn-cloudfront-distribution-functionassociation-functionarn""", alias="FunctionARN")
    EventType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-functionassociation.html#cfn-cloudfront-distribution-functionassociation-eventtype""", alias="EventType")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.FunctionAssociation:
        from troposphere.cloudfront import FunctionAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GeoRestriction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html
    Properties:
        - Name: Locations
        - Name: RestrictionType
    
    """
    
    Locations_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html#cfn-cloudfront-distribution-georestriction-locations""", alias="Locations")
    RestrictionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html#cfn-cloudfront-distribution-georestriction-restrictiontype""", alias="RestrictionType")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.GeoRestriction:
        from troposphere.cloudfront import GeoRestriction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaFunctionAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html
    Properties:
        - Name: IncludeBody
        - Name: EventType
        - Name: LambdaFunctionARN
    
    """
    
    IncludeBody_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html#cfn-cloudfront-distribution-lambdafunctionassociation-includebody""", alias="IncludeBody")
    EventType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html#cfn-cloudfront-distribution-lambdafunctionassociation-eventtype""", alias="EventType")
    LambdaFunctionARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html#cfn-cloudfront-distribution-lambdafunctionassociation-lambdafunctionarn""", alias="LambdaFunctionARN")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.LambdaFunctionAssociation:
        from troposphere.cloudfront import LambdaFunctionAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LegacyCustomOrigin(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html
    Properties:
        - Name: HTTPSPort
        - Name: OriginSSLProtocols
        - Name: DNSName
        - Name: HTTPPort
        - Name: OriginProtocolPolicy
    
    """
    
    HTTPSPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-httpsport""", alias="HTTPSPort")
    OriginSSLProtocols_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-originsslprotocols""", alias="OriginSSLProtocols")
    DNSName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-dnsname""", alias="DNSName")
    HTTPPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-httpport""", alias="HTTPPort")
    OriginProtocolPolicy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-originprotocolpolicy""", alias="OriginProtocolPolicy")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.LegacyCustomOrigin:
        from troposphere.cloudfront import LegacyCustomOrigin as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LegacyS3Origin(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html
    Properties:
        - Name: OriginAccessIdentity
        - Name: DNSName
    
    """
    
    OriginAccessIdentity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html#cfn-cloudfront-distribution-legacys3origin-originaccessidentity""", alias="OriginAccessIdentity")
    DNSName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html#cfn-cloudfront-distribution-legacys3origin-dnsname""", alias="DNSName")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.LegacyS3Origin:
        from troposphere.cloudfront import LegacyS3Origin as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Logging(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html
    Properties:
        - Name: IncludeCookies
        - Name: Bucket
        - Name: Prefix
    
    """
    
    IncludeCookies_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html#cfn-cloudfront-distribution-logging-includecookies""", alias="IncludeCookies")
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html#cfn-cloudfront-distribution-logging-bucket""", alias="Bucket")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html#cfn-cloudfront-distribution-logging-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.Logging:
        from troposphere.cloudfront import Logging as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Origin(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html
    Properties:
        - Name: ConnectionTimeout
        - Name: OriginAccessControlId
        - Name: ConnectionAttempts
        - Name: OriginCustomHeaders
        - Name: DomainName
        - Name: OriginShield
        - Name: S3OriginConfig
        - Name: OriginPath
        - Name: Id
        - Name: CustomOriginConfig
    
    """
    
    ConnectionTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-connectiontimeout""", alias="ConnectionTimeout")
    OriginAccessControlId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-originaccesscontrolid""", alias="OriginAccessControlId")
    ConnectionAttempts_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-connectionattempts""", alias="ConnectionAttempts")
    OriginCustomHeaders_: Optional[List['OriginCustomHeader']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-origincustomheaders""", alias="OriginCustomHeaders")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-domainname""", alias="DomainName")
    OriginShield_: Optional['OriginShield'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-originshield""", alias="OriginShield")
    S3OriginConfig_: Optional['S3OriginConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-s3originconfig""", alias="S3OriginConfig")
    OriginPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-originpath""", alias="OriginPath")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-id""", alias="Id")
    CustomOriginConfig_: Optional['CustomOriginConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-customoriginconfig""", alias="CustomOriginConfig")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.Origin:
        from troposphere.cloudfront import Origin as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OriginCustomHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html
    Properties:
        - Name: HeaderValue
        - Name: HeaderName
    
    """
    
    HeaderValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html#cfn-cloudfront-distribution-origincustomheader-headervalue""", alias="HeaderValue")
    HeaderName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html#cfn-cloudfront-distribution-origincustomheader-headername""", alias="HeaderName")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.OriginCustomHeader:
        from troposphere.cloudfront import OriginCustomHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OriginGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html
    Properties:
        - Name: Id
        - Name: FailoverCriteria
        - Name: Members
    
    """
    
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html#cfn-cloudfront-distribution-origingroup-id""", alias="Id")
    FailoverCriteria_: 'OriginGroupFailoverCriteria' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html#cfn-cloudfront-distribution-origingroup-failovercriteria""", alias="FailoverCriteria")
    Members_: 'OriginGroupMembers' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html#cfn-cloudfront-distribution-origingroup-members""", alias="Members")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.OriginGroup:
        from troposphere.cloudfront import OriginGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OriginGroupFailoverCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupfailovercriteria.html
    Properties:
        - Name: StatusCodes
    
    """
    
    StatusCodes_: 'StatusCodes' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupfailovercriteria.html#cfn-cloudfront-distribution-origingroupfailovercriteria-statuscodes""", alias="StatusCodes")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.OriginGroupFailoverCriteria:
        from troposphere.cloudfront import OriginGroupFailoverCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OriginGroupMember(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmember.html
    Properties:
        - Name: OriginId
    
    """
    
    OriginId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmember.html#cfn-cloudfront-distribution-origingroupmember-originid""", alias="OriginId")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.OriginGroupMember:
        from troposphere.cloudfront import OriginGroupMember as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OriginGroupMembers(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html
    Properties:
        - Name: Quantity
        - Name: Items
    
    """
    
    Quantity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html#cfn-cloudfront-distribution-origingroupmembers-quantity""", alias="Quantity")
    Items_: List['OriginGroupMember'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html#cfn-cloudfront-distribution-origingroupmembers-items""", alias="Items")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.OriginGroupMembers:
        from troposphere.cloudfront import OriginGroupMembers as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OriginGroups(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html
    Properties:
        - Name: Quantity
        - Name: Items
    
    """
    
    Quantity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html#cfn-cloudfront-distribution-origingroups-quantity""", alias="Quantity")
    Items_: Optional[List['OriginGroup']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html#cfn-cloudfront-distribution-origingroups-items""", alias="Items")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.OriginGroups:
        from troposphere.cloudfront import OriginGroups as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OriginShield(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-originshield.html
    Properties:
        - Name: OriginShieldRegion
        - Name: Enabled
    
    """
    
    OriginShieldRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-originshield.html#cfn-cloudfront-distribution-originshield-originshieldregion""", alias="OriginShieldRegion")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-originshield.html#cfn-cloudfront-distribution-originshield-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.OriginShield:
        from troposphere.cloudfront import OriginShield as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Restrictions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-restrictions.html
    Properties:
        - Name: GeoRestriction
    
    """
    
    GeoRestriction_: 'GeoRestriction' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-restrictions.html#cfn-cloudfront-distribution-restrictions-georestriction""", alias="GeoRestriction")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.Restrictions:
        from troposphere.cloudfront import Restrictions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3OriginConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-s3originconfig.html
    Properties:
        - Name: OriginAccessIdentity
    
    """
    
    OriginAccessIdentity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-s3originconfig.html#cfn-cloudfront-distribution-s3originconfig-originaccessidentity""", alias="OriginAccessIdentity")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.S3OriginConfig:
        from troposphere.cloudfront import S3OriginConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatusCodes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html
    Properties:
        - Name: Quantity
        - Name: Items
    
    """
    
    Quantity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html#cfn-cloudfront-distribution-statuscodes-quantity""", alias="Quantity")
    Items_: List[int] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html#cfn-cloudfront-distribution-statuscodes-items""", alias="Items")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.StatusCodes:
        from troposphere.cloudfront import StatusCodes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ViewerCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html
    Properties:
        - Name: IamCertificateId
        - Name: SslSupportMethod
        - Name: MinimumProtocolVersion
        - Name: CloudFrontDefaultCertificate
        - Name: AcmCertificateArn
    
    """
    
    IamCertificateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-iamcertificateid""", alias="IamCertificateId")
    SslSupportMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-sslsupportmethod""", alias="SslSupportMethod")
    MinimumProtocolVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-minimumprotocolversion""", alias="MinimumProtocolVersion")
    CloudFrontDefaultCertificate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-cloudfrontdefaultcertificate""", alias="CloudFrontDefaultCertificate")
    AcmCertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-acmcertificatearn""", alias="AcmCertificateArn")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.ViewerCertificate:
        from troposphere.cloudfront import ViewerCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FunctionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionconfig.html
    Properties:
        - Name: Comment
        - Name: Runtime
    
    """
    
    Comment_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionconfig.html#cfn-cloudfront-function-functionconfig-comment""", alias="Comment")
    Runtime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionconfig.html#cfn-cloudfront-function-functionconfig-runtime""", alias="Runtime")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.FunctionConfig:
        from troposphere.cloudfront import FunctionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FunctionMetadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionmetadata.html
    Properties:
        - Name: FunctionARN
    
    """
    
    FunctionARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionmetadata.html#cfn-cloudfront-function-functionmetadata-functionarn""", alias="FunctionARN")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.FunctionMetadata:
        from troposphere.cloudfront import FunctionMetadata as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeyGroupConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keygroup-keygroupconfig.html
    Properties:
        - Name: Comment
        - Name: Items
        - Name: Name
    
    """
    
    Comment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keygroup-keygroupconfig.html#cfn-cloudfront-keygroup-keygroupconfig-comment""", alias="Comment")
    Items_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keygroup-keygroupconfig.html#cfn-cloudfront-keygroup-keygroupconfig-items""", alias="Items")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keygroup-keygroupconfig.html#cfn-cloudfront-keygroup-keygroupconfig-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.KeyGroupConfig:
        from troposphere.cloudfront import KeyGroupConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MonitoringSubscription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-monitoringsubscription-monitoringsubscription.html
    Properties:
        - Name: RealtimeMetricsSubscriptionConfig
    
    """
    
    RealtimeMetricsSubscriptionConfig_: Optional['RealtimeMetricsSubscriptionConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-monitoringsubscription-monitoringsubscription.html#cfn-cloudfront-monitoringsubscription-monitoringsubscription-realtimemetricssubscriptionconfig""", alias="RealtimeMetricsSubscriptionConfig")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.MonitoringSubscription:
        from troposphere.cloudfront import MonitoringSubscription as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RealtimeMetricsSubscriptionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-monitoringsubscription-realtimemetricssubscriptionconfig.html
    Properties:
        - Name: RealtimeMetricsSubscriptionStatus
    
    """
    
    RealtimeMetricsSubscriptionStatus_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-monitoringsubscription-realtimemetricssubscriptionconfig.html#cfn-cloudfront-monitoringsubscription-realtimemetricssubscriptionconfig-realtimemetricssubscriptionstatus""", alias="RealtimeMetricsSubscriptionStatus")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.RealtimeMetricsSubscriptionConfig:
        from troposphere.cloudfront import RealtimeMetricsSubscriptionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OriginAccessControlConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originaccesscontrol-originaccesscontrolconfig.html
    Properties:
        - Name: SigningBehavior
        - Name: Description
        - Name: OriginAccessControlOriginType
        - Name: SigningProtocol
        - Name: Name
    
    """
    
    SigningBehavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originaccesscontrol-originaccesscontrolconfig.html#cfn-cloudfront-originaccesscontrol-originaccesscontrolconfig-signingbehavior""", alias="SigningBehavior")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originaccesscontrol-originaccesscontrolconfig.html#cfn-cloudfront-originaccesscontrol-originaccesscontrolconfig-description""", alias="Description")
    OriginAccessControlOriginType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originaccesscontrol-originaccesscontrolconfig.html#cfn-cloudfront-originaccesscontrol-originaccesscontrolconfig-originaccesscontrolorigintype""", alias="OriginAccessControlOriginType")
    SigningProtocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originaccesscontrol-originaccesscontrolconfig.html#cfn-cloudfront-originaccesscontrol-originaccesscontrolconfig-signingprotocol""", alias="SigningProtocol")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originaccesscontrol-originaccesscontrolconfig.html#cfn-cloudfront-originaccesscontrol-originaccesscontrolconfig-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.OriginAccessControlConfig:
        from troposphere.cloudfront import OriginAccessControlConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CookiesConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-cookiesconfig.html
    Properties:
        - Name: Cookies
        - Name: CookieBehavior
    
    """
    
    Cookies_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-cookiesconfig.html#cfn-cloudfront-originrequestpolicy-cookiesconfig-cookies""", alias="Cookies")
    CookieBehavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-cookiesconfig.html#cfn-cloudfront-originrequestpolicy-cookiesconfig-cookiebehavior""", alias="CookieBehavior")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.CookiesConfig:
        from troposphere.cloudfront import CookiesConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HeadersConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-headersconfig.html
    Properties:
        - Name: Headers
        - Name: HeaderBehavior
    
    """
    
    Headers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-headersconfig.html#cfn-cloudfront-originrequestpolicy-headersconfig-headers""", alias="Headers")
    HeaderBehavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-headersconfig.html#cfn-cloudfront-originrequestpolicy-headersconfig-headerbehavior""", alias="HeaderBehavior")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.HeadersConfig:
        from troposphere.cloudfront import HeadersConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OriginRequestPolicyConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html
    Properties:
        - Name: Comment
        - Name: HeadersConfig
        - Name: CookiesConfig
        - Name: QueryStringsConfig
        - Name: Name
    
    """
    
    Comment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-comment""", alias="Comment")
    HeadersConfig_: 'HeadersConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-headersconfig""", alias="HeadersConfig")
    CookiesConfig_: 'CookiesConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-cookiesconfig""", alias="CookiesConfig")
    QueryStringsConfig_: 'QueryStringsConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-querystringsconfig""", alias="QueryStringsConfig")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.OriginRequestPolicyConfig:
        from troposphere.cloudfront import OriginRequestPolicyConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QueryStringsConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-querystringsconfig.html
    Properties:
        - Name: QueryStrings
        - Name: QueryStringBehavior
    
    """
    
    QueryStrings_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-querystringsconfig.html#cfn-cloudfront-originrequestpolicy-querystringsconfig-querystrings""", alias="QueryStrings")
    QueryStringBehavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-querystringsconfig.html#cfn-cloudfront-originrequestpolicy-querystringsconfig-querystringbehavior""", alias="QueryStringBehavior")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.QueryStringsConfig:
        from troposphere.cloudfront import QueryStringsConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PublicKeyConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html
    Properties:
        - Name: Comment
        - Name: CallerReference
        - Name: EncodedKey
        - Name: Name
    
    """
    
    Comment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html#cfn-cloudfront-publickey-publickeyconfig-comment""", alias="Comment")
    CallerReference_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html#cfn-cloudfront-publickey-publickeyconfig-callerreference""", alias="CallerReference")
    EncodedKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html#cfn-cloudfront-publickey-publickeyconfig-encodedkey""", alias="EncodedKey")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html#cfn-cloudfront-publickey-publickeyconfig-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.PublicKeyConfig:
        from troposphere.cloudfront import PublicKeyConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EndPoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-endpoint.html
    Properties:
        - Name: KinesisStreamConfig
        - Name: StreamType
    
    """
    
    KinesisStreamConfig_: 'KinesisStreamConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-endpoint.html#cfn-cloudfront-realtimelogconfig-endpoint-kinesisstreamconfig""", alias="KinesisStreamConfig")
    StreamType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-endpoint.html#cfn-cloudfront-realtimelogconfig-endpoint-streamtype""", alias="StreamType")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.EndPoint:
        from troposphere.cloudfront import EndPoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisStreamConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig.html
    Properties:
        - Name: StreamArn
        - Name: RoleArn
    
    """
    
    StreamArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig.html#cfn-cloudfront-realtimelogconfig-kinesisstreamconfig-streamarn""", alias="StreamArn")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig.html#cfn-cloudfront-realtimelogconfig-kinesisstreamconfig-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.KinesisStreamConfig:
        from troposphere.cloudfront import KinesisStreamConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessControlAllowHeaders(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowheaders.html
    Properties:
        - Name: Items
    
    """
    
    Items_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowheaders.html#cfn-cloudfront-responseheaderspolicy-accesscontrolallowheaders-items""", alias="Items")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.AccessControlAllowHeaders:
        from troposphere.cloudfront import AccessControlAllowHeaders as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessControlAllowMethods(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods.html
    Properties:
        - Name: Items
    
    """
    
    Items_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods.html#cfn-cloudfront-responseheaderspolicy-accesscontrolallowmethods-items""", alias="Items")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.AccessControlAllowMethods:
        from troposphere.cloudfront import AccessControlAllowMethods as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessControlAllowOrigins(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins.html
    Properties:
        - Name: Items
    
    """
    
    Items_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins.html#cfn-cloudfront-responseheaderspolicy-accesscontrolalloworigins-items""", alias="Items")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.AccessControlAllowOrigins:
        from troposphere.cloudfront import AccessControlAllowOrigins as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessControlExposeHeaders(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolexposeheaders.html
    Properties:
        - Name: Items
    
    """
    
    Items_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolexposeheaders.html#cfn-cloudfront-responseheaderspolicy-accesscontrolexposeheaders-items""", alias="Items")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.AccessControlExposeHeaders:
        from troposphere.cloudfront import AccessControlExposeHeaders as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContentSecurityPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contentsecuritypolicy.html
    Properties:
        - Name: ContentSecurityPolicy
        - Name: Override
    
    """
    
    ContentSecurityPolicy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contentsecuritypolicy.html#cfn-cloudfront-responseheaderspolicy-contentsecuritypolicy-contentsecuritypolicy""", alias="ContentSecurityPolicy")
    Override_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contentsecuritypolicy.html#cfn-cloudfront-responseheaderspolicy-contentsecuritypolicy-override""", alias="Override")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.ContentSecurityPolicy:
        from troposphere.cloudfront import ContentSecurityPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContentTypeOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions.html
    Properties:
        - Name: Override
    
    """
    
    Override_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions.html#cfn-cloudfront-responseheaderspolicy-contenttypeoptions-override""", alias="Override")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.ContentTypeOptions:
        from troposphere.cloudfront import ContentTypeOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CorsConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html
    Properties:
        - Name: AccessControlAllowCredentials
        - Name: AccessControlAllowHeaders
        - Name: OriginOverride
        - Name: AccessControlAllowMethods
        - Name: AccessControlExposeHeaders
        - Name: AccessControlAllowOrigins
        - Name: AccessControlMaxAgeSec
    
    """
    
    AccessControlAllowCredentials_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolallowcredentials""", alias="AccessControlAllowCredentials")
    AccessControlAllowHeaders_: 'AccessControlAllowHeaders' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolallowheaders""", alias="AccessControlAllowHeaders")
    OriginOverride_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-originoverride""", alias="OriginOverride")
    AccessControlAllowMethods_: 'AccessControlAllowMethods' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolallowmethods""", alias="AccessControlAllowMethods")
    AccessControlExposeHeaders_: Optional['AccessControlExposeHeaders'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolexposeheaders""", alias="AccessControlExposeHeaders")
    AccessControlAllowOrigins_: 'AccessControlAllowOrigins' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolalloworigins""", alias="AccessControlAllowOrigins")
    AccessControlMaxAgeSec_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolmaxagesec""", alias="AccessControlMaxAgeSec")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.CorsConfig:
        from troposphere.cloudfront import CorsConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html
    Properties:
        - Name: Header
        - Name: Value
        - Name: Override
    
    """
    
    Header_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html#cfn-cloudfront-responseheaderspolicy-customheader-header""", alias="Header")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html#cfn-cloudfront-responseheaderspolicy-customheader-value""", alias="Value")
    Override_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html#cfn-cloudfront-responseheaderspolicy-customheader-override""", alias="Override")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.CustomHeader:
        from troposphere.cloudfront import CustomHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomHeadersConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheadersconfig.html
    Properties:
        - Name: Items
    
    """
    
    Items_: List['CustomHeader'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheadersconfig.html#cfn-cloudfront-responseheaderspolicy-customheadersconfig-items""", alias="Items")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.CustomHeadersConfig:
        from troposphere.cloudfront import CustomHeadersConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FrameOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-frameoptions.html
    Properties:
        - Name: FrameOption
        - Name: Override
    
    """
    
    FrameOption_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-frameoptions.html#cfn-cloudfront-responseheaderspolicy-frameoptions-frameoption""", alias="FrameOption")
    Override_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-frameoptions.html#cfn-cloudfront-responseheaderspolicy-frameoptions-override""", alias="Override")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.FrameOptions:
        from troposphere.cloudfront import FrameOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReferrerPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-referrerpolicy.html
    Properties:
        - Name: Override
        - Name: ReferrerPolicy
    
    """
    
    Override_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-referrerpolicy.html#cfn-cloudfront-responseheaderspolicy-referrerpolicy-override""", alias="Override")
    ReferrerPolicy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-referrerpolicy.html#cfn-cloudfront-responseheaderspolicy-referrerpolicy-referrerpolicy""", alias="ReferrerPolicy")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.ReferrerPolicy:
        from troposphere.cloudfront import ReferrerPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RemoveHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-removeheader.html
    Properties:
        - Name: Header
    
    """
    
    Header_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-removeheader.html#cfn-cloudfront-responseheaderspolicy-removeheader-header""", alias="Header")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.RemoveHeader:
        from troposphere.cloudfront import RemoveHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RemoveHeadersConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-removeheadersconfig.html
    Properties:
        - Name: Items
    
    """
    
    Items_: List['RemoveHeader'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-removeheadersconfig.html#cfn-cloudfront-responseheaderspolicy-removeheadersconfig-items""", alias="Items")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.RemoveHeadersConfig:
        from troposphere.cloudfront import RemoveHeadersConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResponseHeadersPolicyConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html
    Properties:
        - Name: Comment
        - Name: SecurityHeadersConfig
        - Name: RemoveHeadersConfig
        - Name: CorsConfig
        - Name: ServerTimingHeadersConfig
        - Name: CustomHeadersConfig
        - Name: Name
    
    """
    
    Comment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-comment""", alias="Comment")
    SecurityHeadersConfig_: Optional['SecurityHeadersConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-securityheadersconfig""", alias="SecurityHeadersConfig")
    RemoveHeadersConfig_: Optional['RemoveHeadersConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-removeheadersconfig""", alias="RemoveHeadersConfig")
    CorsConfig_: Optional['CorsConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-corsconfig""", alias="CorsConfig")
    ServerTimingHeadersConfig_: Optional['ServerTimingHeadersConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-servertimingheadersconfig""", alias="ServerTimingHeadersConfig")
    CustomHeadersConfig_: Optional['CustomHeadersConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-customheadersconfig""", alias="CustomHeadersConfig")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.ResponseHeadersPolicyConfig:
        from troposphere.cloudfront import ResponseHeadersPolicyConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SecurityHeadersConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html
    Properties:
        - Name: ContentSecurityPolicy
        - Name: FrameOptions
        - Name: ContentTypeOptions
        - Name: StrictTransportSecurity
        - Name: XSSProtection
        - Name: ReferrerPolicy
    
    """
    
    ContentSecurityPolicy_: Optional['ContentSecurityPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-contentsecuritypolicy""", alias="ContentSecurityPolicy")
    FrameOptions_: Optional['FrameOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-frameoptions""", alias="FrameOptions")
    ContentTypeOptions_: Optional['ContentTypeOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-contenttypeoptions""", alias="ContentTypeOptions")
    StrictTransportSecurity_: Optional['StrictTransportSecurity'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-stricttransportsecurity""", alias="StrictTransportSecurity")
    XSSProtection_: Optional['XSSProtection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-xssprotection""", alias="XSSProtection")
    ReferrerPolicy_: Optional['ReferrerPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-referrerpolicy""", alias="ReferrerPolicy")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.SecurityHeadersConfig:
        from troposphere.cloudfront import SecurityHeadersConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServerTimingHeadersConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-servertimingheadersconfig.html
    Properties:
        - Name: Enabled
        - Name: SamplingRate
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-servertimingheadersconfig.html#cfn-cloudfront-responseheaderspolicy-servertimingheadersconfig-enabled""", alias="Enabled")
    SamplingRate_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-servertimingheadersconfig.html#cfn-cloudfront-responseheaderspolicy-servertimingheadersconfig-samplingrate""", alias="SamplingRate")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.ServerTimingHeadersConfig:
        from troposphere.cloudfront import ServerTimingHeadersConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StrictTransportSecurity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html
    Properties:
        - Name: Preload
        - Name: AccessControlMaxAgeSec
        - Name: IncludeSubdomains
        - Name: Override
    
    """
    
    Preload_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html#cfn-cloudfront-responseheaderspolicy-stricttransportsecurity-preload""", alias="Preload")
    AccessControlMaxAgeSec_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html#cfn-cloudfront-responseheaderspolicy-stricttransportsecurity-accesscontrolmaxagesec""", alias="AccessControlMaxAgeSec")
    IncludeSubdomains_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html#cfn-cloudfront-responseheaderspolicy-stricttransportsecurity-includesubdomains""", alias="IncludeSubdomains")
    Override_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html#cfn-cloudfront-responseheaderspolicy-stricttransportsecurity-override""", alias="Override")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.StrictTransportSecurity:
        from troposphere.cloudfront import StrictTransportSecurity as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class XSSProtection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html
    Properties:
        - Name: ReportUri
        - Name: Override
        - Name: Protection
        - Name: ModeBlock
    
    """
    
    ReportUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html#cfn-cloudfront-responseheaderspolicy-xssprotection-reporturi""", alias="ReportUri")
    Override_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html#cfn-cloudfront-responseheaderspolicy-xssprotection-override""", alias="Override")
    Protection_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html#cfn-cloudfront-responseheaderspolicy-xssprotection-protection""", alias="Protection")
    ModeBlock_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html#cfn-cloudfront-responseheaderspolicy-xssprotection-modeblock""", alias="ModeBlock")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.XSSProtection:
        from troposphere.cloudfront import XSSProtection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Logging(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html
    Properties:
        - Name: Bucket
        - Name: Enabled
        - Name: Prefix
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html#cfn-cloudfront-streamingdistribution-logging-bucket""", alias="Bucket")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html#cfn-cloudfront-streamingdistribution-logging-enabled""", alias="Enabled")
    Prefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html#cfn-cloudfront-streamingdistribution-logging-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.Logging:
        from troposphere.cloudfront import Logging as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Origin(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html
    Properties:
        - Name: DomainName
        - Name: OriginAccessIdentity
    
    """
    
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html#cfn-cloudfront-streamingdistribution-s3origin-domainname""", alias="DomainName")
    OriginAccessIdentity_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html#cfn-cloudfront-streamingdistribution-s3origin-originaccessidentity""", alias="OriginAccessIdentity")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.S3Origin:
        from troposphere.cloudfront import S3Origin as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StreamingDistributionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html
    Properties:
        - Name: Logging
        - Name: Comment
        - Name: PriceClass
        - Name: S3Origin
        - Name: Enabled
        - Name: Aliases
        - Name: TrustedSigners
    
    """
    
    Logging_: Optional['Logging'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-logging""", alias="Logging")
    Comment_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-comment""", alias="Comment")
    PriceClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-priceclass""", alias="PriceClass")
    S3Origin_: 'S3Origin' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-s3origin""", alias="S3Origin")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-enabled""", alias="Enabled")
    Aliases_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-aliases""", alias="Aliases")
    TrustedSigners_: 'TrustedSigners' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-trustedsigners""", alias="TrustedSigners")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.StreamingDistributionConfig:
        from troposphere.cloudfront import StreamingDistributionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrustedSigners(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html
    Properties:
        - Name: Enabled
        - Name: AwsAccountNumbers
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html#cfn-cloudfront-streamingdistribution-trustedsigners-enabled""", alias="Enabled")
    AwsAccountNumbers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html#cfn-cloudfront-streamingdistribution-trustedsigners-awsaccountnumbers""", alias="AwsAccountNumbers")
    


    @property
    def tropo_type(self) -> troposphere.cloudfront.TrustedSigners:
        from troposphere.cloudfront import TrustedSigners as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class CachePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cachepolicy.html
    Properties:
        - Name: CachePolicyConfig
    Attributes:
        - Name: LastModifiedTime
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CachePolicyConfig_: 'CachePolicyConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cachepolicy.html#cfn-cloudfront-cachepolicy-cachepolicyconfig""", alias="CachePolicyConfig")
    

    @property
    def tropo_type(self) -> troposphere.cloudfront.CachePolicy:
        from troposphere.cloudfront import CachePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudfront import CachePolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class CloudFrontOriginAccessIdentity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html
    Properties:
        - Name: CloudFrontOriginAccessIdentityConfig
    Attributes:
        - Name: S3CanonicalUserId
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CloudFrontOriginAccessIdentityConfig_: 'CloudFrontOriginAccessIdentityConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html#cfn-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig""", alias="CloudFrontOriginAccessIdentityConfig")
    

    @property
    def tropo_type(self) -> troposphere.cloudfront.CloudFrontOriginAccessIdentity:
        from troposphere.cloudfront import CloudFrontOriginAccessIdentity as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudfront import CloudFrontOriginAccessIdentity as TropoT
        return resource_to_troposphere(self, TropoT)


class ContinuousDeploymentPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-continuousdeploymentpolicy.html
    Properties:
        - Name: ContinuousDeploymentPolicyConfig
    Attributes:
        - Name: LastModifiedTime
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ContinuousDeploymentPolicyConfig_: 'ContinuousDeploymentPolicyConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-continuousdeploymentpolicy.html#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig""", alias="ContinuousDeploymentPolicyConfig")
    

    @property
    def tropo_type(self) -> troposphere.cloudfront.ContinuousDeploymentPolicy:
        from troposphere.cloudfront import ContinuousDeploymentPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudfront import ContinuousDeploymentPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class Distribution(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html
    Properties:
        - Name: DistributionConfig
        - Name: Tags
    Attributes:
        - Name: DomainName
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DistributionConfig_: 'DistributionConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html#cfn-cloudfront-distribution-distributionconfig""", alias="DistributionConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html#cfn-cloudfront-distribution-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.cloudfront.Distribution:
        from troposphere.cloudfront import Distribution as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudfront import Distribution as TropoT
        return resource_to_troposphere(self, TropoT)


class Function(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html
    Properties:
        - Name: FunctionConfig
        - Name: FunctionMetadata
        - Name: AutoPublish
        - Name: FunctionCode
        - Name: Name
    Attributes:
        - Name: FunctionARN
        - Name: FunctionMetadata.FunctionARN
        - Name: Stage
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FunctionConfig_: 'FunctionConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#cfn-cloudfront-function-functionconfig""", alias="FunctionConfig")
    FunctionMetadata_: Optional['FunctionMetadata'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#cfn-cloudfront-function-functionmetadata""", alias="FunctionMetadata")
    AutoPublish_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#cfn-cloudfront-function-autopublish""", alias="AutoPublish")
    FunctionCode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#cfn-cloudfront-function-functioncode""", alias="FunctionCode")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#cfn-cloudfront-function-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.cloudfront.Function:
        from troposphere.cloudfront import Function as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudfront import Function as TropoT
        return resource_to_troposphere(self, TropoT)


class KeyGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keygroup.html
    Properties:
        - Name: KeyGroupConfig
    Attributes:
        - Name: LastModifiedTime
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KeyGroupConfig_: 'KeyGroupConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keygroup.html#cfn-cloudfront-keygroup-keygroupconfig""", alias="KeyGroupConfig")
    

    @property
    def tropo_type(self) -> troposphere.cloudfront.KeyGroup:
        from troposphere.cloudfront import KeyGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudfront import KeyGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class MonitoringSubscription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-monitoringsubscription.html
    Properties:
        - Name: MonitoringSubscription
        - Name: DistributionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MonitoringSubscription_: 'MonitoringSubscription' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-monitoringsubscription.html#cfn-cloudfront-monitoringsubscription-monitoringsubscription""", alias="MonitoringSubscription")
    DistributionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-monitoringsubscription.html#cfn-cloudfront-monitoringsubscription-distributionid""", alias="DistributionId")
    

    @property
    def tropo_type(self) -> troposphere.cloudfront.MonitoringSubscription:
        from troposphere.cloudfront import MonitoringSubscription as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudfront import MonitoringSubscription as TropoT
        return resource_to_troposphere(self, TropoT)


class OriginAccessControl(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originaccesscontrol.html
    Properties:
        - Name: OriginAccessControlConfig
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OriginAccessControlConfig_: 'OriginAccessControlConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originaccesscontrol.html#cfn-cloudfront-originaccesscontrol-originaccesscontrolconfig""", alias="OriginAccessControlConfig")
    

    @property
    def tropo_type(self) -> troposphere.cloudfront.OriginAccessControl:
        from troposphere.cloudfront import OriginAccessControl as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudfront import OriginAccessControl as TropoT
        return resource_to_troposphere(self, TropoT)


class OriginRequestPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originrequestpolicy.html
    Properties:
        - Name: OriginRequestPolicyConfig
    Attributes:
        - Name: LastModifiedTime
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OriginRequestPolicyConfig_: 'OriginRequestPolicyConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originrequestpolicy.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig""", alias="OriginRequestPolicyConfig")
    

    @property
    def tropo_type(self) -> troposphere.cloudfront.OriginRequestPolicy:
        from troposphere.cloudfront import OriginRequestPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudfront import OriginRequestPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class PublicKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html
    Properties:
        - Name: PublicKeyConfig
    Attributes:
        - Name: CreatedTime
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PublicKeyConfig_: 'PublicKeyConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html#cfn-cloudfront-publickey-publickeyconfig""", alias="PublicKeyConfig")
    

    @property
    def tropo_type(self) -> troposphere.cloudfront.PublicKey:
        from troposphere.cloudfront import PublicKey as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudfront import PublicKey as TropoT
        return resource_to_troposphere(self, TropoT)


class RealtimeLogConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html
    Properties:
        - Name: Fields
        - Name: EndPoints
        - Name: SamplingRate
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Fields_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-fields""", alias="Fields")
    EndPoints_: List['EndPoint'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-endpoints""", alias="EndPoints")
    SamplingRate_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-samplingrate""", alias="SamplingRate")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.cloudfront.RealtimeLogConfig:
        from troposphere.cloudfront import RealtimeLogConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudfront import RealtimeLogConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class ResponseHeadersPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-responseheaderspolicy.html
    Properties:
        - Name: ResponseHeadersPolicyConfig
    Attributes:
        - Name: LastModifiedTime
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResponseHeadersPolicyConfig_: 'ResponseHeadersPolicyConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-responseheaderspolicy.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig""", alias="ResponseHeadersPolicyConfig")
    

    @property
    def tropo_type(self) -> troposphere.cloudfront.ResponseHeadersPolicy:
        from troposphere.cloudfront import ResponseHeadersPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudfront import ResponseHeadersPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class StreamingDistribution(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html
    Properties:
        - Name: StreamingDistributionConfig
        - Name: Tags
    Attributes:
        - Name: DomainName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StreamingDistributionConfig_: 'StreamingDistributionConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig""", alias="StreamingDistributionConfig")
    Tags_: List['Tag'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html#cfn-cloudfront-streamingdistribution-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.cloudfront.StreamingDistribution:
        from troposphere.cloudfront import StreamingDistribution as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudfront import StreamingDistribution as TropoT
        return resource_to_troposphere(self, TropoT)

