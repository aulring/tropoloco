from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class NotificationChannelConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationchannelconfig.html
    Properties:
        - Name: Filters
        - Name: Sns
    
    """
    
    Filters_: Optional['NotificationFilterConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationchannelconfig.html#cfn-devopsguru-notificationchannel-notificationchannelconfig-filters""", alias="Filters")
    Sns_: Optional['SnsChannelConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationchannelconfig.html#cfn-devopsguru-notificationchannel-notificationchannelconfig-sns""", alias="Sns")
    


    @property
    def tropo_type(self) -> troposphere.devopsguru.NotificationChannelConfig:
        from troposphere.devopsguru import NotificationChannelConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationFilterConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationfilterconfig.html
    Properties:
        - Name: MessageTypes
        - Name: Severities
    
    """
    
    MessageTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationfilterconfig.html#cfn-devopsguru-notificationchannel-notificationfilterconfig-messagetypes""", alias="MessageTypes")
    Severities_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationfilterconfig.html#cfn-devopsguru-notificationchannel-notificationfilterconfig-severities""", alias="Severities")
    


    @property
    def tropo_type(self) -> troposphere.devopsguru.NotificationFilterConfig:
        from troposphere.devopsguru import NotificationFilterConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SnsChannelConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-snschannelconfig.html
    Properties:
        - Name: TopicArn
    
    """
    
    TopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-snschannelconfig.html#cfn-devopsguru-notificationchannel-snschannelconfig-topicarn""", alias="TopicArn")
    


    @property
    def tropo_type(self) -> troposphere.devopsguru.SnsChannelConfig:
        from troposphere.devopsguru import SnsChannelConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudFormationCollectionFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter.html
    Properties:
        - Name: StackNames
    
    """
    
    StackNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter.html#cfn-devopsguru-resourcecollection-cloudformationcollectionfilter-stacknames""", alias="StackNames")
    


    @property
    def tropo_type(self) -> troposphere.devopsguru.CloudFormationCollectionFilter:
        from troposphere.devopsguru import CloudFormationCollectionFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceCollectionFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-resourcecollectionfilter.html
    Properties:
        - Name: CloudFormation
        - Name: Tags
    
    """
    
    CloudFormation_: Optional['CloudFormationCollectionFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-resourcecollectionfilter.html#cfn-devopsguru-resourcecollection-resourcecollectionfilter-cloudformation""", alias="CloudFormation")
    Tags_: Optional[List['TagCollection']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-resourcecollectionfilter.html#cfn-devopsguru-resourcecollection-resourcecollectionfilter-tags""", alias="Tags")
    


    @property
    def tropo_type(self) -> troposphere.devopsguru.ResourceCollectionFilter:
        from troposphere.devopsguru import ResourceCollectionFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagCollection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-tagcollection.html
    Properties:
        - Name: AppBoundaryKey
        - Name: TagValues
    
    """
    
    AppBoundaryKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-tagcollection.html#cfn-devopsguru-resourcecollection-tagcollection-appboundarykey""", alias="AppBoundaryKey")
    TagValues_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-tagcollection.html#cfn-devopsguru-resourcecollection-tagcollection-tagvalues""", alias="TagValues")
    


    @property
    def tropo_type(self) -> troposphere.devopsguru.TagCollection:
        from troposphere.devopsguru import TagCollection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class LogAnomalyDetectionIntegration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-loganomalydetectionintegration.html
    Attributes:
        - Name: AccountId
    """
    
    pass
    

    @property
    def tropo_type(self) -> troposphere.devopsguru.LogAnomalyDetectionIntegration:
        from troposphere.devopsguru import LogAnomalyDetectionIntegration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.devopsguru import LogAnomalyDetectionIntegration as TropoT
        return resource_to_troposphere(self, TropoT)


class NotificationChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html
    Properties:
        - Name: Config
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Config_: 'NotificationChannelConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html#cfn-devopsguru-notificationchannel-config""", alias="Config")
    

    @property
    def tropo_type(self) -> troposphere.devopsguru.NotificationChannel:
        from troposphere.devopsguru import NotificationChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.devopsguru import NotificationChannel as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourceCollection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html
    Properties:
        - Name: ResourceCollectionFilter
    Attributes:
        - Name: ResourceCollectionType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceCollectionFilter_: 'ResourceCollectionFilter' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html#cfn-devopsguru-resourcecollection-resourcecollectionfilter""", alias="ResourceCollectionFilter")
    

    @property
    def tropo_type(self) -> troposphere.devopsguru.ResourceCollection:
        from troposphere.devopsguru import ResourceCollection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.devopsguru import ResourceCollection as TropoT
        return resource_to_troposphere(self, TropoT)

