from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class GatewayRouteHostnameMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html
    Properties:
        - Name: Suffix
        - Name: Exact
    
    """
    
    Suffix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html#cfn-appmesh-gatewayroute-gatewayroutehostnamematch-suffix""", alias="Suffix")
    Exact_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html#cfn-appmesh-gatewayroute-gatewayroutehostnamematch-exact""", alias="Exact")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GatewayRouteHostnameMatch:
        from troposphere.appmesh import GatewayRouteHostnameMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GatewayRouteHostnameRewrite(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.html
    Properties:
        - Name: DefaultTargetHostname
    
    """
    
    DefaultTargetHostname_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.html#cfn-appmesh-gatewayroute-gatewayroutehostnamerewrite-defaulttargethostname""", alias="DefaultTargetHostname")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GatewayRouteHostnameRewrite:
        from troposphere.appmesh import GatewayRouteHostnameRewrite as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GatewayRouteMetadataMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html
    Properties:
        - Name: Suffix
        - Name: Regex
        - Name: Exact
        - Name: Prefix
        - Name: Range
    
    """
    
    Suffix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-suffix""", alias="Suffix")
    Regex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-regex""", alias="Regex")
    Exact_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-exact""", alias="Exact")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-prefix""", alias="Prefix")
    Range_: Optional['GatewayRouteRangeMatch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-range""", alias="Range")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GatewayRouteMetadataMatch:
        from troposphere.appmesh import GatewayRouteMetadataMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GatewayRouteRangeMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html
    Properties:
        - Name: Start
        - Name: End
    
    """
    
    Start_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html#cfn-appmesh-gatewayroute-gatewayrouterangematch-start""", alias="Start")
    End_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html#cfn-appmesh-gatewayroute-gatewayrouterangematch-end""", alias="End")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GatewayRouteRangeMatch:
        from troposphere.appmesh import GatewayRouteRangeMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GatewayRouteSpec(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html
    Properties:
        - Name: HttpRoute
        - Name: Priority
        - Name: Http2Route
        - Name: GrpcRoute
    
    """
    
    HttpRoute_: Optional['HttpGatewayRoute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-httproute""", alias="HttpRoute")
    Priority_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-priority""", alias="Priority")
    Http2Route_: Optional['HttpGatewayRoute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-http2route""", alias="Http2Route")
    GrpcRoute_: Optional['GrpcGatewayRoute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-grpcroute""", alias="GrpcRoute")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GatewayRouteSpec:
        from troposphere.appmesh import GatewayRouteSpec as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GatewayRouteTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html
    Properties:
        - Name: Port
        - Name: VirtualService
    
    """
    
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html#cfn-appmesh-gatewayroute-gatewayroutetarget-port""", alias="Port")
    VirtualService_: 'GatewayRouteVirtualService' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html#cfn-appmesh-gatewayroute-gatewayroutetarget-virtualservice""", alias="VirtualService")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GatewayRouteTarget:
        from troposphere.appmesh import GatewayRouteTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GatewayRouteVirtualService(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice.html
    Properties:
        - Name: VirtualServiceName
    
    """
    
    VirtualServiceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice.html#cfn-appmesh-gatewayroute-gatewayroutevirtualservice-virtualservicename""", alias="VirtualServiceName")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GatewayRouteVirtualService:
        from troposphere.appmesh import GatewayRouteVirtualService as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrpcGatewayRoute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html
    Properties:
        - Name: Action
        - Name: Match
    
    """
    
    Action_: 'GrpcGatewayRouteAction' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html#cfn-appmesh-gatewayroute-grpcgatewayroute-action""", alias="Action")
    Match_: 'GrpcGatewayRouteMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html#cfn-appmesh-gatewayroute-grpcgatewayroute-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GrpcGatewayRoute:
        from troposphere.appmesh import GrpcGatewayRoute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrpcGatewayRouteAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html
    Properties:
        - Name: Target
        - Name: Rewrite
    
    """
    
    Target_: 'GatewayRouteTarget' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html#cfn-appmesh-gatewayroute-grpcgatewayrouteaction-target""", alias="Target")
    Rewrite_: Optional['GrpcGatewayRouteRewrite'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html#cfn-appmesh-gatewayroute-grpcgatewayrouteaction-rewrite""", alias="Rewrite")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GrpcGatewayRouteAction:
        from troposphere.appmesh import GrpcGatewayRouteAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrpcGatewayRouteMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html
    Properties:
        - Name: ServiceName
        - Name: Port
        - Name: Hostname
        - Name: Metadata
    
    """
    
    ServiceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-servicename""", alias="ServiceName")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-port""", alias="Port")
    Hostname_: Optional['GatewayRouteHostnameMatch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-hostname""", alias="Hostname")
    Metadata_: Optional[List['GrpcGatewayRouteMetadata']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-metadata""", alias="Metadata")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GrpcGatewayRouteMatch:
        from troposphere.appmesh import GrpcGatewayRouteMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrpcGatewayRouteMetadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html
    Properties:
        - Name: Invert
        - Name: Name
        - Name: Match
    
    """
    
    Invert_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-invert""", alias="Invert")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-name""", alias="Name")
    Match_: Optional['GatewayRouteMetadataMatch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GrpcGatewayRouteMetadata:
        from troposphere.appmesh import GrpcGatewayRouteMetadata as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrpcGatewayRouteRewrite(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html
    Properties:
        - Name: Hostname
    
    """
    
    Hostname_: Optional['GatewayRouteHostnameRewrite'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html#cfn-appmesh-gatewayroute-grpcgatewayrouterewrite-hostname""", alias="Hostname")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GrpcGatewayRouteRewrite:
        from troposphere.appmesh import GrpcGatewayRouteRewrite as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpGatewayRoute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html
    Properties:
        - Name: Action
        - Name: Match
    
    """
    
    Action_: 'HttpGatewayRouteAction' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html#cfn-appmesh-gatewayroute-httpgatewayroute-action""", alias="Action")
    Match_: 'HttpGatewayRouteMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html#cfn-appmesh-gatewayroute-httpgatewayroute-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpGatewayRoute:
        from troposphere.appmesh import HttpGatewayRoute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpGatewayRouteAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html
    Properties:
        - Name: Target
        - Name: Rewrite
    
    """
    
    Target_: 'GatewayRouteTarget' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html#cfn-appmesh-gatewayroute-httpgatewayrouteaction-target""", alias="Target")
    Rewrite_: Optional['HttpGatewayRouteRewrite'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html#cfn-appmesh-gatewayroute-httpgatewayrouteaction-rewrite""", alias="Rewrite")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpGatewayRouteAction:
        from troposphere.appmesh import HttpGatewayRouteAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpGatewayRouteHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html
    Properties:
        - Name: Invert
        - Name: Name
        - Name: Match
    
    """
    
    Invert_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html#cfn-appmesh-gatewayroute-httpgatewayrouteheader-invert""", alias="Invert")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html#cfn-appmesh-gatewayroute-httpgatewayrouteheader-name""", alias="Name")
    Match_: Optional['HttpGatewayRouteHeaderMatch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html#cfn-appmesh-gatewayroute-httpgatewayrouteheader-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpGatewayRouteHeader:
        from troposphere.appmesh import HttpGatewayRouteHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpGatewayRouteHeaderMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html
    Properties:
        - Name: Suffix
        - Name: Regex
        - Name: Exact
        - Name: Prefix
        - Name: Range
    
    """
    
    Suffix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-suffix""", alias="Suffix")
    Regex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-regex""", alias="Regex")
    Exact_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-exact""", alias="Exact")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-prefix""", alias="Prefix")
    Range_: Optional['GatewayRouteRangeMatch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-range""", alias="Range")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpGatewayRouteHeaderMatch:
        from troposphere.appmesh import HttpGatewayRouteHeaderMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpGatewayRouteMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html
    Properties:
        - Name: Path
        - Name: Headers
        - Name: Port
        - Name: Hostname
        - Name: Prefix
        - Name: Method
        - Name: QueryParameters
    
    """
    
    Path_: Optional['HttpPathMatch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-path""", alias="Path")
    Headers_: Optional[List['HttpGatewayRouteHeader']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-headers""", alias="Headers")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-port""", alias="Port")
    Hostname_: Optional['GatewayRouteHostnameMatch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-hostname""", alias="Hostname")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-prefix""", alias="Prefix")
    Method_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-method""", alias="Method")
    QueryParameters_: Optional[List['QueryParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-queryparameters""", alias="QueryParameters")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpGatewayRouteMatch:
        from troposphere.appmesh import HttpGatewayRouteMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpGatewayRoutePathRewrite(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.html
    Properties:
        - Name: Exact
    
    """
    
    Exact_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.html#cfn-appmesh-gatewayroute-httpgatewayroutepathrewrite-exact""", alias="Exact")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpGatewayRoutePathRewrite:
        from troposphere.appmesh import HttpGatewayRoutePathRewrite as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpGatewayRoutePrefixRewrite(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html
    Properties:
        - Name: Value
        - Name: DefaultPrefix
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-value""", alias="Value")
    DefaultPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-defaultprefix""", alias="DefaultPrefix")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpGatewayRoutePrefixRewrite:
        from troposphere.appmesh import HttpGatewayRoutePrefixRewrite as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpGatewayRouteRewrite(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html
    Properties:
        - Name: Path
        - Name: Hostname
        - Name: Prefix
    
    """
    
    Path_: Optional['HttpGatewayRoutePathRewrite'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-path""", alias="Path")
    Hostname_: Optional['GatewayRouteHostnameRewrite'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-hostname""", alias="Hostname")
    Prefix_: Optional['HttpGatewayRoutePrefixRewrite'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpGatewayRouteRewrite:
        from troposphere.appmesh import HttpGatewayRouteRewrite as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpPathMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html
    Properties:
        - Name: Regex
        - Name: Exact
    
    """
    
    Regex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html#cfn-appmesh-gatewayroute-httppathmatch-regex""", alias="Regex")
    Exact_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html#cfn-appmesh-gatewayroute-httppathmatch-exact""", alias="Exact")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpPathMatch:
        from troposphere.appmesh import HttpPathMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpQueryParameterMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpqueryparametermatch.html
    Properties:
        - Name: Exact
    
    """
    
    Exact_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpqueryparametermatch.html#cfn-appmesh-gatewayroute-httpqueryparametermatch-exact""", alias="Exact")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpQueryParameterMatch:
        from troposphere.appmesh import HttpQueryParameterMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QueryParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html
    Properties:
        - Name: Name
        - Name: Match
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html#cfn-appmesh-gatewayroute-queryparameter-name""", alias="Name")
    Match_: Optional['HttpQueryParameterMatch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html#cfn-appmesh-gatewayroute-queryparameter-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.QueryParameter:
        from troposphere.appmesh import QueryParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EgressFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-egressfilter.html
    Properties:
        - Name: Type
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-egressfilter.html#cfn-appmesh-mesh-egressfilter-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.EgressFilter:
        from troposphere.appmesh import EgressFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MeshServiceDiscovery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshservicediscovery.html
    Properties:
        - Name: IpPreference
    
    """
    
    IpPreference_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshservicediscovery.html#cfn-appmesh-mesh-meshservicediscovery-ippreference""", alias="IpPreference")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.MeshServiceDiscovery:
        from troposphere.appmesh import MeshServiceDiscovery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MeshSpec(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html
    Properties:
        - Name: EgressFilter
        - Name: ServiceDiscovery
    
    """
    
    EgressFilter_: Optional['EgressFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html#cfn-appmesh-mesh-meshspec-egressfilter""", alias="EgressFilter")
    ServiceDiscovery_: Optional['MeshServiceDiscovery'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html#cfn-appmesh-mesh-meshspec-servicediscovery""", alias="ServiceDiscovery")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.MeshSpec:
        from troposphere.appmesh import MeshSpec as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Duration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html
    Properties:
        - Name: Value
        - Name: Unit
    
    """
    
    Value_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html#cfn-appmesh-route-duration-value""", alias="Value")
    Unit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html#cfn-appmesh-route-duration-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.Duration:
        from troposphere.appmesh import Duration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrpcRetryPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html
    Properties:
        - Name: MaxRetries
        - Name: PerRetryTimeout
        - Name: GrpcRetryEvents
        - Name: HttpRetryEvents
        - Name: TcpRetryEvents
    
    """
    
    MaxRetries_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-maxretries""", alias="MaxRetries")
    PerRetryTimeout_: 'Duration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-perretrytimeout""", alias="PerRetryTimeout")
    GrpcRetryEvents_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-grpcretryevents""", alias="GrpcRetryEvents")
    HttpRetryEvents_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-httpretryevents""", alias="HttpRetryEvents")
    TcpRetryEvents_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-tcpretryevents""", alias="TcpRetryEvents")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GrpcRetryPolicy:
        from troposphere.appmesh import GrpcRetryPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrpcRoute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html
    Properties:
        - Name: Action
        - Name: Timeout
        - Name: RetryPolicy
        - Name: Match
    
    """
    
    Action_: 'GrpcRouteAction' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-action""", alias="Action")
    Timeout_: Optional['GrpcTimeout'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-timeout""", alias="Timeout")
    RetryPolicy_: Optional['GrpcRetryPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-retrypolicy""", alias="RetryPolicy")
    Match_: 'GrpcRouteMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GrpcRoute:
        from troposphere.appmesh import GrpcRoute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrpcRouteAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcrouteaction.html
    Properties:
        - Name: WeightedTargets
    
    """
    
    WeightedTargets_: List['WeightedTarget'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcrouteaction.html#cfn-appmesh-route-grpcrouteaction-weightedtargets""", alias="WeightedTargets")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GrpcRouteAction:
        from troposphere.appmesh import GrpcRouteAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrpcRouteMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html
    Properties:
        - Name: ServiceName
        - Name: Port
        - Name: Metadata
        - Name: MethodName
    
    """
    
    ServiceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-servicename""", alias="ServiceName")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-port""", alias="Port")
    Metadata_: Optional[List['GrpcRouteMetadata']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-metadata""", alias="Metadata")
    MethodName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-methodname""", alias="MethodName")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GrpcRouteMatch:
        from troposphere.appmesh import GrpcRouteMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrpcRouteMetadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html
    Properties:
        - Name: Invert
        - Name: Name
        - Name: Match
    
    """
    
    Invert_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html#cfn-appmesh-route-grpcroutemetadata-invert""", alias="Invert")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html#cfn-appmesh-route-grpcroutemetadata-name""", alias="Name")
    Match_: Optional['GrpcRouteMetadataMatchMethod'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html#cfn-appmesh-route-grpcroutemetadata-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GrpcRouteMetadata:
        from troposphere.appmesh import GrpcRouteMetadata as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrpcRouteMetadataMatchMethod(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html
    Properties:
        - Name: Suffix
        - Name: Regex
        - Name: Exact
        - Name: Prefix
        - Name: Range
    
    """
    
    Suffix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-suffix""", alias="Suffix")
    Regex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-regex""", alias="Regex")
    Exact_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-exact""", alias="Exact")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-prefix""", alias="Prefix")
    Range_: Optional['MatchRange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-range""", alias="Range")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GrpcRouteMetadataMatchMethod:
        from troposphere.appmesh import GrpcRouteMetadataMatchMethod as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrpcTimeout(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html
    Properties:
        - Name: PerRequest
        - Name: Idle
    
    """
    
    PerRequest_: Optional['Duration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html#cfn-appmesh-route-grpctimeout-perrequest""", alias="PerRequest")
    Idle_: Optional['Duration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html#cfn-appmesh-route-grpctimeout-idle""", alias="Idle")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GrpcTimeout:
        from troposphere.appmesh import GrpcTimeout as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HeaderMatchMethod(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html
    Properties:
        - Name: Suffix
        - Name: Regex
        - Name: Exact
        - Name: Prefix
        - Name: Range
    
    """
    
    Suffix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-suffix""", alias="Suffix")
    Regex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-regex""", alias="Regex")
    Exact_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-exact""", alias="Exact")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-prefix""", alias="Prefix")
    Range_: Optional['MatchRange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-range""", alias="Range")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HeaderMatchMethod:
        from troposphere.appmesh import HeaderMatchMethod as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpPathMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html
    Properties:
        - Name: Regex
        - Name: Exact
    
    """
    
    Regex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html#cfn-appmesh-route-httppathmatch-regex""", alias="Regex")
    Exact_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html#cfn-appmesh-route-httppathmatch-exact""", alias="Exact")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpPathMatch:
        from troposphere.appmesh import HttpPathMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpQueryParameterMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpqueryparametermatch.html
    Properties:
        - Name: Exact
    
    """
    
    Exact_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpqueryparametermatch.html#cfn-appmesh-route-httpqueryparametermatch-exact""", alias="Exact")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpQueryParameterMatch:
        from troposphere.appmesh import HttpQueryParameterMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpRetryPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html
    Properties:
        - Name: MaxRetries
        - Name: PerRetryTimeout
        - Name: HttpRetryEvents
        - Name: TcpRetryEvents
    
    """
    
    MaxRetries_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-maxretries""", alias="MaxRetries")
    PerRetryTimeout_: 'Duration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-perretrytimeout""", alias="PerRetryTimeout")
    HttpRetryEvents_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-httpretryevents""", alias="HttpRetryEvents")
    TcpRetryEvents_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-tcpretryevents""", alias="TcpRetryEvents")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpRetryPolicy:
        from troposphere.appmesh import HttpRetryPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpRoute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html
    Properties:
        - Name: Action
        - Name: Timeout
        - Name: RetryPolicy
        - Name: Match
    
    """
    
    Action_: 'HttpRouteAction' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-action""", alias="Action")
    Timeout_: Optional['HttpTimeout'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-timeout""", alias="Timeout")
    RetryPolicy_: Optional['HttpRetryPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-retrypolicy""", alias="RetryPolicy")
    Match_: 'HttpRouteMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpRoute:
        from troposphere.appmesh import HttpRoute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpRouteAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteaction.html
    Properties:
        - Name: WeightedTargets
    
    """
    
    WeightedTargets_: List['WeightedTarget'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteaction.html#cfn-appmesh-route-httprouteaction-weightedtargets""", alias="WeightedTargets")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpRouteAction:
        from troposphere.appmesh import HttpRouteAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpRouteHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html
    Properties:
        - Name: Invert
        - Name: Name
        - Name: Match
    
    """
    
    Invert_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html#cfn-appmesh-route-httprouteheader-invert""", alias="Invert")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html#cfn-appmesh-route-httprouteheader-name""", alias="Name")
    Match_: Optional['HeaderMatchMethod'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html#cfn-appmesh-route-httprouteheader-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpRouteHeader:
        from troposphere.appmesh import HttpRouteHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpRouteMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html
    Properties:
        - Name: Path
        - Name: Scheme
        - Name: Headers
        - Name: Port
        - Name: Prefix
        - Name: Method
        - Name: QueryParameters
    
    """
    
    Path_: Optional['HttpPathMatch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-path""", alias="Path")
    Scheme_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-scheme""", alias="Scheme")
    Headers_: Optional[List['HttpRouteHeader']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-headers""", alias="Headers")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-port""", alias="Port")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-prefix""", alias="Prefix")
    Method_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-method""", alias="Method")
    QueryParameters_: Optional[List['QueryParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-queryparameters""", alias="QueryParameters")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpRouteMatch:
        from troposphere.appmesh import HttpRouteMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpTimeout(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html
    Properties:
        - Name: PerRequest
        - Name: Idle
    
    """
    
    PerRequest_: Optional['Duration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html#cfn-appmesh-route-httptimeout-perrequest""", alias="PerRequest")
    Idle_: Optional['Duration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html#cfn-appmesh-route-httptimeout-idle""", alias="Idle")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpTimeout:
        from troposphere.appmesh import HttpTimeout as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MatchRange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html
    Properties:
        - Name: Start
        - Name: End
    
    """
    
    Start_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html#cfn-appmesh-route-matchrange-start""", alias="Start")
    End_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html#cfn-appmesh-route-matchrange-end""", alias="End")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.MatchRange:
        from troposphere.appmesh import MatchRange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QueryParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html
    Properties:
        - Name: Name
        - Name: Match
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html#cfn-appmesh-route-queryparameter-name""", alias="Name")
    Match_: Optional['HttpQueryParameterMatch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html#cfn-appmesh-route-queryparameter-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.QueryParameter:
        from troposphere.appmesh import QueryParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RouteSpec(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html
    Properties:
        - Name: HttpRoute
        - Name: Priority
        - Name: Http2Route
        - Name: GrpcRoute
        - Name: TcpRoute
    
    """
    
    HttpRoute_: Optional['HttpRoute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-httproute""", alias="HttpRoute")
    Priority_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-priority""", alias="Priority")
    Http2Route_: Optional['HttpRoute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-http2route""", alias="Http2Route")
    GrpcRoute_: Optional['GrpcRoute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-grpcroute""", alias="GrpcRoute")
    TcpRoute_: Optional['TcpRoute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-tcproute""", alias="TcpRoute")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.RouteSpec:
        from troposphere.appmesh import RouteSpec as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TcpRoute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html
    Properties:
        - Name: Action
        - Name: Timeout
        - Name: Match
    
    """
    
    Action_: 'TcpRouteAction' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html#cfn-appmesh-route-tcproute-action""", alias="Action")
    Timeout_: Optional['TcpTimeout'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html#cfn-appmesh-route-tcproute-timeout""", alias="Timeout")
    Match_: Optional['TcpRouteMatch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html#cfn-appmesh-route-tcproute-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.TcpRoute:
        from troposphere.appmesh import TcpRoute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TcpRouteAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcprouteaction.html
    Properties:
        - Name: WeightedTargets
    
    """
    
    WeightedTargets_: List['WeightedTarget'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcprouteaction.html#cfn-appmesh-route-tcprouteaction-weightedtargets""", alias="WeightedTargets")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.TcpRouteAction:
        from troposphere.appmesh import TcpRouteAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TcpRouteMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproutematch.html
    Properties:
        - Name: Port
    
    """
    
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproutematch.html#cfn-appmesh-route-tcproutematch-port""", alias="Port")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.TcpRouteMatch:
        from troposphere.appmesh import TcpRouteMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TcpTimeout(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcptimeout.html
    Properties:
        - Name: Idle
    
    """
    
    Idle_: Optional['Duration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcptimeout.html#cfn-appmesh-route-tcptimeout-idle""", alias="Idle")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.TcpTimeout:
        from troposphere.appmesh import TcpTimeout as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WeightedTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html
    Properties:
        - Name: VirtualNode
        - Name: Port
        - Name: Weight
    
    """
    
    VirtualNode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html#cfn-appmesh-route-weightedtarget-virtualnode""", alias="VirtualNode")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html#cfn-appmesh-route-weightedtarget-port""", alias="Port")
    Weight_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html#cfn-appmesh-route-weightedtarget-weight""", alias="Weight")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.WeightedTarget:
        from troposphere.appmesh import WeightedTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JsonFormatRef(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-jsonformatref.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-jsonformatref.html#cfn-appmesh-virtualgateway-jsonformatref-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-jsonformatref.html#cfn-appmesh-virtualgateway-jsonformatref-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.JsonFormatRef:
        from troposphere.appmesh import JsonFormatRef as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggingFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-loggingformat.html
    Properties:
        - Name: Text
        - Name: Json
    
    """
    
    Text_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-loggingformat.html#cfn-appmesh-virtualgateway-loggingformat-text""", alias="Text")
    Json_: Optional[List['JsonFormatRef']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-loggingformat.html#cfn-appmesh-virtualgateway-loggingformat-json""", alias="Json")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.LoggingFormat:
        from troposphere.appmesh import LoggingFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SubjectAlternativeNameMatchers(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenamematchers.html
    Properties:
        - Name: Exact
    
    """
    
    Exact_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenamematchers.html#cfn-appmesh-virtualgateway-subjectalternativenamematchers-exact""", alias="Exact")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.SubjectAlternativeNameMatchers:
        from troposphere.appmesh import SubjectAlternativeNameMatchers as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SubjectAlternativeNames(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenames.html
    Properties:
        - Name: Match
    
    """
    
    Match_: 'SubjectAlternativeNameMatchers' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenames.html#cfn-appmesh-virtualgateway-subjectalternativenames-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.SubjectAlternativeNames:
        from troposphere.appmesh import SubjectAlternativeNames as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayAccessLog(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.html
    Properties:
        - Name: File
    
    """
    
    File_: Optional['VirtualGatewayFileAccessLog'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.html#cfn-appmesh-virtualgateway-virtualgatewayaccesslog-file""", alias="File")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayAccessLog:
        from troposphere.appmesh import VirtualGatewayAccessLog as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayBackendDefaults(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.html
    Properties:
        - Name: ClientPolicy
    
    """
    
    ClientPolicy_: Optional['VirtualGatewayClientPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.html#cfn-appmesh-virtualgateway-virtualgatewaybackenddefaults-clientpolicy""", alias="ClientPolicy")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayBackendDefaults:
        from troposphere.appmesh import VirtualGatewayBackendDefaults as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayClientPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicy.html
    Properties:
        - Name: TLS
    
    """
    
    TLS_: Optional['VirtualGatewayClientPolicyTls'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicy-tls""", alias="TLS")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayClientPolicy:
        from troposphere.appmesh import VirtualGatewayClientPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayClientPolicyTls(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html
    Properties:
        - Name: Validation
        - Name: Enforce
        - Name: Ports
        - Name: Certificate
    
    """
    
    Validation_: 'VirtualGatewayTlsValidationContext' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-validation""", alias="Validation")
    Enforce_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-enforce""", alias="Enforce")
    Ports_: Optional[List[int]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-ports""", alias="Ports")
    Certificate_: Optional['VirtualGatewayClientTlsCertificate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-certificate""", alias="Certificate")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayClientPolicyTls:
        from troposphere.appmesh import VirtualGatewayClientPolicyTls as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayClientTlsCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html
    Properties:
        - Name: SDS
        - Name: File
    
    """
    
    SDS_: Optional['VirtualGatewayListenerTlsSdsCertificate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-sds""", alias="SDS")
    File_: Optional['VirtualGatewayListenerTlsFileCertificate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-file""", alias="File")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayClientTlsCertificate:
        from troposphere.appmesh import VirtualGatewayClientTlsCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayConnectionPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html
    Properties:
        - Name: HTTP2
        - Name: HTTP
        - Name: GRPC
    
    """
    
    HTTP2_: Optional['VirtualGatewayHttp2ConnectionPool'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-http2""", alias="HTTP2")
    HTTP_: Optional['VirtualGatewayHttpConnectionPool'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-http""", alias="HTTP")
    GRPC_: Optional['VirtualGatewayGrpcConnectionPool'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-grpc""", alias="GRPC")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayConnectionPool:
        from troposphere.appmesh import VirtualGatewayConnectionPool as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayFileAccessLog(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayfileaccesslog.html
    Properties:
        - Name: Path
        - Name: Format
    
    """
    
    Path_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayfileaccesslog.html#cfn-appmesh-virtualgateway-virtualgatewayfileaccesslog-path""", alias="Path")
    Format_: Optional['LoggingFormat'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayfileaccesslog.html#cfn-appmesh-virtualgateway-virtualgatewayfileaccesslog-format""", alias="Format")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayFileAccessLog:
        from troposphere.appmesh import VirtualGatewayFileAccessLog as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayGrpcConnectionPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaygrpcconnectionpool.html
    Properties:
        - Name: MaxRequests
    
    """
    
    MaxRequests_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaygrpcconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewaygrpcconnectionpool-maxrequests""", alias="MaxRequests")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayGrpcConnectionPool:
        from troposphere.appmesh import VirtualGatewayGrpcConnectionPool as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayHealthCheckPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html
    Properties:
        - Name: Path
        - Name: UnhealthyThreshold
        - Name: Port
        - Name: HealthyThreshold
        - Name: TimeoutMillis
        - Name: Protocol
        - Name: IntervalMillis
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-path""", alias="Path")
    UnhealthyThreshold_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-unhealthythreshold""", alias="UnhealthyThreshold")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-port""", alias="Port")
    HealthyThreshold_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-healthythreshold""", alias="HealthyThreshold")
    TimeoutMillis_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-timeoutmillis""", alias="TimeoutMillis")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-protocol""", alias="Protocol")
    IntervalMillis_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-intervalmillis""", alias="IntervalMillis")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayHealthCheckPolicy:
        from troposphere.appmesh import VirtualGatewayHealthCheckPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayHttp2ConnectionPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttp2connectionpool.html
    Properties:
        - Name: MaxRequests
    
    """
    
    MaxRequests_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttp2connectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayhttp2connectionpool-maxrequests""", alias="MaxRequests")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayHttp2ConnectionPool:
        from troposphere.appmesh import VirtualGatewayHttp2ConnectionPool as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayHttpConnectionPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html
    Properties:
        - Name: MaxConnections
        - Name: MaxPendingRequests
    
    """
    
    MaxConnections_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxconnections""", alias="MaxConnections")
    MaxPendingRequests_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxpendingrequests""", alias="MaxPendingRequests")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayHttpConnectionPool:
        from troposphere.appmesh import VirtualGatewayHttpConnectionPool as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayListener(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html
    Properties:
        - Name: ConnectionPool
        - Name: HealthCheck
        - Name: TLS
        - Name: PortMapping
    
    """
    
    ConnectionPool_: Optional['VirtualGatewayConnectionPool'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-connectionpool""", alias="ConnectionPool")
    HealthCheck_: Optional['VirtualGatewayHealthCheckPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-healthcheck""", alias="HealthCheck")
    TLS_: Optional['VirtualGatewayListenerTls'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-tls""", alias="TLS")
    PortMapping_: 'VirtualGatewayPortMapping' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-portmapping""", alias="PortMapping")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayListener:
        from troposphere.appmesh import VirtualGatewayListener as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayListenerTls(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html
    Properties:
        - Name: Validation
        - Name: Mode
        - Name: Certificate
    
    """
    
    Validation_: Optional['VirtualGatewayListenerTlsValidationContext'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-validation""", alias="Validation")
    Mode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-mode""", alias="Mode")
    Certificate_: 'VirtualGatewayListenerTlsCertificate' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-certificate""", alias="Certificate")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayListenerTls:
        from troposphere.appmesh import VirtualGatewayListenerTls as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayListenerTlsAcmCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate.html
    Properties:
        - Name: CertificateArn
    
    """
    
    CertificateArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate-certificatearn""", alias="CertificateArn")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayListenerTlsAcmCertificate:
        from troposphere.appmesh import VirtualGatewayListenerTlsAcmCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayListenerTlsCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html
    Properties:
        - Name: SDS
        - Name: ACM
        - Name: File
    
    """
    
    SDS_: Optional['VirtualGatewayListenerTlsSdsCertificate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-sds""", alias="SDS")
    ACM_: Optional['VirtualGatewayListenerTlsAcmCertificate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-acm""", alias="ACM")
    File_: Optional['VirtualGatewayListenerTlsFileCertificate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-file""", alias="File")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayListenerTlsCertificate:
        from troposphere.appmesh import VirtualGatewayListenerTlsCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayListenerTlsFileCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html
    Properties:
        - Name: PrivateKey
        - Name: CertificateChain
    
    """
    
    PrivateKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-privatekey""", alias="PrivateKey")
    CertificateChain_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-certificatechain""", alias="CertificateChain")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayListenerTlsFileCertificate:
        from troposphere.appmesh import VirtualGatewayListenerTlsFileCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayListenerTlsSdsCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate.html
    Properties:
        - Name: SecretName
    
    """
    
    SecretName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate-secretname""", alias="SecretName")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayListenerTlsSdsCertificate:
        from troposphere.appmesh import VirtualGatewayListenerTlsSdsCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayListenerTlsValidationContext(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html
    Properties:
        - Name: SubjectAlternativeNames
        - Name: Trust
    
    """
    
    SubjectAlternativeNames_: Optional['SubjectAlternativeNames'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-subjectalternativenames""", alias="SubjectAlternativeNames")
    Trust_: 'VirtualGatewayListenerTlsValidationContextTrust' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-trust""", alias="Trust")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayListenerTlsValidationContext:
        from troposphere.appmesh import VirtualGatewayListenerTlsValidationContext as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayListenerTlsValidationContextTrust(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html
    Properties:
        - Name: SDS
        - Name: File
    
    """
    
    SDS_: Optional['VirtualGatewayTlsValidationContextSdsTrust'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust-sds""", alias="SDS")
    File_: Optional['VirtualGatewayTlsValidationContextFileTrust'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust-file""", alias="File")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayListenerTlsValidationContextTrust:
        from troposphere.appmesh import VirtualGatewayListenerTlsValidationContextTrust as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayLogging(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylogging.html
    Properties:
        - Name: AccessLog
    
    """
    
    AccessLog_: Optional['VirtualGatewayAccessLog'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylogging.html#cfn-appmesh-virtualgateway-virtualgatewaylogging-accesslog""", alias="AccessLog")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayLogging:
        from troposphere.appmesh import VirtualGatewayLogging as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayPortMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html
    Properties:
        - Name: Port
        - Name: Protocol
    
    """
    
    Port_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html#cfn-appmesh-virtualgateway-virtualgatewayportmapping-port""", alias="Port")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html#cfn-appmesh-virtualgateway-virtualgatewayportmapping-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayPortMapping:
        from troposphere.appmesh import VirtualGatewayPortMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewaySpec(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html
    Properties:
        - Name: Logging
        - Name: Listeners
        - Name: BackendDefaults
    
    """
    
    Logging_: Optional['VirtualGatewayLogging'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-logging""", alias="Logging")
    Listeners_: List['VirtualGatewayListener'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-listeners""", alias="Listeners")
    BackendDefaults_: Optional['VirtualGatewayBackendDefaults'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-backenddefaults""", alias="BackendDefaults")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewaySpec:
        from troposphere.appmesh import VirtualGatewaySpec as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayTlsValidationContext(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html
    Properties:
        - Name: SubjectAlternativeNames
        - Name: Trust
    
    """
    
    SubjectAlternativeNames_: Optional['SubjectAlternativeNames'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-subjectalternativenames""", alias="SubjectAlternativeNames")
    Trust_: 'VirtualGatewayTlsValidationContextTrust' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-trust""", alias="Trust")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayTlsValidationContext:
        from troposphere.appmesh import VirtualGatewayTlsValidationContext as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayTlsValidationContextAcmTrust(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust.html
    Properties:
        - Name: CertificateAuthorityArns
    
    """
    
    CertificateAuthorityArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust-certificateauthorityarns""", alias="CertificateAuthorityArns")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayTlsValidationContextAcmTrust:
        from troposphere.appmesh import VirtualGatewayTlsValidationContextAcmTrust as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayTlsValidationContextFileTrust(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust.html
    Properties:
        - Name: CertificateChain
    
    """
    
    CertificateChain_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust-certificatechain""", alias="CertificateChain")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayTlsValidationContextFileTrust:
        from troposphere.appmesh import VirtualGatewayTlsValidationContextFileTrust as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayTlsValidationContextSdsTrust(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust.html
    Properties:
        - Name: SecretName
    
    """
    
    SecretName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust-secretname""", alias="SecretName")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayTlsValidationContextSdsTrust:
        from troposphere.appmesh import VirtualGatewayTlsValidationContextSdsTrust as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualGatewayTlsValidationContextTrust(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html
    Properties:
        - Name: SDS
        - Name: ACM
        - Name: File
    
    """
    
    SDS_: Optional['VirtualGatewayTlsValidationContextSdsTrust'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-sds""", alias="SDS")
    ACM_: Optional['VirtualGatewayTlsValidationContextAcmTrust'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-acm""", alias="ACM")
    File_: Optional['VirtualGatewayTlsValidationContextFileTrust'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-file""", alias="File")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGatewayTlsValidationContextTrust:
        from troposphere.appmesh import VirtualGatewayTlsValidationContextTrust as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessLog(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-accesslog.html
    Properties:
        - Name: File
    
    """
    
    File_: Optional['FileAccessLog'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-accesslog.html#cfn-appmesh-virtualnode-accesslog-file""", alias="File")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.AccessLog:
        from troposphere.appmesh import AccessLog as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AwsCloudMapInstanceAttribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html#cfn-appmesh-virtualnode-awscloudmapinstanceattribute-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html#cfn-appmesh-virtualnode-awscloudmapinstanceattribute-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.AwsCloudMapInstanceAttribute:
        from troposphere.appmesh import AwsCloudMapInstanceAttribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AwsCloudMapServiceDiscovery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html
    Properties:
        - Name: NamespaceName
        - Name: ServiceName
        - Name: IpPreference
        - Name: Attributes
    
    """
    
    NamespaceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-namespacename""", alias="NamespaceName")
    ServiceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-servicename""", alias="ServiceName")
    IpPreference_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-ippreference""", alias="IpPreference")
    Attributes_: Optional[List['AwsCloudMapInstanceAttribute']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-attributes""", alias="Attributes")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.AwsCloudMapServiceDiscovery:
        from troposphere.appmesh import AwsCloudMapServiceDiscovery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Backend(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backend.html
    Properties:
        - Name: VirtualService
    
    """
    
    VirtualService_: Optional['VirtualServiceBackend'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backend.html#cfn-appmesh-virtualnode-backend-virtualservice""", alias="VirtualService")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.Backend:
        from troposphere.appmesh import Backend as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BackendDefaults(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backenddefaults.html
    Properties:
        - Name: ClientPolicy
    
    """
    
    ClientPolicy_: Optional['ClientPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backenddefaults.html#cfn-appmesh-virtualnode-backenddefaults-clientpolicy""", alias="ClientPolicy")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.BackendDefaults:
        from troposphere.appmesh import BackendDefaults as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClientPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicy.html
    Properties:
        - Name: TLS
    
    """
    
    TLS_: Optional['ClientPolicyTls'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicy.html#cfn-appmesh-virtualnode-clientpolicy-tls""", alias="TLS")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.ClientPolicy:
        from troposphere.appmesh import ClientPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClientPolicyTls(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html
    Properties:
        - Name: Validation
        - Name: Enforce
        - Name: Ports
        - Name: Certificate
    
    """
    
    Validation_: 'TlsValidationContext' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-validation""", alias="Validation")
    Enforce_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-enforce""", alias="Enforce")
    Ports_: Optional[List[int]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-ports""", alias="Ports")
    Certificate_: Optional['ClientTlsCertificate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-certificate""", alias="Certificate")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.ClientPolicyTls:
        from troposphere.appmesh import ClientPolicyTls as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClientTlsCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html
    Properties:
        - Name: SDS
        - Name: File
    
    """
    
    SDS_: Optional['ListenerTlsSdsCertificate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html#cfn-appmesh-virtualnode-clienttlscertificate-sds""", alias="SDS")
    File_: Optional['ListenerTlsFileCertificate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html#cfn-appmesh-virtualnode-clienttlscertificate-file""", alias="File")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.ClientTlsCertificate:
        from troposphere.appmesh import ClientTlsCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DnsServiceDiscovery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html
    Properties:
        - Name: IpPreference
        - Name: Hostname
        - Name: ResponseType
    
    """
    
    IpPreference_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html#cfn-appmesh-virtualnode-dnsservicediscovery-ippreference""", alias="IpPreference")
    Hostname_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html#cfn-appmesh-virtualnode-dnsservicediscovery-hostname""", alias="Hostname")
    ResponseType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html#cfn-appmesh-virtualnode-dnsservicediscovery-responsetype""", alias="ResponseType")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.DnsServiceDiscovery:
        from troposphere.appmesh import DnsServiceDiscovery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Duration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html
    Properties:
        - Name: Value
        - Name: Unit
    
    """
    
    Value_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html#cfn-appmesh-virtualnode-duration-value""", alias="Value")
    Unit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html#cfn-appmesh-virtualnode-duration-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.Duration:
        from troposphere.appmesh import Duration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FileAccessLog(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-fileaccesslog.html
    Properties:
        - Name: Path
        - Name: Format
    
    """
    
    Path_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-fileaccesslog.html#cfn-appmesh-virtualnode-fileaccesslog-path""", alias="Path")
    Format_: Optional['LoggingFormat'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-fileaccesslog.html#cfn-appmesh-virtualnode-fileaccesslog-format""", alias="Format")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.FileAccessLog:
        from troposphere.appmesh import FileAccessLog as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrpcTimeout(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html
    Properties:
        - Name: PerRequest
        - Name: Idle
    
    """
    
    PerRequest_: Optional['Duration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html#cfn-appmesh-virtualnode-grpctimeout-perrequest""", alias="PerRequest")
    Idle_: Optional['Duration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html#cfn-appmesh-virtualnode-grpctimeout-idle""", alias="Idle")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.GrpcTimeout:
        from troposphere.appmesh import GrpcTimeout as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HealthCheck(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html
    Properties:
        - Name: Path
        - Name: UnhealthyThreshold
        - Name: Port
        - Name: HealthyThreshold
        - Name: TimeoutMillis
        - Name: Protocol
        - Name: IntervalMillis
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-path""", alias="Path")
    UnhealthyThreshold_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-unhealthythreshold""", alias="UnhealthyThreshold")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-port""", alias="Port")
    HealthyThreshold_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-healthythreshold""", alias="HealthyThreshold")
    TimeoutMillis_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-timeoutmillis""", alias="TimeoutMillis")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-protocol""", alias="Protocol")
    IntervalMillis_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-intervalmillis""", alias="IntervalMillis")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HealthCheck:
        from troposphere.appmesh import HealthCheck as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HttpTimeout(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html
    Properties:
        - Name: PerRequest
        - Name: Idle
    
    """
    
    PerRequest_: Optional['Duration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html#cfn-appmesh-virtualnode-httptimeout-perrequest""", alias="PerRequest")
    Idle_: Optional['Duration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html#cfn-appmesh-virtualnode-httptimeout-idle""", alias="Idle")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.HttpTimeout:
        from troposphere.appmesh import HttpTimeout as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JsonFormatRef(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-jsonformatref.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-jsonformatref.html#cfn-appmesh-virtualnode-jsonformatref-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-jsonformatref.html#cfn-appmesh-virtualnode-jsonformatref-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.JsonFormatRef:
        from troposphere.appmesh import JsonFormatRef as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Listener(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html
    Properties:
        - Name: ConnectionPool
        - Name: Timeout
        - Name: HealthCheck
        - Name: TLS
        - Name: PortMapping
        - Name: OutlierDetection
    
    """
    
    ConnectionPool_: Optional['VirtualNodeConnectionPool'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-connectionpool""", alias="ConnectionPool")
    Timeout_: Optional['ListenerTimeout'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-timeout""", alias="Timeout")
    HealthCheck_: Optional['HealthCheck'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-healthcheck""", alias="HealthCheck")
    TLS_: Optional['ListenerTls'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-tls""", alias="TLS")
    PortMapping_: 'PortMapping' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-portmapping""", alias="PortMapping")
    OutlierDetection_: Optional['OutlierDetection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-outlierdetection""", alias="OutlierDetection")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.Listener:
        from troposphere.appmesh import Listener as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ListenerTimeout(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html
    Properties:
        - Name: TCP
        - Name: HTTP2
        - Name: HTTP
        - Name: GRPC
    
    """
    
    TCP_: Optional['TcpTimeout'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-tcp""", alias="TCP")
    HTTP2_: Optional['HttpTimeout'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-http2""", alias="HTTP2")
    HTTP_: Optional['HttpTimeout'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-http""", alias="HTTP")
    GRPC_: Optional['GrpcTimeout'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-grpc""", alias="GRPC")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.ListenerTimeout:
        from troposphere.appmesh import ListenerTimeout as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ListenerTls(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html
    Properties:
        - Name: Validation
        - Name: Mode
        - Name: Certificate
    
    """
    
    Validation_: Optional['ListenerTlsValidationContext'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-validation""", alias="Validation")
    Mode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-mode""", alias="Mode")
    Certificate_: 'ListenerTlsCertificate' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-certificate""", alias="Certificate")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.ListenerTls:
        from troposphere.appmesh import ListenerTls as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ListenerTlsAcmCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsacmcertificate.html
    Properties:
        - Name: CertificateArn
    
    """
    
    CertificateArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsacmcertificate.html#cfn-appmesh-virtualnode-listenertlsacmcertificate-certificatearn""", alias="CertificateArn")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.ListenerTlsAcmCertificate:
        from troposphere.appmesh import ListenerTlsAcmCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ListenerTlsCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html
    Properties:
        - Name: SDS
        - Name: ACM
        - Name: File
    
    """
    
    SDS_: Optional['ListenerTlsSdsCertificate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-sds""", alias="SDS")
    ACM_: Optional['ListenerTlsAcmCertificate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-acm""", alias="ACM")
    File_: Optional['ListenerTlsFileCertificate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-file""", alias="File")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.ListenerTlsCertificate:
        from troposphere.appmesh import ListenerTlsCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ListenerTlsFileCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsfilecertificate.html
    Properties:
        - Name: PrivateKey
        - Name: CertificateChain
    
    """
    
    PrivateKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsfilecertificate.html#cfn-appmesh-virtualnode-listenertlsfilecertificate-privatekey""", alias="PrivateKey")
    CertificateChain_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsfilecertificate.html#cfn-appmesh-virtualnode-listenertlsfilecertificate-certificatechain""", alias="CertificateChain")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.ListenerTlsFileCertificate:
        from troposphere.appmesh import ListenerTlsFileCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ListenerTlsSdsCertificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlssdscertificate.html
    Properties:
        - Name: SecretName
    
    """
    
    SecretName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlssdscertificate.html#cfn-appmesh-virtualnode-listenertlssdscertificate-secretname""", alias="SecretName")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.ListenerTlsSdsCertificate:
        from troposphere.appmesh import ListenerTlsSdsCertificate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ListenerTlsValidationContext(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html
    Properties:
        - Name: SubjectAlternativeNames
        - Name: Trust
    
    """
    
    SubjectAlternativeNames_: Optional['SubjectAlternativeNames'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html#cfn-appmesh-virtualnode-listenertlsvalidationcontext-subjectalternativenames""", alias="SubjectAlternativeNames")
    Trust_: 'ListenerTlsValidationContextTrust' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html#cfn-appmesh-virtualnode-listenertlsvalidationcontext-trust""", alias="Trust")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.ListenerTlsValidationContext:
        from troposphere.appmesh import ListenerTlsValidationContext as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ListenerTlsValidationContextTrust(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html
    Properties:
        - Name: SDS
        - Name: File
    
    """
    
    SDS_: Optional['TlsValidationContextSdsTrust'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-sds""", alias="SDS")
    File_: Optional['TlsValidationContextFileTrust'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-file""", alias="File")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.ListenerTlsValidationContextTrust:
        from troposphere.appmesh import ListenerTlsValidationContextTrust as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Logging(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-logging.html
    Properties:
        - Name: AccessLog
    
    """
    
    AccessLog_: Optional['AccessLog'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-logging.html#cfn-appmesh-virtualnode-logging-accesslog""", alias="AccessLog")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.Logging:
        from troposphere.appmesh import Logging as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggingFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-loggingformat.html
    Properties:
        - Name: Text
        - Name: Json
    
    """
    
    Text_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-loggingformat.html#cfn-appmesh-virtualnode-loggingformat-text""", alias="Text")
    Json_: Optional[List['JsonFormatRef']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-loggingformat.html#cfn-appmesh-virtualnode-loggingformat-json""", alias="Json")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.LoggingFormat:
        from troposphere.appmesh import LoggingFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutlierDetection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html
    Properties:
        - Name: MaxEjectionPercent
        - Name: BaseEjectionDuration
        - Name: MaxServerErrors
        - Name: Interval
    
    """
    
    MaxEjectionPercent_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-maxejectionpercent""", alias="MaxEjectionPercent")
    BaseEjectionDuration_: 'Duration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-baseejectionduration""", alias="BaseEjectionDuration")
    MaxServerErrors_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-maxservererrors""", alias="MaxServerErrors")
    Interval_: 'Duration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-interval""", alias="Interval")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.OutlierDetection:
        from troposphere.appmesh import OutlierDetection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PortMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html
    Properties:
        - Name: Port
        - Name: Protocol
    
    """
    
    Port_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html#cfn-appmesh-virtualnode-portmapping-port""", alias="Port")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html#cfn-appmesh-virtualnode-portmapping-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.PortMapping:
        from troposphere.appmesh import PortMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceDiscovery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html
    Properties:
        - Name: DNS
        - Name: AWSCloudMap
    
    """
    
    DNS_: Optional['DnsServiceDiscovery'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html#cfn-appmesh-virtualnode-servicediscovery-dns""", alias="DNS")
    AWSCloudMap_: Optional['AwsCloudMapServiceDiscovery'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html#cfn-appmesh-virtualnode-servicediscovery-awscloudmap""", alias="AWSCloudMap")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.ServiceDiscovery:
        from troposphere.appmesh import ServiceDiscovery as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SubjectAlternativeNameMatchers(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenamematchers.html
    Properties:
        - Name: Exact
    
    """
    
    Exact_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenamematchers.html#cfn-appmesh-virtualnode-subjectalternativenamematchers-exact""", alias="Exact")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.SubjectAlternativeNameMatchers:
        from troposphere.appmesh import SubjectAlternativeNameMatchers as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SubjectAlternativeNames(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenames.html
    Properties:
        - Name: Match
    
    """
    
    Match_: 'SubjectAlternativeNameMatchers' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenames.html#cfn-appmesh-virtualnode-subjectalternativenames-match""", alias="Match")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.SubjectAlternativeNames:
        from troposphere.appmesh import SubjectAlternativeNames as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TcpTimeout(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tcptimeout.html
    Properties:
        - Name: Idle
    
    """
    
    Idle_: Optional['Duration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tcptimeout.html#cfn-appmesh-virtualnode-tcptimeout-idle""", alias="Idle")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.TcpTimeout:
        from troposphere.appmesh import TcpTimeout as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TlsValidationContext(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html
    Properties:
        - Name: SubjectAlternativeNames
        - Name: Trust
    
    """
    
    SubjectAlternativeNames_: Optional['SubjectAlternativeNames'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html#cfn-appmesh-virtualnode-tlsvalidationcontext-subjectalternativenames""", alias="SubjectAlternativeNames")
    Trust_: 'TlsValidationContextTrust' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html#cfn-appmesh-virtualnode-tlsvalidationcontext-trust""", alias="Trust")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.TlsValidationContext:
        from troposphere.appmesh import TlsValidationContext as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TlsValidationContextAcmTrust(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust.html
    Properties:
        - Name: CertificateAuthorityArns
    
    """
    
    CertificateAuthorityArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust.html#cfn-appmesh-virtualnode-tlsvalidationcontextacmtrust-certificateauthorityarns""", alias="CertificateAuthorityArns")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.TlsValidationContextAcmTrust:
        from troposphere.appmesh import TlsValidationContextAcmTrust as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TlsValidationContextFileTrust(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust.html
    Properties:
        - Name: CertificateChain
    
    """
    
    CertificateChain_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust.html#cfn-appmesh-virtualnode-tlsvalidationcontextfiletrust-certificatechain""", alias="CertificateChain")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.TlsValidationContextFileTrust:
        from troposphere.appmesh import TlsValidationContextFileTrust as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TlsValidationContextSdsTrust(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust.html
    Properties:
        - Name: SecretName
    
    """
    
    SecretName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust.html#cfn-appmesh-virtualnode-tlsvalidationcontextsdstrust-secretname""", alias="SecretName")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.TlsValidationContextSdsTrust:
        from troposphere.appmesh import TlsValidationContextSdsTrust as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TlsValidationContextTrust(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html
    Properties:
        - Name: SDS
        - Name: ACM
        - Name: File
    
    """
    
    SDS_: Optional['TlsValidationContextSdsTrust'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-sds""", alias="SDS")
    ACM_: Optional['TlsValidationContextAcmTrust'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-acm""", alias="ACM")
    File_: Optional['TlsValidationContextFileTrust'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-file""", alias="File")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.TlsValidationContextTrust:
        from troposphere.appmesh import TlsValidationContextTrust as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualNodeConnectionPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html
    Properties:
        - Name: TCP
        - Name: HTTP2
        - Name: HTTP
        - Name: GRPC
    
    """
    
    TCP_: Optional['VirtualNodeTcpConnectionPool'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-tcp""", alias="TCP")
    HTTP2_: Optional['VirtualNodeHttp2ConnectionPool'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-http2""", alias="HTTP2")
    HTTP_: Optional['VirtualNodeHttpConnectionPool'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-http""", alias="HTTP")
    GRPC_: Optional['VirtualNodeGrpcConnectionPool'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-grpc""", alias="GRPC")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualNodeConnectionPool:
        from troposphere.appmesh import VirtualNodeConnectionPool as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualNodeGrpcConnectionPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool.html
    Properties:
        - Name: MaxRequests
    
    """
    
    MaxRequests_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool.html#cfn-appmesh-virtualnode-virtualnodegrpcconnectionpool-maxrequests""", alias="MaxRequests")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualNodeGrpcConnectionPool:
        from troposphere.appmesh import VirtualNodeGrpcConnectionPool as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualNodeHttp2ConnectionPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttp2connectionpool.html
    Properties:
        - Name: MaxRequests
    
    """
    
    MaxRequests_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttp2connectionpool.html#cfn-appmesh-virtualnode-virtualnodehttp2connectionpool-maxrequests""", alias="MaxRequests")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualNodeHttp2ConnectionPool:
        from troposphere.appmesh import VirtualNodeHttp2ConnectionPool as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualNodeHttpConnectionPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttpconnectionpool.html
    Properties:
        - Name: MaxConnections
        - Name: MaxPendingRequests
    
    """
    
    MaxConnections_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttpconnectionpool.html#cfn-appmesh-virtualnode-virtualnodehttpconnectionpool-maxconnections""", alias="MaxConnections")
    MaxPendingRequests_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttpconnectionpool.html#cfn-appmesh-virtualnode-virtualnodehttpconnectionpool-maxpendingrequests""", alias="MaxPendingRequests")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualNodeHttpConnectionPool:
        from troposphere.appmesh import VirtualNodeHttpConnectionPool as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualNodeSpec(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html
    Properties:
        - Name: Logging
        - Name: Backends
        - Name: Listeners
        - Name: BackendDefaults
        - Name: ServiceDiscovery
    
    """
    
    Logging_: Optional['Logging'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-logging""", alias="Logging")
    Backends_: Optional[List['Backend']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-backends""", alias="Backends")
    Listeners_: Optional[List['Listener']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-listeners""", alias="Listeners")
    BackendDefaults_: Optional['BackendDefaults'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-backenddefaults""", alias="BackendDefaults")
    ServiceDiscovery_: Optional['ServiceDiscovery'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-servicediscovery""", alias="ServiceDiscovery")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualNodeSpec:
        from troposphere.appmesh import VirtualNodeSpec as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualNodeTcpConnectionPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodetcpconnectionpool.html
    Properties:
        - Name: MaxConnections
    
    """
    
    MaxConnections_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodetcpconnectionpool.html#cfn-appmesh-virtualnode-virtualnodetcpconnectionpool-maxconnections""", alias="MaxConnections")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualNodeTcpConnectionPool:
        from troposphere.appmesh import VirtualNodeTcpConnectionPool as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualServiceBackend(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html
    Properties:
        - Name: ClientPolicy
        - Name: VirtualServiceName
    
    """
    
    ClientPolicy_: Optional['ClientPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html#cfn-appmesh-virtualnode-virtualservicebackend-clientpolicy""", alias="ClientPolicy")
    VirtualServiceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html#cfn-appmesh-virtualnode-virtualservicebackend-virtualservicename""", alias="VirtualServiceName")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualServiceBackend:
        from troposphere.appmesh import VirtualServiceBackend as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PortMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html
    Properties:
        - Name: Port
        - Name: Protocol
    
    """
    
    Port_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html#cfn-appmesh-virtualrouter-portmapping-port""", alias="Port")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html#cfn-appmesh-virtualrouter-portmapping-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.PortMapping:
        from troposphere.appmesh import PortMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualRouterListener(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html
    Properties:
        - Name: PortMapping
    
    """
    
    PortMapping_: 'PortMapping' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html#cfn-appmesh-virtualrouter-virtualrouterlistener-portmapping""", alias="PortMapping")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualRouterListener:
        from troposphere.appmesh import VirtualRouterListener as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualRouterSpec(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterspec.html
    Properties:
        - Name: Listeners
    
    """
    
    Listeners_: List['VirtualRouterListener'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterspec.html#cfn-appmesh-virtualrouter-virtualrouterspec-listeners""", alias="Listeners")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualRouterSpec:
        from troposphere.appmesh import VirtualRouterSpec as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualNodeServiceProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualnodeserviceprovider.html
    Properties:
        - Name: VirtualNodeName
    
    """
    
    VirtualNodeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualnodeserviceprovider.html#cfn-appmesh-virtualservice-virtualnodeserviceprovider-virtualnodename""", alias="VirtualNodeName")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualNodeServiceProvider:
        from troposphere.appmesh import VirtualNodeServiceProvider as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualRouterServiceProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualrouterserviceprovider.html
    Properties:
        - Name: VirtualRouterName
    
    """
    
    VirtualRouterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualrouterserviceprovider.html#cfn-appmesh-virtualservice-virtualrouterserviceprovider-virtualroutername""", alias="VirtualRouterName")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualRouterServiceProvider:
        from troposphere.appmesh import VirtualRouterServiceProvider as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualServiceProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html
    Properties:
        - Name: VirtualNode
        - Name: VirtualRouter
    
    """
    
    VirtualNode_: Optional['VirtualNodeServiceProvider'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html#cfn-appmesh-virtualservice-virtualserviceprovider-virtualnode""", alias="VirtualNode")
    VirtualRouter_: Optional['VirtualRouterServiceProvider'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html#cfn-appmesh-virtualservice-virtualserviceprovider-virtualrouter""", alias="VirtualRouter")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualServiceProvider:
        from troposphere.appmesh import VirtualServiceProvider as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VirtualServiceSpec(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualservicespec.html
    Properties:
        - Name: Provider
    
    """
    
    Provider_: Optional['VirtualServiceProvider'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualservicespec.html#cfn-appmesh-virtualservice-virtualservicespec-provider""", alias="Provider")
    


    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualServiceSpec:
        from troposphere.appmesh import VirtualServiceSpec as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class GatewayRoute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html
    Properties:
        - Name: MeshName
        - Name: VirtualGatewayName
        - Name: MeshOwner
        - Name: GatewayRouteName
        - Name: Spec
        - Name: Tags
    Attributes:
        - Name: Uid
        - Name: MeshName
        - Name: VirtualGatewayName
        - Name: MeshOwner
        - Name: ResourceOwner
        - Name: GatewayRouteName
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MeshName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-meshname""", alias="MeshName")
    VirtualGatewayName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-virtualgatewayname""", alias="VirtualGatewayName")
    MeshOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-meshowner""", alias="MeshOwner")
    GatewayRouteName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-gatewayroutename""", alias="GatewayRouteName")
    Spec_: 'GatewayRouteSpec' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-spec""", alias="Spec")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.appmesh.GatewayRoute:
        from troposphere.appmesh import GatewayRoute as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appmesh import GatewayRoute as TropoT
        return resource_to_troposphere(self, TropoT)


class Mesh(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html
    Properties:
        - Name: MeshName
        - Name: Spec
        - Name: Tags
    Attributes:
        - Name: Uid
        - Name: MeshName
        - Name: MeshOwner
        - Name: ResourceOwner
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MeshName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-meshname""", alias="MeshName")
    Spec_: Optional['MeshSpec'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-spec""", alias="Spec")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.appmesh.Mesh:
        from troposphere.appmesh import Mesh as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appmesh import Mesh as TropoT
        return resource_to_troposphere(self, TropoT)


class Route(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html
    Properties:
        - Name: MeshName
        - Name: VirtualRouterName
        - Name: MeshOwner
        - Name: RouteName
        - Name: Spec
        - Name: Tags
    Attributes:
        - Name: Uid
        - Name: MeshName
        - Name: VirtualRouterName
        - Name: MeshOwner
        - Name: ResourceOwner
        - Name: RouteName
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MeshName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-meshname""", alias="MeshName")
    VirtualRouterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-virtualroutername""", alias="VirtualRouterName")
    MeshOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-meshowner""", alias="MeshOwner")
    RouteName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-routename""", alias="RouteName")
    Spec_: 'RouteSpec' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-spec""", alias="Spec")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.appmesh.Route:
        from troposphere.appmesh import Route as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appmesh import Route as TropoT
        return resource_to_troposphere(self, TropoT)


class VirtualGateway(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html
    Properties:
        - Name: VirtualGatewayName
        - Name: MeshName
        - Name: MeshOwner
        - Name: Spec
        - Name: Tags
    Attributes:
        - Name: Uid
        - Name: VirtualGatewayName
        - Name: MeshName
        - Name: MeshOwner
        - Name: ResourceOwner
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VirtualGatewayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-virtualgatewayname""", alias="VirtualGatewayName")
    MeshName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-meshname""", alias="MeshName")
    MeshOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-meshowner""", alias="MeshOwner")
    Spec_: 'VirtualGatewaySpec' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-spec""", alias="Spec")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualGateway:
        from troposphere.appmesh import VirtualGateway as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appmesh import VirtualGateway as TropoT
        return resource_to_troposphere(self, TropoT)


class VirtualNode(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html
    Properties:
        - Name: MeshName
        - Name: MeshOwner
        - Name: Spec
        - Name: VirtualNodeName
        - Name: Tags
    Attributes:
        - Name: Uid
        - Name: MeshName
        - Name: MeshOwner
        - Name: ResourceOwner
        - Name: Arn
        - Name: VirtualNodeName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MeshName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-meshname""", alias="MeshName")
    MeshOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-meshowner""", alias="MeshOwner")
    Spec_: 'VirtualNodeSpec' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-spec""", alias="Spec")
    VirtualNodeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-virtualnodename""", alias="VirtualNodeName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualNode:
        from troposphere.appmesh import VirtualNode as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appmesh import VirtualNode as TropoT
        return resource_to_troposphere(self, TropoT)


class VirtualRouter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html
    Properties:
        - Name: MeshName
        - Name: VirtualRouterName
        - Name: MeshOwner
        - Name: Spec
        - Name: Tags
    Attributes:
        - Name: Uid
        - Name: MeshName
        - Name: VirtualRouterName
        - Name: MeshOwner
        - Name: ResourceOwner
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MeshName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-meshname""", alias="MeshName")
    VirtualRouterName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-virtualroutername""", alias="VirtualRouterName")
    MeshOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-meshowner""", alias="MeshOwner")
    Spec_: 'VirtualRouterSpec' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-spec""", alias="Spec")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualRouter:
        from troposphere.appmesh import VirtualRouter as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appmesh import VirtualRouter as TropoT
        return resource_to_troposphere(self, TropoT)


class VirtualService(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html
    Properties:
        - Name: MeshName
        - Name: MeshOwner
        - Name: VirtualServiceName
        - Name: Spec
        - Name: Tags
    Attributes:
        - Name: Uid
        - Name: MeshName
        - Name: MeshOwner
        - Name: ResourceOwner
        - Name: VirtualServiceName
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MeshName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-meshname""", alias="MeshName")
    MeshOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-meshowner""", alias="MeshOwner")
    VirtualServiceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-virtualservicename""", alias="VirtualServiceName")
    Spec_: 'VirtualServiceSpec' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-spec""", alias="Spec")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.appmesh.VirtualService:
        from troposphere.appmesh import VirtualService as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appmesh import VirtualService as TropoT
        return resource_to_troposphere(self, TropoT)

