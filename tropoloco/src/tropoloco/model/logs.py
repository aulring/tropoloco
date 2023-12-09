from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Dimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html#cfn-logs-metricfilter-dimension-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html#cfn-logs-metricfilter-dimension-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.logs.Dimension:
        from troposphere.logs import Dimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricTransformation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html
    Properties:
        - Name: DefaultValue
        - Name: MetricName
        - Name: MetricValue
        - Name: MetricNamespace
        - Name: Dimensions
        - Name: Unit
    
    """
    
    DefaultValue_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-defaultvalue""", alias="DefaultValue")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-metricname""", alias="MetricName")
    MetricValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-metricvalue""", alias="MetricValue")
    MetricNamespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-metricnamespace""", alias="MetricNamespace")
    Dimensions_: Optional[List['Dimension']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-dimensions""", alias="Dimensions")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.logs.MetricTransformation:
        from troposphere.logs import MetricTransformation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AccountPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html
    Properties:
        - Name: PolicyType
        - Name: Scope
        - Name: PolicyName
        - Name: PolicyDocument
    Attributes:
        - Name: AccountId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PolicyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html#cfn-logs-accountpolicy-policytype""", alias="PolicyType")
    Scope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html#cfn-logs-accountpolicy-scope""", alias="Scope")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html#cfn-logs-accountpolicy-policyname""", alias="PolicyName")
    PolicyDocument_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html#cfn-logs-accountpolicy-policydocument""", alias="PolicyDocument")
    

    @property
    def tropo_type(self) -> troposphere.logs.AccountPolicy:
        from troposphere.logs import AccountPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.logs import AccountPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class Delivery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html
    Properties:
        - Name: DeliveryDestinationArn
        - Name: DeliverySourceName
        - Name: Tags
    Attributes:
        - Name: DeliveryId
        - Name: Arn
        - Name: DeliveryDestinationType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DeliveryDestinationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html#cfn-logs-delivery-deliverydestinationarn""", alias="DeliveryDestinationArn")
    DeliverySourceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html#cfn-logs-delivery-deliverysourcename""", alias="DeliverySourceName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html#cfn-logs-delivery-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.logs.Delivery:
        from troposphere.logs import Delivery as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.logs import Delivery as TropoT
        return resource_to_troposphere(self, TropoT)


class DeliveryDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html
    Properties:
        - Name: DestinationResourceArn
        - Name: DeliveryDestinationPolicy
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
        - Name: DeliveryDestinationType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DestinationResourceArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html#cfn-logs-deliverydestination-destinationresourcearn""", alias="DestinationResourceArn")
    DeliveryDestinationPolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html#cfn-logs-deliverydestination-deliverydestinationpolicy""", alias="DeliveryDestinationPolicy")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html#cfn-logs-deliverydestination-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html#cfn-logs-deliverydestination-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.logs.DeliveryDestination:
        from troposphere.logs import DeliveryDestination as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.logs import DeliveryDestination as TropoT
        return resource_to_troposphere(self, TropoT)


class DeliverySource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.html
    Properties:
        - Name: ResourceArn
        - Name: LogType
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Service
        - Name: Arn
        - Name: ResourceArns
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.html#cfn-logs-deliverysource-resourcearn""", alias="ResourceArn")
    LogType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.html#cfn-logs-deliverysource-logtype""", alias="LogType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.html#cfn-logs-deliverysource-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.html#cfn-logs-deliverysource-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.logs.DeliverySource:
        from troposphere.logs import DeliverySource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.logs import DeliverySource as TropoT
        return resource_to_troposphere(self, TropoT)


class Destination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html
    Properties:
        - Name: DestinationPolicy
        - Name: DestinationName
        - Name: TargetArn
        - Name: RoleArn
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DestinationPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-destinationpolicy""", alias="DestinationPolicy")
    DestinationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-destinationname""", alias="DestinationName")
    TargetArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-targetarn""", alias="TargetArn")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-rolearn""", alias="RoleArn")
    

    @property
    def tropo_type(self) -> troposphere.logs.Destination:
        from troposphere.logs import Destination as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.logs import Destination as TropoT
        return resource_to_troposphere(self, TropoT)


class LogAnomalyDetector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html
    Properties:
        - Name: AnomalyVisibilityTime
        - Name: FilterPattern
        - Name: AccountId
        - Name: KmsKeyId
        - Name: LogGroupArnList
        - Name: EvaluationFrequency
        - Name: DetectorName
    Attributes:
        - Name: CreationTimeStamp
        - Name: AnomalyDetectorStatus
        - Name: AnomalyDetectorArn
        - Name: LastModifiedTimeStamp
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AnomalyVisibilityTime_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-anomalyvisibilitytime""", alias="AnomalyVisibilityTime")
    FilterPattern_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-filterpattern""", alias="FilterPattern")
    AccountId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-accountid""", alias="AccountId")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-kmskeyid""", alias="KmsKeyId")
    LogGroupArnList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-loggrouparnlist""", alias="LogGroupArnList")
    EvaluationFrequency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-evaluationfrequency""", alias="EvaluationFrequency")
    DetectorName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-detectorname""", alias="DetectorName")
    

    @property
    def tropo_type(self) -> troposphere.logs.LogAnomalyDetector:
        from troposphere.logs import LogAnomalyDetector as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.logs import LogAnomalyDetector as TropoT
        return resource_to_troposphere(self, TropoT)


class LogGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html
    Properties:
        - Name: RetentionInDays
        - Name: KmsKeyId
        - Name: LogGroupClass
        - Name: LogGroupName
        - Name: Tags
        - Name: DataProtectionPolicy
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RetentionInDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-retentionindays""", alias="RetentionInDays")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-kmskeyid""", alias="KmsKeyId")
    LogGroupClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-loggroupclass""", alias="LogGroupClass")
    LogGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-loggroupname""", alias="LogGroupName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-tags""", alias="Tags")
    DataProtectionPolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-dataprotectionpolicy""", alias="DataProtectionPolicy")
    

    @property
    def tropo_type(self) -> troposphere.logs.LogGroup:
        from troposphere.logs import LogGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.logs import LogGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class LogStream(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html
    Properties:
        - Name: LogStreamName
        - Name: LogGroupName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LogStreamName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html#cfn-logs-logstream-logstreamname""", alias="LogStreamName")
    LogGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html#cfn-logs-logstream-loggroupname""", alias="LogGroupName")
    

    @property
    def tropo_type(self) -> troposphere.logs.LogStream:
        from troposphere.logs import LogStream as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.logs import LogStream as TropoT
        return resource_to_troposphere(self, TropoT)


class MetricFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html
    Properties:
        - Name: MetricTransformations
        - Name: FilterPattern
        - Name: LogGroupName
        - Name: FilterName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MetricTransformations_: List['MetricTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-logs-metricfilter-metrictransformations""", alias="MetricTransformations")
    FilterPattern_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-logs-metricfilter-filterpattern""", alias="FilterPattern")
    LogGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-logs-metricfilter-loggroupname""", alias="LogGroupName")
    FilterName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-logs-metricfilter-filtername""", alias="FilterName")
    

    @property
    def tropo_type(self) -> troposphere.logs.MetricFilter:
        from troposphere.logs import MetricFilter as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.logs import MetricFilter as TropoT
        return resource_to_troposphere(self, TropoT)


class QueryDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html
    Properties:
        - Name: QueryString
        - Name: LogGroupNames
        - Name: Name
    Attributes:
        - Name: QueryDefinitionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    QueryString_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html#cfn-logs-querydefinition-querystring""", alias="QueryString")
    LogGroupNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html#cfn-logs-querydefinition-loggroupnames""", alias="LogGroupNames")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html#cfn-logs-querydefinition-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.logs.QueryDefinition:
        from troposphere.logs import QueryDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.logs import QueryDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourcePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-resourcepolicy.html
    Properties:
        - Name: PolicyName
        - Name: PolicyDocument
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-resourcepolicy.html#cfn-logs-resourcepolicy-policyname""", alias="PolicyName")
    PolicyDocument_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-resourcepolicy.html#cfn-logs-resourcepolicy-policydocument""", alias="PolicyDocument")
    

    @property
    def tropo_type(self) -> troposphere.logs.ResourcePolicy:
        from troposphere.logs import ResourcePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.logs import ResourcePolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class SubscriptionFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html
    Properties:
        - Name: FilterPattern
        - Name: Distribution
        - Name: LogGroupName
        - Name: FilterName
        - Name: DestinationArn
        - Name: RoleArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FilterPattern_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-filterpattern""", alias="FilterPattern")
    Distribution_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-distribution""", alias="Distribution")
    LogGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-loggroupname""", alias="LogGroupName")
    FilterName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-filtername""", alias="FilterName")
    DestinationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-destinationarn""", alias="DestinationArn")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-rolearn""", alias="RoleArn")
    

    @property
    def tropo_type(self) -> troposphere.logs.SubscriptionFilter:
        from troposphere.logs import SubscriptionFilter as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.logs import SubscriptionFilter as TropoT
        return resource_to_troposphere(self, TropoT)

