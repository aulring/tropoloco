from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DashboardOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-dashboardoptions.html
    Properties:
        - Name: EngagementMetrics
    
    """
    
    EngagementMetrics_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-dashboardoptions.html#cfn-ses-configurationset-dashboardoptions-engagementmetrics""", alias="EngagementMetrics")
    


    @property
    def tropo_type(self) -> troposphere.ses.DashboardOptions:
        from troposphere.ses import DashboardOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeliveryOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html
    Properties:
        - Name: SendingPoolName
        - Name: TlsPolicy
    
    """
    
    SendingPoolName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html#cfn-ses-configurationset-deliveryoptions-sendingpoolname""", alias="SendingPoolName")
    TlsPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html#cfn-ses-configurationset-deliveryoptions-tlspolicy""", alias="TlsPolicy")
    


    @property
    def tropo_type(self) -> troposphere.ses.DeliveryOptions:
        from troposphere.ses import DeliveryOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GuardianOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-guardianoptions.html
    Properties:
        - Name: OptimizedSharedDelivery
    
    """
    
    OptimizedSharedDelivery_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-guardianoptions.html#cfn-ses-configurationset-guardianoptions-optimizedshareddelivery""", alias="OptimizedSharedDelivery")
    


    @property
    def tropo_type(self) -> troposphere.ses.GuardianOptions:
        from troposphere.ses import GuardianOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReputationOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-reputationoptions.html
    Properties:
        - Name: ReputationMetricsEnabled
    
    """
    
    ReputationMetricsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-reputationoptions.html#cfn-ses-configurationset-reputationoptions-reputationmetricsenabled""", alias="ReputationMetricsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.ses.ReputationOptions:
        from troposphere.ses import ReputationOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SendingOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-sendingoptions.html
    Properties:
        - Name: SendingEnabled
    
    """
    
    SendingEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-sendingoptions.html#cfn-ses-configurationset-sendingoptions-sendingenabled""", alias="SendingEnabled")
    


    @property
    def tropo_type(self) -> troposphere.ses.SendingOptions:
        from troposphere.ses import SendingOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SuppressionOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-suppressionoptions.html
    Properties:
        - Name: SuppressedReasons
    
    """
    
    SuppressedReasons_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-suppressionoptions.html#cfn-ses-configurationset-suppressionoptions-suppressedreasons""", alias="SuppressedReasons")
    


    @property
    def tropo_type(self) -> troposphere.ses.SuppressionOptions:
        from troposphere.ses import SuppressionOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrackingOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-trackingoptions.html
    Properties:
        - Name: CustomRedirectDomain
    
    """
    
    CustomRedirectDomain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-trackingoptions.html#cfn-ses-configurationset-trackingoptions-customredirectdomain""", alias="CustomRedirectDomain")
    


    @property
    def tropo_type(self) -> troposphere.ses.TrackingOptions:
        from troposphere.ses import TrackingOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VdmOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-vdmoptions.html
    Properties:
        - Name: DashboardOptions
        - Name: GuardianOptions
    
    """
    
    DashboardOptions_: Optional['DashboardOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-vdmoptions.html#cfn-ses-configurationset-vdmoptions-dashboardoptions""", alias="DashboardOptions")
    GuardianOptions_: Optional['GuardianOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-vdmoptions.html#cfn-ses-configurationset-vdmoptions-guardianoptions""", alias="GuardianOptions")
    


    @property
    def tropo_type(self) -> troposphere.ses.VdmOptions:
        from troposphere.ses import VdmOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html
    Properties:
        - Name: DimensionConfigurations
    
    """
    
    DimensionConfigurations_: Optional[List['DimensionConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html#cfn-ses-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations""", alias="DimensionConfigurations")
    


    @property
    def tropo_type(self) -> troposphere.ses.CloudWatchDestination:
        from troposphere.ses import CloudWatchDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DimensionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html
    Properties:
        - Name: DimensionValueSource
        - Name: DefaultDimensionValue
        - Name: DimensionName
    
    """
    
    DimensionValueSource_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource""", alias="DimensionValueSource")
    DefaultDimensionValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue""", alias="DefaultDimensionValue")
    DimensionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionname""", alias="DimensionName")
    


    @property
    def tropo_type(self) -> troposphere.ses.DimensionConfiguration:
        from troposphere.ses import DimensionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EventDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html
    Properties:
        - Name: SnsDestination
        - Name: CloudWatchDestination
        - Name: Enabled
        - Name: MatchingEventTypes
        - Name: Name
        - Name: KinesisFirehoseDestination
    
    """
    
    SnsDestination_: Optional['SnsDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-snsdestination""", alias="SnsDestination")
    CloudWatchDestination_: Optional['CloudWatchDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-cloudwatchdestination""", alias="CloudWatchDestination")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-enabled""", alias="Enabled")
    MatchingEventTypes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-matchingeventtypes""", alias="MatchingEventTypes")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-name""", alias="Name")
    KinesisFirehoseDestination_: Optional['KinesisFirehoseDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-kinesisfirehosedestination""", alias="KinesisFirehoseDestination")
    


    @property
    def tropo_type(self) -> troposphere.ses.EventDestination:
        from troposphere.ses import EventDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisFirehoseDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html
    Properties:
        - Name: IAMRoleARN
        - Name: DeliveryStreamARN
    
    """
    
    IAMRoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-iamrolearn""", alias="IAMRoleARN")
    DeliveryStreamARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-deliverystreamarn""", alias="DeliveryStreamARN")
    


    @property
    def tropo_type(self) -> troposphere.ses.KinesisFirehoseDestination:
        from troposphere.ses import KinesisFirehoseDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnsDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-snsdestination.html
    Properties:
        - Name: TopicARN
    
    """
    
    TopicARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-snsdestination.html#cfn-ses-configurationseteventdestination-snsdestination-topicarn""", alias="TopicARN")
    


    @property
    def tropo_type(self) -> troposphere.ses.SnsDestination:
        from troposphere.ses import SnsDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Topic(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html
    Properties:
        - Name: Description
        - Name: DisplayName
        - Name: DefaultSubscriptionStatus
        - Name: TopicName
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-description""", alias="Description")
    DisplayName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-displayname""", alias="DisplayName")
    DefaultSubscriptionStatus_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-defaultsubscriptionstatus""", alias="DefaultSubscriptionStatus")
    TopicName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-topicname""", alias="TopicName")
    


    @property
    def tropo_type(self) -> troposphere.ses.Topic:
        from troposphere.ses import Topic as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfigurationSetAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-configurationsetattributes.html
    Properties:
        - Name: ConfigurationSetName
    
    """
    
    ConfigurationSetName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-configurationsetattributes.html#cfn-ses-emailidentity-configurationsetattributes-configurationsetname""", alias="ConfigurationSetName")
    


    @property
    def tropo_type(self) -> troposphere.ses.ConfigurationSetAttributes:
        from troposphere.ses import ConfigurationSetAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DkimAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimattributes.html
    Properties:
        - Name: SigningEnabled
    
    """
    
    SigningEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimattributes.html#cfn-ses-emailidentity-dkimattributes-signingenabled""", alias="SigningEnabled")
    


    @property
    def tropo_type(self) -> troposphere.ses.DkimAttributes:
        from troposphere.ses import DkimAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DkimSigningAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html
    Properties:
        - Name: DomainSigningPrivateKey
        - Name: DomainSigningSelector
        - Name: NextSigningKeyLength
    
    """
    
    DomainSigningPrivateKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-domainsigningprivatekey""", alias="DomainSigningPrivateKey")
    DomainSigningSelector_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-domainsigningselector""", alias="DomainSigningSelector")
    NextSigningKeyLength_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-nextsigningkeylength""", alias="NextSigningKeyLength")
    


    @property
    def tropo_type(self) -> troposphere.ses.DkimSigningAttributes:
        from troposphere.ses import DkimSigningAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FeedbackAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-feedbackattributes.html
    Properties:
        - Name: EmailForwardingEnabled
    
    """
    
    EmailForwardingEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-feedbackattributes.html#cfn-ses-emailidentity-feedbackattributes-emailforwardingenabled""", alias="EmailForwardingEnabled")
    


    @property
    def tropo_type(self) -> troposphere.ses.FeedbackAttributes:
        from troposphere.ses import FeedbackAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MailFromAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html
    Properties:
        - Name: MailFromDomain
        - Name: BehaviorOnMxFailure
    
    """
    
    MailFromDomain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html#cfn-ses-emailidentity-mailfromattributes-mailfromdomain""", alias="MailFromDomain")
    BehaviorOnMxFailure_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html#cfn-ses-emailidentity-mailfromattributes-behavioronmxfailure""", alias="BehaviorOnMxFailure")
    


    @property
    def tropo_type(self) -> troposphere.ses.MailFromAttributes:
        from troposphere.ses import MailFromAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Filter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html
    Properties:
        - Name: IpFilter
        - Name: Name
    
    """
    
    IpFilter_: 'IpFilter' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html#cfn-ses-receiptfilter-filter-ipfilter""", alias="IpFilter")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html#cfn-ses-receiptfilter-filter-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ses.Filter:
        from troposphere.ses import Filter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IpFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html
    Properties:
        - Name: Policy
        - Name: Cidr
    
    """
    
    Policy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html#cfn-ses-receiptfilter-ipfilter-policy""", alias="Policy")
    Cidr_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html#cfn-ses-receiptfilter-ipfilter-cidr""", alias="Cidr")
    


    @property
    def tropo_type(self) -> troposphere.ses.IpFilter:
        from troposphere.ses import IpFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html
    Properties:
        - Name: BounceAction
        - Name: S3Action
        - Name: StopAction
        - Name: SNSAction
        - Name: WorkmailAction
        - Name: AddHeaderAction
        - Name: LambdaAction
    
    """
    
    BounceAction_: Optional['BounceAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-bounceaction""", alias="BounceAction")
    S3Action_: Optional['S3Action'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-s3action""", alias="S3Action")
    StopAction_: Optional['StopAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-stopaction""", alias="StopAction")
    SNSAction_: Optional['SNSAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-snsaction""", alias="SNSAction")
    WorkmailAction_: Optional['WorkmailAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-workmailaction""", alias="WorkmailAction")
    AddHeaderAction_: Optional['AddHeaderAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-addheaderaction""", alias="AddHeaderAction")
    LambdaAction_: Optional['LambdaAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-lambdaaction""", alias="LambdaAction")
    


    @property
    def tropo_type(self) -> troposphere.ses.Action:
        from troposphere.ses import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AddHeaderAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html
    Properties:
        - Name: HeaderValue
        - Name: HeaderName
    
    """
    
    HeaderValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headervalue""", alias="HeaderValue")
    HeaderName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headername""", alias="HeaderName")
    


    @property
    def tropo_type(self) -> troposphere.ses.AddHeaderAction:
        from troposphere.ses import AddHeaderAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BounceAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html
    Properties:
        - Name: Sender
        - Name: SmtpReplyCode
        - Name: Message
        - Name: TopicArn
        - Name: StatusCode
    
    """
    
    Sender_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-sender""", alias="Sender")
    SmtpReplyCode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-smtpreplycode""", alias="SmtpReplyCode")
    Message_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-message""", alias="Message")
    TopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-topicarn""", alias="TopicArn")
    StatusCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-statuscode""", alias="StatusCode")
    


    @property
    def tropo_type(self) -> troposphere.ses.BounceAction:
        from troposphere.ses import BounceAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html
    Properties:
        - Name: FunctionArn
        - Name: TopicArn
        - Name: InvocationType
    
    """
    
    FunctionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-functionarn""", alias="FunctionArn")
    TopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-topicarn""", alias="TopicArn")
    InvocationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-invocationtype""", alias="InvocationType")
    


    @property
    def tropo_type(self) -> troposphere.ses.LambdaAction:
        from troposphere.ses import LambdaAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html
    Properties:
        - Name: ScanEnabled
        - Name: Recipients
        - Name: Actions
        - Name: Enabled
        - Name: Name
        - Name: TlsPolicy
    
    """
    
    ScanEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-scanenabled""", alias="ScanEnabled")
    Recipients_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-recipients""", alias="Recipients")
    Actions_: Optional[List['Action']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-actions""", alias="Actions")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-enabled""", alias="Enabled")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-name""", alias="Name")
    TlsPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-tlspolicy""", alias="TlsPolicy")
    


    @property
    def tropo_type(self) -> troposphere.ses.Rule:
        from troposphere.ses import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html
    Properties:
        - Name: BucketName
        - Name: KmsKeyArn
        - Name: TopicArn
        - Name: ObjectKeyPrefix
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-bucketname""", alias="BucketName")
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-kmskeyarn""", alias="KmsKeyArn")
    TopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-topicarn""", alias="TopicArn")
    ObjectKeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-objectkeyprefix""", alias="ObjectKeyPrefix")
    


    @property
    def tropo_type(self) -> troposphere.ses.S3Action:
        from troposphere.ses import S3Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SNSAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html
    Properties:
        - Name: TopicArn
        - Name: Encoding
    
    """
    
    TopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-topicarn""", alias="TopicArn")
    Encoding_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-encoding""", alias="Encoding")
    


    @property
    def tropo_type(self) -> troposphere.ses.SNSAction:
        from troposphere.ses import SNSAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StopAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html
    Properties:
        - Name: Scope
        - Name: TopicArn
    
    """
    
    Scope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-scope""", alias="Scope")
    TopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-topicarn""", alias="TopicArn")
    


    @property
    def tropo_type(self) -> troposphere.ses.StopAction:
        from troposphere.ses import StopAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WorkmailAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html
    Properties:
        - Name: TopicArn
        - Name: OrganizationArn
    
    """
    
    TopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-topicarn""", alias="TopicArn")
    OrganizationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-organizationarn""", alias="OrganizationArn")
    


    @property
    def tropo_type(self) -> troposphere.ses.WorkmailAction:
        from troposphere.ses import WorkmailAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Template(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html
    Properties:
        - Name: HtmlPart
        - Name: TextPart
        - Name: TemplateName
        - Name: SubjectPart
    
    """
    
    HtmlPart_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-htmlpart""", alias="HtmlPart")
    TextPart_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-textpart""", alias="TextPart")
    TemplateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-templatename""", alias="TemplateName")
    SubjectPart_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-subjectpart""", alias="SubjectPart")
    


    @property
    def tropo_type(self) -> troposphere.ses.Template:
        from troposphere.ses import Template as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DashboardAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-dashboardattributes.html
    Properties:
        - Name: EngagementMetrics
    
    """
    
    EngagementMetrics_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-dashboardattributes.html#cfn-ses-vdmattributes-dashboardattributes-engagementmetrics""", alias="EngagementMetrics")
    


    @property
    def tropo_type(self) -> troposphere.ses.DashboardAttributes:
        from troposphere.ses import DashboardAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GuardianAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-guardianattributes.html
    Properties:
        - Name: OptimizedSharedDelivery
    
    """
    
    OptimizedSharedDelivery_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-guardianattributes.html#cfn-ses-vdmattributes-guardianattributes-optimizedshareddelivery""", alias="OptimizedSharedDelivery")
    


    @property
    def tropo_type(self) -> troposphere.ses.GuardianAttributes:
        from troposphere.ses import GuardianAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ConfigurationSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html
    Properties:
        - Name: SendingOptions
        - Name: SuppressionOptions
        - Name: TrackingOptions
        - Name: ReputationOptions
        - Name: VdmOptions
        - Name: DeliveryOptions
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SendingOptions_: Optional['SendingOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-sendingoptions""", alias="SendingOptions")
    SuppressionOptions_: Optional['SuppressionOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-suppressionoptions""", alias="SuppressionOptions")
    TrackingOptions_: Optional['TrackingOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-trackingoptions""", alias="TrackingOptions")
    ReputationOptions_: Optional['ReputationOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-reputationoptions""", alias="ReputationOptions")
    VdmOptions_: Optional['VdmOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-vdmoptions""", alias="VdmOptions")
    DeliveryOptions_: Optional['DeliveryOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-deliveryoptions""", alias="DeliveryOptions")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ses.ConfigurationSet:
        from troposphere.ses import ConfigurationSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ses import ConfigurationSet as TropoT
        return resource_to_troposphere(self, TropoT)


class ConfigurationSetEventDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html
    Properties:
        - Name: ConfigurationSetName
        - Name: EventDestination
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConfigurationSetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-configurationsetname""", alias="ConfigurationSetName")
    EventDestination_: 'EventDestination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-eventdestination""", alias="EventDestination")
    

    @property
    def tropo_type(self) -> troposphere.ses.ConfigurationSetEventDestination:
        from troposphere.ses import ConfigurationSetEventDestination as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ses import ConfigurationSetEventDestination as TropoT
        return resource_to_troposphere(self, TropoT)


class ContactList(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html
    Properties:
        - Name: Description
        - Name: Topics
        - Name: ContactListName
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description""", alias="Description")
    Topics_: Optional[List['Topic']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics""", alias="Topics")
    ContactListName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname""", alias="ContactListName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ses.ContactList:
        from troposphere.ses import ContactList as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ses import ContactList as TropoT
        return resource_to_troposphere(self, TropoT)


class DedicatedIpPool(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html
    Properties:
        - Name: PoolName
        - Name: ScalingMode
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PoolName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html#cfn-ses-dedicatedippool-poolname""", alias="PoolName")
    ScalingMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html#cfn-ses-dedicatedippool-scalingmode""", alias="ScalingMode")
    

    @property
    def tropo_type(self) -> troposphere.ses.DedicatedIpPool:
        from troposphere.ses import DedicatedIpPool as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ses import DedicatedIpPool as TropoT
        return resource_to_troposphere(self, TropoT)


class EmailIdentity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html
    Properties:
        - Name: ConfigurationSetAttributes
        - Name: EmailIdentity
        - Name: DkimSigningAttributes
        - Name: DkimAttributes
        - Name: FeedbackAttributes
        - Name: MailFromAttributes
    Attributes:
        - Name: DkimDNSTokenValue1
        - Name: DkimDNSTokenName2
        - Name: DkimDNSTokenName3
        - Name: DkimDNSTokenName1
        - Name: DkimDNSTokenValue2
        - Name: DkimDNSTokenValue3
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConfigurationSetAttributes_: Optional['ConfigurationSetAttributes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-configurationsetattributes""", alias="ConfigurationSetAttributes")
    EmailIdentity_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-emailidentity""", alias="EmailIdentity")
    DkimSigningAttributes_: Optional['DkimSigningAttributes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-dkimsigningattributes""", alias="DkimSigningAttributes")
    DkimAttributes_: Optional['DkimAttributes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-dkimattributes""", alias="DkimAttributes")
    FeedbackAttributes_: Optional['FeedbackAttributes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-feedbackattributes""", alias="FeedbackAttributes")
    MailFromAttributes_: Optional['MailFromAttributes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-mailfromattributes""", alias="MailFromAttributes")
    

    @property
    def tropo_type(self) -> troposphere.ses.EmailIdentity:
        from troposphere.ses import EmailIdentity as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ses import EmailIdentity as TropoT
        return resource_to_troposphere(self, TropoT)


class ReceiptFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html
    Properties:
        - Name: Filter
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Filter_: 'Filter' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html#cfn-ses-receiptfilter-filter""", alias="Filter")
    

    @property
    def tropo_type(self) -> troposphere.ses.ReceiptFilter:
        from troposphere.ses import ReceiptFilter as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ses import ReceiptFilter as TropoT
        return resource_to_troposphere(self, TropoT)


class ReceiptRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html
    Properties:
        - Name: After
        - Name: Rule
        - Name: RuleSetName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    After_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-after""", alias="After")
    Rule_: 'Rule' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rule""", alias="Rule")
    RuleSetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rulesetname""", alias="RuleSetName")
    

    @property
    def tropo_type(self) -> troposphere.ses.ReceiptRule:
        from troposphere.ses import ReceiptRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ses import ReceiptRule as TropoT
        return resource_to_troposphere(self, TropoT)


class ReceiptRuleSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html
    Properties:
        - Name: RuleSetName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RuleSetName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html#cfn-ses-receiptruleset-rulesetname""", alias="RuleSetName")
    

    @property
    def tropo_type(self) -> troposphere.ses.ReceiptRuleSet:
        from troposphere.ses import ReceiptRuleSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ses import ReceiptRuleSet as TropoT
        return resource_to_troposphere(self, TropoT)


class Template(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html
    Properties:
        - Name: Template
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Template_: Optional['Template'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html#cfn-ses-template-template""", alias="Template")
    

    @property
    def tropo_type(self) -> troposphere.ses.Template:
        from troposphere.ses import Template as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ses import Template as TropoT
        return resource_to_troposphere(self, TropoT)


class VdmAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html
    Properties:
        - Name: DashboardAttributes
        - Name: GuardianAttributes
    Attributes:
        - Name: VdmAttributesResourceId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DashboardAttributes_: Optional['DashboardAttributes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html#cfn-ses-vdmattributes-dashboardattributes""", alias="DashboardAttributes")
    GuardianAttributes_: Optional['GuardianAttributes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html#cfn-ses-vdmattributes-guardianattributes""", alias="GuardianAttributes")
    

    @property
    def tropo_type(self) -> troposphere.ses.VdmAttributes:
        from troposphere.ses import VdmAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ses import VdmAttributes as TropoT
        return resource_to_troposphere(self, TropoT)

