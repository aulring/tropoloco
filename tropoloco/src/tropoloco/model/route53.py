from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrcollection-location.html
    Properties:
        - Name: CidrList
        - Name: LocationName
    
    """
    
    CidrList_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrcollection-location.html#cfn-route53-cidrcollection-location-cidrlist""", alias="CidrList")
    LocationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrcollection-location.html#cfn-route53-cidrcollection-location-locationname""", alias="LocationName")
    


    @property
    def tropo_type(self) -> troposphere.route53.Location:
        from troposphere.route53 import Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AlarmIdentifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html
    Properties:
        - Name: Region
        - Name: Name
    
    """
    
    Region_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html#cfn-route53-healthcheck-alarmidentifier-region""", alias="Region")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html#cfn-route53-healthcheck-alarmidentifier-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.route53.AlarmIdentifier:
        from troposphere.route53 import AlarmIdentifier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HealthCheckConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html
    Properties:
        - Name: EnableSNI
        - Name: ChildHealthChecks
        - Name: MeasureLatency
        - Name: Port
        - Name: Regions
        - Name: InsufficientDataHealthStatus
        - Name: SearchString
        - Name: Type
        - Name: ResourcePath
        - Name: RoutingControlArn
        - Name: FullyQualifiedDomainName
        - Name: Inverted
        - Name: HealthThreshold
        - Name: RequestInterval
        - Name: AlarmIdentifier
        - Name: FailureThreshold
        - Name: IPAddress
    
    """
    
    EnableSNI_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-enablesni""", alias="EnableSNI")
    ChildHealthChecks_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-childhealthchecks""", alias="ChildHealthChecks")
    MeasureLatency_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-measurelatency""", alias="MeasureLatency")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-port""", alias="Port")
    Regions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-regions""", alias="Regions")
    InsufficientDataHealthStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-insufficientdatahealthstatus""", alias="InsufficientDataHealthStatus")
    SearchString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-searchstring""", alias="SearchString")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-type""", alias="Type")
    ResourcePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-resourcepath""", alias="ResourcePath")
    RoutingControlArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-routingcontrolarn""", alias="RoutingControlArn")
    FullyQualifiedDomainName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-fullyqualifieddomainname""", alias="FullyQualifiedDomainName")
    Inverted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-inverted""", alias="Inverted")
    HealthThreshold_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-healththreshold""", alias="HealthThreshold")
    RequestInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-requestinterval""", alias="RequestInterval")
    AlarmIdentifier_: Optional['AlarmIdentifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-alarmidentifier""", alias="AlarmIdentifier")
    FailureThreshold_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-failurethreshold""", alias="FailureThreshold")
    IPAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-ipaddress""", alias="IPAddress")
    


    @property
    def tropo_type(self) -> troposphere.route53.HealthCheckConfig:
        from troposphere.route53 import HealthCheckConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HealthCheckTag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthchecktag.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthchecktag.html#cfn-route53-healthcheck-healthchecktag-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthchecktag.html#cfn-route53-healthcheck-healthchecktag-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.route53.HealthCheckTag:
        from troposphere.route53 import HealthCheckTag as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HostedZoneConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html
    Properties:
        - Name: Comment
    
    """
    
    Comment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html#cfn-route53-hostedzone-hostedzoneconfig-comment""", alias="Comment")
    


    @property
    def tropo_type(self) -> troposphere.route53.HostedZoneConfig:
        from troposphere.route53 import HostedZoneConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HostedZoneTag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzonetag.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzonetag.html#cfn-route53-hostedzone-hostedzonetag-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzonetag.html#cfn-route53-hostedzone-hostedzonetag-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.route53.HostedZoneTag:
        from troposphere.route53 import HostedZoneTag as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QueryLoggingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html
    Properties:
        - Name: CloudWatchLogsLogGroupArn
    
    """
    
    CloudWatchLogsLogGroupArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html#cfn-route53-hostedzone-queryloggingconfig-cloudwatchlogsloggrouparn""", alias="CloudWatchLogsLogGroupArn")
    


    @property
    def tropo_type(self) -> troposphere.route53.QueryLoggingConfig:
        from troposphere.route53 import QueryLoggingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VPC(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-vpc.html
    Properties:
        - Name: VPCRegion
        - Name: VPCId
    
    """
    
    VPCRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-vpc.html#cfn-route53-hostedzone-vpc-vpcregion""", alias="VPCRegion")
    VPCId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-vpc.html#cfn-route53-hostedzone-vpc-vpcid""", alias="VPCId")
    


    @property
    def tropo_type(self) -> troposphere.route53.VPC:
        from troposphere.route53 import VPC as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AliasTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html
    Properties:
        - Name: DNSName
        - Name: EvaluateTargetHealth
        - Name: HostedZoneId
    
    """
    
    DNSName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-dnshostname""", alias="DNSName")
    EvaluateTargetHealth_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-evaluatetargethealth""", alias="EvaluateTargetHealth")
    HostedZoneId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-hostedzoneid""", alias="HostedZoneId")
    


    @property
    def tropo_type(self) -> troposphere.route53.AliasTarget:
        from troposphere.route53 import AliasTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CidrRoutingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrroutingconfig.html
    Properties:
        - Name: CollectionId
        - Name: LocationName
    
    """
    
    CollectionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrroutingconfig.html#cfn-route53-cidrroutingconfig-collectionid""", alias="CollectionId")
    LocationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrroutingconfig.html#cfn-route53-cidrroutingconfig-locationname""", alias="LocationName")
    


    @property
    def tropo_type(self) -> troposphere.route53.CidrRoutingConfig:
        from troposphere.route53 import CidrRoutingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GeoLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html
    Properties:
        - Name: ContinentCode
        - Name: CountryCode
        - Name: SubdivisionCode
    
    """
    
    ContinentCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-continentcode""", alias="ContinentCode")
    CountryCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-countrycode""", alias="CountryCode")
    SubdivisionCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-subdivisioncode""", alias="SubdivisionCode")
    


    @property
    def tropo_type(self) -> troposphere.route53.GeoLocation:
        from troposphere.route53 import GeoLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AliasTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html
    Properties:
        - Name: DNSName
        - Name: EvaluateTargetHealth
        - Name: HostedZoneId
    
    """
    
    DNSName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-dnshostname""", alias="DNSName")
    EvaluateTargetHealth_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-evaluatetargethealth""", alias="EvaluateTargetHealth")
    HostedZoneId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-hostedzoneid""", alias="HostedZoneId")
    


    @property
    def tropo_type(self) -> troposphere.route53.AliasTarget:
        from troposphere.route53 import AliasTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CidrRoutingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrroutingconfig.html
    Properties:
        - Name: CollectionId
        - Name: LocationName
    
    """
    
    CollectionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrroutingconfig.html#cfn-route53-cidrroutingconfig-collectionid""", alias="CollectionId")
    LocationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrroutingconfig.html#cfn-route53-cidrroutingconfig-locationname""", alias="LocationName")
    


    @property
    def tropo_type(self) -> troposphere.route53.CidrRoutingConfig:
        from troposphere.route53 import CidrRoutingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GeoLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html
    Properties:
        - Name: ContinentCode
        - Name: CountryCode
        - Name: SubdivisionCode
    
    """
    
    ContinentCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordsetgroup-geolocation-continentcode""", alias="ContinentCode")
    CountryCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-countrycode""", alias="CountryCode")
    SubdivisionCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-subdivisioncode""", alias="SubdivisionCode")
    


    @property
    def tropo_type(self) -> troposphere.route53.GeoLocation:
        from troposphere.route53 import GeoLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecordSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html
    Properties:
        - Name: AliasTarget
        - Name: CidrRoutingConfig
        - Name: Failover
        - Name: GeoLocation
        - Name: HealthCheckId
        - Name: HostedZoneId
        - Name: HostedZoneName
        - Name: MultiValueAnswer
        - Name: Name
        - Name: Region
        - Name: ResourceRecords
        - Name: SetIdentifier
        - Name: TTL
        - Name: Type
        - Name: Weight
    
    """
    
    AliasTarget_: Optional['AliasTarget'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-aliastarget""", alias="AliasTarget")
    CidrRoutingConfig_: Optional['CidrRoutingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-cidrroutingconfig""", alias="CidrRoutingConfig")
    Failover_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-failover""", alias="Failover")
    GeoLocation_: Optional['GeoLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-geolocation""", alias="GeoLocation")
    HealthCheckId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-healthcheckid""", alias="HealthCheckId")
    HostedZoneId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzoneid""", alias="HostedZoneId")
    HostedZoneName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzonename""", alias="HostedZoneName")
    MultiValueAnswer_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-multivalueanswer""", alias="MultiValueAnswer")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-name""", alias="Name")
    Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-region""", alias="Region")
    ResourceRecords_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-resourcerecords""", alias="ResourceRecords")
    SetIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-setidentifier""", alias="SetIdentifier")
    TTL_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-ttl""", alias="TTL")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-type""", alias="Type")
    Weight_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-weight""", alias="Weight")
    


    @property
    def tropo_type(self) -> troposphere.route53.RecordSet:
        from troposphere.route53 import RecordSet as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class CidrCollection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-cidrcollection.html
    Properties:
        - Name: Locations
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Locations_: Optional[List['Location']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-cidrcollection.html#cfn-route53-cidrcollection-locations""", alias="Locations")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-cidrcollection.html#cfn-route53-cidrcollection-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53.CidrCollection:
        from troposphere.route53 import CidrCollection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53 import CidrCollection as TropoT
        return resource_to_troposphere(self, TropoT)


class DNSSEC(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-dnssec.html
    Properties:
        - Name: HostedZoneId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    HostedZoneId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-dnssec.html#cfn-route53-dnssec-hostedzoneid""", alias="HostedZoneId")
    

    @property
    def tropo_type(self) -> troposphere.route53.DNSSEC:
        from troposphere.route53 import DNSSEC as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53 import DNSSEC as TropoT
        return resource_to_troposphere(self, TropoT)


class HealthCheck(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html
    Properties:
        - Name: HealthCheckConfig
        - Name: HealthCheckTags
    Attributes:
        - Name: HealthCheckId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    HealthCheckConfig_: 'HealthCheckConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthcheckconfig""", alias="HealthCheckConfig")
    HealthCheckTags_: Optional[Tags] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthchecktags""", alias="HealthCheckTags")
    

    @property
    def tropo_type(self) -> troposphere.route53.HealthCheck:
        from troposphere.route53 import HealthCheck as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53 import HealthCheck as TropoT
        return resource_to_troposphere(self, TropoT)


class HostedZone(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html
    Properties:
        - Name: HostedZoneTags
        - Name: VPCs
        - Name: HostedZoneConfig
        - Name: QueryLoggingConfig
        - Name: Name
    Attributes:
        - Name: Id
        - Name: NameServers
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    HostedZoneTags_: Optional[List['HostedZoneTag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-hostedzonetags""", alias="HostedZoneTags")
    VPCs_: Optional[List['VPC']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-vpcs""", alias="VPCs")
    HostedZoneConfig_: Optional['HostedZoneConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-hostedzoneconfig""", alias="HostedZoneConfig")
    QueryLoggingConfig_: Optional['QueryLoggingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-queryloggingconfig""", alias="QueryLoggingConfig")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53.HostedZone:
        from troposphere.route53 import HostedZone as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53 import HostedZone as TropoT
        return resource_to_troposphere(self, TropoT)


class KeySigningKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html
    Properties:
        - Name: Status
        - Name: KeyManagementServiceArn
        - Name: HostedZoneId
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-status""", alias="Status")
    KeyManagementServiceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-keymanagementservicearn""", alias="KeyManagementServiceArn")
    HostedZoneId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-hostedzoneid""", alias="HostedZoneId")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.route53.KeySigningKey:
        from troposphere.route53 import KeySigningKey as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53 import KeySigningKey as TropoT
        return resource_to_troposphere(self, TropoT)


class RecordSetType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html
    Properties:
        - Name: AliasTarget
        - Name: CidrRoutingConfig
        - Name: Comment
        - Name: Failover
        - Name: GeoLocation
        - Name: HealthCheckId
        - Name: HostedZoneId
        - Name: HostedZoneName
        - Name: MultiValueAnswer
        - Name: Name
        - Name: Region
        - Name: ResourceRecords
        - Name: SetIdentifier
        - Name: TTL
        - Name: Type
        - Name: Weight
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AliasTarget_: Optional['AliasTarget'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-aliastarget""", alias="AliasTarget")
    CidrRoutingConfig_: Optional['CidrRoutingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-cidrroutingconfig""", alias="CidrRoutingConfig")
    Comment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-comment""", alias="Comment")
    Failover_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-failover""", alias="Failover")
    GeoLocation_: Optional['GeoLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-geolocation""", alias="GeoLocation")
    HealthCheckId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-healthcheckid""", alias="HealthCheckId")
    HostedZoneId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzoneid""", alias="HostedZoneId")
    HostedZoneName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzonename""", alias="HostedZoneName")
    MultiValueAnswer_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-multivalueanswer""", alias="MultiValueAnswer")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-name""", alias="Name")
    Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-region""", alias="Region")
    ResourceRecords_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-resourcerecords""", alias="ResourceRecords")
    SetIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-setidentifier""", alias="SetIdentifier")
    TTL_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-ttl""", alias="TTL")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-type""", alias="Type")
    Weight_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-weight""", alias="Weight")
    

    @property
    def tropo_type(self) -> troposphere.route53.RecordSet:
        from troposphere.route53 import RecordSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53 import RecordSet as TropoT
        return resource_to_troposphere(self, TropoT)


class RecordSetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html
    Properties:
        - Name: Comment
        - Name: HostedZoneId
        - Name: HostedZoneName
        - Name: RecordSets
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Comment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-comment""", alias="Comment")
    HostedZoneId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-hostedzoneid""", alias="HostedZoneId")
    HostedZoneName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-hostedzonename""", alias="HostedZoneName")
    RecordSets_: Optional[List['RecordSet']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-recordsets""", alias="RecordSets")
    

    @property
    def tropo_type(self) -> troposphere.route53.RecordSetGroup:
        from troposphere.route53 import RecordSetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53 import RecordSetGroup as TropoT
        return resource_to_troposphere(self, TropoT)

