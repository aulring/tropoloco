from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DeliveryOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-deliveryoptions.html
    Properties:
        - Name: SendingPoolName
    
    """
    
    SendingPoolName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-deliveryoptions.html#cfn-pinpointemail-configurationset-deliveryoptions-sendingpoolname""", alias="SendingPoolName")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.DeliveryOptions:
        from troposphere.pinpointemail import DeliveryOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReputationOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-reputationoptions.html
    Properties:
        - Name: ReputationMetricsEnabled
    
    """
    
    ReputationMetricsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-reputationoptions.html#cfn-pinpointemail-configurationset-reputationoptions-reputationmetricsenabled""", alias="ReputationMetricsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.ReputationOptions:
        from troposphere.pinpointemail import ReputationOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SendingOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-sendingoptions.html
    Properties:
        - Name: SendingEnabled
    
    """
    
    SendingEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-sendingoptions.html#cfn-pinpointemail-configurationset-sendingoptions-sendingenabled""", alias="SendingEnabled")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.SendingOptions:
        from troposphere.pinpointemail import SendingOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tags(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-tags.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-tags.html#cfn-pinpointemail-configurationset-tags-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-tags.html#cfn-pinpointemail-configurationset-tags-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.Tags:
        from troposphere.pinpointemail import Tags as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrackingOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-trackingoptions.html
    Properties:
        - Name: CustomRedirectDomain
    
    """
    
    CustomRedirectDomain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-trackingoptions.html#cfn-pinpointemail-configurationset-trackingoptions-customredirectdomain""", alias="CustomRedirectDomain")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.TrackingOptions:
        from troposphere.pinpointemail import TrackingOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination.html
    Properties:
        - Name: DimensionConfigurations
    
    """
    
    DimensionConfigurations_: Optional[List['DimensionConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination.html#cfn-pinpointemail-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations""", alias="DimensionConfigurations")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.CloudWatchDestination:
        from troposphere.pinpointemail import CloudWatchDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DimensionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html
    Properties:
        - Name: DimensionValueSource
        - Name: DefaultDimensionValue
        - Name: DimensionName
    
    """
    
    DimensionValueSource_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource""", alias="DimensionValueSource")
    DefaultDimensionValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue""", alias="DefaultDimensionValue")
    DimensionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionname""", alias="DimensionName")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.DimensionConfiguration:
        from troposphere.pinpointemail import DimensionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EventDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html
    Properties:
        - Name: SnsDestination
        - Name: CloudWatchDestination
        - Name: Enabled
        - Name: MatchingEventTypes
        - Name: PinpointDestination
        - Name: KinesisFirehoseDestination
    
    """
    
    SnsDestination_: Optional['SnsDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-snsdestination""", alias="SnsDestination")
    CloudWatchDestination_: Optional['CloudWatchDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-cloudwatchdestination""", alias="CloudWatchDestination")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-enabled""", alias="Enabled")
    MatchingEventTypes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-matchingeventtypes""", alias="MatchingEventTypes")
    PinpointDestination_: Optional['PinpointDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-pinpointdestination""", alias="PinpointDestination")
    KinesisFirehoseDestination_: Optional['KinesisFirehoseDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-kinesisfirehosedestination""", alias="KinesisFirehoseDestination")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.EventDestination:
        from troposphere.pinpointemail import EventDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisFirehoseDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html
    Properties:
        - Name: DeliveryStreamArn
        - Name: IamRoleArn
    
    """
    
    DeliveryStreamArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html#cfn-pinpointemail-configurationseteventdestination-kinesisfirehosedestination-deliverystreamarn""", alias="DeliveryStreamArn")
    IamRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html#cfn-pinpointemail-configurationseteventdestination-kinesisfirehosedestination-iamrolearn""", alias="IamRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.KinesisFirehoseDestination:
        from troposphere.pinpointemail import KinesisFirehoseDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PinpointDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination.html
    Properties:
        - Name: ApplicationArn
    
    """
    
    ApplicationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination.html#cfn-pinpointemail-configurationseteventdestination-pinpointdestination-applicationarn""", alias="ApplicationArn")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.PinpointDestination:
        from troposphere.pinpointemail import PinpointDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnsDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-snsdestination.html
    Properties:
        - Name: TopicArn
    
    """
    
    TopicArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-snsdestination.html#cfn-pinpointemail-configurationseteventdestination-snsdestination-topicarn""", alias="TopicArn")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.SnsDestination:
        from troposphere.pinpointemail import SnsDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tags(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html#cfn-pinpointemail-dedicatedippool-tags-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html#cfn-pinpointemail-dedicatedippool-tags-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.Tags:
        from troposphere.pinpointemail import Tags as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MailFromAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html
    Properties:
        - Name: MailFromDomain
        - Name: BehaviorOnMxFailure
    
    """
    
    MailFromDomain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html#cfn-pinpointemail-identity-mailfromattributes-mailfromdomain""", alias="MailFromDomain")
    BehaviorOnMxFailure_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html#cfn-pinpointemail-identity-mailfromattributes-behavioronmxfailure""", alias="BehaviorOnMxFailure")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.MailFromAttributes:
        from troposphere.pinpointemail import MailFromAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tags(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-tags.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-tags.html#cfn-pinpointemail-identity-tags-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-tags.html#cfn-pinpointemail-identity-tags-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.pinpointemail.Tags:
        from troposphere.pinpointemail import Tags as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ConfigurationSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html
    Properties:
        - Name: SendingOptions
        - Name: TrackingOptions
        - Name: ReputationOptions
        - Name: DeliveryOptions
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SendingOptions_: Optional['SendingOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-sendingoptions""", alias="SendingOptions")
    TrackingOptions_: Optional['TrackingOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-trackingoptions""", alias="TrackingOptions")
    ReputationOptions_: Optional['ReputationOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-reputationoptions""", alias="ReputationOptions")
    DeliveryOptions_: Optional['DeliveryOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-deliveryoptions""", alias="DeliveryOptions")
    Tags_: Optional[List['Tags']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.pinpointemail.ConfigurationSet:
        from troposphere.pinpointemail import ConfigurationSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpointemail import ConfigurationSet as TropoT
        return resource_to_troposphere(self, TropoT)


class ConfigurationSetEventDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html
    Properties:
        - Name: EventDestinationName
        - Name: ConfigurationSetName
        - Name: EventDestination
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EventDestinationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestinationname""", alias="EventDestinationName")
    ConfigurationSetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-configurationsetname""", alias="ConfigurationSetName")
    EventDestination_: Optional['EventDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination""", alias="EventDestination")
    

    @property
    def tropo_type(self) -> troposphere.pinpointemail.ConfigurationSetEventDestination:
        from troposphere.pinpointemail import ConfigurationSetEventDestination as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpointemail import ConfigurationSetEventDestination as TropoT
        return resource_to_troposphere(self, TropoT)


class DedicatedIpPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html
    Properties:
        - Name: PoolName
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PoolName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html#cfn-pinpointemail-dedicatedippool-poolname""", alias="PoolName")
    Tags_: Optional[List['Tags']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html#cfn-pinpointemail-dedicatedippool-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.pinpointemail.DedicatedIpPool:
        from troposphere.pinpointemail import DedicatedIpPool as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpointemail import DedicatedIpPool as TropoT
        return resource_to_troposphere(self, TropoT)


class Identity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html
    Properties:
        - Name: FeedbackForwardingEnabled
        - Name: DkimSigningEnabled
        - Name: Tags
        - Name: Name
        - Name: MailFromAttributes
    Attributes:
        - Name: IdentityDNSRecordName3
        - Name: IdentityDNSRecordName1
        - Name: IdentityDNSRecordName2
        - Name: IdentityDNSRecordValue3
        - Name: IdentityDNSRecordValue2
        - Name: IdentityDNSRecordValue1
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FeedbackForwardingEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-feedbackforwardingenabled""", alias="FeedbackForwardingEnabled")
    DkimSigningEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-dkimsigningenabled""", alias="DkimSigningEnabled")
    Tags_: Optional[List['Tags']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-name""", alias="Name")
    MailFromAttributes_: Optional['MailFromAttributes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-mailfromattributes""", alias="MailFromAttributes")
    

    @property
    def tropo_type(self) -> troposphere.pinpointemail.Identity:
        from troposphere.pinpointemail import Identity as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpointemail import Identity as TropoT
        return resource_to_troposphere(self, TropoT)

