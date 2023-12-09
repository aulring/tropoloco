from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class LoggingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-loggingconfig.html
    Properties:
        - Name: FailureFeedbackRoleArn
        - Name: SuccessFeedbackSampleRate
        - Name: SuccessFeedbackRoleArn
        - Name: Protocol
    
    """
    
    FailureFeedbackRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-loggingconfig.html#cfn-sns-topic-loggingconfig-failurefeedbackrolearn""", alias="FailureFeedbackRoleArn")
    SuccessFeedbackSampleRate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-loggingconfig.html#cfn-sns-topic-loggingconfig-successfeedbacksamplerate""", alias="SuccessFeedbackSampleRate")
    SuccessFeedbackRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-loggingconfig.html#cfn-sns-topic-loggingconfig-successfeedbackrolearn""", alias="SuccessFeedbackRoleArn")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-loggingconfig.html#cfn-sns-topic-loggingconfig-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.sns.LoggingConfig:
        from troposphere.sns import LoggingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Subscription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-subscription.html
    Properties:
        - Name: Endpoint
        - Name: Protocol
    
    """
    
    Endpoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-subscription.html#cfn-sns-topic-subscription-endpoint""", alias="Endpoint")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-subscription.html#cfn-sns-topic-subscription-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.sns.Subscription:
        from troposphere.sns import Subscription as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Subscription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html
    Properties:
        - Name: DeliveryPolicy
        - Name: Endpoint
        - Name: FilterPolicy
        - Name: FilterPolicyScope
        - Name: Protocol
        - Name: RawMessageDelivery
        - Name: RedrivePolicy
        - Name: Region
        - Name: ReplayPolicy
        - Name: SubscriptionRoleArn
        - Name: TopicArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DeliveryPolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-deliverypolicy""", alias="DeliveryPolicy")
    Endpoint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-endpoint""", alias="Endpoint")
    FilterPolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-filterpolicy""", alias="FilterPolicy")
    FilterPolicyScope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-filterpolicyscope""", alias="FilterPolicyScope")
    Protocol_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-protocol""", alias="Protocol")
    RawMessageDelivery_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-rawmessagedelivery""", alias="RawMessageDelivery")
    RedrivePolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-redrivepolicy""", alias="RedrivePolicy")
    Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-region""", alias="Region")
    ReplayPolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-replaypolicy""", alias="ReplayPolicy")
    SubscriptionRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-subscriptionrolearn""", alias="SubscriptionRoleArn")
    TopicArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#topicarn""", alias="TopicArn")
    

    @property
    def tropo_type(self) -> troposphere.sns.Subscription:
        from troposphere.sns import Subscription as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sns import Subscription as TropoT
        return resource_to_troposphere(self, TropoT)


class Topic(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html
    Properties:
        - Name: SignatureVersion
        - Name: DeliveryStatusLogging
        - Name: KmsMasterKeyId
        - Name: TracingConfig
        - Name: FifoTopic
        - Name: DisplayName
        - Name: ContentBasedDeduplication
        - Name: Subscription
        - Name: Tags
        - Name: DataProtectionPolicy
        - Name: TopicName
        - Name: ArchivePolicy
    Attributes:
        - Name: TopicArn
        - Name: TopicName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SignatureVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-signatureversion""", alias="SignatureVersion")
    DeliveryStatusLogging_: Optional[List['LoggingConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-deliverystatuslogging""", alias="DeliveryStatusLogging")
    KmsMasterKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-kmsmasterkeyid""", alias="KmsMasterKeyId")
    TracingConfig_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-tracingconfig""", alias="TracingConfig")
    FifoTopic_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-fifotopic""", alias="FifoTopic")
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-displayname""", alias="DisplayName")
    ContentBasedDeduplication_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-contentbaseddeduplication""", alias="ContentBasedDeduplication")
    Subscription_: Optional[List['Subscription']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-subscription""", alias="Subscription")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-tags""", alias="Tags")
    DataProtectionPolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-dataprotectionpolicy""", alias="DataProtectionPolicy")
    TopicName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-topicname""", alias="TopicName")
    ArchivePolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-archivepolicy""", alias="ArchivePolicy")
    

    @property
    def tropo_type(self) -> troposphere.sns.Topic:
        from troposphere.sns import Topic as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sns import Topic as TropoT
        return resource_to_troposphere(self, TropoT)


class TopicInlinePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicinlinepolicy.html
    Properties:
        - Name: TopicArn
        - Name: PolicyDocument
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TopicArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicinlinepolicy.html#cfn-sns-topicinlinepolicy-topicarn""", alias="TopicArn")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicinlinepolicy.html#cfn-sns-topicinlinepolicy-policydocument""", alias="PolicyDocument")
    

    @property
    def tropo_type(self) -> troposphere.sns.TopicInlinePolicy:
        from troposphere.sns import TopicInlinePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sns import TopicInlinePolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class TopicPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicpolicy.html
    Properties:
        - Name: Topics
        - Name: PolicyDocument
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Topics_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicpolicy.html#cfn-sns-topicpolicy-topics""", alias="Topics")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicpolicy.html#cfn-sns-topicpolicy-policydocument""", alias="PolicyDocument")
    

    @property
    def tropo_type(self) -> troposphere.sns.TopicPolicy:
        from troposphere.sns import TopicPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sns import TopicPolicy as TropoT
        return resource_to_troposphere(self, TropoT)

