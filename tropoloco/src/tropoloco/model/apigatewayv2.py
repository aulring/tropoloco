from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class BodyS3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html
    Properties:
        - Name: Etag
        - Name: Bucket
        - Name: Version
        - Name: Key
    
    """
    
    Etag_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-etag""", alias="Etag")
    Bucket_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-bucket""", alias="Bucket")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-version""", alias="Version")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.BodyS3Location:
        from troposphere.apigatewayv2 import BodyS3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Cors(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html
    Properties:
        - Name: AllowOrigins
        - Name: AllowCredentials
        - Name: ExposeHeaders
        - Name: AllowHeaders
        - Name: MaxAge
        - Name: AllowMethods
    
    """
    
    AllowOrigins_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-alloworigins""", alias="AllowOrigins")
    AllowCredentials_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowcredentials""", alias="AllowCredentials")
    ExposeHeaders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-exposeheaders""", alias="ExposeHeaders")
    AllowHeaders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowheaders""", alias="AllowHeaders")
    MaxAge_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-maxage""", alias="MaxAge")
    AllowMethods_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowmethods""", alias="AllowMethods")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.Cors:
        from troposphere.apigatewayv2 import Cors as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessLogSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html
    Properties:
        - Name: Format
        - Name: DestinationArn
    
    """
    
    Format_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-format""", alias="Format")
    DestinationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-destinationarn""", alias="DestinationArn")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.AccessLogSettings:
        from troposphere.apigatewayv2 import AccessLogSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IntegrationOverrides(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html
    Properties:
        - Name: Description
        - Name: PayloadFormatVersion
        - Name: TimeoutInMillis
        - Name: IntegrationMethod
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-description""", alias="Description")
    PayloadFormatVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-payloadformatversion""", alias="PayloadFormatVersion")
    TimeoutInMillis_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-timeoutinmillis""", alias="TimeoutInMillis")
    IntegrationMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-integrationmethod""", alias="IntegrationMethod")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.IntegrationOverrides:
        from troposphere.apigatewayv2 import IntegrationOverrides as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RouteOverrides(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html
    Properties:
        - Name: Target
        - Name: AuthorizerId
        - Name: OperationName
        - Name: AuthorizationScopes
        - Name: AuthorizationType
    
    """
    
    Target_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-target""", alias="Target")
    AuthorizerId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-authorizerid""", alias="AuthorizerId")
    OperationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-operationname""", alias="OperationName")
    AuthorizationScopes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-authorizationscopes""", alias="AuthorizationScopes")
    AuthorizationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-authorizationtype""", alias="AuthorizationType")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.RouteOverrides:
        from troposphere.apigatewayv2 import RouteOverrides as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RouteSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html
    Properties:
        - Name: LoggingLevel
        - Name: DataTraceEnabled
        - Name: ThrottlingBurstLimit
        - Name: DetailedMetricsEnabled
        - Name: ThrottlingRateLimit
    
    """
    
    LoggingLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-logginglevel""", alias="LoggingLevel")
    DataTraceEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-datatraceenabled""", alias="DataTraceEnabled")
    ThrottlingBurstLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingburstlimit""", alias="ThrottlingBurstLimit")
    DetailedMetricsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-detailedmetricsenabled""", alias="DetailedMetricsEnabled")
    ThrottlingRateLimit_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingratelimit""", alias="ThrottlingRateLimit")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.RouteSettings:
        from troposphere.apigatewayv2 import RouteSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StageOverrides(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html
    Properties:
        - Name: Description
        - Name: AccessLogSettings
        - Name: AutoDeploy
        - Name: RouteSettings
        - Name: StageVariables
        - Name: DefaultRouteSettings
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-description""", alias="Description")
    AccessLogSettings_: Optional['AccessLogSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-accesslogsettings""", alias="AccessLogSettings")
    AutoDeploy_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-autodeploy""", alias="AutoDeploy")
    RouteSettings_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-routesettings""", alias="RouteSettings")
    StageVariables_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-stagevariables""", alias="StageVariables")
    DefaultRouteSettings_: Optional['RouteSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-defaultroutesettings""", alias="DefaultRouteSettings")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.StageOverrides:
        from troposphere.apigatewayv2 import StageOverrides as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JWTConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html
    Properties:
        - Name: Issuer
        - Name: Audience
    
    """
    
    Issuer_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html#cfn-apigatewayv2-authorizer-jwtconfiguration-issuer""", alias="Issuer")
    Audience_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html#cfn-apigatewayv2-authorizer-jwtconfiguration-audience""", alias="Audience")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.JWTConfiguration:
        from troposphere.apigatewayv2 import JWTConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DomainNameConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html
    Properties:
        - Name: OwnershipVerificationCertificateArn
        - Name: SecurityPolicy
        - Name: EndpointType
        - Name: CertificateName
        - Name: CertificateArn
    
    """
    
    OwnershipVerificationCertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-ownershipverificationcertificatearn""", alias="OwnershipVerificationCertificateArn")
    SecurityPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-securitypolicy""", alias="SecurityPolicy")
    EndpointType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-endpointtype""", alias="EndpointType")
    CertificateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatename""", alias="CertificateName")
    CertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatearn""", alias="CertificateArn")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.DomainNameConfiguration:
        from troposphere.apigatewayv2 import DomainNameConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MutualTlsAuthentication(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html
    Properties:
        - Name: TruststoreVersion
        - Name: TruststoreUri
    
    """
    
    TruststoreVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html#cfn-apigatewayv2-domainname-mutualtlsauthentication-truststoreversion""", alias="TruststoreVersion")
    TruststoreUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html#cfn-apigatewayv2-domainname-mutualtlsauthentication-truststoreuri""", alias="TruststoreUri")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.MutualTlsAuthentication:
        from troposphere.apigatewayv2 import MutualTlsAuthentication as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResponseParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html
    Properties:
        - Name: Destination
        - Name: Source
    
    """
    
    Destination_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html#cfn-apigatewayv2-integration-responseparameter-destination""", alias="Destination")
    Source_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html#cfn-apigatewayv2-integration-responseparameter-source""", alias="Source")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.ResponseParameter:
        from troposphere.apigatewayv2 import ResponseParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResponseParameterList(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameterlist.html
    Properties:
        - Name: ResponseParameters
    
    """
    
    ResponseParameters_: Optional[List['ResponseParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameterlist.html#cfn-apigatewayv2-integration-responseparameterlist-responseparameters""", alias="ResponseParameters")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.ResponseParameterList:
        from troposphere.apigatewayv2 import ResponseParameterList as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TlsConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-tlsconfig.html
    Properties:
        - Name: ServerNameToVerify
    
    """
    
    ServerNameToVerify_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-tlsconfig.html#cfn-apigatewayv2-integration-tlsconfig-servernametoverify""", alias="ServerNameToVerify")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.TlsConfig:
        from troposphere.apigatewayv2 import TlsConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ParameterConstraints(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-routeresponse-parameterconstraints.html
    Properties:
        - Name: Required
    
    """
    
    Required_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-routeresponse-parameterconstraints.html#cfn-apigatewayv2-routeresponse-parameterconstraints-required""", alias="Required")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.ParameterConstraints:
        from troposphere.apigatewayv2 import ParameterConstraints as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessLogSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html
    Properties:
        - Name: Format
        - Name: DestinationArn
    
    """
    
    Format_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html#cfn-apigatewayv2-stage-accesslogsettings-format""", alias="Format")
    DestinationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html#cfn-apigatewayv2-stage-accesslogsettings-destinationarn""", alias="DestinationArn")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.AccessLogSettings:
        from troposphere.apigatewayv2 import AccessLogSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RouteSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html
    Properties:
        - Name: LoggingLevel
        - Name: DataTraceEnabled
        - Name: ThrottlingBurstLimit
        - Name: DetailedMetricsEnabled
        - Name: ThrottlingRateLimit
    
    """
    
    LoggingLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-logginglevel""", alias="LoggingLevel")
    DataTraceEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-datatraceenabled""", alias="DataTraceEnabled")
    ThrottlingBurstLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-throttlingburstlimit""", alias="ThrottlingBurstLimit")
    DetailedMetricsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-detailedmetricsenabled""", alias="DetailedMetricsEnabled")
    ThrottlingRateLimit_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-throttlingratelimit""", alias="ThrottlingRateLimit")
    


    @property
    def tropo_type(self) -> troposphere.apigatewayv2.RouteSettings:
        from troposphere.apigatewayv2 import RouteSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Api(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html
    Properties:
        - Name: RouteSelectionExpression
        - Name: BodyS3Location
        - Name: Description
        - Name: BasePath
        - Name: FailOnWarnings
        - Name: DisableExecuteApiEndpoint
        - Name: DisableSchemaValidation
        - Name: Name
        - Name: Target
        - Name: CredentialsArn
        - Name: CorsConfiguration
        - Name: Version
        - Name: ProtocolType
        - Name: RouteKey
        - Name: Body
        - Name: Tags
        - Name: ApiKeySelectionExpression
    Attributes:
        - Name: ApiEndpoint
        - Name: ApiId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RouteSelectionExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-routeselectionexpression""", alias="RouteSelectionExpression")
    BodyS3Location_: Optional['BodyS3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-bodys3location""", alias="BodyS3Location")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-description""", alias="Description")
    BasePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-basepath""", alias="BasePath")
    FailOnWarnings_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-failonwarnings""", alias="FailOnWarnings")
    DisableExecuteApiEndpoint_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-disableexecuteapiendpoint""", alias="DisableExecuteApiEndpoint")
    DisableSchemaValidation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-disableschemavalidation""", alias="DisableSchemaValidation")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-name""", alias="Name")
    Target_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-target""", alias="Target")
    CredentialsArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-credentialsarn""", alias="CredentialsArn")
    CorsConfiguration_: Optional['Cors'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-corsconfiguration""", alias="CorsConfiguration")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-version""", alias="Version")
    ProtocolType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-protocoltype""", alias="ProtocolType")
    RouteKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-routekey""", alias="RouteKey")
    Body_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-body""", alias="Body")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-tags""", alias="Tags")
    ApiKeySelectionExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-apikeyselectionexpression""", alias="ApiKeySelectionExpression")
    

    @property
    def tropo_type(self) -> troposphere.apigatewayv2.Api:
        from troposphere.apigatewayv2 import Api as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigatewayv2 import Api as TropoT
        return resource_to_troposphere(self, TropoT)


class ApiGatewayManagedOverrides(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html
    Properties:
        - Name: Integration
        - Name: Stage
        - Name: ApiId
        - Name: Route
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Integration_: Optional['IntegrationOverrides'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integration""", alias="Integration")
    Stage_: Optional['StageOverrides'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stage""", alias="Stage")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-apiid""", alias="ApiId")
    Route_: Optional['RouteOverrides'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-route""", alias="Route")
    

    @property
    def tropo_type(self) -> troposphere.apigatewayv2.ApiGatewayManagedOverrides:
        from troposphere.apigatewayv2 import ApiGatewayManagedOverrides as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigatewayv2 import ApiGatewayManagedOverrides as TropoT
        return resource_to_troposphere(self, TropoT)


class ApiMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html
    Properties:
        - Name: DomainName
        - Name: Stage
        - Name: ApiMappingKey
        - Name: ApiId
    Attributes:
        - Name: ApiMappingId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-domainname""", alias="DomainName")
    Stage_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-stage""", alias="Stage")
    ApiMappingKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-apimappingkey""", alias="ApiMappingKey")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-apiid""", alias="ApiId")
    

    @property
    def tropo_type(self) -> troposphere.apigatewayv2.ApiMapping:
        from troposphere.apigatewayv2 import ApiMapping as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigatewayv2 import ApiMapping as TropoT
        return resource_to_troposphere(self, TropoT)


class Authorizer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html
    Properties:
        - Name: IdentityValidationExpression
        - Name: AuthorizerUri
        - Name: AuthorizerCredentialsArn
        - Name: AuthorizerType
        - Name: JwtConfiguration
        - Name: AuthorizerResultTtlInSeconds
        - Name: IdentitySource
        - Name: AuthorizerPayloadFormatVersion
        - Name: EnableSimpleResponses
        - Name: ApiId
        - Name: Name
    Attributes:
        - Name: AuthorizerId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IdentityValidationExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-identityvalidationexpression""", alias="IdentityValidationExpression")
    AuthorizerUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizeruri""", alias="AuthorizerUri")
    AuthorizerCredentialsArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizercredentialsarn""", alias="AuthorizerCredentialsArn")
    AuthorizerType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizertype""", alias="AuthorizerType")
    JwtConfiguration_: Optional['JWTConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-jwtconfiguration""", alias="JwtConfiguration")
    AuthorizerResultTtlInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizerresultttlinseconds""", alias="AuthorizerResultTtlInSeconds")
    IdentitySource_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-identitysource""", alias="IdentitySource")
    AuthorizerPayloadFormatVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizerpayloadformatversion""", alias="AuthorizerPayloadFormatVersion")
    EnableSimpleResponses_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-enablesimpleresponses""", alias="EnableSimpleResponses")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-apiid""", alias="ApiId")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.apigatewayv2.Authorizer:
        from troposphere.apigatewayv2 import Authorizer as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigatewayv2 import Authorizer as TropoT
        return resource_to_troposphere(self, TropoT)


class Deployment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html
    Properties:
        - Name: Description
        - Name: StageName
        - Name: ApiId
    Attributes:
        - Name: DeploymentId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-description""", alias="Description")
    StageName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-stagename""", alias="StageName")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-apiid""", alias="ApiId")
    

    @property
    def tropo_type(self) -> troposphere.apigatewayv2.Deployment:
        from troposphere.apigatewayv2 import Deployment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigatewayv2 import Deployment as TropoT
        return resource_to_troposphere(self, TropoT)


class DomainName(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html
    Properties:
        - Name: MutualTlsAuthentication
        - Name: DomainName
        - Name: DomainNameConfigurations
        - Name: Tags
    Attributes:
        - Name: RegionalHostedZoneId
        - Name: RegionalDomainName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MutualTlsAuthentication_: Optional['MutualTlsAuthentication'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-mutualtlsauthentication""", alias="MutualTlsAuthentication")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-domainname""", alias="DomainName")
    DomainNameConfigurations_: Optional[List['DomainNameConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-domainnameconfigurations""", alias="DomainNameConfigurations")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.apigatewayv2.DomainName:
        from troposphere.apigatewayv2 import DomainName as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigatewayv2 import DomainName as TropoT
        return resource_to_troposphere(self, TropoT)


class Integration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html
    Properties:
        - Name: Description
        - Name: TemplateSelectionExpression
        - Name: ConnectionType
        - Name: ResponseParameters
        - Name: IntegrationMethod
        - Name: PassthroughBehavior
        - Name: RequestParameters
        - Name: ConnectionId
        - Name: IntegrationUri
        - Name: PayloadFormatVersion
        - Name: CredentialsArn
        - Name: RequestTemplates
        - Name: TimeoutInMillis
        - Name: TlsConfig
        - Name: ContentHandlingStrategy
        - Name: IntegrationSubtype
        - Name: ApiId
        - Name: IntegrationType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-description""", alias="Description")
    TemplateSelectionExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-templateselectionexpression""", alias="TemplateSelectionExpression")
    ConnectionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-connectiontype""", alias="ConnectionType")
    ResponseParameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-responseparameters""", alias="ResponseParameters")
    IntegrationMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationmethod""", alias="IntegrationMethod")
    PassthroughBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-passthroughbehavior""", alias="PassthroughBehavior")
    RequestParameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-requestparameters""", alias="RequestParameters")
    ConnectionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-connectionid""", alias="ConnectionId")
    IntegrationUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationuri""", alias="IntegrationUri")
    PayloadFormatVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-payloadformatversion""", alias="PayloadFormatVersion")
    CredentialsArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-credentialsarn""", alias="CredentialsArn")
    RequestTemplates_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-requesttemplates""", alias="RequestTemplates")
    TimeoutInMillis_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-timeoutinmillis""", alias="TimeoutInMillis")
    TlsConfig_: Optional['TlsConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-tlsconfig""", alias="TlsConfig")
    ContentHandlingStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-contenthandlingstrategy""", alias="ContentHandlingStrategy")
    IntegrationSubtype_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationsubtype""", alias="IntegrationSubtype")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-apiid""", alias="ApiId")
    IntegrationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationtype""", alias="IntegrationType")
    

    @property
    def tropo_type(self) -> troposphere.apigatewayv2.Integration:
        from troposphere.apigatewayv2 import Integration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigatewayv2 import Integration as TropoT
        return resource_to_troposphere(self, TropoT)


class IntegrationResponse(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html
    Properties:
        - Name: ResponseTemplates
        - Name: TemplateSelectionExpression
        - Name: ResponseParameters
        - Name: ContentHandlingStrategy
        - Name: IntegrationId
        - Name: IntegrationResponseKey
        - Name: ApiId
    Attributes:
        - Name: IntegrationResponseId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResponseTemplates_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-responsetemplates""", alias="ResponseTemplates")
    TemplateSelectionExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-templateselectionexpression""", alias="TemplateSelectionExpression")
    ResponseParameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-responseparameters""", alias="ResponseParameters")
    ContentHandlingStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-contenthandlingstrategy""", alias="ContentHandlingStrategy")
    IntegrationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-integrationid""", alias="IntegrationId")
    IntegrationResponseKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-integrationresponsekey""", alias="IntegrationResponseKey")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-apiid""", alias="ApiId")
    

    @property
    def tropo_type(self) -> troposphere.apigatewayv2.IntegrationResponse:
        from troposphere.apigatewayv2 import IntegrationResponse as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigatewayv2 import IntegrationResponse as TropoT
        return resource_to_troposphere(self, TropoT)


class Model(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html
    Properties:
        - Name: Description
        - Name: ContentType
        - Name: Schema
        - Name: ApiId
        - Name: Name
    Attributes:
        - Name: ModelId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-description""", alias="Description")
    ContentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-contenttype""", alias="ContentType")
    Schema_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-schema""", alias="Schema")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-apiid""", alias="ApiId")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.apigatewayv2.Model:
        from troposphere.apigatewayv2 import Model as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigatewayv2 import Model as TropoT
        return resource_to_troposphere(self, TropoT)


class Route(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html
    Properties:
        - Name: Target
        - Name: RouteResponseSelectionExpression
        - Name: RequestModels
        - Name: OperationName
        - Name: AuthorizerId
        - Name: AuthorizationScopes
        - Name: ApiKeyRequired
        - Name: RouteKey
        - Name: AuthorizationType
        - Name: ModelSelectionExpression
        - Name: ApiId
        - Name: RequestParameters
    Attributes:
        - Name: RouteId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Target_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-target""", alias="Target")
    RouteResponseSelectionExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-routeresponseselectionexpression""", alias="RouteResponseSelectionExpression")
    RequestModels_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestmodels""", alias="RequestModels")
    OperationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-operationname""", alias="OperationName")
    AuthorizerId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizerid""", alias="AuthorizerId")
    AuthorizationScopes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationscopes""", alias="AuthorizationScopes")
    ApiKeyRequired_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-apikeyrequired""", alias="ApiKeyRequired")
    RouteKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-routekey""", alias="RouteKey")
    AuthorizationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationtype""", alias="AuthorizationType")
    ModelSelectionExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-modelselectionexpression""", alias="ModelSelectionExpression")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-apiid""", alias="ApiId")
    RequestParameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestparameters""", alias="RequestParameters")
    

    @property
    def tropo_type(self) -> troposphere.apigatewayv2.Route:
        from troposphere.apigatewayv2 import Route as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigatewayv2 import Route as TropoT
        return resource_to_troposphere(self, TropoT)


class RouteResponse(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html
    Properties:
        - Name: RouteResponseKey
        - Name: ResponseParameters
        - Name: RouteId
        - Name: ModelSelectionExpression
        - Name: ApiId
        - Name: ResponseModels
    Attributes:
        - Name: RouteResponseId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RouteResponseKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-routeresponsekey""", alias="RouteResponseKey")
    ResponseParameters_: Optional[Dict[str, 'ParameterConstraints']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-responseparameters""", alias="ResponseParameters")
    RouteId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-routeid""", alias="RouteId")
    ModelSelectionExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-modelselectionexpression""", alias="ModelSelectionExpression")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-apiid""", alias="ApiId")
    ResponseModels_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-responsemodels""", alias="ResponseModels")
    

    @property
    def tropo_type(self) -> troposphere.apigatewayv2.RouteResponse:
        from troposphere.apigatewayv2 import RouteResponse as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigatewayv2 import RouteResponse as TropoT
        return resource_to_troposphere(self, TropoT)


class Stage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html
    Properties:
        - Name: ClientCertificateId
        - Name: DeploymentId
        - Name: Description
        - Name: AccessLogSettings
        - Name: AutoDeploy
        - Name: RouteSettings
        - Name: StageName
        - Name: StageVariables
        - Name: AccessPolicyId
        - Name: ApiId
        - Name: DefaultRouteSettings
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ClientCertificateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-clientcertificateid""", alias="ClientCertificateId")
    DeploymentId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-deploymentid""", alias="DeploymentId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-description""", alias="Description")
    AccessLogSettings_: Optional['AccessLogSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesslogsettings""", alias="AccessLogSettings")
    AutoDeploy_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-autodeploy""", alias="AutoDeploy")
    RouteSettings_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-routesettings""", alias="RouteSettings")
    StageName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagename""", alias="StageName")
    StageVariables_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagevariables""", alias="StageVariables")
    AccessPolicyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesspolicyid""", alias="AccessPolicyId")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-apiid""", alias="ApiId")
    DefaultRouteSettings_: Optional['RouteSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-defaultroutesettings""", alias="DefaultRouteSettings")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.apigatewayv2.Stage:
        from troposphere.apigatewayv2 import Stage as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigatewayv2 import Stage as TropoT
        return resource_to_troposphere(self, TropoT)


class VpcLink(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html
    Properties:
        - Name: SubnetIds
        - Name: SecurityGroupIds
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: VpcLinkId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-subnetids""", alias="SubnetIds")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-securitygroupids""", alias="SecurityGroupIds")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.apigatewayv2.VpcLink:
        from troposphere.apigatewayv2 import VpcLink as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.apigatewayv2 import VpcLink as TropoT
        return resource_to_troposphere(self, TropoT)

