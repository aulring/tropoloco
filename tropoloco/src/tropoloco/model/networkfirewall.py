from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class SubnetMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html
    Properties:
        - Name: IPAddressType
        - Name: SubnetId
    
    """
    
    IPAddressType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html#cfn-networkfirewall-firewall-subnetmapping-ipaddresstype""", alias="IPAddressType")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html#cfn-networkfirewall-firewall-subnetmapping-subnetid""", alias="SubnetId")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.SubnetMapping:
        from troposphere.networkfirewall import SubnetMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ActionDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-actiondefinition.html
    Properties:
        - Name: PublishMetricAction
    
    """
    
    PublishMetricAction_: Optional['PublishMetricAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-actiondefinition.html#cfn-networkfirewall-firewallpolicy-actiondefinition-publishmetricaction""", alias="PublishMetricAction")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.ActionDefinition:
        from troposphere.networkfirewall import ActionDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html
    Properties:
        - Name: ActionName
        - Name: ActionDefinition
    
    """
    
    ActionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html#cfn-networkfirewall-firewallpolicy-customaction-actionname""", alias="ActionName")
    ActionDefinition_: 'ActionDefinition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html#cfn-networkfirewall-firewallpolicy-customaction-actiondefinition""", alias="ActionDefinition")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.CustomAction:
        from troposphere.networkfirewall import CustomAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Dimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimension.html
    Properties:
        - Name: Value
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimension.html#cfn-networkfirewall-firewallpolicy-dimension-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.Dimension:
        from troposphere.networkfirewall import Dimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FirewallPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html
    Properties:
        - Name: StatelessRuleGroupReferences
        - Name: StatefulRuleGroupReferences
        - Name: StatelessDefaultActions
        - Name: StatefulEngineOptions
        - Name: StatelessCustomActions
        - Name: StatelessFragmentDefaultActions
        - Name: PolicyVariables
        - Name: StatefulDefaultActions
    
    """
    
    StatelessRuleGroupReferences_: Optional[List['StatelessRuleGroupReference']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessrulegroupreferences""", alias="StatelessRuleGroupReferences")
    StatefulRuleGroupReferences_: Optional[List['StatefulRuleGroupReference']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulrulegroupreferences""", alias="StatefulRuleGroupReferences")
    StatelessDefaultActions_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessdefaultactions""", alias="StatelessDefaultActions")
    StatefulEngineOptions_: Optional['StatefulEngineOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulengineoptions""", alias="StatefulEngineOptions")
    StatelessCustomActions_: Optional[List['CustomAction']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelesscustomactions""", alias="StatelessCustomActions")
    StatelessFragmentDefaultActions_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessfragmentdefaultactions""", alias="StatelessFragmentDefaultActions")
    PolicyVariables_: Optional['PolicyVariables'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-policyvariables""", alias="PolicyVariables")
    StatefulDefaultActions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefuldefaultactions""", alias="StatefulDefaultActions")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.FirewallPolicy:
        from troposphere.networkfirewall import FirewallPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IPSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-ipset.html
    Properties:
        - Name: Definition
    
    """
    
    Definition_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-ipset.html#cfn-networkfirewall-firewallpolicy-ipset-definition""", alias="Definition")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.IPSet:
        from troposphere.networkfirewall import IPSet as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PolicyVariables(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-policyvariables.html
    Properties:
        - Name: RuleVariables
    
    """
    
    RuleVariables_: Optional[Dict[str, 'IPSet']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-policyvariables.html#cfn-networkfirewall-firewallpolicy-policyvariables-rulevariables""", alias="RuleVariables")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.PolicyVariables:
        from troposphere.networkfirewall import PolicyVariables as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PublishMetricAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html
    Properties:
        - Name: Dimensions
    
    """
    
    Dimensions_: List['Dimension'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html#cfn-networkfirewall-firewallpolicy-publishmetricaction-dimensions""", alias="Dimensions")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.PublishMetricAction:
        from troposphere.networkfirewall import PublishMetricAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatefulEngineOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html
    Properties:
        - Name: StreamExceptionPolicy
        - Name: RuleOrder
    
    """
    
    StreamExceptionPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html#cfn-networkfirewall-firewallpolicy-statefulengineoptions-streamexceptionpolicy""", alias="StreamExceptionPolicy")
    RuleOrder_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html#cfn-networkfirewall-firewallpolicy-statefulengineoptions-ruleorder""", alias="RuleOrder")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.StatefulEngineOptions:
        from troposphere.networkfirewall import StatefulEngineOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatefulRuleGroupOverride(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride.html
    Properties:
        - Name: Action
    
    """
    
    Action_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupoverride-action""", alias="Action")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.StatefulRuleGroupOverride:
        from troposphere.networkfirewall import StatefulRuleGroupOverride as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatefulRuleGroupReference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html
    Properties:
        - Name: ResourceArn
        - Name: Priority
        - Name: Override
    
    """
    
    ResourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupreference-resourcearn""", alias="ResourceArn")
    Priority_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupreference-priority""", alias="Priority")
    Override_: Optional['StatefulRuleGroupOverride'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupreference-override""", alias="Override")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.StatefulRuleGroupReference:
        from troposphere.networkfirewall import StatefulRuleGroupReference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatelessRuleGroupReference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html
    Properties:
        - Name: ResourceArn
        - Name: Priority
    
    """
    
    ResourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statelessrulegroupreference-resourcearn""", alias="ResourceArn")
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statelessrulegroupreference-priority""", alias="Priority")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.StatelessRuleGroupReference:
        from troposphere.networkfirewall import StatelessRuleGroupReference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogDestinationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html
    Properties:
        - Name: LogType
        - Name: LogDestination
        - Name: LogDestinationType
    
    """
    
    LogType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logtype""", alias="LogType")
    LogDestination_: Dict[str, str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestination""", alias="LogDestination")
    LogDestinationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestinationtype""", alias="LogDestinationType")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.LogDestinationConfig:
        from troposphere.networkfirewall import LogDestinationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html
    Properties:
        - Name: LogDestinationConfigs
    
    """
    
    LogDestinationConfigs_: List['LogDestinationConfig'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-loggingconfiguration-logdestinationconfigs""", alias="LogDestinationConfigs")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.LoggingConfiguration:
        from troposphere.networkfirewall import LoggingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ActionDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html
    Properties:
        - Name: PublishMetricAction
    
    """
    
    PublishMetricAction_: Optional['PublishMetricAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html#cfn-networkfirewall-rulegroup-actiondefinition-publishmetricaction""", alias="PublishMetricAction")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.ActionDefinition:
        from troposphere.networkfirewall import ActionDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Address(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-address.html
    Properties:
        - Name: AddressDefinition
    
    """
    
    AddressDefinition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-address.html#cfn-networkfirewall-rulegroup-address-addressdefinition""", alias="AddressDefinition")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.Address:
        from troposphere.networkfirewall import Address as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html
    Properties:
        - Name: ActionName
        - Name: ActionDefinition
    
    """
    
    ActionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html#cfn-networkfirewall-rulegroup-customaction-actionname""", alias="ActionName")
    ActionDefinition_: 'ActionDefinition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html#cfn-networkfirewall-rulegroup-customaction-actiondefinition""", alias="ActionDefinition")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.CustomAction:
        from troposphere.networkfirewall import CustomAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Dimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html
    Properties:
        - Name: Value
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html#cfn-networkfirewall-rulegroup-dimension-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.Dimension:
        from troposphere.networkfirewall import Dimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Header(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html
    Properties:
        - Name: Destination
        - Name: Protocol
        - Name: SourcePort
        - Name: Direction
        - Name: DestinationPort
        - Name: Source
    
    """
    
    Destination_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-destination""", alias="Destination")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-protocol""", alias="Protocol")
    SourcePort_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-sourceport""", alias="SourcePort")
    Direction_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-direction""", alias="Direction")
    DestinationPort_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-destinationport""", alias="DestinationPort")
    Source_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-source""", alias="Source")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.Header:
        from troposphere.networkfirewall import Header as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IPSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html
    Properties:
        - Name: Definition
    
    """
    
    Definition_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html#cfn-networkfirewall-rulegroup-ipset-definition""", alias="Definition")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.IPSet:
        from troposphere.networkfirewall import IPSet as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IPSetReference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipsetreference.html
    Properties:
        - Name: ReferenceArn
    
    """
    
    ReferenceArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipsetreference.html#cfn-networkfirewall-rulegroup-ipsetreference-referencearn""", alias="ReferenceArn")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.IPSetReference:
        from troposphere.networkfirewall import IPSetReference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MatchAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html
    Properties:
        - Name: Protocols
        - Name: TCPFlags
        - Name: DestinationPorts
        - Name: Destinations
        - Name: Sources
        - Name: SourcePorts
    
    """
    
    Protocols_: Optional[List[int]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-protocols""", alias="Protocols")
    TCPFlags_: Optional[List['TCPFlagField']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-tcpflags""", alias="TCPFlags")
    DestinationPorts_: Optional[List['PortRange']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-destinationports""", alias="DestinationPorts")
    Destinations_: Optional[List['Address']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-destinations""", alias="Destinations")
    Sources_: Optional[List['Address']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-sources""", alias="Sources")
    SourcePorts_: Optional[List['PortRange']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-sourceports""", alias="SourcePorts")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.MatchAttributes:
        from troposphere.networkfirewall import MatchAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PortRange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html
    Properties:
        - Name: FromPort
        - Name: ToPort
    
    """
    
    FromPort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html#cfn-networkfirewall-rulegroup-portrange-fromport""", alias="FromPort")
    ToPort_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html#cfn-networkfirewall-rulegroup-portrange-toport""", alias="ToPort")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.PortRange:
        from troposphere.networkfirewall import PortRange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PortSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html
    Properties:
        - Name: Definition
    
    """
    
    Definition_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html#cfn-networkfirewall-rulegroup-portset-definition""", alias="Definition")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.PortSet:
        from troposphere.networkfirewall import PortSet as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PublishMetricAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html
    Properties:
        - Name: Dimensions
    
    """
    
    Dimensions_: List['Dimension'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html#cfn-networkfirewall-rulegroup-publishmetricaction-dimensions""", alias="Dimensions")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.PublishMetricAction:
        from troposphere.networkfirewall import PublishMetricAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReferenceSets(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-referencesets.html
    Properties:
        - Name: IPSetReferences
    
    """
    
    IPSetReferences_: Optional[Dict[str, 'IPSetReference']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-referencesets.html#cfn-networkfirewall-rulegroup-referencesets-ipsetreferences""", alias="IPSetReferences")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.ReferenceSets:
        from troposphere.networkfirewall import ReferenceSets as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html
    Properties:
        - Name: Actions
        - Name: MatchAttributes
    
    """
    
    Actions_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html#cfn-networkfirewall-rulegroup-ruledefinition-actions""", alias="Actions")
    MatchAttributes_: 'MatchAttributes' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html#cfn-networkfirewall-rulegroup-ruledefinition-matchattributes""", alias="MatchAttributes")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.RuleDefinition:
        from troposphere.networkfirewall import RuleDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleGroupProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html
    Properties:
        - Name: StatefulRuleOptions
        - Name: ReferenceSets
        - Name: RulesSource
        - Name: RuleVariables
    
    """
    
    StatefulRuleOptions_: Optional['StatefulRuleOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-statefulruleoptions""", alias="StatefulRuleOptions")
    ReferenceSets_: Optional['ReferenceSets'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-referencesets""", alias="ReferenceSets")
    RulesSource_: 'RulesSource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-rulessource""", alias="RulesSource")
    RuleVariables_: Optional['RuleVariables'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-rulevariables""", alias="RuleVariables")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.RuleGroupProperty:
        from troposphere.networkfirewall import RuleGroupProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html
    Properties:
        - Name: Keyword
        - Name: Settings
    
    """
    
    Keyword_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html#cfn-networkfirewall-rulegroup-ruleoption-keyword""", alias="Keyword")
    Settings_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html#cfn-networkfirewall-rulegroup-ruleoption-settings""", alias="Settings")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.RuleOption:
        from troposphere.networkfirewall import RuleOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleVariables(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html
    Properties:
        - Name: PortSets
        - Name: IPSets
    
    """
    
    PortSets_: Optional[Dict[str, 'PortSet']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html#cfn-networkfirewall-rulegroup-rulevariables-portsets""", alias="PortSets")
    IPSets_: Optional[Dict[str, 'IPSet']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html#cfn-networkfirewall-rulegroup-rulevariables-ipsets""", alias="IPSets")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.RuleVariables:
        from troposphere.networkfirewall import RuleVariables as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RulesSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html
    Properties:
        - Name: StatelessRulesAndCustomActions
        - Name: StatefulRules
        - Name: RulesString
        - Name: RulesSourceList
    
    """
    
    StatelessRulesAndCustomActions_: Optional['StatelessRulesAndCustomActions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-statelessrulesandcustomactions""", alias="StatelessRulesAndCustomActions")
    StatefulRules_: Optional[List['StatefulRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-statefulrules""", alias="StatefulRules")
    RulesString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-rulesstring""", alias="RulesString")
    RulesSourceList_: Optional['RulesSourceList'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-rulessourcelist""", alias="RulesSourceList")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.RulesSource:
        from troposphere.networkfirewall import RulesSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RulesSourceList(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html
    Properties:
        - Name: GeneratedRulesType
        - Name: TargetTypes
        - Name: Targets
    
    """
    
    GeneratedRulesType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-generatedrulestype""", alias="GeneratedRulesType")
    TargetTypes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-targettypes""", alias="TargetTypes")
    Targets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-targets""", alias="Targets")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.RulesSourceList:
        from troposphere.networkfirewall import RulesSourceList as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatefulRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html
    Properties:
        - Name: Action
        - Name: Header
        - Name: RuleOptions
    
    """
    
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-action""", alias="Action")
    Header_: 'Header' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-header""", alias="Header")
    RuleOptions_: List['RuleOption'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-ruleoptions""", alias="RuleOptions")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.StatefulRule:
        from troposphere.networkfirewall import StatefulRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatefulRuleOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulruleoptions.html
    Properties:
        - Name: RuleOrder
    
    """
    
    RuleOrder_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulruleoptions.html#cfn-networkfirewall-rulegroup-statefulruleoptions-ruleorder""", alias="RuleOrder")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.StatefulRuleOptions:
        from troposphere.networkfirewall import StatefulRuleOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatelessRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html
    Properties:
        - Name: Priority
        - Name: RuleDefinition
    
    """
    
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html#cfn-networkfirewall-rulegroup-statelessrule-priority""", alias="Priority")
    RuleDefinition_: 'RuleDefinition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html#cfn-networkfirewall-rulegroup-statelessrule-ruledefinition""", alias="RuleDefinition")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.StatelessRule:
        from troposphere.networkfirewall import StatelessRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StatelessRulesAndCustomActions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html
    Properties:
        - Name: StatelessRules
        - Name: CustomActions
    
    """
    
    StatelessRules_: List['StatelessRule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-statelessrules""", alias="StatelessRules")
    CustomActions_: Optional[List['CustomAction']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-customactions""", alias="CustomActions")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.StatelessRulesAndCustomActions:
        from troposphere.networkfirewall import StatelessRulesAndCustomActions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TCPFlagField(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html
    Properties:
        - Name: Flags
        - Name: Masks
    
    """
    
    Flags_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html#cfn-networkfirewall-rulegroup-tcpflagfield-flags""", alias="Flags")
    Masks_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html#cfn-networkfirewall-rulegroup-tcpflagfield-masks""", alias="Masks")
    


    @property
    def tropo_type(self) -> troposphere.networkfirewall.TCPFlagField:
        from troposphere.networkfirewall import TCPFlagField as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Firewall(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html
    Properties:
        - Name: FirewallPolicyArn
        - Name: SubnetChangeProtection
        - Name: Description
        - Name: FirewallName
        - Name: VpcId
        - Name: DeleteProtection
        - Name: FirewallPolicyChangeProtection
        - Name: Tags
        - Name: SubnetMappings
    Attributes:
        - Name: FirewallArn
        - Name: EndpointIds
        - Name: FirewallId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FirewallPolicyArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicyarn""", alias="FirewallPolicyArn")
    SubnetChangeProtection_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetchangeprotection""", alias="SubnetChangeProtection")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-description""", alias="Description")
    FirewallName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallname""", alias="FirewallName")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-vpcid""", alias="VpcId")
    DeleteProtection_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-deleteprotection""", alias="DeleteProtection")
    FirewallPolicyChangeProtection_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicychangeprotection""", alias="FirewallPolicyChangeProtection")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-tags""", alias="Tags")
    SubnetMappings_: List['SubnetMapping'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetmappings""", alias="SubnetMappings")
    

    @property
    def tropo_type(self) -> troposphere.networkfirewall.Firewall:
        from troposphere.networkfirewall import Firewall as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkfirewall import Firewall as TropoT
        return resource_to_troposphere(self, TropoT)


class FirewallPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html
    Properties:
        - Name: Description
        - Name: FirewallPolicyName
        - Name: Tags
        - Name: FirewallPolicy
    Attributes:
        - Name: FirewallPolicyArn
        - Name: FirewallPolicyId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-description""", alias="Description")
    FirewallPolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicyname""", alias="FirewallPolicyName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-tags""", alias="Tags")
    FirewallPolicy_: 'FirewallPolicy' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy""", alias="FirewallPolicy")
    

    @property
    def tropo_type(self) -> troposphere.networkfirewall.FirewallPolicy:
        from troposphere.networkfirewall import FirewallPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkfirewall import FirewallPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class LoggingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html
    Properties:
        - Name: FirewallName
        - Name: FirewallArn
        - Name: LoggingConfiguration
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FirewallName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-firewallname""", alias="FirewallName")
    FirewallArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-firewallarn""", alias="FirewallArn")
    LoggingConfiguration_: 'LoggingConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-loggingconfiguration""", alias="LoggingConfiguration")
    

    @property
    def tropo_type(self) -> troposphere.networkfirewall.LoggingConfiguration:
        from troposphere.networkfirewall import LoggingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkfirewall import LoggingConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class RuleGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: Capacity
        - Name: RuleGroupName
        - Name: RuleGroup
        - Name: Tags
    Attributes:
        - Name: RuleGroupId
        - Name: RuleGroupArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-description""", alias="Description")
    Capacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-capacity""", alias="Capacity")
    RuleGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroupname""", alias="RuleGroupName")
    RuleGroup_: Optional['RuleGroup'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup""", alias="RuleGroup")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.networkfirewall.RuleGroup:
        from troposphere.networkfirewall import RuleGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.networkfirewall import RuleGroup as TropoT
        return resource_to_troposphere(self, TropoT)

