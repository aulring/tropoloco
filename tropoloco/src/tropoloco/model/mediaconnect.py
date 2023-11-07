from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class BridgeFlowSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeflowsource.html
    Properties:
        - Name: FlowVpcInterfaceAttachment
        - Name: FlowArn
        - Name: Name
    
    """
    
    FlowVpcInterfaceAttachment_: Optional['VpcInterfaceAttachment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeflowsource.html#cfn-mediaconnect-bridge-bridgeflowsource-flowvpcinterfaceattachment""", alias="FlowVpcInterfaceAttachment")
    FlowArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeflowsource.html#cfn-mediaconnect-bridge-bridgeflowsource-flowarn""", alias="FlowArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeflowsource.html#cfn-mediaconnect-bridge-bridgeflowsource-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.BridgeFlowSource:
        from troposphere.mediaconnect import BridgeFlowSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BridgeNetworkOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html
    Properties:
        - Name: NetworkName
        - Name: Port
        - Name: IpAddress
        - Name: Protocol
        - Name: Ttl
        - Name: Name
    
    """
    
    NetworkName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-networkname""", alias="NetworkName")
    Port_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-port""", alias="Port")
    IpAddress_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-ipaddress""", alias="IpAddress")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-protocol""", alias="Protocol")
    Ttl_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-ttl""", alias="Ttl")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.BridgeNetworkOutput:
        from troposphere.mediaconnect import BridgeNetworkOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BridgeNetworkSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html
    Properties:
        - Name: NetworkName
        - Name: MulticastIp
        - Name: Port
        - Name: Protocol
        - Name: Name
    
    """
    
    NetworkName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-networkname""", alias="NetworkName")
    MulticastIp_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-multicastip""", alias="MulticastIp")
    Port_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-port""", alias="Port")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-protocol""", alias="Protocol")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.BridgeNetworkSource:
        from troposphere.mediaconnect import BridgeNetworkSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BridgeOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeoutput.html
    Properties:
        - Name: NetworkOutput
    
    """
    
    NetworkOutput_: Optional['BridgeNetworkOutput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeoutput.html#cfn-mediaconnect-bridge-bridgeoutput-networkoutput""", alias="NetworkOutput")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.BridgeOutput:
        from troposphere.mediaconnect import BridgeOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BridgeSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgesource.html
    Properties:
        - Name: NetworkSource
        - Name: FlowSource
    
    """
    
    NetworkSource_: Optional['BridgeNetworkSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgesource.html#cfn-mediaconnect-bridge-bridgesource-networksource""", alias="NetworkSource")
    FlowSource_: Optional['BridgeFlowSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgesource.html#cfn-mediaconnect-bridge-bridgesource-flowsource""", alias="FlowSource")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.BridgeSource:
        from troposphere.mediaconnect import BridgeSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EgressGatewayBridge(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-egressgatewaybridge.html
    Properties:
        - Name: MaxBitrate
    
    """
    
    MaxBitrate_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-egressgatewaybridge.html#cfn-mediaconnect-bridge-egressgatewaybridge-maxbitrate""", alias="MaxBitrate")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.EgressGatewayBridge:
        from troposphere.mediaconnect import EgressGatewayBridge as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FailoverConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-failoverconfig.html
    Properties:
        - Name: State
        - Name: SourcePriority
        - Name: FailoverMode
    
    """
    
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-failoverconfig.html#cfn-mediaconnect-bridge-failoverconfig-state""", alias="State")
    SourcePriority_: Optional['SourcePriority'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-failoverconfig.html#cfn-mediaconnect-bridge-failoverconfig-sourcepriority""", alias="SourcePriority")
    FailoverMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-failoverconfig.html#cfn-mediaconnect-bridge-failoverconfig-failovermode""", alias="FailoverMode")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.FailoverConfig:
        from troposphere.mediaconnect import FailoverConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IngressGatewayBridge(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-ingressgatewaybridge.html
    Properties:
        - Name: MaxOutputs
        - Name: MaxBitrate
    
    """
    
    MaxOutputs_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-ingressgatewaybridge.html#cfn-mediaconnect-bridge-ingressgatewaybridge-maxoutputs""", alias="MaxOutputs")
    MaxBitrate_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-ingressgatewaybridge.html#cfn-mediaconnect-bridge-ingressgatewaybridge-maxbitrate""", alias="MaxBitrate")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.IngressGatewayBridge:
        from troposphere.mediaconnect import IngressGatewayBridge as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourcePriority(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-sourcepriority.html
    Properties:
        - Name: PrimarySource
    
    """
    
    PrimarySource_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-sourcepriority.html#cfn-mediaconnect-bridge-sourcepriority-primarysource""", alias="PrimarySource")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.SourcePriority:
        from troposphere.mediaconnect import SourcePriority as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcInterfaceAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-vpcinterfaceattachment.html
    Properties:
        - Name: VpcInterfaceName
    
    """
    
    VpcInterfaceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-vpcinterfaceattachment.html#cfn-mediaconnect-bridge-vpcinterfaceattachment-vpcinterfacename""", alias="VpcInterfaceName")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.VpcInterfaceAttachment:
        from troposphere.mediaconnect import VpcInterfaceAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BridgeNetworkOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html
    Properties:
        - Name: NetworkName
        - Name: Port
        - Name: IpAddress
        - Name: Protocol
        - Name: Ttl
    
    """
    
    NetworkName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-networkname""", alias="NetworkName")
    Port_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-port""", alias="Port")
    IpAddress_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-ipaddress""", alias="IpAddress")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-protocol""", alias="Protocol")
    Ttl_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-ttl""", alias="Ttl")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.BridgeNetworkOutput:
        from troposphere.mediaconnect import BridgeNetworkOutput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BridgeFlowSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgeflowsource.html
    Properties:
        - Name: FlowVpcInterfaceAttachment
        - Name: FlowArn
    
    """
    
    FlowVpcInterfaceAttachment_: Optional['VpcInterfaceAttachment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgeflowsource.html#cfn-mediaconnect-bridgesource-bridgeflowsource-flowvpcinterfaceattachment""", alias="FlowVpcInterfaceAttachment")
    FlowArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgeflowsource.html#cfn-mediaconnect-bridgesource-bridgeflowsource-flowarn""", alias="FlowArn")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.BridgeFlowSource:
        from troposphere.mediaconnect import BridgeFlowSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BridgeNetworkSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html
    Properties:
        - Name: NetworkName
        - Name: MulticastIp
        - Name: Port
        - Name: Protocol
    
    """
    
    NetworkName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html#cfn-mediaconnect-bridgesource-bridgenetworksource-networkname""", alias="NetworkName")
    MulticastIp_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html#cfn-mediaconnect-bridgesource-bridgenetworksource-multicastip""", alias="MulticastIp")
    Port_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html#cfn-mediaconnect-bridgesource-bridgenetworksource-port""", alias="Port")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html#cfn-mediaconnect-bridgesource-bridgenetworksource-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.BridgeNetworkSource:
        from troposphere.mediaconnect import BridgeNetworkSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcInterfaceAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-vpcinterfaceattachment.html
    Properties:
        - Name: VpcInterfaceName
    
    """
    
    VpcInterfaceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-vpcinterfaceattachment.html#cfn-mediaconnect-bridgesource-vpcinterfaceattachment-vpcinterfacename""", alias="VpcInterfaceName")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.VpcInterfaceAttachment:
        from troposphere.mediaconnect import VpcInterfaceAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Encryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html
    Properties:
        - Name: SecretArn
        - Name: KeyType
        - Name: ResourceId
        - Name: DeviceId
        - Name: Region
        - Name: ConstantInitializationVector
        - Name: Algorithm
        - Name: RoleArn
        - Name: Url
    
    """
    
    SecretArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-secretarn""", alias="SecretArn")
    KeyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-keytype""", alias="KeyType")
    ResourceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-resourceid""", alias="ResourceId")
    DeviceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-deviceid""", alias="DeviceId")
    Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-region""", alias="Region")
    ConstantInitializationVector_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-constantinitializationvector""", alias="ConstantInitializationVector")
    Algorithm_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-algorithm""", alias="Algorithm")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-rolearn""", alias="RoleArn")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.Encryption:
        from troposphere.mediaconnect import Encryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FailoverConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html
    Properties:
        - Name: State
        - Name: SourcePriority
        - Name: FailoverMode
        - Name: RecoveryWindow
    
    """
    
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-state""", alias="State")
    SourcePriority_: Optional['SourcePriority'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-sourcepriority""", alias="SourcePriority")
    FailoverMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-failovermode""", alias="FailoverMode")
    RecoveryWindow_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-recoverywindow""", alias="RecoveryWindow")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.FailoverConfig:
        from troposphere.mediaconnect import FailoverConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GatewayBridgeSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-gatewaybridgesource.html
    Properties:
        - Name: BridgeArn
        - Name: VpcInterfaceAttachment
    
    """
    
    BridgeArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-gatewaybridgesource.html#cfn-mediaconnect-flow-gatewaybridgesource-bridgearn""", alias="BridgeArn")
    VpcInterfaceAttachment_: Optional['VpcInterfaceAttachment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-gatewaybridgesource.html#cfn-mediaconnect-flow-gatewaybridgesource-vpcinterfaceattachment""", alias="VpcInterfaceAttachment")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.GatewayBridgeSource:
        from troposphere.mediaconnect import GatewayBridgeSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Source(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html
    Properties:
        - Name: IngestIp
        - Name: StreamId
        - Name: Description
        - Name: SenderIpAddress
        - Name: IngestPort
        - Name: SenderControlPort
        - Name: Decryption
        - Name: GatewayBridgeSource
        - Name: SourceListenerAddress
        - Name: SourceListenerPort
        - Name: Name
        - Name: WhitelistCidr
        - Name: EntitlementArn
        - Name: SourceArn
        - Name: MinLatency
        - Name: VpcInterfaceName
        - Name: MaxBitrate
        - Name: Protocol
        - Name: MaxLatency
        - Name: SourceIngestPort
    
    """
    
    IngestIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-ingestip""", alias="IngestIp")
    StreamId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-streamid""", alias="StreamId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-description""", alias="Description")
    SenderIpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-senderipaddress""", alias="SenderIpAddress")
    IngestPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-ingestport""", alias="IngestPort")
    SenderControlPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sendercontrolport""", alias="SenderControlPort")
    Decryption_: Optional['Encryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-decryption""", alias="Decryption")
    GatewayBridgeSource_: Optional['GatewayBridgeSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-gatewaybridgesource""", alias="GatewayBridgeSource")
    SourceListenerAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sourcelisteneraddress""", alias="SourceListenerAddress")
    SourceListenerPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sourcelistenerport""", alias="SourceListenerPort")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-name""", alias="Name")
    WhitelistCidr_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-whitelistcidr""", alias="WhitelistCidr")
    EntitlementArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-entitlementarn""", alias="EntitlementArn")
    SourceArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sourcearn""", alias="SourceArn")
    MinLatency_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-minlatency""", alias="MinLatency")
    VpcInterfaceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-vpcinterfacename""", alias="VpcInterfaceName")
    MaxBitrate_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-maxbitrate""", alias="MaxBitrate")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-protocol""", alias="Protocol")
    MaxLatency_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-maxlatency""", alias="MaxLatency")
    SourceIngestPort_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sourceingestport""", alias="SourceIngestPort")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.Source:
        from troposphere.mediaconnect import Source as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourcePriority(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-sourcepriority.html
    Properties:
        - Name: PrimarySource
    
    """
    
    PrimarySource_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-sourcepriority.html#cfn-mediaconnect-flow-sourcepriority-primarysource""", alias="PrimarySource")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.SourcePriority:
        from troposphere.mediaconnect import SourcePriority as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcInterfaceAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-vpcinterfaceattachment.html
    Properties:
        - Name: VpcInterfaceName
    
    """
    
    VpcInterfaceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-vpcinterfaceattachment.html#cfn-mediaconnect-flow-vpcinterfaceattachment-vpcinterfacename""", alias="VpcInterfaceName")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.VpcInterfaceAttachment:
        from troposphere.mediaconnect import VpcInterfaceAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Encryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html
    Properties:
        - Name: SecretArn
        - Name: KeyType
        - Name: ResourceId
        - Name: DeviceId
        - Name: Region
        - Name: ConstantInitializationVector
        - Name: Algorithm
        - Name: RoleArn
        - Name: Url
    
    """
    
    SecretArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-secretarn""", alias="SecretArn")
    KeyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-keytype""", alias="KeyType")
    ResourceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-resourceid""", alias="ResourceId")
    DeviceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-deviceid""", alias="DeviceId")
    Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-region""", alias="Region")
    ConstantInitializationVector_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-constantinitializationvector""", alias="ConstantInitializationVector")
    Algorithm_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-algorithm""", alias="Algorithm")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-rolearn""", alias="RoleArn")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.Encryption:
        from troposphere.mediaconnect import Encryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Encryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html
    Properties:
        - Name: SecretArn
        - Name: KeyType
        - Name: Algorithm
        - Name: RoleArn
    
    """
    
    SecretArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-secretarn""", alias="SecretArn")
    KeyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-keytype""", alias="KeyType")
    Algorithm_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-algorithm""", alias="Algorithm")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.Encryption:
        from troposphere.mediaconnect import Encryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcInterfaceAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-vpcinterfaceattachment.html
    Properties:
        - Name: VpcInterfaceName
    
    """
    
    VpcInterfaceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-vpcinterfaceattachment.html#cfn-mediaconnect-flowoutput-vpcinterfaceattachment-vpcinterfacename""", alias="VpcInterfaceName")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.VpcInterfaceAttachment:
        from troposphere.mediaconnect import VpcInterfaceAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Encryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html
    Properties:
        - Name: SecretArn
        - Name: KeyType
        - Name: ResourceId
        - Name: DeviceId
        - Name: Region
        - Name: ConstantInitializationVector
        - Name: Algorithm
        - Name: RoleArn
        - Name: Url
    
    """
    
    SecretArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-secretarn""", alias="SecretArn")
    KeyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-keytype""", alias="KeyType")
    ResourceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-resourceid""", alias="ResourceId")
    DeviceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-deviceid""", alias="DeviceId")
    Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-region""", alias="Region")
    ConstantInitializationVector_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-constantinitializationvector""", alias="ConstantInitializationVector")
    Algorithm_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-algorithm""", alias="Algorithm")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-rolearn""", alias="RoleArn")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.Encryption:
        from troposphere.mediaconnect import Encryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GatewayBridgeSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-gatewaybridgesource.html
    Properties:
        - Name: BridgeArn
        - Name: VpcInterfaceAttachment
    
    """
    
    BridgeArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-gatewaybridgesource.html#cfn-mediaconnect-flowsource-gatewaybridgesource-bridgearn""", alias="BridgeArn")
    VpcInterfaceAttachment_: Optional['VpcInterfaceAttachment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-gatewaybridgesource.html#cfn-mediaconnect-flowsource-gatewaybridgesource-vpcinterfaceattachment""", alias="VpcInterfaceAttachment")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.GatewayBridgeSource:
        from troposphere.mediaconnect import GatewayBridgeSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcInterfaceAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-vpcinterfaceattachment.html
    Properties:
        - Name: VpcInterfaceName
    
    """
    
    VpcInterfaceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-vpcinterfaceattachment.html#cfn-mediaconnect-flowsource-vpcinterfaceattachment-vpcinterfacename""", alias="VpcInterfaceName")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.VpcInterfaceAttachment:
        from troposphere.mediaconnect import VpcInterfaceAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GatewayNetwork(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-gateway-gatewaynetwork.html
    Properties:
        - Name: CidrBlock
        - Name: Name
    
    """
    
    CidrBlock_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-gateway-gatewaynetwork.html#cfn-mediaconnect-gateway-gatewaynetwork-cidrblock""", alias="CidrBlock")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-gateway-gatewaynetwork.html#cfn-mediaconnect-gateway-gatewaynetwork-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.mediaconnect.GatewayNetwork:
        from troposphere.mediaconnect import GatewayNetwork as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Bridge(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html
    Properties:
        - Name: SourceFailoverConfig
        - Name: IngressGatewayBridge
        - Name: EgressGatewayBridge
        - Name: Outputs
        - Name: PlacementArn
        - Name: Sources
        - Name: Name
    Attributes:
        - Name: BridgeArn
        - Name: BridgeState
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SourceFailoverConfig_: Optional['FailoverConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-sourcefailoverconfig""", alias="SourceFailoverConfig")
    IngressGatewayBridge_: Optional['IngressGatewayBridge'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-ingressgatewaybridge""", alias="IngressGatewayBridge")
    EgressGatewayBridge_: Optional['EgressGatewayBridge'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-egressgatewaybridge""", alias="EgressGatewayBridge")
    Outputs_: Optional[List['BridgeOutput']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-outputs""", alias="Outputs")
    PlacementArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-placementarn""", alias="PlacementArn")
    Sources_: List['BridgeSource'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-sources""", alias="Sources")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.mediaconnect.Bridge:
        from troposphere.mediaconnect import Bridge as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediaconnect import Bridge as TropoT
        return resource_to_troposphere(self, TropoT)


class BridgeOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html
    Properties:
        - Name: BridgeArn
        - Name: NetworkOutput
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BridgeArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html#cfn-mediaconnect-bridgeoutput-bridgearn""", alias="BridgeArn")
    NetworkOutput_: 'BridgeNetworkOutput' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html#cfn-mediaconnect-bridgeoutput-networkoutput""", alias="NetworkOutput")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html#cfn-mediaconnect-bridgeoutput-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.mediaconnect.BridgeOutput:
        from troposphere.mediaconnect import BridgeOutput as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediaconnect import BridgeOutput as TropoT
        return resource_to_troposphere(self, TropoT)


class BridgeSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html
    Properties:
        - Name: NetworkSource
        - Name: BridgeArn
        - Name: FlowSource
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NetworkSource_: Optional['BridgeNetworkSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html#cfn-mediaconnect-bridgesource-networksource""", alias="NetworkSource")
    BridgeArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html#cfn-mediaconnect-bridgesource-bridgearn""", alias="BridgeArn")
    FlowSource_: Optional['BridgeFlowSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html#cfn-mediaconnect-bridgesource-flowsource""", alias="FlowSource")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html#cfn-mediaconnect-bridgesource-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.mediaconnect.BridgeSource:
        from troposphere.mediaconnect import BridgeSource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediaconnect import BridgeSource as TropoT
        return resource_to_troposphere(self, TropoT)


class Flow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html
    Properties:
        - Name: SourceFailoverConfig
        - Name: AvailabilityZone
        - Name: Source
        - Name: Name
    Attributes:
        - Name: FlowAvailabilityZone
        - Name: Source.SourceIngestPort
        - Name: Source.IngestIp
        - Name: Source.SourceArn
        - Name: FlowArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SourceFailoverConfig_: Optional['FailoverConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-sourcefailoverconfig""", alias="SourceFailoverConfig")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-availabilityzone""", alias="AvailabilityZone")
    Source_: 'Source' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-source""", alias="Source")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.mediaconnect.Flow:
        from troposphere.mediaconnect import Flow as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediaconnect import Flow as TropoT
        return resource_to_troposphere(self, TropoT)


class FlowEntitlement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html
    Properties:
        - Name: DataTransferSubscriberFeePercent
        - Name: Description
        - Name: Encryption
        - Name: Subscribers
        - Name: FlowArn
        - Name: EntitlementStatus
        - Name: Name
    Attributes:
        - Name: EntitlementArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DataTransferSubscriberFeePercent_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-datatransfersubscriberfeepercent""", alias="DataTransferSubscriberFeePercent")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-description""", alias="Description")
    Encryption_: Optional['Encryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-encryption""", alias="Encryption")
    Subscribers_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-subscribers""", alias="Subscribers")
    FlowArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-flowarn""", alias="FlowArn")
    EntitlementStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-entitlementstatus""", alias="EntitlementStatus")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.mediaconnect.FlowEntitlement:
        from troposphere.mediaconnect import FlowEntitlement as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediaconnect import FlowEntitlement as TropoT
        return resource_to_troposphere(self, TropoT)


class FlowOutput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html
    Properties:
        - Name: Destination
        - Name: SmoothingLatency
        - Name: StreamId
        - Name: Description
        - Name: Port
        - Name: RemoteId
        - Name: Encryption
        - Name: Name
        - Name: VpcInterfaceAttachment
        - Name: MinLatency
        - Name: Protocol
        - Name: FlowArn
        - Name: MaxLatency
        - Name: CidrAllowList
    Attributes:
        - Name: OutputArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Destination_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-destination""", alias="Destination")
    SmoothingLatency_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-smoothinglatency""", alias="SmoothingLatency")
    StreamId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-streamid""", alias="StreamId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-description""", alias="Description")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-port""", alias="Port")
    RemoteId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-remoteid""", alias="RemoteId")
    Encryption_: Optional['Encryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-encryption""", alias="Encryption")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-name""", alias="Name")
    VpcInterfaceAttachment_: Optional['VpcInterfaceAttachment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-vpcinterfaceattachment""", alias="VpcInterfaceAttachment")
    MinLatency_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-minlatency""", alias="MinLatency")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-protocol""", alias="Protocol")
    FlowArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-flowarn""", alias="FlowArn")
    MaxLatency_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-maxlatency""", alias="MaxLatency")
    CidrAllowList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-cidrallowlist""", alias="CidrAllowList")
    

    @property
    def tropo_type(self) -> troposphere.mediaconnect.FlowOutput:
        from troposphere.mediaconnect import FlowOutput as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediaconnect import FlowOutput as TropoT
        return resource_to_troposphere(self, TropoT)


class FlowSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html
    Properties:
        - Name: StreamId
        - Name: Description
        - Name: SenderIpAddress
        - Name: IngestPort
        - Name: SenderControlPort
        - Name: Decryption
        - Name: GatewayBridgeSource
        - Name: SourceListenerAddress
        - Name: SourceListenerPort
        - Name: Name
        - Name: WhitelistCidr
        - Name: EntitlementArn
        - Name: MinLatency
        - Name: VpcInterfaceName
        - Name: MaxBitrate
        - Name: Protocol
        - Name: FlowArn
        - Name: MaxLatency
    Attributes:
        - Name: IngestIp
        - Name: SourceArn
        - Name: SourceIngestPort
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StreamId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-streamid""", alias="StreamId")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-description""", alias="Description")
    SenderIpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-senderipaddress""", alias="SenderIpAddress")
    IngestPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-ingestport""", alias="IngestPort")
    SenderControlPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-sendercontrolport""", alias="SenderControlPort")
    Decryption_: Optional['Encryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-decryption""", alias="Decryption")
    GatewayBridgeSource_: Optional['GatewayBridgeSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-gatewaybridgesource""", alias="GatewayBridgeSource")
    SourceListenerAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-sourcelisteneraddress""", alias="SourceListenerAddress")
    SourceListenerPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-sourcelistenerport""", alias="SourceListenerPort")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-name""", alias="Name")
    WhitelistCidr_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-whitelistcidr""", alias="WhitelistCidr")
    EntitlementArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-entitlementarn""", alias="EntitlementArn")
    MinLatency_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-minlatency""", alias="MinLatency")
    VpcInterfaceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-vpcinterfacename""", alias="VpcInterfaceName")
    MaxBitrate_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-maxbitrate""", alias="MaxBitrate")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-protocol""", alias="Protocol")
    FlowArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-flowarn""", alias="FlowArn")
    MaxLatency_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-maxlatency""", alias="MaxLatency")
    

    @property
    def tropo_type(self) -> troposphere.mediaconnect.FlowSource:
        from troposphere.mediaconnect import FlowSource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediaconnect import FlowSource as TropoT
        return resource_to_troposphere(self, TropoT)


class FlowVpcInterface(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html
    Properties:
        - Name: SubnetId
        - Name: FlowArn
        - Name: SecurityGroupIds
        - Name: RoleArn
        - Name: Name
    Attributes:
        - Name: NetworkInterfaceIds
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-subnetid""", alias="SubnetId")
    FlowArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-flowarn""", alias="FlowArn")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-securitygroupids""", alias="SecurityGroupIds")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-rolearn""", alias="RoleArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.mediaconnect.FlowVpcInterface:
        from troposphere.mediaconnect import FlowVpcInterface as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediaconnect import FlowVpcInterface as TropoT
        return resource_to_troposphere(self, TropoT)


class Gateway(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html
    Properties:
        - Name: Networks
        - Name: EgressCidrBlocks
        - Name: Name
    Attributes:
        - Name: GatewayArn
        - Name: GatewayState
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Networks_: List['GatewayNetwork'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html#cfn-mediaconnect-gateway-networks""", alias="Networks")
    EgressCidrBlocks_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html#cfn-mediaconnect-gateway-egresscidrblocks""", alias="EgressCidrBlocks")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html#cfn-mediaconnect-gateway-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.mediaconnect.Gateway:
        from troposphere.mediaconnect import Gateway as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.mediaconnect import Gateway as TropoT
        return resource_to_troposphere(self, TropoT)

