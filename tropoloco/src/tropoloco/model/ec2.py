from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class TagSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservation-tagspecification.html
    Properties:
        - Name: ResourceType
        - Name: Tags
    
    """
    
    ResourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservation-tagspecification.html#cfn-ec2-capacityreservation-tagspecification-resourcetype""", alias="ResourceType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservation-tagspecification.html#cfn-ec2-capacityreservation-tagspecification-tags""", alias="Tags")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TagSpecifications:
        from troposphere.ec2 import TagSpecifications as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceTypeSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservationfleet-instancetypespecification.html
    Properties:
        - Name: Priority
        - Name: AvailabilityZoneId
        - Name: AvailabilityZone
        - Name: InstancePlatform
        - Name: InstanceType
        - Name: Weight
        - Name: EbsOptimized
    
    """
    
    Priority_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservationfleet-instancetypespecification.html#cfn-ec2-capacityreservationfleet-instancetypespecification-priority""", alias="Priority")
    AvailabilityZoneId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservationfleet-instancetypespecification.html#cfn-ec2-capacityreservationfleet-instancetypespecification-availabilityzoneid""", alias="AvailabilityZoneId")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservationfleet-instancetypespecification.html#cfn-ec2-capacityreservationfleet-instancetypespecification-availabilityzone""", alias="AvailabilityZone")
    InstancePlatform_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservationfleet-instancetypespecification.html#cfn-ec2-capacityreservationfleet-instancetypespecification-instanceplatform""", alias="InstancePlatform")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservationfleet-instancetypespecification.html#cfn-ec2-capacityreservationfleet-instancetypespecification-instancetype""", alias="InstanceType")
    Weight_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservationfleet-instancetypespecification.html#cfn-ec2-capacityreservationfleet-instancetypespecification-weight""", alias="Weight")
    EbsOptimized_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservationfleet-instancetypespecification.html#cfn-ec2-capacityreservationfleet-instancetypespecification-ebsoptimized""", alias="EbsOptimized")
    


    @property
    def tropo_type(self) -> troposphere.ec2.InstanceTypeSpecification:
        from troposphere.ec2 import InstanceTypeSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservationfleet-tagspecification.html
    Properties:
        - Name: ResourceType
        - Name: Tags
    
    """
    
    ResourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservationfleet-tagspecification.html#cfn-ec2-capacityreservationfleet-tagspecification-resourcetype""", alias="ResourceType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservationfleet-tagspecification.html#cfn-ec2-capacityreservationfleet-tagspecification-tags""", alias="Tags")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TagSpecifications:
        from troposphere.ec2 import TagSpecifications as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CertificateAuthenticationRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-certificateauthenticationrequest.html
    Properties:
        - Name: ClientRootCertificateChainArn
    
    """
    
    ClientRootCertificateChainArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-certificateauthenticationrequest.html#cfn-ec2-clientvpnendpoint-certificateauthenticationrequest-clientrootcertificatechainarn""", alias="ClientRootCertificateChainArn")
    


    @property
    def tropo_type(self) -> troposphere.ec2.CertificateAuthenticationRequest:
        from troposphere.ec2 import CertificateAuthenticationRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClientAuthenticationRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientauthenticationrequest.html
    Properties:
        - Name: MutualAuthentication
        - Name: Type
        - Name: FederatedAuthentication
        - Name: ActiveDirectory
    
    """
    
    MutualAuthentication_: Optional['CertificateAuthenticationRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientauthenticationrequest.html#cfn-ec2-clientvpnendpoint-clientauthenticationrequest-mutualauthentication""", alias="MutualAuthentication")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientauthenticationrequest.html#cfn-ec2-clientvpnendpoint-clientauthenticationrequest-type""", alias="Type")
    FederatedAuthentication_: Optional['FederatedAuthenticationRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientauthenticationrequest.html#cfn-ec2-clientvpnendpoint-clientauthenticationrequest-federatedauthentication""", alias="FederatedAuthentication")
    ActiveDirectory_: Optional['DirectoryServiceAuthenticationRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientauthenticationrequest.html#cfn-ec2-clientvpnendpoint-clientauthenticationrequest-activedirectory""", alias="ActiveDirectory")
    


    @property
    def tropo_type(self) -> troposphere.ec2.ClientAuthenticationRequest:
        from troposphere.ec2 import ClientAuthenticationRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClientConnectOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientconnectoptions.html
    Properties:
        - Name: LambdaFunctionArn
        - Name: Enabled
    
    """
    
    LambdaFunctionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientconnectoptions.html#cfn-ec2-clientvpnendpoint-clientconnectoptions-lambdafunctionarn""", alias="LambdaFunctionArn")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientconnectoptions.html#cfn-ec2-clientvpnendpoint-clientconnectoptions-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.ec2.ClientConnectOptions:
        from troposphere.ec2 import ClientConnectOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClientLoginBannerOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientloginbanneroptions.html
    Properties:
        - Name: Enabled
        - Name: BannerText
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientloginbanneroptions.html#cfn-ec2-clientvpnendpoint-clientloginbanneroptions-enabled""", alias="Enabled")
    BannerText_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientloginbanneroptions.html#cfn-ec2-clientvpnendpoint-clientloginbanneroptions-bannertext""", alias="BannerText")
    


    @property
    def tropo_type(self) -> troposphere.ec2.ClientLoginBannerOptions:
        from troposphere.ec2 import ClientLoginBannerOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectionLogOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-connectionlogoptions.html
    Properties:
        - Name: CloudwatchLogStream
        - Name: Enabled
        - Name: CloudwatchLogGroup
    
    """
    
    CloudwatchLogStream_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-connectionlogoptions.html#cfn-ec2-clientvpnendpoint-connectionlogoptions-cloudwatchlogstream""", alias="CloudwatchLogStream")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-connectionlogoptions.html#cfn-ec2-clientvpnendpoint-connectionlogoptions-enabled""", alias="Enabled")
    CloudwatchLogGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-connectionlogoptions.html#cfn-ec2-clientvpnendpoint-connectionlogoptions-cloudwatchloggroup""", alias="CloudwatchLogGroup")
    


    @property
    def tropo_type(self) -> troposphere.ec2.ConnectionLogOptions:
        from troposphere.ec2 import ConnectionLogOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DirectoryServiceAuthenticationRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-directoryserviceauthenticationrequest.html
    Properties:
        - Name: DirectoryId
    
    """
    
    DirectoryId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-directoryserviceauthenticationrequest.html#cfn-ec2-clientvpnendpoint-directoryserviceauthenticationrequest-directoryid""", alias="DirectoryId")
    


    @property
    def tropo_type(self) -> troposphere.ec2.DirectoryServiceAuthenticationRequest:
        from troposphere.ec2 import DirectoryServiceAuthenticationRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FederatedAuthenticationRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-federatedauthenticationrequest.html
    Properties:
        - Name: SelfServiceSAMLProviderArn
        - Name: SAMLProviderArn
    
    """
    
    SelfServiceSAMLProviderArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-federatedauthenticationrequest.html#cfn-ec2-clientvpnendpoint-federatedauthenticationrequest-selfservicesamlproviderarn""", alias="SelfServiceSAMLProviderArn")
    SAMLProviderArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-federatedauthenticationrequest.html#cfn-ec2-clientvpnendpoint-federatedauthenticationrequest-samlproviderarn""", alias="SAMLProviderArn")
    


    @property
    def tropo_type(self) -> troposphere.ec2.FederatedAuthenticationRequest:
        from troposphere.ec2 import FederatedAuthenticationRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-tagspecification.html
    Properties:
        - Name: ResourceType
        - Name: Tags
    
    """
    
    ResourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-tagspecification.html#cfn-ec2-clientvpnendpoint-tagspecification-resourcetype""", alias="ResourceType")
    Tags_: List['Tag'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-tagspecification.html#cfn-ec2-clientvpnendpoint-tagspecification-tags""", alias="Tags")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TagSpecifications:
        from troposphere.ec2 import TagSpecifications as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AcceleratorCountRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-acceleratorcountrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-acceleratorcountrequest.html#cfn-ec2-ec2fleet-acceleratorcountrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-acceleratorcountrequest.html#cfn-ec2-ec2fleet-acceleratorcountrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AcceleratorCountRequest:
        from troposphere.ec2 import AcceleratorCountRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AcceleratorTotalMemoryMiBRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-acceleratortotalmemorymibrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-acceleratortotalmemorymibrequest.html#cfn-ec2-ec2fleet-acceleratortotalmemorymibrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-acceleratortotalmemorymibrequest.html#cfn-ec2-ec2fleet-acceleratortotalmemorymibrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AcceleratorTotalMemoryMiBRequest:
        from troposphere.ec2 import AcceleratorTotalMemoryMiBRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BaselineEbsBandwidthMbpsRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-baselineebsbandwidthmbpsrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-baselineebsbandwidthmbpsrequest.html#cfn-ec2-ec2fleet-baselineebsbandwidthmbpsrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-baselineebsbandwidthmbpsrequest.html#cfn-ec2-ec2fleet-baselineebsbandwidthmbpsrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.BaselineEbsBandwidthMbpsRequest:
        from troposphere.ec2 import BaselineEbsBandwidthMbpsRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacityRebalance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-capacityrebalance.html
    Properties:
        - Name: TerminationDelay
        - Name: ReplacementStrategy
    
    """
    
    TerminationDelay_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-capacityrebalance.html#cfn-ec2-ec2fleet-capacityrebalance-terminationdelay""", alias="TerminationDelay")
    ReplacementStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-capacityrebalance.html#cfn-ec2-ec2fleet-capacityrebalance-replacementstrategy""", alias="ReplacementStrategy")
    


    @property
    def tropo_type(self) -> troposphere.ec2.CapacityRebalance:
        from troposphere.ec2 import CapacityRebalance as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacityReservationOptionsRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-capacityreservationoptionsrequest.html
    Properties:
        - Name: UsageStrategy
    
    """
    
    UsageStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-capacityreservationoptionsrequest.html#cfn-ec2-ec2fleet-capacityreservationoptionsrequest-usagestrategy""", alias="UsageStrategy")
    


    @property
    def tropo_type(self) -> troposphere.ec2.CapacityReservationOptionsRequest:
        from troposphere.ec2 import CapacityReservationOptionsRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FleetLaunchTemplateConfigRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest.html
    Properties:
        - Name: LaunchTemplateSpecification
        - Name: Overrides
    
    """
    
    LaunchTemplateSpecification_: Optional['FleetLaunchTemplateSpecificationRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-launchtemplatespecification""", alias="LaunchTemplateSpecification")
    Overrides_: Optional[List['FleetLaunchTemplateOverridesRequest']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-overrides""", alias="Overrides")
    


    @property
    def tropo_type(self) -> troposphere.ec2.FleetLaunchTemplateConfigRequest:
        from troposphere.ec2 import FleetLaunchTemplateConfigRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FleetLaunchTemplateOverridesRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html
    Properties:
        - Name: WeightedCapacity
        - Name: Placement
        - Name: Priority
        - Name: AvailabilityZone
        - Name: SubnetId
        - Name: InstanceRequirements
        - Name: InstanceType
        - Name: MaxPrice
    
    """
    
    WeightedCapacity_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-weightedcapacity""", alias="WeightedCapacity")
    Placement_: Optional['Placement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-placement""", alias="Placement")
    Priority_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-priority""", alias="Priority")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-availabilityzone""", alias="AvailabilityZone")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-subnetid""", alias="SubnetId")
    InstanceRequirements_: Optional['InstanceRequirementsRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-instancerequirements""", alias="InstanceRequirements")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-instancetype""", alias="InstanceType")
    MaxPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-maxprice""", alias="MaxPrice")
    


    @property
    def tropo_type(self) -> troposphere.ec2.FleetLaunchTemplateOverridesRequest:
        from troposphere.ec2 import FleetLaunchTemplateOverridesRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FleetLaunchTemplateSpecificationRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html
    Properties:
        - Name: LaunchTemplateName
        - Name: Version
        - Name: LaunchTemplateId
    
    """
    
    LaunchTemplateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplatename""", alias="LaunchTemplateName")
    Version_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-version""", alias="Version")
    LaunchTemplateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplateid""", alias="LaunchTemplateId")
    


    @property
    def tropo_type(self) -> troposphere.ec2.FleetLaunchTemplateSpecificationRequest:
        from troposphere.ec2 import FleetLaunchTemplateSpecificationRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceRequirementsRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html
    Properties:
        - Name: LocalStorageTypes
        - Name: InstanceGenerations
        - Name: NetworkInterfaceCount
        - Name: MemoryGiBPerVCpu
        - Name: AcceleratorTypes
        - Name: VCpuCount
        - Name: ExcludedInstanceTypes
        - Name: AcceleratorManufacturers
        - Name: AllowedInstanceTypes
        - Name: LocalStorage
        - Name: CpuManufacturers
        - Name: NetworkBandwidthGbps
        - Name: AcceleratorCount
        - Name: BareMetal
        - Name: RequireHibernateSupport
        - Name: SpotMaxPricePercentageOverLowestPrice
        - Name: BaselineEbsBandwidthMbps
        - Name: OnDemandMaxPricePercentageOverLowestPrice
        - Name: AcceleratorNames
        - Name: AcceleratorTotalMemoryMiB
        - Name: BurstablePerformance
        - Name: MemoryMiB
        - Name: TotalLocalStorageGB
    
    """
    
    LocalStorageTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-localstoragetypes""", alias="LocalStorageTypes")
    InstanceGenerations_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-instancegenerations""", alias="InstanceGenerations")
    NetworkInterfaceCount_: Optional['NetworkInterfaceCountRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-networkinterfacecount""", alias="NetworkInterfaceCount")
    MemoryGiBPerVCpu_: Optional['MemoryGiBPerVCpuRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-memorygibpervcpu""", alias="MemoryGiBPerVCpu")
    AcceleratorTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratortypes""", alias="AcceleratorTypes")
    VCpuCount_: Optional['VCpuCountRangeRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-vcpucount""", alias="VCpuCount")
    ExcludedInstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-excludedinstancetypes""", alias="ExcludedInstanceTypes")
    AcceleratorManufacturers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratormanufacturers""", alias="AcceleratorManufacturers")
    AllowedInstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-allowedinstancetypes""", alias="AllowedInstanceTypes")
    LocalStorage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-localstorage""", alias="LocalStorage")
    CpuManufacturers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-cpumanufacturers""", alias="CpuManufacturers")
    NetworkBandwidthGbps_: Optional['NetworkBandwidthGbpsRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-networkbandwidthgbps""", alias="NetworkBandwidthGbps")
    AcceleratorCount_: Optional['AcceleratorCountRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratorcount""", alias="AcceleratorCount")
    BareMetal_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-baremetal""", alias="BareMetal")
    RequireHibernateSupport_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-requirehibernatesupport""", alias="RequireHibernateSupport")
    SpotMaxPricePercentageOverLowestPrice_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-spotmaxpricepercentageoverlowestprice""", alias="SpotMaxPricePercentageOverLowestPrice")
    BaselineEbsBandwidthMbps_: Optional['BaselineEbsBandwidthMbpsRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-baselineebsbandwidthmbps""", alias="BaselineEbsBandwidthMbps")
    OnDemandMaxPricePercentageOverLowestPrice_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-ondemandmaxpricepercentageoverlowestprice""", alias="OnDemandMaxPricePercentageOverLowestPrice")
    AcceleratorNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratornames""", alias="AcceleratorNames")
    AcceleratorTotalMemoryMiB_: Optional['AcceleratorTotalMemoryMiBRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-acceleratortotalmemorymib""", alias="AcceleratorTotalMemoryMiB")
    BurstablePerformance_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-burstableperformance""", alias="BurstablePerformance")
    MemoryMiB_: Optional['MemoryMiBRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-memorymib""", alias="MemoryMiB")
    TotalLocalStorageGB_: Optional['TotalLocalStorageGBRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html#cfn-ec2-ec2fleet-instancerequirementsrequest-totallocalstoragegb""", alias="TotalLocalStorageGB")
    


    @property
    def tropo_type(self) -> troposphere.ec2.InstanceRequirementsRequest:
        from troposphere.ec2 import InstanceRequirementsRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MaintenanceStrategies(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-maintenancestrategies.html
    Properties:
        - Name: CapacityRebalance
    
    """
    
    CapacityRebalance_: Optional['CapacityRebalance'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-maintenancestrategies.html#cfn-ec2-ec2fleet-maintenancestrategies-capacityrebalance""", alias="CapacityRebalance")
    


    @property
    def tropo_type(self) -> troposphere.ec2.MaintenanceStrategies:
        from troposphere.ec2 import MaintenanceStrategies as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MemoryGiBPerVCpuRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-memorygibpervcpurequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-memorygibpervcpurequest.html#cfn-ec2-ec2fleet-memorygibpervcpurequest-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-memorygibpervcpurequest.html#cfn-ec2-ec2fleet-memorygibpervcpurequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.MemoryGiBPerVCpuRequest:
        from troposphere.ec2 import MemoryGiBPerVCpuRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MemoryMiBRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-memorymibrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-memorymibrequest.html#cfn-ec2-ec2fleet-memorymibrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-memorymibrequest.html#cfn-ec2-ec2fleet-memorymibrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.MemoryMiBRequest:
        from troposphere.ec2 import MemoryMiBRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkBandwidthGbpsRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest.html#cfn-ec2-ec2fleet-networkbandwidthgbpsrequest-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest.html#cfn-ec2-ec2fleet-networkbandwidthgbpsrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.NetworkBandwidthGbpsRequest:
        from troposphere.ec2 import NetworkBandwidthGbpsRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkInterfaceCountRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkinterfacecountrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkinterfacecountrequest.html#cfn-ec2-ec2fleet-networkinterfacecountrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkinterfacecountrequest.html#cfn-ec2-ec2fleet-networkinterfacecountrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.NetworkInterfaceCountRequest:
        from troposphere.ec2 import NetworkInterfaceCountRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnDemandOptionsRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-ondemandoptionsrequest.html
    Properties:
        - Name: SingleAvailabilityZone
        - Name: AllocationStrategy
        - Name: SingleInstanceType
        - Name: MinTargetCapacity
        - Name: MaxTotalPrice
        - Name: CapacityReservationOptions
    
    """
    
    SingleAvailabilityZone_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-ondemandoptionsrequest.html#cfn-ec2-ec2fleet-ondemandoptionsrequest-singleavailabilityzone""", alias="SingleAvailabilityZone")
    AllocationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-ondemandoptionsrequest.html#cfn-ec2-ec2fleet-ondemandoptionsrequest-allocationstrategy""", alias="AllocationStrategy")
    SingleInstanceType_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-ondemandoptionsrequest.html#cfn-ec2-ec2fleet-ondemandoptionsrequest-singleinstancetype""", alias="SingleInstanceType")
    MinTargetCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-ondemandoptionsrequest.html#cfn-ec2-ec2fleet-ondemandoptionsrequest-mintargetcapacity""", alias="MinTargetCapacity")
    MaxTotalPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-ondemandoptionsrequest.html#cfn-ec2-ec2fleet-ondemandoptionsrequest-maxtotalprice""", alias="MaxTotalPrice")
    CapacityReservationOptions_: Optional['CapacityReservationOptionsRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-ondemandoptionsrequest.html#cfn-ec2-ec2fleet-ondemandoptionsrequest-capacityreservationoptions""", alias="CapacityReservationOptions")
    


    @property
    def tropo_type(self) -> troposphere.ec2.OnDemandOptionsRequest:
        from troposphere.ec2 import OnDemandOptionsRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Placement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-placement.html
    Properties:
        - Name: GroupName
        - Name: Tenancy
        - Name: SpreadDomain
        - Name: PartitionNumber
        - Name: AvailabilityZone
        - Name: Affinity
        - Name: HostId
        - Name: HostResourceGroupArn
    
    """
    
    GroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-placement.html#cfn-ec2-ec2fleet-placement-groupname""", alias="GroupName")
    Tenancy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-placement.html#cfn-ec2-ec2fleet-placement-tenancy""", alias="Tenancy")
    SpreadDomain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-placement.html#cfn-ec2-ec2fleet-placement-spreaddomain""", alias="SpreadDomain")
    PartitionNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-placement.html#cfn-ec2-ec2fleet-placement-partitionnumber""", alias="PartitionNumber")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-placement.html#cfn-ec2-ec2fleet-placement-availabilityzone""", alias="AvailabilityZone")
    Affinity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-placement.html#cfn-ec2-ec2fleet-placement-affinity""", alias="Affinity")
    HostId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-placement.html#cfn-ec2-ec2fleet-placement-hostid""", alias="HostId")
    HostResourceGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-placement.html#cfn-ec2-ec2fleet-placement-hostresourcegrouparn""", alias="HostResourceGroupArn")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Placement:
        from troposphere.ec2 import Placement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpotOptionsRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html
    Properties:
        - Name: SingleAvailabilityZone
        - Name: AllocationStrategy
        - Name: SingleInstanceType
        - Name: MinTargetCapacity
        - Name: MaxTotalPrice
        - Name: MaintenanceStrategies
        - Name: InstanceInterruptionBehavior
        - Name: InstancePoolsToUseCount
    
    """
    
    SingleAvailabilityZone_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html#cfn-ec2-ec2fleet-spotoptionsrequest-singleavailabilityzone""", alias="SingleAvailabilityZone")
    AllocationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html#cfn-ec2-ec2fleet-spotoptionsrequest-allocationstrategy""", alias="AllocationStrategy")
    SingleInstanceType_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html#cfn-ec2-ec2fleet-spotoptionsrequest-singleinstancetype""", alias="SingleInstanceType")
    MinTargetCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html#cfn-ec2-ec2fleet-spotoptionsrequest-mintargetcapacity""", alias="MinTargetCapacity")
    MaxTotalPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html#cfn-ec2-ec2fleet-spotoptionsrequest-maxtotalprice""", alias="MaxTotalPrice")
    MaintenanceStrategies_: Optional['MaintenanceStrategies'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html#cfn-ec2-ec2fleet-spotoptionsrequest-maintenancestrategies""", alias="MaintenanceStrategies")
    InstanceInterruptionBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html#cfn-ec2-ec2fleet-spotoptionsrequest-instanceinterruptionbehavior""", alias="InstanceInterruptionBehavior")
    InstancePoolsToUseCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html#cfn-ec2-ec2fleet-spotoptionsrequest-instancepoolstousecount""", alias="InstancePoolsToUseCount")
    


    @property
    def tropo_type(self) -> troposphere.ec2.SpotOptionsRequest:
        from troposphere.ec2 import SpotOptionsRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-tagspecification.html
    Properties:
        - Name: ResourceType
        - Name: Tags
    
    """
    
    ResourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-tagspecification.html#cfn-ec2-ec2fleet-tagspecification-resourcetype""", alias="ResourceType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-tagspecification.html#cfn-ec2-ec2fleet-tagspecification-tags""", alias="Tags")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TagSpecifications:
        from troposphere.ec2 import TagSpecifications as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetCapacitySpecificationRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html
    Properties:
        - Name: DefaultTargetCapacityType
        - Name: TotalTargetCapacity
        - Name: OnDemandTargetCapacity
        - Name: SpotTargetCapacity
        - Name: TargetCapacityUnitType
    
    """
    
    DefaultTargetCapacityType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html#cfn-ec2-ec2fleet-targetcapacityspecificationrequest-defaulttargetcapacitytype""", alias="DefaultTargetCapacityType")
    TotalTargetCapacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html#cfn-ec2-ec2fleet-targetcapacityspecificationrequest-totaltargetcapacity""", alias="TotalTargetCapacity")
    OnDemandTargetCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html#cfn-ec2-ec2fleet-targetcapacityspecificationrequest-ondemandtargetcapacity""", alias="OnDemandTargetCapacity")
    SpotTargetCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html#cfn-ec2-ec2fleet-targetcapacityspecificationrequest-spottargetcapacity""", alias="SpotTargetCapacity")
    TargetCapacityUnitType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html#cfn-ec2-ec2fleet-targetcapacityspecificationrequest-targetcapacityunittype""", alias="TargetCapacityUnitType")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TargetCapacitySpecificationRequest:
        from troposphere.ec2 import TargetCapacitySpecificationRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TotalLocalStorageGBRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-totallocalstoragegbrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-totallocalstoragegbrequest.html#cfn-ec2-ec2fleet-totallocalstoragegbrequest-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-totallocalstoragegbrequest.html#cfn-ec2-ec2fleet-totallocalstoragegbrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TotalLocalStorageGBRequest:
        from troposphere.ec2 import TotalLocalStorageGBRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VCpuCountRangeRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-vcpucountrangerequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-vcpucountrangerequest.html#cfn-ec2-ec2fleet-vcpucountrangerequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-vcpucountrangerequest.html#cfn-ec2-ec2fleet-vcpucountrangerequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.VCpuCountRangeRequest:
        from troposphere.ec2 import VCpuCountRangeRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DestinationOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-flowlog-destinationoptions.html
    Properties:
        - Name: PerHourPartition
        - Name: HiveCompatiblePartitions
        - Name: FileFormat
    
    """
    
    PerHourPartition_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-flowlog-destinationoptions.html#cfn-ec2-flowlog-destinationoptions-perhourpartition""", alias="PerHourPartition")
    HiveCompatiblePartitions_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-flowlog-destinationoptions.html#cfn-ec2-flowlog-destinationoptions-hivecompatiblepartitions""", alias="HiveCompatiblePartitions")
    FileFormat_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-flowlog-destinationoptions.html#cfn-ec2-flowlog-destinationoptions-fileformat""", alias="FileFormat")
    


    @property
    def tropo_type(self) -> troposphere.ec2.DestinationOptions:
        from troposphere.ec2 import DestinationOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IpamOperatingRegion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ipam-ipamoperatingregion.html
    Properties:
        - Name: RegionName
    
    """
    
    RegionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ipam-ipamoperatingregion.html#cfn-ec2-ipam-ipamoperatingregion-regionname""", alias="RegionName")
    


    @property
    def tropo_type(self) -> troposphere.ec2.IpamOperatingRegion:
        from troposphere.ec2 import IpamOperatingRegion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProvisionedCidr(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ipampool-provisionedcidr.html
    Properties:
        - Name: Cidr
    
    """
    
    Cidr_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ipampool-provisionedcidr.html#cfn-ec2-ipampool-provisionedcidr-cidr""", alias="Cidr")
    


    @property
    def tropo_type(self) -> troposphere.ec2.ProvisionedCidr:
        from troposphere.ec2 import ProvisionedCidr as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IpamOperatingRegion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ipamresourcediscovery-ipamoperatingregion.html
    Properties:
        - Name: RegionName
    
    """
    
    RegionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ipamresourcediscovery-ipamoperatingregion.html#cfn-ec2-ipamresourcediscovery-ipamoperatingregion-regionname""", alias="RegionName")
    


    @property
    def tropo_type(self) -> troposphere.ec2.IpamOperatingRegion:
        from troposphere.ec2 import IpamOperatingRegion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssociationParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-ssmassociations-associationparameters.html
    Properties:
        - Name: Key
        - Name: Value
    
    """
    
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-ssmassociations-associationparameters.html#cfn-ec2-instance-ssmassociations-associationparameters-key""", alias="Key")
    Value_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-ssmassociations-associationparameters.html#cfn-ec2-instance-ssmassociations-associationparameters-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AssociationParameter:
        from troposphere.ec2 import AssociationParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BlockDeviceMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html
    Properties:
        - Name: DeviceName
        - Name: Ebs
        - Name: NoDevice
        - Name: VirtualName
    
    """
    
    DeviceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html#cfn-ec2-blockdev-mapping-devicename""", alias="DeviceName")
    Ebs_: Optional['Ebs'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html#cfn-ec2-blockdev-mapping-ebs""", alias="Ebs")
    NoDevice_: Optional['NoDevice'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html#cfn-ec2-blockdev-mapping-nodevice""", alias="NoDevice")
    VirtualName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html#cfn-ec2-blockdev-mapping-virtualname""", alias="VirtualName")
    


    @property
    def tropo_type(self) -> troposphere.ec2.BlockDeviceMapping:
        from troposphere.ec2 import BlockDeviceMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CpuOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-cpuoptions.html
    Properties:
        - Name: CoreCount
        - Name: ThreadsPerCore
    
    """
    
    CoreCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-cpuoptions.html#cfn-ec2-instance-cpuoptions-corecount""", alias="CoreCount")
    ThreadsPerCore_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-cpuoptions.html#cfn-ec2-instance-cpuoptions-threadspercore""", alias="ThreadsPerCore")
    


    @property
    def tropo_type(self) -> troposphere.ec2.CpuOptions:
        from troposphere.ec2 import CpuOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CreditSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-creditspecification.html
    Properties:
        - Name: CPUCredits
    
    """
    
    CPUCredits_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-creditspecification.html#cfn-ec2-instance-creditspecification-cpucredits""", alias="CPUCredits")
    


    @property
    def tropo_type(self) -> troposphere.ec2.CreditSpecification:
        from troposphere.ec2 import CreditSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ebs(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html
    Properties:
        - Name: DeleteOnTermination
        - Name: Encrypted
        - Name: Iops
        - Name: KmsKeyId
        - Name: SnapshotId
        - Name: VolumeSize
        - Name: VolumeType
    
    """
    
    DeleteOnTermination_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-blockdev-template-deleteontermination""", alias="DeleteOnTermination")
    Encrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-blockdev-template-encrypted""", alias="Encrypted")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-blockdev-template-iops""", alias="Iops")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-instance-ebs-kmskeyid""", alias="KmsKeyId")
    SnapshotId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-blockdev-template-snapshotid""", alias="SnapshotId")
    VolumeSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-blockdev-template-volumesize""", alias="VolumeSize")
    VolumeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-blockdev-template-volumetype""", alias="VolumeType")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Ebs:
        from troposphere.ec2 import Ebs as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ElasticGpuSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-elasticgpuspecification.html
    Properties:
        - Name: Type
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-elasticgpuspecification.html#cfn-ec2-instance-elasticgpuspecification-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.ec2.ElasticGpuSpecification:
        from troposphere.ec2 import ElasticGpuSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ElasticInferenceAccelerator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-elasticinferenceaccelerator.html
    Properties:
        - Name: Count
        - Name: Type
    
    """
    
    Count_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-elasticinferenceaccelerator.html#cfn-ec2-instance-elasticinferenceaccelerator-count""", alias="Count")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-elasticinferenceaccelerator.html#cfn-ec2-instance-elasticinferenceaccelerator-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.ec2.ElasticInferenceAccelerator:
        from troposphere.ec2 import ElasticInferenceAccelerator as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnclaveOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-enclaveoptions.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-enclaveoptions.html#cfn-ec2-instance-enclaveoptions-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.ec2.EnclaveOptions:
        from troposphere.ec2 import EnclaveOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HibernationOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-hibernationoptions.html
    Properties:
        - Name: Configured
    
    """
    
    Configured_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-hibernationoptions.html#cfn-ec2-instance-hibernationoptions-configured""", alias="Configured")
    


    @property
    def tropo_type(self) -> troposphere.ec2.HibernationOptions:
        from troposphere.ec2 import HibernationOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceIpv6Address(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-instanceipv6address.html
    Properties:
        - Name: Ipv6Address
    
    """
    
    Ipv6Address_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-instanceipv6address.html#cfn-ec2-instance-instanceipv6address-ipv6address""", alias="Ipv6Address")
    


    @property
    def tropo_type(self) -> troposphere.ec2.InstanceIpv6Address:
        from troposphere.ec2 import InstanceIpv6Address as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchTemplateSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-launchtemplatespecification.html
    Properties:
        - Name: LaunchTemplateId
        - Name: LaunchTemplateName
        - Name: Version
    
    """
    
    LaunchTemplateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-launchtemplatespecification.html#cfn-ec2-instance-launchtemplatespecification-launchtemplateid""", alias="LaunchTemplateId")
    LaunchTemplateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-launchtemplatespecification.html#cfn-ec2-instance-launchtemplatespecification-launchtemplatename""", alias="LaunchTemplateName")
    Version_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-launchtemplatespecification.html#cfn-ec2-instance-launchtemplatespecification-version""", alias="Version")
    


    @property
    def tropo_type(self) -> troposphere.ec2.LaunchTemplateSpecification:
        from troposphere.ec2 import LaunchTemplateSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LicenseSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-licensespecification.html
    Properties:
        - Name: LicenseConfigurationArn
    
    """
    
    LicenseConfigurationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-licensespecification.html#cfn-ec2-instance-licensespecification-licenseconfigurationarn""", alias="LicenseConfigurationArn")
    


    @property
    def tropo_type(self) -> troposphere.ec2.LicenseSpecification:
        from troposphere.ec2 import LicenseSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkInterface(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html
    Properties:
        - Name: AssociateCarrierIpAddress
        - Name: AssociatePublicIpAddress
        - Name: DeleteOnTermination
        - Name: Description
        - Name: DeviceIndex
        - Name: GroupSet
        - Name: Ipv6AddressCount
        - Name: Ipv6Addresses
        - Name: NetworkInterfaceId
        - Name: PrivateIpAddress
        - Name: PrivateIpAddresses
        - Name: SecondaryPrivateIpAddressCount
        - Name: SubnetId
    
    """
    
    AssociateCarrierIpAddress_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#cfn-ec2-instance-networkinterface-associatecarrieripaddress""", alias="AssociateCarrierIpAddress")
    AssociatePublicIpAddress_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-associatepubip""", alias="AssociatePublicIpAddress")
    DeleteOnTermination_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-delete""", alias="DeleteOnTermination")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-description""", alias="Description")
    DeviceIndex_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-deviceindex""", alias="DeviceIndex")
    GroupSet_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-groupset""", alias="GroupSet")
    Ipv6AddressCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#cfn-ec2-instance-networkinterface-ipv6addresscount""", alias="Ipv6AddressCount")
    Ipv6Addresses_: Optional[List['InstanceIpv6Address']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#cfn-ec2-instance-networkinterface-ipv6addresses""", alias="Ipv6Addresses")
    NetworkInterfaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-network-iface""", alias="NetworkInterfaceId")
    PrivateIpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-privateipaddress""", alias="PrivateIpAddress")
    PrivateIpAddresses_: Optional[List['PrivateIpAddressSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-privateipaddresses""", alias="PrivateIpAddresses")
    SecondaryPrivateIpAddressCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-secondprivateip""", alias="SecondaryPrivateIpAddressCount")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-subnetid""", alias="SubnetId")
    


    @property
    def tropo_type(self) -> troposphere.ec2.NetworkInterface:
        from troposphere.ec2 import NetworkInterface as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NoDevice(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-nodevice.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.ec2.NoDevice:
        from troposphere.ec2 import NoDevice as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateDnsNameOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-privatednsnameoptions.html
    Properties:
        - Name: EnableResourceNameDnsAAAARecord
        - Name: EnableResourceNameDnsARecord
        - Name: HostnameType
    
    """
    
    EnableResourceNameDnsAAAARecord_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-privatednsnameoptions.html#cfn-ec2-instance-privatednsnameoptions-enableresourcenamednsaaaarecord""", alias="EnableResourceNameDnsAAAARecord")
    EnableResourceNameDnsARecord_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-privatednsnameoptions.html#cfn-ec2-instance-privatednsnameoptions-enableresourcenamednsarecord""", alias="EnableResourceNameDnsARecord")
    HostnameType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-privatednsnameoptions.html#cfn-ec2-instance-privatednsnameoptions-hostnametype""", alias="HostnameType")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PrivateDnsNameOptions:
        from troposphere.ec2 import PrivateDnsNameOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateIpAddressSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-interface-privateipspec.html
    Properties:
        - Name: Primary
        - Name: PrivateIpAddress
    
    """
    
    Primary_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-interface-privateipspec.html#cfn-ec2-networkinterface-privateipspecification-primary""", alias="Primary")
    PrivateIpAddress_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-interface-privateipspec.html#cfn-ec2-networkinterface-privateipspecification-privateipaddress""", alias="PrivateIpAddress")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PrivateIpAddressSpecification:
        from troposphere.ec2 import PrivateIpAddressSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SsmAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-ssmassociations.html
    Properties:
        - Name: AssociationParameters
        - Name: DocumentName
    
    """
    
    AssociationParameters_: Optional[List['AssociationParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-ssmassociations.html#cfn-ec2-instance-ssmassociations-associationparameters""", alias="AssociationParameters")
    DocumentName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-ssmassociations.html#cfn-ec2-instance-ssmassociations-documentname""", alias="DocumentName")
    


    @property
    def tropo_type(self) -> troposphere.ec2.SsmAssociation:
        from troposphere.ec2 import SsmAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Volume(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-mount-point.html
    Properties:
        - Name: Device
        - Name: VolumeId
    
    """
    
    Device_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-mount-point.html#cfn-ec2-mountpoint-device""", alias="Device")
    VolumeId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-mount-point.html#cfn-ec2-mountpoint-volumeid""", alias="VolumeId")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Volume:
        from troposphere.ec2 import Volume as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AcceleratorCount(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-acceleratorcount.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-acceleratorcount.html#cfn-ec2-launchtemplate-acceleratorcount-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-acceleratorcount.html#cfn-ec2-launchtemplate-acceleratorcount-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AcceleratorCount:
        from troposphere.ec2 import AcceleratorCount as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AcceleratorTotalMemoryMiB(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-acceleratortotalmemorymib.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-acceleratortotalmemorymib.html#cfn-ec2-launchtemplate-acceleratortotalmemorymib-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-acceleratortotalmemorymib.html#cfn-ec2-launchtemplate-acceleratortotalmemorymib-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AcceleratorTotalMemoryMiB:
        from troposphere.ec2 import AcceleratorTotalMemoryMiB as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BaselineEbsBandwidthMbps(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-baselineebsbandwidthmbps.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-baselineebsbandwidthmbps.html#cfn-ec2-launchtemplate-baselineebsbandwidthmbps-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-baselineebsbandwidthmbps.html#cfn-ec2-launchtemplate-baselineebsbandwidthmbps-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.BaselineEbsBandwidthMbps:
        from troposphere.ec2 import BaselineEbsBandwidthMbps as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BlockDeviceMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping.html
    Properties:
        - Name: Ebs
        - Name: NoDevice
        - Name: VirtualName
        - Name: DeviceName
    
    """
    
    Ebs_: Optional['Ebs'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping.html#cfn-ec2-launchtemplate-blockdevicemapping-ebs""", alias="Ebs")
    NoDevice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping.html#cfn-ec2-launchtemplate-blockdevicemapping-nodevice""", alias="NoDevice")
    VirtualName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping.html#cfn-ec2-launchtemplate-blockdevicemapping-virtualname""", alias="VirtualName")
    DeviceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping.html#cfn-ec2-launchtemplate-blockdevicemapping-devicename""", alias="DeviceName")
    


    @property
    def tropo_type(self) -> troposphere.ec2.BlockDeviceMapping:
        from troposphere.ec2 import BlockDeviceMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacityReservationSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-capacityreservationspecification.html
    Properties:
        - Name: CapacityReservationPreference
        - Name: CapacityReservationTarget
    
    """
    
    CapacityReservationPreference_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-capacityreservationspecification.html#cfn-ec2-launchtemplate-capacityreservationspecification-capacityreservationpreference""", alias="CapacityReservationPreference")
    CapacityReservationTarget_: Optional['CapacityReservationTarget'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-capacityreservationspecification.html#cfn-ec2-launchtemplate-capacityreservationspecification-capacityreservationtarget""", alias="CapacityReservationTarget")
    


    @property
    def tropo_type(self) -> troposphere.ec2.CapacityReservationSpecification:
        from troposphere.ec2 import CapacityReservationSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacityReservationTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-capacityreservationtarget.html
    Properties:
        - Name: CapacityReservationResourceGroupArn
        - Name: CapacityReservationId
    
    """
    
    CapacityReservationResourceGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-capacityreservationtarget.html#cfn-ec2-launchtemplate-capacityreservationtarget-capacityreservationresourcegrouparn""", alias="CapacityReservationResourceGroupArn")
    CapacityReservationId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-capacityreservationtarget.html#cfn-ec2-launchtemplate-capacityreservationtarget-capacityreservationid""", alias="CapacityReservationId")
    


    @property
    def tropo_type(self) -> troposphere.ec2.CapacityReservationTarget:
        from troposphere.ec2 import CapacityReservationTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectionTrackingSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-connectiontrackingspecification.html
    Properties:
        - Name: UdpTimeout
        - Name: TcpEstablishedTimeout
        - Name: UdpStreamTimeout
    
    """
    
    UdpTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-connectiontrackingspecification.html#cfn-ec2-launchtemplate-connectiontrackingspecification-udptimeout""", alias="UdpTimeout")
    TcpEstablishedTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-connectiontrackingspecification.html#cfn-ec2-launchtemplate-connectiontrackingspecification-tcpestablishedtimeout""", alias="TcpEstablishedTimeout")
    UdpStreamTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-connectiontrackingspecification.html#cfn-ec2-launchtemplate-connectiontrackingspecification-udpstreamtimeout""", alias="UdpStreamTimeout")
    


    @property
    def tropo_type(self) -> troposphere.ec2.ConnectionTrackingSpecification:
        from troposphere.ec2 import ConnectionTrackingSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CpuOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-cpuoptions.html
    Properties:
        - Name: ThreadsPerCore
        - Name: AmdSevSnp
        - Name: CoreCount
    
    """
    
    ThreadsPerCore_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-cpuoptions.html#cfn-ec2-launchtemplate-cpuoptions-threadspercore""", alias="ThreadsPerCore")
    AmdSevSnp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-cpuoptions.html#cfn-ec2-launchtemplate-cpuoptions-amdsevsnp""", alias="AmdSevSnp")
    CoreCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-cpuoptions.html#cfn-ec2-launchtemplate-cpuoptions-corecount""", alias="CoreCount")
    


    @property
    def tropo_type(self) -> troposphere.ec2.CpuOptions:
        from troposphere.ec2 import CpuOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CreditSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-creditspecification.html
    Properties:
        - Name: CpuCredits
    
    """
    
    CpuCredits_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-creditspecification.html#cfn-ec2-launchtemplate-creditspecification-cpucredits""", alias="CpuCredits")
    


    @property
    def tropo_type(self) -> troposphere.ec2.CreditSpecification:
        from troposphere.ec2 import CreditSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ebs(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ebs.html
    Properties:
        - Name: SnapshotId
        - Name: VolumeType
        - Name: KmsKeyId
        - Name: Encrypted
        - Name: Throughput
        - Name: Iops
        - Name: VolumeSize
        - Name: DeleteOnTermination
    
    """
    
    SnapshotId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ebs.html#cfn-ec2-launchtemplate-ebs-snapshotid""", alias="SnapshotId")
    VolumeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ebs.html#cfn-ec2-launchtemplate-ebs-volumetype""", alias="VolumeType")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ebs.html#cfn-ec2-launchtemplate-ebs-kmskeyid""", alias="KmsKeyId")
    Encrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ebs.html#cfn-ec2-launchtemplate-ebs-encrypted""", alias="Encrypted")
    Throughput_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ebs.html#cfn-ec2-launchtemplate-ebs-throughput""", alias="Throughput")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ebs.html#cfn-ec2-launchtemplate-ebs-iops""", alias="Iops")
    VolumeSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ebs.html#cfn-ec2-launchtemplate-ebs-volumesize""", alias="VolumeSize")
    DeleteOnTermination_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ebs.html#cfn-ec2-launchtemplate-ebs-deleteontermination""", alias="DeleteOnTermination")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Ebs:
        from troposphere.ec2 import Ebs as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ElasticGpuSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-elasticgpuspecification.html
    Properties:
        - Name: Type
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-elasticgpuspecification.html#cfn-ec2-launchtemplate-elasticgpuspecification-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.ec2.ElasticGpuSpecification:
        from troposphere.ec2 import ElasticGpuSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnaSrdSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-enasrdspecification.html
    Properties:
        - Name: EnaSrdEnabled
        - Name: EnaSrdUdpSpecification
    
    """
    
    EnaSrdEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-enasrdspecification.html#cfn-ec2-launchtemplate-enasrdspecification-enasrdenabled""", alias="EnaSrdEnabled")
    EnaSrdUdpSpecification_: Optional['EnaSrdUdpSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-enasrdspecification.html#cfn-ec2-launchtemplate-enasrdspecification-enasrdudpspecification""", alias="EnaSrdUdpSpecification")
    


    @property
    def tropo_type(self) -> troposphere.ec2.EnaSrdSpecification:
        from troposphere.ec2 import EnaSrdSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnaSrdUdpSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-enasrdudpspecification.html
    Properties:
        - Name: EnaSrdUdpEnabled
    
    """
    
    EnaSrdUdpEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-enasrdudpspecification.html#cfn-ec2-launchtemplate-enasrdudpspecification-enasrdudpenabled""", alias="EnaSrdUdpEnabled")
    


    @property
    def tropo_type(self) -> troposphere.ec2.EnaSrdUdpSpecification:
        from troposphere.ec2 import EnaSrdUdpSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnclaveOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-enclaveoptions.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-enclaveoptions.html#cfn-ec2-launchtemplate-enclaveoptions-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.ec2.EnclaveOptions:
        from troposphere.ec2 import EnclaveOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HibernationOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-hibernationoptions.html
    Properties:
        - Name: Configured
    
    """
    
    Configured_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-hibernationoptions.html#cfn-ec2-launchtemplate-hibernationoptions-configured""", alias="Configured")
    


    @property
    def tropo_type(self) -> troposphere.ec2.HibernationOptions:
        from troposphere.ec2 import HibernationOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IamInstanceProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-iaminstanceprofile.html
    Properties:
        - Name: Arn
        - Name: Name
    
    """
    
    Arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-iaminstanceprofile.html#cfn-ec2-launchtemplate-iaminstanceprofile-arn""", alias="Arn")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-iaminstanceprofile.html#cfn-ec2-launchtemplate-iaminstanceprofile-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ec2.IamInstanceProfile:
        from troposphere.ec2 import IamInstanceProfile as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceMarketOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancemarketoptions.html
    Properties:
        - Name: SpotOptions
        - Name: MarketType
    
    """
    
    SpotOptions_: Optional['SpotOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancemarketoptions.html#cfn-ec2-launchtemplate-instancemarketoptions-spotoptions""", alias="SpotOptions")
    MarketType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancemarketoptions.html#cfn-ec2-launchtemplate-instancemarketoptions-markettype""", alias="MarketType")
    


    @property
    def tropo_type(self) -> troposphere.ec2.InstanceMarketOptions:
        from troposphere.ec2 import InstanceMarketOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceRequirements(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html
    Properties:
        - Name: LocalStorageTypes
        - Name: InstanceGenerations
        - Name: NetworkInterfaceCount
        - Name: MemoryGiBPerVCpu
        - Name: AcceleratorTypes
        - Name: VCpuCount
        - Name: ExcludedInstanceTypes
        - Name: AcceleratorManufacturers
        - Name: AllowedInstanceTypes
        - Name: LocalStorage
        - Name: CpuManufacturers
        - Name: AcceleratorCount
        - Name: NetworkBandwidthGbps
        - Name: BareMetal
        - Name: RequireHibernateSupport
        - Name: SpotMaxPricePercentageOverLowestPrice
        - Name: BaselineEbsBandwidthMbps
        - Name: OnDemandMaxPricePercentageOverLowestPrice
        - Name: AcceleratorNames
        - Name: AcceleratorTotalMemoryMiB
        - Name: BurstablePerformance
        - Name: MemoryMiB
        - Name: TotalLocalStorageGB
    
    """
    
    LocalStorageTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-localstoragetypes""", alias="LocalStorageTypes")
    InstanceGenerations_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-instancegenerations""", alias="InstanceGenerations")
    NetworkInterfaceCount_: Optional['NetworkInterfaceCount'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-networkinterfacecount""", alias="NetworkInterfaceCount")
    MemoryGiBPerVCpu_: Optional['MemoryGiBPerVCpu'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-memorygibpervcpu""", alias="MemoryGiBPerVCpu")
    AcceleratorTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-acceleratortypes""", alias="AcceleratorTypes")
    VCpuCount_: Optional['VCpuCount'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-vcpucount""", alias="VCpuCount")
    ExcludedInstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-excludedinstancetypes""", alias="ExcludedInstanceTypes")
    AcceleratorManufacturers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-acceleratormanufacturers""", alias="AcceleratorManufacturers")
    AllowedInstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-allowedinstancetypes""", alias="AllowedInstanceTypes")
    LocalStorage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-localstorage""", alias="LocalStorage")
    CpuManufacturers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-cpumanufacturers""", alias="CpuManufacturers")
    AcceleratorCount_: Optional['AcceleratorCount'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-acceleratorcount""", alias="AcceleratorCount")
    NetworkBandwidthGbps_: Optional['NetworkBandwidthGbps'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-networkbandwidthgbps""", alias="NetworkBandwidthGbps")
    BareMetal_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-baremetal""", alias="BareMetal")
    RequireHibernateSupport_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-requirehibernatesupport""", alias="RequireHibernateSupport")
    SpotMaxPricePercentageOverLowestPrice_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-spotmaxpricepercentageoverlowestprice""", alias="SpotMaxPricePercentageOverLowestPrice")
    BaselineEbsBandwidthMbps_: Optional['BaselineEbsBandwidthMbps'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-baselineebsbandwidthmbps""", alias="BaselineEbsBandwidthMbps")
    OnDemandMaxPricePercentageOverLowestPrice_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-ondemandmaxpricepercentageoverlowestprice""", alias="OnDemandMaxPricePercentageOverLowestPrice")
    AcceleratorNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-acceleratornames""", alias="AcceleratorNames")
    AcceleratorTotalMemoryMiB_: Optional['AcceleratorTotalMemoryMiB'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-acceleratortotalmemorymib""", alias="AcceleratorTotalMemoryMiB")
    BurstablePerformance_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-burstableperformance""", alias="BurstablePerformance")
    MemoryMiB_: Optional['MemoryMiB'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-memorymib""", alias="MemoryMiB")
    TotalLocalStorageGB_: Optional['TotalLocalStorageGB'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-instancerequirements.html#cfn-ec2-launchtemplate-instancerequirements-totallocalstoragegb""", alias="TotalLocalStorageGB")
    


    @property
    def tropo_type(self) -> troposphere.ec2.InstanceRequirements:
        from troposphere.ec2 import InstanceRequirements as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ipv4PrefixSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ipv4prefixspecification.html
    Properties:
        - Name: Ipv4Prefix
    
    """
    
    Ipv4Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ipv4prefixspecification.html#cfn-ec2-launchtemplate-ipv4prefixspecification-ipv4prefix""", alias="Ipv4Prefix")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Ipv4PrefixSpecification:
        from troposphere.ec2 import Ipv4PrefixSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ipv6Add(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ipv6add.html
    Properties:
        - Name: Ipv6Address
    
    """
    
    Ipv6Address_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ipv6add.html#cfn-ec2-launchtemplate-ipv6add-ipv6address""", alias="Ipv6Address")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Ipv6Add:
        from troposphere.ec2 import Ipv6Add as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ipv6PrefixSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ipv6prefixspecification.html
    Properties:
        - Name: Ipv6Prefix
    
    """
    
    Ipv6Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ipv6prefixspecification.html#cfn-ec2-launchtemplate-ipv6prefixspecification-ipv6prefix""", alias="Ipv6Prefix")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Ipv6PrefixSpecification:
        from troposphere.ec2 import Ipv6PrefixSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchTemplateData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html
    Properties:
        - Name: SecurityGroups
        - Name: TagSpecifications
        - Name: UserData
        - Name: BlockDeviceMappings
        - Name: MaintenanceOptions
        - Name: IamInstanceProfile
        - Name: KernelId
        - Name: EbsOptimized
        - Name: ElasticGpuSpecifications
        - Name: ElasticInferenceAccelerators
        - Name: Placement
        - Name: NetworkInterfaces
        - Name: EnclaveOptions
        - Name: ImageId
        - Name: InstanceType
        - Name: Monitoring
        - Name: HibernationOptions
        - Name: MetadataOptions
        - Name: LicenseSpecifications
        - Name: InstanceInitiatedShutdownBehavior
        - Name: DisableApiStop
        - Name: CpuOptions
        - Name: PrivateDnsNameOptions
        - Name: SecurityGroupIds
        - Name: KeyName
        - Name: DisableApiTermination
        - Name: InstanceMarketOptions
        - Name: InstanceRequirements
        - Name: RamDiskId
        - Name: CapacityReservationSpecification
        - Name: CreditSpecification
    
    """
    
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-securitygroups""", alias="SecurityGroups")
    TagSpecifications_: Optional[List['TagSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-tagspecifications""", alias="TagSpecifications")
    UserData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-userdata""", alias="UserData")
    BlockDeviceMappings_: Optional[List['BlockDeviceMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-blockdevicemappings""", alias="BlockDeviceMappings")
    MaintenanceOptions_: Optional['MaintenanceOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-maintenanceoptions""", alias="MaintenanceOptions")
    IamInstanceProfile_: Optional['IamInstanceProfile'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-iaminstanceprofile""", alias="IamInstanceProfile")
    KernelId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-kernelid""", alias="KernelId")
    EbsOptimized_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-ebsoptimized""", alias="EbsOptimized")
    ElasticGpuSpecifications_: Optional[List['ElasticGpuSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-elasticgpuspecifications""", alias="ElasticGpuSpecifications")
    ElasticInferenceAccelerators_: Optional[List['LaunchTemplateElasticInferenceAccelerator']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-elasticinferenceaccelerators""", alias="ElasticInferenceAccelerators")
    Placement_: Optional['Placement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-placement""", alias="Placement")
    NetworkInterfaces_: Optional[List['NetworkInterface']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-networkinterfaces""", alias="NetworkInterfaces")
    EnclaveOptions_: Optional['EnclaveOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-enclaveoptions""", alias="EnclaveOptions")
    ImageId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-imageid""", alias="ImageId")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-instancetype""", alias="InstanceType")
    Monitoring_: Optional['Monitoring'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-monitoring""", alias="Monitoring")
    HibernationOptions_: Optional['HibernationOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-hibernationoptions""", alias="HibernationOptions")
    MetadataOptions_: Optional['MetadataOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-metadataoptions""", alias="MetadataOptions")
    LicenseSpecifications_: Optional[List['LicenseSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-licensespecifications""", alias="LicenseSpecifications")
    InstanceInitiatedShutdownBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-instanceinitiatedshutdownbehavior""", alias="InstanceInitiatedShutdownBehavior")
    DisableApiStop_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-disableapistop""", alias="DisableApiStop")
    CpuOptions_: Optional['CpuOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-cpuoptions""", alias="CpuOptions")
    PrivateDnsNameOptions_: Optional['PrivateDnsNameOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-privatednsnameoptions""", alias="PrivateDnsNameOptions")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-securitygroupids""", alias="SecurityGroupIds")
    KeyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-keyname""", alias="KeyName")
    DisableApiTermination_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-disableapitermination""", alias="DisableApiTermination")
    InstanceMarketOptions_: Optional['InstanceMarketOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-instancemarketoptions""", alias="InstanceMarketOptions")
    InstanceRequirements_: Optional['InstanceRequirements'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-instancerequirements""", alias="InstanceRequirements")
    RamDiskId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-ramdiskid""", alias="RamDiskId")
    CapacityReservationSpecification_: Optional['CapacityReservationSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-capacityreservationspecification""", alias="CapacityReservationSpecification")
    CreditSpecification_: Optional['CreditSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-creditspecification""", alias="CreditSpecification")
    


    @property
    def tropo_type(self) -> troposphere.ec2.LaunchTemplateData:
        from troposphere.ec2 import LaunchTemplateData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchTemplateElasticInferenceAccelerator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplateelasticinferenceaccelerator.html
    Properties:
        - Name: Type
        - Name: Count
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplateelasticinferenceaccelerator.html#cfn-ec2-launchtemplate-launchtemplateelasticinferenceaccelerator-type""", alias="Type")
    Count_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplateelasticinferenceaccelerator.html#cfn-ec2-launchtemplate-launchtemplateelasticinferenceaccelerator-count""", alias="Count")
    


    @property
    def tropo_type(self) -> troposphere.ec2.LaunchTemplateElasticInferenceAccelerator:
        from troposphere.ec2 import LaunchTemplateElasticInferenceAccelerator as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchTemplateTagSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatetagspecification.html
    Properties:
        - Name: ResourceType
        - Name: Tags
    
    """
    
    ResourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatetagspecification.html#cfn-ec2-launchtemplate-launchtemplatetagspecification-resourcetype""", alias="ResourceType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatetagspecification.html#cfn-ec2-launchtemplate-launchtemplatetagspecification-tags""", alias="Tags")
    


    @property
    def tropo_type(self) -> troposphere.ec2.LaunchTemplateTagSpecification:
        from troposphere.ec2 import LaunchTemplateTagSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LicenseSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-licensespecification.html
    Properties:
        - Name: LicenseConfigurationArn
    
    """
    
    LicenseConfigurationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-licensespecification.html#cfn-ec2-launchtemplate-licensespecification-licenseconfigurationarn""", alias="LicenseConfigurationArn")
    


    @property
    def tropo_type(self) -> troposphere.ec2.LicenseSpecification:
        from troposphere.ec2 import LicenseSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MaintenanceOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-maintenanceoptions.html
    Properties:
        - Name: AutoRecovery
    
    """
    
    AutoRecovery_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-maintenanceoptions.html#cfn-ec2-launchtemplate-maintenanceoptions-autorecovery""", alias="AutoRecovery")
    


    @property
    def tropo_type(self) -> troposphere.ec2.MaintenanceOptions:
        from troposphere.ec2 import MaintenanceOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MemoryGiBPerVCpu(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-memorygibpervcpu.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-memorygibpervcpu.html#cfn-ec2-launchtemplate-memorygibpervcpu-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-memorygibpervcpu.html#cfn-ec2-launchtemplate-memorygibpervcpu-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.MemoryGiBPerVCpu:
        from troposphere.ec2 import MemoryGiBPerVCpu as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MemoryMiB(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-memorymib.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-memorymib.html#cfn-ec2-launchtemplate-memorymib-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-memorymib.html#cfn-ec2-launchtemplate-memorymib-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.MemoryMiB:
        from troposphere.ec2 import MemoryMiB as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetadataOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-metadataoptions.html
    Properties:
        - Name: HttpPutResponseHopLimit
        - Name: HttpTokens
        - Name: HttpProtocolIpv6
        - Name: InstanceMetadataTags
        - Name: HttpEndpoint
    
    """
    
    HttpPutResponseHopLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-metadataoptions.html#cfn-ec2-launchtemplate-metadataoptions-httpputresponsehoplimit""", alias="HttpPutResponseHopLimit")
    HttpTokens_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-metadataoptions.html#cfn-ec2-launchtemplate-metadataoptions-httptokens""", alias="HttpTokens")
    HttpProtocolIpv6_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-metadataoptions.html#cfn-ec2-launchtemplate-metadataoptions-httpprotocolipv6""", alias="HttpProtocolIpv6")
    InstanceMetadataTags_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-metadataoptions.html#cfn-ec2-launchtemplate-metadataoptions-instancemetadatatags""", alias="InstanceMetadataTags")
    HttpEndpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-metadataoptions.html#cfn-ec2-launchtemplate-metadataoptions-httpendpoint""", alias="HttpEndpoint")
    


    @property
    def tropo_type(self) -> troposphere.ec2.MetadataOptions:
        from troposphere.ec2 import MetadataOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Monitoring(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-monitoring.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-monitoring.html#cfn-ec2-launchtemplate-monitoring-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Monitoring:
        from troposphere.ec2 import Monitoring as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkBandwidthGbps(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkbandwidthgbps.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkbandwidthgbps.html#cfn-ec2-launchtemplate-networkbandwidthgbps-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkbandwidthgbps.html#cfn-ec2-launchtemplate-networkbandwidthgbps-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.NetworkBandwidthGbps:
        from troposphere.ec2 import NetworkBandwidthGbps as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkInterface(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html
    Properties:
        - Name: Description
        - Name: PrivateIpAddress
        - Name: PrivateIpAddresses
        - Name: SecondaryPrivateIpAddressCount
        - Name: Ipv6PrefixCount
        - Name: Ipv4Prefixes
        - Name: DeviceIndex
        - Name: PrimaryIpv6
        - Name: Ipv4PrefixCount
        - Name: Ipv6Prefixes
        - Name: SubnetId
        - Name: Ipv6Addresses
        - Name: AssociatePublicIpAddress
        - Name: NetworkInterfaceId
        - Name: NetworkCardIndex
        - Name: InterfaceType
        - Name: AssociateCarrierIpAddress
        - Name: EnaSrdSpecification
        - Name: Ipv6AddressCount
        - Name: Groups
        - Name: DeleteOnTermination
        - Name: ConnectionTrackingSpecification
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-description""", alias="Description")
    PrivateIpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-privateipaddress""", alias="PrivateIpAddress")
    PrivateIpAddresses_: Optional[List['PrivateIpAdd']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-privateipaddresses""", alias="PrivateIpAddresses")
    SecondaryPrivateIpAddressCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-secondaryprivateipaddresscount""", alias="SecondaryPrivateIpAddressCount")
    Ipv6PrefixCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-ipv6prefixcount""", alias="Ipv6PrefixCount")
    Ipv4Prefixes_: Optional[List['Ipv4PrefixSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-ipv4prefixes""", alias="Ipv4Prefixes")
    DeviceIndex_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-deviceindex""", alias="DeviceIndex")
    PrimaryIpv6_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-primaryipv6""", alias="PrimaryIpv6")
    Ipv4PrefixCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-ipv4prefixcount""", alias="Ipv4PrefixCount")
    Ipv6Prefixes_: Optional[List['Ipv6PrefixSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-ipv6prefixes""", alias="Ipv6Prefixes")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-subnetid""", alias="SubnetId")
    Ipv6Addresses_: Optional[List['Ipv6Add']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-ipv6addresses""", alias="Ipv6Addresses")
    AssociatePublicIpAddress_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-associatepublicipaddress""", alias="AssociatePublicIpAddress")
    NetworkInterfaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-networkinterfaceid""", alias="NetworkInterfaceId")
    NetworkCardIndex_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-networkcardindex""", alias="NetworkCardIndex")
    InterfaceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-interfacetype""", alias="InterfaceType")
    AssociateCarrierIpAddress_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-associatecarrieripaddress""", alias="AssociateCarrierIpAddress")
    EnaSrdSpecification_: Optional['EnaSrdSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-enasrdspecification""", alias="EnaSrdSpecification")
    Ipv6AddressCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-ipv6addresscount""", alias="Ipv6AddressCount")
    Groups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-groups""", alias="Groups")
    DeleteOnTermination_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-deleteontermination""", alias="DeleteOnTermination")
    ConnectionTrackingSpecification_: Optional['ConnectionTrackingSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-connectiontrackingspecification""", alias="ConnectionTrackingSpecification")
    


    @property
    def tropo_type(self) -> troposphere.ec2.NetworkInterface:
        from troposphere.ec2 import NetworkInterface as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkInterfaceCount(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterfacecount.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterfacecount.html#cfn-ec2-launchtemplate-networkinterfacecount-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterfacecount.html#cfn-ec2-launchtemplate-networkinterfacecount-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.NetworkInterfaceCount:
        from troposphere.ec2 import NetworkInterfaceCount as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Placement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-placement.html
    Properties:
        - Name: GroupName
        - Name: Tenancy
        - Name: SpreadDomain
        - Name: PartitionNumber
        - Name: AvailabilityZone
        - Name: Affinity
        - Name: HostId
        - Name: HostResourceGroupArn
        - Name: GroupId
    
    """
    
    GroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-placement.html#cfn-ec2-launchtemplate-placement-groupname""", alias="GroupName")
    Tenancy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-placement.html#cfn-ec2-launchtemplate-placement-tenancy""", alias="Tenancy")
    SpreadDomain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-placement.html#cfn-ec2-launchtemplate-placement-spreaddomain""", alias="SpreadDomain")
    PartitionNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-placement.html#cfn-ec2-launchtemplate-placement-partitionnumber""", alias="PartitionNumber")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-placement.html#cfn-ec2-launchtemplate-placement-availabilityzone""", alias="AvailabilityZone")
    Affinity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-placement.html#cfn-ec2-launchtemplate-placement-affinity""", alias="Affinity")
    HostId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-placement.html#cfn-ec2-launchtemplate-placement-hostid""", alias="HostId")
    HostResourceGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-placement.html#cfn-ec2-launchtemplate-placement-hostresourcegrouparn""", alias="HostResourceGroupArn")
    GroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-placement.html#cfn-ec2-launchtemplate-placement-groupid""", alias="GroupId")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Placement:
        from troposphere.ec2 import Placement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateDnsNameOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-privatednsnameoptions.html
    Properties:
        - Name: EnableResourceNameDnsARecord
        - Name: HostnameType
        - Name: EnableResourceNameDnsAAAARecord
    
    """
    
    EnableResourceNameDnsARecord_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-privatednsnameoptions.html#cfn-ec2-launchtemplate-privatednsnameoptions-enableresourcenamednsarecord""", alias="EnableResourceNameDnsARecord")
    HostnameType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-privatednsnameoptions.html#cfn-ec2-launchtemplate-privatednsnameoptions-hostnametype""", alias="HostnameType")
    EnableResourceNameDnsAAAARecord_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-privatednsnameoptions.html#cfn-ec2-launchtemplate-privatednsnameoptions-enableresourcenamednsaaaarecord""", alias="EnableResourceNameDnsAAAARecord")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PrivateDnsNameOptions:
        from troposphere.ec2 import PrivateDnsNameOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateIpAdd(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-privateipadd.html
    Properties:
        - Name: PrivateIpAddress
        - Name: Primary
    
    """
    
    PrivateIpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-privateipadd.html#cfn-ec2-launchtemplate-privateipadd-privateipaddress""", alias="PrivateIpAddress")
    Primary_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-privateipadd.html#cfn-ec2-launchtemplate-privateipadd-primary""", alias="Primary")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PrivateIpAdd:
        from troposphere.ec2 import PrivateIpAdd as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpotOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-spotoptions.html
    Properties:
        - Name: SpotInstanceType
        - Name: InstanceInterruptionBehavior
        - Name: MaxPrice
        - Name: BlockDurationMinutes
        - Name: ValidUntil
    
    """
    
    SpotInstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-spotoptions.html#cfn-ec2-launchtemplate-spotoptions-spotinstancetype""", alias="SpotInstanceType")
    InstanceInterruptionBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-spotoptions.html#cfn-ec2-launchtemplate-spotoptions-instanceinterruptionbehavior""", alias="InstanceInterruptionBehavior")
    MaxPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-spotoptions.html#cfn-ec2-launchtemplate-spotoptions-maxprice""", alias="MaxPrice")
    BlockDurationMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-spotoptions.html#cfn-ec2-launchtemplate-spotoptions-blockdurationminutes""", alias="BlockDurationMinutes")
    ValidUntil_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-spotoptions.html#cfn-ec2-launchtemplate-spotoptions-validuntil""", alias="ValidUntil")
    


    @property
    def tropo_type(self) -> troposphere.ec2.SpotOptions:
        from troposphere.ec2 import SpotOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecification.html
    Properties:
        - Name: ResourceType
        - Name: Tags
    
    """
    
    ResourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecification.html#cfn-ec2-launchtemplate-tagspecification-resourcetype""", alias="ResourceType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecification.html#cfn-ec2-launchtemplate-tagspecification-tags""", alias="Tags")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TagSpecifications:
        from troposphere.ec2 import TagSpecifications as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TotalLocalStorageGB(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-totallocalstoragegb.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-totallocalstoragegb.html#cfn-ec2-launchtemplate-totallocalstoragegb-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-totallocalstoragegb.html#cfn-ec2-launchtemplate-totallocalstoragegb-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TotalLocalStorageGB:
        from troposphere.ec2 import TotalLocalStorageGB as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VCpuCount(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-vcpucount.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-vcpucount.html#cfn-ec2-launchtemplate-vcpucount-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-vcpucount.html#cfn-ec2-launchtemplate-vcpucount-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.VCpuCount:
        from troposphere.ec2 import VCpuCount as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Icmp(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkaclentry-icmp.html
    Properties:
        - Name: Type
        - Name: Code
    
    """
    
    Type_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkaclentry-icmp.html#cfn-ec2-networkaclentry-icmp-type""", alias="Type")
    Code_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkaclentry-icmp.html#cfn-ec2-networkaclentry-icmp-code""", alias="Code")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Icmp:
        from troposphere.ec2 import Icmp as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PortRange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkaclentry-portrange.html
    Properties:
        - Name: From
        - Name: To
    
    """
    
    From_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkaclentry-portrange.html#cfn-ec2-networkaclentry-portrange-from""", alias="From")
    To_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkaclentry-portrange.html#cfn-ec2-networkaclentry-portrange-to""", alias="To")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PortRange:
        from troposphere.ec2 import PortRange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessScopePathRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-accessscopepathrequest.html
    Properties:
        - Name: Destination
        - Name: ThroughResources
        - Name: Source
    
    """
    
    Destination_: Optional['PathStatementRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-accessscopepathrequest.html#cfn-ec2-networkinsightsaccessscope-accessscopepathrequest-destination""", alias="Destination")
    ThroughResources_: Optional[List['ThroughResourcesStatementRequest']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-accessscopepathrequest.html#cfn-ec2-networkinsightsaccessscope-accessscopepathrequest-throughresources""", alias="ThroughResources")
    Source_: Optional['PathStatementRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-accessscopepathrequest.html#cfn-ec2-networkinsightsaccessscope-accessscopepathrequest-source""", alias="Source")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AccessScopePathRequest:
        from troposphere.ec2 import AccessScopePathRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PacketHeaderStatementRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-packetheaderstatementrequest.html
    Properties:
        - Name: Protocols
        - Name: DestinationPorts
        - Name: DestinationAddresses
        - Name: DestinationPrefixLists
        - Name: SourceAddresses
        - Name: SourcePorts
        - Name: SourcePrefixLists
    
    """
    
    Protocols_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-packetheaderstatementrequest.html#cfn-ec2-networkinsightsaccessscope-packetheaderstatementrequest-protocols""", alias="Protocols")
    DestinationPorts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-packetheaderstatementrequest.html#cfn-ec2-networkinsightsaccessscope-packetheaderstatementrequest-destinationports""", alias="DestinationPorts")
    DestinationAddresses_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-packetheaderstatementrequest.html#cfn-ec2-networkinsightsaccessscope-packetheaderstatementrequest-destinationaddresses""", alias="DestinationAddresses")
    DestinationPrefixLists_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-packetheaderstatementrequest.html#cfn-ec2-networkinsightsaccessscope-packetheaderstatementrequest-destinationprefixlists""", alias="DestinationPrefixLists")
    SourceAddresses_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-packetheaderstatementrequest.html#cfn-ec2-networkinsightsaccessscope-packetheaderstatementrequest-sourceaddresses""", alias="SourceAddresses")
    SourcePorts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-packetheaderstatementrequest.html#cfn-ec2-networkinsightsaccessscope-packetheaderstatementrequest-sourceports""", alias="SourcePorts")
    SourcePrefixLists_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-packetheaderstatementrequest.html#cfn-ec2-networkinsightsaccessscope-packetheaderstatementrequest-sourceprefixlists""", alias="SourcePrefixLists")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PacketHeaderStatementRequest:
        from troposphere.ec2 import PacketHeaderStatementRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PathStatementRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-pathstatementrequest.html
    Properties:
        - Name: ResourceStatement
        - Name: PacketHeaderStatement
    
    """
    
    ResourceStatement_: Optional['ResourceStatementRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-pathstatementrequest.html#cfn-ec2-networkinsightsaccessscope-pathstatementrequest-resourcestatement""", alias="ResourceStatement")
    PacketHeaderStatement_: Optional['PacketHeaderStatementRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-pathstatementrequest.html#cfn-ec2-networkinsightsaccessscope-pathstatementrequest-packetheaderstatement""", alias="PacketHeaderStatement")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PathStatementRequest:
        from troposphere.ec2 import PathStatementRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceStatementRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-resourcestatementrequest.html
    Properties:
        - Name: ResourceTypes
        - Name: Resources
    
    """
    
    ResourceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-resourcestatementrequest.html#cfn-ec2-networkinsightsaccessscope-resourcestatementrequest-resourcetypes""", alias="ResourceTypes")
    Resources_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-resourcestatementrequest.html#cfn-ec2-networkinsightsaccessscope-resourcestatementrequest-resources""", alias="Resources")
    


    @property
    def tropo_type(self) -> troposphere.ec2.ResourceStatementRequest:
        from troposphere.ec2 import ResourceStatementRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ThroughResourcesStatementRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-throughresourcesstatementrequest.html
    Properties:
        - Name: ResourceStatement
    
    """
    
    ResourceStatement_: Optional['ResourceStatementRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsaccessscope-throughresourcesstatementrequest.html#cfn-ec2-networkinsightsaccessscope-throughresourcesstatementrequest-resourcestatement""", alias="ResourceStatement")
    


    @property
    def tropo_type(self) -> troposphere.ec2.ThroughResourcesStatementRequest:
        from troposphere.ec2 import ThroughResourcesStatementRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AdditionalDetail(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-additionaldetail.html
    Properties:
        - Name: ServiceName
        - Name: AdditionalDetailType
        - Name: LoadBalancers
        - Name: Component
    
    """
    
    ServiceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-additionaldetail.html#cfn-ec2-networkinsightsanalysis-additionaldetail-servicename""", alias="ServiceName")
    AdditionalDetailType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-additionaldetail.html#cfn-ec2-networkinsightsanalysis-additionaldetail-additionaldetailtype""", alias="AdditionalDetailType")
    LoadBalancers_: Optional[List['AnalysisComponent']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-additionaldetail.html#cfn-ec2-networkinsightsanalysis-additionaldetail-loadbalancers""", alias="LoadBalancers")
    Component_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-additionaldetail.html#cfn-ec2-networkinsightsanalysis-additionaldetail-component""", alias="Component")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AdditionalDetail:
        from troposphere.ec2 import AdditionalDetail as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AlternatePathHint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-alternatepathhint.html
    Properties:
        - Name: ComponentArn
        - Name: ComponentId
    
    """
    
    ComponentArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-alternatepathhint.html#cfn-ec2-networkinsightsanalysis-alternatepathhint-componentarn""", alias="ComponentArn")
    ComponentId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-alternatepathhint.html#cfn-ec2-networkinsightsanalysis-alternatepathhint-componentid""", alias="ComponentId")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AlternatePathHint:
        from troposphere.ec2 import AlternatePathHint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalysisAclRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisaclrule.html
    Properties:
        - Name: PortRange
        - Name: Cidr
        - Name: RuleAction
        - Name: Egress
        - Name: RuleNumber
        - Name: Protocol
    
    """
    
    PortRange_: Optional['PortRange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisaclrule.html#cfn-ec2-networkinsightsanalysis-analysisaclrule-portrange""", alias="PortRange")
    Cidr_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisaclrule.html#cfn-ec2-networkinsightsanalysis-analysisaclrule-cidr""", alias="Cidr")
    RuleAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisaclrule.html#cfn-ec2-networkinsightsanalysis-analysisaclrule-ruleaction""", alias="RuleAction")
    Egress_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisaclrule.html#cfn-ec2-networkinsightsanalysis-analysisaclrule-egress""", alias="Egress")
    RuleNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisaclrule.html#cfn-ec2-networkinsightsanalysis-analysisaclrule-rulenumber""", alias="RuleNumber")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisaclrule.html#cfn-ec2-networkinsightsanalysis-analysisaclrule-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AnalysisAclRule:
        from troposphere.ec2 import AnalysisAclRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalysisComponent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysiscomponent.html
    Properties:
        - Name: Id
        - Name: Arn
    
    """
    
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysiscomponent.html#cfn-ec2-networkinsightsanalysis-analysiscomponent-id""", alias="Id")
    Arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysiscomponent.html#cfn-ec2-networkinsightsanalysis-analysiscomponent-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AnalysisComponent:
        from troposphere.ec2 import AnalysisComponent as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalysisLoadBalancerListener(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisloadbalancerlistener.html
    Properties:
        - Name: InstancePort
        - Name: LoadBalancerPort
    
    """
    
    InstancePort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisloadbalancerlistener.html#cfn-ec2-networkinsightsanalysis-analysisloadbalancerlistener-instanceport""", alias="InstancePort")
    LoadBalancerPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisloadbalancerlistener.html#cfn-ec2-networkinsightsanalysis-analysisloadbalancerlistener-loadbalancerport""", alias="LoadBalancerPort")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AnalysisLoadBalancerListener:
        from troposphere.ec2 import AnalysisLoadBalancerListener as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalysisLoadBalancerTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisloadbalancertarget.html
    Properties:
        - Name: Address
        - Name: Instance
        - Name: Port
        - Name: AvailabilityZone
    
    """
    
    Address_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisloadbalancertarget.html#cfn-ec2-networkinsightsanalysis-analysisloadbalancertarget-address""", alias="Address")
    Instance_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisloadbalancertarget.html#cfn-ec2-networkinsightsanalysis-analysisloadbalancertarget-instance""", alias="Instance")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisloadbalancertarget.html#cfn-ec2-networkinsightsanalysis-analysisloadbalancertarget-port""", alias="Port")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisloadbalancertarget.html#cfn-ec2-networkinsightsanalysis-analysisloadbalancertarget-availabilityzone""", alias="AvailabilityZone")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AnalysisLoadBalancerTarget:
        from troposphere.ec2 import AnalysisLoadBalancerTarget as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalysisPacketHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysispacketheader.html
    Properties:
        - Name: DestinationPortRanges
        - Name: SourcePortRanges
        - Name: DestinationAddresses
        - Name: Protocol
        - Name: SourceAddresses
    
    """
    
    DestinationPortRanges_: Optional[List['PortRange']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysispacketheader.html#cfn-ec2-networkinsightsanalysis-analysispacketheader-destinationportranges""", alias="DestinationPortRanges")
    SourcePortRanges_: Optional[List['PortRange']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysispacketheader.html#cfn-ec2-networkinsightsanalysis-analysispacketheader-sourceportranges""", alias="SourcePortRanges")
    DestinationAddresses_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysispacketheader.html#cfn-ec2-networkinsightsanalysis-analysispacketheader-destinationaddresses""", alias="DestinationAddresses")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysispacketheader.html#cfn-ec2-networkinsightsanalysis-analysispacketheader-protocol""", alias="Protocol")
    SourceAddresses_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysispacketheader.html#cfn-ec2-networkinsightsanalysis-analysispacketheader-sourceaddresses""", alias="SourceAddresses")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AnalysisPacketHeader:
        from troposphere.ec2 import AnalysisPacketHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalysisRouteTableRoute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisroutetableroute.html
    Properties:
        - Name: Origin
        - Name: destinationPrefixListId
        - Name: TransitGatewayId
        - Name: VpcPeeringConnectionId
        - Name: instanceId
        - Name: State
        - Name: egressOnlyInternetGatewayId
        - Name: destinationCidr
        - Name: NetworkInterfaceId
        - Name: NatGatewayId
        - Name: gatewayId
    
    """
    
    Origin_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisroutetableroute.html#cfn-ec2-networkinsightsanalysis-analysisroutetableroute-origin""", alias="Origin")
    destinationPrefixListId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisroutetableroute.html#cfn-ec2-networkinsightsanalysis-analysisroutetableroute-destinationprefixlistid""", alias="destinationPrefixListId")
    TransitGatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisroutetableroute.html#cfn-ec2-networkinsightsanalysis-analysisroutetableroute-transitgatewayid""", alias="TransitGatewayId")
    VpcPeeringConnectionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisroutetableroute.html#cfn-ec2-networkinsightsanalysis-analysisroutetableroute-vpcpeeringconnectionid""", alias="VpcPeeringConnectionId")
    instanceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisroutetableroute.html#cfn-ec2-networkinsightsanalysis-analysisroutetableroute-instanceid""", alias="instanceId")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisroutetableroute.html#cfn-ec2-networkinsightsanalysis-analysisroutetableroute-state""", alias="State")
    egressOnlyInternetGatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisroutetableroute.html#cfn-ec2-networkinsightsanalysis-analysisroutetableroute-egressonlyinternetgatewayid""", alias="egressOnlyInternetGatewayId")
    destinationCidr_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisroutetableroute.html#cfn-ec2-networkinsightsanalysis-analysisroutetableroute-destinationcidr""", alias="destinationCidr")
    NetworkInterfaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisroutetableroute.html#cfn-ec2-networkinsightsanalysis-analysisroutetableroute-networkinterfaceid""", alias="NetworkInterfaceId")
    NatGatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisroutetableroute.html#cfn-ec2-networkinsightsanalysis-analysisroutetableroute-natgatewayid""", alias="NatGatewayId")
    gatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysisroutetableroute.html#cfn-ec2-networkinsightsanalysis-analysisroutetableroute-gatewayid""", alias="gatewayId")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AnalysisRouteTableRoute:
        from troposphere.ec2 import AnalysisRouteTableRoute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalysisSecurityGroupRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysissecuritygrouprule.html
    Properties:
        - Name: PortRange
        - Name: Cidr
        - Name: PrefixListId
        - Name: SecurityGroupId
        - Name: Protocol
        - Name: Direction
    
    """
    
    PortRange_: Optional['PortRange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysissecuritygrouprule.html#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-portrange""", alias="PortRange")
    Cidr_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysissecuritygrouprule.html#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-cidr""", alias="Cidr")
    PrefixListId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysissecuritygrouprule.html#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-prefixlistid""", alias="PrefixListId")
    SecurityGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysissecuritygrouprule.html#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-securitygroupid""", alias="SecurityGroupId")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysissecuritygrouprule.html#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-protocol""", alias="Protocol")
    Direction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-analysissecuritygrouprule.html#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-direction""", alias="Direction")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AnalysisSecurityGroupRule:
        from troposphere.ec2 import AnalysisSecurityGroupRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Explanation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html
    Properties:
        - Name: VpnGateway
        - Name: PacketField
        - Name: TransitGatewayAttachment
        - Name: Protocols
        - Name: IngressRouteTable
        - Name: ClassicLoadBalancerListener
        - Name: VpcPeeringConnection
        - Name: Address
        - Name: Port
        - Name: Addresses
        - Name: ElasticLoadBalancerListener
        - Name: TransitGatewayRouteTable
        - Name: ExplanationCode
        - Name: InternetGateway
        - Name: SourceVpc
        - Name: AttachedTo
        - Name: PrefixList
        - Name: TransitGatewayRouteTableRoute
        - Name: ComponentRegion
        - Name: LoadBalancerTargetGroup
        - Name: NetworkInterface
        - Name: CustomerGateway
        - Name: DestinationVpc
        - Name: SecurityGroup
        - Name: TransitGateway
        - Name: RouteTable
        - Name: State
        - Name: LoadBalancerListenerPort
        - Name: vpcEndpoint
        - Name: Subnet
        - Name: Cidrs
        - Name: Destination
        - Name: SecurityGroups
        - Name: ComponentAccount
        - Name: VpnConnection
        - Name: Vpc
        - Name: NatGateway
        - Name: Direction
        - Name: LoadBalancerTargetPort
        - Name: LoadBalancerTarget
        - Name: LoadBalancerTargetGroups
        - Name: Component
        - Name: MissingComponent
        - Name: RouteTableRoute
        - Name: AvailabilityZones
        - Name: PortRanges
        - Name: Acl
        - Name: SecurityGroupRule
        - Name: SubnetRouteTable
        - Name: LoadBalancerArn
        - Name: AclRule
    
    """
    
    VpnGateway_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-vpngateway""", alias="VpnGateway")
    PacketField_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-packetfield""", alias="PacketField")
    TransitGatewayAttachment_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-transitgatewayattachment""", alias="TransitGatewayAttachment")
    Protocols_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-protocols""", alias="Protocols")
    IngressRouteTable_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-ingressroutetable""", alias="IngressRouteTable")
    ClassicLoadBalancerListener_: Optional['AnalysisLoadBalancerListener'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-classicloadbalancerlistener""", alias="ClassicLoadBalancerListener")
    VpcPeeringConnection_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-vpcpeeringconnection""", alias="VpcPeeringConnection")
    Address_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-address""", alias="Address")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-port""", alias="Port")
    Addresses_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-addresses""", alias="Addresses")
    ElasticLoadBalancerListener_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-elasticloadbalancerlistener""", alias="ElasticLoadBalancerListener")
    TransitGatewayRouteTable_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-transitgatewayroutetable""", alias="TransitGatewayRouteTable")
    ExplanationCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-explanationcode""", alias="ExplanationCode")
    InternetGateway_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-internetgateway""", alias="InternetGateway")
    SourceVpc_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-sourcevpc""", alias="SourceVpc")
    AttachedTo_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-attachedto""", alias="AttachedTo")
    PrefixList_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-prefixlist""", alias="PrefixList")
    TransitGatewayRouteTableRoute_: Optional['TransitGatewayRouteTableRoute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-transitgatewayroutetableroute""", alias="TransitGatewayRouteTableRoute")
    ComponentRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-componentregion""", alias="ComponentRegion")
    LoadBalancerTargetGroup_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-loadbalancertargetgroup""", alias="LoadBalancerTargetGroup")
    NetworkInterface_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-networkinterface""", alias="NetworkInterface")
    CustomerGateway_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-customergateway""", alias="CustomerGateway")
    DestinationVpc_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-destinationvpc""", alias="DestinationVpc")
    SecurityGroup_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-securitygroup""", alias="SecurityGroup")
    TransitGateway_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-transitgateway""", alias="TransitGateway")
    RouteTable_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-routetable""", alias="RouteTable")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-state""", alias="State")
    LoadBalancerListenerPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-loadbalancerlistenerport""", alias="LoadBalancerListenerPort")
    vpcEndpoint_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-vpcendpoint""", alias="vpcEndpoint")
    Subnet_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-subnet""", alias="Subnet")
    Cidrs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-cidrs""", alias="Cidrs")
    Destination_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-destination""", alias="Destination")
    SecurityGroups_: Optional[List['AnalysisComponent']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-securitygroups""", alias="SecurityGroups")
    ComponentAccount_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-componentaccount""", alias="ComponentAccount")
    VpnConnection_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-vpnconnection""", alias="VpnConnection")
    Vpc_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-vpc""", alias="Vpc")
    NatGateway_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-natgateway""", alias="NatGateway")
    Direction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-direction""", alias="Direction")
    LoadBalancerTargetPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-loadbalancertargetport""", alias="LoadBalancerTargetPort")
    LoadBalancerTarget_: Optional['AnalysisLoadBalancerTarget'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-loadbalancertarget""", alias="LoadBalancerTarget")
    LoadBalancerTargetGroups_: Optional[List['AnalysisComponent']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-loadbalancertargetgroups""", alias="LoadBalancerTargetGroups")
    Component_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-component""", alias="Component")
    MissingComponent_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-missingcomponent""", alias="MissingComponent")
    RouteTableRoute_: Optional['AnalysisRouteTableRoute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-routetableroute""", alias="RouteTableRoute")
    AvailabilityZones_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-availabilityzones""", alias="AvailabilityZones")
    PortRanges_: Optional[List['PortRange']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-portranges""", alias="PortRanges")
    Acl_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-acl""", alias="Acl")
    SecurityGroupRule_: Optional['AnalysisSecurityGroupRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-securitygrouprule""", alias="SecurityGroupRule")
    SubnetRouteTable_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-subnetroutetable""", alias="SubnetRouteTable")
    LoadBalancerArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-loadbalancerarn""", alias="LoadBalancerArn")
    AclRule_: Optional['AnalysisAclRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-explanation.html#cfn-ec2-networkinsightsanalysis-explanation-aclrule""", alias="AclRule")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Explanation:
        from troposphere.ec2 import Explanation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PathComponent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html
    Properties:
        - Name: AdditionalDetails
        - Name: InboundHeader
        - Name: Vpc
        - Name: DestinationVpc
        - Name: SecurityGroupRule
        - Name: TransitGateway
        - Name: ElasticLoadBalancerListener
        - Name: Explanations
        - Name: ServiceName
        - Name: SequenceNumber
        - Name: SourceVpc
        - Name: OutboundHeader
        - Name: AclRule
        - Name: TransitGatewayRouteTableRoute
        - Name: Component
        - Name: Subnet
        - Name: RouteTableRoute
    
    """
    
    AdditionalDetails_: Optional[List['AdditionalDetail']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-additionaldetails""", alias="AdditionalDetails")
    InboundHeader_: Optional['AnalysisPacketHeader'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-inboundheader""", alias="InboundHeader")
    Vpc_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-vpc""", alias="Vpc")
    DestinationVpc_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-destinationvpc""", alias="DestinationVpc")
    SecurityGroupRule_: Optional['AnalysisSecurityGroupRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-securitygrouprule""", alias="SecurityGroupRule")
    TransitGateway_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-transitgateway""", alias="TransitGateway")
    ElasticLoadBalancerListener_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-elasticloadbalancerlistener""", alias="ElasticLoadBalancerListener")
    Explanations_: Optional[List['Explanation']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-explanations""", alias="Explanations")
    ServiceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-servicename""", alias="ServiceName")
    SequenceNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-sequencenumber""", alias="SequenceNumber")
    SourceVpc_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-sourcevpc""", alias="SourceVpc")
    OutboundHeader_: Optional['AnalysisPacketHeader'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-outboundheader""", alias="OutboundHeader")
    AclRule_: Optional['AnalysisAclRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-aclrule""", alias="AclRule")
    TransitGatewayRouteTableRoute_: Optional['TransitGatewayRouteTableRoute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-transitgatewayroutetableroute""", alias="TransitGatewayRouteTableRoute")
    Component_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-component""", alias="Component")
    Subnet_: Optional['AnalysisComponent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-subnet""", alias="Subnet")
    RouteTableRoute_: Optional['AnalysisRouteTableRoute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-pathcomponent.html#cfn-ec2-networkinsightsanalysis-pathcomponent-routetableroute""", alias="RouteTableRoute")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PathComponent:
        from troposphere.ec2 import PathComponent as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PortRange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-portrange.html
    Properties:
        - Name: From
        - Name: To
    
    """
    
    From_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-portrange.html#cfn-ec2-networkinsightsanalysis-portrange-from""", alias="From")
    To_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-portrange.html#cfn-ec2-networkinsightsanalysis-portrange-to""", alias="To")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PortRange:
        from troposphere.ec2 import PortRange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TransitGatewayRouteTableRoute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-transitgatewayroutetableroute.html
    Properties:
        - Name: PrefixListId
        - Name: ResourceId
        - Name: State
        - Name: ResourceType
        - Name: RouteOrigin
        - Name: DestinationCidr
        - Name: AttachmentId
    
    """
    
    PrefixListId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-transitgatewayroutetableroute.html#cfn-ec2-networkinsightsanalysis-transitgatewayroutetableroute-prefixlistid""", alias="PrefixListId")
    ResourceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-transitgatewayroutetableroute.html#cfn-ec2-networkinsightsanalysis-transitgatewayroutetableroute-resourceid""", alias="ResourceId")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-transitgatewayroutetableroute.html#cfn-ec2-networkinsightsanalysis-transitgatewayroutetableroute-state""", alias="State")
    ResourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-transitgatewayroutetableroute.html#cfn-ec2-networkinsightsanalysis-transitgatewayroutetableroute-resourcetype""", alias="ResourceType")
    RouteOrigin_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-transitgatewayroutetableroute.html#cfn-ec2-networkinsightsanalysis-transitgatewayroutetableroute-routeorigin""", alias="RouteOrigin")
    DestinationCidr_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-transitgatewayroutetableroute.html#cfn-ec2-networkinsightsanalysis-transitgatewayroutetableroute-destinationcidr""", alias="DestinationCidr")
    AttachmentId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-transitgatewayroutetableroute.html#cfn-ec2-networkinsightsanalysis-transitgatewayroutetableroute-attachmentid""", alias="AttachmentId")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayRouteTableRoute:
        from troposphere.ec2 import TransitGatewayRouteTableRoute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FilterPortRange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightspath-filterportrange.html
    Properties:
        - Name: FromPort
        - Name: ToPort
    
    """
    
    FromPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightspath-filterportrange.html#cfn-ec2-networkinsightspath-filterportrange-fromport""", alias="FromPort")
    ToPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightspath-filterportrange.html#cfn-ec2-networkinsightspath-filterportrange-toport""", alias="ToPort")
    


    @property
    def tropo_type(self) -> troposphere.ec2.FilterPortRange:
        from troposphere.ec2 import FilterPortRange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PathFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightspath-pathfilter.html
    Properties:
        - Name: SourceAddress
        - Name: DestinationPortRange
        - Name: SourcePortRange
        - Name: DestinationAddress
    
    """
    
    SourceAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightspath-pathfilter.html#cfn-ec2-networkinsightspath-pathfilter-sourceaddress""", alias="SourceAddress")
    DestinationPortRange_: Optional['FilterPortRange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightspath-pathfilter.html#cfn-ec2-networkinsightspath-pathfilter-destinationportrange""", alias="DestinationPortRange")
    SourcePortRange_: Optional['FilterPortRange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightspath-pathfilter.html#cfn-ec2-networkinsightspath-pathfilter-sourceportrange""", alias="SourcePortRange")
    DestinationAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightspath-pathfilter.html#cfn-ec2-networkinsightspath-pathfilter-destinationaddress""", alias="DestinationAddress")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PathFilter:
        from troposphere.ec2 import PathFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceIpv6Address(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinterface-instanceipv6address.html
    Properties:
        - Name: Ipv6Address
    
    """
    
    Ipv6Address_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinterface-instanceipv6address.html#cfn-ec2-networkinterface-instanceipv6address-ipv6address""", alias="Ipv6Address")
    


    @property
    def tropo_type(self) -> troposphere.ec2.InstanceIpv6Address:
        from troposphere.ec2 import InstanceIpv6Address as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ipv4PrefixSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinterface-ipv4prefixspecification.html
    Properties:
        - Name: Ipv4Prefix
    
    """
    
    Ipv4Prefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinterface-ipv4prefixspecification.html#cfn-ec2-networkinterface-ipv4prefixspecification-ipv4prefix""", alias="Ipv4Prefix")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Ipv4PrefixSpecification:
        from troposphere.ec2 import Ipv4PrefixSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ipv6PrefixSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinterface-ipv6prefixspecification.html
    Properties:
        - Name: Ipv6Prefix
    
    """
    
    Ipv6Prefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinterface-ipv6prefixspecification.html#cfn-ec2-networkinterface-ipv6prefixspecification-ipv6prefix""", alias="Ipv6Prefix")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Ipv6PrefixSpecification:
        from troposphere.ec2 import Ipv6PrefixSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateIpAddressSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinterface-privateipaddressspecification.html
    Properties:
        - Name: PrivateIpAddress
        - Name: Primary
    
    """
    
    PrivateIpAddress_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinterface-privateipaddressspecification.html#cfn-ec2-networkinterface-privateipaddressspecification-privateipaddress""", alias="PrivateIpAddress")
    Primary_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinterface-privateipaddressspecification.html#cfn-ec2-networkinterface-privateipaddressspecification-primary""", alias="Primary")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PrivateIpAddressSpecification:
        from troposphere.ec2 import PrivateIpAddressSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Entry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-prefixlist-entry.html
    Properties:
        - Name: Description
        - Name: Cidr
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-prefixlist-entry.html#cfn-ec2-prefixlist-entry-description""", alias="Description")
    Cidr_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-prefixlist-entry.html#cfn-ec2-prefixlist-entry-cidr""", alias="Cidr")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Entry:
        from troposphere.ec2 import Entry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Egress(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html
    Properties:
        - Name: CidrIp
        - Name: CidrIpv6
        - Name: Description
        - Name: DestinationPrefixListId
        - Name: DestinationSecurityGroupId
        - Name: FromPort
        - Name: IpProtocol
        - Name: ToPort
    
    """
    
    CidrIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-cidrip""", alias="CidrIp")
    CidrIpv6_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-cidripv6""", alias="CidrIpv6")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-description""", alias="Description")
    DestinationPrefixListId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-destinationprefixlistid""", alias="DestinationPrefixListId")
    DestinationSecurityGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-destsecgroupid""", alias="DestinationSecurityGroupId")
    FromPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-fromport""", alias="FromPort")
    IpProtocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-ipprotocol""", alias="IpProtocol")
    ToPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-toport""", alias="ToPort")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Egress:
        from troposphere.ec2 import Egress as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ingress(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html
    Properties:
        - Name: CidrIp
        - Name: CidrIpv6
        - Name: Description
        - Name: FromPort
        - Name: IpProtocol
        - Name: SourcePrefixListId
        - Name: SourceSecurityGroupId
        - Name: SourceSecurityGroupName
        - Name: SourceSecurityGroupOwnerId
        - Name: ToPort
    
    """
    
    CidrIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-cidrip""", alias="CidrIp")
    CidrIpv6_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-cidripv6""", alias="CidrIpv6")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-description""", alias="Description")
    FromPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-fromport""", alias="FromPort")
    IpProtocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-ipprotocol""", alias="IpProtocol")
    SourcePrefixListId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-securitygroup-ingress-sourceprefixlistid""", alias="SourcePrefixListId")
    SourceSecurityGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-sourcesecuritygroupid""", alias="SourceSecurityGroupId")
    SourceSecurityGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-sourcesecuritygroupname""", alias="SourceSecurityGroupName")
    SourceSecurityGroupOwnerId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-sourcesecuritygroupownerid""", alias="SourceSecurityGroupOwnerId")
    ToPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-toport""", alias="ToPort")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Ingress:
        from troposphere.ec2 import Ingress as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AcceleratorCountRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-acceleratorcountrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-acceleratorcountrequest.html#cfn-ec2-spotfleet-acceleratorcountrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-acceleratorcountrequest.html#cfn-ec2-spotfleet-acceleratorcountrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AcceleratorCountRequest:
        from troposphere.ec2 import AcceleratorCountRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AcceleratorTotalMemoryMiBRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-acceleratortotalmemorymibrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-acceleratortotalmemorymibrequest.html#cfn-ec2-spotfleet-acceleratortotalmemorymibrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-acceleratortotalmemorymibrequest.html#cfn-ec2-spotfleet-acceleratortotalmemorymibrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.AcceleratorTotalMemoryMiBRequest:
        from troposphere.ec2 import AcceleratorTotalMemoryMiBRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BaselineEbsBandwidthMbpsRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-baselineebsbandwidthmbpsrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-baselineebsbandwidthmbpsrequest.html#cfn-ec2-spotfleet-baselineebsbandwidthmbpsrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-baselineebsbandwidthmbpsrequest.html#cfn-ec2-spotfleet-baselineebsbandwidthmbpsrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.BaselineEbsBandwidthMbpsRequest:
        from troposphere.ec2 import BaselineEbsBandwidthMbpsRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BlockDeviceMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-blockdevicemapping.html
    Properties:
        - Name: Ebs
        - Name: NoDevice
        - Name: VirtualName
        - Name: DeviceName
    
    """
    
    Ebs_: Optional['EbsBlockDevice'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-blockdevicemapping.html#cfn-ec2-spotfleet-blockdevicemapping-ebs""", alias="Ebs")
    NoDevice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-blockdevicemapping.html#cfn-ec2-spotfleet-blockdevicemapping-nodevice""", alias="NoDevice")
    VirtualName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-blockdevicemapping.html#cfn-ec2-spotfleet-blockdevicemapping-virtualname""", alias="VirtualName")
    DeviceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-blockdevicemapping.html#cfn-ec2-spotfleet-blockdevicemapping-devicename""", alias="DeviceName")
    


    @property
    def tropo_type(self) -> troposphere.ec2.BlockDeviceMapping:
        from troposphere.ec2 import BlockDeviceMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClassicLoadBalancer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-classicloadbalancer.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-classicloadbalancer.html#cfn-ec2-spotfleet-classicloadbalancer-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ec2.ClassicLoadBalancer:
        from troposphere.ec2 import ClassicLoadBalancer as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClassicLoadBalancersConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-classicloadbalancersconfig.html
    Properties:
        - Name: ClassicLoadBalancers
    
    """
    
    ClassicLoadBalancers_: List['ClassicLoadBalancer'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-classicloadbalancersconfig.html#cfn-ec2-spotfleet-classicloadbalancersconfig-classicloadbalancers""", alias="ClassicLoadBalancers")
    


    @property
    def tropo_type(self) -> troposphere.ec2.ClassicLoadBalancersConfig:
        from troposphere.ec2 import ClassicLoadBalancersConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EbsBlockDevice(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-ebsblockdevice.html
    Properties:
        - Name: SnapshotId
        - Name: VolumeType
        - Name: Encrypted
        - Name: Iops
        - Name: VolumeSize
        - Name: DeleteOnTermination
    
    """
    
    SnapshotId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-ebsblockdevice.html#cfn-ec2-spotfleet-ebsblockdevice-snapshotid""", alias="SnapshotId")
    VolumeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-ebsblockdevice.html#cfn-ec2-spotfleet-ebsblockdevice-volumetype""", alias="VolumeType")
    Encrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-ebsblockdevice.html#cfn-ec2-spotfleet-ebsblockdevice-encrypted""", alias="Encrypted")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-ebsblockdevice.html#cfn-ec2-spotfleet-ebsblockdevice-iops""", alias="Iops")
    VolumeSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-ebsblockdevice.html#cfn-ec2-spotfleet-ebsblockdevice-volumesize""", alias="VolumeSize")
    DeleteOnTermination_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-ebsblockdevice.html#cfn-ec2-spotfleet-ebsblockdevice-deleteontermination""", alias="DeleteOnTermination")
    


    @property
    def tropo_type(self) -> troposphere.ec2.EbsBlockDevice:
        from troposphere.ec2 import EbsBlockDevice as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FleetLaunchTemplateSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification.html
    Properties:
        - Name: LaunchTemplateName
        - Name: Version
        - Name: LaunchTemplateId
    
    """
    
    LaunchTemplateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification.html#cfn-ec2-spotfleet-fleetlaunchtemplatespecification-launchtemplatename""", alias="LaunchTemplateName")
    Version_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification.html#cfn-ec2-spotfleet-fleetlaunchtemplatespecification-version""", alias="Version")
    LaunchTemplateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification.html#cfn-ec2-spotfleet-fleetlaunchtemplatespecification-launchtemplateid""", alias="LaunchTemplateId")
    


    @property
    def tropo_type(self) -> troposphere.ec2.FleetLaunchTemplateSpecification:
        from troposphere.ec2 import FleetLaunchTemplateSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GroupIdentifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-groupidentifier.html
    Properties:
        - Name: GroupId
    
    """
    
    GroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-groupidentifier.html#cfn-ec2-spotfleet-groupidentifier-groupid""", alias="GroupId")
    


    @property
    def tropo_type(self) -> troposphere.ec2.GroupIdentifier:
        from troposphere.ec2 import GroupIdentifier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IamInstanceProfileSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-iaminstanceprofilespecification.html
    Properties:
        - Name: Arn
    
    """
    
    Arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-iaminstanceprofilespecification.html#cfn-ec2-spotfleet-iaminstanceprofilespecification-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.ec2.IamInstanceProfileSpecification:
        from troposphere.ec2 import IamInstanceProfileSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceIpv6Address(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instanceipv6address.html
    Properties:
        - Name: Ipv6Address
    
    """
    
    Ipv6Address_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instanceipv6address.html#cfn-ec2-spotfleet-instanceipv6address-ipv6address""", alias="Ipv6Address")
    


    @property
    def tropo_type(self) -> troposphere.ec2.InstanceIpv6Address:
        from troposphere.ec2 import InstanceIpv6Address as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceNetworkInterfaceSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancenetworkinterfacespecification.html
    Properties:
        - Name: Description
        - Name: PrivateIpAddresses
        - Name: SecondaryPrivateIpAddressCount
        - Name: DeviceIndex
        - Name: Groups
        - Name: Ipv6AddressCount
        - Name: Ipv6Addresses
        - Name: SubnetId
        - Name: AssociatePublicIpAddress
        - Name: NetworkInterfaceId
        - Name: DeleteOnTermination
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancenetworkinterfacespecification.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-description""", alias="Description")
    PrivateIpAddresses_: Optional[List['PrivateIpAddressSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancenetworkinterfacespecification.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-privateipaddresses""", alias="PrivateIpAddresses")
    SecondaryPrivateIpAddressCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancenetworkinterfacespecification.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-secondaryprivateipaddresscount""", alias="SecondaryPrivateIpAddressCount")
    DeviceIndex_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancenetworkinterfacespecification.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-deviceindex""", alias="DeviceIndex")
    Groups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancenetworkinterfacespecification.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-groups""", alias="Groups")
    Ipv6AddressCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancenetworkinterfacespecification.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-ipv6addresscount""", alias="Ipv6AddressCount")
    Ipv6Addresses_: Optional[List['InstanceIpv6Address']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancenetworkinterfacespecification.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-ipv6addresses""", alias="Ipv6Addresses")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancenetworkinterfacespecification.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-subnetid""", alias="SubnetId")
    AssociatePublicIpAddress_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancenetworkinterfacespecification.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-associatepublicipaddress""", alias="AssociatePublicIpAddress")
    NetworkInterfaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancenetworkinterfacespecification.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-networkinterfaceid""", alias="NetworkInterfaceId")
    DeleteOnTermination_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancenetworkinterfacespecification.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-deleteontermination""", alias="DeleteOnTermination")
    


    @property
    def tropo_type(self) -> troposphere.ec2.InstanceNetworkInterfaceSpecification:
        from troposphere.ec2 import InstanceNetworkInterfaceSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceRequirementsRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html
    Properties:
        - Name: LocalStorageTypes
        - Name: InstanceGenerations
        - Name: NetworkInterfaceCount
        - Name: MemoryGiBPerVCpu
        - Name: AcceleratorTypes
        - Name: VCpuCount
        - Name: ExcludedInstanceTypes
        - Name: AcceleratorManufacturers
        - Name: AllowedInstanceTypes
        - Name: LocalStorage
        - Name: CpuManufacturers
        - Name: NetworkBandwidthGbps
        - Name: AcceleratorCount
        - Name: BareMetal
        - Name: RequireHibernateSupport
        - Name: SpotMaxPricePercentageOverLowestPrice
        - Name: BaselineEbsBandwidthMbps
        - Name: OnDemandMaxPricePercentageOverLowestPrice
        - Name: AcceleratorNames
        - Name: AcceleratorTotalMemoryMiB
        - Name: BurstablePerformance
        - Name: MemoryMiB
        - Name: TotalLocalStorageGB
    
    """
    
    LocalStorageTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-localstoragetypes""", alias="LocalStorageTypes")
    InstanceGenerations_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-instancegenerations""", alias="InstanceGenerations")
    NetworkInterfaceCount_: Optional['NetworkInterfaceCountRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-networkinterfacecount""", alias="NetworkInterfaceCount")
    MemoryGiBPerVCpu_: Optional['MemoryGiBPerVCpuRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-memorygibpervcpu""", alias="MemoryGiBPerVCpu")
    AcceleratorTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-acceleratortypes""", alias="AcceleratorTypes")
    VCpuCount_: Optional['VCpuCountRangeRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-vcpucount""", alias="VCpuCount")
    ExcludedInstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-excludedinstancetypes""", alias="ExcludedInstanceTypes")
    AcceleratorManufacturers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-acceleratormanufacturers""", alias="AcceleratorManufacturers")
    AllowedInstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-allowedinstancetypes""", alias="AllowedInstanceTypes")
    LocalStorage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-localstorage""", alias="LocalStorage")
    CpuManufacturers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-cpumanufacturers""", alias="CpuManufacturers")
    NetworkBandwidthGbps_: Optional['NetworkBandwidthGbpsRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-networkbandwidthgbps""", alias="NetworkBandwidthGbps")
    AcceleratorCount_: Optional['AcceleratorCountRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-acceleratorcount""", alias="AcceleratorCount")
    BareMetal_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-baremetal""", alias="BareMetal")
    RequireHibernateSupport_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-requirehibernatesupport""", alias="RequireHibernateSupport")
    SpotMaxPricePercentageOverLowestPrice_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-spotmaxpricepercentageoverlowestprice""", alias="SpotMaxPricePercentageOverLowestPrice")
    BaselineEbsBandwidthMbps_: Optional['BaselineEbsBandwidthMbpsRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-baselineebsbandwidthmbps""", alias="BaselineEbsBandwidthMbps")
    OnDemandMaxPricePercentageOverLowestPrice_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-ondemandmaxpricepercentageoverlowestprice""", alias="OnDemandMaxPricePercentageOverLowestPrice")
    AcceleratorNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-acceleratornames""", alias="AcceleratorNames")
    AcceleratorTotalMemoryMiB_: Optional['AcceleratorTotalMemoryMiBRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-acceleratortotalmemorymib""", alias="AcceleratorTotalMemoryMiB")
    BurstablePerformance_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-burstableperformance""", alias="BurstablePerformance")
    MemoryMiB_: Optional['MemoryMiBRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-memorymib""", alias="MemoryMiB")
    TotalLocalStorageGB_: Optional['TotalLocalStorageGBRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html#cfn-ec2-spotfleet-instancerequirementsrequest-totallocalstoragegb""", alias="TotalLocalStorageGB")
    


    @property
    def tropo_type(self) -> troposphere.ec2.InstanceRequirementsRequest:
        from troposphere.ec2 import InstanceRequirementsRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchTemplateConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateconfig.html
    Properties:
        - Name: LaunchTemplateSpecification
        - Name: Overrides
    
    """
    
    LaunchTemplateSpecification_: Optional['FleetLaunchTemplateSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateconfig.html#cfn-ec2-spotfleet-launchtemplateconfig-launchtemplatespecification""", alias="LaunchTemplateSpecification")
    Overrides_: Optional[List['LaunchTemplateOverrides']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateconfig.html#cfn-ec2-spotfleet-launchtemplateconfig-overrides""", alias="Overrides")
    


    @property
    def tropo_type(self) -> troposphere.ec2.LaunchTemplateConfig:
        from troposphere.ec2 import LaunchTemplateConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchTemplateOverrides(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html
    Properties:
        - Name: SpotPrice
        - Name: WeightedCapacity
        - Name: Priority
        - Name: AvailabilityZone
        - Name: SubnetId
        - Name: InstanceRequirements
        - Name: InstanceType
    
    """
    
    SpotPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html#cfn-ec2-spotfleet-launchtemplateoverrides-spotprice""", alias="SpotPrice")
    WeightedCapacity_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html#cfn-ec2-spotfleet-launchtemplateoverrides-weightedcapacity""", alias="WeightedCapacity")
    Priority_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html#cfn-ec2-spotfleet-launchtemplateoverrides-priority""", alias="Priority")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html#cfn-ec2-spotfleet-launchtemplateoverrides-availabilityzone""", alias="AvailabilityZone")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html#cfn-ec2-spotfleet-launchtemplateoverrides-subnetid""", alias="SubnetId")
    InstanceRequirements_: Optional['InstanceRequirementsRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html#cfn-ec2-spotfleet-launchtemplateoverrides-instancerequirements""", alias="InstanceRequirements")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html#cfn-ec2-spotfleet-launchtemplateoverrides-instancetype""", alias="InstanceType")
    


    @property
    def tropo_type(self) -> troposphere.ec2.LaunchTemplateOverrides:
        from troposphere.ec2 import LaunchTemplateOverrides as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoadBalancersConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-loadbalancersconfig.html
    Properties:
        - Name: ClassicLoadBalancersConfig
        - Name: TargetGroupsConfig
    
    """
    
    ClassicLoadBalancersConfig_: Optional['ClassicLoadBalancersConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-loadbalancersconfig.html#cfn-ec2-spotfleet-loadbalancersconfig-classicloadbalancersconfig""", alias="ClassicLoadBalancersConfig")
    TargetGroupsConfig_: Optional['TargetGroupsConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-loadbalancersconfig.html#cfn-ec2-spotfleet-loadbalancersconfig-targetgroupsconfig""", alias="TargetGroupsConfig")
    


    @property
    def tropo_type(self) -> troposphere.ec2.LoadBalancersConfig:
        from troposphere.ec2 import LoadBalancersConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MemoryGiBPerVCpuRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-memorygibpervcpurequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-memorygibpervcpurequest.html#cfn-ec2-spotfleet-memorygibpervcpurequest-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-memorygibpervcpurequest.html#cfn-ec2-spotfleet-memorygibpervcpurequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.MemoryGiBPerVCpuRequest:
        from troposphere.ec2 import MemoryGiBPerVCpuRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MemoryMiBRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-memorymibrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-memorymibrequest.html#cfn-ec2-spotfleet-memorymibrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-memorymibrequest.html#cfn-ec2-spotfleet-memorymibrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.MemoryMiBRequest:
        from troposphere.ec2 import MemoryMiBRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkBandwidthGbpsRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest.html#cfn-ec2-spotfleet-networkbandwidthgbpsrequest-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest.html#cfn-ec2-spotfleet-networkbandwidthgbpsrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.NetworkBandwidthGbpsRequest:
        from troposphere.ec2 import NetworkBandwidthGbpsRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkInterfaceCountRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkinterfacecountrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkinterfacecountrequest.html#cfn-ec2-spotfleet-networkinterfacecountrequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkinterfacecountrequest.html#cfn-ec2-spotfleet-networkinterfacecountrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.NetworkInterfaceCountRequest:
        from troposphere.ec2 import NetworkInterfaceCountRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateIpAddressSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-privateipaddressspecification.html
    Properties:
        - Name: PrivateIpAddress
        - Name: Primary
    
    """
    
    PrivateIpAddress_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-privateipaddressspecification.html#cfn-ec2-spotfleet-privateipaddressspecification-privateipaddress""", alias="PrivateIpAddress")
    Primary_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-privateipaddressspecification.html#cfn-ec2-spotfleet-privateipaddressspecification-primary""", alias="Primary")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PrivateIpAddressSpecification:
        from troposphere.ec2 import PrivateIpAddressSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpotCapacityRebalance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotcapacityrebalance.html
    Properties:
        - Name: TerminationDelay
        - Name: ReplacementStrategy
    
    """
    
    TerminationDelay_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotcapacityrebalance.html#cfn-ec2-spotfleet-spotcapacityrebalance-terminationdelay""", alias="TerminationDelay")
    ReplacementStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotcapacityrebalance.html#cfn-ec2-spotfleet-spotcapacityrebalance-replacementstrategy""", alias="ReplacementStrategy")
    


    @property
    def tropo_type(self) -> troposphere.ec2.SpotCapacityRebalance:
        from troposphere.ec2 import SpotCapacityRebalance as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpotFleetLaunchSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html
    Properties:
        - Name: SecurityGroups
        - Name: TagSpecifications
        - Name: UserData
        - Name: BlockDeviceMappings
        - Name: IamInstanceProfile
        - Name: KernelId
        - Name: SubnetId
        - Name: EbsOptimized
        - Name: KeyName
        - Name: RamdiskId
        - Name: SpotPrice
        - Name: WeightedCapacity
        - Name: Placement
        - Name: NetworkInterfaces
        - Name: ImageId
        - Name: InstanceRequirements
        - Name: InstanceType
        - Name: Monitoring
    
    """
    
    SecurityGroups_: Optional[List['GroupIdentifier']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-securitygroups""", alias="SecurityGroups")
    TagSpecifications_: Optional[List['SpotFleetTagSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-tagspecifications""", alias="TagSpecifications")
    UserData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-userdata""", alias="UserData")
    BlockDeviceMappings_: Optional[List['BlockDeviceMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-blockdevicemappings""", alias="BlockDeviceMappings")
    IamInstanceProfile_: Optional['IamInstanceProfileSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-iaminstanceprofile""", alias="IamInstanceProfile")
    KernelId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-kernelid""", alias="KernelId")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-subnetid""", alias="SubnetId")
    EbsOptimized_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-ebsoptimized""", alias="EbsOptimized")
    KeyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-keyname""", alias="KeyName")
    RamdiskId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-ramdiskid""", alias="RamdiskId")
    SpotPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-spotprice""", alias="SpotPrice")
    WeightedCapacity_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-weightedcapacity""", alias="WeightedCapacity")
    Placement_: Optional['SpotPlacement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-placement""", alias="Placement")
    NetworkInterfaces_: Optional[List['InstanceNetworkInterfaceSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-networkinterfaces""", alias="NetworkInterfaces")
    ImageId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-imageid""", alias="ImageId")
    InstanceRequirements_: Optional['InstanceRequirementsRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-instancerequirements""", alias="InstanceRequirements")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-instancetype""", alias="InstanceType")
    Monitoring_: Optional['SpotFleetMonitoring'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-monitoring""", alias="Monitoring")
    


    @property
    def tropo_type(self) -> troposphere.ec2.SpotFleetLaunchSpecification:
        from troposphere.ec2 import SpotFleetLaunchSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpotFleetMonitoring(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetmonitoring.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetmonitoring.html#cfn-ec2-spotfleet-spotfleetmonitoring-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.ec2.SpotFleetMonitoring:
        from troposphere.ec2 import SpotFleetMonitoring as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpotFleetRequestConfigData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html
    Properties:
        - Name: Context
        - Name: SpotMaxTotalPrice
        - Name: ExcessCapacityTerminationPolicy
        - Name: TagSpecifications
        - Name: InstancePoolsToUseCount
        - Name: LaunchTemplateConfigs
        - Name: TargetCapacityUnitType
        - Name: IamFleetRole
        - Name: SpotMaintenanceStrategies
        - Name: TerminateInstancesWithExpiration
        - Name: ValidUntil
        - Name: OnDemandMaxTotalPrice
        - Name: OnDemandAllocationStrategy
        - Name: SpotPrice
        - Name: AllocationStrategy
        - Name: OnDemandTargetCapacity
        - Name: Type
        - Name: LaunchSpecifications
        - Name: InstanceInterruptionBehavior
        - Name: LoadBalancersConfig
        - Name: ValidFrom
        - Name: ReplaceUnhealthyInstances
        - Name: TargetCapacity
    
    """
    
    Context_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-context""", alias="Context")
    SpotMaxTotalPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-spotmaxtotalprice""", alias="SpotMaxTotalPrice")
    ExcessCapacityTerminationPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-excesscapacityterminationpolicy""", alias="ExcessCapacityTerminationPolicy")
    TagSpecifications_: Optional[List['SpotFleetTagSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-tagspecifications""", alias="TagSpecifications")
    InstancePoolsToUseCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-instancepoolstousecount""", alias="InstancePoolsToUseCount")
    LaunchTemplateConfigs_: Optional[List['LaunchTemplateConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-launchtemplateconfigs""", alias="LaunchTemplateConfigs")
    TargetCapacityUnitType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-targetcapacityunittype""", alias="TargetCapacityUnitType")
    IamFleetRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-iamfleetrole""", alias="IamFleetRole")
    SpotMaintenanceStrategies_: Optional['SpotMaintenanceStrategies'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-spotmaintenancestrategies""", alias="SpotMaintenanceStrategies")
    TerminateInstancesWithExpiration_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-terminateinstanceswithexpiration""", alias="TerminateInstancesWithExpiration")
    ValidUntil_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-validuntil""", alias="ValidUntil")
    OnDemandMaxTotalPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-ondemandmaxtotalprice""", alias="OnDemandMaxTotalPrice")
    OnDemandAllocationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-ondemandallocationstrategy""", alias="OnDemandAllocationStrategy")
    SpotPrice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-spotprice""", alias="SpotPrice")
    AllocationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-allocationstrategy""", alias="AllocationStrategy")
    OnDemandTargetCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-ondemandtargetcapacity""", alias="OnDemandTargetCapacity")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-type""", alias="Type")
    LaunchSpecifications_: Optional[List['SpotFleetLaunchSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications""", alias="LaunchSpecifications")
    InstanceInterruptionBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-instanceinterruptionbehavior""", alias="InstanceInterruptionBehavior")
    LoadBalancersConfig_: Optional['LoadBalancersConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-loadbalancersconfig""", alias="LoadBalancersConfig")
    ValidFrom_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-validfrom""", alias="ValidFrom")
    ReplaceUnhealthyInstances_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-replaceunhealthyinstances""", alias="ReplaceUnhealthyInstances")
    TargetCapacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-targetcapacity""", alias="TargetCapacity")
    


    @property
    def tropo_type(self) -> troposphere.ec2.SpotFleetRequestConfigData:
        from troposphere.ec2 import SpotFleetRequestConfigData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpotFleetTagSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleettagspecification.html
    Properties:
        - Name: ResourceType
        - Name: Tags
    
    """
    
    ResourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleettagspecification.html#cfn-ec2-spotfleet-spotfleettagspecification-resourcetype""", alias="ResourceType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleettagspecification.html#cfn-ec2-spotfleet-spotfleettagspecification-tags""", alias="Tags")
    


    @property
    def tropo_type(self) -> troposphere.ec2.SpotFleetTagSpecification:
        from troposphere.ec2 import SpotFleetTagSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpotMaintenanceStrategies(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotmaintenancestrategies.html
    Properties:
        - Name: CapacityRebalance
    
    """
    
    CapacityRebalance_: Optional['SpotCapacityRebalance'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotmaintenancestrategies.html#cfn-ec2-spotfleet-spotmaintenancestrategies-capacityrebalance""", alias="CapacityRebalance")
    


    @property
    def tropo_type(self) -> troposphere.ec2.SpotMaintenanceStrategies:
        from troposphere.ec2 import SpotMaintenanceStrategies as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpotPlacement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotplacement.html
    Properties:
        - Name: GroupName
        - Name: Tenancy
        - Name: AvailabilityZone
    
    """
    
    GroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotplacement.html#cfn-ec2-spotfleet-spotplacement-groupname""", alias="GroupName")
    Tenancy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotplacement.html#cfn-ec2-spotfleet-spotplacement-tenancy""", alias="Tenancy")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotplacement.html#cfn-ec2-spotfleet-spotplacement-availabilityzone""", alias="AvailabilityZone")
    


    @property
    def tropo_type(self) -> troposphere.ec2.SpotPlacement:
        from troposphere.ec2 import SpotPlacement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-targetgroup.html
    Properties:
        - Name: Arn
    
    """
    
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-targetgroup.html#cfn-ec2-spotfleet-targetgroup-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TargetGroup:
        from troposphere.ec2 import TargetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetGroupsConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-targetgroupsconfig.html
    Properties:
        - Name: TargetGroups
    
    """
    
    TargetGroups_: List['TargetGroup'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-targetgroupsconfig.html#cfn-ec2-spotfleet-targetgroupsconfig-targetgroups""", alias="TargetGroups")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TargetGroupsConfig:
        from troposphere.ec2 import TargetGroupsConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TotalLocalStorageGBRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-totallocalstoragegbrequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-totallocalstoragegbrequest.html#cfn-ec2-spotfleet-totallocalstoragegbrequest-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-totallocalstoragegbrequest.html#cfn-ec2-spotfleet-totallocalstoragegbrequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TotalLocalStorageGBRequest:
        from troposphere.ec2 import TotalLocalStorageGBRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VCpuCountRangeRequest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-vcpucountrangerequest.html
    Properties:
        - Name: Min
        - Name: Max
    
    """
    
    Min_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-vcpucountrangerequest.html#cfn-ec2-spotfleet-vcpucountrangerequest-min""", alias="Min")
    Max_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-vcpucountrangerequest.html#cfn-ec2-spotfleet-vcpucountrangerequest-max""", alias="Max")
    


    @property
    def tropo_type(self) -> troposphere.ec2.VCpuCountRangeRequest:
        from troposphere.ec2 import VCpuCountRangeRequest as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateDnsNameOptionsOnLaunch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html
    Properties:
        - Name: EnableResourceNameDnsARecord
        - Name: HostnameType
        - Name: EnableResourceNameDnsAAAARecord
    
    """
    
    EnableResourceNameDnsARecord_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html#cfn-ec2-subnet-privatednsnameoptionsonlaunch-enableresourcenamednsarecord""", alias="EnableResourceNameDnsARecord")
    HostnameType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html#cfn-ec2-subnet-privatednsnameoptionsonlaunch-hostnametype""", alias="HostnameType")
    EnableResourceNameDnsAAAARecord_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html#cfn-ec2-subnet-privatednsnameoptionsonlaunch-enableresourcenamednsaaaarecord""", alias="EnableResourceNameDnsAAAARecord")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PrivateDnsNameOptionsOnLaunch:
        from troposphere.ec2 import PrivateDnsNameOptionsOnLaunch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrafficMirrorPortRange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-trafficmirrorfilterrule-trafficmirrorportrange.html
    Properties:
        - Name: FromPort
        - Name: ToPort
    
    """
    
    FromPort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-trafficmirrorfilterrule-trafficmirrorportrange.html#cfn-ec2-trafficmirrorfilterrule-trafficmirrorportrange-fromport""", alias="FromPort")
    ToPort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-trafficmirrorfilterrule-trafficmirrorportrange.html#cfn-ec2-trafficmirrorfilterrule-trafficmirrorportrange-toport""", alias="ToPort")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TrafficMirrorPortRange:
        from troposphere.ec2 import TrafficMirrorPortRange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Options(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayattachment-options.html
    Properties:
        - Name: Ipv6Support
        - Name: ApplianceModeSupport
        - Name: SecurityGroupReferencingSupport
        - Name: DnsSupport
    
    """
    
    Ipv6Support_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayattachment-options.html#cfn-ec2-transitgatewayattachment-options-ipv6support""", alias="Ipv6Support")
    ApplianceModeSupport_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayattachment-options.html#cfn-ec2-transitgatewayattachment-options-appliancemodesupport""", alias="ApplianceModeSupport")
    SecurityGroupReferencingSupport_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayattachment-options.html#cfn-ec2-transitgatewayattachment-options-securitygroupreferencingsupport""", alias="SecurityGroupReferencingSupport")
    DnsSupport_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayattachment-options.html#cfn-ec2-transitgatewayattachment-options-dnssupport""", alias="DnsSupport")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Options:
        from troposphere.ec2 import Options as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TransitGatewayConnectOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayconnect-transitgatewayconnectoptions.html
    Properties:
        - Name: Protocol
    
    """
    
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayconnect-transitgatewayconnectoptions.html#cfn-ec2-transitgatewayconnect-transitgatewayconnectoptions-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayConnectOptions:
        from troposphere.ec2 import TransitGatewayConnectOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Options(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewaymulticastdomain-options.html
    Properties:
        - Name: StaticSourcesSupport
        - Name: AutoAcceptSharedAssociations
        - Name: Igmpv2Support
    
    """
    
    StaticSourcesSupport_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewaymulticastdomain-options.html#cfn-ec2-transitgatewaymulticastdomain-options-staticsourcessupport""", alias="StaticSourcesSupport")
    AutoAcceptSharedAssociations_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewaymulticastdomain-options.html#cfn-ec2-transitgatewaymulticastdomain-options-autoacceptsharedassociations""", alias="AutoAcceptSharedAssociations")
    Igmpv2Support_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewaymulticastdomain-options.html#cfn-ec2-transitgatewaymulticastdomain-options-igmpv2support""", alias="Igmpv2Support")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Options:
        from troposphere.ec2 import Options as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PeeringAttachmentStatus(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewaypeeringattachment-peeringattachmentstatus.html
    Properties:
        - Name: Message
        - Name: Code
    
    """
    
    Message_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewaypeeringattachment-peeringattachmentstatus.html#cfn-ec2-transitgatewaypeeringattachment-peeringattachmentstatus-message""", alias="Message")
    Code_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewaypeeringattachment-peeringattachmentstatus.html#cfn-ec2-transitgatewaypeeringattachment-peeringattachmentstatus-code""", alias="Code")
    


    @property
    def tropo_type(self) -> troposphere.ec2.PeeringAttachmentStatus:
        from troposphere.ec2 import PeeringAttachmentStatus as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Options(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayvpcattachment-options.html
    Properties:
        - Name: Ipv6Support
        - Name: ApplianceModeSupport
        - Name: DnsSupport
    
    """
    
    Ipv6Support_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayvpcattachment-options.html#cfn-ec2-transitgatewayvpcattachment-options-ipv6support""", alias="Ipv6Support")
    ApplianceModeSupport_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayvpcattachment-options.html#cfn-ec2-transitgatewayvpcattachment-options-appliancemodesupport""", alias="ApplianceModeSupport")
    DnsSupport_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayvpcattachment-options.html#cfn-ec2-transitgatewayvpcattachment-options-dnssupport""", alias="DnsSupport")
    


    @property
    def tropo_type(self) -> troposphere.ec2.Options:
        from troposphere.ec2 import Options as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpnTunnelOptionsSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-vpnconnection-vpntunneloptionsspecification.html
    Properties:
        - Name: PreSharedKey
        - Name: TunnelInsideCidr
    
    """
    
    PreSharedKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-vpnconnection-vpntunneloptionsspecification.html#cfn-ec2-vpnconnection-vpntunneloptionsspecification-presharedkey""", alias="PreSharedKey")
    TunnelInsideCidr_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-vpnconnection-vpntunneloptionsspecification.html#cfn-ec2-vpnconnection-vpntunneloptionsspecification-tunnelinsidecidr""", alias="TunnelInsideCidr")
    


    @property
    def tropo_type(self) -> troposphere.ec2.VpnTunnelOptionsSpecification:
        from troposphere.ec2 import VpnTunnelOptionsSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoadBalancerOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessendpoint-loadbalanceroptions.html
    Properties:
        - Name: LoadBalancerArn
        - Name: Port
        - Name: Protocol
        - Name: SubnetIds
    
    """
    
    LoadBalancerArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessendpoint-loadbalanceroptions.html#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-loadbalancerarn""", alias="LoadBalancerArn")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessendpoint-loadbalanceroptions.html#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-port""", alias="Port")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessendpoint-loadbalanceroptions.html#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-protocol""", alias="Protocol")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessendpoint-loadbalanceroptions.html#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.ec2.LoadBalancerOptions:
        from troposphere.ec2 import LoadBalancerOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkInterfaceOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessendpoint-networkinterfaceoptions.html
    Properties:
        - Name: Port
        - Name: NetworkInterfaceId
        - Name: Protocol
    
    """
    
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessendpoint-networkinterfaceoptions.html#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-port""", alias="Port")
    NetworkInterfaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessendpoint-networkinterfaceoptions.html#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-networkinterfaceid""", alias="NetworkInterfaceId")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessendpoint-networkinterfaceoptions.html#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.ec2.NetworkInterfaceOptions:
        from troposphere.ec2 import NetworkInterfaceOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SseSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessendpoint-ssespecification.html
    Properties:
        - Name: CustomerManagedKeyEnabled
        - Name: KmsKeyArn
    
    """
    
    CustomerManagedKeyEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessendpoint-ssespecification.html#cfn-ec2-verifiedaccessendpoint-ssespecification-customermanagedkeyenabled""", alias="CustomerManagedKeyEnabled")
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessendpoint-ssespecification.html#cfn-ec2-verifiedaccessendpoint-ssespecification-kmskeyarn""", alias="KmsKeyArn")
    


    @property
    def tropo_type(self) -> troposphere.ec2.SseSpecification:
        from troposphere.ec2 import SseSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SseSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessgroup-ssespecification.html
    Properties:
        - Name: CustomerManagedKeyEnabled
        - Name: KmsKeyArn
    
    """
    
    CustomerManagedKeyEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessgroup-ssespecification.html#cfn-ec2-verifiedaccessgroup-ssespecification-customermanagedkeyenabled""", alias="CustomerManagedKeyEnabled")
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessgroup-ssespecification.html#cfn-ec2-verifiedaccessgroup-ssespecification-kmskeyarn""", alias="KmsKeyArn")
    


    @property
    def tropo_type(self) -> troposphere.ec2.SseSpecification:
        from troposphere.ec2 import SseSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchLogs(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-cloudwatchlogs.html
    Properties:
        - Name: LogGroup
        - Name: Enabled
    
    """
    
    LogGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-cloudwatchlogs.html#cfn-ec2-verifiedaccessinstance-cloudwatchlogs-loggroup""", alias="LogGroup")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-cloudwatchlogs.html#cfn-ec2-verifiedaccessinstance-cloudwatchlogs-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.ec2.CloudWatchLogs:
        from troposphere.ec2 import CloudWatchLogs as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisDataFirehose(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-kinesisdatafirehose.html
    Properties:
        - Name: DeliveryStream
        - Name: Enabled
    
    """
    
    DeliveryStream_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-kinesisdatafirehose.html#cfn-ec2-verifiedaccessinstance-kinesisdatafirehose-deliverystream""", alias="DeliveryStream")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-kinesisdatafirehose.html#cfn-ec2-verifiedaccessinstance-kinesisdatafirehose-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.ec2.KinesisDataFirehose:
        from troposphere.ec2 import KinesisDataFirehose as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-s3.html
    Properties:
        - Name: BucketName
        - Name: Enabled
        - Name: Prefix
        - Name: BucketOwner
    
    """
    
    BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-s3.html#cfn-ec2-verifiedaccessinstance-s3-bucketname""", alias="BucketName")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-s3.html#cfn-ec2-verifiedaccessinstance-s3-enabled""", alias="Enabled")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-s3.html#cfn-ec2-verifiedaccessinstance-s3-prefix""", alias="Prefix")
    BucketOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-s3.html#cfn-ec2-verifiedaccessinstance-s3-bucketowner""", alias="BucketOwner")
    


    @property
    def tropo_type(self) -> troposphere.ec2.S3:
        from troposphere.ec2 import S3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VerifiedAccessLogs(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-verifiedaccesslogs.html
    Properties:
        - Name: S3
        - Name: LogVersion
        - Name: KinesisDataFirehose
        - Name: CloudWatchLogs
        - Name: IncludeTrustContext
    
    """
    
    S3_: Optional['S3'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-verifiedaccesslogs.html#cfn-ec2-verifiedaccessinstance-verifiedaccesslogs-s3""", alias="S3")
    LogVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-verifiedaccesslogs.html#cfn-ec2-verifiedaccessinstance-verifiedaccesslogs-logversion""", alias="LogVersion")
    KinesisDataFirehose_: Optional['KinesisDataFirehose'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-verifiedaccesslogs.html#cfn-ec2-verifiedaccessinstance-verifiedaccesslogs-kinesisdatafirehose""", alias="KinesisDataFirehose")
    CloudWatchLogs_: Optional['CloudWatchLogs'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-verifiedaccesslogs.html#cfn-ec2-verifiedaccessinstance-verifiedaccesslogs-cloudwatchlogs""", alias="CloudWatchLogs")
    IncludeTrustContext_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-verifiedaccesslogs.html#cfn-ec2-verifiedaccessinstance-verifiedaccesslogs-includetrustcontext""", alias="IncludeTrustContext")
    


    @property
    def tropo_type(self) -> troposphere.ec2.VerifiedAccessLogs:
        from troposphere.ec2 import VerifiedAccessLogs as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VerifiedAccessTrustProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-verifiedaccesstrustprovider.html
    Properties:
        - Name: Description
        - Name: DeviceTrustProviderType
        - Name: VerifiedAccessTrustProviderId
        - Name: TrustProviderType
        - Name: UserTrustProviderType
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccessinstance-verifiedaccesstrustprovider-description""", alias="Description")
    DeviceTrustProviderType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccessinstance-verifiedaccesstrustprovider-devicetrustprovidertype""", alias="DeviceTrustProviderType")
    VerifiedAccessTrustProviderId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccessinstance-verifiedaccesstrustprovider-verifiedaccesstrustproviderid""", alias="VerifiedAccessTrustProviderId")
    TrustProviderType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccessinstance-verifiedaccesstrustprovider-trustprovidertype""", alias="TrustProviderType")
    UserTrustProviderType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccessinstance-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccessinstance-verifiedaccesstrustprovider-usertrustprovidertype""", alias="UserTrustProviderType")
    


    @property
    def tropo_type(self) -> troposphere.ec2.VerifiedAccessTrustProvider:
        from troposphere.ec2 import VerifiedAccessTrustProvider as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeviceOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-deviceoptions.html
    Properties:
        - Name: TenantId
        - Name: PublicSigningKeyUrl
    
    """
    
    TenantId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-deviceoptions.html#cfn-ec2-verifiedaccesstrustprovider-deviceoptions-tenantid""", alias="TenantId")
    PublicSigningKeyUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-deviceoptions.html#cfn-ec2-verifiedaccesstrustprovider-deviceoptions-publicsigningkeyurl""", alias="PublicSigningKeyUrl")
    


    @property
    def tropo_type(self) -> troposphere.ec2.DeviceOptions:
        from troposphere.ec2 import DeviceOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OidcOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions.html
    Properties:
        - Name: TokenEndpoint
        - Name: Scope
        - Name: Issuer
        - Name: ClientSecret
        - Name: UserInfoEndpoint
        - Name: ClientId
        - Name: AuthorizationEndpoint
    
    """
    
    TokenEndpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions.html#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-tokenendpoint""", alias="TokenEndpoint")
    Scope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions.html#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-scope""", alias="Scope")
    Issuer_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions.html#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-issuer""", alias="Issuer")
    ClientSecret_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions.html#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-clientsecret""", alias="ClientSecret")
    UserInfoEndpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions.html#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-userinfoendpoint""", alias="UserInfoEndpoint")
    ClientId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions.html#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-clientid""", alias="ClientId")
    AuthorizationEndpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-oidcoptions.html#cfn-ec2-verifiedaccesstrustprovider-oidcoptions-authorizationendpoint""", alias="AuthorizationEndpoint")
    


    @property
    def tropo_type(self) -> troposphere.ec2.OidcOptions:
        from troposphere.ec2 import OidcOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SseSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-ssespecification.html
    Properties:
        - Name: CustomerManagedKeyEnabled
        - Name: KmsKeyArn
    
    """
    
    CustomerManagedKeyEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-ssespecification.html#cfn-ec2-verifiedaccesstrustprovider-ssespecification-customermanagedkeyenabled""", alias="CustomerManagedKeyEnabled")
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-verifiedaccesstrustprovider-ssespecification.html#cfn-ec2-verifiedaccesstrustprovider-ssespecification-kmskeyarn""", alias="KmsKeyArn")
    


    @property
    def tropo_type(self) -> troposphere.ec2.SseSpecification:
        from troposphere.ec2 import SseSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class CapacityReservation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html
    Properties:
        - Name: Tenancy
        - Name: EndDateType
        - Name: TagSpecifications
        - Name: AvailabilityZone
        - Name: EndDate
        - Name: EbsOptimized
        - Name: OutPostArn
        - Name: InstanceCount
        - Name: PlacementGroupArn
        - Name: InstancePlatform
        - Name: InstanceType
        - Name: EphemeralStorage
        - Name: InstanceMatchCriteria
    Attributes:
        - Name: Tenancy
        - Name: AvailableInstanceCount
        - Name: AvailabilityZone
        - Name: TotalInstanceCount
        - Name: Id
        - Name: InstanceType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Tenancy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-tenancy""", alias="Tenancy")
    EndDateType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-enddatetype""", alias="EndDateType")
    TagSpecifications_: Optional[List['TagSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-tagspecifications""", alias="TagSpecifications")
    AvailabilityZone_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-availabilityzone""", alias="AvailabilityZone")
    EndDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-enddate""", alias="EndDate")
    EbsOptimized_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-ebsoptimized""", alias="EbsOptimized")
    OutPostArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-outpostarn""", alias="OutPostArn")
    InstanceCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-instancecount""", alias="InstanceCount")
    PlacementGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-placementgrouparn""", alias="PlacementGroupArn")
    InstancePlatform_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-instanceplatform""", alias="InstancePlatform")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-instancetype""", alias="InstanceType")
    EphemeralStorage_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-ephemeralstorage""", alias="EphemeralStorage")
    InstanceMatchCriteria_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-instancematchcriteria""", alias="InstanceMatchCriteria")
    

    @property
    def tropo_type(self) -> troposphere.ec2.CapacityReservation:
        from troposphere.ec2 import CapacityReservation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import CapacityReservation as TropoT
        return resource_to_troposphere(self, TropoT)


class CapacityReservationFleet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservationfleet.html
    Properties:
        - Name: Tenancy
        - Name: TotalTargetCapacity
        - Name: AllocationStrategy
        - Name: TagSpecifications
        - Name: NoRemoveEndDate
        - Name: InstanceTypeSpecifications
        - Name: RemoveEndDate
        - Name: InstanceMatchCriteria
        - Name: EndDate
    Attributes:
        - Name: CapacityReservationFleetId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Tenancy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservationfleet.html#cfn-ec2-capacityreservationfleet-tenancy""", alias="Tenancy")
    TotalTargetCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservationfleet.html#cfn-ec2-capacityreservationfleet-totaltargetcapacity""", alias="TotalTargetCapacity")
    AllocationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservationfleet.html#cfn-ec2-capacityreservationfleet-allocationstrategy""", alias="AllocationStrategy")
    TagSpecifications_: Optional[List['TagSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservationfleet.html#cfn-ec2-capacityreservationfleet-tagspecifications""", alias="TagSpecifications")
    NoRemoveEndDate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservationfleet.html#cfn-ec2-capacityreservationfleet-noremoveenddate""", alias="NoRemoveEndDate")
    InstanceTypeSpecifications_: Optional[List['InstanceTypeSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservationfleet.html#cfn-ec2-capacityreservationfleet-instancetypespecifications""", alias="InstanceTypeSpecifications")
    RemoveEndDate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservationfleet.html#cfn-ec2-capacityreservationfleet-removeenddate""", alias="RemoveEndDate")
    InstanceMatchCriteria_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservationfleet.html#cfn-ec2-capacityreservationfleet-instancematchcriteria""", alias="InstanceMatchCriteria")
    EndDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservationfleet.html#cfn-ec2-capacityreservationfleet-enddate""", alias="EndDate")
    

    @property
    def tropo_type(self) -> troposphere.ec2.CapacityReservationFleet:
        from troposphere.ec2 import CapacityReservationFleet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import CapacityReservationFleet as TropoT
        return resource_to_troposphere(self, TropoT)


class CarrierGateway(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-carriergateway.html
    Properties:
        - Name: VpcId
        - Name: Tags
    Attributes:
        - Name: OwnerId
        - Name: State
        - Name: CarrierGatewayId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-carriergateway.html#cfn-ec2-carriergateway-vpcid""", alias="VpcId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-carriergateway.html#cfn-ec2-carriergateway-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.CarrierGateway:
        from troposphere.ec2 import CarrierGateway as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import CarrierGateway as TropoT
        return resource_to_troposphere(self, TropoT)


class ClientVpnAuthorizationRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html
    Properties:
        - Name: ClientVpnEndpointId
        - Name: Description
        - Name: AccessGroupId
        - Name: TargetNetworkCidr
        - Name: AuthorizeAllGroups
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ClientVpnEndpointId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-clientvpnendpointid""", alias="ClientVpnEndpointId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-description""", alias="Description")
    AccessGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-accessgroupid""", alias="AccessGroupId")
    TargetNetworkCidr_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-targetnetworkcidr""", alias="TargetNetworkCidr")
    AuthorizeAllGroups_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-authorizeallgroups""", alias="AuthorizeAllGroups")
    

    @property
    def tropo_type(self) -> troposphere.ec2.ClientVpnAuthorizationRule:
        from troposphere.ec2 import ClientVpnAuthorizationRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import ClientVpnAuthorizationRule as TropoT
        return resource_to_troposphere(self, TropoT)


class ClientVpnEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html
    Properties:
        - Name: ClientCidrBlock
        - Name: ClientConnectOptions
        - Name: Description
        - Name: TagSpecifications
        - Name: AuthenticationOptions
        - Name: ServerCertificateArn
        - Name: SessionTimeoutHours
        - Name: DnsServers
        - Name: SecurityGroupIds
        - Name: ConnectionLogOptions
        - Name: SplitTunnel
        - Name: ClientLoginBannerOptions
        - Name: VpcId
        - Name: SelfServicePortal
        - Name: TransportProtocol
        - Name: VpnPort
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ClientCidrBlock_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-clientcidrblock""", alias="ClientCidrBlock")
    ClientConnectOptions_: Optional['ClientConnectOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-clientconnectoptions""", alias="ClientConnectOptions")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-description""", alias="Description")
    TagSpecifications_: Optional[List['TagSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-tagspecifications""", alias="TagSpecifications")
    AuthenticationOptions_: List['ClientAuthenticationRequest'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-authenticationoptions""", alias="AuthenticationOptions")
    ServerCertificateArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-servercertificatearn""", alias="ServerCertificateArn")
    SessionTimeoutHours_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-sessiontimeouthours""", alias="SessionTimeoutHours")
    DnsServers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-dnsservers""", alias="DnsServers")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-securitygroupids""", alias="SecurityGroupIds")
    ConnectionLogOptions_: 'ConnectionLogOptions' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-connectionlogoptions""", alias="ConnectionLogOptions")
    SplitTunnel_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-splittunnel""", alias="SplitTunnel")
    ClientLoginBannerOptions_: Optional['ClientLoginBannerOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-clientloginbanneroptions""", alias="ClientLoginBannerOptions")
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-vpcid""", alias="VpcId")
    SelfServicePortal_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-selfserviceportal""", alias="SelfServicePortal")
    TransportProtocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-transportprotocol""", alias="TransportProtocol")
    VpnPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-vpnport""", alias="VpnPort")
    

    @property
    def tropo_type(self) -> troposphere.ec2.ClientVpnEndpoint:
        from troposphere.ec2 import ClientVpnEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import ClientVpnEndpoint as TropoT
        return resource_to_troposphere(self, TropoT)


class ClientVpnRoute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html
    Properties:
        - Name: ClientVpnEndpointId
        - Name: TargetVpcSubnetId
        - Name: Description
        - Name: DestinationCidrBlock
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ClientVpnEndpointId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html#cfn-ec2-clientvpnroute-clientvpnendpointid""", alias="ClientVpnEndpointId")
    TargetVpcSubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html#cfn-ec2-clientvpnroute-targetvpcsubnetid""", alias="TargetVpcSubnetId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html#cfn-ec2-clientvpnroute-description""", alias="Description")
    DestinationCidrBlock_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html#cfn-ec2-clientvpnroute-destinationcidrblock""", alias="DestinationCidrBlock")
    

    @property
    def tropo_type(self) -> troposphere.ec2.ClientVpnRoute:
        from troposphere.ec2 import ClientVpnRoute as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import ClientVpnRoute as TropoT
        return resource_to_troposphere(self, TropoT)


class ClientVpnTargetNetworkAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.html
    Properties:
        - Name: ClientVpnEndpointId
        - Name: SubnetId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ClientVpnEndpointId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.html#cfn-ec2-clientvpntargetnetworkassociation-clientvpnendpointid""", alias="ClientVpnEndpointId")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.html#cfn-ec2-clientvpntargetnetworkassociation-subnetid""", alias="SubnetId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.ClientVpnTargetNetworkAssociation:
        from troposphere.ec2 import ClientVpnTargetNetworkAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import ClientVpnTargetNetworkAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class CustomerGateway(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customergateway.html
    Properties:
        - Name: Type
        - Name: IpAddress
        - Name: BgpAsn
        - Name: Tags
        - Name: DeviceName
    Attributes:
        - Name: CustomerGatewayId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customergateway.html#cfn-ec2-customergateway-type""", alias="Type")
    IpAddress_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customergateway.html#cfn-ec2-customergateway-ipaddress""", alias="IpAddress")
    BgpAsn_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customergateway.html#cfn-ec2-customergateway-bgpasn""", alias="BgpAsn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customergateway.html#cfn-ec2-customergateway-tags""", alias="Tags")
    DeviceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customergateway.html#cfn-ec2-customergateway-devicename""", alias="DeviceName")
    

    @property
    def tropo_type(self) -> troposphere.ec2.CustomerGateway:
        from troposphere.ec2 import CustomerGateway as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import CustomerGateway as TropoT
        return resource_to_troposphere(self, TropoT)


class DHCPOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcpoptions.html
    Properties:
        - Name: NetbiosNameServers
        - Name: NtpServers
        - Name: DomainName
        - Name: NetbiosNodeType
        - Name: DomainNameServers
        - Name: Tags
    Attributes:
        - Name: DhcpOptionsId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NetbiosNameServers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcpoptions.html#cfn-ec2-dhcpoptions-netbiosnameservers""", alias="NetbiosNameServers")
    NtpServers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcpoptions.html#cfn-ec2-dhcpoptions-ntpservers""", alias="NtpServers")
    DomainName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcpoptions.html#cfn-ec2-dhcpoptions-domainname""", alias="DomainName")
    NetbiosNodeType_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcpoptions.html#cfn-ec2-dhcpoptions-netbiosnodetype""", alias="NetbiosNodeType")
    DomainNameServers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcpoptions.html#cfn-ec2-dhcpoptions-domainnameservers""", alias="DomainNameServers")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcpoptions.html#cfn-ec2-dhcpoptions-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.DHCPOptions:
        from troposphere.ec2 import DHCPOptions as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import DHCPOptions as TropoT
        return resource_to_troposphere(self, TropoT)


class EC2Fleet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html
    Properties:
        - Name: Context
        - Name: TargetCapacitySpecification
        - Name: OnDemandOptions
        - Name: Type
        - Name: ExcessCapacityTerminationPolicy
        - Name: TagSpecifications
        - Name: SpotOptions
        - Name: ValidFrom
        - Name: ReplaceUnhealthyInstances
        - Name: LaunchTemplateConfigs
        - Name: TerminateInstancesWithExpiration
        - Name: ValidUntil
    Attributes:
        - Name: FleetId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Context_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-context""", alias="Context")
    TargetCapacitySpecification_: 'TargetCapacitySpecificationRequest' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-targetcapacityspecification""", alias="TargetCapacitySpecification")
    OnDemandOptions_: Optional['OnDemandOptionsRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-ondemandoptions""", alias="OnDemandOptions")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-type""", alias="Type")
    ExcessCapacityTerminationPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-excesscapacityterminationpolicy""", alias="ExcessCapacityTerminationPolicy")
    TagSpecifications_: Optional[List['TagSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-tagspecifications""", alias="TagSpecifications")
    SpotOptions_: Optional['SpotOptionsRequest'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-spotoptions""", alias="SpotOptions")
    ValidFrom_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-validfrom""", alias="ValidFrom")
    ReplaceUnhealthyInstances_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-replaceunhealthyinstances""", alias="ReplaceUnhealthyInstances")
    LaunchTemplateConfigs_: List['FleetLaunchTemplateConfigRequest'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-launchtemplateconfigs""", alias="LaunchTemplateConfigs")
    TerminateInstancesWithExpiration_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-terminateinstanceswithexpiration""", alias="TerminateInstancesWithExpiration")
    ValidUntil_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-validuntil""", alias="ValidUntil")
    

    @property
    def tropo_type(self) -> troposphere.ec2.EC2Fleet:
        from troposphere.ec2 import EC2Fleet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import EC2Fleet as TropoT
        return resource_to_troposphere(self, TropoT)


class EIP(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eip.html
    Properties:
        - Name: InstanceId
        - Name: PublicIpv4Pool
        - Name: TransferAddress
        - Name: Domain
        - Name: Tags
        - Name: NetworkBorderGroup
    Attributes:
        - Name: PublicIp
        - Name: AllocationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InstanceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eip.html#cfn-ec2-eip-instanceid""", alias="InstanceId")
    PublicIpv4Pool_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eip.html#cfn-ec2-eip-publicipv4pool""", alias="PublicIpv4Pool")
    TransferAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eip.html#cfn-ec2-eip-transferaddress""", alias="TransferAddress")
    Domain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eip.html#cfn-ec2-eip-domain""", alias="Domain")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eip.html#cfn-ec2-eip-tags""", alias="Tags")
    NetworkBorderGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eip.html#cfn-ec2-eip-networkbordergroup""", alias="NetworkBorderGroup")
    

    @property
    def tropo_type(self) -> troposphere.ec2.EIP:
        from troposphere.ec2 import EIP as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import EIP as TropoT
        return resource_to_troposphere(self, TropoT)


class EIPAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eipassociation.html
    Properties:
        - Name: PrivateIpAddress
        - Name: InstanceId
        - Name: AllocationId
        - Name: NetworkInterfaceId
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PrivateIpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eipassociation.html#cfn-ec2-eipassociation-privateipaddress""", alias="PrivateIpAddress")
    InstanceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eipassociation.html#cfn-ec2-eipassociation-instanceid""", alias="InstanceId")
    AllocationId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eipassociation.html#cfn-ec2-eipassociation-allocationid""", alias="AllocationId")
    NetworkInterfaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-eipassociation.html#cfn-ec2-eipassociation-networkinterfaceid""", alias="NetworkInterfaceId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.EIPAssociation:
        from troposphere.ec2 import EIPAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import EIPAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class EgressOnlyInternetGateway(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-egressonlyinternetgateway.html
    Properties:
        - Name: VpcId
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-egressonlyinternetgateway.html#cfn-ec2-egressonlyinternetgateway-vpcid""", alias="VpcId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.EgressOnlyInternetGateway:
        from troposphere.ec2 import EgressOnlyInternetGateway as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import EgressOnlyInternetGateway as TropoT
        return resource_to_troposphere(self, TropoT)


class EnclaveCertificateIamRoleAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html
    Properties:
        - Name: RoleArn
        - Name: CertificateArn
    Attributes:
        - Name: EncryptionKmsKeyId
        - Name: CertificateS3BucketName
        - Name: CertificateS3ObjectKey
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html#cfn-ec2-enclavecertificateiamroleassociation-rolearn""", alias="RoleArn")
    CertificateArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html#cfn-ec2-enclavecertificateiamroleassociation-certificatearn""", alias="CertificateArn")
    

    @property
    def tropo_type(self) -> troposphere.ec2.EnclaveCertificateIamRoleAssociation:
        from troposphere.ec2 import EnclaveCertificateIamRoleAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import EnclaveCertificateIamRoleAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class FlowLog(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html
    Properties:
        - Name: LogFormat
        - Name: ResourceId
        - Name: MaxAggregationInterval
        - Name: DestinationOptions
        - Name: ResourceType
        - Name: DeliverCrossAccountRole
        - Name: LogDestination
        - Name: LogGroupName
        - Name: DeliverLogsPermissionArn
        - Name: LogDestinationType
        - Name: Tags
        - Name: TrafficType
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LogFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-logformat""", alias="LogFormat")
    ResourceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-resourceid""", alias="ResourceId")
    MaxAggregationInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-maxaggregationinterval""", alias="MaxAggregationInterval")
    DestinationOptions_: Optional['DestinationOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-destinationoptions""", alias="DestinationOptions")
    ResourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-resourcetype""", alias="ResourceType")
    DeliverCrossAccountRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-delivercrossaccountrole""", alias="DeliverCrossAccountRole")
    LogDestination_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-logdestination""", alias="LogDestination")
    LogGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-loggroupname""", alias="LogGroupName")
    DeliverLogsPermissionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-deliverlogspermissionarn""", alias="DeliverLogsPermissionArn")
    LogDestinationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-logdestinationtype""", alias="LogDestinationType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-tags""", alias="Tags")
    TrafficType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-traffictype""", alias="TrafficType")
    

    @property
    def tropo_type(self) -> troposphere.ec2.FlowLog:
        from troposphere.ec2 import FlowLog as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import FlowLog as TropoT
        return resource_to_troposphere(self, TropoT)


class GatewayRouteTableAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-gatewayroutetableassociation.html
    Properties:
        - Name: RouteTableId
        - Name: GatewayId
    Attributes:
        - Name: AssociationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RouteTableId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-gatewayroutetableassociation.html#cfn-ec2-gatewayroutetableassociation-routetableid""", alias="RouteTableId")
    GatewayId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-gatewayroutetableassociation.html#cfn-ec2-gatewayroutetableassociation-gatewayid""", alias="GatewayId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.GatewayRouteTableAssociation:
        from troposphere.ec2 import GatewayRouteTableAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import GatewayRouteTableAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class Host(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html
    Properties:
        - Name: HostRecovery
        - Name: InstanceFamily
        - Name: AutoPlacement
        - Name: OutpostArn
        - Name: HostMaintenance
        - Name: AvailabilityZone
        - Name: InstanceType
        - Name: AssetId
    Attributes:
        - Name: HostId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    HostRecovery_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-hostrecovery""", alias="HostRecovery")
    InstanceFamily_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-instancefamily""", alias="InstanceFamily")
    AutoPlacement_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-autoplacement""", alias="AutoPlacement")
    OutpostArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-outpostarn""", alias="OutpostArn")
    HostMaintenance_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-hostmaintenance""", alias="HostMaintenance")
    AvailabilityZone_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-availabilityzone""", alias="AvailabilityZone")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-instancetype""", alias="InstanceType")
    AssetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-assetid""", alias="AssetId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.Host:
        from troposphere.ec2 import Host as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import Host as TropoT
        return resource_to_troposphere(self, TropoT)


class IPAM(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipam.html
    Properties:
        - Name: Description
        - Name: Tier
        - Name: Tags
        - Name: OperatingRegions
    Attributes:
        - Name: DefaultResourceDiscoveryAssociationId
        - Name: DefaultResourceDiscoveryId
        - Name: IpamId
        - Name: ResourceDiscoveryAssociationCount
        - Name: ScopeCount
        - Name: Arn
        - Name: PrivateDefaultScopeId
        - Name: PublicDefaultScopeId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipam.html#cfn-ec2-ipam-description""", alias="Description")
    Tier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipam.html#cfn-ec2-ipam-tier""", alias="Tier")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipam.html#cfn-ec2-ipam-tags""", alias="Tags")
    OperatingRegions_: Optional[List['IpamOperatingRegion']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipam.html#cfn-ec2-ipam-operatingregions""", alias="OperatingRegions")
    

    @property
    def tropo_type(self) -> troposphere.ec2.IPAM:
        from troposphere.ec2 import IPAM as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import IPAM as TropoT
        return resource_to_troposphere(self, TropoT)


class IPAMAllocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamallocation.html
    Properties:
        - Name: Description
        - Name: Cidr
        - Name: NetmaskLength
        - Name: IpamPoolId
    Attributes:
        - Name: IpamPoolAllocationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamallocation.html#cfn-ec2-ipamallocation-description""", alias="Description")
    Cidr_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamallocation.html#cfn-ec2-ipamallocation-cidr""", alias="Cidr")
    NetmaskLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamallocation.html#cfn-ec2-ipamallocation-netmasklength""", alias="NetmaskLength")
    IpamPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamallocation.html#cfn-ec2-ipamallocation-ipampoolid""", alias="IpamPoolId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.IPAMAllocation:
        from troposphere.ec2 import IPAMAllocation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import IPAMAllocation as TropoT
        return resource_to_troposphere(self, TropoT)


class IPAMPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html
    Properties:
        - Name: AwsService
        - Name: Locale
        - Name: PublicIpSource
        - Name: Description
        - Name: SourceIpamPoolId
        - Name: AllocationMinNetmaskLength
        - Name: IpamScopeId
        - Name: ProvisionedCidrs
        - Name: AllocationMaxNetmaskLength
        - Name: AllocationDefaultNetmaskLength
        - Name: AutoImport
        - Name: AddressFamily
        - Name: AllocationResourceTags
        - Name: PubliclyAdvertisable
        - Name: Tags
    Attributes:
        - Name: IpamPoolId
        - Name: IpamArn
        - Name: PoolDepth
        - Name: State
        - Name: IpamScopeArn
        - Name: IpamScopeType
        - Name: Arn
        - Name: StateMessage
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AwsService_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-awsservice""", alias="AwsService")
    Locale_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-locale""", alias="Locale")
    PublicIpSource_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-publicipsource""", alias="PublicIpSource")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-description""", alias="Description")
    SourceIpamPoolId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-sourceipampoolid""", alias="SourceIpamPoolId")
    AllocationMinNetmaskLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-allocationminnetmasklength""", alias="AllocationMinNetmaskLength")
    IpamScopeId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-ipamscopeid""", alias="IpamScopeId")
    ProvisionedCidrs_: Optional[List['ProvisionedCidr']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-provisionedcidrs""", alias="ProvisionedCidrs")
    AllocationMaxNetmaskLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-allocationmaxnetmasklength""", alias="AllocationMaxNetmaskLength")
    AllocationDefaultNetmaskLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-allocationdefaultnetmasklength""", alias="AllocationDefaultNetmaskLength")
    AutoImport_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-autoimport""", alias="AutoImport")
    AddressFamily_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-addressfamily""", alias="AddressFamily")
    AllocationResourceTags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-allocationresourcetags""", alias="AllocationResourceTags")
    PubliclyAdvertisable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-publiclyadvertisable""", alias="PubliclyAdvertisable")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html#cfn-ec2-ipampool-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.IPAMPool:
        from troposphere.ec2 import IPAMPool as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import IPAMPool as TropoT
        return resource_to_troposphere(self, TropoT)


class IPAMPoolCidr(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampoolcidr.html
    Properties:
        - Name: Cidr
        - Name: NetmaskLength
        - Name: IpamPoolId
    Attributes:
        - Name: IpamPoolCidrId
        - Name: State
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Cidr_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampoolcidr.html#cfn-ec2-ipampoolcidr-cidr""", alias="Cidr")
    NetmaskLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampoolcidr.html#cfn-ec2-ipampoolcidr-netmasklength""", alias="NetmaskLength")
    IpamPoolId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampoolcidr.html#cfn-ec2-ipampoolcidr-ipampoolid""", alias="IpamPoolId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.IPAMPoolCidr:
        from troposphere.ec2 import IPAMPoolCidr as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import IPAMPoolCidr as TropoT
        return resource_to_troposphere(self, TropoT)


class IPAMResourceDiscovery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamresourcediscovery.html
    Properties:
        - Name: Description
        - Name: Tags
        - Name: OperatingRegions
    Attributes:
        - Name: IsDefault
        - Name: OwnerId
        - Name: State
        - Name: IpamResourceDiscoveryRegion
        - Name: IpamResourceDiscoveryArn
        - Name: IpamResourceDiscoveryId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamresourcediscovery.html#cfn-ec2-ipamresourcediscovery-description""", alias="Description")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamresourcediscovery.html#cfn-ec2-ipamresourcediscovery-tags""", alias="Tags")
    OperatingRegions_: Optional[List['IpamOperatingRegion']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamresourcediscovery.html#cfn-ec2-ipamresourcediscovery-operatingregions""", alias="OperatingRegions")
    

    @property
    def tropo_type(self) -> troposphere.ec2.IPAMResourceDiscovery:
        from troposphere.ec2 import IPAMResourceDiscovery as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import IPAMResourceDiscovery as TropoT
        return resource_to_troposphere(self, TropoT)


class IPAMResourceDiscoveryAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamresourcediscoveryassociation.html
    Properties:
        - Name: IpamId
        - Name: Tags
        - Name: IpamResourceDiscoveryId
    Attributes:
        - Name: IsDefault
        - Name: ResourceDiscoveryStatus
        - Name: OwnerId
        - Name: IpamArn
        - Name: IpamResourceDiscoveryAssociationId
        - Name: IpamResourceDiscoveryAssociationArn
        - Name: State
        - Name: IpamRegion
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IpamId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamresourcediscoveryassociation.html#cfn-ec2-ipamresourcediscoveryassociation-ipamid""", alias="IpamId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamresourcediscoveryassociation.html#cfn-ec2-ipamresourcediscoveryassociation-tags""", alias="Tags")
    IpamResourceDiscoveryId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamresourcediscoveryassociation.html#cfn-ec2-ipamresourcediscoveryassociation-ipamresourcediscoveryid""", alias="IpamResourceDiscoveryId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.IPAMResourceDiscoveryAssociation:
        from troposphere.ec2 import IPAMResourceDiscoveryAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import IPAMResourceDiscoveryAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class IPAMScope(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamscope.html
    Properties:
        - Name: Description
        - Name: IpamId
        - Name: Tags
    Attributes:
        - Name: IpamScopeId
        - Name: IsDefault
        - Name: IpamArn
        - Name: IpamScopeType
        - Name: PoolCount
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamscope.html#cfn-ec2-ipamscope-description""", alias="Description")
    IpamId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamscope.html#cfn-ec2-ipamscope-ipamid""", alias="IpamId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamscope.html#cfn-ec2-ipamscope-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.IPAMScope:
        from troposphere.ec2 import IPAMScope as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import IPAMScope as TropoT
        return resource_to_troposphere(self, TropoT)


class Instance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html
    Properties:
        - Name: AdditionalInfo
        - Name: Affinity
        - Name: AvailabilityZone
        - Name: BlockDeviceMappings
        - Name: CpuOptions
        - Name: CreditSpecification
        - Name: DisableApiTermination
        - Name: EbsOptimized
        - Name: ElasticGpuSpecifications
        - Name: ElasticInferenceAccelerators
        - Name: EnclaveOptions
        - Name: HibernationOptions
        - Name: HostId
        - Name: HostResourceGroupArn
        - Name: IamInstanceProfile
        - Name: ImageId
        - Name: InstanceInitiatedShutdownBehavior
        - Name: InstanceType
        - Name: Ipv6AddressCount
        - Name: Ipv6Addresses
        - Name: KernelId
        - Name: KeyName
        - Name: LaunchTemplate
        - Name: LicenseSpecifications
        - Name: Monitoring
        - Name: NetworkInterfaces
        - Name: PlacementGroupName
        - Name: PrivateDnsNameOptions
        - Name: PrivateIpAddress
        - Name: PropagateTagsToVolumeOnCreation
        - Name: RamdiskId
        - Name: SecurityGroupIds
        - Name: SecurityGroups
        - Name: SourceDestCheck
        - Name: SsmAssociations
        - Name: SubnetId
        - Name: Tags
        - Name: Tenancy
        - Name: UserData
        - Name: Volumes
    Attributes:
        - Name: AvailabilityZone
        - Name: PrivateDnsName
        - Name: PrivateIp
        - Name: PublicDnsName
        - Name: PublicIp
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AdditionalInfo_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-additionalinfo""", alias="AdditionalInfo")
    Affinity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-affinity""", alias="Affinity")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-availabilityzone""", alias="AvailabilityZone")
    BlockDeviceMappings_: Optional[List['BlockDeviceMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-blockdevicemappings""", alias="BlockDeviceMappings")
    CpuOptions_: Optional['CpuOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-cpuoptions""", alias="CpuOptions")
    CreditSpecification_: Optional['CreditSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-creditspecification""", alias="CreditSpecification")
    DisableApiTermination_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-disableapitermination""", alias="DisableApiTermination")
    EbsOptimized_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ebsoptimized""", alias="EbsOptimized")
    ElasticGpuSpecifications_: Optional[List['ElasticGpuSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-elasticgpuspecifications""", alias="ElasticGpuSpecifications")
    ElasticInferenceAccelerators_: Optional[List['ElasticInferenceAccelerator']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-elasticinferenceaccelerators""", alias="ElasticInferenceAccelerators")
    EnclaveOptions_: Optional['EnclaveOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-enclaveoptions""", alias="EnclaveOptions")
    HibernationOptions_: Optional['HibernationOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-hibernationoptions""", alias="HibernationOptions")
    HostId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-hostid""", alias="HostId")
    HostResourceGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-hostresourcegrouparn""", alias="HostResourceGroupArn")
    IamInstanceProfile_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-iaminstanceprofile""", alias="IamInstanceProfile")
    ImageId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-imageid""", alias="ImageId")
    InstanceInitiatedShutdownBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-instanceinitiatedshutdownbehavior""", alias="InstanceInitiatedShutdownBehavior")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-instancetype""", alias="InstanceType")
    Ipv6AddressCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ipv6addresscount""", alias="Ipv6AddressCount")
    Ipv6Addresses_: Optional[List['InstanceIpv6Address']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ipv6addresses""", alias="Ipv6Addresses")
    KernelId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-kernelid""", alias="KernelId")
    KeyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-keyname""", alias="KeyName")
    LaunchTemplate_: Optional['LaunchTemplateSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-launchtemplate""", alias="LaunchTemplate")
    LicenseSpecifications_: Optional[List['LicenseSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-licensespecifications""", alias="LicenseSpecifications")
    Monitoring_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-monitoring""", alias="Monitoring")
    NetworkInterfaces_: Optional[List['NetworkInterface']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-networkinterfaces""", alias="NetworkInterfaces")
    PlacementGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-placementgroupname""", alias="PlacementGroupName")
    PrivateDnsNameOptions_: Optional['PrivateDnsNameOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-privatednsnameoptions""", alias="PrivateDnsNameOptions")
    PrivateIpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-privateipaddress""", alias="PrivateIpAddress")
    PropagateTagsToVolumeOnCreation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-propagatetagstovolumeoncreation""", alias="PropagateTagsToVolumeOnCreation")
    RamdiskId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ramdiskid""", alias="RamdiskId")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-securitygroupids""", alias="SecurityGroupIds")
    SecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-securitygroups""", alias="SecurityGroups")
    SourceDestCheck_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-sourcedestcheck""", alias="SourceDestCheck")
    SsmAssociations_: Optional[List['SsmAssociation']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ssmassociations""", alias="SsmAssociations")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-subnetid""", alias="SubnetId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-tags""", alias="Tags")
    Tenancy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-tenancy""", alias="Tenancy")
    UserData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-userdata""", alias="UserData")
    Volumes_: Optional[List['Volume']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-volumes""", alias="Volumes")
    

    @property
    def tropo_type(self) -> troposphere.ec2.Instance:
        from troposphere.ec2 import Instance as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import Instance as TropoT
        return resource_to_troposphere(self, TropoT)


class InstanceConnectEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instanceconnectendpoint.html
    Properties:
        - Name: PreserveClientIp
        - Name: SubnetId
        - Name: ClientToken
        - Name: SecurityGroupIds
        - Name: Tags
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PreserveClientIp_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instanceconnectendpoint.html#cfn-ec2-instanceconnectendpoint-preserveclientip""", alias="PreserveClientIp")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instanceconnectendpoint.html#cfn-ec2-instanceconnectendpoint-subnetid""", alias="SubnetId")
    ClientToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instanceconnectendpoint.html#cfn-ec2-instanceconnectendpoint-clienttoken""", alias="ClientToken")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instanceconnectendpoint.html#cfn-ec2-instanceconnectendpoint-securitygroupids""", alias="SecurityGroupIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instanceconnectendpoint.html#cfn-ec2-instanceconnectendpoint-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.InstanceConnectEndpoint:
        from troposphere.ec2 import InstanceConnectEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import InstanceConnectEndpoint as TropoT
        return resource_to_troposphere(self, TropoT)


class InternetGateway(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-internetgateway.html
    Properties:
        - Name: Tags
    Attributes:
        - Name: InternetGatewayId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-internetgateway.html#cfn-ec2-internetgateway-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.InternetGateway:
        from troposphere.ec2 import InternetGateway as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import InternetGateway as TropoT
        return resource_to_troposphere(self, TropoT)


class KeyPair(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-keypair.html
    Properties:
        - Name: KeyName
        - Name: KeyType
        - Name: KeyFormat
        - Name: PublicKeyMaterial
        - Name: Tags
    Attributes:
        - Name: KeyPairId
        - Name: KeyFingerprint
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KeyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-keypair.html#cfn-ec2-keypair-keyname""", alias="KeyName")
    KeyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-keypair.html#cfn-ec2-keypair-keytype""", alias="KeyType")
    KeyFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-keypair.html#cfn-ec2-keypair-keyformat""", alias="KeyFormat")
    PublicKeyMaterial_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-keypair.html#cfn-ec2-keypair-publickeymaterial""", alias="PublicKeyMaterial")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-keypair.html#cfn-ec2-keypair-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.KeyPair:
        from troposphere.ec2 import KeyPair as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import KeyPair as TropoT
        return resource_to_troposphere(self, TropoT)


class LaunchTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html
    Properties:
        - Name: LaunchTemplateName
        - Name: LaunchTemplateData
        - Name: VersionDescription
        - Name: TagSpecifications
    Attributes:
        - Name: LatestVersionNumber
        - Name: LaunchTemplateId
        - Name: DefaultVersionNumber
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LaunchTemplateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#cfn-ec2-launchtemplate-launchtemplatename""", alias="LaunchTemplateName")
    LaunchTemplateData_: 'LaunchTemplateData' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#cfn-ec2-launchtemplate-launchtemplatedata""", alias="LaunchTemplateData")
    VersionDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#cfn-ec2-launchtemplate-versiondescription""", alias="VersionDescription")
    TagSpecifications_: Optional[List['LaunchTemplateTagSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#cfn-ec2-launchtemplate-tagspecifications""", alias="TagSpecifications")
    

    @property
    def tropo_type(self) -> troposphere.ec2.LaunchTemplate:
        from troposphere.ec2 import LaunchTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import LaunchTemplate as TropoT
        return resource_to_troposphere(self, TropoT)


class LocalGatewayRoute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html
    Properties:
        - Name: LocalGatewayRouteTableId
        - Name: DestinationCidrBlock
        - Name: NetworkInterfaceId
        - Name: LocalGatewayVirtualInterfaceGroupId
    Attributes:
        - Name: Type
        - Name: State
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LocalGatewayRouteTableId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html#cfn-ec2-localgatewayroute-localgatewayroutetableid""", alias="LocalGatewayRouteTableId")
    DestinationCidrBlock_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html#cfn-ec2-localgatewayroute-destinationcidrblock""", alias="DestinationCidrBlock")
    NetworkInterfaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html#cfn-ec2-localgatewayroute-networkinterfaceid""", alias="NetworkInterfaceId")
    LocalGatewayVirtualInterfaceGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html#cfn-ec2-localgatewayroute-localgatewayvirtualinterfacegroupid""", alias="LocalGatewayVirtualInterfaceGroupId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.LocalGatewayRoute:
        from troposphere.ec2 import LocalGatewayRoute as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import LocalGatewayRoute as TropoT
        return resource_to_troposphere(self, TropoT)


class LocalGatewayRouteTable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetable.html
    Properties:
        - Name: LocalGatewayId
        - Name: Mode
        - Name: Tags
    Attributes:
        - Name: OwnerId
        - Name: State
        - Name: OutpostArn
        - Name: LocalGatewayRouteTableId
        - Name: LocalGatewayRouteTableArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LocalGatewayId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetable.html#cfn-ec2-localgatewayroutetable-localgatewayid""", alias="LocalGatewayId")
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetable.html#cfn-ec2-localgatewayroutetable-mode""", alias="Mode")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetable.html#cfn-ec2-localgatewayroutetable-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.LocalGatewayRouteTable:
        from troposphere.ec2 import LocalGatewayRouteTable as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import LocalGatewayRouteTable as TropoT
        return resource_to_troposphere(self, TropoT)


class LocalGatewayRouteTableVPCAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevpcassociation.html
    Properties:
        - Name: VpcId
        - Name: LocalGatewayRouteTableId
        - Name: Tags
    Attributes:
        - Name: LocalGatewayId
        - Name: State
        - Name: LocalGatewayRouteTableVpcAssociationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevpcassociation.html#cfn-ec2-localgatewayroutetablevpcassociation-vpcid""", alias="VpcId")
    LocalGatewayRouteTableId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevpcassociation.html#cfn-ec2-localgatewayroutetablevpcassociation-localgatewayroutetableid""", alias="LocalGatewayRouteTableId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevpcassociation.html#cfn-ec2-localgatewayroutetablevpcassociation-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.LocalGatewayRouteTableVPCAssociation:
        from troposphere.ec2 import LocalGatewayRouteTableVPCAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import LocalGatewayRouteTableVPCAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class LocalGatewayRouteTableVirtualInterfaceGroupAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevirtualinterfacegroupassociation.html
    Properties:
        - Name: LocalGatewayRouteTableId
        - Name: Tags
        - Name: LocalGatewayVirtualInterfaceGroupId
    Attributes:
        - Name: OwnerId
        - Name: LocalGatewayId
        - Name: State
        - Name: LocalGatewayRouteTableVirtualInterfaceGroupAssociationId
        - Name: LocalGatewayRouteTableArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LocalGatewayRouteTableId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevirtualinterfacegroupassociation.html#cfn-ec2-localgatewayroutetablevirtualinterfacegroupassociation-localgatewayroutetableid""", alias="LocalGatewayRouteTableId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevirtualinterfacegroupassociation.html#cfn-ec2-localgatewayroutetablevirtualinterfacegroupassociation-tags""", alias="Tags")
    LocalGatewayVirtualInterfaceGroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevirtualinterfacegroupassociation.html#cfn-ec2-localgatewayroutetablevirtualinterfacegroupassociation-localgatewayvirtualinterfacegroupid""", alias="LocalGatewayVirtualInterfaceGroupId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.LocalGatewayRouteTableVirtualInterfaceGroupAssociation:
        from troposphere.ec2 import LocalGatewayRouteTableVirtualInterfaceGroupAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import LocalGatewayRouteTableVirtualInterfaceGroupAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class NatGateway(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html
    Properties:
        - Name: SecondaryAllocationIds
        - Name: PrivateIpAddress
        - Name: ConnectivityType
        - Name: SecondaryPrivateIpAddresses
        - Name: SecondaryPrivateIpAddressCount
        - Name: AllocationId
        - Name: SubnetId
        - Name: Tags
        - Name: MaxDrainDurationSeconds
    Attributes:
        - Name: NatGatewayId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SecondaryAllocationIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-secondaryallocationids""", alias="SecondaryAllocationIds")
    PrivateIpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-privateipaddress""", alias="PrivateIpAddress")
    ConnectivityType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-connectivitytype""", alias="ConnectivityType")
    SecondaryPrivateIpAddresses_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-secondaryprivateipaddresses""", alias="SecondaryPrivateIpAddresses")
    SecondaryPrivateIpAddressCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-secondaryprivateipaddresscount""", alias="SecondaryPrivateIpAddressCount")
    AllocationId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-allocationid""", alias="AllocationId")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-subnetid""", alias="SubnetId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-tags""", alias="Tags")
    MaxDrainDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-maxdraindurationseconds""", alias="MaxDrainDurationSeconds")
    

    @property
    def tropo_type(self) -> troposphere.ec2.NatGateway:
        from troposphere.ec2 import NatGateway as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import NatGateway as TropoT
        return resource_to_troposphere(self, TropoT)


class NetworkAcl(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkacl.html
    Properties:
        - Name: VpcId
        - Name: Tags
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkacl.html#cfn-ec2-networkacl-vpcid""", alias="VpcId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkacl.html#cfn-ec2-networkacl-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.NetworkAcl:
        from troposphere.ec2 import NetworkAcl as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import NetworkAcl as TropoT
        return resource_to_troposphere(self, TropoT)


class NetworkAclEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.html
    Properties:
        - Name: PortRange
        - Name: NetworkAclId
        - Name: RuleAction
        - Name: CidrBlock
        - Name: Egress
        - Name: RuleNumber
        - Name: Ipv6CidrBlock
        - Name: Protocol
        - Name: Icmp
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PortRange_: Optional['PortRange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.html#cfn-ec2-networkaclentry-portrange""", alias="PortRange")
    NetworkAclId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.html#cfn-ec2-networkaclentry-networkaclid""", alias="NetworkAclId")
    RuleAction_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.html#cfn-ec2-networkaclentry-ruleaction""", alias="RuleAction")
    CidrBlock_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.html#cfn-ec2-networkaclentry-cidrblock""", alias="CidrBlock")
    Egress_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.html#cfn-ec2-networkaclentry-egress""", alias="Egress")
    RuleNumber_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.html#cfn-ec2-networkaclentry-rulenumber""", alias="RuleNumber")
    Ipv6CidrBlock_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.html#cfn-ec2-networkaclentry-ipv6cidrblock""", alias="Ipv6CidrBlock")
    Protocol_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.html#cfn-ec2-networkaclentry-protocol""", alias="Protocol")
    Icmp_: Optional['Icmp'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.html#cfn-ec2-networkaclentry-icmp""", alias="Icmp")
    

    @property
    def tropo_type(self) -> troposphere.ec2.NetworkAclEntry:
        from troposphere.ec2 import NetworkAclEntry as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import NetworkAclEntry as TropoT
        return resource_to_troposphere(self, TropoT)


class NetworkInsightsAccessScope(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsaccessscope.html
    Properties:
        - Name: ExcludePaths
        - Name: MatchPaths
        - Name: Tags
    Attributes:
        - Name: UpdatedDate
        - Name: CreatedDate
        - Name: NetworkInsightsAccessScopeArn
        - Name: NetworkInsightsAccessScopeId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ExcludePaths_: Optional[List['AccessScopePathRequest']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsaccessscope.html#cfn-ec2-networkinsightsaccessscope-excludepaths""", alias="ExcludePaths")
    MatchPaths_: Optional[List['AccessScopePathRequest']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsaccessscope.html#cfn-ec2-networkinsightsaccessscope-matchpaths""", alias="MatchPaths")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsaccessscope.html#cfn-ec2-networkinsightsaccessscope-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.NetworkInsightsAccessScope:
        from troposphere.ec2 import NetworkInsightsAccessScope as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import NetworkInsightsAccessScope as TropoT
        return resource_to_troposphere(self, TropoT)


class NetworkInsightsAccessScopeAnalysis(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsaccessscopeanalysis.html
    Properties:
        - Name: NetworkInsightsAccessScopeId
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: StartDate
        - Name: NetworkInsightsAccessScopeAnalysisId
        - Name: NetworkInsightsAccessScopeAnalysisArn
        - Name: EndDate
        - Name: AnalyzedEniCount
        - Name: FindingsFound
        - Name: StatusMessage
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NetworkInsightsAccessScopeId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsaccessscopeanalysis.html#cfn-ec2-networkinsightsaccessscopeanalysis-networkinsightsaccessscopeid""", alias="NetworkInsightsAccessScopeId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsaccessscopeanalysis.html#cfn-ec2-networkinsightsaccessscopeanalysis-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.NetworkInsightsAccessScopeAnalysis:
        from troposphere.ec2 import NetworkInsightsAccessScopeAnalysis as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import NetworkInsightsAccessScopeAnalysis as TropoT
        return resource_to_troposphere(self, TropoT)


class NetworkInsightsAnalysis(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html
    Properties:
        - Name: NetworkInsightsPathId
        - Name: FilterInArns
        - Name: AdditionalAccounts
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: ReturnPathComponents
        - Name: StartDate
        - Name: NetworkInsightsAnalysisId
        - Name: AlternatePathHints
        - Name: Explanations
        - Name: NetworkPathFound
        - Name: SuggestedAccounts
        - Name: ForwardPathComponents
        - Name: NetworkInsightsAnalysisArn
        - Name: StatusMessage
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NetworkInsightsPathId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-networkinsightspathid""", alias="NetworkInsightsPathId")
    FilterInArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-filterinarns""", alias="FilterInArns")
    AdditionalAccounts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-additionalaccounts""", alias="AdditionalAccounts")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightsanalysis.html#cfn-ec2-networkinsightsanalysis-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.NetworkInsightsAnalysis:
        from troposphere.ec2 import NetworkInsightsAnalysis as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import NetworkInsightsAnalysis as TropoT
        return resource_to_troposphere(self, TropoT)


class NetworkInsightsPath(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightspath.html
    Properties:
        - Name: Destination
        - Name: DestinationIp
        - Name: SourceIp
        - Name: FilterAtDestination
        - Name: FilterAtSource
        - Name: Protocol
        - Name: DestinationPort
        - Name: Source
        - Name: Tags
    Attributes:
        - Name: SourceArn
        - Name: NetworkInsightsPathId
        - Name: CreatedDate
        - Name: NetworkInsightsPathArn
        - Name: DestinationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Destination_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightspath.html#cfn-ec2-networkinsightspath-destination""", alias="Destination")
    DestinationIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightspath.html#cfn-ec2-networkinsightspath-destinationip""", alias="DestinationIp")
    SourceIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightspath.html#cfn-ec2-networkinsightspath-sourceip""", alias="SourceIp")
    FilterAtDestination_: Optional['PathFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightspath.html#cfn-ec2-networkinsightspath-filteratdestination""", alias="FilterAtDestination")
    FilterAtSource_: Optional['PathFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightspath.html#cfn-ec2-networkinsightspath-filteratsource""", alias="FilterAtSource")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightspath.html#cfn-ec2-networkinsightspath-protocol""", alias="Protocol")
    DestinationPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightspath.html#cfn-ec2-networkinsightspath-destinationport""", alias="DestinationPort")
    Source_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightspath.html#cfn-ec2-networkinsightspath-source""", alias="Source")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinsightspath.html#cfn-ec2-networkinsightspath-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.NetworkInsightsPath:
        from troposphere.ec2 import NetworkInsightsPath as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import NetworkInsightsPath as TropoT
        return resource_to_troposphere(self, TropoT)


class NetworkInterface(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html
    Properties:
        - Name: Description
        - Name: PrivateIpAddress
        - Name: PrivateIpAddresses
        - Name: SecondaryPrivateIpAddressCount
        - Name: Ipv6PrefixCount
        - Name: Ipv4Prefixes
        - Name: Ipv4PrefixCount
        - Name: GroupSet
        - Name: Ipv6Addresses
        - Name: Ipv6Prefixes
        - Name: SubnetId
        - Name: SourceDestCheck
        - Name: InterfaceType
        - Name: Ipv6AddressCount
        - Name: Tags
    Attributes:
        - Name: SecondaryPrivateIpAddresses
        - Name: PrimaryPrivateIpAddress
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-description""", alias="Description")
    PrivateIpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-privateipaddress""", alias="PrivateIpAddress")
    PrivateIpAddresses_: Optional[List['PrivateIpAddressSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-privateipaddresses""", alias="PrivateIpAddresses")
    SecondaryPrivateIpAddressCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-secondaryprivateipaddresscount""", alias="SecondaryPrivateIpAddressCount")
    Ipv6PrefixCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-ipv6prefixcount""", alias="Ipv6PrefixCount")
    Ipv4Prefixes_: Optional[List['Ipv4PrefixSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-ipv4prefixes""", alias="Ipv4Prefixes")
    Ipv4PrefixCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-ipv4prefixcount""", alias="Ipv4PrefixCount")
    GroupSet_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-groupset""", alias="GroupSet")
    Ipv6Addresses_: Optional[List['InstanceIpv6Address']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-ipv6addresses""", alias="Ipv6Addresses")
    Ipv6Prefixes_: Optional[List['Ipv6PrefixSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-ipv6prefixes""", alias="Ipv6Prefixes")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-subnetid""", alias="SubnetId")
    SourceDestCheck_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-sourcedestcheck""", alias="SourceDestCheck")
    InterfaceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-interfacetype""", alias="InterfaceType")
    Ipv6AddressCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-ipv6addresscount""", alias="Ipv6AddressCount")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterface.html#cfn-ec2-networkinterface-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.NetworkInterface:
        from troposphere.ec2 import NetworkInterface as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import NetworkInterface as TropoT
        return resource_to_troposphere(self, TropoT)


class NetworkInterfaceAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfaceattachment.html
    Properties:
        - Name: InstanceId
        - Name: DeviceIndex
        - Name: NetworkInterfaceId
        - Name: DeleteOnTermination
    Attributes:
        - Name: AttachmentId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InstanceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfaceattachment.html#cfn-ec2-networkinterfaceattachment-instanceid""", alias="InstanceId")
    DeviceIndex_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfaceattachment.html#cfn-ec2-networkinterfaceattachment-deviceindex""", alias="DeviceIndex")
    NetworkInterfaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfaceattachment.html#cfn-ec2-networkinterfaceattachment-networkinterfaceid""", alias="NetworkInterfaceId")
    DeleteOnTermination_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfaceattachment.html#cfn-ec2-networkinterfaceattachment-deleteontermination""", alias="DeleteOnTermination")
    

    @property
    def tropo_type(self) -> troposphere.ec2.NetworkInterfaceAttachment:
        from troposphere.ec2 import NetworkInterfaceAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import NetworkInterfaceAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class NetworkInterfacePermission(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html
    Properties:
        - Name: AwsAccountId
        - Name: NetworkInterfaceId
        - Name: Permission
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AwsAccountId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html#cfn-ec2-networkinterfacepermission-awsaccountid""", alias="AwsAccountId")
    NetworkInterfaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html#cfn-ec2-networkinterfacepermission-networkinterfaceid""", alias="NetworkInterfaceId")
    Permission_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html#cfn-ec2-networkinterfacepermission-permission""", alias="Permission")
    

    @property
    def tropo_type(self) -> troposphere.ec2.NetworkInterfacePermission:
        from troposphere.ec2 import NetworkInterfacePermission as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import NetworkInterfacePermission as TropoT
        return resource_to_troposphere(self, TropoT)


class NetworkPerformanceMetricSubscription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkperformancemetricsubscription.html
    Properties:
        - Name: Destination
        - Name: Statistic
        - Name: Metric
        - Name: Source
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Destination_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkperformancemetricsubscription.html#cfn-ec2-networkperformancemetricsubscription-destination""", alias="Destination")
    Statistic_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkperformancemetricsubscription.html#cfn-ec2-networkperformancemetricsubscription-statistic""", alias="Statistic")
    Metric_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkperformancemetricsubscription.html#cfn-ec2-networkperformancemetricsubscription-metric""", alias="Metric")
    Source_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkperformancemetricsubscription.html#cfn-ec2-networkperformancemetricsubscription-source""", alias="Source")
    

    @property
    def tropo_type(self) -> troposphere.ec2.NetworkPerformanceMetricSubscription:
        from troposphere.ec2 import NetworkPerformanceMetricSubscription as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import NetworkPerformanceMetricSubscription as TropoT
        return resource_to_troposphere(self, TropoT)


class PlacementGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.html
    Properties:
        - Name: SpreadLevel
        - Name: Strategy
        - Name: PartitionCount
        - Name: Tags
    Attributes:
        - Name: GroupName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SpreadLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.html#cfn-ec2-placementgroup-spreadlevel""", alias="SpreadLevel")
    Strategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.html#cfn-ec2-placementgroup-strategy""", alias="Strategy")
    PartitionCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.html#cfn-ec2-placementgroup-partitioncount""", alias="PartitionCount")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.html#cfn-ec2-placementgroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.PlacementGroup:
        from troposphere.ec2 import PlacementGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import PlacementGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class PrefixList(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-prefixlist.html
    Properties:
        - Name: MaxEntries
        - Name: PrefixListName
        - Name: Entries
        - Name: AddressFamily
        - Name: Tags
    Attributes:
        - Name: OwnerId
        - Name: PrefixListId
        - Name: Version
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MaxEntries_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-prefixlist.html#cfn-ec2-prefixlist-maxentries""", alias="MaxEntries")
    PrefixListName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-prefixlist.html#cfn-ec2-prefixlist-prefixlistname""", alias="PrefixListName")
    Entries_: Optional[List['Entry']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-prefixlist.html#cfn-ec2-prefixlist-entries""", alias="Entries")
    AddressFamily_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-prefixlist.html#cfn-ec2-prefixlist-addressfamily""", alias="AddressFamily")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-prefixlist.html#cfn-ec2-prefixlist-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.PrefixList:
        from troposphere.ec2 import PrefixList as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import PrefixList as TropoT
        return resource_to_troposphere(self, TropoT)


class Route(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html
    Properties:
        - Name: DestinationIpv6CidrBlock
        - Name: RouteTableId
        - Name: InstanceId
        - Name: LocalGatewayId
        - Name: CarrierGatewayId
        - Name: DestinationCidrBlock
        - Name: GatewayId
        - Name: NetworkInterfaceId
        - Name: VpcEndpointId
        - Name: TransitGatewayId
        - Name: VpcPeeringConnectionId
        - Name: EgressOnlyInternetGatewayId
        - Name: DestinationPrefixListId
        - Name: NatGatewayId
    Attributes:
        - Name: CidrBlock
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DestinationIpv6CidrBlock_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-destinationipv6cidrblock""", alias="DestinationIpv6CidrBlock")
    RouteTableId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-routetableid""", alias="RouteTableId")
    InstanceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-instanceid""", alias="InstanceId")
    LocalGatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-localgatewayid""", alias="LocalGatewayId")
    CarrierGatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-carriergatewayid""", alias="CarrierGatewayId")
    DestinationCidrBlock_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-destinationcidrblock""", alias="DestinationCidrBlock")
    GatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-gatewayid""", alias="GatewayId")
    NetworkInterfaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-networkinterfaceid""", alias="NetworkInterfaceId")
    VpcEndpointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-vpcendpointid""", alias="VpcEndpointId")
    TransitGatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-transitgatewayid""", alias="TransitGatewayId")
    VpcPeeringConnectionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-vpcpeeringconnectionid""", alias="VpcPeeringConnectionId")
    EgressOnlyInternetGatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-egressonlyinternetgatewayid""", alias="EgressOnlyInternetGatewayId")
    DestinationPrefixListId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-destinationprefixlistid""", alias="DestinationPrefixListId")
    NatGatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-natgatewayid""", alias="NatGatewayId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.Route:
        from troposphere.ec2 import Route as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import Route as TropoT
        return resource_to_troposphere(self, TropoT)


class RouteTable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-routetable.html
    Properties:
        - Name: VpcId
        - Name: Tags
    Attributes:
        - Name: RouteTableId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-routetable.html#cfn-ec2-routetable-vpcid""", alias="VpcId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-routetable.html#cfn-ec2-routetable-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.RouteTable:
        from troposphere.ec2 import RouteTable as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import RouteTable as TropoT
        return resource_to_troposphere(self, TropoT)


class SecurityGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html
    Properties:
        - Name: GroupDescription
        - Name: GroupName
        - Name: SecurityGroupEgress
        - Name: SecurityGroupIngress
        - Name: Tags
        - Name: VpcId
    Attributes:
        - Name: GroupId
        - Name: VpcId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GroupDescription_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-groupdescription""", alias="GroupDescription")
    GroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-groupname""", alias="GroupName")
    SecurityGroupEgress_: Optional[List['Egress']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-securitygroupegress""", alias="SecurityGroupEgress")
    SecurityGroupIngress_: Optional[List['Ingress']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-securitygroupingress""", alias="SecurityGroupIngress")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-tags""", alias="Tags")
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-vpcid""", alias="VpcId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.SecurityGroup:
        from troposphere.ec2 import SecurityGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import SecurityGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class SecurityGroupEgress(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html
    Properties:
        - Name: CidrIp
        - Name: CidrIpv6
        - Name: Description
        - Name: DestinationPrefixListId
        - Name: DestinationSecurityGroupId
        - Name: FromPort
        - Name: GroupId
        - Name: IpProtocol
        - Name: ToPort
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CidrIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-cidrip""", alias="CidrIp")
    CidrIpv6_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-cidripv6""", alias="CidrIpv6")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-description""", alias="Description")
    DestinationPrefixListId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-destinationprefixlistid""", alias="DestinationPrefixListId")
    DestinationSecurityGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-destinationsecuritygroupid""", alias="DestinationSecurityGroupId")
    FromPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-fromport""", alias="FromPort")
    GroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-groupid""", alias="GroupId")
    IpProtocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-ipprotocol""", alias="IpProtocol")
    ToPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-toport""", alias="ToPort")
    

    @property
    def tropo_type(self) -> troposphere.ec2.SecurityGroupEgress:
        from troposphere.ec2 import SecurityGroupEgress as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import SecurityGroupEgress as TropoT
        return resource_to_troposphere(self, TropoT)


class SecurityGroupIngress(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html
    Properties:
        - Name: CidrIp
        - Name: CidrIpv6
        - Name: Description
        - Name: FromPort
        - Name: GroupId
        - Name: GroupName
        - Name: IpProtocol
        - Name: SourcePrefixListId
        - Name: SourceSecurityGroupId
        - Name: SourceSecurityGroupName
        - Name: SourceSecurityGroupOwnerId
        - Name: ToPort
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CidrIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-cidrip""", alias="CidrIp")
    CidrIpv6_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-cidripv6""", alias="CidrIpv6")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-description""", alias="Description")
    FromPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-fromport""", alias="FromPort")
    GroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-groupid""", alias="GroupId")
    GroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-groupname""", alias="GroupName")
    IpProtocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-ipprotocol""", alias="IpProtocol")
    SourcePrefixListId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-securitygroupingress-sourceprefixlistid""", alias="SourcePrefixListId")
    SourceSecurityGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-sourcesecuritygroupid""", alias="SourceSecurityGroupId")
    SourceSecurityGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-sourcesecuritygroupname""", alias="SourceSecurityGroupName")
    SourceSecurityGroupOwnerId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-sourcesecuritygroupownerid""", alias="SourceSecurityGroupOwnerId")
    ToPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-toport""", alias="ToPort")
    

    @property
    def tropo_type(self) -> troposphere.ec2.SecurityGroupIngress:
        from troposphere.ec2 import SecurityGroupIngress as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import SecurityGroupIngress as TropoT
        return resource_to_troposphere(self, TropoT)


class SpotFleet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-spotfleet.html
    Properties:
        - Name: SpotFleetRequestConfigData
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SpotFleetRequestConfigData_: 'SpotFleetRequestConfigData' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-spotfleet.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata""", alias="SpotFleetRequestConfigData")
    

    @property
    def tropo_type(self) -> troposphere.ec2.SpotFleet:
        from troposphere.ec2 import SpotFleet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import SpotFleet as TropoT
        return resource_to_troposphere(self, TropoT)


class Subnet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html
    Properties:
        - Name: MapPublicIpOnLaunch
        - Name: EnableDns64
        - Name: AvailabilityZoneId
        - Name: OutpostArn
        - Name: AvailabilityZone
        - Name: CidrBlock
        - Name: Ipv6NetmaskLength
        - Name: AssignIpv6AddressOnCreation
        - Name: VpcId
        - Name: Ipv4NetmaskLength
        - Name: PrivateDnsNameOptionsOnLaunch
        - Name: Ipv6Native
        - Name: Ipv6CidrBlock
        - Name: Tags
    Attributes:
        - Name: VpcId
        - Name: NetworkAclAssociationId
        - Name: AvailabilityZoneId
        - Name: OutpostArn
        - Name: AvailabilityZone
        - Name: CidrBlock
        - Name: SubnetId
        - Name: Ipv6CidrBlocks
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MapPublicIpOnLaunch_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-mappubliciponlaunch""", alias="MapPublicIpOnLaunch")
    EnableDns64_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-enabledns64""", alias="EnableDns64")
    AvailabilityZoneId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-availabilityzoneid""", alias="AvailabilityZoneId")
    OutpostArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-outpostarn""", alias="OutpostArn")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-availabilityzone""", alias="AvailabilityZone")
    CidrBlock_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-cidrblock""", alias="CidrBlock")
    Ipv6NetmaskLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-ipv6netmasklength""", alias="Ipv6NetmaskLength")
    AssignIpv6AddressOnCreation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-assignipv6addressoncreation""", alias="AssignIpv6AddressOnCreation")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-vpcid""", alias="VpcId")
    Ipv4NetmaskLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-ipv4netmasklength""", alias="Ipv4NetmaskLength")
    PrivateDnsNameOptionsOnLaunch_: Optional['PrivateDnsNameOptionsOnLaunch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-privatednsnameoptionsonlaunch""", alias="PrivateDnsNameOptionsOnLaunch")
    Ipv6Native_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-ipv6native""", alias="Ipv6Native")
    Ipv6CidrBlock_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-ipv6cidrblock""", alias="Ipv6CidrBlock")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.Subnet:
        from troposphere.ec2 import Subnet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import Subnet as TropoT
        return resource_to_troposphere(self, TropoT)


class SubnetCidrBlock(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.html
    Properties:
        - Name: SubnetId
        - Name: Ipv6CidrBlock
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.html#cfn-ec2-subnetcidrblock-subnetid""", alias="SubnetId")
    Ipv6CidrBlock_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.html#cfn-ec2-subnetcidrblock-ipv6cidrblock""", alias="Ipv6CidrBlock")
    

    @property
    def tropo_type(self) -> troposphere.ec2.SubnetCidrBlock:
        from troposphere.ec2 import SubnetCidrBlock as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import SubnetCidrBlock as TropoT
        return resource_to_troposphere(self, TropoT)


class SubnetNetworkAclAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-network-acl-assoc.html
    Properties:
        - Name: NetworkAclId
        - Name: SubnetId
    Attributes:
        - Name: AssociationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NetworkAclId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-network-acl-assoc.html#cfn-ec2-subnetnetworkaclassociation-networkaclid""", alias="NetworkAclId")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-network-acl-assoc.html#cfn-ec2-subnetnetworkaclassociation-associationid""", alias="SubnetId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.SubnetNetworkAclAssociation:
        from troposphere.ec2 import SubnetNetworkAclAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import SubnetNetworkAclAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class SubnetRouteTableAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetroutetableassociation.html
    Properties:
        - Name: RouteTableId
        - Name: SubnetId
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RouteTableId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetroutetableassociation.html#cfn-ec2-subnetroutetableassociation-routetableid""", alias="RouteTableId")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetroutetableassociation.html#cfn-ec2-subnetroutetableassociation-subnetid""", alias="SubnetId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.SubnetRouteTableAssociation:
        from troposphere.ec2 import SubnetRouteTableAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import SubnetRouteTableAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class TrafficMirrorFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilter.html
    Properties:
        - Name: Description
        - Name: NetworkServices
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilter.html#cfn-ec2-trafficmirrorfilter-description""", alias="Description")
    NetworkServices_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilter.html#cfn-ec2-trafficmirrorfilter-networkservices""", alias="NetworkServices")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilter.html#cfn-ec2-trafficmirrorfilter-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TrafficMirrorFilter:
        from troposphere.ec2 import TrafficMirrorFilter as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TrafficMirrorFilter as TropoT
        return resource_to_troposphere(self, TropoT)


class TrafficMirrorFilterRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html
    Properties:
        - Name: DestinationPortRange
        - Name: Description
        - Name: SourcePortRange
        - Name: RuleAction
        - Name: SourceCidrBlock
        - Name: RuleNumber
        - Name: DestinationCidrBlock
        - Name: TrafficMirrorFilterId
        - Name: TrafficDirection
        - Name: Protocol
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DestinationPortRange_: Optional['TrafficMirrorPortRange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html#cfn-ec2-trafficmirrorfilterrule-destinationportrange""", alias="DestinationPortRange")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html#cfn-ec2-trafficmirrorfilterrule-description""", alias="Description")
    SourcePortRange_: Optional['TrafficMirrorPortRange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html#cfn-ec2-trafficmirrorfilterrule-sourceportrange""", alias="SourcePortRange")
    RuleAction_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html#cfn-ec2-trafficmirrorfilterrule-ruleaction""", alias="RuleAction")
    SourceCidrBlock_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html#cfn-ec2-trafficmirrorfilterrule-sourcecidrblock""", alias="SourceCidrBlock")
    RuleNumber_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html#cfn-ec2-trafficmirrorfilterrule-rulenumber""", alias="RuleNumber")
    DestinationCidrBlock_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html#cfn-ec2-trafficmirrorfilterrule-destinationcidrblock""", alias="DestinationCidrBlock")
    TrafficMirrorFilterId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html#cfn-ec2-trafficmirrorfilterrule-trafficmirrorfilterid""", alias="TrafficMirrorFilterId")
    TrafficDirection_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html#cfn-ec2-trafficmirrorfilterrule-trafficdirection""", alias="TrafficDirection")
    Protocol_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html#cfn-ec2-trafficmirrorfilterrule-protocol""", alias="Protocol")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TrafficMirrorFilterRule:
        from troposphere.ec2 import TrafficMirrorFilterRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TrafficMirrorFilterRule as TropoT
        return resource_to_troposphere(self, TropoT)


class TrafficMirrorSession(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html
    Properties:
        - Name: TrafficMirrorTargetId
        - Name: Description
        - Name: SessionNumber
        - Name: VirtualNetworkId
        - Name: PacketLength
        - Name: NetworkInterfaceId
        - Name: TrafficMirrorFilterId
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TrafficMirrorTargetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html#cfn-ec2-trafficmirrorsession-trafficmirrortargetid""", alias="TrafficMirrorTargetId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html#cfn-ec2-trafficmirrorsession-description""", alias="Description")
    SessionNumber_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html#cfn-ec2-trafficmirrorsession-sessionnumber""", alias="SessionNumber")
    VirtualNetworkId_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html#cfn-ec2-trafficmirrorsession-virtualnetworkid""", alias="VirtualNetworkId")
    PacketLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html#cfn-ec2-trafficmirrorsession-packetlength""", alias="PacketLength")
    NetworkInterfaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html#cfn-ec2-trafficmirrorsession-networkinterfaceid""", alias="NetworkInterfaceId")
    TrafficMirrorFilterId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html#cfn-ec2-trafficmirrorsession-trafficmirrorfilterid""", alias="TrafficMirrorFilterId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html#cfn-ec2-trafficmirrorsession-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TrafficMirrorSession:
        from troposphere.ec2 import TrafficMirrorSession as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TrafficMirrorSession as TropoT
        return resource_to_troposphere(self, TropoT)


class TrafficMirrorTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrortarget.html
    Properties:
        - Name: NetworkLoadBalancerArn
        - Name: Description
        - Name: NetworkInterfaceId
        - Name: GatewayLoadBalancerEndpointId
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NetworkLoadBalancerArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrortarget.html#cfn-ec2-trafficmirrortarget-networkloadbalancerarn""", alias="NetworkLoadBalancerArn")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrortarget.html#cfn-ec2-trafficmirrortarget-description""", alias="Description")
    NetworkInterfaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrortarget.html#cfn-ec2-trafficmirrortarget-networkinterfaceid""", alias="NetworkInterfaceId")
    GatewayLoadBalancerEndpointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrortarget.html#cfn-ec2-trafficmirrortarget-gatewayloadbalancerendpointid""", alias="GatewayLoadBalancerEndpointId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrortarget.html#cfn-ec2-trafficmirrortarget-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TrafficMirrorTarget:
        from troposphere.ec2 import TrafficMirrorTarget as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TrafficMirrorTarget as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGateway(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html
    Properties:
        - Name: DefaultRouteTablePropagation
        - Name: Description
        - Name: TransitGatewayCidrBlocks
        - Name: AssociationDefaultRouteTableId
        - Name: AutoAcceptSharedAttachments
        - Name: PropagationDefaultRouteTableId
        - Name: DefaultRouteTableAssociation
        - Name: VpnEcmpSupport
        - Name: DnsSupport
        - Name: MulticastSupport
        - Name: AmazonSideAsn
        - Name: Tags
    Attributes:
        - Name: TransitGatewayArn
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DefaultRouteTablePropagation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-defaultroutetablepropagation""", alias="DefaultRouteTablePropagation")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-description""", alias="Description")
    TransitGatewayCidrBlocks_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-transitgatewaycidrblocks""", alias="TransitGatewayCidrBlocks")
    AssociationDefaultRouteTableId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-associationdefaultroutetableid""", alias="AssociationDefaultRouteTableId")
    AutoAcceptSharedAttachments_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-autoacceptsharedattachments""", alias="AutoAcceptSharedAttachments")
    PropagationDefaultRouteTableId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-propagationdefaultroutetableid""", alias="PropagationDefaultRouteTableId")
    DefaultRouteTableAssociation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-defaultroutetableassociation""", alias="DefaultRouteTableAssociation")
    VpnEcmpSupport_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-vpnecmpsupport""", alias="VpnEcmpSupport")
    DnsSupport_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-dnssupport""", alias="DnsSupport")
    MulticastSupport_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-multicastsupport""", alias="MulticastSupport")
    AmazonSideAsn_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-amazonsideasn""", alias="AmazonSideAsn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TransitGateway:
        from troposphere.ec2 import TransitGateway as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TransitGateway as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html
    Properties:
        - Name: Options
        - Name: TransitGatewayId
        - Name: VpcId
        - Name: SubnetIds
        - Name: Tags
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Options_: Optional['Options'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html#cfn-ec2-transitgatewayattachment-options""", alias="Options")
    TransitGatewayId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html#cfn-ec2-transitgatewayattachment-transitgatewayid""", alias="TransitGatewayId")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html#cfn-ec2-transitgatewayattachment-vpcid""", alias="VpcId")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html#cfn-ec2-transitgatewayattachment-subnetids""", alias="SubnetIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html#cfn-ec2-transitgatewayattachment-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayAttachment:
        from troposphere.ec2 import TransitGatewayAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TransitGatewayAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayConnect(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayconnect.html
    Properties:
        - Name: Options
        - Name: TransportTransitGatewayAttachmentId
        - Name: Tags
    Attributes:
        - Name: TransitGatewayId
        - Name: State
        - Name: CreationTime
        - Name: TransitGatewayAttachmentId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Options_: 'TransitGatewayConnectOptions' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayconnect.html#cfn-ec2-transitgatewayconnect-options""", alias="Options")
    TransportTransitGatewayAttachmentId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayconnect.html#cfn-ec2-transitgatewayconnect-transporttransitgatewayattachmentid""", alias="TransportTransitGatewayAttachmentId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayconnect.html#cfn-ec2-transitgatewayconnect-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayConnect:
        from troposphere.ec2 import TransitGatewayConnect as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TransitGatewayConnect as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayMulticastDomain(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomain.html
    Properties:
        - Name: Options
        - Name: TransitGatewayId
        - Name: Tags
    Attributes:
        - Name: TransitGatewayMulticastDomainArn
        - Name: State
        - Name: CreationTime
        - Name: TransitGatewayMulticastDomainId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Options_: Optional['Options'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomain.html#cfn-ec2-transitgatewaymulticastdomain-options""", alias="Options")
    TransitGatewayId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomain.html#cfn-ec2-transitgatewaymulticastdomain-transitgatewayid""", alias="TransitGatewayId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomain.html#cfn-ec2-transitgatewaymulticastdomain-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayMulticastDomain:
        from troposphere.ec2 import TransitGatewayMulticastDomain as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TransitGatewayMulticastDomain as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayMulticastDomainAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomainassociation.html
    Properties:
        - Name: TransitGatewayMulticastDomainId
        - Name: SubnetId
        - Name: TransitGatewayAttachmentId
    Attributes:
        - Name: ResourceId
        - Name: State
        - Name: ResourceType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TransitGatewayMulticastDomainId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomainassociation.html#cfn-ec2-transitgatewaymulticastdomainassociation-transitgatewaymulticastdomainid""", alias="TransitGatewayMulticastDomainId")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomainassociation.html#cfn-ec2-transitgatewaymulticastdomainassociation-subnetid""", alias="SubnetId")
    TransitGatewayAttachmentId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomainassociation.html#cfn-ec2-transitgatewaymulticastdomainassociation-transitgatewayattachmentid""", alias="TransitGatewayAttachmentId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayMulticastDomainAssociation:
        from troposphere.ec2 import TransitGatewayMulticastDomainAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TransitGatewayMulticastDomainAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayMulticastGroupMember(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.html
    Properties:
        - Name: TransitGatewayMulticastDomainId
        - Name: NetworkInterfaceId
        - Name: GroupIpAddress
    Attributes:
        - Name: GroupMember
        - Name: ResourceId
        - Name: MemberType
        - Name: SourceType
        - Name: ResourceType
        - Name: SubnetId
        - Name: GroupSource
        - Name: TransitGatewayAttachmentId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TransitGatewayMulticastDomainId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.html#cfn-ec2-transitgatewaymulticastgroupmember-transitgatewaymulticastdomainid""", alias="TransitGatewayMulticastDomainId")
    NetworkInterfaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.html#cfn-ec2-transitgatewaymulticastgroupmember-networkinterfaceid""", alias="NetworkInterfaceId")
    GroupIpAddress_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.html#cfn-ec2-transitgatewaymulticastgroupmember-groupipaddress""", alias="GroupIpAddress")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayMulticastGroupMember:
        from troposphere.ec2 import TransitGatewayMulticastGroupMember as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TransitGatewayMulticastGroupMember as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayMulticastGroupSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html
    Properties:
        - Name: TransitGatewayMulticastDomainId
        - Name: NetworkInterfaceId
        - Name: GroupIpAddress
    Attributes:
        - Name: GroupMember
        - Name: ResourceId
        - Name: MemberType
        - Name: SourceType
        - Name: ResourceType
        - Name: SubnetId
        - Name: GroupSource
        - Name: TransitGatewayAttachmentId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TransitGatewayMulticastDomainId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html#cfn-ec2-transitgatewaymulticastgroupsource-transitgatewaymulticastdomainid""", alias="TransitGatewayMulticastDomainId")
    NetworkInterfaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html#cfn-ec2-transitgatewaymulticastgroupsource-networkinterfaceid""", alias="NetworkInterfaceId")
    GroupIpAddress_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html#cfn-ec2-transitgatewaymulticastgroupsource-groupipaddress""", alias="GroupIpAddress")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayMulticastGroupSource:
        from troposphere.ec2 import TransitGatewayMulticastGroupSource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TransitGatewayMulticastGroupSource as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayPeeringAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html
    Properties:
        - Name: TransitGatewayId
        - Name: PeerTransitGatewayId
        - Name: PeerAccountId
        - Name: PeerRegion
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: State
        - Name: CreationTime
        - Name: Status.Message
        - Name: Status.Code
        - Name: TransitGatewayAttachmentId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TransitGatewayId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-transitgatewayid""", alias="TransitGatewayId")
    PeerTransitGatewayId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-peertransitgatewayid""", alias="PeerTransitGatewayId")
    PeerAccountId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-peeraccountid""", alias="PeerAccountId")
    PeerRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-peerregion""", alias="PeerRegion")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html#cfn-ec2-transitgatewaypeeringattachment-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayPeeringAttachment:
        from troposphere.ec2 import TransitGatewayPeeringAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TransitGatewayPeeringAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayRoute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html
    Properties:
        - Name: TransitGatewayRouteTableId
        - Name: DestinationCidrBlock
        - Name: Blackhole
        - Name: TransitGatewayAttachmentId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TransitGatewayRouteTableId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html#cfn-ec2-transitgatewayroute-transitgatewayroutetableid""", alias="TransitGatewayRouteTableId")
    DestinationCidrBlock_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html#cfn-ec2-transitgatewayroute-destinationcidrblock""", alias="DestinationCidrBlock")
    Blackhole_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html#cfn-ec2-transitgatewayroute-blackhole""", alias="Blackhole")
    TransitGatewayAttachmentId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html#cfn-ec2-transitgatewayroute-transitgatewayattachmentid""", alias="TransitGatewayAttachmentId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayRoute:
        from troposphere.ec2 import TransitGatewayRoute as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TransitGatewayRoute as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayRouteTable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.html
    Properties:
        - Name: TransitGatewayId
        - Name: Tags
    Attributes:
        - Name: TransitGatewayRouteTableId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TransitGatewayId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.html#cfn-ec2-transitgatewayroutetable-transitgatewayid""", alias="TransitGatewayId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.html#cfn-ec2-transitgatewayroutetable-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayRouteTable:
        from troposphere.ec2 import TransitGatewayRouteTable as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TransitGatewayRouteTable as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayRouteTableAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.html
    Properties:
        - Name: TransitGatewayRouteTableId
        - Name: TransitGatewayAttachmentId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TransitGatewayRouteTableId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.html#cfn-ec2-transitgatewayroutetableassociation-transitgatewayroutetableid""", alias="TransitGatewayRouteTableId")
    TransitGatewayAttachmentId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.html#cfn-ec2-transitgatewayroutetableassociation-transitgatewayattachmentid""", alias="TransitGatewayAttachmentId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayRouteTableAssociation:
        from troposphere.ec2 import TransitGatewayRouteTableAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TransitGatewayRouteTableAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayRouteTablePropagation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.html
    Properties:
        - Name: TransitGatewayRouteTableId
        - Name: TransitGatewayAttachmentId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TransitGatewayRouteTableId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.html#cfn-ec2-transitgatewayroutetablepropagation-transitgatewayroutetableid""", alias="TransitGatewayRouteTableId")
    TransitGatewayAttachmentId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.html#cfn-ec2-transitgatewayroutetablepropagation-transitgatewayattachmentid""", alias="TransitGatewayAttachmentId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayRouteTablePropagation:
        from troposphere.ec2 import TransitGatewayRouteTablePropagation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TransitGatewayRouteTablePropagation as TropoT
        return resource_to_troposphere(self, TropoT)


class TransitGatewayVpcAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.html
    Properties:
        - Name: Options
        - Name: TransitGatewayId
        - Name: VpcId
        - Name: RemoveSubnetIds
        - Name: SubnetIds
        - Name: AddSubnetIds
        - Name: Tags
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Options_: Optional['Options'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.html#cfn-ec2-transitgatewayvpcattachment-options""", alias="Options")
    TransitGatewayId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.html#cfn-ec2-transitgatewayvpcattachment-transitgatewayid""", alias="TransitGatewayId")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.html#cfn-ec2-transitgatewayvpcattachment-vpcid""", alias="VpcId")
    RemoveSubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.html#cfn-ec2-transitgatewayvpcattachment-removesubnetids""", alias="RemoveSubnetIds")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.html#cfn-ec2-transitgatewayvpcattachment-subnetids""", alias="SubnetIds")
    AddSubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.html#cfn-ec2-transitgatewayvpcattachment-addsubnetids""", alias="AddSubnetIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.html#cfn-ec2-transitgatewayvpcattachment-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.TransitGatewayVpcAttachment:
        from troposphere.ec2 import TransitGatewayVpcAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import TransitGatewayVpcAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class VPC(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html
    Properties:
        - Name: InstanceTenancy
        - Name: Ipv4NetmaskLength
        - Name: CidrBlock
        - Name: Ipv4IpamPoolId
        - Name: EnableDnsSupport
        - Name: EnableDnsHostnames
        - Name: Tags
    Attributes:
        - Name: VpcId
        - Name: CidrBlockAssociations
        - Name: CidrBlock
        - Name: DefaultNetworkAcl
        - Name: Ipv6CidrBlocks
        - Name: DefaultSecurityGroup
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InstanceTenancy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-ec2-vpc-instancetenancy""", alias="InstanceTenancy")
    Ipv4NetmaskLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-ec2-vpc-ipv4netmasklength""", alias="Ipv4NetmaskLength")
    CidrBlock_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-ec2-vpc-cidrblock""", alias="CidrBlock")
    Ipv4IpamPoolId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-ec2-vpc-ipv4ipampoolid""", alias="Ipv4IpamPoolId")
    EnableDnsSupport_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-ec2-vpc-enablednssupport""", alias="EnableDnsSupport")
    EnableDnsHostnames_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-ec2-vpc-enablednshostnames""", alias="EnableDnsHostnames")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-ec2-vpc-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VPC:
        from troposphere.ec2 import VPC as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VPC as TropoT
        return resource_to_troposphere(self, TropoT)


class VPCCidrBlock(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html
    Properties:
        - Name: AmazonProvidedIpv6CidrBlock
        - Name: CidrBlock
        - Name: Ipv4IpamPoolId
        - Name: Ipv4NetmaskLength
        - Name: Ipv6CidrBlock
        - Name: Ipv6IpamPoolId
        - Name: Ipv6NetmaskLength
        - Name: Ipv6Pool
        - Name: VpcId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AmazonProvidedIpv6CidrBlock_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-amazonprovidedipv6cidrblock""", alias="AmazonProvidedIpv6CidrBlock")
    CidrBlock_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-cidrblock""", alias="CidrBlock")
    Ipv4IpamPoolId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-ipv4ipampoolid""", alias="Ipv4IpamPoolId")
    Ipv4NetmaskLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-ipv4netmasklength""", alias="Ipv4NetmaskLength")
    Ipv6CidrBlock_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-ipv6cidrblock""", alias="Ipv6CidrBlock")
    Ipv6IpamPoolId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-ipv6ipampoolid""", alias="Ipv6IpamPoolId")
    Ipv6NetmaskLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-ipv6netmasklength""", alias="Ipv6NetmaskLength")
    Ipv6Pool_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-ipv6pool""", alias="Ipv6Pool")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-vpcid""", alias="VpcId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VPCCidrBlock:
        from troposphere.ec2 import VPCCidrBlock as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VPCCidrBlock as TropoT
        return resource_to_troposphere(self, TropoT)


class VPCDHCPOptionsAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcdhcpoptionsassociation.html
    Properties:
        - Name: VpcId
        - Name: DhcpOptionsId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcdhcpoptionsassociation.html#cfn-ec2-vpcdhcpoptionsassociation-vpcid""", alias="VpcId")
    DhcpOptionsId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcdhcpoptionsassociation.html#cfn-ec2-vpcdhcpoptionsassociation-dhcpoptionsid""", alias="DhcpOptionsId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VPCDHCPOptionsAssociation:
        from troposphere.ec2 import VPCDHCPOptionsAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VPCDHCPOptionsAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class VPCEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html
    Properties:
        - Name: PrivateDnsEnabled
        - Name: VpcId
        - Name: RouteTableIds
        - Name: ServiceName
        - Name: PolicyDocument
        - Name: VpcEndpointType
        - Name: SecurityGroupIds
        - Name: SubnetIds
    Attributes:
        - Name: CreationTimestamp
        - Name: NetworkInterfaceIds
        - Name: Id
        - Name: DnsEntries
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PrivateDnsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-privatednsenabled""", alias="PrivateDnsEnabled")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-vpcid""", alias="VpcId")
    RouteTableIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-routetableids""", alias="RouteTableIds")
    ServiceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-servicename""", alias="ServiceName")
    PolicyDocument_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-policydocument""", alias="PolicyDocument")
    VpcEndpointType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-vpcendpointtype""", alias="VpcEndpointType")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-subnetids""", alias="SubnetIds")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VPCEndpoint:
        from troposphere.ec2 import VPCEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VPCEndpoint as TropoT
        return resource_to_troposphere(self, TropoT)


class VPCEndpointConnectionNotification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html
    Properties:
        - Name: ConnectionEvents
        - Name: VPCEndpointId
        - Name: ConnectionNotificationArn
        - Name: ServiceId
    Attributes:
        - Name: VPCEndpointConnectionNotificationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConnectionEvents_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html#cfn-ec2-vpcendpointconnectionnotification-connectionevents""", alias="ConnectionEvents")
    VPCEndpointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html#cfn-ec2-vpcendpointconnectionnotification-vpcendpointid""", alias="VPCEndpointId")
    ConnectionNotificationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html#cfn-ec2-vpcendpointconnectionnotification-connectionnotificationarn""", alias="ConnectionNotificationArn")
    ServiceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html#cfn-ec2-vpcendpointconnectionnotification-serviceid""", alias="ServiceId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VPCEndpointConnectionNotification:
        from troposphere.ec2 import VPCEndpointConnectionNotification as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VPCEndpointConnectionNotification as TropoT
        return resource_to_troposphere(self, TropoT)


class VPCEndpointService(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html
    Properties:
        - Name: NetworkLoadBalancerArns
        - Name: PayerResponsibility
        - Name: AcceptanceRequired
        - Name: ContributorInsightsEnabled
        - Name: GatewayLoadBalancerArns
    Attributes:
        - Name: ServiceId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NetworkLoadBalancerArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html#cfn-ec2-vpcendpointservice-networkloadbalancerarns""", alias="NetworkLoadBalancerArns")
    PayerResponsibility_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html#cfn-ec2-vpcendpointservice-payerresponsibility""", alias="PayerResponsibility")
    AcceptanceRequired_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html#cfn-ec2-vpcendpointservice-acceptancerequired""", alias="AcceptanceRequired")
    ContributorInsightsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html#cfn-ec2-vpcendpointservice-contributorinsightsenabled""", alias="ContributorInsightsEnabled")
    GatewayLoadBalancerArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html#cfn-ec2-vpcendpointservice-gatewayloadbalancerarns""", alias="GatewayLoadBalancerArns")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VPCEndpointService:
        from troposphere.ec2 import VPCEndpointService as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VPCEndpointService as TropoT
        return resource_to_troposphere(self, TropoT)


class VPCEndpointServicePermissions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.html
    Properties:
        - Name: AllowedPrincipals
        - Name: ServiceId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AllowedPrincipals_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.html#cfn-ec2-vpcendpointservicepermissions-allowedprincipals""", alias="AllowedPrincipals")
    ServiceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.html#cfn-ec2-vpcendpointservicepermissions-serviceid""", alias="ServiceId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VPCEndpointServicePermissions:
        from troposphere.ec2 import VPCEndpointServicePermissions as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VPCEndpointServicePermissions as TropoT
        return resource_to_troposphere(self, TropoT)


class VPCGatewayAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcgatewayattachment.html
    Properties:
        - Name: InternetGatewayId
        - Name: VpcId
        - Name: VpnGatewayId
    Attributes:
        - Name: AttachmentType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InternetGatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcgatewayattachment.html#cfn-ec2-vpcgatewayattachment-internetgatewayid""", alias="InternetGatewayId")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcgatewayattachment.html#cfn-ec2-vpcgatewayattachment-vpcid""", alias="VpcId")
    VpnGatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcgatewayattachment.html#cfn-ec2-vpcgatewayattachment-vpngatewayid""", alias="VpnGatewayId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VPCGatewayAttachment:
        from troposphere.ec2 import VPCGatewayAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VPCGatewayAttachment as TropoT
        return resource_to_troposphere(self, TropoT)


class VPCPeeringConnection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html
    Properties:
        - Name: PeerRoleArn
        - Name: VpcId
        - Name: PeerVpcId
        - Name: PeerRegion
        - Name: PeerOwnerId
        - Name: Tags
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PeerRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-peerrolearn""", alias="PeerRoleArn")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-vpcid""", alias="VpcId")
    PeerVpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-peervpcid""", alias="PeerVpcId")
    PeerRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-peerregion""", alias="PeerRegion")
    PeerOwnerId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-peerownerid""", alias="PeerOwnerId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VPCPeeringConnection:
        from troposphere.ec2 import VPCPeeringConnection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VPCPeeringConnection as TropoT
        return resource_to_troposphere(self, TropoT)


class VPNConnection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnection.html
    Properties:
        - Name: TransitGatewayId
        - Name: Type
        - Name: VpnTunnelOptionsSpecifications
        - Name: CustomerGatewayId
        - Name: VpnGatewayId
        - Name: StaticRoutesOnly
        - Name: Tags
    Attributes:
        - Name: VpnConnectionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TransitGatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnection.html#cfn-ec2-vpnconnection-transitgatewayid""", alias="TransitGatewayId")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnection.html#cfn-ec2-vpnconnection-type""", alias="Type")
    VpnTunnelOptionsSpecifications_: Optional[List['VpnTunnelOptionsSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnection.html#cfn-ec2-vpnconnection-vpntunneloptionsspecifications""", alias="VpnTunnelOptionsSpecifications")
    CustomerGatewayId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnection.html#cfn-ec2-vpnconnection-customergatewayid""", alias="CustomerGatewayId")
    VpnGatewayId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnection.html#cfn-ec2-vpnconnection-vpngatewayid""", alias="VpnGatewayId")
    StaticRoutesOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnection.html#cfn-ec2-vpnconnection-staticroutesonly""", alias="StaticRoutesOnly")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnection.html#cfn-ec2-vpnconnection-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VPNConnection:
        from troposphere.ec2 import VPNConnection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VPNConnection as TropoT
        return resource_to_troposphere(self, TropoT)


class VPNConnectionRoute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnectionroute.html
    Properties:
        - Name: DestinationCidrBlock
        - Name: VpnConnectionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DestinationCidrBlock_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnectionroute.html#cfn-ec2-vpnconnectionroute-destinationcidrblock""", alias="DestinationCidrBlock")
    VpnConnectionId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpnconnectionroute.html#cfn-ec2-vpnconnectionroute-vpnconnectionid""", alias="VpnConnectionId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VPNConnectionRoute:
        from troposphere.ec2 import VPNConnectionRoute as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VPNConnectionRoute as TropoT
        return resource_to_troposphere(self, TropoT)


class VPNGateway(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpngateway.html
    Properties:
        - Name: Type
        - Name: AmazonSideAsn
        - Name: Tags
    Attributes:
        - Name: VPNGatewayId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpngateway.html#cfn-ec2-vpngateway-type""", alias="Type")
    AmazonSideAsn_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpngateway.html#cfn-ec2-vpngateway-amazonsideasn""", alias="AmazonSideAsn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpngateway.html#cfn-ec2-vpngateway-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VPNGateway:
        from troposphere.ec2 import VPNGateway as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VPNGateway as TropoT
        return resource_to_troposphere(self, TropoT)


class VPNGatewayRoutePropagation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gatewayrouteprop.html
    Properties:
        - Name: RouteTableIds
        - Name: VpnGatewayId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RouteTableIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gatewayrouteprop.html#cfn-ec2-vpngatewayrouteprop-routetableids""", alias="RouteTableIds")
    VpnGatewayId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gatewayrouteprop.html#cfn-ec2-vpngatewayrouteprop-vpngatewayid""", alias="VpnGatewayId")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VPNGatewayRoutePropagation:
        from troposphere.ec2 import VPNGatewayRoutePropagation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VPNGatewayRoutePropagation as TropoT
        return resource_to_troposphere(self, TropoT)


class VerifiedAccessEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html
    Properties:
        - Name: AttachmentType
        - Name: Description
        - Name: DomainCertificateArn
        - Name: VerifiedAccessGroupId
        - Name: SecurityGroupIds
        - Name: LoadBalancerOptions
        - Name: ApplicationDomain
        - Name: PolicyEnabled
        - Name: EndpointDomainPrefix
        - Name: EndpointType
        - Name: PolicyDocument
        - Name: SseSpecification
        - Name: Tags
        - Name: NetworkInterfaceOptions
    Attributes:
        - Name: Status
        - Name: EndpointDomain
        - Name: CreationTime
        - Name: LastUpdatedTime
        - Name: DeviceValidationDomain
        - Name: VerifiedAccessInstanceId
        - Name: VerifiedAccessEndpointId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AttachmentType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-attachmenttype""", alias="AttachmentType")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-description""", alias="Description")
    DomainCertificateArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-domaincertificatearn""", alias="DomainCertificateArn")
    VerifiedAccessGroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-verifiedaccessgroupid""", alias="VerifiedAccessGroupId")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-securitygroupids""", alias="SecurityGroupIds")
    LoadBalancerOptions_: Optional['LoadBalancerOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions""", alias="LoadBalancerOptions")
    ApplicationDomain_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-applicationdomain""", alias="ApplicationDomain")
    PolicyEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-policyenabled""", alias="PolicyEnabled")
    EndpointDomainPrefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-endpointdomainprefix""", alias="EndpointDomainPrefix")
    EndpointType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-endpointtype""", alias="EndpointType")
    PolicyDocument_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-policydocument""", alias="PolicyDocument")
    SseSpecification_: Optional['SseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-ssespecification""", alias="SseSpecification")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-tags""", alias="Tags")
    NetworkInterfaceOptions_: Optional['NetworkInterfaceOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html#cfn-ec2-verifiedaccessendpoint-networkinterfaceoptions""", alias="NetworkInterfaceOptions")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VerifiedAccessEndpoint:
        from troposphere.ec2 import VerifiedAccessEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VerifiedAccessEndpoint as TropoT
        return resource_to_troposphere(self, TropoT)


class VerifiedAccessGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessgroup.html
    Properties:
        - Name: Description
        - Name: PolicyDocument
        - Name: SseSpecification
        - Name: VerifiedAccessInstanceId
        - Name: Tags
        - Name: PolicyEnabled
    Attributes:
        - Name: Owner
        - Name: CreationTime
        - Name: LastUpdatedTime
        - Name: VerifiedAccessGroupId
        - Name: VerifiedAccessGroupArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessgroup.html#cfn-ec2-verifiedaccessgroup-description""", alias="Description")
    PolicyDocument_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessgroup.html#cfn-ec2-verifiedaccessgroup-policydocument""", alias="PolicyDocument")
    SseSpecification_: Optional['SseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessgroup.html#cfn-ec2-verifiedaccessgroup-ssespecification""", alias="SseSpecification")
    VerifiedAccessInstanceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessgroup.html#cfn-ec2-verifiedaccessgroup-verifiedaccessinstanceid""", alias="VerifiedAccessInstanceId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessgroup.html#cfn-ec2-verifiedaccessgroup-tags""", alias="Tags")
    PolicyEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessgroup.html#cfn-ec2-verifiedaccessgroup-policyenabled""", alias="PolicyEnabled")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VerifiedAccessGroup:
        from troposphere.ec2 import VerifiedAccessGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VerifiedAccessGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class VerifiedAccessInstance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessinstance.html
    Properties:
        - Name: VerifiedAccessTrustProviders
        - Name: Description
        - Name: FipsEnabled
        - Name: LoggingConfigurations
        - Name: VerifiedAccessTrustProviderIds
        - Name: Tags
    Attributes:
        - Name: CreationTime
        - Name: LastUpdatedTime
        - Name: VerifiedAccessInstanceId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VerifiedAccessTrustProviders_: Optional[List['VerifiedAccessTrustProvider']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessinstance.html#cfn-ec2-verifiedaccessinstance-verifiedaccesstrustproviders""", alias="VerifiedAccessTrustProviders")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessinstance.html#cfn-ec2-verifiedaccessinstance-description""", alias="Description")
    FipsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessinstance.html#cfn-ec2-verifiedaccessinstance-fipsenabled""", alias="FipsEnabled")
    LoggingConfigurations_: Optional['VerifiedAccessLogs'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessinstance.html#cfn-ec2-verifiedaccessinstance-loggingconfigurations""", alias="LoggingConfigurations")
    VerifiedAccessTrustProviderIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessinstance.html#cfn-ec2-verifiedaccessinstance-verifiedaccesstrustproviderids""", alias="VerifiedAccessTrustProviderIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessinstance.html#cfn-ec2-verifiedaccessinstance-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VerifiedAccessInstance:
        from troposphere.ec2 import VerifiedAccessInstance as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VerifiedAccessInstance as TropoT
        return resource_to_troposphere(self, TropoT)


class VerifiedAccessTrustProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccesstrustprovider.html
    Properties:
        - Name: PolicyReferenceName
        - Name: DeviceOptions
        - Name: DeviceTrustProviderType
        - Name: Description
        - Name: OidcOptions
        - Name: TrustProviderType
        - Name: SseSpecification
        - Name: UserTrustProviderType
        - Name: Tags
    Attributes:
        - Name: VerifiedAccessTrustProviderId
        - Name: CreationTime
        - Name: LastUpdatedTime
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PolicyReferenceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccesstrustprovider-policyreferencename""", alias="PolicyReferenceName")
    DeviceOptions_: Optional['DeviceOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccesstrustprovider-deviceoptions""", alias="DeviceOptions")
    DeviceTrustProviderType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccesstrustprovider-devicetrustprovidertype""", alias="DeviceTrustProviderType")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccesstrustprovider-description""", alias="Description")
    OidcOptions_: Optional['OidcOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccesstrustprovider-oidcoptions""", alias="OidcOptions")
    TrustProviderType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccesstrustprovider-trustprovidertype""", alias="TrustProviderType")
    SseSpecification_: Optional['SseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccesstrustprovider-ssespecification""", alias="SseSpecification")
    UserTrustProviderType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccesstrustprovider-usertrustprovidertype""", alias="UserTrustProviderType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccesstrustprovider.html#cfn-ec2-verifiedaccesstrustprovider-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VerifiedAccessTrustProvider:
        from troposphere.ec2 import VerifiedAccessTrustProvider as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VerifiedAccessTrustProvider as TropoT
        return resource_to_troposphere(self, TropoT)


class Volume(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html
    Properties:
        - Name: MultiAttachEnabled
        - Name: SnapshotId
        - Name: VolumeType
        - Name: KmsKeyId
        - Name: Encrypted
        - Name: Size
        - Name: AutoEnableIO
        - Name: OutpostArn
        - Name: AvailabilityZone
        - Name: Throughput
        - Name: Iops
        - Name: Tags
    Attributes:
        - Name: VolumeId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MultiAttachEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-multiattachenabled""", alias="MultiAttachEnabled")
    SnapshotId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-snapshotid""", alias="SnapshotId")
    VolumeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-volumetype""", alias="VolumeType")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-kmskeyid""", alias="KmsKeyId")
    Encrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-encrypted""", alias="Encrypted")
    Size_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-size""", alias="Size")
    AutoEnableIO_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-autoenableio""", alias="AutoEnableIO")
    OutpostArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-outpostarn""", alias="OutpostArn")
    AvailabilityZone_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-availabilityzone""", alias="AvailabilityZone")
    Throughput_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-throughput""", alias="Throughput")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-iops""", alias="Iops")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volume.html#cfn-ec2-volume-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ec2.Volume:
        from troposphere.ec2 import Volume as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import Volume as TropoT
        return resource_to_troposphere(self, TropoT)


class VolumeAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volumeattachment.html
    Properties:
        - Name: VolumeId
        - Name: InstanceId
        - Name: Device
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VolumeId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volumeattachment.html#cfn-ec2-volumeattachment-volumeid""", alias="VolumeId")
    InstanceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volumeattachment.html#cfn-ec2-volumeattachment-instanceid""", alias="InstanceId")
    Device_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volumeattachment.html#cfn-ec2-volumeattachment-device""", alias="Device")
    

    @property
    def tropo_type(self) -> troposphere.ec2.VolumeAttachment:
        from troposphere.ec2 import VolumeAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ec2 import VolumeAttachment as TropoT
        return resource_to_troposphere(self, TropoT)

