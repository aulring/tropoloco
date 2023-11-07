from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-action.html
    Properties:
        - Name: Order
        - Name: TargetGroupArn
        - Name: FixedResponseConfig
        - Name: AuthenticateCognitoConfig
        - Name: Type
        - Name: RedirectConfig
        - Name: ForwardConfig
        - Name: AuthenticateOidcConfig
    
    """
    
    Order_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-action.html#cfn-elasticloadbalancingv2-listener-action-order""", alias="Order")
    TargetGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-action.html#cfn-elasticloadbalancingv2-listener-action-targetgrouparn""", alias="TargetGroupArn")
    FixedResponseConfig_: Optional['FixedResponseConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-action.html#cfn-elasticloadbalancingv2-listener-action-fixedresponseconfig""", alias="FixedResponseConfig")
    AuthenticateCognitoConfig_: Optional['AuthenticateCognitoConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-action.html#cfn-elasticloadbalancingv2-listener-action-authenticatecognitoconfig""", alias="AuthenticateCognitoConfig")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-action.html#cfn-elasticloadbalancingv2-listener-action-type""", alias="Type")
    RedirectConfig_: Optional['RedirectConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-action.html#cfn-elasticloadbalancingv2-listener-action-redirectconfig""", alias="RedirectConfig")
    ForwardConfig_: Optional['ForwardConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-action.html#cfn-elasticloadbalancingv2-listener-action-forwardconfig""", alias="ForwardConfig")
    AuthenticateOidcConfig_: Optional['AuthenticateOidcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-action.html#cfn-elasticloadbalancingv2-listener-action-authenticateoidcconfig""", alias="AuthenticateOidcConfig")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.Action:
        from troposphere.elasticloadbalancingv2 import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuthenticateCognitoConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticatecognitoconfig.html
    Properties:
        - Name: OnUnauthenticatedRequest
        - Name: UserPoolClientId
        - Name: UserPoolDomain
        - Name: SessionTimeout
        - Name: Scope
        - Name: SessionCookieName
        - Name: UserPoolArn
        - Name: AuthenticationRequestExtraParams
    
    """
    
    OnUnauthenticatedRequest_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listener-authenticatecognitoconfig-onunauthenticatedrequest""", alias="OnUnauthenticatedRequest")
    UserPoolClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listener-authenticatecognitoconfig-userpoolclientid""", alias="UserPoolClientId")
    UserPoolDomain_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listener-authenticatecognitoconfig-userpooldomain""", alias="UserPoolDomain")
    SessionTimeout_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listener-authenticatecognitoconfig-sessiontimeout""", alias="SessionTimeout")
    Scope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listener-authenticatecognitoconfig-scope""", alias="Scope")
    SessionCookieName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listener-authenticatecognitoconfig-sessioncookiename""", alias="SessionCookieName")
    UserPoolArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listener-authenticatecognitoconfig-userpoolarn""", alias="UserPoolArn")
    AuthenticationRequestExtraParams_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listener-authenticatecognitoconfig-authenticationrequestextraparams""", alias="AuthenticationRequestExtraParams")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.AuthenticateCognitoConfig:
        from troposphere.elasticloadbalancingv2 import AuthenticateCognitoConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuthenticateOidcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticateoidcconfig.html
    Properties:
        - Name: OnUnauthenticatedRequest
        - Name: TokenEndpoint
        - Name: UseExistingClientSecret
        - Name: SessionTimeout
        - Name: Scope
        - Name: Issuer
        - Name: ClientSecret
        - Name: UserInfoEndpoint
        - Name: ClientId
        - Name: AuthorizationEndpoint
        - Name: SessionCookieName
        - Name: AuthenticationRequestExtraParams
    
    """
    
    OnUnauthenticatedRequest_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listener-authenticateoidcconfig-onunauthenticatedrequest""", alias="OnUnauthenticatedRequest")
    TokenEndpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listener-authenticateoidcconfig-tokenendpoint""", alias="TokenEndpoint")
    UseExistingClientSecret_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listener-authenticateoidcconfig-useexistingclientsecret""", alias="UseExistingClientSecret")
    SessionTimeout_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listener-authenticateoidcconfig-sessiontimeout""", alias="SessionTimeout")
    Scope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listener-authenticateoidcconfig-scope""", alias="Scope")
    Issuer_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listener-authenticateoidcconfig-issuer""", alias="Issuer")
    ClientSecret_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listener-authenticateoidcconfig-clientsecret""", alias="ClientSecret")
    UserInfoEndpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listener-authenticateoidcconfig-userinfoendpoint""", alias="UserInfoEndpoint")
    ClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listener-authenticateoidcconfig-clientid""", alias="ClientId")
    AuthorizationEndpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listener-authenticateoidcconfig-authorizationendpoint""", alias="AuthorizationEndpoint")
    SessionCookieName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listener-authenticateoidcconfig-sessioncookiename""", alias="SessionCookieName")
    AuthenticationRequestExtraParams_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listener-authenticateoidcconfig-authenticationrequestextraparams""", alias="AuthenticationRequestExtraParams")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.AuthenticateOidcConfig:
        from troposphere.elasticloadbalancingv2 import AuthenticateOidcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Certificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-certificate.html
    Properties:
        - Name: CertificateArn
    
    """
    
    CertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-certificate.html#cfn-elasticloadbalancingv2-listener-certificate-certificatearn""", alias="CertificateArn")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.Certificate:
        from troposphere.elasticloadbalancingv2 import Certificate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FixedResponseConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-fixedresponseconfig.html
    Properties:
        - Name: ContentType
        - Name: StatusCode
        - Name: MessageBody
    
    """
    
    ContentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-fixedresponseconfig.html#cfn-elasticloadbalancingv2-listener-fixedresponseconfig-contenttype""", alias="ContentType")
    StatusCode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-fixedresponseconfig.html#cfn-elasticloadbalancingv2-listener-fixedresponseconfig-statuscode""", alias="StatusCode")
    MessageBody_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-fixedresponseconfig.html#cfn-elasticloadbalancingv2-listener-fixedresponseconfig-messagebody""", alias="MessageBody")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.FixedResponseConfig:
        from troposphere.elasticloadbalancingv2 import FixedResponseConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ForwardConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-forwardconfig.html
    Properties:
        - Name: TargetGroupStickinessConfig
        - Name: TargetGroups
    
    """
    
    TargetGroupStickinessConfig_: Optional['TargetGroupStickinessConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-forwardconfig.html#cfn-elasticloadbalancingv2-listener-forwardconfig-targetgroupstickinessconfig""", alias="TargetGroupStickinessConfig")
    TargetGroups_: Optional[List['TargetGroupTuple']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-forwardconfig.html#cfn-elasticloadbalancingv2-listener-forwardconfig-targetgroups""", alias="TargetGroups")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.ForwardConfig:
        from troposphere.elasticloadbalancingv2 import ForwardConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RedirectConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-redirectconfig.html
    Properties:
        - Name: Path
        - Name: Query
        - Name: Port
        - Name: Host
        - Name: Protocol
        - Name: StatusCode
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-redirectconfig.html#cfn-elasticloadbalancingv2-listener-redirectconfig-path""", alias="Path")
    Query_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-redirectconfig.html#cfn-elasticloadbalancingv2-listener-redirectconfig-query""", alias="Query")
    Port_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-redirectconfig.html#cfn-elasticloadbalancingv2-listener-redirectconfig-port""", alias="Port")
    Host_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-redirectconfig.html#cfn-elasticloadbalancingv2-listener-redirectconfig-host""", alias="Host")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-redirectconfig.html#cfn-elasticloadbalancingv2-listener-redirectconfig-protocol""", alias="Protocol")
    StatusCode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-redirectconfig.html#cfn-elasticloadbalancingv2-listener-redirectconfig-statuscode""", alias="StatusCode")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.RedirectConfig:
        from troposphere.elasticloadbalancingv2 import RedirectConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetGroupStickinessConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-targetgroupstickinessconfig.html
    Properties:
        - Name: Enabled
        - Name: DurationSeconds
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-targetgroupstickinessconfig.html#cfn-elasticloadbalancingv2-listener-targetgroupstickinessconfig-enabled""", alias="Enabled")
    DurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-targetgroupstickinessconfig.html#cfn-elasticloadbalancingv2-listener-targetgroupstickinessconfig-durationseconds""", alias="DurationSeconds")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.TargetGroupStickinessConfig:
        from troposphere.elasticloadbalancingv2 import TargetGroupStickinessConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetGroupTuple(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-targetgrouptuple.html
    Properties:
        - Name: TargetGroupArn
        - Name: Weight
    
    """
    
    TargetGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-targetgrouptuple.html#cfn-elasticloadbalancingv2-listener-targetgrouptuple-targetgrouparn""", alias="TargetGroupArn")
    Weight_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-targetgrouptuple.html#cfn-elasticloadbalancingv2-listener-targetgrouptuple-weight""", alias="Weight")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.TargetGroupTuple:
        from troposphere.elasticloadbalancingv2 import TargetGroupTuple as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Certificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-certificates.html
    Properties:
        - Name: CertificateArn
    
    """
    
    CertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-certificates.html#cfn-elasticloadbalancingv2-listener-certificates-certificatearn""", alias="CertificateArn")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.Certificate:
        from troposphere.elasticloadbalancingv2 import Certificate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-action.html
    Properties:
        - Name: Order
        - Name: TargetGroupArn
        - Name: FixedResponseConfig
        - Name: AuthenticateCognitoConfig
        - Name: Type
        - Name: RedirectConfig
        - Name: ForwardConfig
        - Name: AuthenticateOidcConfig
    
    """
    
    Order_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-action.html#cfn-elasticloadbalancingv2-listenerrule-action-order""", alias="Order")
    TargetGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-action.html#cfn-elasticloadbalancingv2-listenerrule-action-targetgrouparn""", alias="TargetGroupArn")
    FixedResponseConfig_: Optional['FixedResponseConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-action.html#cfn-elasticloadbalancingv2-listenerrule-action-fixedresponseconfig""", alias="FixedResponseConfig")
    AuthenticateCognitoConfig_: Optional['AuthenticateCognitoConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-action.html#cfn-elasticloadbalancingv2-listenerrule-action-authenticatecognitoconfig""", alias="AuthenticateCognitoConfig")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-action.html#cfn-elasticloadbalancingv2-listenerrule-action-type""", alias="Type")
    RedirectConfig_: Optional['RedirectConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-action.html#cfn-elasticloadbalancingv2-listenerrule-action-redirectconfig""", alias="RedirectConfig")
    ForwardConfig_: Optional['ForwardConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-action.html#cfn-elasticloadbalancingv2-listenerrule-action-forwardconfig""", alias="ForwardConfig")
    AuthenticateOidcConfig_: Optional['AuthenticateOidcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-action.html#cfn-elasticloadbalancingv2-listenerrule-action-authenticateoidcconfig""", alias="AuthenticateOidcConfig")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.Action:
        from troposphere.elasticloadbalancingv2 import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuthenticateCognitoConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig.html
    Properties:
        - Name: OnUnauthenticatedRequest
        - Name: UserPoolClientId
        - Name: UserPoolDomain
        - Name: SessionTimeout
        - Name: Scope
        - Name: SessionCookieName
        - Name: UserPoolArn
        - Name: AuthenticationRequestExtraParams
    
    """
    
    OnUnauthenticatedRequest_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-onunauthenticatedrequest""", alias="OnUnauthenticatedRequest")
    UserPoolClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-userpoolclientid""", alias="UserPoolClientId")
    UserPoolDomain_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-userpooldomain""", alias="UserPoolDomain")
    SessionTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-sessiontimeout""", alias="SessionTimeout")
    Scope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-scope""", alias="Scope")
    SessionCookieName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-sessioncookiename""", alias="SessionCookieName")
    UserPoolArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-userpoolarn""", alias="UserPoolArn")
    AuthenticationRequestExtraParams_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticatecognitoconfig-authenticationrequestextraparams""", alias="AuthenticationRequestExtraParams")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.AuthenticateCognitoConfig:
        from troposphere.elasticloadbalancingv2 import AuthenticateCognitoConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuthenticateOidcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.html
    Properties:
        - Name: OnUnauthenticatedRequest
        - Name: TokenEndpoint
        - Name: UseExistingClientSecret
        - Name: SessionTimeout
        - Name: Scope
        - Name: Issuer
        - Name: ClientSecret
        - Name: UserInfoEndpoint
        - Name: ClientId
        - Name: AuthorizationEndpoint
        - Name: SessionCookieName
        - Name: AuthenticationRequestExtraParams
    
    """
    
    OnUnauthenticatedRequest_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticateoidcconfig-onunauthenticatedrequest""", alias="OnUnauthenticatedRequest")
    TokenEndpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticateoidcconfig-tokenendpoint""", alias="TokenEndpoint")
    UseExistingClientSecret_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticateoidcconfig-useexistingclientsecret""", alias="UseExistingClientSecret")
    SessionTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticateoidcconfig-sessiontimeout""", alias="SessionTimeout")
    Scope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticateoidcconfig-scope""", alias="Scope")
    Issuer_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticateoidcconfig-issuer""", alias="Issuer")
    ClientSecret_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticateoidcconfig-clientsecret""", alias="ClientSecret")
    UserInfoEndpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticateoidcconfig-userinfoendpoint""", alias="UserInfoEndpoint")
    ClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticateoidcconfig-clientid""", alias="ClientId")
    AuthorizationEndpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticateoidcconfig-authorizationendpoint""", alias="AuthorizationEndpoint")
    SessionCookieName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticateoidcconfig-sessioncookiename""", alias="SessionCookieName")
    AuthenticationRequestExtraParams_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-authenticateoidcconfig.html#cfn-elasticloadbalancingv2-listenerrule-authenticateoidcconfig-authenticationrequestextraparams""", alias="AuthenticationRequestExtraParams")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.AuthenticateOidcConfig:
        from troposphere.elasticloadbalancingv2 import AuthenticateOidcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FixedResponseConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig.html
    Properties:
        - Name: ContentType
        - Name: StatusCode
        - Name: MessageBody
    
    """
    
    ContentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig.html#cfn-elasticloadbalancingv2-listenerrule-fixedresponseconfig-contenttype""", alias="ContentType")
    StatusCode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig.html#cfn-elasticloadbalancingv2-listenerrule-fixedresponseconfig-statuscode""", alias="StatusCode")
    MessageBody_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-fixedresponseconfig.html#cfn-elasticloadbalancingv2-listenerrule-fixedresponseconfig-messagebody""", alias="MessageBody")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.FixedResponseConfig:
        from troposphere.elasticloadbalancingv2 import FixedResponseConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ForwardConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig.html
    Properties:
        - Name: TargetGroupStickinessConfig
        - Name: TargetGroups
    
    """
    
    TargetGroupStickinessConfig_: Optional['TargetGroupStickinessConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig.html#cfn-elasticloadbalancingv2-listenerrule-forwardconfig-targetgroupstickinessconfig""", alias="TargetGroupStickinessConfig")
    TargetGroups_: Optional[List['TargetGroupTuple']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig.html#cfn-elasticloadbalancingv2-listenerrule-forwardconfig-targetgroups""", alias="TargetGroups")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.ForwardConfig:
        from troposphere.elasticloadbalancingv2 import ForwardConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HostHeaderConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-hostheaderconfig.html
    Properties:
        - Name: Values
    
    """
    
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-hostheaderconfig.html#cfn-elasticloadbalancingv2-listenerrule-hostheaderconfig-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.HostHeaderConfig:
        from troposphere.elasticloadbalancingv2 import HostHeaderConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpHeaderConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-httpheaderconfig.html
    Properties:
        - Name: Values
        - Name: HttpHeaderName
    
    """
    
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-httpheaderconfig.html#cfn-elasticloadbalancingv2-listenerrule-httpheaderconfig-values""", alias="Values")
    HttpHeaderName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-httpheaderconfig.html#cfn-elasticloadbalancingv2-listenerrule-httpheaderconfig-httpheadername""", alias="HttpHeaderName")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.HttpHeaderConfig:
        from troposphere.elasticloadbalancingv2 import HttpHeaderConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpRequestMethodConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-httprequestmethodconfig.html
    Properties:
        - Name: Values
    
    """
    
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-httprequestmethodconfig.html#cfn-elasticloadbalancingv2-listenerrule-httprequestmethodconfig-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.HttpRequestMethodConfig:
        from troposphere.elasticloadbalancingv2 import HttpRequestMethodConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PathPatternConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-pathpatternconfig.html
    Properties:
        - Name: Values
    
    """
    
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-pathpatternconfig.html#cfn-elasticloadbalancingv2-listenerrule-pathpatternconfig-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.PathPatternConfig:
        from troposphere.elasticloadbalancingv2 import PathPatternConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QueryStringConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-querystringconfig.html
    Properties:
        - Name: Values
    
    """
    
    Values_: Optional[List['QueryStringKeyValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-querystringconfig.html#cfn-elasticloadbalancingv2-listenerrule-querystringconfig-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.QueryStringConfig:
        from troposphere.elasticloadbalancingv2 import QueryStringConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QueryStringKeyValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-querystringkeyvalue.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-querystringkeyvalue.html#cfn-elasticloadbalancingv2-listenerrule-querystringkeyvalue-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-querystringkeyvalue.html#cfn-elasticloadbalancingv2-listenerrule-querystringkeyvalue-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.QueryStringKeyValue:
        from troposphere.elasticloadbalancingv2 import QueryStringKeyValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RedirectConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-redirectconfig.html
    Properties:
        - Name: Path
        - Name: Query
        - Name: Port
        - Name: Host
        - Name: Protocol
        - Name: StatusCode
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-redirectconfig.html#cfn-elasticloadbalancingv2-listenerrule-redirectconfig-path""", alias="Path")
    Query_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-redirectconfig.html#cfn-elasticloadbalancingv2-listenerrule-redirectconfig-query""", alias="Query")
    Port_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-redirectconfig.html#cfn-elasticloadbalancingv2-listenerrule-redirectconfig-port""", alias="Port")
    Host_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-redirectconfig.html#cfn-elasticloadbalancingv2-listenerrule-redirectconfig-host""", alias="Host")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-redirectconfig.html#cfn-elasticloadbalancingv2-listenerrule-redirectconfig-protocol""", alias="Protocol")
    StatusCode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-redirectconfig.html#cfn-elasticloadbalancingv2-listenerrule-redirectconfig-statuscode""", alias="StatusCode")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.RedirectConfig:
        from troposphere.elasticloadbalancingv2 import RedirectConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-rulecondition.html
    Properties:
        - Name: Field
        - Name: HttpHeaderConfig
        - Name: Values
        - Name: QueryStringConfig
        - Name: HostHeaderConfig
        - Name: HttpRequestMethodConfig
        - Name: PathPatternConfig
        - Name: SourceIpConfig
    
    """
    
    Field_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-rulecondition.html#cfn-elasticloadbalancingv2-listenerrule-rulecondition-field""", alias="Field")
    HttpHeaderConfig_: Optional['HttpHeaderConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-rulecondition.html#cfn-elasticloadbalancingv2-listenerrule-rulecondition-httpheaderconfig""", alias="HttpHeaderConfig")
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-rulecondition.html#cfn-elasticloadbalancingv2-listenerrule-rulecondition-values""", alias="Values")
    QueryStringConfig_: Optional['QueryStringConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-rulecondition.html#cfn-elasticloadbalancingv2-listenerrule-rulecondition-querystringconfig""", alias="QueryStringConfig")
    HostHeaderConfig_: Optional['HostHeaderConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-rulecondition.html#cfn-elasticloadbalancingv2-listenerrule-rulecondition-hostheaderconfig""", alias="HostHeaderConfig")
    HttpRequestMethodConfig_: Optional['HttpRequestMethodConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-rulecondition.html#cfn-elasticloadbalancingv2-listenerrule-rulecondition-httprequestmethodconfig""", alias="HttpRequestMethodConfig")
    PathPatternConfig_: Optional['PathPatternConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-rulecondition.html#cfn-elasticloadbalancingv2-listenerrule-rulecondition-pathpatternconfig""", alias="PathPatternConfig")
    SourceIpConfig_: Optional['SourceIpConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-rulecondition.html#cfn-elasticloadbalancingv2-listenerrule-rulecondition-sourceipconfig""", alias="SourceIpConfig")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.RuleCondition:
        from troposphere.elasticloadbalancingv2 import RuleCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceIpConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-sourceipconfig.html
    Properties:
        - Name: Values
    
    """
    
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-sourceipconfig.html#cfn-elasticloadbalancingv2-listenerrule-sourceipconfig-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.SourceIpConfig:
        from troposphere.elasticloadbalancingv2 import SourceIpConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetGroupStickinessConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig.html
    Properties:
        - Name: Enabled
        - Name: DurationSeconds
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig.html#cfn-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig-enabled""", alias="Enabled")
    DurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig.html#cfn-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig-durationseconds""", alias="DurationSeconds")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.TargetGroupStickinessConfig:
        from troposphere.elasticloadbalancingv2 import TargetGroupStickinessConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetGroupTuple(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-targetgrouptuple.html
    Properties:
        - Name: TargetGroupArn
        - Name: Weight
    
    """
    
    TargetGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-targetgrouptuple.html#cfn-elasticloadbalancingv2-listenerrule-targetgrouptuple-targetgrouparn""", alias="TargetGroupArn")
    Weight_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-targetgrouptuple.html#cfn-elasticloadbalancingv2-listenerrule-targetgrouptuple-weight""", alias="Weight")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.TargetGroupTuple:
        from troposphere.elasticloadbalancingv2 import TargetGroupTuple as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoadBalancerAttribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-loadbalancer-loadbalancerattribute.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-loadbalancer-loadbalancerattribute.html#cfn-elasticloadbalancingv2-loadbalancer-loadbalancerattribute-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-loadbalancer-loadbalancerattribute.html#cfn-elasticloadbalancingv2-loadbalancer-loadbalancerattribute-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.LoadBalancerAttribute:
        from troposphere.elasticloadbalancingv2 import LoadBalancerAttribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SubnetMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-loadbalancer-subnetmapping.html
    Properties:
        - Name: AllocationId
        - Name: IPv6Address
        - Name: SubnetId
        - Name: PrivateIPv4Address
    
    """
    
    AllocationId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-loadbalancer-subnetmapping.html#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-allocationid""", alias="AllocationId")
    IPv6Address_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-loadbalancer-subnetmapping.html#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-ipv6address""", alias="IPv6Address")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-loadbalancer-subnetmapping.html#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-subnetid""", alias="SubnetId")
    PrivateIPv4Address_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-loadbalancer-subnetmapping.html#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-privateipv4address""", alias="PrivateIPv4Address")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.SubnetMapping:
        from troposphere.elasticloadbalancingv2 import SubnetMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Matcher(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-targetgroup-matcher.html
    Properties:
        - Name: GrpcCode
        - Name: HttpCode
    
    """
    
    GrpcCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-targetgroup-matcher.html#cfn-elasticloadbalancingv2-targetgroup-matcher-grpccode""", alias="GrpcCode")
    HttpCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-targetgroup-matcher.html#cfn-elasticloadbalancingv2-targetgroup-matcher-httpcode""", alias="HttpCode")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.Matcher:
        from troposphere.elasticloadbalancingv2 import Matcher as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetDescription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-targetgroup-targetdescription.html
    Properties:
        - Name: Port
        - Name: AvailabilityZone
        - Name: Id
    
    """
    
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-targetgroup-targetdescription.html#cfn-elasticloadbalancingv2-targetgroup-targetdescription-port""", alias="Port")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-targetgroup-targetdescription.html#cfn-elasticloadbalancingv2-targetgroup-targetdescription-availabilityzone""", alias="AvailabilityZone")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-targetgroup-targetdescription.html#cfn-elasticloadbalancingv2-targetgroup-targetdescription-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.TargetDescription:
        from troposphere.elasticloadbalancingv2 import TargetDescription as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetGroupAttribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-targetgroup-targetgroupattribute.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-targetgroup-targetgroupattribute.html#cfn-elasticloadbalancingv2-targetgroup-targetgroupattribute-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-targetgroup-targetgroupattribute.html#cfn-elasticloadbalancingv2-targetgroup-targetgroupattribute-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.TargetGroupAttribute:
        from troposphere.elasticloadbalancingv2 import TargetGroupAttribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Listener(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html
    Properties:
        - Name: AlpnPolicy
        - Name: SslPolicy
        - Name: LoadBalancerArn
        - Name: DefaultActions
        - Name: Port
        - Name: Certificates
        - Name: Protocol
    Attributes:
        - Name: ListenerArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AlpnPolicy_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html#cfn-elasticloadbalancingv2-listener-alpnpolicy""", alias="AlpnPolicy")
    SslPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html#cfn-elasticloadbalancingv2-listener-sslpolicy""", alias="SslPolicy")
    LoadBalancerArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html#cfn-elasticloadbalancingv2-listener-loadbalancerarn""", alias="LoadBalancerArn")
    DefaultActions_: List['Action'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html#cfn-elasticloadbalancingv2-listener-defaultactions""", alias="DefaultActions")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html#cfn-elasticloadbalancingv2-listener-port""", alias="Port")
    Certificates_: Optional[List['Certificate']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html#cfn-elasticloadbalancingv2-listener-certificates""", alias="Certificates")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html#cfn-elasticloadbalancingv2-listener-protocol""", alias="Protocol")
    

    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.Listener:
        from troposphere.elasticloadbalancingv2 import Listener as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticloadbalancingv2 import Listener as TropoT
        return resource_to_troposphere(self, TropoT)


class ListenerCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenercertificate.html
    Properties:
        - Name: Certificates
        - Name: ListenerArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Certificates_: List['Certificate'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenercertificate.html#cfn-elasticloadbalancingv2-listenercertificate-certificates""", alias="Certificates")
    ListenerArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenercertificate.html#cfn-elasticloadbalancingv2-listenercertificate-listenerarn""", alias="ListenerArn")
    

    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.ListenerCertificate:
        from troposphere.elasticloadbalancingv2 import ListenerCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticloadbalancingv2 import ListenerCertificate as TropoT
        return resource_to_troposphere(self, TropoT)


class ListenerRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.html
    Properties:
        - Name: ListenerArn
        - Name: Actions
        - Name: Priority
        - Name: Conditions
    Attributes:
        - Name: IsDefault
        - Name: RuleArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ListenerArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.html#cfn-elasticloadbalancingv2-listenerrule-listenerarn""", alias="ListenerArn")
    Actions_: List['Action'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.html#cfn-elasticloadbalancingv2-listenerrule-actions""", alias="Actions")
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.html#cfn-elasticloadbalancingv2-listenerrule-priority""", alias="Priority")
    Conditions_: List['RuleCondition'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.html#cfn-elasticloadbalancingv2-listenerrule-conditions""", alias="Conditions")
    

    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.ListenerRule:
        from troposphere.elasticloadbalancingv2 import ListenerRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticloadbalancingv2 import ListenerRule as TropoT
        return resource_to_troposphere(self, TropoT)


class LoadBalancer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html
    Properties:
        - Name: IpAddressType
        - Name: SecurityGroups
        - Name: LoadBalancerAttributes
        - Name: Subnets
        - Name: Type
        - Name: Scheme
        - Name: Tags
        - Name: Name
        - Name: SubnetMappings
    Attributes:
        - Name: SecurityGroups
        - Name: LoadBalancerName
        - Name: CanonicalHostedZoneID
        - Name: LoadBalancerArn
        - Name: DNSName
        - Name: LoadBalancerFullName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IpAddressType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#cfn-elasticloadbalancingv2-loadbalancer-ipaddresstype""", alias="IpAddressType")
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#cfn-elasticloadbalancingv2-loadbalancer-securitygroups""", alias="SecurityGroups")
    LoadBalancerAttributes_: Optional[List['LoadBalancerAttribute']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#cfn-elasticloadbalancingv2-loadbalancer-loadbalancerattributes""", alias="LoadBalancerAttributes")
    Subnets_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#cfn-elasticloadbalancingv2-loadbalancer-subnets""", alias="Subnets")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#cfn-elasticloadbalancingv2-loadbalancer-type""", alias="Type")
    Scheme_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#cfn-elasticloadbalancingv2-loadbalancer-scheme""", alias="Scheme")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#cfn-elasticloadbalancingv2-loadbalancer-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#cfn-elasticloadbalancingv2-loadbalancer-name""", alias="Name")
    SubnetMappings_: Optional[List['SubnetMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#cfn-elasticloadbalancingv2-loadbalancer-subnetmappings""", alias="SubnetMappings")
    

    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.LoadBalancer:
        from troposphere.elasticloadbalancingv2 import LoadBalancer as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticloadbalancingv2 import LoadBalancer as TropoT
        return resource_to_troposphere(self, TropoT)


class TargetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html
    Properties:
        - Name: IpAddressType
        - Name: HealthCheckIntervalSeconds
        - Name: Matcher
        - Name: HealthCheckPath
        - Name: Port
        - Name: Targets
        - Name: HealthCheckEnabled
        - Name: ProtocolVersion
        - Name: UnhealthyThresholdCount
        - Name: HealthCheckTimeoutSeconds
        - Name: Name
        - Name: VpcId
        - Name: HealthyThresholdCount
        - Name: HealthCheckProtocol
        - Name: TargetGroupAttributes
        - Name: TargetType
        - Name: HealthCheckPort
        - Name: Protocol
        - Name: Tags
    Attributes:
        - Name: TargetGroupArn
        - Name: LoadBalancerArns
        - Name: TargetGroupFullName
        - Name: TargetGroupName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IpAddressType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-ipaddresstype""", alias="IpAddressType")
    HealthCheckIntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-healthcheckintervalseconds""", alias="HealthCheckIntervalSeconds")
    Matcher_: Optional['Matcher'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-matcher""", alias="Matcher")
    HealthCheckPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-healthcheckpath""", alias="HealthCheckPath")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-port""", alias="Port")
    Targets_: Optional[List['TargetDescription']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-targets""", alias="Targets")
    HealthCheckEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-healthcheckenabled""", alias="HealthCheckEnabled")
    ProtocolVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-protocolversion""", alias="ProtocolVersion")
    UnhealthyThresholdCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-unhealthythresholdcount""", alias="UnhealthyThresholdCount")
    HealthCheckTimeoutSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-healthchecktimeoutseconds""", alias="HealthCheckTimeoutSeconds")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-name""", alias="Name")
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-vpcid""", alias="VpcId")
    HealthyThresholdCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-healthythresholdcount""", alias="HealthyThresholdCount")
    HealthCheckProtocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-healthcheckprotocol""", alias="HealthCheckProtocol")
    TargetGroupAttributes_: Optional[List['TargetGroupAttribute']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-targetgroupattributes""", alias="TargetGroupAttributes")
    TargetType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-targettype""", alias="TargetType")
    HealthCheckPort_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-healthcheckport""", alias="HealthCheckPort")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-protocol""", alias="Protocol")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html#cfn-elasticloadbalancingv2-targetgroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.elasticloadbalancingv2.TargetGroup:
        from troposphere.elasticloadbalancingv2 import TargetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticloadbalancingv2 import TargetGroup as TropoT
        return resource_to_troposphere(self, TropoT)

