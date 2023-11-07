from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ApiKeyAuthParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-apikeyauthparameters.html
    Properties:
        - Name: ApiKeyValue
        - Name: ApiKeyName
    
    """
    
    ApiKeyValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-apikeyauthparameters.html#cfn-events-connection-apikeyauthparameters-apikeyvalue""", alias="ApiKeyValue")
    ApiKeyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-apikeyauthparameters.html#cfn-events-connection-apikeyauthparameters-apikeyname""", alias="ApiKeyName")
    


    @property
    def tropo_type(self) -> troposphere.events.ApiKeyAuthParameters:
        from troposphere.events import ApiKeyAuthParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuthParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-authparameters.html
    Properties:
        - Name: InvocationHttpParameters
        - Name: BasicAuthParameters
        - Name: ApiKeyAuthParameters
        - Name: OAuthParameters
    
    """
    
    InvocationHttpParameters_: Optional['ConnectionHttpParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-authparameters.html#cfn-events-connection-authparameters-invocationhttpparameters""", alias="InvocationHttpParameters")
    BasicAuthParameters_: Optional['BasicAuthParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-authparameters.html#cfn-events-connection-authparameters-basicauthparameters""", alias="BasicAuthParameters")
    ApiKeyAuthParameters_: Optional['ApiKeyAuthParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-authparameters.html#cfn-events-connection-authparameters-apikeyauthparameters""", alias="ApiKeyAuthParameters")
    OAuthParameters_: Optional['OAuthParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-authparameters.html#cfn-events-connection-authparameters-oauthparameters""", alias="OAuthParameters")
    


    @property
    def tropo_type(self) -> troposphere.events.AuthParameters:
        from troposphere.events import AuthParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BasicAuthParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-basicauthparameters.html
    Properties:
        - Name: Username
        - Name: Password
    
    """
    
    Username_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-basicauthparameters.html#cfn-events-connection-basicauthparameters-username""", alias="Username")
    Password_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-basicauthparameters.html#cfn-events-connection-basicauthparameters-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.events.BasicAuthParameters:
        from troposphere.events import BasicAuthParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClientParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-clientparameters.html
    Properties:
        - Name: ClientSecret
        - Name: ClientID
    
    """
    
    ClientSecret_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-clientparameters.html#cfn-events-connection-clientparameters-clientsecret""", alias="ClientSecret")
    ClientID_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-clientparameters.html#cfn-events-connection-clientparameters-clientid""", alias="ClientID")
    


    @property
    def tropo_type(self) -> troposphere.events.ClientParameters:
        from troposphere.events import ClientParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectionHttpParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-connectionhttpparameters.html
    Properties:
        - Name: HeaderParameters
        - Name: QueryStringParameters
        - Name: BodyParameters
    
    """
    
    HeaderParameters_: Optional[List['Parameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-connectionhttpparameters.html#cfn-events-connection-connectionhttpparameters-headerparameters""", alias="HeaderParameters")
    QueryStringParameters_: Optional[List['Parameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-connectionhttpparameters.html#cfn-events-connection-connectionhttpparameters-querystringparameters""", alias="QueryStringParameters")
    BodyParameters_: Optional[List['Parameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-connectionhttpparameters.html#cfn-events-connection-connectionhttpparameters-bodyparameters""", alias="BodyParameters")
    


    @property
    def tropo_type(self) -> troposphere.events.ConnectionHttpParameters:
        from troposphere.events import ConnectionHttpParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OAuthParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-oauthparameters.html
    Properties:
        - Name: ClientParameters
        - Name: OAuthHttpParameters
        - Name: AuthorizationEndpoint
        - Name: HttpMethod
    
    """
    
    ClientParameters_: 'ClientParameters' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-oauthparameters.html#cfn-events-connection-oauthparameters-clientparameters""", alias="ClientParameters")
    OAuthHttpParameters_: Optional['ConnectionHttpParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-oauthparameters.html#cfn-events-connection-oauthparameters-oauthhttpparameters""", alias="OAuthHttpParameters")
    AuthorizationEndpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-oauthparameters.html#cfn-events-connection-oauthparameters-authorizationendpoint""", alias="AuthorizationEndpoint")
    HttpMethod_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-oauthparameters.html#cfn-events-connection-oauthparameters-httpmethod""", alias="HttpMethod")
    


    @property
    def tropo_type(self) -> troposphere.events.OAuthParameters:
        from troposphere.events import OAuthParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Parameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-parameter.html
    Properties:
        - Name: Value
        - Name: IsValueSecret
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-parameter.html#cfn-events-connection-parameter-value""", alias="Value")
    IsValueSecret_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-parameter.html#cfn-events-connection-parameter-isvaluesecret""", alias="IsValueSecret")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-parameter.html#cfn-events-connection-parameter-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.events.Parameter:
        from troposphere.events import Parameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EndpointEventBus(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-endpointeventbus.html
    Properties:
        - Name: EventBusArn
    
    """
    
    EventBusArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-endpointeventbus.html#cfn-events-endpoint-endpointeventbus-eventbusarn""", alias="EventBusArn")
    


    @property
    def tropo_type(self) -> troposphere.events.EndpointEventBus:
        from troposphere.events import EndpointEventBus as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FailoverConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-failoverconfig.html
    Properties:
        - Name: Secondary
        - Name: Primary
    
    """
    
    Secondary_: 'Secondary' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-failoverconfig.html#cfn-events-endpoint-failoverconfig-secondary""", alias="Secondary")
    Primary_: 'Primary' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-failoverconfig.html#cfn-events-endpoint-failoverconfig-primary""", alias="Primary")
    


    @property
    def tropo_type(self) -> troposphere.events.FailoverConfig:
        from troposphere.events import FailoverConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Primary(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-primary.html
    Properties:
        - Name: HealthCheck
    
    """
    
    HealthCheck_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-primary.html#cfn-events-endpoint-primary-healthcheck""", alias="HealthCheck")
    


    @property
    def tropo_type(self) -> troposphere.events.Primary:
        from troposphere.events import Primary as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-replicationconfig.html
    Properties:
        - Name: State
    
    """
    
    State_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-replicationconfig.html#cfn-events-endpoint-replicationconfig-state""", alias="State")
    


    @property
    def tropo_type(self) -> troposphere.events.ReplicationConfig:
        from troposphere.events import ReplicationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RoutingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-routingconfig.html
    Properties:
        - Name: FailoverConfig
    
    """
    
    FailoverConfig_: 'FailoverConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-routingconfig.html#cfn-events-endpoint-routingconfig-failoverconfig""", alias="FailoverConfig")
    


    @property
    def tropo_type(self) -> troposphere.events.RoutingConfig:
        from troposphere.events import RoutingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Secondary(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-secondary.html
    Properties:
        - Name: Route
    
    """
    
    Route_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-secondary.html#cfn-events-endpoint-secondary-route""", alias="Route")
    


    @property
    def tropo_type(self) -> troposphere.events.Secondary:
        from troposphere.events import Secondary as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Condition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html
    Properties:
        - Name: Type
        - Name: Value
        - Name: Key
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html#cfn-events-eventbuspolicy-condition-type""", alias="Type")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html#cfn-events-eventbuspolicy-condition-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html#cfn-events-eventbuspolicy-condition-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.events.Condition:
        from troposphere.events import Condition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AwsVpcConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-awsvpcconfiguration.html
    Properties:
        - Name: SecurityGroups
        - Name: Subnets
        - Name: AssignPublicIp
    
    """
    
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-awsvpcconfiguration.html#cfn-events-rule-awsvpcconfiguration-securitygroups""", alias="SecurityGroups")
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-awsvpcconfiguration.html#cfn-events-rule-awsvpcconfiguration-subnets""", alias="Subnets")
    AssignPublicIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-awsvpcconfiguration.html#cfn-events-rule-awsvpcconfiguration-assignpublicip""", alias="AssignPublicIp")
    


    @property
    def tropo_type(self) -> troposphere.events.AwsVpcConfiguration:
        from troposphere.events import AwsVpcConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchArrayProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batcharrayproperties.html
    Properties:
        - Name: Size
    
    """
    
    Size_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batcharrayproperties.html#cfn-events-rule-batcharrayproperties-size""", alias="Size")
    


    @property
    def tropo_type(self) -> troposphere.events.BatchArrayProperties:
        from troposphere.events import BatchArrayProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batchparameters.html
    Properties:
        - Name: ArrayProperties
        - Name: JobName
        - Name: RetryStrategy
        - Name: JobDefinition
    
    """
    
    ArrayProperties_: Optional['BatchArrayProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batchparameters.html#cfn-events-rule-batchparameters-arrayproperties""", alias="ArrayProperties")
    JobName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batchparameters.html#cfn-events-rule-batchparameters-jobname""", alias="JobName")
    RetryStrategy_: Optional['BatchRetryStrategy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batchparameters.html#cfn-events-rule-batchparameters-retrystrategy""", alias="RetryStrategy")
    JobDefinition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batchparameters.html#cfn-events-rule-batchparameters-jobdefinition""", alias="JobDefinition")
    


    @property
    def tropo_type(self) -> troposphere.events.BatchParameters:
        from troposphere.events import BatchParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchRetryStrategy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batchretrystrategy.html
    Properties:
        - Name: Attempts
    
    """
    
    Attempts_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-batchretrystrategy.html#cfn-events-rule-batchretrystrategy-attempts""", alias="Attempts")
    


    @property
    def tropo_type(self) -> troposphere.events.BatchRetryStrategy:
        from troposphere.events import BatchRetryStrategy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacityProviderStrategyItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-capacityproviderstrategyitem.html
    Properties:
        - Name: CapacityProvider
        - Name: Base
        - Name: Weight
    
    """
    
    CapacityProvider_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-capacityproviderstrategyitem.html#cfn-events-rule-capacityproviderstrategyitem-capacityprovider""", alias="CapacityProvider")
    Base_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-capacityproviderstrategyitem.html#cfn-events-rule-capacityproviderstrategyitem-base""", alias="Base")
    Weight_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-capacityproviderstrategyitem.html#cfn-events-rule-capacityproviderstrategyitem-weight""", alias="Weight")
    


    @property
    def tropo_type(self) -> troposphere.events.CapacityProviderStrategyItem:
        from troposphere.events import CapacityProviderStrategyItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeadLetterConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-deadletterconfig.html
    Properties:
        - Name: Arn
    
    """
    
    Arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-deadletterconfig.html#cfn-events-rule-deadletterconfig-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.events.DeadLetterConfig:
        from troposphere.events import DeadLetterConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EcsParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html
    Properties:
        - Name: PlatformVersion
        - Name: Group
        - Name: EnableECSManagedTags
        - Name: EnableExecuteCommand
        - Name: PlacementConstraints
        - Name: PropagateTags
        - Name: TaskCount
        - Name: PlacementStrategies
        - Name: CapacityProviderStrategy
        - Name: LaunchType
        - Name: ReferenceId
        - Name: TagList
        - Name: NetworkConfiguration
        - Name: TaskDefinitionArn
    
    """
    
    PlatformVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-platformversion""", alias="PlatformVersion")
    Group_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-group""", alias="Group")
    EnableECSManagedTags_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-enableecsmanagedtags""", alias="EnableECSManagedTags")
    EnableExecuteCommand_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-enableexecutecommand""", alias="EnableExecuteCommand")
    PlacementConstraints_: Optional[List['PlacementConstraint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-placementconstraints""", alias="PlacementConstraints")
    PropagateTags_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-propagatetags""", alias="PropagateTags")
    TaskCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-taskcount""", alias="TaskCount")
    PlacementStrategies_: Optional[List['PlacementStrategy']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-placementstrategies""", alias="PlacementStrategies")
    CapacityProviderStrategy_: Optional[List['CapacityProviderStrategyItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-capacityproviderstrategy""", alias="CapacityProviderStrategy")
    LaunchType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-launchtype""", alias="LaunchType")
    ReferenceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-referenceid""", alias="ReferenceId")
    TagList_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-taglist""", alias="TagList")
    NetworkConfiguration_: Optional['NetworkConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-networkconfiguration""", alias="NetworkConfiguration")
    TaskDefinitionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-taskdefinitionarn""", alias="TaskDefinitionArn")
    


    @property
    def tropo_type(self) -> troposphere.events.EcsParameters:
        from troposphere.events import EcsParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-httpparameters.html
    Properties:
        - Name: PathParameterValues
        - Name: HeaderParameters
        - Name: QueryStringParameters
    
    """
    
    PathParameterValues_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-httpparameters.html#cfn-events-rule-httpparameters-pathparametervalues""", alias="PathParameterValues")
    HeaderParameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-httpparameters.html#cfn-events-rule-httpparameters-headerparameters""", alias="HeaderParameters")
    QueryStringParameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-httpparameters.html#cfn-events-rule-httpparameters-querystringparameters""", alias="QueryStringParameters")
    


    @property
    def tropo_type(self) -> troposphere.events.HttpParameters:
        from troposphere.events import HttpParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputTransformer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html
    Properties:
        - Name: InputPathsMap
        - Name: InputTemplate
    
    """
    
    InputPathsMap_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html#cfn-events-rule-inputtransformer-inputpathsmap""", alias="InputPathsMap")
    InputTemplate_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html#cfn-events-rule-inputtransformer-inputtemplate""", alias="InputTemplate")
    


    @property
    def tropo_type(self) -> troposphere.events.InputTransformer:
        from troposphere.events import InputTransformer as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-kinesisparameters.html
    Properties:
        - Name: PartitionKeyPath
    
    """
    
    PartitionKeyPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-kinesisparameters.html#cfn-events-rule-kinesisparameters-partitionkeypath""", alias="PartitionKeyPath")
    


    @property
    def tropo_type(self) -> troposphere.events.KinesisParameters:
        from troposphere.events import KinesisParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-networkconfiguration.html
    Properties:
        - Name: AwsVpcConfiguration
    
    """
    
    AwsVpcConfiguration_: Optional['AwsVpcConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-networkconfiguration.html#cfn-events-rule-networkconfiguration-awsvpcconfiguration""", alias="AwsVpcConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.events.NetworkConfiguration:
        from troposphere.events import NetworkConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PlacementConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementconstraint.html
    Properties:
        - Name: Type
        - Name: Expression
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementconstraint.html#cfn-events-rule-placementconstraint-type""", alias="Type")
    Expression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementconstraint.html#cfn-events-rule-placementconstraint-expression""", alias="Expression")
    


    @property
    def tropo_type(self) -> troposphere.events.PlacementConstraint:
        from troposphere.events import PlacementConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PlacementStrategy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementstrategy.html
    Properties:
        - Name: Field
        - Name: Type
    
    """
    
    Field_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementstrategy.html#cfn-events-rule-placementstrategy-field""", alias="Field")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementstrategy.html#cfn-events-rule-placementstrategy-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.events.PlacementStrategy:
        from troposphere.events import PlacementStrategy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RedshiftDataParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-redshiftdataparameters.html
    Properties:
        - Name: StatementName
        - Name: Sqls
        - Name: Database
        - Name: SecretManagerArn
        - Name: DbUser
        - Name: Sql
        - Name: WithEvent
    
    """
    
    StatementName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-redshiftdataparameters.html#cfn-events-rule-redshiftdataparameters-statementname""", alias="StatementName")
    Sqls_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-redshiftdataparameters.html#cfn-events-rule-redshiftdataparameters-sqls""", alias="Sqls")
    Database_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-redshiftdataparameters.html#cfn-events-rule-redshiftdataparameters-database""", alias="Database")
    SecretManagerArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-redshiftdataparameters.html#cfn-events-rule-redshiftdataparameters-secretmanagerarn""", alias="SecretManagerArn")
    DbUser_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-redshiftdataparameters.html#cfn-events-rule-redshiftdataparameters-dbuser""", alias="DbUser")
    Sql_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-redshiftdataparameters.html#cfn-events-rule-redshiftdataparameters-sql""", alias="Sql")
    WithEvent_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-redshiftdataparameters.html#cfn-events-rule-redshiftdataparameters-withevent""", alias="WithEvent")
    


    @property
    def tropo_type(self) -> troposphere.events.RedshiftDataParameters:
        from troposphere.events import RedshiftDataParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RetryPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-retrypolicy.html
    Properties:
        - Name: MaximumRetryAttempts
        - Name: MaximumEventAgeInSeconds
    
    """
    
    MaximumRetryAttempts_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-retrypolicy.html#cfn-events-rule-retrypolicy-maximumretryattempts""", alias="MaximumRetryAttempts")
    MaximumEventAgeInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-retrypolicy.html#cfn-events-rule-retrypolicy-maximumeventageinseconds""", alias="MaximumEventAgeInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.events.RetryPolicy:
        from troposphere.events import RetryPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RunCommandParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandparameters.html
    Properties:
        - Name: RunCommandTargets
    
    """
    
    RunCommandTargets_: List['RunCommandTarget'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandparameters.html#cfn-events-rule-runcommandparameters-runcommandtargets""", alias="RunCommandTargets")
    


    @property
    def tropo_type(self) -> troposphere.events.RunCommandParameters:
        from troposphere.events import RunCommandParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RunCommandTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html
    Properties:
        - Name: Values
        - Name: Key
    
    """
    
    Values_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html#cfn-events-rule-runcommandtarget-values""", alias="Values")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html#cfn-events-rule-runcommandtarget-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.events.RunCommandTarget:
        from troposphere.events import RunCommandTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SageMakerPipelineParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sagemakerpipelineparameter.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sagemakerpipelineparameter.html#cfn-events-rule-sagemakerpipelineparameter-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sagemakerpipelineparameter.html#cfn-events-rule-sagemakerpipelineparameter-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.events.SageMakerPipelineParameter:
        from troposphere.events import SageMakerPipelineParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SageMakerPipelineParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sagemakerpipelineparameters.html
    Properties:
        - Name: PipelineParameterList
    
    """
    
    PipelineParameterList_: Optional[List['SageMakerPipelineParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sagemakerpipelineparameters.html#cfn-events-rule-sagemakerpipelineparameters-pipelineparameterlist""", alias="PipelineParameterList")
    


    @property
    def tropo_type(self) -> troposphere.events.SageMakerPipelineParameters:
        from troposphere.events import SageMakerPipelineParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SqsParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sqsparameters.html
    Properties:
        - Name: MessageGroupId
    
    """
    
    MessageGroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sqsparameters.html#cfn-events-rule-sqsparameters-messagegroupid""", alias="MessageGroupId")
    


    @property
    def tropo_type(self) -> troposphere.events.SqsParameters:
        from troposphere.events import SqsParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Target(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html
    Properties:
        - Name: InputPath
        - Name: HttpParameters
        - Name: DeadLetterConfig
        - Name: RunCommandParameters
        - Name: InputTransformer
        - Name: KinesisParameters
        - Name: RoleArn
        - Name: RedshiftDataParameters
        - Name: Input
        - Name: SqsParameters
        - Name: EcsParameters
        - Name: BatchParameters
        - Name: Id
        - Name: Arn
        - Name: SageMakerPipelineParameters
        - Name: RetryPolicy
    
    """
    
    InputPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-inputpath""", alias="InputPath")
    HttpParameters_: Optional['HttpParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-httpparameters""", alias="HttpParameters")
    DeadLetterConfig_: Optional['DeadLetterConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-deadletterconfig""", alias="DeadLetterConfig")
    RunCommandParameters_: Optional['RunCommandParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-runcommandparameters""", alias="RunCommandParameters")
    InputTransformer_: Optional['InputTransformer'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-inputtransformer""", alias="InputTransformer")
    KinesisParameters_: Optional['KinesisParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-kinesisparameters""", alias="KinesisParameters")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-rolearn""", alias="RoleArn")
    RedshiftDataParameters_: Optional['RedshiftDataParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-redshiftdataparameters""", alias="RedshiftDataParameters")
    Input_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-input""", alias="Input")
    SqsParameters_: Optional['SqsParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-sqsparameters""", alias="SqsParameters")
    EcsParameters_: Optional['EcsParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-ecsparameters""", alias="EcsParameters")
    BatchParameters_: Optional['BatchParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-batchparameters""", alias="BatchParameters")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-id""", alias="Id")
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-arn""", alias="Arn")
    SageMakerPipelineParameters_: Optional['SageMakerPipelineParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-sagemakerpipelineparameters""", alias="SageMakerPipelineParameters")
    RetryPolicy_: Optional['RetryPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-retrypolicy""", alias="RetryPolicy")
    


    @property
    def tropo_type(self) -> troposphere.events.Target:
        from troposphere.events import Target as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ApiDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.html
    Properties:
        - Name: Description
        - Name: ConnectionArn
        - Name: InvocationEndpoint
        - Name: HttpMethod
        - Name: Name
        - Name: InvocationRateLimitPerSecond
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.html#cfn-events-apidestination-description""", alias="Description")
    ConnectionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.html#cfn-events-apidestination-connectionarn""", alias="ConnectionArn")
    InvocationEndpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.html#cfn-events-apidestination-invocationendpoint""", alias="InvocationEndpoint")
    HttpMethod_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.html#cfn-events-apidestination-httpmethod""", alias="HttpMethod")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.html#cfn-events-apidestination-name""", alias="Name")
    InvocationRateLimitPerSecond_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-apidestination.html#cfn-events-apidestination-invocationratelimitpersecond""", alias="InvocationRateLimitPerSecond")
    

    @property
    def tropo_type(self) -> troposphere.events.ApiDestination:
        from troposphere.events import ApiDestination as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.events import ApiDestination as TropoT
        return resource_to_troposphere(self, TropoT)


class Archive(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-archive.html
    Properties:
        - Name: EventPattern
        - Name: Description
        - Name: SourceArn
        - Name: ArchiveName
        - Name: RetentionDays
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EventPattern_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-archive.html#cfn-events-archive-eventpattern""", alias="EventPattern")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-archive.html#cfn-events-archive-description""", alias="Description")
    SourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-archive.html#cfn-events-archive-sourcearn""", alias="SourceArn")
    ArchiveName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-archive.html#cfn-events-archive-archivename""", alias="ArchiveName")
    RetentionDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-archive.html#cfn-events-archive-retentiondays""", alias="RetentionDays")
    

    @property
    def tropo_type(self) -> troposphere.events.Archive:
        from troposphere.events import Archive as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.events import Archive as TropoT
        return resource_to_troposphere(self, TropoT)


class Connection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-connection.html
    Properties:
        - Name: AuthParameters
        - Name: Description
        - Name: AuthorizationType
        - Name: Name
    Attributes:
        - Name: SecretArn
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AuthParameters_: Optional['AuthParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-connection.html#cfn-events-connection-authparameters""", alias="AuthParameters")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-connection.html#cfn-events-connection-description""", alias="Description")
    AuthorizationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-connection.html#cfn-events-connection-authorizationtype""", alias="AuthorizationType")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-connection.html#cfn-events-connection-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.events.Connection:
        from troposphere.events import Connection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.events import Connection as TropoT
        return resource_to_troposphere(self, TropoT)


class Endpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.html
    Properties:
        - Name: EventBuses
        - Name: Description
        - Name: ReplicationConfig
        - Name: RoutingConfig
        - Name: RoleArn
        - Name: Name
    Attributes:
        - Name: State
        - Name: StateReason
        - Name: EndpointId
        - Name: Arn
        - Name: EndpointUrl
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EventBuses_: List['EndpointEventBus'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.html#cfn-events-endpoint-eventbuses""", alias="EventBuses")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.html#cfn-events-endpoint-description""", alias="Description")
    ReplicationConfig_: Optional['ReplicationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.html#cfn-events-endpoint-replicationconfig""", alias="ReplicationConfig")
    RoutingConfig_: 'RoutingConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.html#cfn-events-endpoint-routingconfig""", alias="RoutingConfig")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.html#cfn-events-endpoint-rolearn""", alias="RoleArn")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.html#cfn-events-endpoint-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.events.Endpoint:
        from troposphere.events import Endpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.events import Endpoint as TropoT
        return resource_to_troposphere(self, TropoT)


class EventBus(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.html
    Properties:
        - Name: Policy
        - Name: EventSourceName
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.html#cfn-events-eventbus-policy""", alias="Policy")
    EventSourceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.html#cfn-events-eventbus-eventsourcename""", alias="EventSourceName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.html#cfn-events-eventbus-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.html#cfn-events-eventbus-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.events.EventBus:
        from troposphere.events import EventBus as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.events import EventBus as TropoT
        return resource_to_troposphere(self, TropoT)


class EventBusPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html
    Properties:
        - Name: EventBusName
        - Name: Condition
        - Name: Action
        - Name: StatementId
        - Name: Statement
        - Name: Principal
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EventBusName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-eventbusname""", alias="EventBusName")
    Condition_: Optional['Condition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-condition""", alias="Condition")
    Action_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-action""", alias="Action")
    StatementId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-statementid""", alias="StatementId")
    Statement_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-statement""", alias="Statement")
    Principal_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-principal""", alias="Principal")
    

    @property
    def tropo_type(self) -> troposphere.events.EventBusPolicy:
        from troposphere.events import EventBusPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.events import EventBusPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html
    Properties:
        - Name: EventBusName
        - Name: EventPattern
        - Name: ScheduleExpression
        - Name: Description
        - Name: State
        - Name: Targets
        - Name: RoleArn
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EventBusName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-eventbusname""", alias="EventBusName")
    EventPattern_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-eventpattern""", alias="EventPattern")
    ScheduleExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-scheduleexpression""", alias="ScheduleExpression")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-description""", alias="Description")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-state""", alias="State")
    Targets_: Optional[List['Target']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-targets""", alias="Targets")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-rolearn""", alias="RoleArn")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.events.Rule:
        from troposphere.events import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.events import Rule as TropoT
        return resource_to_troposphere(self, TropoT)

