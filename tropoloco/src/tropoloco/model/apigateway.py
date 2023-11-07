from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class StageKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-apikey-stagekey.html
    Properties:
        - Name: StageName
        - Name: RestApiId
    
    """
    
    StageName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-apikey-stagekey.html#cfn-apigateway-apikey-stagekey-stagename""", alias="StageName")
    RestApiId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-apikey-stagekey.html#cfn-apigateway-apikey-stagekey-restapiid""", alias="RestApiId")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.StageKey:
        from troposphere.apigateway import StageKey as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessLogSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-accesslogsetting.html
    Properties:
        - Name: Format
        - Name: DestinationArn
    
    """
    
    Format_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-accesslogsetting.html#cfn-apigateway-deployment-accesslogsetting-format""", alias="Format")
    DestinationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-accesslogsetting.html#cfn-apigateway-deployment-accesslogsetting-destinationarn""", alias="DestinationArn")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.AccessLogSetting:
        from troposphere.apigateway import AccessLogSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CanarySetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-canarysetting.html
    Properties:
        - Name: StageVariableOverrides
        - Name: PercentTraffic
        - Name: UseStageCache
    
    """
    
    StageVariableOverrides_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-canarysetting.html#cfn-apigateway-deployment-canarysetting-stagevariableoverrides""", alias="StageVariableOverrides")
    PercentTraffic_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-canarysetting.html#cfn-apigateway-deployment-canarysetting-percenttraffic""", alias="PercentTraffic")
    UseStageCache_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-canarysetting.html#cfn-apigateway-deployment-canarysetting-usestagecache""", alias="UseStageCache")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.CanarySetting:
        from troposphere.apigateway import CanarySetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentCanarySettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-deploymentcanarysettings.html
    Properties:
        - Name: StageVariableOverrides
        - Name: PercentTraffic
        - Name: UseStageCache
    
    """
    
    StageVariableOverrides_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-deploymentcanarysettings.html#cfn-apigateway-deployment-deploymentcanarysettings-stagevariableoverrides""", alias="StageVariableOverrides")
    PercentTraffic_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-deploymentcanarysettings.html#cfn-apigateway-deployment-deploymentcanarysettings-percenttraffic""", alias="PercentTraffic")
    UseStageCache_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-deploymentcanarysettings.html#cfn-apigateway-deployment-deploymentcanarysettings-usestagecache""", alias="UseStageCache")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.DeploymentCanarySettings:
        from troposphere.apigateway import DeploymentCanarySettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MethodSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-methodsetting.html
    Properties:
        - Name: CacheTtlInSeconds
        - Name: LoggingLevel
        - Name: ResourcePath
        - Name: CacheDataEncrypted
        - Name: DataTraceEnabled
        - Name: ThrottlingBurstLimit
        - Name: CachingEnabled
        - Name: MetricsEnabled
        - Name: HttpMethod
        - Name: ThrottlingRateLimit
    
    """
    
    CacheTtlInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-methodsetting.html#cfn-apigateway-deployment-methodsetting-cachettlinseconds""", alias="CacheTtlInSeconds")
    LoggingLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-methodsetting.html#cfn-apigateway-deployment-methodsetting-logginglevel""", alias="LoggingLevel")
    ResourcePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-methodsetting.html#cfn-apigateway-deployment-methodsetting-resourcepath""", alias="ResourcePath")
    CacheDataEncrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-methodsetting.html#cfn-apigateway-deployment-methodsetting-cachedataencrypted""", alias="CacheDataEncrypted")
    DataTraceEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-methodsetting.html#cfn-apigateway-deployment-methodsetting-datatraceenabled""", alias="DataTraceEnabled")
    ThrottlingBurstLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-methodsetting.html#cfn-apigateway-deployment-methodsetting-throttlingburstlimit""", alias="ThrottlingBurstLimit")
    CachingEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-methodsetting.html#cfn-apigateway-deployment-methodsetting-cachingenabled""", alias="CachingEnabled")
    MetricsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-methodsetting.html#cfn-apigateway-deployment-methodsetting-metricsenabled""", alias="MetricsEnabled")
    HttpMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-methodsetting.html#cfn-apigateway-deployment-methodsetting-httpmethod""", alias="HttpMethod")
    ThrottlingRateLimit_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-methodsetting.html#cfn-apigateway-deployment-methodsetting-throttlingratelimit""", alias="ThrottlingRateLimit")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.MethodSetting:
        from troposphere.apigateway import MethodSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StageDescription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html
    Properties:
        - Name: CacheTtlInSeconds
        - Name: Description
        - Name: LoggingLevel
        - Name: CanarySetting
        - Name: ThrottlingRateLimit
        - Name: ClientCertificateId
        - Name: Variables
        - Name: DocumentationVersion
        - Name: CacheDataEncrypted
        - Name: DataTraceEnabled
        - Name: ThrottlingBurstLimit
        - Name: CachingEnabled
        - Name: TracingEnabled
        - Name: MethodSettings
        - Name: AccessLogSetting
        - Name: CacheClusterSize
        - Name: MetricsEnabled
        - Name: Tags
        - Name: CacheClusterEnabled
    
    """
    
    CacheTtlInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-cachettlinseconds""", alias="CacheTtlInSeconds")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-description""", alias="Description")
    LoggingLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-logginglevel""", alias="LoggingLevel")
    CanarySetting_: Optional['CanarySetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-canarysetting""", alias="CanarySetting")
    ThrottlingRateLimit_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-throttlingratelimit""", alias="ThrottlingRateLimit")
    ClientCertificateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-clientcertificateid""", alias="ClientCertificateId")
    Variables_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-variables""", alias="Variables")
    DocumentationVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-documentationversion""", alias="DocumentationVersion")
    CacheDataEncrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-cachedataencrypted""", alias="CacheDataEncrypted")
    DataTraceEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-datatraceenabled""", alias="DataTraceEnabled")
    ThrottlingBurstLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-throttlingburstlimit""", alias="ThrottlingBurstLimit")
    CachingEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-cachingenabled""", alias="CachingEnabled")
    TracingEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-tracingenabled""", alias="TracingEnabled")
    MethodSettings_: Optional[List['MethodSetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-methodsettings""", alias="MethodSettings")
    AccessLogSetting_: Optional['AccessLogSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-accesslogsetting""", alias="AccessLogSetting")
    CacheClusterSize_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-cacheclustersize""", alias="CacheClusterSize")
    MetricsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-metricsenabled""", alias="MetricsEnabled")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-tags""", alias="Tags")
    CacheClusterEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html#cfn-apigateway-deployment-stagedescription-cacheclusterenabled""", alias="CacheClusterEnabled")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.StageDescription:
        from troposphere.apigateway import StageDescription as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-documentationpart-location.html
    Properties:
        - Name: Path
        - Name: Type
        - Name: Method
        - Name: StatusCode
        - Name: Name
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-documentationpart-location.html#cfn-apigateway-documentationpart-location-path""", alias="Path")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-documentationpart-location.html#cfn-apigateway-documentationpart-location-type""", alias="Type")
    Method_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-documentationpart-location.html#cfn-apigateway-documentationpart-location-method""", alias="Method")
    StatusCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-documentationpart-location.html#cfn-apigateway-documentationpart-location-statuscode""", alias="StatusCode")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-documentationpart-location.html#cfn-apigateway-documentationpart-location-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.Location:
        from troposphere.apigateway import Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EndpointConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-domainname-endpointconfiguration.html
    Properties:
        - Name: Types
    
    """
    
    Types_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-domainname-endpointconfiguration.html#cfn-apigateway-domainname-endpointconfiguration-types""", alias="Types")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.EndpointConfiguration:
        from troposphere.apigateway import EndpointConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MutualTlsAuthentication(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-domainname-mutualtlsauthentication.html
    Properties:
        - Name: TruststoreVersion
        - Name: TruststoreUri
    
    """
    
    TruststoreVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-domainname-mutualtlsauthentication.html#cfn-apigateway-domainname-mutualtlsauthentication-truststoreversion""", alias="TruststoreVersion")
    TruststoreUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-domainname-mutualtlsauthentication.html#cfn-apigateway-domainname-mutualtlsauthentication-truststoreuri""", alias="TruststoreUri")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.MutualTlsAuthentication:
        from troposphere.apigateway import MutualTlsAuthentication as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Integration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html
    Properties:
        - Name: CacheKeyParameters
        - Name: CacheNamespace
        - Name: ConnectionId
        - Name: ConnectionType
        - Name: ContentHandling
        - Name: Credentials
        - Name: IntegrationHttpMethod
        - Name: IntegrationResponses
        - Name: PassthroughBehavior
        - Name: RequestParameters
        - Name: RequestTemplates
        - Name: TimeoutInMillis
        - Name: Type
        - Name: Uri
    
    """
    
    CacheKeyParameters_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-cachekeyparameters""", alias="CacheKeyParameters")
    CacheNamespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-cachenamespace""", alias="CacheNamespace")
    ConnectionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-connectionid""", alias="ConnectionId")
    ConnectionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-connectiontype""", alias="ConnectionType")
    ContentHandling_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-contenthandling""", alias="ContentHandling")
    Credentials_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-credentials""", alias="Credentials")
    IntegrationHttpMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-integrationhttpmethod""", alias="IntegrationHttpMethod")
    IntegrationResponses_: Optional[List['IntegrationResponse']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-integrationresponses""", alias="IntegrationResponses")
    PassthroughBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-passthroughbehavior""", alias="PassthroughBehavior")
    RequestParameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-requestparameters""", alias="RequestParameters")
    RequestTemplates_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-requesttemplates""", alias="RequestTemplates")
    TimeoutInMillis_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-timeoutinmillis""", alias="TimeoutInMillis")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-type""", alias="Type")
    Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html#cfn-apigateway-method-integration-uri""", alias="Uri")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.Integration:
        from troposphere.apigateway import Integration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IntegrationResponse(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration-integrationresponse.html
    Properties:
        - Name: ContentHandling
        - Name: ResponseParameters
        - Name: ResponseTemplates
        - Name: SelectionPattern
        - Name: StatusCode
    
    """
    
    ContentHandling_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration-integrationresponse.html#cfn-apigateway-method-integrationresponse-contenthandling""", alias="ContentHandling")
    ResponseParameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration-integrationresponse.html#cfn-apigateway-method-integration-integrationresponse-responseparameters""", alias="ResponseParameters")
    ResponseTemplates_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration-integrationresponse.html#cfn-apigateway-method-integration-integrationresponse-responsetemplates""", alias="ResponseTemplates")
    SelectionPattern_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration-integrationresponse.html#cfn-apigateway-method-integration-integrationresponse-selectionpattern""", alias="SelectionPattern")
    StatusCode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration-integrationresponse.html#cfn-apigateway-method-integration-integrationresponse-statuscode""", alias="StatusCode")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.IntegrationResponse:
        from troposphere.apigateway import IntegrationResponse as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MethodResponse(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-methodresponse.html
    Properties:
        - Name: ResponseModels
        - Name: ResponseParameters
        - Name: StatusCode
    
    """
    
    ResponseModels_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-methodresponse.html#cfn-apigateway-method-methodresponse-responsemodels""", alias="ResponseModels")
    ResponseParameters_: Optional[Dict[str, bool]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-methodresponse.html#cfn-apigateway-method-methodresponse-responseparameters""", alias="ResponseParameters")
    StatusCode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-methodresponse.html#cfn-apigateway-method-methodresponse-statuscode""", alias="StatusCode")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.MethodResponse:
        from troposphere.apigateway import MethodResponse as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EndpointConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-restapi-endpointconfiguration.html
    Properties:
        - Name: Types
        - Name: VpcEndpointIds
    
    """
    
    Types_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-restapi-endpointconfiguration.html#cfn-apigateway-restapi-endpointconfiguration-types""", alias="Types")
    VpcEndpointIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-restapi-endpointconfiguration.html#cfn-apigateway-restapi-endpointconfiguration-vpcendpointids""", alias="VpcEndpointIds")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.EndpointConfiguration:
        from troposphere.apigateway import EndpointConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-restapi-s3location.html
    Properties:
        - Name: Bucket
        - Name: ETag
        - Name: Version
        - Name: Key
    
    """
    
    Bucket_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-restapi-s3location.html#cfn-apigateway-restapi-s3location-bucket""", alias="Bucket")
    ETag_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-restapi-s3location.html#cfn-apigateway-restapi-s3location-etag""", alias="ETag")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-restapi-s3location.html#cfn-apigateway-restapi-s3location-version""", alias="Version")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-restapi-s3location.html#cfn-apigateway-restapi-s3location-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.S3Location:
        from troposphere.apigateway import S3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessLogSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-accesslogsetting.html
    Properties:
        - Name: Format
        - Name: DestinationArn
    
    """
    
    Format_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-accesslogsetting.html#cfn-apigateway-stage-accesslogsetting-format""", alias="Format")
    DestinationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-accesslogsetting.html#cfn-apigateway-stage-accesslogsetting-destinationarn""", alias="DestinationArn")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.AccessLogSetting:
        from troposphere.apigateway import AccessLogSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CanarySetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-canarysetting.html
    Properties:
        - Name: DeploymentId
        - Name: StageVariableOverrides
        - Name: PercentTraffic
        - Name: UseStageCache
    
    """
    
    DeploymentId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-canarysetting.html#cfn-apigateway-stage-canarysetting-deploymentid""", alias="DeploymentId")
    StageVariableOverrides_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-canarysetting.html#cfn-apigateway-stage-canarysetting-stagevariableoverrides""", alias="StageVariableOverrides")
    PercentTraffic_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-canarysetting.html#cfn-apigateway-stage-canarysetting-percenttraffic""", alias="PercentTraffic")
    UseStageCache_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-canarysetting.html#cfn-apigateway-stage-canarysetting-usestagecache""", alias="UseStageCache")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.CanarySetting:
        from troposphere.apigateway import CanarySetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MethodSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.html
    Properties:
        - Name: CacheTtlInSeconds
        - Name: LoggingLevel
        - Name: ResourcePath
        - Name: CacheDataEncrypted
        - Name: DataTraceEnabled
        - Name: ThrottlingBurstLimit
        - Name: CachingEnabled
        - Name: MetricsEnabled
        - Name: HttpMethod
        - Name: ThrottlingRateLimit
    
    """
    
    CacheTtlInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.html#cfn-apigateway-stage-methodsetting-cachettlinseconds""", alias="CacheTtlInSeconds")
    LoggingLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.html#cfn-apigateway-stage-methodsetting-logginglevel""", alias="LoggingLevel")
    ResourcePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.html#cfn-apigateway-stage-methodsetting-resourcepath""", alias="ResourcePath")
    CacheDataEncrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.html#cfn-apigateway-stage-methodsetting-cachedataencrypted""", alias="CacheDataEncrypted")
    DataTraceEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.html#cfn-apigateway-stage-methodsetting-datatraceenabled""", alias="DataTraceEnabled")
    ThrottlingBurstLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.html#cfn-apigateway-stage-methodsetting-throttlingburstlimit""", alias="ThrottlingBurstLimit")
    CachingEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.html#cfn-apigateway-stage-methodsetting-cachingenabled""", alias="CachingEnabled")
    MetricsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.html#cfn-apigateway-stage-methodsetting-metricsenabled""", alias="MetricsEnabled")
    HttpMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.html#cfn-apigateway-stage-methodsetting-httpmethod""", alias="HttpMethod")
    ThrottlingRateLimit_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.html#cfn-apigateway-stage-methodsetting-throttlingratelimit""", alias="ThrottlingRateLimit")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.MethodSetting:
        from troposphere.apigateway import MethodSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ApiStage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-apistage.html
    Properties:
        - Name: Stage
        - Name: ApiId
        - Name: Throttle
    
    """
    
    Stage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-apistage.html#cfn-apigateway-usageplan-apistage-stage""", alias="Stage")
    ApiId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-apistage.html#cfn-apigateway-usageplan-apistage-apiid""", alias="ApiId")
    Throttle_: Optional[Dict[str, 'ThrottleSettings']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-apistage.html#cfn-apigateway-usageplan-apistage-throttle""", alias="Throttle")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.ApiStage:
        from troposphere.apigateway import ApiStage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QuotaSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-quotasettings.html
    Properties:
        - Name: Period
        - Name: Limit
        - Name: Offset
    
    """
    
    Period_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-quotasettings.html#cfn-apigateway-usageplan-quotasettings-period""", alias="Period")
    Limit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-quotasettings.html#cfn-apigateway-usageplan-quotasettings-limit""", alias="Limit")
    Offset_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-quotasettings.html#cfn-apigateway-usageplan-quotasettings-offset""", alias="Offset")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.QuotaSettings:
        from troposphere.apigateway import QuotaSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ThrottleSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-throttlesettings.html
    Properties:
        - Name: BurstLimit
        - Name: RateLimit
    
    """
    
    BurstLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-throttlesettings.html#cfn-apigateway-usageplan-throttlesettings-burstlimit""", alias="BurstLimit")
    RateLimit_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-throttlesettings.html#cfn-apigateway-usageplan-throttlesettings-ratelimit""", alias="RateLimit")
    


    @property
    def tropo_type(self) -> troposphere.apigateway.ThrottleSettings:
        from troposphere.apigateway import ThrottleSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Account(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-account.html
    Properties:
        - Name: CloudWatchRoleArn
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CloudWatchRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-account.html#cfn-apigateway-account-cloudwatchrolearn""", alias="CloudWatchRoleArn")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.Account:
        from troposphere.apigateway import Account as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import Account as TropoT
        return resource_to_troposphere(self, TropoT)


class ApiKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.html
    Properties:
        - Name: Description
        - Name: StageKeys
        - Name: Value
        - Name: Enabled
        - Name: CustomerId
        - Name: GenerateDistinctId
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: APIKeyId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.html#cfn-apigateway-apikey-description""", alias="Description")
    StageKeys_: Optional[List['StageKey']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.html#cfn-apigateway-apikey-stagekeys""", alias="StageKeys")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.html#cfn-apigateway-apikey-value""", alias="Value")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.html#cfn-apigateway-apikey-enabled""", alias="Enabled")
    CustomerId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.html#cfn-apigateway-apikey-customerid""", alias="CustomerId")
    GenerateDistinctId_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.html#cfn-apigateway-apikey-generatedistinctid""", alias="GenerateDistinctId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.html#cfn-apigateway-apikey-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.html#cfn-apigateway-apikey-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.ApiKey:
        from troposphere.apigateway import ApiKey as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import ApiKey as TropoT
        return resource_to_troposphere(self, TropoT)


class Authorizer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html
    Properties:
        - Name: ProviderARNs
        - Name: AuthorizerCredentials
        - Name: IdentityValidationExpression
        - Name: Type
        - Name: AuthorizerUri
        - Name: AuthorizerResultTtlInSeconds
        - Name: RestApiId
        - Name: IdentitySource
        - Name: AuthType
        - Name: Name
    Attributes:
        - Name: AuthorizerId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ProviderARNs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html#cfn-apigateway-authorizer-providerarns""", alias="ProviderARNs")
    AuthorizerCredentials_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html#cfn-apigateway-authorizer-authorizercredentials""", alias="AuthorizerCredentials")
    IdentityValidationExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html#cfn-apigateway-authorizer-identityvalidationexpression""", alias="IdentityValidationExpression")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html#cfn-apigateway-authorizer-type""", alias="Type")
    AuthorizerUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html#cfn-apigateway-authorizer-authorizeruri""", alias="AuthorizerUri")
    AuthorizerResultTtlInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html#cfn-apigateway-authorizer-authorizerresultttlinseconds""", alias="AuthorizerResultTtlInSeconds")
    RestApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html#cfn-apigateway-authorizer-restapiid""", alias="RestApiId")
    IdentitySource_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html#cfn-apigateway-authorizer-identitysource""", alias="IdentitySource")
    AuthType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html#cfn-apigateway-authorizer-authtype""", alias="AuthType")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html#cfn-apigateway-authorizer-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.Authorizer:
        from troposphere.apigateway import Authorizer as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import Authorizer as TropoT
        return resource_to_troposphere(self, TropoT)


class BasePathMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-basepathmapping.html
    Properties:
        - Name: DomainName
        - Name: RestApiId
        - Name: Stage
        - Name: BasePath
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-basepathmapping.html#cfn-apigateway-basepathmapping-domainname""", alias="DomainName")
    RestApiId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-basepathmapping.html#cfn-apigateway-basepathmapping-restapiid""", alias="RestApiId")
    Stage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-basepathmapping.html#cfn-apigateway-basepathmapping-stage""", alias="Stage")
    BasePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-basepathmapping.html#cfn-apigateway-basepathmapping-basepath""", alias="BasePath")
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-basepathmapping.html#cfn-apigateway-basepathmapping-id""", alias="Id")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.BasePathMapping:
        from troposphere.apigateway import BasePathMapping as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import BasePathMapping as TropoT
        return resource_to_troposphere(self, TropoT)


class ClientCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-clientcertificate.html
    Properties:
        - Name: Description
        - Name: Tags
    Attributes:
        - Name: ClientCertificateId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-clientcertificate.html#cfn-apigateway-clientcertificate-description""", alias="Description")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-clientcertificate.html#cfn-apigateway-clientcertificate-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.ClientCertificate:
        from troposphere.apigateway import ClientCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import ClientCertificate as TropoT
        return resource_to_troposphere(self, TropoT)


class Deployment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-deployment.html
    Properties:
        - Name: Description
        - Name: StageDescription
        - Name: StageName
        - Name: RestApiId
        - Name: DeploymentCanarySettings
    Attributes:
        - Name: DeploymentId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-deployment.html#cfn-apigateway-deployment-description""", alias="Description")
    StageDescription_: Optional['StageDescription'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-deployment.html#cfn-apigateway-deployment-stagedescription""", alias="StageDescription")
    StageName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-deployment.html#cfn-apigateway-deployment-stagename""", alias="StageName")
    RestApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-deployment.html#cfn-apigateway-deployment-restapiid""", alias="RestApiId")
    DeploymentCanarySettings_: Optional['DeploymentCanarySettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-deployment.html#cfn-apigateway-deployment-deploymentcanarysettings""", alias="DeploymentCanarySettings")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.Deployment:
        from troposphere.apigateway import Deployment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import Deployment as TropoT
        return resource_to_troposphere(self, TropoT)


class DocumentationPart(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationpart.html
    Properties:
        - Name: RestApiId
        - Name: Properties
        - Name: Location
    Attributes:
        - Name: DocumentationPartId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RestApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationpart.html#cfn-apigateway-documentationpart-restapiid""", alias="RestApiId")
    Properties_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationpart.html#cfn-apigateway-documentationpart-properties""", alias="Properties")
    Location_: 'Location' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationpart.html#cfn-apigateway-documentationpart-location""", alias="Location")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.DocumentationPart:
        from troposphere.apigateway import DocumentationPart as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import DocumentationPart as TropoT
        return resource_to_troposphere(self, TropoT)


class DocumentationVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationversion.html
    Properties:
        - Name: Description
        - Name: DocumentationVersion
        - Name: RestApiId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationversion.html#cfn-apigateway-documentationversion-description""", alias="Description")
    DocumentationVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationversion.html#cfn-apigateway-documentationversion-documentationversion""", alias="DocumentationVersion")
    RestApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationversion.html#cfn-apigateway-documentationversion-restapiid""", alias="RestApiId")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.DocumentationVersion:
        from troposphere.apigateway import DocumentationVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import DocumentationVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class DomainName(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html
    Properties:
        - Name: MutualTlsAuthentication
        - Name: OwnershipVerificationCertificateArn
        - Name: DomainName
        - Name: SecurityPolicy
        - Name: EndpointConfiguration
        - Name: RegionalCertificateArn
        - Name: Tags
        - Name: CertificateArn
    Attributes:
        - Name: RegionalHostedZoneId
        - Name: RegionalDomainName
        - Name: DistributionHostedZoneId
        - Name: DistributionDomainName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MutualTlsAuthentication_: Optional['MutualTlsAuthentication'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-mutualtlsauthentication""", alias="MutualTlsAuthentication")
    OwnershipVerificationCertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-ownershipverificationcertificatearn""", alias="OwnershipVerificationCertificateArn")
    DomainName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-domainname""", alias="DomainName")
    SecurityPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-securitypolicy""", alias="SecurityPolicy")
    EndpointConfiguration_: Optional['EndpointConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-endpointconfiguration""", alias="EndpointConfiguration")
    RegionalCertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-regionalcertificatearn""", alias="RegionalCertificateArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-tags""", alias="Tags")
    CertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-certificatearn""", alias="CertificateArn")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.DomainName:
        from troposphere.apigateway import DomainName as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import DomainName as TropoT
        return resource_to_troposphere(self, TropoT)


class GatewayResponse(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-gatewayresponse.html
    Properties:
        - Name: ResponseTemplates
        - Name: ResponseParameters
        - Name: RestApiId
        - Name: StatusCode
        - Name: ResponseType
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResponseTemplates_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-gatewayresponse.html#cfn-apigateway-gatewayresponse-responsetemplates""", alias="ResponseTemplates")
    ResponseParameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-gatewayresponse.html#cfn-apigateway-gatewayresponse-responseparameters""", alias="ResponseParameters")
    RestApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-gatewayresponse.html#cfn-apigateway-gatewayresponse-restapiid""", alias="RestApiId")
    StatusCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-gatewayresponse.html#cfn-apigateway-gatewayresponse-statuscode""", alias="StatusCode")
    ResponseType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-gatewayresponse.html#cfn-apigateway-gatewayresponse-responsetype""", alias="ResponseType")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.GatewayResponse:
        from troposphere.apigateway import GatewayResponse as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import GatewayResponse as TropoT
        return resource_to_troposphere(self, TropoT)


class Method(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html
    Properties:
        - Name: ApiKeyRequired
        - Name: AuthorizationScopes
        - Name: AuthorizationType
        - Name: AuthorizerId
        - Name: HttpMethod
        - Name: Integration
        - Name: MethodResponses
        - Name: OperationName
        - Name: RequestModels
        - Name: RequestParameters
        - Name: RequestValidatorId
        - Name: ResourceId
        - Name: RestApiId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApiKeyRequired_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html#cfn-apigateway-method-apikeyrequired""", alias="ApiKeyRequired")
    AuthorizationScopes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html#cfn-apigateway-method-authorizationscopes""", alias="AuthorizationScopes")
    AuthorizationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html#cfn-apigateway-method-authorizationtype""", alias="AuthorizationType")
    AuthorizerId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html#cfn-apigateway-method-authorizerid""", alias="AuthorizerId")
    HttpMethod_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html#cfn-apigateway-method-httpmethod""", alias="HttpMethod")
    Integration_: Optional['Integration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html#cfn-apigateway-method-integration""", alias="Integration")
    MethodResponses_: Optional[List['MethodResponse']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html#cfn-apigateway-method-methodresponses""", alias="MethodResponses")
    OperationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html#cfn-apigateway-method-operationname""", alias="OperationName")
    RequestModels_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html#cfn-apigateway-method-requestmodels""", alias="RequestModels")
    RequestParameters_: Optional[Dict[str, bool]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html#cfn-apigateway-method-requestparameters""", alias="RequestParameters")
    RequestValidatorId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html#cfn-apigateway-method-requestvalidatorid""", alias="RequestValidatorId")
    ResourceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html#cfn-apigateway-method-resourceid""", alias="ResourceId")
    RestApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html#cfn-apigateway-method-restapiid""", alias="RestApiId")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.Method:
        from troposphere.apigateway import Method as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import Method as TropoT
        return resource_to_troposphere(self, TropoT)


class Model(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-model.html
    Properties:
        - Name: Description
        - Name: ContentType
        - Name: Schema
        - Name: RestApiId
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-model.html#cfn-apigateway-model-description""", alias="Description")
    ContentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-model.html#cfn-apigateway-model-contenttype""", alias="ContentType")
    Schema_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-model.html#cfn-apigateway-model-schema""", alias="Schema")
    RestApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-model.html#cfn-apigateway-model-restapiid""", alias="RestApiId")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-model.html#cfn-apigateway-model-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.Model:
        from troposphere.apigateway import Model as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import Model as TropoT
        return resource_to_troposphere(self, TropoT)


class RequestValidator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-requestvalidator.html
    Properties:
        - Name: ValidateRequestParameters
        - Name: RestApiId
        - Name: ValidateRequestBody
        - Name: Name
    Attributes:
        - Name: RequestValidatorId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ValidateRequestParameters_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-requestvalidator.html#cfn-apigateway-requestvalidator-validaterequestparameters""", alias="ValidateRequestParameters")
    RestApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-requestvalidator.html#cfn-apigateway-requestvalidator-restapiid""", alias="RestApiId")
    ValidateRequestBody_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-requestvalidator.html#cfn-apigateway-requestvalidator-validaterequestbody""", alias="ValidateRequestBody")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-requestvalidator.html#cfn-apigateway-requestvalidator-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.RequestValidator:
        from troposphere.apigateway import RequestValidator as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import RequestValidator as TropoT
        return resource_to_troposphere(self, TropoT)


class Resource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-resource.html
    Properties:
        - Name: ParentId
        - Name: PathPart
        - Name: RestApiId
    Attributes:
        - Name: ResourceId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ParentId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-resource.html#cfn-apigateway-resource-parentid""", alias="ParentId")
    PathPart_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-resource.html#cfn-apigateway-resource-pathpart""", alias="PathPart")
    RestApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-resource.html#cfn-apigateway-resource-restapiid""", alias="RestApiId")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.Resource:
        from troposphere.apigateway import Resource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import Resource as TropoT
        return resource_to_troposphere(self, TropoT)


class RestApi(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html
    Properties:
        - Name: Policy
        - Name: BodyS3Location
        - Name: Description
        - Name: MinimumCompressionSize
        - Name: Parameters
        - Name: CloneFrom
        - Name: Mode
        - Name: DisableExecuteApiEndpoint
        - Name: FailOnWarnings
        - Name: BinaryMediaTypes
        - Name: Name
        - Name: ApiKeySourceType
        - Name: EndpointConfiguration
        - Name: Body
        - Name: Tags
    Attributes:
        - Name: RootResourceId
        - Name: RestApiId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-policy""", alias="Policy")
    BodyS3Location_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-bodys3location""", alias="BodyS3Location")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-description""", alias="Description")
    MinimumCompressionSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-minimumcompressionsize""", alias="MinimumCompressionSize")
    Parameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-parameters""", alias="Parameters")
    CloneFrom_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-clonefrom""", alias="CloneFrom")
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-mode""", alias="Mode")
    DisableExecuteApiEndpoint_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-disableexecuteapiendpoint""", alias="DisableExecuteApiEndpoint")
    FailOnWarnings_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-failonwarnings""", alias="FailOnWarnings")
    BinaryMediaTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-binarymediatypes""", alias="BinaryMediaTypes")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-name""", alias="Name")
    ApiKeySourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-apikeysourcetype""", alias="ApiKeySourceType")
    EndpointConfiguration_: Optional['EndpointConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-endpointconfiguration""", alias="EndpointConfiguration")
    Body_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-body""", alias="Body")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html#cfn-apigateway-restapi-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.RestApi:
        from troposphere.apigateway import RestApi as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import RestApi as TropoT
        return resource_to_troposphere(self, TropoT)


class Stage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html
    Properties:
        - Name: DeploymentId
        - Name: Description
        - Name: StageName
        - Name: RestApiId
        - Name: CanarySetting
        - Name: ClientCertificateId
        - Name: Variables
        - Name: DocumentationVersion
        - Name: TracingEnabled
        - Name: MethodSettings
        - Name: AccessLogSetting
        - Name: CacheClusterSize
        - Name: Tags
        - Name: CacheClusterEnabled
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DeploymentId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-deploymentid""", alias="DeploymentId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-description""", alias="Description")
    StageName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-stagename""", alias="StageName")
    RestApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-restapiid""", alias="RestApiId")
    CanarySetting_: Optional['CanarySetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-canarysetting""", alias="CanarySetting")
    ClientCertificateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-clientcertificateid""", alias="ClientCertificateId")
    Variables_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-variables""", alias="Variables")
    DocumentationVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-documentationversion""", alias="DocumentationVersion")
    TracingEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-tracingenabled""", alias="TracingEnabled")
    MethodSettings_: Optional[List['MethodSetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-methodsettings""", alias="MethodSettings")
    AccessLogSetting_: Optional['AccessLogSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-accesslogsetting""", alias="AccessLogSetting")
    CacheClusterSize_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-cacheclustersize""", alias="CacheClusterSize")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-tags""", alias="Tags")
    CacheClusterEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html#cfn-apigateway-stage-cacheclusterenabled""", alias="CacheClusterEnabled")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.Stage:
        from troposphere.apigateway import Stage as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import Stage as TropoT
        return resource_to_troposphere(self, TropoT)


class UsagePlan(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html
    Properties:
        - Name: Description
        - Name: Quota
        - Name: ApiStages
        - Name: Tags
        - Name: Throttle
        - Name: UsagePlanName
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html#cfn-apigateway-usageplan-description""", alias="Description")
    Quota_: Optional['QuotaSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html#cfn-apigateway-usageplan-quota""", alias="Quota")
    ApiStages_: Optional[List['ApiStage']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html#cfn-apigateway-usageplan-apistages""", alias="ApiStages")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html#cfn-apigateway-usageplan-tags""", alias="Tags")
    Throttle_: Optional['ThrottleSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html#cfn-apigateway-usageplan-throttle""", alias="Throttle")
    UsagePlanName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html#cfn-apigateway-usageplan-usageplanname""", alias="UsagePlanName")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.UsagePlan:
        from troposphere.apigateway import UsagePlan as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import UsagePlan as TropoT
        return resource_to_troposphere(self, TropoT)


class UsagePlanKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplankey.html
    Properties:
        - Name: KeyType
        - Name: UsagePlanId
        - Name: KeyId
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KeyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplankey.html#cfn-apigateway-usageplankey-keytype""", alias="KeyType")
    UsagePlanId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplankey.html#cfn-apigateway-usageplankey-usageplanid""", alias="UsagePlanId")
    KeyId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplankey.html#cfn-apigateway-usageplankey-keyid""", alias="KeyId")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.UsagePlanKey:
        from troposphere.apigateway import UsagePlanKey as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import UsagePlanKey as TropoT
        return resource_to_troposphere(self, TropoT)


class VpcLink(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-vpclink.html
    Properties:
        - Name: Description
        - Name: TargetArns
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: VpcLinkId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-vpclink.html#cfn-apigateway-vpclink-description""", alias="Description")
    TargetArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-vpclink.html#cfn-apigateway-vpclink-targetarns""", alias="TargetArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-vpclink.html#cfn-apigateway-vpclink-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-vpclink.html#cfn-apigateway-vpclink-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.apigateway.VpcLink:
        from troposphere.apigateway import VpcLink as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigateway import VpcLink as TropoT
        return resource_to_troposphere(self, TropoT)

