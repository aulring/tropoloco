from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class EndpointConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html
    Properties:
        - Name: EndpointId
        - Name: Weight
        - Name: ClientIPPreservationEnabled
    
    """
    
    EndpointId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html#cfn-globalaccelerator-endpointgroup-endpointconfiguration-endpointid""", alias="EndpointId")
    Weight_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html#cfn-globalaccelerator-endpointgroup-endpointconfiguration-weight""", alias="Weight")
    ClientIPPreservationEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html#cfn-globalaccelerator-endpointgroup-endpointconfiguration-clientippreservationenabled""", alias="ClientIPPreservationEnabled")
    


    @property
    def tropo_type(self) -> troposphere.globalaccelerator.EndpointConfiguration:
        from troposphere.globalaccelerator import EndpointConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PortOverride(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-portoverride.html
    Properties:
        - Name: ListenerPort
        - Name: EndpointPort
    
    """
    
    ListenerPort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-portoverride.html#cfn-globalaccelerator-endpointgroup-portoverride-listenerport""", alias="ListenerPort")
    EndpointPort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-portoverride.html#cfn-globalaccelerator-endpointgroup-portoverride-endpointport""", alias="EndpointPort")
    


    @property
    def tropo_type(self) -> troposphere.globalaccelerator.PortOverride:
        from troposphere.globalaccelerator import PortOverride as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PortRange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-listener-portrange.html
    Properties:
        - Name: FromPort
        - Name: ToPort
    
    """
    
    FromPort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-listener-portrange.html#cfn-globalaccelerator-listener-portrange-fromport""", alias="FromPort")
    ToPort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-listener-portrange.html#cfn-globalaccelerator-listener-portrange-toport""", alias="ToPort")
    


    @property
    def tropo_type(self) -> troposphere.globalaccelerator.PortRange:
        from troposphere.globalaccelerator import PortRange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Accelerator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html
    Properties:
        - Name: IpAddressType
        - Name: IpAddresses
        - Name: Enabled
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Ipv4Addresses
        - Name: DnsName
        - Name: DualStackDnsName
        - Name: AcceleratorArn
        - Name: Ipv6Addresses
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IpAddressType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-ipaddresstype""", alias="IpAddressType")
    IpAddresses_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-ipaddresses""", alias="IpAddresses")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-enabled""", alias="Enabled")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html#cfn-globalaccelerator-accelerator-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.globalaccelerator.Accelerator:
        from troposphere.globalaccelerator import Accelerator as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.globalaccelerator import Accelerator as TropoT
        return resource_to_troposphere(self, TropoT)


class EndpointGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html
    Properties:
        - Name: ListenerArn
        - Name: PortOverrides
        - Name: HealthCheckIntervalSeconds
        - Name: EndpointGroupRegion
        - Name: HealthCheckPath
        - Name: TrafficDialPercentage
        - Name: HealthCheckProtocol
        - Name: ThresholdCount
        - Name: HealthCheckPort
        - Name: EndpointConfigurations
    Attributes:
        - Name: EndpointGroupArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ListenerArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-listenerarn""", alias="ListenerArn")
    PortOverrides_: Optional[List['PortOverride']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-portoverrides""", alias="PortOverrides")
    HealthCheckIntervalSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckintervalseconds""", alias="HealthCheckIntervalSeconds")
    EndpointGroupRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-endpointgroupregion""", alias="EndpointGroupRegion")
    HealthCheckPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckpath""", alias="HealthCheckPath")
    TrafficDialPercentage_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-trafficdialpercentage""", alias="TrafficDialPercentage")
    HealthCheckProtocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckprotocol""", alias="HealthCheckProtocol")
    ThresholdCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-thresholdcount""", alias="ThresholdCount")
    HealthCheckPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-healthcheckport""", alias="HealthCheckPort")
    EndpointConfigurations_: Optional[List['EndpointConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html#cfn-globalaccelerator-endpointgroup-endpointconfigurations""", alias="EndpointConfigurations")
    

    @property
    def tropo_type(self) -> troposphere.globalaccelerator.EndpointGroup:
        from troposphere.globalaccelerator import EndpointGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.globalaccelerator import EndpointGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class Listener(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html
    Properties:
        - Name: PortRanges
        - Name: AcceleratorArn
        - Name: Protocol
        - Name: ClientAffinity
    Attributes:
        - Name: ListenerArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PortRanges_: List['PortRange'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-portranges""", alias="PortRanges")
    AcceleratorArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-acceleratorarn""", alias="AcceleratorArn")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-protocol""", alias="Protocol")
    ClientAffinity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html#cfn-globalaccelerator-listener-clientaffinity""", alias="ClientAffinity")
    

    @property
    def tropo_type(self) -> troposphere.globalaccelerator.Listener:
        from troposphere.globalaccelerator import Listener as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.globalaccelerator import Listener as TropoT
        return resource_to_troposphere(self, TropoT)

