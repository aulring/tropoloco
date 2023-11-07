from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



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
        - Name: KmsMasterKeyId
        - Name: TracingConfig
        - Name: DisplayName
        - Name: FifoTopic
        - Name: ContentBasedDeduplication
        - Name: Subscription
        - Name: Tags
        - Name: DataProtectionPolicy
        - Name: ArchivePolicy
        - Name: TopicName
    Attributes:
        - Name: TopicArn
        - Name: TopicName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SignatureVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-signatureversion""", alias="SignatureVersion")
    KmsMasterKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-kmsmasterkeyid""", alias="KmsMasterKeyId")
    TracingConfig_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-tracingconfig""", alias="TracingConfig")
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-displayname""", alias="DisplayName")
    FifoTopic_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-fifotopic""", alias="FifoTopic")
    ContentBasedDeduplication_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-contentbaseddeduplication""", alias="ContentBasedDeduplication")
    Subscription_: Optional[List['Subscription']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-subscription""", alias="Subscription")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-tags""", alias="Tags")
    DataProtectionPolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-dataprotectionpolicy""", alias="DataProtectionPolicy")
    ArchivePolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-archivepolicy""", alias="ArchivePolicy")
    TopicName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-topicname""", alias="TopicName")
    

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

