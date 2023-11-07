from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class PrivateDnsPropertiesMutable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-privatednspropertiesmutable.html
    Properties:
        - Name: SOA
    
    """
    
    SOA_: Optional['SOA'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-privatednspropertiesmutable.html#cfn-servicediscovery-privatednsnamespace-privatednspropertiesmutable-soa""", alias="SOA")
    


    @property
    def tropo_type(self) -> troposphere.servicediscovery.PrivateDnsPropertiesMutable:
        from troposphere.servicediscovery import PrivateDnsPropertiesMutable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Properties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-properties.html
    Properties:
        - Name: DnsProperties
    
    """
    
    DnsProperties_: Optional['PrivateDnsPropertiesMutable'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-properties.html#cfn-servicediscovery-privatednsnamespace-properties-dnsproperties""", alias="DnsProperties")
    


    @property
    def tropo_type(self) -> troposphere.servicediscovery.Properties:
        from troposphere.servicediscovery import Properties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SOA(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-soa.html
    Properties:
        - Name: TTL
    
    """
    
    TTL_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-soa.html#cfn-servicediscovery-privatednsnamespace-soa-ttl""", alias="TTL")
    


    @property
    def tropo_type(self) -> troposphere.servicediscovery.SOA:
        from troposphere.servicediscovery import SOA as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Properties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-properties.html
    Properties:
        - Name: DnsProperties
    
    """
    
    DnsProperties_: Optional['PublicDnsPropertiesMutable'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-properties.html#cfn-servicediscovery-publicdnsnamespace-properties-dnsproperties""", alias="DnsProperties")
    


    @property
    def tropo_type(self) -> troposphere.servicediscovery.Properties:
        from troposphere.servicediscovery import Properties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PublicDnsPropertiesMutable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-publicdnspropertiesmutable.html
    Properties:
        - Name: SOA
    
    """
    
    SOA_: Optional['SOA'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-publicdnspropertiesmutable.html#cfn-servicediscovery-publicdnsnamespace-publicdnspropertiesmutable-soa""", alias="SOA")
    


    @property
    def tropo_type(self) -> troposphere.servicediscovery.PublicDnsPropertiesMutable:
        from troposphere.servicediscovery import PublicDnsPropertiesMutable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SOA(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-soa.html
    Properties:
        - Name: TTL
    
    """
    
    TTL_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-soa.html#cfn-servicediscovery-publicdnsnamespace-soa-ttl""", alias="TTL")
    


    @property
    def tropo_type(self) -> troposphere.servicediscovery.SOA:
        from troposphere.servicediscovery import SOA as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DnsConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html
    Properties:
        - Name: DnsRecords
        - Name: RoutingPolicy
        - Name: NamespaceId
    
    """
    
    DnsRecords_: List['DnsRecord'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html#cfn-servicediscovery-service-dnsconfig-dnsrecords""", alias="DnsRecords")
    RoutingPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html#cfn-servicediscovery-service-dnsconfig-routingpolicy""", alias="RoutingPolicy")
    NamespaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html#cfn-servicediscovery-service-dnsconfig-namespaceid""", alias="NamespaceId")
    


    @property
    def tropo_type(self) -> troposphere.servicediscovery.DnsConfig:
        from troposphere.servicediscovery import DnsConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DnsRecord(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsrecord.html
    Properties:
        - Name: Type
        - Name: TTL
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsrecord.html#cfn-servicediscovery-service-dnsrecord-type""", alias="Type")
    TTL_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsrecord.html#cfn-servicediscovery-service-dnsrecord-ttl""", alias="TTL")
    


    @property
    def tropo_type(self) -> troposphere.servicediscovery.DnsRecord:
        from troposphere.servicediscovery import DnsRecord as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HealthCheckConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html
    Properties:
        - Name: Type
        - Name: ResourcePath
        - Name: FailureThreshold
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html#cfn-servicediscovery-service-healthcheckconfig-type""", alias="Type")
    ResourcePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html#cfn-servicediscovery-service-healthcheckconfig-resourcepath""", alias="ResourcePath")
    FailureThreshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html#cfn-servicediscovery-service-healthcheckconfig-failurethreshold""", alias="FailureThreshold")
    


    @property
    def tropo_type(self) -> troposphere.servicediscovery.HealthCheckConfig:
        from troposphere.servicediscovery import HealthCheckConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HealthCheckCustomConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckcustomconfig.html
    Properties:
        - Name: FailureThreshold
    
    """
    
    FailureThreshold_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckcustomconfig.html#cfn-servicediscovery-service-healthcheckcustomconfig-failurethreshold""", alias="FailureThreshold")
    


    @property
    def tropo_type(self) -> troposphere.servicediscovery.HealthCheckCustomConfig:
        from troposphere.servicediscovery import HealthCheckCustomConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class HttpNamespace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html
    Properties:
        - Name: Description
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html#cfn-servicediscovery-httpnamespace-description""", alias="Description")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html#cfn-servicediscovery-httpnamespace-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html#cfn-servicediscovery-httpnamespace-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.servicediscovery.HttpNamespace:
        from troposphere.servicediscovery import HttpNamespace as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicediscovery import HttpNamespace as TropoT
        return resource_to_troposphere(self, TropoT)


class Instance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html
    Properties:
        - Name: InstanceAttributes
        - Name: InstanceId
        - Name: ServiceId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InstanceAttributes_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-instanceattributes""", alias="InstanceAttributes")
    InstanceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-instanceid""", alias="InstanceId")
    ServiceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-serviceid""", alias="ServiceId")
    

    @property
    def tropo_type(self) -> troposphere.servicediscovery.Instance:
        from troposphere.servicediscovery import Instance as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicediscovery import Instance as TropoT
        return resource_to_troposphere(self, TropoT)


class PrivateDnsNamespace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html
    Properties:
        - Name: Description
        - Name: Vpc
        - Name: Properties
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: HostedZoneId
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-description""", alias="Description")
    Vpc_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-vpc""", alias="Vpc")
    Properties_: Optional['Properties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-properties""", alias="Properties")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.servicediscovery.PrivateDnsNamespace:
        from troposphere.servicediscovery import PrivateDnsNamespace as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicediscovery import PrivateDnsNamespace as TropoT
        return resource_to_troposphere(self, TropoT)


class PublicDnsNamespace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html
    Properties:
        - Name: Description
        - Name: Properties
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: HostedZoneId
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-description""", alias="Description")
    Properties_: Optional['Properties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-properties""", alias="Properties")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.servicediscovery.PublicDnsNamespace:
        from troposphere.servicediscovery import PublicDnsNamespace as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicediscovery import PublicDnsNamespace as TropoT
        return resource_to_troposphere(self, TropoT)


class Service(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: HealthCheckCustomConfig
        - Name: DnsConfig
        - Name: NamespaceId
        - Name: HealthCheckConfig
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-description""", alias="Description")
    HealthCheckCustomConfig_: Optional['HealthCheckCustomConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-healthcheckcustomconfig""", alias="HealthCheckCustomConfig")
    DnsConfig_: Optional['DnsConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-dnsconfig""", alias="DnsConfig")
    NamespaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-namespaceid""", alias="NamespaceId")
    HealthCheckConfig_: Optional['HealthCheckConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-healthcheckconfig""", alias="HealthCheckConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.servicediscovery.Service:
        from troposphere.servicediscovery import Service as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicediscovery import Service as TropoT
        return resource_to_troposphere(self, TropoT)

