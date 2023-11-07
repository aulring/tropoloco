from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AuthorizationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html
    Properties:
        - Name: AwsIamConfig
        - Name: AuthorizationType
    
    """
    
    AwsIamConfig_: Optional['AwsIamConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html#cfn-appsync-datasource-authorizationconfig-awsiamconfig""", alias="AwsIamConfig")
    AuthorizationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html#cfn-appsync-datasource-authorizationconfig-authorizationtype""", alias="AuthorizationType")
    


    @property
    def tropo_type(self) -> troposphere.appsync.AuthorizationConfig:
        from troposphere.appsync import AuthorizationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AwsIamConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html
    Properties:
        - Name: SigningRegion
        - Name: SigningServiceName
    
    """
    
    SigningRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html#cfn-appsync-datasource-awsiamconfig-signingregion""", alias="SigningRegion")
    SigningServiceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html#cfn-appsync-datasource-awsiamconfig-signingservicename""", alias="SigningServiceName")
    


    @property
    def tropo_type(self) -> troposphere.appsync.AwsIamConfig:
        from troposphere.appsync import AwsIamConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeltaSyncConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html
    Properties:
        - Name: BaseTableTTL
        - Name: DeltaSyncTableTTL
        - Name: DeltaSyncTableName
    
    """
    
    BaseTableTTL_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-basetablettl""", alias="BaseTableTTL")
    DeltaSyncTableTTL_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-deltasynctablettl""", alias="DeltaSyncTableTTL")
    DeltaSyncTableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-deltasynctablename""", alias="DeltaSyncTableName")
    


    @property
    def tropo_type(self) -> troposphere.appsync.DeltaSyncConfig:
        from troposphere.appsync import DeltaSyncConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynamoDBConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html
    Properties:
        - Name: TableName
        - Name: AwsRegion
        - Name: Versioned
        - Name: DeltaSyncConfig
        - Name: UseCallerCredentials
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-tablename""", alias="TableName")
    AwsRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-awsregion""", alias="AwsRegion")
    Versioned_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-versioned""", alias="Versioned")
    DeltaSyncConfig_: Optional['DeltaSyncConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-deltasyncconfig""", alias="DeltaSyncConfig")
    UseCallerCredentials_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-usecallercredentials""", alias="UseCallerCredentials")
    


    @property
    def tropo_type(self) -> troposphere.appsync.DynamoDBConfig:
        from troposphere.appsync import DynamoDBConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ElasticsearchConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html
    Properties:
        - Name: AwsRegion
        - Name: Endpoint
    
    """
    
    AwsRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html#cfn-appsync-datasource-elasticsearchconfig-awsregion""", alias="AwsRegion")
    Endpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html#cfn-appsync-datasource-elasticsearchconfig-endpoint""", alias="Endpoint")
    


    @property
    def tropo_type(self) -> troposphere.appsync.ElasticsearchConfig:
        from troposphere.appsync import ElasticsearchConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EventBridgeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-eventbridgeconfig.html
    Properties:
        - Name: EventBusArn
    
    """
    
    EventBusArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-eventbridgeconfig.html#cfn-appsync-datasource-eventbridgeconfig-eventbusarn""", alias="EventBusArn")
    


    @property
    def tropo_type(self) -> troposphere.appsync.EventBridgeConfig:
        from troposphere.appsync import EventBridgeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html
    Properties:
        - Name: Endpoint
        - Name: AuthorizationConfig
    
    """
    
    Endpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html#cfn-appsync-datasource-httpconfig-endpoint""", alias="Endpoint")
    AuthorizationConfig_: Optional['AuthorizationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html#cfn-appsync-datasource-httpconfig-authorizationconfig""", alias="AuthorizationConfig")
    


    @property
    def tropo_type(self) -> troposphere.appsync.HttpConfig:
        from troposphere.appsync import HttpConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html
    Properties:
        - Name: LambdaFunctionArn
    
    """
    
    LambdaFunctionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html#cfn-appsync-datasource-lambdaconfig-lambdafunctionarn""", alias="LambdaFunctionArn")
    


    @property
    def tropo_type(self) -> troposphere.appsync.LambdaConfig:
        from troposphere.appsync import LambdaConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OpenSearchServiceConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html
    Properties:
        - Name: AwsRegion
        - Name: Endpoint
    
    """
    
    AwsRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html#cfn-appsync-datasource-opensearchserviceconfig-awsregion""", alias="AwsRegion")
    Endpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html#cfn-appsync-datasource-opensearchserviceconfig-endpoint""", alias="Endpoint")
    


    @property
    def tropo_type(self) -> troposphere.appsync.OpenSearchServiceConfig:
        from troposphere.appsync import OpenSearchServiceConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RdsHttpEndpointConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html
    Properties:
        - Name: AwsRegion
        - Name: Schema
        - Name: DatabaseName
        - Name: DbClusterIdentifier
        - Name: AwsSecretStoreArn
    
    """
    
    AwsRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-awsregion""", alias="AwsRegion")
    Schema_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-schema""", alias="Schema")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-databasename""", alias="DatabaseName")
    DbClusterIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-dbclusteridentifier""", alias="DbClusterIdentifier")
    AwsSecretStoreArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-awssecretstorearn""", alias="AwsSecretStoreArn")
    


    @property
    def tropo_type(self) -> troposphere.appsync.RdsHttpEndpointConfig:
        from troposphere.appsync import RdsHttpEndpointConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RelationalDatabaseConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html
    Properties:
        - Name: RdsHttpEndpointConfig
        - Name: RelationalDatabaseSourceType
    
    """
    
    RdsHttpEndpointConfig_: Optional['RdsHttpEndpointConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html#cfn-appsync-datasource-relationaldatabaseconfig-rdshttpendpointconfig""", alias="RdsHttpEndpointConfig")
    RelationalDatabaseSourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html#cfn-appsync-datasource-relationaldatabaseconfig-relationaldatabasesourcetype""", alias="RelationalDatabaseSourceType")
    


    @property
    def tropo_type(self) -> troposphere.appsync.RelationalDatabaseConfig:
        from troposphere.appsync import RelationalDatabaseConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AppSyncRuntime(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-appsyncruntime.html
    Properties:
        - Name: RuntimeVersion
        - Name: Name
    
    """
    
    RuntimeVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-appsyncruntime.html#cfn-appsync-functionconfiguration-appsyncruntime-runtimeversion""", alias="RuntimeVersion")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-appsyncruntime.html#cfn-appsync-functionconfiguration-appsyncruntime-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.appsync.AppSyncRuntime:
        from troposphere.appsync import AppSyncRuntime as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaConflictHandlerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html
    Properties:
        - Name: LambdaConflictHandlerArn
    
    """
    
    LambdaConflictHandlerArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html#cfn-appsync-functionconfiguration-lambdaconflicthandlerconfig-lambdaconflicthandlerarn""", alias="LambdaConflictHandlerArn")
    


    @property
    def tropo_type(self) -> troposphere.appsync.LambdaConflictHandlerConfig:
        from troposphere.appsync import LambdaConflictHandlerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SyncConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html
    Properties:
        - Name: ConflictHandler
        - Name: ConflictDetection
        - Name: LambdaConflictHandlerConfig
    
    """
    
    ConflictHandler_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html#cfn-appsync-functionconfiguration-syncconfig-conflicthandler""", alias="ConflictHandler")
    ConflictDetection_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html#cfn-appsync-functionconfiguration-syncconfig-conflictdetection""", alias="ConflictDetection")
    LambdaConflictHandlerConfig_: Optional['LambdaConflictHandlerConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html#cfn-appsync-functionconfiguration-syncconfig-lambdaconflicthandlerconfig""", alias="LambdaConflictHandlerConfig")
    


    @property
    def tropo_type(self) -> troposphere.appsync.SyncConfig:
        from troposphere.appsync import SyncConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AdditionalAuthenticationProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html
    Properties:
        - Name: OpenIDConnectConfig
        - Name: LambdaAuthorizerConfig
        - Name: UserPoolConfig
        - Name: AuthenticationType
    
    """
    
    OpenIDConnectConfig_: Optional['OpenIDConnectConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-openidconnectconfig""", alias="OpenIDConnectConfig")
    LambdaAuthorizerConfig_: Optional['LambdaAuthorizerConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-lambdaauthorizerconfig""", alias="LambdaAuthorizerConfig")
    UserPoolConfig_: Optional['CognitoUserPoolConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-userpoolconfig""", alias="UserPoolConfig")
    AuthenticationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-authenticationtype""", alias="AuthenticationType")
    


    @property
    def tropo_type(self) -> troposphere.appsync.AdditionalAuthenticationProvider:
        from troposphere.appsync import AdditionalAuthenticationProvider as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CognitoUserPoolConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html
    Properties:
        - Name: AppIdClientRegex
        - Name: UserPoolId
        - Name: AwsRegion
    
    """
    
    AppIdClientRegex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-appidclientregex""", alias="AppIdClientRegex")
    UserPoolId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-userpoolid""", alias="UserPoolId")
    AwsRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-awsregion""", alias="AwsRegion")
    


    @property
    def tropo_type(self) -> troposphere.appsync.CognitoUserPoolConfig:
        from troposphere.appsync import CognitoUserPoolConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaAuthorizerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html
    Properties:
        - Name: IdentityValidationExpression
        - Name: AuthorizerUri
        - Name: AuthorizerResultTtlInSeconds
    
    """
    
    IdentityValidationExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig-identityvalidationexpression""", alias="IdentityValidationExpression")
    AuthorizerUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig-authorizeruri""", alias="AuthorizerUri")
    AuthorizerResultTtlInSeconds_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig-authorizerresultttlinseconds""", alias="AuthorizerResultTtlInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.appsync.LambdaAuthorizerConfig:
        from troposphere.appsync import LambdaAuthorizerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html
    Properties:
        - Name: CloudWatchLogsRoleArn
        - Name: ExcludeVerboseContent
        - Name: FieldLogLevel
    
    """
    
    CloudWatchLogsRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-cloudwatchlogsrolearn""", alias="CloudWatchLogsRoleArn")
    ExcludeVerboseContent_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-excludeverbosecontent""", alias="ExcludeVerboseContent")
    FieldLogLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-fieldloglevel""", alias="FieldLogLevel")
    


    @property
    def tropo_type(self) -> troposphere.appsync.LogConfig:
        from troposphere.appsync import LogConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OpenIDConnectConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html
    Properties:
        - Name: Issuer
        - Name: ClientId
        - Name: AuthTTL
        - Name: IatTTL
    
    """
    
    Issuer_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-issuer""", alias="Issuer")
    ClientId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-clientid""", alias="ClientId")
    AuthTTL_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-authttl""", alias="AuthTTL")
    IatTTL_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-iatttl""", alias="IatTTL")
    


    @property
    def tropo_type(self) -> troposphere.appsync.OpenIDConnectConfig:
        from troposphere.appsync import OpenIDConnectConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserPoolConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html
    Properties:
        - Name: AppIdClientRegex
        - Name: UserPoolId
        - Name: AwsRegion
        - Name: DefaultAction
    
    """
    
    AppIdClientRegex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-appidclientregex""", alias="AppIdClientRegex")
    UserPoolId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-userpoolid""", alias="UserPoolId")
    AwsRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-awsregion""", alias="AwsRegion")
    DefaultAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-defaultaction""", alias="DefaultAction")
    


    @property
    def tropo_type(self) -> troposphere.appsync.UserPoolConfig:
        from troposphere.appsync import UserPoolConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AppSyncRuntime(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-appsyncruntime.html
    Properties:
        - Name: RuntimeVersion
        - Name: Name
    
    """
    
    RuntimeVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-appsyncruntime.html#cfn-appsync-resolver-appsyncruntime-runtimeversion""", alias="RuntimeVersion")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-appsyncruntime.html#cfn-appsync-resolver-appsyncruntime-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.appsync.AppSyncRuntime:
        from troposphere.appsync import AppSyncRuntime as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CachingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html
    Properties:
        - Name: CachingKeys
        - Name: Ttl
    
    """
    
    CachingKeys_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html#cfn-appsync-resolver-cachingconfig-cachingkeys""", alias="CachingKeys")
    Ttl_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html#cfn-appsync-resolver-cachingconfig-ttl""", alias="Ttl")
    


    @property
    def tropo_type(self) -> troposphere.appsync.CachingConfig:
        from troposphere.appsync import CachingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaConflictHandlerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html
    Properties:
        - Name: LambdaConflictHandlerArn
    
    """
    
    LambdaConflictHandlerArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html#cfn-appsync-resolver-lambdaconflicthandlerconfig-lambdaconflicthandlerarn""", alias="LambdaConflictHandlerArn")
    


    @property
    def tropo_type(self) -> troposphere.appsync.LambdaConflictHandlerConfig:
        from troposphere.appsync import LambdaConflictHandlerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PipelineConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html
    Properties:
        - Name: Functions
    
    """
    
    Functions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html#cfn-appsync-resolver-pipelineconfig-functions""", alias="Functions")
    


    @property
    def tropo_type(self) -> troposphere.appsync.PipelineConfig:
        from troposphere.appsync import PipelineConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SyncConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html
    Properties:
        - Name: ConflictHandler
        - Name: ConflictDetection
        - Name: LambdaConflictHandlerConfig
    
    """
    
    ConflictHandler_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-conflicthandler""", alias="ConflictHandler")
    ConflictDetection_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-conflictdetection""", alias="ConflictDetection")
    LambdaConflictHandlerConfig_: Optional['LambdaConflictHandlerConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-lambdaconflicthandlerconfig""", alias="LambdaConflictHandlerConfig")
    


    @property
    def tropo_type(self) -> troposphere.appsync.SyncConfig:
        from troposphere.appsync import SyncConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceApiAssociationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-sourceapiassociation-sourceapiassociationconfig.html
    Properties:
        - Name: MergeType
    
    """
    
    MergeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-sourceapiassociation-sourceapiassociationconfig.html#cfn-appsync-sourceapiassociation-sourceapiassociationconfig-mergetype""", alias="MergeType")
    


    @property
    def tropo_type(self) -> troposphere.appsync.SourceApiAssociationConfig:
        from troposphere.appsync import SourceApiAssociationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ApiCache(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html
    Properties:
        - Name: Type
        - Name: TransitEncryptionEnabled
        - Name: AtRestEncryptionEnabled
        - Name: ApiId
        - Name: ApiCachingBehavior
        - Name: Ttl
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-type""", alias="Type")
    TransitEncryptionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-transitencryptionenabled""", alias="TransitEncryptionEnabled")
    AtRestEncryptionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-atrestencryptionenabled""", alias="AtRestEncryptionEnabled")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apiid""", alias="ApiId")
    ApiCachingBehavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apicachingbehavior""", alias="ApiCachingBehavior")
    Ttl_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-ttl""", alias="Ttl")
    

    @property
    def tropo_type(self) -> troposphere.appsync.ApiCache:
        from troposphere.appsync import ApiCache as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appsync import ApiCache as TropoT
        return resource_to_troposphere(self, TropoT)


class ApiKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html
    Properties:
        - Name: Description
        - Name: ApiKeyId
        - Name: Expires
        - Name: ApiId
    Attributes:
        - Name: ApiKey
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-description""", alias="Description")
    ApiKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apikeyid""", alias="ApiKeyId")
    Expires_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-expires""", alias="Expires")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apiid""", alias="ApiId")
    

    @property
    def tropo_type(self) -> troposphere.appsync.ApiKey:
        from troposphere.appsync import ApiKey as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appsync import ApiKey as TropoT
        return resource_to_troposphere(self, TropoT)


class DataSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html
    Properties:
        - Name: Type
        - Name: OpenSearchServiceConfig
        - Name: Description
        - Name: ServiceRoleArn
        - Name: EventBridgeConfig
        - Name: HttpConfig
        - Name: RelationalDatabaseConfig
        - Name: LambdaConfig
        - Name: ApiId
        - Name: Name
        - Name: DynamoDBConfig
        - Name: ElasticsearchConfig
    Attributes:
        - Name: DataSourceArn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-type""", alias="Type")
    OpenSearchServiceConfig_: Optional['OpenSearchServiceConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-opensearchserviceconfig""", alias="OpenSearchServiceConfig")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-description""", alias="Description")
    ServiceRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-servicerolearn""", alias="ServiceRoleArn")
    EventBridgeConfig_: Optional['EventBridgeConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-eventbridgeconfig""", alias="EventBridgeConfig")
    HttpConfig_: Optional['HttpConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-httpconfig""", alias="HttpConfig")
    RelationalDatabaseConfig_: Optional['RelationalDatabaseConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-relationaldatabaseconfig""", alias="RelationalDatabaseConfig")
    LambdaConfig_: Optional['LambdaConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-lambdaconfig""", alias="LambdaConfig")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-apiid""", alias="ApiId")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-name""", alias="Name")
    DynamoDBConfig_: Optional['DynamoDBConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-dynamodbconfig""", alias="DynamoDBConfig")
    ElasticsearchConfig_: Optional['ElasticsearchConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-elasticsearchconfig""", alias="ElasticsearchConfig")
    

    @property
    def tropo_type(self) -> troposphere.appsync.DataSource:
        from troposphere.appsync import DataSource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appsync import DataSource as TropoT
        return resource_to_troposphere(self, TropoT)


class DomainName(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html
    Properties:
        - Name: Description
        - Name: DomainName
        - Name: CertificateArn
    Attributes:
        - Name: AppSyncDomainName
        - Name: DomainName
        - Name: HostedZoneId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html#cfn-appsync-domainname-description""", alias="Description")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html#cfn-appsync-domainname-domainname""", alias="DomainName")
    CertificateArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html#cfn-appsync-domainname-certificatearn""", alias="CertificateArn")
    

    @property
    def tropo_type(self) -> troposphere.appsync.DomainName:
        from troposphere.appsync import DomainName as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appsync import DomainName as TropoT
        return resource_to_troposphere(self, TropoT)


class DomainNameApiAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html
    Properties:
        - Name: DomainName
        - Name: ApiId
    Attributes:
        - Name: ApiAssociationIdentifier
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html#cfn-appsync-domainnameapiassociation-domainname""", alias="DomainName")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html#cfn-appsync-domainnameapiassociation-apiid""", alias="ApiId")
    

    @property
    def tropo_type(self) -> troposphere.appsync.DomainNameApiAssociation:
        from troposphere.appsync import DomainNameApiAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appsync import DomainNameApiAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class FunctionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html
    Properties:
        - Name: Description
        - Name: RequestMappingTemplate
        - Name: ResponseMappingTemplate
        - Name: MaxBatchSize
        - Name: SyncConfig
        - Name: Code
        - Name: Name
        - Name: ResponseMappingTemplateS3Location
        - Name: Runtime
        - Name: CodeS3Location
        - Name: DataSourceName
        - Name: FunctionVersion
        - Name: RequestMappingTemplateS3Location
        - Name: ApiId
    Attributes:
        - Name: FunctionId
        - Name: FunctionArn
        - Name: DataSourceName
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-description""", alias="Description")
    RequestMappingTemplate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplate""", alias="RequestMappingTemplate")
    ResponseMappingTemplate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplate""", alias="ResponseMappingTemplate")
    MaxBatchSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-maxbatchsize""", alias="MaxBatchSize")
    SyncConfig_: Optional['SyncConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-syncconfig""", alias="SyncConfig")
    Code_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-code""", alias="Code")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-name""", alias="Name")
    ResponseMappingTemplateS3Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplates3location""", alias="ResponseMappingTemplateS3Location")
    Runtime_: Optional['AppSyncRuntime'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-runtime""", alias="Runtime")
    CodeS3Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-codes3location""", alias="CodeS3Location")
    DataSourceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-datasourcename""", alias="DataSourceName")
    FunctionVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-functionversion""", alias="FunctionVersion")
    RequestMappingTemplateS3Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplates3location""", alias="RequestMappingTemplateS3Location")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-apiid""", alias="ApiId")
    

    @property
    def tropo_type(self) -> troposphere.appsync.FunctionConfiguration:
        from troposphere.appsync import FunctionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appsync import FunctionConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class GraphQLApi(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html
    Properties:
        - Name: OpenIDConnectConfig
        - Name: MergedApiExecutionRoleArn
        - Name: OwnerContact
        - Name: Name
        - Name: AdditionalAuthenticationProviders
        - Name: ApiType
        - Name: LambdaAuthorizerConfig
        - Name: XrayEnabled
        - Name: Visibility
        - Name: UserPoolConfig
        - Name: Tags
        - Name: AuthenticationType
        - Name: LogConfig
    Attributes:
        - Name: RealtimeUrl
        - Name: GraphQLUrl
        - Name: GraphQLDns
        - Name: RealtimeDns
        - Name: Arn
        - Name: ApiId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OpenIDConnectConfig_: Optional['OpenIDConnectConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-openidconnectconfig""", alias="OpenIDConnectConfig")
    MergedApiExecutionRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-mergedapiexecutionrolearn""", alias="MergedApiExecutionRoleArn")
    OwnerContact_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-ownercontact""", alias="OwnerContact")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-name""", alias="Name")
    AdditionalAuthenticationProviders_: Optional[List['AdditionalAuthenticationProvider']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-additionalauthenticationproviders""", alias="AdditionalAuthenticationProviders")
    ApiType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-apitype""", alias="ApiType")
    LambdaAuthorizerConfig_: Optional['LambdaAuthorizerConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig""", alias="LambdaAuthorizerConfig")
    XrayEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-xrayenabled""", alias="XrayEnabled")
    Visibility_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-visibility""", alias="Visibility")
    UserPoolConfig_: Optional['UserPoolConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-userpoolconfig""", alias="UserPoolConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-tags""", alias="Tags")
    AuthenticationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-authenticationtype""", alias="AuthenticationType")
    LogConfig_: Optional['LogConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-logconfig""", alias="LogConfig")
    

    @property
    def tropo_type(self) -> troposphere.appsync.GraphQLApi:
        from troposphere.appsync import GraphQLApi as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appsync import GraphQLApi as TropoT
        return resource_to_troposphere(self, TropoT)


class GraphQLSchema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html
    Properties:
        - Name: Definition
        - Name: DefinitionS3Location
        - Name: ApiId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Definition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definition""", alias="Definition")
    DefinitionS3Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definitions3location""", alias="DefinitionS3Location")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-apiid""", alias="ApiId")
    

    @property
    def tropo_type(self) -> troposphere.appsync.GraphQLSchema:
        from troposphere.appsync import GraphQLSchema as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appsync import GraphQLSchema as TropoT
        return resource_to_troposphere(self, TropoT)


class Resolver(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html
    Properties:
        - Name: TypeName
        - Name: PipelineConfig
        - Name: RequestMappingTemplate
        - Name: ResponseMappingTemplate
        - Name: MaxBatchSize
        - Name: SyncConfig
        - Name: Code
        - Name: ResponseMappingTemplateS3Location
        - Name: Runtime
        - Name: CodeS3Location
        - Name: DataSourceName
        - Name: Kind
        - Name: CachingConfig
        - Name: RequestMappingTemplateS3Location
        - Name: ApiId
        - Name: FieldName
    Attributes:
        - Name: TypeName
        - Name: ResolverArn
        - Name: FieldName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TypeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-typename""", alias="TypeName")
    PipelineConfig_: Optional['PipelineConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-pipelineconfig""", alias="PipelineConfig")
    RequestMappingTemplate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplate""", alias="RequestMappingTemplate")
    ResponseMappingTemplate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplate""", alias="ResponseMappingTemplate")
    MaxBatchSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-maxbatchsize""", alias="MaxBatchSize")
    SyncConfig_: Optional['SyncConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-syncconfig""", alias="SyncConfig")
    Code_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-code""", alias="Code")
    ResponseMappingTemplateS3Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplates3location""", alias="ResponseMappingTemplateS3Location")
    Runtime_: Optional['AppSyncRuntime'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-runtime""", alias="Runtime")
    CodeS3Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-codes3location""", alias="CodeS3Location")
    DataSourceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-datasourcename""", alias="DataSourceName")
    Kind_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-kind""", alias="Kind")
    CachingConfig_: Optional['CachingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-cachingconfig""", alias="CachingConfig")
    RequestMappingTemplateS3Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplates3location""", alias="RequestMappingTemplateS3Location")
    ApiId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-apiid""", alias="ApiId")
    FieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-fieldname""", alias="FieldName")
    

    @property
    def tropo_type(self) -> troposphere.appsync.Resolver:
        from troposphere.appsync import Resolver as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appsync import Resolver as TropoT
        return resource_to_troposphere(self, TropoT)


class SourceApiAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-sourceapiassociation.html
    Properties:
        - Name: Description
        - Name: SourceApiAssociationConfig
        - Name: MergedApiIdentifier
        - Name: SourceApiIdentifier
    Attributes:
        - Name: AssociationArn
        - Name: MergedApiId
        - Name: SourceApiArn
        - Name: LastSuccessfulMergeDate
        - Name: SourceApiAssociationStatusDetail
        - Name: MergedApiArn
        - Name: AssociationId
        - Name: SourceApiAssociationStatus
        - Name: SourceApiId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-sourceapiassociation.html#cfn-appsync-sourceapiassociation-description""", alias="Description")
    SourceApiAssociationConfig_: Optional['SourceApiAssociationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-sourceapiassociation.html#cfn-appsync-sourceapiassociation-sourceapiassociationconfig""", alias="SourceApiAssociationConfig")
    MergedApiIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-sourceapiassociation.html#cfn-appsync-sourceapiassociation-mergedapiidentifier""", alias="MergedApiIdentifier")
    SourceApiIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-sourceapiassociation.html#cfn-appsync-sourceapiassociation-sourceapiidentifier""", alias="SourceApiIdentifier")
    

    @property
    def tropo_type(self) -> troposphere.appsync.SourceApiAssociation:
        from troposphere.appsync import SourceApiAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appsync import SourceApiAssociation as TropoT
        return resource_to_troposphere(self, TropoT)

