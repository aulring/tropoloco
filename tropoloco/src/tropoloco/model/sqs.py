from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################




######################################################################
# AWS Resource
######################################################################


class Queue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html
    Properties:
        - Name: ReceiveMessageWaitTimeSeconds
        - Name: FifoThroughputLimit
        - Name: KmsMasterKeyId
        - Name: FifoQueue
        - Name: MaximumMessageSize
        - Name: VisibilityTimeout
        - Name: KmsDataKeyReusePeriodSeconds
        - Name: RedriveAllowPolicy
        - Name: SqsManagedSseEnabled
        - Name: DelaySeconds
        - Name: RedrivePolicy
        - Name: MessageRetentionPeriod
        - Name: DeduplicationScope
        - Name: ContentBasedDeduplication
        - Name: QueueName
        - Name: Tags
    Attributes:
        - Name: Arn
        - Name: QueueName
        - Name: QueueUrl
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ReceiveMessageWaitTimeSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-receivemessagewaittimeseconds""", alias="ReceiveMessageWaitTimeSeconds")
    FifoThroughputLimit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-fifothroughputlimit""", alias="FifoThroughputLimit")
    KmsMasterKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-kmsmasterkeyid""", alias="KmsMasterKeyId")
    FifoQueue_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-fifoqueue""", alias="FifoQueue")
    MaximumMessageSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-maximummessagesize""", alias="MaximumMessageSize")
    VisibilityTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-visibilitytimeout""", alias="VisibilityTimeout")
    KmsDataKeyReusePeriodSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-kmsdatakeyreuseperiodseconds""", alias="KmsDataKeyReusePeriodSeconds")
    RedriveAllowPolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-redriveallowpolicy""", alias="RedriveAllowPolicy")
    SqsManagedSseEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-sqsmanagedsseenabled""", alias="SqsManagedSseEnabled")
    DelaySeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-delayseconds""", alias="DelaySeconds")
    RedrivePolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-redrivepolicy""", alias="RedrivePolicy")
    MessageRetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-messageretentionperiod""", alias="MessageRetentionPeriod")
    DeduplicationScope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-deduplicationscope""", alias="DeduplicationScope")
    ContentBasedDeduplication_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-contentbaseddeduplication""", alias="ContentBasedDeduplication")
    QueueName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-queuename""", alias="QueueName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html#cfn-sqs-queue-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.sqs.Queue:
        from troposphere.sqs import Queue as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sqs import Queue as TropoT
        return resource_to_troposphere(self, TropoT)


class QueueInlinePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queueinlinepolicy.html
    Properties:
        - Name: PolicyDocument
        - Name: Queue
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queueinlinepolicy.html#cfn-sqs-queueinlinepolicy-policydocument""", alias="PolicyDocument")
    Queue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queueinlinepolicy.html#cfn-sqs-queueinlinepolicy-queue""", alias="Queue")
    

    @property
    def tropo_type(self) -> troposphere.sqs.QueueInlinePolicy:
        from troposphere.sqs import QueueInlinePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sqs import QueueInlinePolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class QueuePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queuepolicy.html
    Properties:
        - Name: PolicyDocument
        - Name: Queues
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queuepolicy.html#cfn-sqs-queuepolicy-policydocument""", alias="PolicyDocument")
    Queues_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queuepolicy.html#cfn-sqs-queuepolicy-queues""", alias="Queues")
    

    @property
    def tropo_type(self) -> troposphere.sqs.QueuePolicy:
        from troposphere.sqs import QueuePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.sqs import QueuePolicy as TropoT
        return resource_to_troposphere(self, TropoT)

