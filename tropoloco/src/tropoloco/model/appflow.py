from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ConnectorProvisioningConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connector-connectorprovisioningconfig.html
    Properties:
        - Name: Lambda
    
    """
    
    Lambda_: Optional['LambdaConnectorProvisioningConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connector-connectorprovisioningconfig.html#cfn-appflow-connector-connectorprovisioningconfig-lambda""", alias="Lambda")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ConnectorProvisioningConfig:
        from troposphere.appflow import ConnectorProvisioningConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaConnectorProvisioningConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connector-lambdaconnectorprovisioningconfig.html
    Properties:
        - Name: LambdaArn
    
    """
    
    LambdaArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connector-lambdaconnectorprovisioningconfig.html#cfn-appflow-connector-lambdaconnectorprovisioningconfig-lambdaarn""", alias="LambdaArn")
    


    @property
    def tropo_type(self) -> troposphere.appflow.LambdaConnectorProvisioningConfig:
        from troposphere.appflow import LambdaConnectorProvisioningConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AmplitudeConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials.html
    Properties:
        - Name: SecretKey
        - Name: ApiKey
    
    """
    
    SecretKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials.html#cfn-appflow-connectorprofile-amplitudeconnectorprofilecredentials-secretkey""", alias="SecretKey")
    ApiKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials.html#cfn-appflow-connectorprofile-amplitudeconnectorprofilecredentials-apikey""", alias="ApiKey")
    


    @property
    def tropo_type(self) -> troposphere.appflow.AmplitudeConnectorProfileCredentials:
        from troposphere.appflow import AmplitudeConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ApiKeyCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-apikeycredentials.html
    Properties:
        - Name: ApiSecretKey
        - Name: ApiKey
    
    """
    
    ApiSecretKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-apikeycredentials.html#cfn-appflow-connectorprofile-apikeycredentials-apisecretkey""", alias="ApiSecretKey")
    ApiKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-apikeycredentials.html#cfn-appflow-connectorprofile-apikeycredentials-apikey""", alias="ApiKey")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ApiKeyCredentials:
        from troposphere.appflow import ApiKeyCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BasicAuthCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-basicauthcredentials.html
    Properties:
        - Name: Username
        - Name: Password
    
    """
    
    Username_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-basicauthcredentials.html#cfn-appflow-connectorprofile-basicauthcredentials-username""", alias="Username")
    Password_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-basicauthcredentials.html#cfn-appflow-connectorprofile-basicauthcredentials-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.appflow.BasicAuthCredentials:
        from troposphere.appflow import BasicAuthCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectorOAuthRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectoroauthrequest.html
    Properties:
        - Name: AuthCode
        - Name: RedirectUri
    
    """
    
    AuthCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectoroauthrequest.html#cfn-appflow-connectorprofile-connectoroauthrequest-authcode""", alias="AuthCode")
    RedirectUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectoroauthrequest.html#cfn-appflow-connectorprofile-connectoroauthrequest-redirecturi""", alias="RedirectUri")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ConnectorOAuthRequest:
        from troposphere.appflow import ConnectorOAuthRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectorProfileConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileconfig.html
    Properties:
        - Name: ConnectorProfileCredentials
        - Name: ConnectorProfileProperties
    
    """
    
    ConnectorProfileCredentials_: Optional['ConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileconfig.html#cfn-appflow-connectorprofile-connectorprofileconfig-connectorprofilecredentials""", alias="ConnectorProfileCredentials")
    ConnectorProfileProperties_: Optional['ConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileconfig.html#cfn-appflow-connectorprofile-connectorprofileconfig-connectorprofileproperties""", alias="ConnectorProfileProperties")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ConnectorProfileConfig:
        from troposphere.appflow import ConnectorProfileConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html
    Properties:
        - Name: Amplitude
        - Name: GoogleAnalytics
        - Name: ServiceNow
        - Name: CustomConnector
        - Name: SAPOData
        - Name: Pardot
        - Name: Veeva
        - Name: Trendmicro
        - Name: Datadog
        - Name: Marketo
        - Name: Redshift
        - Name: Singular
        - Name: Slack
        - Name: Snowflake
        - Name: Dynatrace
        - Name: Zendesk
        - Name: InforNexus
        - Name: Salesforce
    
    """
    
    Amplitude_: Optional['AmplitudeConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-amplitude""", alias="Amplitude")
    GoogleAnalytics_: Optional['GoogleAnalyticsConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-googleanalytics""", alias="GoogleAnalytics")
    ServiceNow_: Optional['ServiceNowConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-servicenow""", alias="ServiceNow")
    CustomConnector_: Optional['CustomConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-customconnector""", alias="CustomConnector")
    SAPOData_: Optional['SAPODataConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-sapodata""", alias="SAPOData")
    Pardot_: Optional['PardotConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-pardot""", alias="Pardot")
    Veeva_: Optional['VeevaConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-veeva""", alias="Veeva")
    Trendmicro_: Optional['TrendmicroConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-trendmicro""", alias="Trendmicro")
    Datadog_: Optional['DatadogConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-datadog""", alias="Datadog")
    Marketo_: Optional['MarketoConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-marketo""", alias="Marketo")
    Redshift_: Optional['RedshiftConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-redshift""", alias="Redshift")
    Singular_: Optional['SingularConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-singular""", alias="Singular")
    Slack_: Optional['SlackConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-slack""", alias="Slack")
    Snowflake_: Optional['SnowflakeConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-snowflake""", alias="Snowflake")
    Dynatrace_: Optional['DynatraceConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-dynatrace""", alias="Dynatrace")
    Zendesk_: Optional['ZendeskConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-zendesk""", alias="Zendesk")
    InforNexus_: Optional['InforNexusConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-infornexus""", alias="InforNexus")
    Salesforce_: Optional['SalesforceConnectorProfileCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-salesforce""", alias="Salesforce")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ConnectorProfileCredentials:
        from troposphere.appflow import ConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html
    Properties:
        - Name: ServiceNow
        - Name: CustomConnector
        - Name: SAPOData
        - Name: Pardot
        - Name: Veeva
        - Name: Datadog
        - Name: Marketo
        - Name: Redshift
        - Name: Slack
        - Name: Snowflake
        - Name: Dynatrace
        - Name: Zendesk
        - Name: InforNexus
        - Name: Salesforce
    
    """
    
    ServiceNow_: Optional['ServiceNowConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-servicenow""", alias="ServiceNow")
    CustomConnector_: Optional['CustomConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-customconnector""", alias="CustomConnector")
    SAPOData_: Optional['SAPODataConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-sapodata""", alias="SAPOData")
    Pardot_: Optional['PardotConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-pardot""", alias="Pardot")
    Veeva_: Optional['VeevaConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-veeva""", alias="Veeva")
    Datadog_: Optional['DatadogConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-datadog""", alias="Datadog")
    Marketo_: Optional['MarketoConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-marketo""", alias="Marketo")
    Redshift_: Optional['RedshiftConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-redshift""", alias="Redshift")
    Slack_: Optional['SlackConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-slack""", alias="Slack")
    Snowflake_: Optional['SnowflakeConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-snowflake""", alias="Snowflake")
    Dynatrace_: Optional['DynatraceConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-dynatrace""", alias="Dynatrace")
    Zendesk_: Optional['ZendeskConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-zendesk""", alias="Zendesk")
    InforNexus_: Optional['InforNexusConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-infornexus""", alias="InforNexus")
    Salesforce_: Optional['SalesforceConnectorProfileProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-salesforce""", alias="Salesforce")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ConnectorProfileProperties:
        from troposphere.appflow import ConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomAuthCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customauthcredentials.html
    Properties:
        - Name: CredentialsMap
        - Name: CustomAuthenticationType
    
    """
    
    CredentialsMap_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customauthcredentials.html#cfn-appflow-connectorprofile-customauthcredentials-credentialsmap""", alias="CredentialsMap")
    CustomAuthenticationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customauthcredentials.html#cfn-appflow-connectorprofile-customauthcredentials-customauthenticationtype""", alias="CustomAuthenticationType")
    


    @property
    def tropo_type(self) -> troposphere.appflow.CustomAuthCredentials:
        from troposphere.appflow import CustomAuthCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html
    Properties:
        - Name: Basic
        - Name: ApiKey
        - Name: Oauth2
        - Name: Custom
        - Name: AuthenticationType
    
    """
    
    Basic_: Optional['BasicAuthCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html#cfn-appflow-connectorprofile-customconnectorprofilecredentials-basic""", alias="Basic")
    ApiKey_: Optional['ApiKeyCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html#cfn-appflow-connectorprofile-customconnectorprofilecredentials-apikey""", alias="ApiKey")
    Oauth2_: Optional['OAuth2Credentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html#cfn-appflow-connectorprofile-customconnectorprofilecredentials-oauth2""", alias="Oauth2")
    Custom_: Optional['CustomAuthCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html#cfn-appflow-connectorprofile-customconnectorprofilecredentials-custom""", alias="Custom")
    AuthenticationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html#cfn-appflow-connectorprofile-customconnectorprofilecredentials-authenticationtype""", alias="AuthenticationType")
    


    @property
    def tropo_type(self) -> troposphere.appflow.CustomConnectorProfileCredentials:
        from troposphere.appflow import CustomConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofileproperties.html
    Properties:
        - Name: OAuth2Properties
        - Name: ProfileProperties
    
    """
    
    OAuth2Properties_: Optional['OAuth2Properties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofileproperties.html#cfn-appflow-connectorprofile-customconnectorprofileproperties-oauth2properties""", alias="OAuth2Properties")
    ProfileProperties_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofileproperties.html#cfn-appflow-connectorprofile-customconnectorprofileproperties-profileproperties""", alias="ProfileProperties")
    


    @property
    def tropo_type(self) -> troposphere.appflow.CustomConnectorProfileProperties:
        from troposphere.appflow import CustomConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatadogConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials.html
    Properties:
        - Name: ApplicationKey
        - Name: ApiKey
    
    """
    
    ApplicationKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials.html#cfn-appflow-connectorprofile-datadogconnectorprofilecredentials-applicationkey""", alias="ApplicationKey")
    ApiKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials.html#cfn-appflow-connectorprofile-datadogconnectorprofilecredentials-apikey""", alias="ApiKey")
    


    @property
    def tropo_type(self) -> troposphere.appflow.DatadogConnectorProfileCredentials:
        from troposphere.appflow import DatadogConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatadogConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-datadogconnectorprofileproperties.html
    Properties:
        - Name: InstanceUrl
    
    """
    
    InstanceUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-datadogconnectorprofileproperties.html#cfn-appflow-connectorprofile-datadogconnectorprofileproperties-instanceurl""", alias="InstanceUrl")
    


    @property
    def tropo_type(self) -> troposphere.appflow.DatadogConnectorProfileProperties:
        from troposphere.appflow import DatadogConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynatraceConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-dynatraceconnectorprofilecredentials.html
    Properties:
        - Name: ApiToken
    
    """
    
    ApiToken_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-dynatraceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-dynatraceconnectorprofilecredentials-apitoken""", alias="ApiToken")
    


    @property
    def tropo_type(self) -> troposphere.appflow.DynatraceConnectorProfileCredentials:
        from troposphere.appflow import DynatraceConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynatraceConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-dynatraceconnectorprofileproperties.html
    Properties:
        - Name: InstanceUrl
    
    """
    
    InstanceUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-dynatraceconnectorprofileproperties.html#cfn-appflow-connectorprofile-dynatraceconnectorprofileproperties-instanceurl""", alias="InstanceUrl")
    


    @property
    def tropo_type(self) -> troposphere.appflow.DynatraceConnectorProfileProperties:
        from troposphere.appflow import DynatraceConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GoogleAnalyticsConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html
    Properties:
        - Name: RefreshToken
        - Name: ClientSecret
        - Name: AccessToken
        - Name: ClientId
        - Name: ConnectorOAuthRequest
    
    """
    
    RefreshToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-refreshtoken""", alias="RefreshToken")
    ClientSecret_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-clientsecret""", alias="ClientSecret")
    AccessToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-accesstoken""", alias="AccessToken")
    ClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-clientid""", alias="ClientId")
    ConnectorOAuthRequest_: Optional['ConnectorOAuthRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-connectoroauthrequest""", alias="ConnectorOAuthRequest")
    


    @property
    def tropo_type(self) -> troposphere.appflow.GoogleAnalyticsConnectorProfileCredentials:
        from troposphere.appflow import GoogleAnalyticsConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InforNexusConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofilecredentials.html
    Properties:
        - Name: AccessKeyId
        - Name: UserId
        - Name: SecretAccessKey
        - Name: Datakey
    
    """
    
    AccessKeyId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofilecredentials.html#cfn-appflow-connectorprofile-infornexusconnectorprofilecredentials-accesskeyid""", alias="AccessKeyId")
    UserId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofilecredentials.html#cfn-appflow-connectorprofile-infornexusconnectorprofilecredentials-userid""", alias="UserId")
    SecretAccessKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofilecredentials.html#cfn-appflow-connectorprofile-infornexusconnectorprofilecredentials-secretaccesskey""", alias="SecretAccessKey")
    Datakey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofilecredentials.html#cfn-appflow-connectorprofile-infornexusconnectorprofilecredentials-datakey""", alias="Datakey")
    


    @property
    def tropo_type(self) -> troposphere.appflow.InforNexusConnectorProfileCredentials:
        from troposphere.appflow import InforNexusConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InforNexusConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofileproperties.html
    Properties:
        - Name: InstanceUrl
    
    """
    
    InstanceUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofileproperties.html#cfn-appflow-connectorprofile-infornexusconnectorprofileproperties-instanceurl""", alias="InstanceUrl")
    


    @property
    def tropo_type(self) -> troposphere.appflow.InforNexusConnectorProfileProperties:
        from troposphere.appflow import InforNexusConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MarketoConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials.html
    Properties:
        - Name: ClientSecret
        - Name: AccessToken
        - Name: ClientId
        - Name: ConnectorOAuthRequest
    
    """
    
    ClientSecret_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials.html#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-clientsecret""", alias="ClientSecret")
    AccessToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials.html#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-accesstoken""", alias="AccessToken")
    ClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials.html#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-clientid""", alias="ClientId")
    ConnectorOAuthRequest_: Optional['ConnectorOAuthRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials.html#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-connectoroauthrequest""", alias="ConnectorOAuthRequest")
    


    @property
    def tropo_type(self) -> troposphere.appflow.MarketoConnectorProfileCredentials:
        from troposphere.appflow import MarketoConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MarketoConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofileproperties.html
    Properties:
        - Name: InstanceUrl
    
    """
    
    InstanceUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofileproperties.html#cfn-appflow-connectorprofile-marketoconnectorprofileproperties-instanceurl""", alias="InstanceUrl")
    


    @property
    def tropo_type(self) -> troposphere.appflow.MarketoConnectorProfileProperties:
        from troposphere.appflow import MarketoConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OAuth2Credentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html
    Properties:
        - Name: OAuthRequest
        - Name: RefreshToken
        - Name: ClientSecret
        - Name: AccessToken
        - Name: ClientId
    
    """
    
    OAuthRequest_: Optional['ConnectorOAuthRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html#cfn-appflow-connectorprofile-oauth2credentials-oauthrequest""", alias="OAuthRequest")
    RefreshToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html#cfn-appflow-connectorprofile-oauth2credentials-refreshtoken""", alias="RefreshToken")
    ClientSecret_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html#cfn-appflow-connectorprofile-oauth2credentials-clientsecret""", alias="ClientSecret")
    AccessToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html#cfn-appflow-connectorprofile-oauth2credentials-accesstoken""", alias="AccessToken")
    ClientId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html#cfn-appflow-connectorprofile-oauth2credentials-clientid""", alias="ClientId")
    


    @property
    def tropo_type(self) -> troposphere.appflow.OAuth2Credentials:
        from troposphere.appflow import OAuth2Credentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OAuth2Properties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2properties.html
    Properties:
        - Name: TokenUrlCustomProperties
        - Name: TokenUrl
        - Name: OAuth2GrantType
    
    """
    
    TokenUrlCustomProperties_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2properties.html#cfn-appflow-connectorprofile-oauth2properties-tokenurlcustomproperties""", alias="TokenUrlCustomProperties")
    TokenUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2properties.html#cfn-appflow-connectorprofile-oauth2properties-tokenurl""", alias="TokenUrl")
    OAuth2GrantType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2properties.html#cfn-appflow-connectorprofile-oauth2properties-oauth2granttype""", alias="OAuth2GrantType")
    


    @property
    def tropo_type(self) -> troposphere.appflow.OAuth2Properties:
        from troposphere.appflow import OAuth2Properties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OAuthCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthcredentials.html
    Properties:
        - Name: RefreshToken
        - Name: AccessToken
        - Name: ClientSecret
        - Name: ClientId
        - Name: ConnectorOAuthRequest
    
    """
    
    RefreshToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthcredentials.html#cfn-appflow-connectorprofile-oauthcredentials-refreshtoken""", alias="RefreshToken")
    AccessToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthcredentials.html#cfn-appflow-connectorprofile-oauthcredentials-accesstoken""", alias="AccessToken")
    ClientSecret_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthcredentials.html#cfn-appflow-connectorprofile-oauthcredentials-clientsecret""", alias="ClientSecret")
    ClientId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthcredentials.html#cfn-appflow-connectorprofile-oauthcredentials-clientid""", alias="ClientId")
    ConnectorOAuthRequest_: Optional['ConnectorOAuthRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthcredentials.html#cfn-appflow-connectorprofile-oauthcredentials-connectoroauthrequest""", alias="ConnectorOAuthRequest")
    


    @property
    def tropo_type(self) -> troposphere.appflow.OAuthCredentials:
        from troposphere.appflow import OAuthCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OAuthProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthproperties.html
    Properties:
        - Name: AuthCodeUrl
        - Name: TokenUrl
        - Name: OAuthScopes
    
    """
    
    AuthCodeUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthproperties.html#cfn-appflow-connectorprofile-oauthproperties-authcodeurl""", alias="AuthCodeUrl")
    TokenUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthproperties.html#cfn-appflow-connectorprofile-oauthproperties-tokenurl""", alias="TokenUrl")
    OAuthScopes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthproperties.html#cfn-appflow-connectorprofile-oauthproperties-oauthscopes""", alias="OAuthScopes")
    


    @property
    def tropo_type(self) -> troposphere.appflow.OAuthProperties:
        from troposphere.appflow import OAuthProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PardotConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials.html
    Properties:
        - Name: RefreshToken
        - Name: AccessToken
        - Name: ClientCredentialsArn
        - Name: ConnectorOAuthRequest
    
    """
    
    RefreshToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials.html#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-refreshtoken""", alias="RefreshToken")
    AccessToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials.html#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-accesstoken""", alias="AccessToken")
    ClientCredentialsArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials.html#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-clientcredentialsarn""", alias="ClientCredentialsArn")
    ConnectorOAuthRequest_: Optional['ConnectorOAuthRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials.html#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-connectoroauthrequest""", alias="ConnectorOAuthRequest")
    


    @property
    def tropo_type(self) -> troposphere.appflow.PardotConnectorProfileCredentials:
        from troposphere.appflow import PardotConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PardotConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties.html
    Properties:
        - Name: InstanceUrl
        - Name: IsSandboxEnvironment
        - Name: BusinessUnitId
    
    """
    
    InstanceUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties.html#cfn-appflow-connectorprofile-pardotconnectorprofileproperties-instanceurl""", alias="InstanceUrl")
    IsSandboxEnvironment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties.html#cfn-appflow-connectorprofile-pardotconnectorprofileproperties-issandboxenvironment""", alias="IsSandboxEnvironment")
    BusinessUnitId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties.html#cfn-appflow-connectorprofile-pardotconnectorprofileproperties-businessunitid""", alias="BusinessUnitId")
    


    @property
    def tropo_type(self) -> troposphere.appflow.PardotConnectorProfileProperties:
        from troposphere.appflow import PardotConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RedshiftConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofilecredentials.html
    Properties:
        - Name: Username
        - Name: Password
    
    """
    
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofilecredentials.html#cfn-appflow-connectorprofile-redshiftconnectorprofilecredentials-username""", alias="Username")
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofilecredentials.html#cfn-appflow-connectorprofile-redshiftconnectorprofilecredentials-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.appflow.RedshiftConnectorProfileCredentials:
        from troposphere.appflow import RedshiftConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RedshiftConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html
    Properties:
        - Name: DatabaseUrl
        - Name: BucketName
        - Name: IsRedshiftServerless
        - Name: DataApiRoleArn
        - Name: DatabaseName
        - Name: WorkgroupName
        - Name: BucketPrefix
        - Name: ClusterIdentifier
        - Name: RoleArn
    
    """
    
    DatabaseUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-databaseurl""", alias="DatabaseUrl")
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-bucketname""", alias="BucketName")
    IsRedshiftServerless_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-isredshiftserverless""", alias="IsRedshiftServerless")
    DataApiRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-dataapirolearn""", alias="DataApiRoleArn")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-databasename""", alias="DatabaseName")
    WorkgroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-workgroupname""", alias="WorkgroupName")
    BucketPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-bucketprefix""", alias="BucketPrefix")
    ClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-clusteridentifier""", alias="ClusterIdentifier")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.appflow.RedshiftConnectorProfileProperties:
        from troposphere.appflow import RedshiftConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SAPODataConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofilecredentials.html
    Properties:
        - Name: BasicAuthCredentials
        - Name: OAuthCredentials
    
    """
    
    BasicAuthCredentials_: Optional['BasicAuthCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofilecredentials.html#cfn-appflow-connectorprofile-sapodataconnectorprofilecredentials-basicauthcredentials""", alias="BasicAuthCredentials")
    OAuthCredentials_: Optional['OAuthCredentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofilecredentials.html#cfn-appflow-connectorprofile-sapodataconnectorprofilecredentials-oauthcredentials""", alias="OAuthCredentials")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SAPODataConnectorProfileCredentials:
        from troposphere.appflow import SAPODataConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SAPODataConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html
    Properties:
        - Name: ApplicationServicePath
        - Name: ApplicationHostUrl
        - Name: OAuthProperties
        - Name: DisableSSO
        - Name: LogonLanguage
        - Name: PrivateLinkServiceName
        - Name: PortNumber
        - Name: ClientNumber
    
    """
    
    ApplicationServicePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-applicationservicepath""", alias="ApplicationServicePath")
    ApplicationHostUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-applicationhosturl""", alias="ApplicationHostUrl")
    OAuthProperties_: Optional['OAuthProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-oauthproperties""", alias="OAuthProperties")
    DisableSSO_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-disablesso""", alias="DisableSSO")
    LogonLanguage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-logonlanguage""", alias="LogonLanguage")
    PrivateLinkServiceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-privatelinkservicename""", alias="PrivateLinkServiceName")
    PortNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-portnumber""", alias="PortNumber")
    ClientNumber_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-clientnumber""", alias="ClientNumber")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SAPODataConnectorProfileProperties:
        from troposphere.appflow import SAPODataConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SalesforceConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html
    Properties:
        - Name: JwtToken
        - Name: RefreshToken
        - Name: AccessToken
        - Name: ClientCredentialsArn
        - Name: ConnectorOAuthRequest
        - Name: OAuth2GrantType
    
    """
    
    JwtToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-jwttoken""", alias="JwtToken")
    RefreshToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-refreshtoken""", alias="RefreshToken")
    AccessToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-accesstoken""", alias="AccessToken")
    ClientCredentialsArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-clientcredentialsarn""", alias="ClientCredentialsArn")
    ConnectorOAuthRequest_: Optional['ConnectorOAuthRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-connectoroauthrequest""", alias="ConnectorOAuthRequest")
    OAuth2GrantType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-oauth2granttype""", alias="OAuth2GrantType")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SalesforceConnectorProfileCredentials:
        from troposphere.appflow import SalesforceConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SalesforceConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofileproperties.html
    Properties:
        - Name: InstanceUrl
        - Name: isSandboxEnvironment
        - Name: usePrivateLinkForMetadataAndAuthorization
    
    """
    
    InstanceUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofileproperties.html#cfn-appflow-connectorprofile-salesforceconnectorprofileproperties-instanceurl""", alias="InstanceUrl")
    isSandboxEnvironment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofileproperties.html#cfn-appflow-connectorprofile-salesforceconnectorprofileproperties-issandboxenvironment""", alias="isSandboxEnvironment")
    usePrivateLinkForMetadataAndAuthorization_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofileproperties.html#cfn-appflow-connectorprofile-salesforceconnectorprofileproperties-useprivatelinkformetadataandauthorization""", alias="usePrivateLinkForMetadataAndAuthorization")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SalesforceConnectorProfileProperties:
        from troposphere.appflow import SalesforceConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceNowConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials.html
    Properties:
        - Name: Username
        - Name: OAuth2Credentials
        - Name: Password
    
    """
    
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials.html#cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-username""", alias="Username")
    OAuth2Credentials_: Optional['OAuth2Credentials'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials.html#cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-oauth2credentials""", alias="OAuth2Credentials")
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials.html#cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ServiceNowConnectorProfileCredentials:
        from troposphere.appflow import ServiceNowConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceNowConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofileproperties.html
    Properties:
        - Name: InstanceUrl
    
    """
    
    InstanceUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofileproperties.html#cfn-appflow-connectorprofile-servicenowconnectorprofileproperties-instanceurl""", alias="InstanceUrl")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ServiceNowConnectorProfileProperties:
        from troposphere.appflow import ServiceNowConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SingularConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-singularconnectorprofilecredentials.html
    Properties:
        - Name: ApiKey
    
    """
    
    ApiKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-singularconnectorprofilecredentials.html#cfn-appflow-connectorprofile-singularconnectorprofilecredentials-apikey""", alias="ApiKey")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SingularConnectorProfileCredentials:
        from troposphere.appflow import SingularConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlackConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofilecredentials.html
    Properties:
        - Name: ClientSecret
        - Name: AccessToken
        - Name: ClientId
        - Name: ConnectorOAuthRequest
    
    """
    
    ClientSecret_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofilecredentials.html#cfn-appflow-connectorprofile-slackconnectorprofilecredentials-clientsecret""", alias="ClientSecret")
    AccessToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofilecredentials.html#cfn-appflow-connectorprofile-slackconnectorprofilecredentials-accesstoken""", alias="AccessToken")
    ClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofilecredentials.html#cfn-appflow-connectorprofile-slackconnectorprofilecredentials-clientid""", alias="ClientId")
    ConnectorOAuthRequest_: Optional['ConnectorOAuthRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofilecredentials.html#cfn-appflow-connectorprofile-slackconnectorprofilecredentials-connectoroauthrequest""", alias="ConnectorOAuthRequest")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SlackConnectorProfileCredentials:
        from troposphere.appflow import SlackConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlackConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofileproperties.html
    Properties:
        - Name: InstanceUrl
    
    """
    
    InstanceUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofileproperties.html#cfn-appflow-connectorprofile-slackconnectorprofileproperties-instanceurl""", alias="InstanceUrl")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SlackConnectorProfileProperties:
        from troposphere.appflow import SlackConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnowflakeConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofilecredentials.html
    Properties:
        - Name: Username
        - Name: Password
    
    """
    
    Username_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofilecredentials.html#cfn-appflow-connectorprofile-snowflakeconnectorprofilecredentials-username""", alias="Username")
    Password_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofilecredentials.html#cfn-appflow-connectorprofile-snowflakeconnectorprofilecredentials-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SnowflakeConnectorProfileCredentials:
        from troposphere.appflow import SnowflakeConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnowflakeConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html
    Properties:
        - Name: Warehouse
        - Name: BucketName
        - Name: PrivateLinkServiceName
        - Name: Stage
        - Name: Region
        - Name: BucketPrefix
        - Name: AccountName
    
    """
    
    Warehouse_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-warehouse""", alias="Warehouse")
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-bucketname""", alias="BucketName")
    PrivateLinkServiceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-privatelinkservicename""", alias="PrivateLinkServiceName")
    Stage_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-stage""", alias="Stage")
    Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-region""", alias="Region")
    BucketPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-bucketprefix""", alias="BucketPrefix")
    AccountName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-accountname""", alias="AccountName")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SnowflakeConnectorProfileProperties:
        from troposphere.appflow import SnowflakeConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrendmicroConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-trendmicroconnectorprofilecredentials.html
    Properties:
        - Name: ApiSecretKey
    
    """
    
    ApiSecretKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-trendmicroconnectorprofilecredentials.html#cfn-appflow-connectorprofile-trendmicroconnectorprofilecredentials-apisecretkey""", alias="ApiSecretKey")
    


    @property
    def tropo_type(self) -> troposphere.appflow.TrendmicroConnectorProfileCredentials:
        from troposphere.appflow import TrendmicroConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VeevaConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials.html
    Properties:
        - Name: Username
        - Name: Password
    
    """
    
    Username_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials.html#cfn-appflow-connectorprofile-veevaconnectorprofilecredentials-username""", alias="Username")
    Password_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials.html#cfn-appflow-connectorprofile-veevaconnectorprofilecredentials-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.appflow.VeevaConnectorProfileCredentials:
        from troposphere.appflow import VeevaConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VeevaConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-veevaconnectorprofileproperties.html
    Properties:
        - Name: InstanceUrl
    
    """
    
    InstanceUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-veevaconnectorprofileproperties.html#cfn-appflow-connectorprofile-veevaconnectorprofileproperties-instanceurl""", alias="InstanceUrl")
    


    @property
    def tropo_type(self) -> troposphere.appflow.VeevaConnectorProfileProperties:
        from troposphere.appflow import VeevaConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ZendeskConnectorProfileCredentials(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofilecredentials.html
    Properties:
        - Name: ClientSecret
        - Name: AccessToken
        - Name: ClientId
        - Name: ConnectorOAuthRequest
    
    """
    
    ClientSecret_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofilecredentials.html#cfn-appflow-connectorprofile-zendeskconnectorprofilecredentials-clientsecret""", alias="ClientSecret")
    AccessToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofilecredentials.html#cfn-appflow-connectorprofile-zendeskconnectorprofilecredentials-accesstoken""", alias="AccessToken")
    ClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofilecredentials.html#cfn-appflow-connectorprofile-zendeskconnectorprofilecredentials-clientid""", alias="ClientId")
    ConnectorOAuthRequest_: Optional['ConnectorOAuthRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofilecredentials.html#cfn-appflow-connectorprofile-zendeskconnectorprofilecredentials-connectoroauthrequest""", alias="ConnectorOAuthRequest")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ZendeskConnectorProfileCredentials:
        from troposphere.appflow import ZendeskConnectorProfileCredentials as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ZendeskConnectorProfileProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofileproperties.html
    Properties:
        - Name: InstanceUrl
    
    """
    
    InstanceUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofileproperties.html#cfn-appflow-connectorprofile-zendeskconnectorprofileproperties-instanceurl""", alias="InstanceUrl")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ZendeskConnectorProfileProperties:
        from troposphere.appflow import ZendeskConnectorProfileProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AggregationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-aggregationconfig.html
    Properties:
        - Name: TargetFileSize
        - Name: AggregationType
    
    """
    
    TargetFileSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-aggregationconfig.html#cfn-appflow-flow-aggregationconfig-targetfilesize""", alias="TargetFileSize")
    AggregationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-aggregationconfig.html#cfn-appflow-flow-aggregationconfig-aggregationtype""", alias="AggregationType")
    


    @property
    def tropo_type(self) -> troposphere.appflow.AggregationConfig:
        from troposphere.appflow import AggregationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AmplitudeSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-amplitudesourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-amplitudesourceproperties.html#cfn-appflow-flow-amplitudesourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appflow.AmplitudeSourceProperties:
        from troposphere.appflow import AmplitudeSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectorOperator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html
    Properties:
        - Name: Amplitude
        - Name: S3
        - Name: GoogleAnalytics
        - Name: ServiceNow
        - Name: CustomConnector
        - Name: SAPOData
        - Name: Pardot
        - Name: Veeva
        - Name: Trendmicro
        - Name: Datadog
        - Name: Marketo
        - Name: Singular
        - Name: Slack
        - Name: Dynatrace
        - Name: Zendesk
        - Name: InforNexus
        - Name: Salesforce
    
    """
    
    Amplitude_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-amplitude""", alias="Amplitude")
    S3_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-s3""", alias="S3")
    GoogleAnalytics_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-googleanalytics""", alias="GoogleAnalytics")
    ServiceNow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-servicenow""", alias="ServiceNow")
    CustomConnector_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-customconnector""", alias="CustomConnector")
    SAPOData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-sapodata""", alias="SAPOData")
    Pardot_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-pardot""", alias="Pardot")
    Veeva_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-veeva""", alias="Veeva")
    Trendmicro_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-trendmicro""", alias="Trendmicro")
    Datadog_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-datadog""", alias="Datadog")
    Marketo_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-marketo""", alias="Marketo")
    Singular_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-singular""", alias="Singular")
    Slack_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-slack""", alias="Slack")
    Dynatrace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-dynatrace""", alias="Dynatrace")
    Zendesk_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-zendesk""", alias="Zendesk")
    InforNexus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-infornexus""", alias="InforNexus")
    Salesforce_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-salesforce""", alias="Salesforce")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ConnectorOperator:
        from troposphere.appflow import ConnectorOperator as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomConnectorDestinationProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html
    Properties:
        - Name: IdFieldNames
        - Name: EntityName
        - Name: WriteOperationType
        - Name: ErrorHandlingConfig
        - Name: CustomProperties
    
    """
    
    IdFieldNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html#cfn-appflow-flow-customconnectordestinationproperties-idfieldnames""", alias="IdFieldNames")
    EntityName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html#cfn-appflow-flow-customconnectordestinationproperties-entityname""", alias="EntityName")
    WriteOperationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html#cfn-appflow-flow-customconnectordestinationproperties-writeoperationtype""", alias="WriteOperationType")
    ErrorHandlingConfig_: Optional['ErrorHandlingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html#cfn-appflow-flow-customconnectordestinationproperties-errorhandlingconfig""", alias="ErrorHandlingConfig")
    CustomProperties_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html#cfn-appflow-flow-customconnectordestinationproperties-customproperties""", alias="CustomProperties")
    


    @property
    def tropo_type(self) -> troposphere.appflow.CustomConnectorDestinationProperties:
        from troposphere.appflow import CustomConnectorDestinationProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomConnectorSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectorsourceproperties.html
    Properties:
        - Name: EntityName
        - Name: DataTransferApi
        - Name: CustomProperties
    
    """
    
    EntityName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectorsourceproperties.html#cfn-appflow-flow-customconnectorsourceproperties-entityname""", alias="EntityName")
    DataTransferApi_: Optional['DataTransferApi'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectorsourceproperties.html#cfn-appflow-flow-customconnectorsourceproperties-datatransferapi""", alias="DataTransferApi")
    CustomProperties_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectorsourceproperties.html#cfn-appflow-flow-customconnectorsourceproperties-customproperties""", alias="CustomProperties")
    


    @property
    def tropo_type(self) -> troposphere.appflow.CustomConnectorSourceProperties:
        from troposphere.appflow import CustomConnectorSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataTransferApi(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-datatransferapi.html
    Properties:
        - Name: Type
        - Name: Name
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-datatransferapi.html#cfn-appflow-flow-datatransferapi-type""", alias="Type")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-datatransferapi.html#cfn-appflow-flow-datatransferapi-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.appflow.DataTransferApi:
        from troposphere.appflow import DataTransferApi as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatadogSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-datadogsourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-datadogsourceproperties.html#cfn-appflow-flow-datadogsourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appflow.DatadogSourceProperties:
        from troposphere.appflow import DatadogSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DestinationConnectorProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html
    Properties:
        - Name: S3
        - Name: CustomConnector
        - Name: Upsolver
        - Name: SAPOData
        - Name: Snowflake
        - Name: LookoutMetrics
        - Name: EventBridge
        - Name: Zendesk
        - Name: Marketo
        - Name: Redshift
        - Name: Salesforce
    
    """
    
    S3_: Optional['S3DestinationProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-s3""", alias="S3")
    CustomConnector_: Optional['CustomConnectorDestinationProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-customconnector""", alias="CustomConnector")
    Upsolver_: Optional['UpsolverDestinationProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-upsolver""", alias="Upsolver")
    SAPOData_: Optional['SAPODataDestinationProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-sapodata""", alias="SAPOData")
    Snowflake_: Optional['SnowflakeDestinationProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-snowflake""", alias="Snowflake")
    LookoutMetrics_: Optional['LookoutMetricsDestinationProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-lookoutmetrics""", alias="LookoutMetrics")
    EventBridge_: Optional['EventBridgeDestinationProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-eventbridge""", alias="EventBridge")
    Zendesk_: Optional['ZendeskDestinationProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-zendesk""", alias="Zendesk")
    Marketo_: Optional['MarketoDestinationProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-marketo""", alias="Marketo")
    Redshift_: Optional['RedshiftDestinationProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-redshift""", alias="Redshift")
    Salesforce_: Optional['SalesforceDestinationProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-salesforce""", alias="Salesforce")
    


    @property
    def tropo_type(self) -> troposphere.appflow.DestinationConnectorProperties:
        from troposphere.appflow import DestinationConnectorProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DestinationFlowConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationflowconfig.html
    Properties:
        - Name: ConnectorProfileName
        - Name: ApiVersion
        - Name: ConnectorType
        - Name: DestinationConnectorProperties
    
    """
    
    ConnectorProfileName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationflowconfig.html#cfn-appflow-flow-destinationflowconfig-connectorprofilename""", alias="ConnectorProfileName")
    ApiVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationflowconfig.html#cfn-appflow-flow-destinationflowconfig-apiversion""", alias="ApiVersion")
    ConnectorType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationflowconfig.html#cfn-appflow-flow-destinationflowconfig-connectortype""", alias="ConnectorType")
    DestinationConnectorProperties_: 'DestinationConnectorProperties' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationflowconfig.html#cfn-appflow-flow-destinationflowconfig-destinationconnectorproperties""", alias="DestinationConnectorProperties")
    


    @property
    def tropo_type(self) -> troposphere.appflow.DestinationFlowConfig:
        from troposphere.appflow import DestinationFlowConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynatraceSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-dynatracesourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-dynatracesourceproperties.html#cfn-appflow-flow-dynatracesourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appflow.DynatraceSourceProperties:
        from troposphere.appflow import DynatraceSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ErrorHandlingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-errorhandlingconfig.html
    Properties:
        - Name: BucketName
        - Name: BucketPrefix
        - Name: FailOnFirstError
    
    """
    
    BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-errorhandlingconfig.html#cfn-appflow-flow-errorhandlingconfig-bucketname""", alias="BucketName")
    BucketPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-errorhandlingconfig.html#cfn-appflow-flow-errorhandlingconfig-bucketprefix""", alias="BucketPrefix")
    FailOnFirstError_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-errorhandlingconfig.html#cfn-appflow-flow-errorhandlingconfig-failonfirsterror""", alias="FailOnFirstError")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ErrorHandlingConfig:
        from troposphere.appflow import ErrorHandlingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EventBridgeDestinationProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-eventbridgedestinationproperties.html
    Properties:
        - Name: Object
        - Name: ErrorHandlingConfig
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-eventbridgedestinationproperties.html#cfn-appflow-flow-eventbridgedestinationproperties-object""", alias="Object")
    ErrorHandlingConfig_: Optional['ErrorHandlingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-eventbridgedestinationproperties.html#cfn-appflow-flow-eventbridgedestinationproperties-errorhandlingconfig""", alias="ErrorHandlingConfig")
    


    @property
    def tropo_type(self) -> troposphere.appflow.EventBridgeDestinationProperties:
        from troposphere.appflow import EventBridgeDestinationProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GlueDataCatalog(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-gluedatacatalog.html
    Properties:
        - Name: DatabaseName
        - Name: RoleArn
        - Name: TablePrefix
    
    """
    
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-gluedatacatalog.html#cfn-appflow-flow-gluedatacatalog-databasename""", alias="DatabaseName")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-gluedatacatalog.html#cfn-appflow-flow-gluedatacatalog-rolearn""", alias="RoleArn")
    TablePrefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-gluedatacatalog.html#cfn-appflow-flow-gluedatacatalog-tableprefix""", alias="TablePrefix")
    


    @property
    def tropo_type(self) -> troposphere.appflow.GlueDataCatalog:
        from troposphere.appflow import GlueDataCatalog as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GoogleAnalyticsSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-googleanalyticssourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-googleanalyticssourceproperties.html#cfn-appflow-flow-googleanalyticssourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appflow.GoogleAnalyticsSourceProperties:
        from troposphere.appflow import GoogleAnalyticsSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IncrementalPullConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-incrementalpullconfig.html
    Properties:
        - Name: DatetimeTypeFieldName
    
    """
    
    DatetimeTypeFieldName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-incrementalpullconfig.html#cfn-appflow-flow-incrementalpullconfig-datetimetypefieldname""", alias="DatetimeTypeFieldName")
    


    @property
    def tropo_type(self) -> troposphere.appflow.IncrementalPullConfig:
        from troposphere.appflow import IncrementalPullConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InforNexusSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-infornexussourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-infornexussourceproperties.html#cfn-appflow-flow-infornexussourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appflow.InforNexusSourceProperties:
        from troposphere.appflow import InforNexusSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LookoutMetricsDestinationProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-lookoutmetricsdestinationproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-lookoutmetricsdestinationproperties.html#cfn-appflow-flow-lookoutmetricsdestinationproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appflow.LookoutMetricsDestinationProperties:
        from troposphere.appflow import LookoutMetricsDestinationProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MarketoDestinationProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-marketodestinationproperties.html
    Properties:
        - Name: Object
        - Name: ErrorHandlingConfig
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-marketodestinationproperties.html#cfn-appflow-flow-marketodestinationproperties-object""", alias="Object")
    ErrorHandlingConfig_: Optional['ErrorHandlingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-marketodestinationproperties.html#cfn-appflow-flow-marketodestinationproperties-errorhandlingconfig""", alias="ErrorHandlingConfig")
    


    @property
    def tropo_type(self) -> troposphere.appflow.MarketoDestinationProperties:
        from troposphere.appflow import MarketoDestinationProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MarketoSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-marketosourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-marketosourceproperties.html#cfn-appflow-flow-marketosourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appflow.MarketoSourceProperties:
        from troposphere.appflow import MarketoSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetadataCatalogConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-metadatacatalogconfig.html
    Properties:
        - Name: GlueDataCatalog
    
    """
    
    GlueDataCatalog_: Optional['GlueDataCatalog'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-metadatacatalogconfig.html#cfn-appflow-flow-metadatacatalogconfig-gluedatacatalog""", alias="GlueDataCatalog")
    


    @property
    def tropo_type(self) -> troposphere.appflow.MetadataCatalogConfig:
        from troposphere.appflow import MetadataCatalogConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PardotSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-pardotsourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-pardotsourceproperties.html#cfn-appflow-flow-pardotsourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appflow.PardotSourceProperties:
        from troposphere.appflow import PardotSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrefixConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-prefixconfig.html
    Properties:
        - Name: PrefixType
        - Name: PathPrefixHierarchy
        - Name: PrefixFormat
    
    """
    
    PrefixType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-prefixconfig.html#cfn-appflow-flow-prefixconfig-prefixtype""", alias="PrefixType")
    PathPrefixHierarchy_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-prefixconfig.html#cfn-appflow-flow-prefixconfig-pathprefixhierarchy""", alias="PathPrefixHierarchy")
    PrefixFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-prefixconfig.html#cfn-appflow-flow-prefixconfig-prefixformat""", alias="PrefixFormat")
    


    @property
    def tropo_type(self) -> troposphere.appflow.PrefixConfig:
        from troposphere.appflow import PrefixConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RedshiftDestinationProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-redshiftdestinationproperties.html
    Properties:
        - Name: Object
        - Name: BucketPrefix
        - Name: IntermediateBucketName
        - Name: ErrorHandlingConfig
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-redshiftdestinationproperties.html#cfn-appflow-flow-redshiftdestinationproperties-object""", alias="Object")
    BucketPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-redshiftdestinationproperties.html#cfn-appflow-flow-redshiftdestinationproperties-bucketprefix""", alias="BucketPrefix")
    IntermediateBucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-redshiftdestinationproperties.html#cfn-appflow-flow-redshiftdestinationproperties-intermediatebucketname""", alias="IntermediateBucketName")
    ErrorHandlingConfig_: Optional['ErrorHandlingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-redshiftdestinationproperties.html#cfn-appflow-flow-redshiftdestinationproperties-errorhandlingconfig""", alias="ErrorHandlingConfig")
    


    @property
    def tropo_type(self) -> troposphere.appflow.RedshiftDestinationProperties:
        from troposphere.appflow import RedshiftDestinationProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3DestinationProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3destinationproperties.html
    Properties:
        - Name: BucketName
        - Name: BucketPrefix
        - Name: S3OutputFormatConfig
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3destinationproperties.html#cfn-appflow-flow-s3destinationproperties-bucketname""", alias="BucketName")
    BucketPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3destinationproperties.html#cfn-appflow-flow-s3destinationproperties-bucketprefix""", alias="BucketPrefix")
    S3OutputFormatConfig_: Optional['S3OutputFormatConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3destinationproperties.html#cfn-appflow-flow-s3destinationproperties-s3outputformatconfig""", alias="S3OutputFormatConfig")
    


    @property
    def tropo_type(self) -> troposphere.appflow.S3DestinationProperties:
        from troposphere.appflow import S3DestinationProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3InputFormatConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3inputformatconfig.html
    Properties:
        - Name: S3InputFileType
    
    """
    
    S3InputFileType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3inputformatconfig.html#cfn-appflow-flow-s3inputformatconfig-s3inputfiletype""", alias="S3InputFileType")
    


    @property
    def tropo_type(self) -> troposphere.appflow.S3InputFormatConfig:
        from troposphere.appflow import S3InputFormatConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3OutputFormatConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3outputformatconfig.html
    Properties:
        - Name: PrefixConfig
        - Name: FileType
        - Name: AggregationConfig
        - Name: PreserveSourceDataTyping
    
    """
    
    PrefixConfig_: Optional['PrefixConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3outputformatconfig.html#cfn-appflow-flow-s3outputformatconfig-prefixconfig""", alias="PrefixConfig")
    FileType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3outputformatconfig.html#cfn-appflow-flow-s3outputformatconfig-filetype""", alias="FileType")
    AggregationConfig_: Optional['AggregationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3outputformatconfig.html#cfn-appflow-flow-s3outputformatconfig-aggregationconfig""", alias="AggregationConfig")
    PreserveSourceDataTyping_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3outputformatconfig.html#cfn-appflow-flow-s3outputformatconfig-preservesourcedatatyping""", alias="PreserveSourceDataTyping")
    


    @property
    def tropo_type(self) -> troposphere.appflow.S3OutputFormatConfig:
        from troposphere.appflow import S3OutputFormatConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3SourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3sourceproperties.html
    Properties:
        - Name: S3InputFormatConfig
        - Name: BucketName
        - Name: BucketPrefix
    
    """
    
    S3InputFormatConfig_: Optional['S3InputFormatConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3sourceproperties.html#cfn-appflow-flow-s3sourceproperties-s3inputformatconfig""", alias="S3InputFormatConfig")
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3sourceproperties.html#cfn-appflow-flow-s3sourceproperties-bucketname""", alias="BucketName")
    BucketPrefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3sourceproperties.html#cfn-appflow-flow-s3sourceproperties-bucketprefix""", alias="BucketPrefix")
    


    @property
    def tropo_type(self) -> troposphere.appflow.S3SourceProperties:
        from troposphere.appflow import S3SourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SAPODataDestinationProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html
    Properties:
        - Name: IdFieldNames
        - Name: ObjectPath
        - Name: WriteOperationType
        - Name: ErrorHandlingConfig
        - Name: SuccessResponseHandlingConfig
    
    """
    
    IdFieldNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html#cfn-appflow-flow-sapodatadestinationproperties-idfieldnames""", alias="IdFieldNames")
    ObjectPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html#cfn-appflow-flow-sapodatadestinationproperties-objectpath""", alias="ObjectPath")
    WriteOperationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html#cfn-appflow-flow-sapodatadestinationproperties-writeoperationtype""", alias="WriteOperationType")
    ErrorHandlingConfig_: Optional['ErrorHandlingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html#cfn-appflow-flow-sapodatadestinationproperties-errorhandlingconfig""", alias="ErrorHandlingConfig")
    SuccessResponseHandlingConfig_: Optional['SuccessResponseHandlingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html#cfn-appflow-flow-sapodatadestinationproperties-successresponsehandlingconfig""", alias="SuccessResponseHandlingConfig")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SAPODataDestinationProperties:
        from troposphere.appflow import SAPODataDestinationProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SAPODataPaginationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatapaginationconfig.html
    Properties:
        - Name: maxPageSize
    
    """
    
    maxPageSize_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatapaginationconfig.html#cfn-appflow-flow-sapodatapaginationconfig-maxpagesize""", alias="maxPageSize")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SAPODataPaginationConfig:
        from troposphere.appflow import SAPODataPaginationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SAPODataParallelismConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodataparallelismconfig.html
    Properties:
        - Name: maxParallelism
    
    """
    
    maxParallelism_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodataparallelismconfig.html#cfn-appflow-flow-sapodataparallelismconfig-maxparallelism""", alias="maxParallelism")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SAPODataParallelismConfig:
        from troposphere.appflow import SAPODataParallelismConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SAPODataSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatasourceproperties.html
    Properties:
        - Name: ObjectPath
        - Name: paginationConfig
        - Name: parallelismConfig
    
    """
    
    ObjectPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatasourceproperties.html#cfn-appflow-flow-sapodatasourceproperties-objectpath""", alias="ObjectPath")
    paginationConfig_: Optional['SAPODataPaginationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatasourceproperties.html#cfn-appflow-flow-sapodatasourceproperties-paginationconfig""", alias="paginationConfig")
    parallelismConfig_: Optional['SAPODataParallelismConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatasourceproperties.html#cfn-appflow-flow-sapodatasourceproperties-parallelismconfig""", alias="parallelismConfig")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SAPODataSourceProperties:
        from troposphere.appflow import SAPODataSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SalesforceDestinationProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcedestinationproperties.html
    Properties:
        - Name: IdFieldNames
        - Name: WriteOperationType
        - Name: DataTransferApi
        - Name: Object
        - Name: ErrorHandlingConfig
    
    """
    
    IdFieldNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcedestinationproperties.html#cfn-appflow-flow-salesforcedestinationproperties-idfieldnames""", alias="IdFieldNames")
    WriteOperationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcedestinationproperties.html#cfn-appflow-flow-salesforcedestinationproperties-writeoperationtype""", alias="WriteOperationType")
    DataTransferApi_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcedestinationproperties.html#cfn-appflow-flow-salesforcedestinationproperties-datatransferapi""", alias="DataTransferApi")
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcedestinationproperties.html#cfn-appflow-flow-salesforcedestinationproperties-object""", alias="Object")
    ErrorHandlingConfig_: Optional['ErrorHandlingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcedestinationproperties.html#cfn-appflow-flow-salesforcedestinationproperties-errorhandlingconfig""", alias="ErrorHandlingConfig")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SalesforceDestinationProperties:
        from troposphere.appflow import SalesforceDestinationProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SalesforceSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcesourceproperties.html
    Properties:
        - Name: IncludeDeletedRecords
        - Name: DataTransferApi
        - Name: Object
        - Name: EnableDynamicFieldUpdate
    
    """
    
    IncludeDeletedRecords_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcesourceproperties.html#cfn-appflow-flow-salesforcesourceproperties-includedeletedrecords""", alias="IncludeDeletedRecords")
    DataTransferApi_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcesourceproperties.html#cfn-appflow-flow-salesforcesourceproperties-datatransferapi""", alias="DataTransferApi")
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcesourceproperties.html#cfn-appflow-flow-salesforcesourceproperties-object""", alias="Object")
    EnableDynamicFieldUpdate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcesourceproperties.html#cfn-appflow-flow-salesforcesourceproperties-enabledynamicfieldupdate""", alias="EnableDynamicFieldUpdate")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SalesforceSourceProperties:
        from troposphere.appflow import SalesforceSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScheduledTriggerProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html
    Properties:
        - Name: ScheduleEndTime
        - Name: ScheduleExpression
        - Name: FirstExecutionFrom
        - Name: TimeZone
        - Name: ScheduleStartTime
        - Name: DataPullMode
        - Name: ScheduleOffset
        - Name: FlowErrorDeactivationThreshold
    
    """
    
    ScheduleEndTime_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-scheduleendtime""", alias="ScheduleEndTime")
    ScheduleExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-scheduleexpression""", alias="ScheduleExpression")
    FirstExecutionFrom_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-firstexecutionfrom""", alias="FirstExecutionFrom")
    TimeZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-timezone""", alias="TimeZone")
    ScheduleStartTime_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-schedulestarttime""", alias="ScheduleStartTime")
    DataPullMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-datapullmode""", alias="DataPullMode")
    ScheduleOffset_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-scheduleoffset""", alias="ScheduleOffset")
    FlowErrorDeactivationThreshold_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-flowerrordeactivationthreshold""", alias="FlowErrorDeactivationThreshold")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ScheduledTriggerProperties:
        from troposphere.appflow import ScheduledTriggerProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceNowSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-servicenowsourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-servicenowsourceproperties.html#cfn-appflow-flow-servicenowsourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ServiceNowSourceProperties:
        from troposphere.appflow import ServiceNowSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SingularSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-singularsourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-singularsourceproperties.html#cfn-appflow-flow-singularsourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SingularSourceProperties:
        from troposphere.appflow import SingularSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlackSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-slacksourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-slacksourceproperties.html#cfn-appflow-flow-slacksourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SlackSourceProperties:
        from troposphere.appflow import SlackSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnowflakeDestinationProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-snowflakedestinationproperties.html
    Properties:
        - Name: Object
        - Name: BucketPrefix
        - Name: IntermediateBucketName
        - Name: ErrorHandlingConfig
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-snowflakedestinationproperties.html#cfn-appflow-flow-snowflakedestinationproperties-object""", alias="Object")
    BucketPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-snowflakedestinationproperties.html#cfn-appflow-flow-snowflakedestinationproperties-bucketprefix""", alias="BucketPrefix")
    IntermediateBucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-snowflakedestinationproperties.html#cfn-appflow-flow-snowflakedestinationproperties-intermediatebucketname""", alias="IntermediateBucketName")
    ErrorHandlingConfig_: Optional['ErrorHandlingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-snowflakedestinationproperties.html#cfn-appflow-flow-snowflakedestinationproperties-errorhandlingconfig""", alias="ErrorHandlingConfig")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SnowflakeDestinationProperties:
        from troposphere.appflow import SnowflakeDestinationProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceConnectorProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html
    Properties:
        - Name: Amplitude
        - Name: S3
        - Name: GoogleAnalytics
        - Name: ServiceNow
        - Name: CustomConnector
        - Name: SAPOData
        - Name: Pardot
        - Name: Veeva
        - Name: Trendmicro
        - Name: Datadog
        - Name: Marketo
        - Name: Singular
        - Name: Slack
        - Name: Dynatrace
        - Name: Zendesk
        - Name: InforNexus
        - Name: Salesforce
    
    """
    
    Amplitude_: Optional['AmplitudeSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-amplitude""", alias="Amplitude")
    S3_: Optional['S3SourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-s3""", alias="S3")
    GoogleAnalytics_: Optional['GoogleAnalyticsSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-googleanalytics""", alias="GoogleAnalytics")
    ServiceNow_: Optional['ServiceNowSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-servicenow""", alias="ServiceNow")
    CustomConnector_: Optional['CustomConnectorSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-customconnector""", alias="CustomConnector")
    SAPOData_: Optional['SAPODataSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-sapodata""", alias="SAPOData")
    Pardot_: Optional['PardotSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-pardot""", alias="Pardot")
    Veeva_: Optional['VeevaSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-veeva""", alias="Veeva")
    Trendmicro_: Optional['TrendmicroSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-trendmicro""", alias="Trendmicro")
    Datadog_: Optional['DatadogSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-datadog""", alias="Datadog")
    Marketo_: Optional['MarketoSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-marketo""", alias="Marketo")
    Singular_: Optional['SingularSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-singular""", alias="Singular")
    Slack_: Optional['SlackSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-slack""", alias="Slack")
    Dynatrace_: Optional['DynatraceSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-dynatrace""", alias="Dynatrace")
    Zendesk_: Optional['ZendeskSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-zendesk""", alias="Zendesk")
    InforNexus_: Optional['InforNexusSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-infornexus""", alias="InforNexus")
    Salesforce_: Optional['SalesforceSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-salesforce""", alias="Salesforce")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SourceConnectorProperties:
        from troposphere.appflow import SourceConnectorProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceFlowConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceflowconfig.html
    Properties:
        - Name: ConnectorProfileName
        - Name: ApiVersion
        - Name: SourceConnectorProperties
        - Name: ConnectorType
        - Name: IncrementalPullConfig
    
    """
    
    ConnectorProfileName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceflowconfig.html#cfn-appflow-flow-sourceflowconfig-connectorprofilename""", alias="ConnectorProfileName")
    ApiVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceflowconfig.html#cfn-appflow-flow-sourceflowconfig-apiversion""", alias="ApiVersion")
    SourceConnectorProperties_: 'SourceConnectorProperties' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceflowconfig.html#cfn-appflow-flow-sourceflowconfig-sourceconnectorproperties""", alias="SourceConnectorProperties")
    ConnectorType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceflowconfig.html#cfn-appflow-flow-sourceflowconfig-connectortype""", alias="ConnectorType")
    IncrementalPullConfig_: Optional['IncrementalPullConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceflowconfig.html#cfn-appflow-flow-sourceflowconfig-incrementalpullconfig""", alias="IncrementalPullConfig")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SourceFlowConfig:
        from troposphere.appflow import SourceFlowConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SuccessResponseHandlingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-successresponsehandlingconfig.html
    Properties:
        - Name: BucketName
        - Name: BucketPrefix
    
    """
    
    BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-successresponsehandlingconfig.html#cfn-appflow-flow-successresponsehandlingconfig-bucketname""", alias="BucketName")
    BucketPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-successresponsehandlingconfig.html#cfn-appflow-flow-successresponsehandlingconfig-bucketprefix""", alias="BucketPrefix")
    


    @property
    def tropo_type(self) -> troposphere.appflow.SuccessResponseHandlingConfig:
        from troposphere.appflow import SuccessResponseHandlingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Task(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-task.html
    Properties:
        - Name: SourceFields
        - Name: DestinationField
        - Name: ConnectorOperator
        - Name: TaskType
        - Name: TaskProperties
    
    """
    
    SourceFields_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-task.html#cfn-appflow-flow-task-sourcefields""", alias="SourceFields")
    DestinationField_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-task.html#cfn-appflow-flow-task-destinationfield""", alias="DestinationField")
    ConnectorOperator_: Optional['ConnectorOperator'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-task.html#cfn-appflow-flow-task-connectoroperator""", alias="ConnectorOperator")
    TaskType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-task.html#cfn-appflow-flow-task-tasktype""", alias="TaskType")
    TaskProperties_: Optional[List['TaskPropertiesObject']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-task.html#cfn-appflow-flow-task-taskproperties""", alias="TaskProperties")
    


    @property
    def tropo_type(self) -> troposphere.appflow.Task:
        from troposphere.appflow import Task as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TaskPropertiesObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-taskpropertiesobject.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-taskpropertiesobject.html#cfn-appflow-flow-taskpropertiesobject-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-taskpropertiesobject.html#cfn-appflow-flow-taskpropertiesobject-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.appflow.TaskPropertiesObject:
        from troposphere.appflow import TaskPropertiesObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrendmicroSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-trendmicrosourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-trendmicrosourceproperties.html#cfn-appflow-flow-trendmicrosourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appflow.TrendmicroSourceProperties:
        from troposphere.appflow import TrendmicroSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TriggerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-triggerconfig.html
    Properties:
        - Name: TriggerType
        - Name: TriggerProperties
    
    """
    
    TriggerType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-triggerconfig.html#cfn-appflow-flow-triggerconfig-triggertype""", alias="TriggerType")
    TriggerProperties_: Optional['ScheduledTriggerProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-triggerconfig.html#cfn-appflow-flow-triggerconfig-triggerproperties""", alias="TriggerProperties")
    


    @property
    def tropo_type(self) -> troposphere.appflow.TriggerConfig:
        from troposphere.appflow import TriggerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UpsolverDestinationProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolverdestinationproperties.html
    Properties:
        - Name: BucketName
        - Name: BucketPrefix
        - Name: S3OutputFormatConfig
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolverdestinationproperties.html#cfn-appflow-flow-upsolverdestinationproperties-bucketname""", alias="BucketName")
    BucketPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolverdestinationproperties.html#cfn-appflow-flow-upsolverdestinationproperties-bucketprefix""", alias="BucketPrefix")
    S3OutputFormatConfig_: 'UpsolverS3OutputFormatConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolverdestinationproperties.html#cfn-appflow-flow-upsolverdestinationproperties-s3outputformatconfig""", alias="S3OutputFormatConfig")
    


    @property
    def tropo_type(self) -> troposphere.appflow.UpsolverDestinationProperties:
        from troposphere.appflow import UpsolverDestinationProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UpsolverS3OutputFormatConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolvers3outputformatconfig.html
    Properties:
        - Name: PrefixConfig
        - Name: FileType
        - Name: AggregationConfig
    
    """
    
    PrefixConfig_: 'PrefixConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolvers3outputformatconfig.html#cfn-appflow-flow-upsolvers3outputformatconfig-prefixconfig""", alias="PrefixConfig")
    FileType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolvers3outputformatconfig.html#cfn-appflow-flow-upsolvers3outputformatconfig-filetype""", alias="FileType")
    AggregationConfig_: Optional['AggregationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolvers3outputformatconfig.html#cfn-appflow-flow-upsolvers3outputformatconfig-aggregationconfig""", alias="AggregationConfig")
    


    @property
    def tropo_type(self) -> troposphere.appflow.UpsolverS3OutputFormatConfig:
        from troposphere.appflow import UpsolverS3OutputFormatConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VeevaSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-veevasourceproperties.html
    Properties:
        - Name: IncludeAllVersions
        - Name: IncludeRenditions
        - Name: DocumentType
        - Name: Object
        - Name: IncludeSourceFiles
    
    """
    
    IncludeAllVersions_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-veevasourceproperties.html#cfn-appflow-flow-veevasourceproperties-includeallversions""", alias="IncludeAllVersions")
    IncludeRenditions_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-veevasourceproperties.html#cfn-appflow-flow-veevasourceproperties-includerenditions""", alias="IncludeRenditions")
    DocumentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-veevasourceproperties.html#cfn-appflow-flow-veevasourceproperties-documenttype""", alias="DocumentType")
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-veevasourceproperties.html#cfn-appflow-flow-veevasourceproperties-object""", alias="Object")
    IncludeSourceFiles_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-veevasourceproperties.html#cfn-appflow-flow-veevasourceproperties-includesourcefiles""", alias="IncludeSourceFiles")
    


    @property
    def tropo_type(self) -> troposphere.appflow.VeevaSourceProperties:
        from troposphere.appflow import VeevaSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ZendeskDestinationProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendeskdestinationproperties.html
    Properties:
        - Name: IdFieldNames
        - Name: WriteOperationType
        - Name: Object
        - Name: ErrorHandlingConfig
    
    """
    
    IdFieldNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendeskdestinationproperties.html#cfn-appflow-flow-zendeskdestinationproperties-idfieldnames""", alias="IdFieldNames")
    WriteOperationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendeskdestinationproperties.html#cfn-appflow-flow-zendeskdestinationproperties-writeoperationtype""", alias="WriteOperationType")
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendeskdestinationproperties.html#cfn-appflow-flow-zendeskdestinationproperties-object""", alias="Object")
    ErrorHandlingConfig_: Optional['ErrorHandlingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendeskdestinationproperties.html#cfn-appflow-flow-zendeskdestinationproperties-errorhandlingconfig""", alias="ErrorHandlingConfig")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ZendeskDestinationProperties:
        from troposphere.appflow import ZendeskDestinationProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ZendeskSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendesksourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendesksourceproperties.html#cfn-appflow-flow-zendesksourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.appflow.ZendeskSourceProperties:
        from troposphere.appflow import ZendeskSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Connector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connector.html
    Properties:
        - Name: ConnectorLabel
        - Name: ConnectorProvisioningType
        - Name: Description
        - Name: ConnectorProvisioningConfig
    Attributes:
        - Name: ConnectorArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConnectorLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connector.html#cfn-appflow-connector-connectorlabel""", alias="ConnectorLabel")
    ConnectorProvisioningType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connector.html#cfn-appflow-connector-connectorprovisioningtype""", alias="ConnectorProvisioningType")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connector.html#cfn-appflow-connector-description""", alias="Description")
    ConnectorProvisioningConfig_: 'ConnectorProvisioningConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connector.html#cfn-appflow-connector-connectorprovisioningconfig""", alias="ConnectorProvisioningConfig")
    

    @property
    def tropo_type(self) -> troposphere.appflow.Connector:
        from troposphere.appflow import Connector as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appflow import Connector as TropoT
        return resource_to_troposphere(self, TropoT)


class ConnectorProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html
    Properties:
        - Name: ConnectorLabel
        - Name: ConnectorProfileName
        - Name: KMSArn
        - Name: ConnectorType
        - Name: ConnectionMode
        - Name: ConnectorProfileConfig
    Attributes:
        - Name: CredentialsArn
        - Name: ConnectorProfileArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConnectorLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectorlabel""", alias="ConnectorLabel")
    ConnectorProfileName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectorprofilename""", alias="ConnectorProfileName")
    KMSArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-kmsarn""", alias="KMSArn")
    ConnectorType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectortype""", alias="ConnectorType")
    ConnectionMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectionmode""", alias="ConnectionMode")
    ConnectorProfileConfig_: Optional['ConnectorProfileConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectorprofileconfig""", alias="ConnectorProfileConfig")
    

    @property
    def tropo_type(self) -> troposphere.appflow.ConnectorProfile:
        from troposphere.appflow import ConnectorProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appflow import ConnectorProfile as TropoT
        return resource_to_troposphere(self, TropoT)


class Flow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html
    Properties:
        - Name: Description
        - Name: KMSArn
        - Name: Tasks
        - Name: FlowName
        - Name: TriggerConfig
        - Name: DestinationFlowConfigList
        - Name: SourceFlowConfig
        - Name: FlowStatus
        - Name: Tags
        - Name: MetadataCatalogConfig
    Attributes:
        - Name: FlowArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-description""", alias="Description")
    KMSArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-kmsarn""", alias="KMSArn")
    Tasks_: List['Task'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-tasks""", alias="Tasks")
    FlowName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-flowname""", alias="FlowName")
    TriggerConfig_: 'TriggerConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-triggerconfig""", alias="TriggerConfig")
    DestinationFlowConfigList_: List['DestinationFlowConfig'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-destinationflowconfiglist""", alias="DestinationFlowConfigList")
    SourceFlowConfig_: 'SourceFlowConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-sourceflowconfig""", alias="SourceFlowConfig")
    FlowStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-flowstatus""", alias="FlowStatus")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-tags""", alias="Tags")
    MetadataCatalogConfig_: Optional['MetadataCatalogConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-metadatacatalogconfig""", alias="MetadataCatalogConfig")
    

    @property
    def tropo_type(self) -> troposphere.appflow.Flow:
        from troposphere.appflow import Flow as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appflow import Flow as TropoT
        return resource_to_troposphere(self, TropoT)

