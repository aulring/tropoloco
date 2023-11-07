from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ApiGatewayProxyInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-application-apigatewayproxyinput.html
    Properties:
        - Name: StageName
        - Name: EndpointType
    
    """
    
    StageName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-application-apigatewayproxyinput.html#cfn-refactorspaces-application-apigatewayproxyinput-stagename""", alias="StageName")
    EndpointType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-application-apigatewayproxyinput.html#cfn-refactorspaces-application-apigatewayproxyinput-endpointtype""", alias="EndpointType")
    


    @property
    def tropo_type(self) -> troposphere.refactorspaces.ApiGatewayProxyInput:
        from troposphere.refactorspaces import ApiGatewayProxyInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefaultRouteInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-defaultrouteinput.html
    Properties:
        - Name: ActivationState
    
    """
    
    ActivationState_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-defaultrouteinput.html#cfn-refactorspaces-route-defaultrouteinput-activationstate""", alias="ActivationState")
    


    @property
    def tropo_type(self) -> troposphere.refactorspaces.DefaultRouteInput:
        from troposphere.refactorspaces import DefaultRouteInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UriPathRouteInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html
    Properties:
        - Name: SourcePath
        - Name: AppendSourcePath
        - Name: ActivationState
        - Name: Methods
        - Name: IncludeChildPaths
    
    """
    
    SourcePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-sourcepath""", alias="SourcePath")
    AppendSourcePath_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-appendsourcepath""", alias="AppendSourcePath")
    ActivationState_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-activationstate""", alias="ActivationState")
    Methods_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-methods""", alias="Methods")
    IncludeChildPaths_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-includechildpaths""", alias="IncludeChildPaths")
    


    @property
    def tropo_type(self) -> troposphere.refactorspaces.UriPathRouteInput:
        from troposphere.refactorspaces import UriPathRouteInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaEndpointInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-lambdaendpointinput.html
    Properties:
        - Name: Arn
    
    """
    
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-lambdaendpointinput.html#cfn-refactorspaces-service-lambdaendpointinput-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.refactorspaces.LambdaEndpointInput:
        from troposphere.refactorspaces import LambdaEndpointInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UrlEndpointInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-urlendpointinput.html
    Properties:
        - Name: HealthUrl
        - Name: Url
    
    """
    
    HealthUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-urlendpointinput.html#cfn-refactorspaces-service-urlendpointinput-healthurl""", alias="HealthUrl")
    Url_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-urlendpointinput.html#cfn-refactorspaces-service-urlendpointinput-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.refactorspaces.UrlEndpointInput:
        from troposphere.refactorspaces import UrlEndpointInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Application(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html
    Properties:
        - Name: EnvironmentIdentifier
        - Name: VpcId
        - Name: ApiGatewayProxy
        - Name: ProxyType
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: NlbArn
        - Name: ProxyUrl
        - Name: NlbName
        - Name: StageName
        - Name: ApiGatewayId
        - Name: VpcLinkId
        - Name: ApplicationIdentifier
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EnvironmentIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-environmentidentifier""", alias="EnvironmentIdentifier")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-vpcid""", alias="VpcId")
    ApiGatewayProxy_: Optional['ApiGatewayProxyInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-apigatewayproxy""", alias="ApiGatewayProxy")
    ProxyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-proxytype""", alias="ProxyType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.refactorspaces.Application:
        from troposphere.refactorspaces import Application as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.refactorspaces import Application as TropoT
        return resource_to_troposphere(self, TropoT)


class Environment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html
    Properties:
        - Name: Description
        - Name: NetworkFabricType
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: TransitGatewayId
        - Name: EnvironmentIdentifier
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-description""", alias="Description")
    NetworkFabricType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-networkfabrictype""", alias="NetworkFabricType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.refactorspaces.Environment:
        from troposphere.refactorspaces import Environment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.refactorspaces import Environment as TropoT
        return resource_to_troposphere(self, TropoT)


class Route(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html
    Properties:
        - Name: UriPathRoute
        - Name: EnvironmentIdentifier
        - Name: RouteType
        - Name: DefaultRoute
        - Name: ServiceIdentifier
        - Name: ApplicationIdentifier
        - Name: Tags
    Attributes:
        - Name: RouteIdentifier
        - Name: Arn
        - Name: PathResourceToId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UriPathRoute_: Optional['UriPathRouteInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-uripathroute""", alias="UriPathRoute")
    EnvironmentIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-environmentidentifier""", alias="EnvironmentIdentifier")
    RouteType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-routetype""", alias="RouteType")
    DefaultRoute_: Optional['DefaultRouteInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-defaultroute""", alias="DefaultRoute")
    ServiceIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-serviceidentifier""", alias="ServiceIdentifier")
    ApplicationIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-applicationidentifier""", alias="ApplicationIdentifier")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.refactorspaces.Route:
        from troposphere.refactorspaces import Route as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.refactorspaces import Route as TropoT
        return resource_to_troposphere(self, TropoT)


class Service(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html
    Properties:
        - Name: LambdaEndpoint
        - Name: UrlEndpoint
        - Name: Description
        - Name: EnvironmentIdentifier
        - Name: VpcId
        - Name: EndpointType
        - Name: ApplicationIdentifier
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ServiceIdentifier
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LambdaEndpoint_: Optional['LambdaEndpointInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-lambdaendpoint""", alias="LambdaEndpoint")
    UrlEndpoint_: Optional['UrlEndpointInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-urlendpoint""", alias="UrlEndpoint")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-description""", alias="Description")
    EnvironmentIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-environmentidentifier""", alias="EnvironmentIdentifier")
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-vpcid""", alias="VpcId")
    EndpointType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-endpointtype""", alias="EndpointType")
    ApplicationIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-applicationidentifier""", alias="ApplicationIdentifier")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.refactorspaces.Service:
        from troposphere.refactorspaces import Service as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.refactorspaces import Service as TropoT
        return resource_to_troposphere(self, TropoT)

