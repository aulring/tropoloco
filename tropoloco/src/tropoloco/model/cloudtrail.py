from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Destination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-channel-destination.html
    Properties:
        - Name: Type
        - Name: Location
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-channel-destination.html#cfn-cloudtrail-channel-destination-type""", alias="Type")
    Location_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-channel-destination.html#cfn-cloudtrail-channel-destination-location""", alias="Location")
    


    @property
    def tropo_type(self) -> troposphere.cloudtrail.Destination:
        from troposphere.cloudtrail import Destination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AdvancedEventSelector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedeventselector.html
    Properties:
        - Name: FieldSelectors
        - Name: Name
    
    """
    
    FieldSelectors_: List['AdvancedFieldSelector'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedeventselector.html#cfn-cloudtrail-eventdatastore-advancedeventselector-fieldselectors""", alias="FieldSelectors")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedeventselector.html#cfn-cloudtrail-eventdatastore-advancedeventselector-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cloudtrail.AdvancedEventSelector:
        from troposphere.cloudtrail import AdvancedEventSelector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AdvancedFieldSelector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html
    Properties:
        - Name: Field
        - Name: Equals
        - Name: NotStartsWith
        - Name: NotEndsWith
        - Name: StartsWith
        - Name: EndsWith
        - Name: NotEquals
    
    """
    
    Field_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-field""", alias="Field")
    Equals_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-equals""", alias="Equals")
    NotStartsWith_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-notstartswith""", alias="NotStartsWith")
    NotEndsWith_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-notendswith""", alias="NotEndsWith")
    StartsWith_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-startswith""", alias="StartsWith")
    EndsWith_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-endswith""", alias="EndsWith")
    NotEquals_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-notequals""", alias="NotEquals")
    


    @property
    def tropo_type(self) -> troposphere.cloudtrail.AdvancedFieldSelector:
        from troposphere.cloudtrail import AdvancedFieldSelector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AdvancedEventSelector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedeventselector.html
    Properties:
        - Name: FieldSelectors
        - Name: Name
    
    """
    
    FieldSelectors_: List['AdvancedFieldSelector'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedeventselector.html#cfn-cloudtrail-trail-advancedeventselector-fieldselectors""", alias="FieldSelectors")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedeventselector.html#cfn-cloudtrail-trail-advancedeventselector-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cloudtrail.AdvancedEventSelector:
        from troposphere.cloudtrail import AdvancedEventSelector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AdvancedFieldSelector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html
    Properties:
        - Name: Field
        - Name: Equals
        - Name: NotStartsWith
        - Name: NotEndsWith
        - Name: StartsWith
        - Name: EndsWith
        - Name: NotEquals
    
    """
    
    Field_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-field""", alias="Field")
    Equals_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-equals""", alias="Equals")
    NotStartsWith_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-notstartswith""", alias="NotStartsWith")
    NotEndsWith_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-notendswith""", alias="NotEndsWith")
    StartsWith_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-startswith""", alias="StartsWith")
    EndsWith_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-endswith""", alias="EndsWith")
    NotEquals_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-notequals""", alias="NotEquals")
    


    @property
    def tropo_type(self) -> troposphere.cloudtrail.AdvancedFieldSelector:
        from troposphere.cloudtrail import AdvancedFieldSelector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html
    Properties:
        - Name: Type
        - Name: Values
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html#cfn-cloudtrail-trail-dataresource-type""", alias="Type")
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html#cfn-cloudtrail-trail-dataresource-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.cloudtrail.DataResource:
        from troposphere.cloudtrail import DataResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EventSelector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html
    Properties:
        - Name: IncludeManagementEvents
        - Name: ReadWriteType
        - Name: ExcludeManagementEventSources
        - Name: DataResources
    
    """
    
    IncludeManagementEvents_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-includemanagementevents""", alias="IncludeManagementEvents")
    ReadWriteType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-readwritetype""", alias="ReadWriteType")
    ExcludeManagementEventSources_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-excludemanagementeventsources""", alias="ExcludeManagementEventSources")
    DataResources_: Optional[List['DataResource']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-dataresources""", alias="DataResources")
    


    @property
    def tropo_type(self) -> troposphere.cloudtrail.EventSelector:
        from troposphere.cloudtrail import EventSelector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InsightSelector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html
    Properties:
        - Name: InsightType
    
    """
    
    InsightType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html#cfn-cloudtrail-trail-insightselector-insighttype""", alias="InsightType")
    


    @property
    def tropo_type(self) -> troposphere.cloudtrail.InsightSelector:
        from troposphere.cloudtrail import InsightSelector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Channel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-channel.html
    Properties:
        - Name: Destinations
        - Name: Source
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ChannelArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Destinations_: Optional[List['Destination']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-channel.html#cfn-cloudtrail-channel-destinations""", alias="Destinations")
    Source_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-channel.html#cfn-cloudtrail-channel-source""", alias="Source")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-channel.html#cfn-cloudtrail-channel-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-channel.html#cfn-cloudtrail-channel-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.cloudtrail.Channel:
        from troposphere.cloudtrail import Channel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudtrail import Channel as TropoT
        return resource_to_troposphere(self, TropoT)


class EventDataStore(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html
    Properties:
        - Name: OrganizationEnabled
        - Name: KmsKeyId
        - Name: AdvancedEventSelectors
        - Name: TerminationProtectionEnabled
        - Name: MultiRegionEnabled
        - Name: RetentionPeriod
        - Name: IngestionEnabled
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: UpdatedTimestamp
        - Name: EventDataStoreArn
        - Name: CreatedTimestamp
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OrganizationEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-organizationenabled""", alias="OrganizationEnabled")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-kmskeyid""", alias="KmsKeyId")
    AdvancedEventSelectors_: Optional[List['AdvancedEventSelector']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-advancedeventselectors""", alias="AdvancedEventSelectors")
    TerminationProtectionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-terminationprotectionenabled""", alias="TerminationProtectionEnabled")
    MultiRegionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-multiregionenabled""", alias="MultiRegionEnabled")
    RetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-retentionperiod""", alias="RetentionPeriod")
    IngestionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-ingestionenabled""", alias="IngestionEnabled")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.cloudtrail.EventDataStore:
        from troposphere.cloudtrail import EventDataStore as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudtrail import EventDataStore as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourcePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-resourcepolicy.html
    Properties:
        - Name: ResourceArn
        - Name: ResourcePolicy
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-resourcepolicy.html#cfn-cloudtrail-resourcepolicy-resourcearn""", alias="ResourceArn")
    ResourcePolicy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-resourcepolicy.html#cfn-cloudtrail-resourcepolicy-resourcepolicy""", alias="ResourcePolicy")
    

    @property
    def tropo_type(self) -> troposphere.cloudtrail.ResourcePolicy:
        from troposphere.cloudtrail import ResourcePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudtrail import ResourcePolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class Trail(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html
    Properties:
        - Name: IncludeGlobalServiceEvents
        - Name: EventSelectors
        - Name: KMSKeyId
        - Name: CloudWatchLogsRoleArn
        - Name: S3KeyPrefix
        - Name: AdvancedEventSelectors
        - Name: TrailName
        - Name: IsOrganizationTrail
        - Name: InsightSelectors
        - Name: CloudWatchLogsLogGroupArn
        - Name: SnsTopicName
        - Name: IsMultiRegionTrail
        - Name: S3BucketName
        - Name: EnableLogFileValidation
        - Name: Tags
        - Name: IsLogging
    Attributes:
        - Name: SnsTopicArn
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IncludeGlobalServiceEvents_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-includeglobalserviceevents""", alias="IncludeGlobalServiceEvents")
    EventSelectors_: Optional[List['EventSelector']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-eventselectors""", alias="EventSelectors")
    KMSKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-kmskeyid""", alias="KMSKeyId")
    CloudWatchLogsRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsrolearn""", alias="CloudWatchLogsRoleArn")
    S3KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3keyprefix""", alias="S3KeyPrefix")
    AdvancedEventSelectors_: Optional[List['AdvancedEventSelector']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-advancedeventselectors""", alias="AdvancedEventSelectors")
    TrailName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-trailname""", alias="TrailName")
    IsOrganizationTrail_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-isorganizationtrail""", alias="IsOrganizationTrail")
    InsightSelectors_: Optional[List['InsightSelector']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-insightselectors""", alias="InsightSelectors")
    CloudWatchLogsLogGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsloggrouparn""", alias="CloudWatchLogsLogGroupArn")
    SnsTopicName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-snstopicname""", alias="SnsTopicName")
    IsMultiRegionTrail_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail""", alias="IsMultiRegionTrail")
    S3BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3bucketname""", alias="S3BucketName")
    EnableLogFileValidation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-enablelogfilevalidation""", alias="EnableLogFileValidation")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-tags""", alias="Tags")
    IsLogging_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-islogging""", alias="IsLogging")
    

    @property
    def tropo_type(self) -> troposphere.cloudtrail.Trail:
        from troposphere.cloudtrail import Trail as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudtrail import Trail as TropoT
        return resource_to_troposphere(self, TropoT)

