from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ConnectAttachmentOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-connectattachmentoptions.html
    Properties:
        - Name: Protocol
    
    """
    
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-connectattachmentoptions.html#cfn-networkmanager-connectattachment-connectattachmentoptions-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.ConnectAttachmentOptions:
        from troposphere.networkmanager import ConnectAttachmentOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProposedSegmentChange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-proposedsegmentchange.html
    Properties:
        - Name: SegmentName
        - Name: Tags
        - Name: AttachmentPolicyRuleNumber
    
    """
    
    SegmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-proposedsegmentchange.html#cfn-networkmanager-connectattachment-proposedsegmentchange-segmentname""", alias="SegmentName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-proposedsegmentchange.html#cfn-networkmanager-connectattachment-proposedsegmentchange-tags""", alias="Tags")
    AttachmentPolicyRuleNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-proposedsegmentchange.html#cfn-networkmanager-connectattachment-proposedsegmentchange-attachmentpolicyrulenumber""", alias="AttachmentPolicyRuleNumber")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.ProposedSegmentChange:
        from troposphere.networkmanager import ProposedSegmentChange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BgpOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-bgpoptions.html
    Properties:
        - Name: PeerAsn
    
    """
    
    PeerAsn_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-bgpoptions.html#cfn-networkmanager-connectpeer-bgpoptions-peerasn""", alias="PeerAsn")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.BgpOptions:
        from troposphere.networkmanager import BgpOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectPeerBgpConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration.html
    Properties:
        - Name: PeerAddress
        - Name: CoreNetworkAddress
        - Name: PeerAsn
        - Name: CoreNetworkAsn
    
    """
    
    PeerAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration.html#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-peeraddress""", alias="PeerAddress")
    CoreNetworkAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration.html#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-corenetworkaddress""", alias="CoreNetworkAddress")
    PeerAsn_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration.html#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-peerasn""", alias="PeerAsn")
    CoreNetworkAsn_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration.html#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-corenetworkasn""", alias="CoreNetworkAsn")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.ConnectPeerBgpConfiguration:
        from troposphere.networkmanager import ConnectPeerBgpConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectPeerConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerconfiguration.html
    Properties:
        - Name: BgpConfigurations
        - Name: PeerAddress
        - Name: CoreNetworkAddress
        - Name: InsideCidrBlocks
        - Name: Protocol
    
    """
    
    BgpConfigurations_: Optional[List['ConnectPeerBgpConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerconfiguration.html#cfn-networkmanager-connectpeer-connectpeerconfiguration-bgpconfigurations""", alias="BgpConfigurations")
    PeerAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerconfiguration.html#cfn-networkmanager-connectpeer-connectpeerconfiguration-peeraddress""", alias="PeerAddress")
    CoreNetworkAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerconfiguration.html#cfn-networkmanager-connectpeer-connectpeerconfiguration-corenetworkaddress""", alias="CoreNetworkAddress")
    InsideCidrBlocks_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerconfiguration.html#cfn-networkmanager-connectpeer-connectpeerconfiguration-insidecidrblocks""", alias="InsideCidrBlocks")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerconfiguration.html#cfn-networkmanager-connectpeer-connectpeerconfiguration-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.ConnectPeerConfiguration:
        from troposphere.networkmanager import ConnectPeerConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CoreNetworkEdge(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html
    Properties:
        - Name: InsideCidrBlocks
        - Name: Asn
        - Name: EdgeLocation
    
    """
    
    InsideCidrBlocks_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html#cfn-networkmanager-corenetwork-corenetworkedge-insidecidrblocks""", alias="InsideCidrBlocks")
    Asn_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html#cfn-networkmanager-corenetwork-corenetworkedge-asn""", alias="Asn")
    EdgeLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html#cfn-networkmanager-corenetwork-corenetworkedge-edgelocation""", alias="EdgeLocation")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.CoreNetworkEdge:
        from troposphere.networkmanager import CoreNetworkEdge as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CoreNetworkSegment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html
    Properties:
        - Name: EdgeLocations
        - Name: SharedSegments
        - Name: Name
    
    """
    
    EdgeLocations_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html#cfn-networkmanager-corenetwork-corenetworksegment-edgelocations""", alias="EdgeLocations")
    SharedSegments_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html#cfn-networkmanager-corenetwork-corenetworksegment-sharedsegments""", alias="SharedSegments")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html#cfn-networkmanager-corenetwork-corenetworksegment-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.CoreNetworkSegment:
        from troposphere.networkmanager import CoreNetworkSegment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AWSLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-awslocation.html
    Properties:
        - Name: Zone
        - Name: SubnetArn
    
    """
    
    Zone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-awslocation.html#cfn-networkmanager-device-awslocation-zone""", alias="Zone")
    SubnetArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-awslocation.html#cfn-networkmanager-device-awslocation-subnetarn""", alias="SubnetArn")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.AWSLocation:
        from troposphere.networkmanager import AWSLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html
    Properties:
        - Name: Address
        - Name: Latitude
        - Name: Longitude
    
    """
    
    Address_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-address""", alias="Address")
    Latitude_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-latitude""", alias="Latitude")
    Longitude_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-longitude""", alias="Longitude")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.Location:
        from troposphere.networkmanager import Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Bandwidth(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html
    Properties:
        - Name: DownloadSpeed
        - Name: UploadSpeed
    
    """
    
    DownloadSpeed_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-downloadspeed""", alias="DownloadSpeed")
    UploadSpeed_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-uploadspeed""", alias="UploadSpeed")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.Bandwidth:
        from troposphere.networkmanager import Bandwidth as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html
    Properties:
        - Name: Address
        - Name: Latitude
        - Name: Longitude
    
    """
    
    Address_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-address""", alias="Address")
    Latitude_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-latitude""", alias="Latitude")
    Longitude_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-longitude""", alias="Longitude")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.Location:
        from troposphere.networkmanager import Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProposedSegmentChange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-sitetositevpnattachment-proposedsegmentchange.html
    Properties:
        - Name: SegmentName
        - Name: Tags
        - Name: AttachmentPolicyRuleNumber
    
    """
    
    SegmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-sitetositevpnattachment-proposedsegmentchange.html#cfn-networkmanager-sitetositevpnattachment-proposedsegmentchange-segmentname""", alias="SegmentName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-sitetositevpnattachment-proposedsegmentchange.html#cfn-networkmanager-sitetositevpnattachment-proposedsegmentchange-tags""", alias="Tags")
    AttachmentPolicyRuleNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-sitetositevpnattachment-proposedsegmentchange.html#cfn-networkmanager-sitetositevpnattachment-proposedsegmentchange-attachmentpolicyrulenumber""", alias="AttachmentPolicyRuleNumber")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.ProposedSegmentChange:
        from troposphere.networkmanager import ProposedSegmentChange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProposedSegmentChange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange.html
    Properties:
        - Name: SegmentName
        - Name: Tags
        - Name: AttachmentPolicyRuleNumber
    
    """
    
    SegmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange.html#cfn-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange-segmentname""", alias="SegmentName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange.html#cfn-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange-tags""", alias="Tags")
    AttachmentPolicyRuleNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange.html#cfn-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange-attachmentpolicyrulenumber""", alias="AttachmentPolicyRuleNumber")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.ProposedSegmentChange:
        from troposphere.networkmanager import ProposedSegmentChange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProposedSegmentChange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-proposedsegmentchange.html
    Properties:
        - Name: SegmentName
        - Name: Tags
        - Name: AttachmentPolicyRuleNumber
    
    """
    
    SegmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-proposedsegmentchange.html#cfn-networkmanager-vpcattachment-proposedsegmentchange-segmentname""", alias="SegmentName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-proposedsegmentchange.html#cfn-networkmanager-vpcattachment-proposedsegmentchange-tags""", alias="Tags")
    AttachmentPolicyRuleNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-proposedsegmentchange.html#cfn-networkmanager-vpcattachment-proposedsegmentchange-attachmentpolicyrulenumber""", alias="AttachmentPolicyRuleNumber")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.ProposedSegmentChange:
        from troposphere.networkmanager import ProposedSegmentChange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-vpcoptions.html
    Properties:
        - Name: Ipv6Support
        - Name: ApplianceModeSupport
    
    """
    
    Ipv6Support_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-vpcoptions.html#cfn-networkmanager-vpcattachment-vpcoptions-ipv6support""", alias="Ipv6Support")
    ApplianceModeSupport_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-vpcoptions.html#cfn-networkmanager-vpcattachment-vpcoptions-appliancemodesupport""", alias="ApplianceModeSupport")
    


    @property
    def tropo_type(self) -> troposphere.networkmanager.VpcOptions:
        from troposphere.networkmanager import VpcOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ConnectAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html
    Properties:
        - Name: ProposedSegmentChange
        - Name: Options
        - Name: TransportAttachmentId
        - Name: CoreNetworkId
        - Name: Tags
        - Name: EdgeLocation
    Attributes:
        - Name: ResourceArn
        - Name: AttachmentType
        - Name: SegmentName
        - Name: State
        - Name: CreatedAt
        - Name: OwnerAccountId
        - Name: UpdatedAt
        - Name: AttachmentId
        - Name: CoreNetworkArn
        - Name: AttachmentPolicyRuleNumber
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ProposedSegmentChange_: Optional['ProposedSegmentChange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-proposedsegmentchange""", alias="ProposedSegmentChange")
    Options_: 'ConnectAttachmentOptions' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-options""", alias="Options")
    TransportAttachmentId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-transportattachmentid""", alias="TransportAttachmentId")
    CoreNetworkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-corenetworkid""", alias="CoreNetworkId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-tags""", alias="Tags")
    EdgeLocation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-edgelocation""", alias="EdgeLocation")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.ConnectAttachment:
        from troposphere.networkmanager import ConnectAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import ConnectAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class ConnectPeer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html
    Properties:
        - Name: ConnectAttachmentId
        - Name: PeerAddress
        - Name: SubnetArn
        - Name: CoreNetworkAddress
        - Name: BgpOptions
        - Name: InsideCidrBlocks
        - Name: Tags
    Attributes:
        - Name: Configuration.BgpConfigurations
        - Name: CoreNetworkId
        - Name: Configuration.InsideCidrBlocks
        - Name: Configuration
        - Name: State
        - Name: CreatedAt
        - Name: ConnectPeerId
        - Name: Configuration.CoreNetworkAddress
        - Name: Configuration.Protocol
        - Name: Configuration.PeerAddress
        - Name: EdgeLocation
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConnectAttachmentId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-connectattachmentid""", alias="ConnectAttachmentId")
    PeerAddress_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-peeraddress""", alias="PeerAddress")
    SubnetArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-subnetarn""", alias="SubnetArn")
    CoreNetworkAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-corenetworkaddress""", alias="CoreNetworkAddress")
    BgpOptions_: Optional['BgpOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-bgpoptions""", alias="BgpOptions")
    InsideCidrBlocks_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-insidecidrblocks""", alias="InsideCidrBlocks")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.ConnectPeer:
        from troposphere.networkmanager import ConnectPeer as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import ConnectPeer as TropoT
        return resource_to_troposphere(self, TropoT)


class CoreNetwork(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html
    Properties:
        - Name: GlobalNetworkId
        - Name: Description
        - Name: PolicyDocument
        - Name: Tags
    Attributes:
        - Name: CoreNetworkId
        - Name: State
        - Name: CreatedAt
        - Name: Segments
        - Name: OwnerAccount
        - Name: Edges
        - Name: CoreNetworkArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GlobalNetworkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-globalnetworkid""", alias="GlobalNetworkId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-description""", alias="Description")
    PolicyDocument_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-policydocument""", alias="PolicyDocument")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.CoreNetwork:
        from troposphere.networkmanager import CoreNetwork as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import CoreNetwork as TropoT
        return resource_to_troposphere(self, TropoT)


class CustomerGatewayAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html
    Properties:
        - Name: GlobalNetworkId
        - Name: DeviceId
        - Name: CustomerGatewayArn
        - Name: LinkId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GlobalNetworkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-globalnetworkid""", alias="GlobalNetworkId")
    DeviceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-deviceid""", alias="DeviceId")
    CustomerGatewayArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-customergatewayarn""", alias="CustomerGatewayArn")
    LinkId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-linkid""", alias="LinkId")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.CustomerGatewayAssociation:
        from troposphere.networkmanager import CustomerGatewayAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import CustomerGatewayAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class Device(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html
    Properties:
        - Name: SiteId
        - Name: AWSLocation
        - Name: Type
        - Name: Description
        - Name: GlobalNetworkId
        - Name: SerialNumber
        - Name: Model
        - Name: Vendor
        - Name: Tags
        - Name: Location
    Attributes:
        - Name: DeviceArn
        - Name: DeviceId
        - Name: State
        - Name: CreatedAt
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SiteId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-siteid""", alias="SiteId")
    AWSLocation_: Optional['AWSLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-awslocation""", alias="AWSLocation")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-description""", alias="Description")
    GlobalNetworkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-globalnetworkid""", alias="GlobalNetworkId")
    SerialNumber_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-serialnumber""", alias="SerialNumber")
    Model_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-model""", alias="Model")
    Vendor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-vendor""", alias="Vendor")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-tags""", alias="Tags")
    Location_: Optional['Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-location""", alias="Location")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.Device:
        from troposphere.networkmanager import Device as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import Device as TropoT
        return resource_to_troposphere(self, TropoT)


class GlobalNetwork(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html
    Properties:
        - Name: Description
        - Name: State
        - Name: CreatedAt
        - Name: Tags
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-description""", alias="Description")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-state""", alias="State")
    CreatedAt_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-createdat""", alias="CreatedAt")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.GlobalNetwork:
        from troposphere.networkmanager import GlobalNetwork as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import GlobalNetwork as TropoT
        return resource_to_troposphere(self, TropoT)


class Link(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html
    Properties:
        - Name: SiteId
        - Name: Type
        - Name: GlobalNetworkId
        - Name: Description
        - Name: Bandwidth
        - Name: Tags
        - Name: Provider
    Attributes:
        - Name: LinkArn
        - Name: State
        - Name: CreatedAt
        - Name: LinkId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SiteId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-siteid""", alias="SiteId")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-type""", alias="Type")
    GlobalNetworkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-globalnetworkid""", alias="GlobalNetworkId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-description""", alias="Description")
    Bandwidth_: 'Bandwidth' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-bandwidth""", alias="Bandwidth")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-tags""", alias="Tags")
    Provider_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-provider""", alias="Provider")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.Link:
        from troposphere.networkmanager import Link as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import Link as TropoT
        return resource_to_troposphere(self, TropoT)


class LinkAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html
    Properties:
        - Name: GlobalNetworkId
        - Name: DeviceId
        - Name: LinkId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GlobalNetworkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-globalnetworkid""", alias="GlobalNetworkId")
    DeviceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-deviceid""", alias="DeviceId")
    LinkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-linkid""", alias="LinkId")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.LinkAssociation:
        from troposphere.networkmanager import LinkAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import LinkAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class Site(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html
    Properties:
        - Name: Description
        - Name: GlobalNetworkId
        - Name: Tags
        - Name: Location
    Attributes:
        - Name: SiteId
        - Name: SiteArn
        - Name: State
        - Name: CreatedAt
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-description""", alias="Description")
    GlobalNetworkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-globalnetworkid""", alias="GlobalNetworkId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-tags""", alias="Tags")
    Location_: Optional['Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-location""", alias="Location")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.Site:
        from troposphere.networkmanager import Site as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import Site as TropoT
        return resource_to_troposphere(self, TropoT)


class SiteToSiteVpnAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html
    Properties:
        - Name: ProposedSegmentChange
        - Name: CoreNetworkId
        - Name: VpnConnectionArn
        - Name: Tags
    Attributes:
        - Name: ResourceArn
        - Name: AttachmentType
        - Name: SegmentName
        - Name: State
        - Name: CreatedAt
        - Name: OwnerAccountId
        - Name: UpdatedAt
        - Name: AttachmentId
        - Name: CoreNetworkArn
        - Name: EdgeLocation
        - Name: AttachmentPolicyRuleNumber
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ProposedSegmentChange_: Optional['ProposedSegmentChange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-proposedsegmentchange""", alias="ProposedSegmentChange")
    CoreNetworkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-corenetworkid""", alias="CoreNetworkId")
    VpnConnectionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-vpnconnectionarn""", alias="VpnConnectionArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.SiteToSiteVpnAttachment:
        from troposphere.networkmanager import SiteToSiteVpnAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import SiteToSiteVpnAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayPeering(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewaypeering.html
    Properties:
        - Name: CoreNetworkId
        - Name: TransitGatewayArn
        - Name: Tags
    Attributes:
        - Name: ResourceArn
        - Name: PeeringType
        - Name: State
        - Name: CreatedAt
        - Name: PeeringId
        - Name: TransitGatewayPeeringAttachmentId
        - Name: OwnerAccountId
        - Name: CoreNetworkArn
        - Name: EdgeLocation
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CoreNetworkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewaypeering.html#cfn-networkmanager-transitgatewaypeering-corenetworkid""", alias="CoreNetworkId")
    TransitGatewayArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewaypeering.html#cfn-networkmanager-transitgatewaypeering-transitgatewayarn""", alias="TransitGatewayArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewaypeering.html#cfn-networkmanager-transitgatewaypeering-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.TransitGatewayPeering:
        from troposphere.networkmanager import TransitGatewayPeering as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import TransitGatewayPeering as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayRegistration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html
    Properties:
        - Name: GlobalNetworkId
        - Name: TransitGatewayArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GlobalNetworkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-globalnetworkid""", alias="GlobalNetworkId")
    TransitGatewayArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-transitgatewayarn""", alias="TransitGatewayArn")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.TransitGatewayRegistration:
        from troposphere.networkmanager import TransitGatewayRegistration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import TransitGatewayRegistration as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayRouteTableAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayroutetableattachment.html
    Properties:
        - Name: ProposedSegmentChange
        - Name: TransitGatewayRouteTableArn
        - Name: PeeringId
        - Name: Tags
    Attributes:
        - Name: ResourceArn
        - Name: CoreNetworkId
        - Name: AttachmentType
        - Name: SegmentName
        - Name: State
        - Name: CreatedAt
        - Name: OwnerAccountId
        - Name: UpdatedAt
        - Name: AttachmentId
        - Name: CoreNetworkArn
        - Name: EdgeLocation
        - Name: AttachmentPolicyRuleNumber
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ProposedSegmentChange_: Optional['ProposedSegmentChange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayroutetableattachment.html#cfn-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange""", alias="ProposedSegmentChange")
    TransitGatewayRouteTableArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayroutetableattachment.html#cfn-networkmanager-transitgatewayroutetableattachment-transitgatewayroutetablearn""", alias="TransitGatewayRouteTableArn")
    PeeringId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayroutetableattachment.html#cfn-networkmanager-transitgatewayroutetableattachment-peeringid""", alias="PeeringId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayroutetableattachment.html#cfn-networkmanager-transitgatewayroutetableattachment-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.TransitGatewayRouteTableAttachment:
        from troposphere.networkmanager import TransitGatewayRouteTableAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import TransitGatewayRouteTableAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class VpcAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html
    Properties:
        - Name: ProposedSegmentChange
        - Name: SubnetArns
        - Name: Options
        - Name: CoreNetworkId
        - Name: VpcArn
        - Name: Tags
    Attributes:
        - Name: ResourceArn
        - Name: AttachmentType
        - Name: SegmentName
        - Name: State
        - Name: CreatedAt
        - Name: OwnerAccountId
        - Name: UpdatedAt
        - Name: AttachmentId
        - Name: CoreNetworkArn
        - Name: EdgeLocation
        - Name: AttachmentPolicyRuleNumber
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ProposedSegmentChange_: Optional['ProposedSegmentChange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-proposedsegmentchange""", alias="ProposedSegmentChange")
    SubnetArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-subnetarns""", alias="SubnetArns")
    Options_: Optional['VpcOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-options""", alias="Options")
    CoreNetworkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-corenetworkid""", alias="CoreNetworkId")
    VpcArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-vpcarn""", alias="VpcArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.networkmanager.VpcAttachment:
        from troposphere.networkmanager import VpcAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkmanager import VpcAttachment as TropoT
        return resource_to_troposphere(self, TropoT)

