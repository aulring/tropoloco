from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ChannelStorage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-channelstorage.html
    Properties:
        - Name: CustomerManagedS3
        - Name: ServiceManagedS3
    
    """
    
    CustomerManagedS3_: Optional['CustomerManagedS3'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-channelstorage.html#cfn-iotanalytics-channel-channelstorage-customermanageds3""", alias="CustomerManagedS3")
    ServiceManagedS3_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-channelstorage.html#cfn-iotanalytics-channel-channelstorage-servicemanageds3""", alias="ServiceManagedS3")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.ChannelStorage:
        from troposphere.iotanalytics import ChannelStorage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomerManagedS3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html
    Properties:
        - Name: Bucket
        - Name: RoleArn
        - Name: KeyPrefix
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html#cfn-iotanalytics-channel-customermanageds3-bucket""", alias="Bucket")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html#cfn-iotanalytics-channel-customermanageds3-rolearn""", alias="RoleArn")
    KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html#cfn-iotanalytics-channel-customermanageds3-keyprefix""", alias="KeyPrefix")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.CustomerManagedS3:
        from troposphere.iotanalytics import CustomerManagedS3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RetentionPeriod(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-retentionperiod.html
    Properties:
        - Name: NumberOfDays
        - Name: Unlimited
    
    """
    
    NumberOfDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-retentionperiod.html#cfn-iotanalytics-channel-retentionperiod-numberofdays""", alias="NumberOfDays")
    Unlimited_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-retentionperiod.html#cfn-iotanalytics-channel-retentionperiod-unlimited""", alias="Unlimited")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.RetentionPeriod:
        from troposphere.iotanalytics import RetentionPeriod as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html
    Properties:
        - Name: ActionName
        - Name: ContainerAction
        - Name: QueryAction
    
    """
    
    ActionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html#cfn-iotanalytics-dataset-action-actionname""", alias="ActionName")
    ContainerAction_: Optional['ContainerAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html#cfn-iotanalytics-dataset-action-containeraction""", alias="ContainerAction")
    QueryAction_: Optional['QueryAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html#cfn-iotanalytics-dataset-action-queryaction""", alias="QueryAction")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.Action:
        from troposphere.iotanalytics import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContainerAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html
    Properties:
        - Name: Variables
        - Name: ExecutionRoleArn
        - Name: Image
        - Name: ResourceConfiguration
    
    """
    
    Variables_: Optional[List['Variable']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html#cfn-iotanalytics-dataset-containeraction-variables""", alias="Variables")
    ExecutionRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html#cfn-iotanalytics-dataset-containeraction-executionrolearn""", alias="ExecutionRoleArn")
    Image_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html#cfn-iotanalytics-dataset-containeraction-image""", alias="Image")
    ResourceConfiguration_: 'ResourceConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html#cfn-iotanalytics-dataset-containeraction-resourceconfiguration""", alias="ResourceConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.ContainerAction:
        from troposphere.iotanalytics import ContainerAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatasetContentDeliveryRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryrule.html
    Properties:
        - Name: Destination
        - Name: EntryName
    
    """
    
    Destination_: 'DatasetContentDeliveryRuleDestination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryrule.html#cfn-iotanalytics-dataset-datasetcontentdeliveryrule-destination""", alias="Destination")
    EntryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryrule.html#cfn-iotanalytics-dataset-datasetcontentdeliveryrule-entryname""", alias="EntryName")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.DatasetContentDeliveryRule:
        from troposphere.iotanalytics import DatasetContentDeliveryRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatasetContentDeliveryRuleDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryruledestination.html
    Properties:
        - Name: IotEventsDestinationConfiguration
        - Name: S3DestinationConfiguration
    
    """
    
    IotEventsDestinationConfiguration_: Optional['IotEventsDestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryruledestination.html#cfn-iotanalytics-dataset-datasetcontentdeliveryruledestination-ioteventsdestinationconfiguration""", alias="IotEventsDestinationConfiguration")
    S3DestinationConfiguration_: Optional['S3DestinationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryruledestination.html#cfn-iotanalytics-dataset-datasetcontentdeliveryruledestination-s3destinationconfiguration""", alias="S3DestinationConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.DatasetContentDeliveryRuleDestination:
        from troposphere.iotanalytics import DatasetContentDeliveryRuleDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatasetContentVersionValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentversionvalue.html
    Properties:
        - Name: DatasetName
    
    """
    
    DatasetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentversionvalue.html#cfn-iotanalytics-dataset-datasetcontentversionvalue-datasetname""", alias="DatasetName")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.DatasetContentVersionValue:
        from troposphere.iotanalytics import DatasetContentVersionValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeltaTime(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html
    Properties:
        - Name: TimeExpression
        - Name: OffsetSeconds
    
    """
    
    TimeExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html#cfn-iotanalytics-dataset-deltatime-timeexpression""", alias="TimeExpression")
    OffsetSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html#cfn-iotanalytics-dataset-deltatime-offsetseconds""", alias="OffsetSeconds")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.DeltaTime:
        from troposphere.iotanalytics import DeltaTime as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeltaTimeSessionWindowConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatimesessionwindowconfiguration.html
    Properties:
        - Name: TimeoutInMinutes
    
    """
    
    TimeoutInMinutes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatimesessionwindowconfiguration.html#cfn-iotanalytics-dataset-deltatimesessionwindowconfiguration-timeoutinminutes""", alias="TimeoutInMinutes")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.DeltaTimeSessionWindowConfiguration:
        from troposphere.iotanalytics import DeltaTimeSessionWindowConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Filter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-filter.html
    Properties:
        - Name: DeltaTime
    
    """
    
    DeltaTime_: Optional['DeltaTime'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-filter.html#cfn-iotanalytics-dataset-filter-deltatime""", alias="DeltaTime")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.Filter:
        from troposphere.iotanalytics import Filter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GlueConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-glueconfiguration.html
    Properties:
        - Name: TableName
        - Name: DatabaseName
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-glueconfiguration.html#cfn-iotanalytics-dataset-glueconfiguration-tablename""", alias="TableName")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-glueconfiguration.html#cfn-iotanalytics-dataset-glueconfiguration-databasename""", alias="DatabaseName")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.GlueConfiguration:
        from troposphere.iotanalytics import GlueConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IotEventsDestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-ioteventsdestinationconfiguration.html
    Properties:
        - Name: InputName
        - Name: RoleArn
    
    """
    
    InputName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-ioteventsdestinationconfiguration.html#cfn-iotanalytics-dataset-ioteventsdestinationconfiguration-inputname""", alias="InputName")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-ioteventsdestinationconfiguration.html#cfn-iotanalytics-dataset-ioteventsdestinationconfiguration-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.IotEventsDestinationConfiguration:
        from troposphere.iotanalytics import IotEventsDestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LateDataRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedatarule.html
    Properties:
        - Name: RuleConfiguration
        - Name: RuleName
    
    """
    
    RuleConfiguration_: 'LateDataRuleConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedatarule.html#cfn-iotanalytics-dataset-latedatarule-ruleconfiguration""", alias="RuleConfiguration")
    RuleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedatarule.html#cfn-iotanalytics-dataset-latedatarule-rulename""", alias="RuleName")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.LateDataRule:
        from troposphere.iotanalytics import LateDataRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LateDataRuleConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedataruleconfiguration.html
    Properties:
        - Name: DeltaTimeSessionWindowConfiguration
    
    """
    
    DeltaTimeSessionWindowConfiguration_: Optional['DeltaTimeSessionWindowConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedataruleconfiguration.html#cfn-iotanalytics-dataset-latedataruleconfiguration-deltatimesessionwindowconfiguration""", alias="DeltaTimeSessionWindowConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.LateDataRuleConfiguration:
        from troposphere.iotanalytics import LateDataRuleConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputFileUriValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-outputfileurivalue.html
    Properties:
        - Name: FileName
    
    """
    
    FileName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-outputfileurivalue.html#cfn-iotanalytics-dataset-outputfileurivalue-filename""", alias="FileName")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.OutputFileUriValue:
        from troposphere.iotanalytics import OutputFileUriValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QueryAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-queryaction.html
    Properties:
        - Name: Filters
        - Name: SqlQuery
    
    """
    
    Filters_: Optional[List['Filter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-queryaction.html#cfn-iotanalytics-dataset-queryaction-filters""", alias="Filters")
    SqlQuery_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-queryaction.html#cfn-iotanalytics-dataset-queryaction-sqlquery""", alias="SqlQuery")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.QueryAction:
        from troposphere.iotanalytics import QueryAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-resourceconfiguration.html
    Properties:
        - Name: VolumeSizeInGB
        - Name: ComputeType
    
    """
    
    VolumeSizeInGB_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-resourceconfiguration.html#cfn-iotanalytics-dataset-resourceconfiguration-volumesizeingb""", alias="VolumeSizeInGB")
    ComputeType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-resourceconfiguration.html#cfn-iotanalytics-dataset-resourceconfiguration-computetype""", alias="ComputeType")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.ResourceConfiguration:
        from troposphere.iotanalytics import ResourceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RetentionPeriod(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-retentionperiod.html
    Properties:
        - Name: NumberOfDays
        - Name: Unlimited
    
    """
    
    NumberOfDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-retentionperiod.html#cfn-iotanalytics-dataset-retentionperiod-numberofdays""", alias="NumberOfDays")
    Unlimited_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-retentionperiod.html#cfn-iotanalytics-dataset-retentionperiod-unlimited""", alias="Unlimited")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.RetentionPeriod:
        from troposphere.iotanalytics import RetentionPeriod as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3DestinationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html
    Properties:
        - Name: GlueConfiguration
        - Name: Bucket
        - Name: Key
        - Name: RoleArn
    
    """
    
    GlueConfiguration_: Optional['GlueConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html#cfn-iotanalytics-dataset-s3destinationconfiguration-glueconfiguration""", alias="GlueConfiguration")
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html#cfn-iotanalytics-dataset-s3destinationconfiguration-bucket""", alias="Bucket")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html#cfn-iotanalytics-dataset-s3destinationconfiguration-key""", alias="Key")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html#cfn-iotanalytics-dataset-s3destinationconfiguration-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.S3DestinationConfiguration:
        from troposphere.iotanalytics import S3DestinationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Schedule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-schedule.html
    Properties:
        - Name: ScheduleExpression
    
    """
    
    ScheduleExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-schedule.html#cfn-iotanalytics-dataset-schedule-scheduleexpression""", alias="ScheduleExpression")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.Schedule:
        from troposphere.iotanalytics import Schedule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Trigger(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html
    Properties:
        - Name: Schedule
        - Name: TriggeringDataset
    
    """
    
    Schedule_: Optional['Schedule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html#cfn-iotanalytics-dataset-trigger-schedule""", alias="Schedule")
    TriggeringDataset_: Optional['TriggeringDataset'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html#cfn-iotanalytics-dataset-trigger-triggeringdataset""", alias="TriggeringDataset")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.Trigger:
        from troposphere.iotanalytics import Trigger as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TriggeringDataset(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-triggeringdataset.html
    Properties:
        - Name: DatasetName
    
    """
    
    DatasetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-triggeringdataset.html#cfn-iotanalytics-dataset-triggeringdataset-datasetname""", alias="DatasetName")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.TriggeringDataset:
        from troposphere.iotanalytics import TriggeringDataset as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Variable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html
    Properties:
        - Name: DatasetContentVersionValue
        - Name: DoubleValue
        - Name: OutputFileUriValue
        - Name: VariableName
        - Name: StringValue
    
    """
    
    DatasetContentVersionValue_: Optional['DatasetContentVersionValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-datasetcontentversionvalue""", alias="DatasetContentVersionValue")
    DoubleValue_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-doublevalue""", alias="DoubleValue")
    OutputFileUriValue_: Optional['OutputFileUriValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-outputfileurivalue""", alias="OutputFileUriValue")
    VariableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-variablename""", alias="VariableName")
    StringValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-stringvalue""", alias="StringValue")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.Variable:
        from troposphere.iotanalytics import Variable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VersioningConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-versioningconfiguration.html
    Properties:
        - Name: MaxVersions
        - Name: Unlimited
    
    """
    
    MaxVersions_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-versioningconfiguration.html#cfn-iotanalytics-dataset-versioningconfiguration-maxversions""", alias="MaxVersions")
    Unlimited_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-versioningconfiguration.html#cfn-iotanalytics-dataset-versioningconfiguration-unlimited""", alias="Unlimited")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.VersioningConfiguration:
        from troposphere.iotanalytics import VersioningConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Column(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-column.html
    Properties:
        - Name: Type
        - Name: Name
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-column.html#cfn-iotanalytics-datastore-column-type""", alias="Type")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-column.html#cfn-iotanalytics-datastore-column-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.Column:
        from troposphere.iotanalytics import Column as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomerManagedS3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html
    Properties:
        - Name: Bucket
        - Name: RoleArn
        - Name: KeyPrefix
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html#cfn-iotanalytics-datastore-customermanageds3-bucket""", alias="Bucket")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html#cfn-iotanalytics-datastore-customermanageds3-rolearn""", alias="RoleArn")
    KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html#cfn-iotanalytics-datastore-customermanageds3-keyprefix""", alias="KeyPrefix")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.CustomerManagedS3:
        from troposphere.iotanalytics import CustomerManagedS3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomerManagedS3Storage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3storage.html
    Properties:
        - Name: Bucket
        - Name: KeyPrefix
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3storage.html#cfn-iotanalytics-datastore-customermanageds3storage-bucket""", alias="Bucket")
    KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3storage.html#cfn-iotanalytics-datastore-customermanageds3storage-keyprefix""", alias="KeyPrefix")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.CustomerManagedS3Storage:
        from troposphere.iotanalytics import CustomerManagedS3Storage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatastorePartition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html
    Properties:
        - Name: Partition
        - Name: TimestampPartition
    
    """
    
    Partition_: Optional['Partition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html#cfn-iotanalytics-datastore-datastorepartition-partition""", alias="Partition")
    TimestampPartition_: Optional['TimestampPartition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html#cfn-iotanalytics-datastore-datastorepartition-timestamppartition""", alias="TimestampPartition")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.DatastorePartition:
        from troposphere.iotanalytics import DatastorePartition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatastorePartitions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartitions.html
    Properties:
        - Name: Partitions
    
    """
    
    Partitions_: Optional[List['DatastorePartition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartitions.html#cfn-iotanalytics-datastore-datastorepartitions-partitions""", alias="Partitions")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.DatastorePartitions:
        from troposphere.iotanalytics import DatastorePartitions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DatastoreStorage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html
    Properties:
        - Name: CustomerManagedS3
        - Name: ServiceManagedS3
        - Name: IotSiteWiseMultiLayerStorage
    
    """
    
    CustomerManagedS3_: Optional['CustomerManagedS3'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html#cfn-iotanalytics-datastore-datastorestorage-customermanageds3""", alias="CustomerManagedS3")
    ServiceManagedS3_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html#cfn-iotanalytics-datastore-datastorestorage-servicemanageds3""", alias="ServiceManagedS3")
    IotSiteWiseMultiLayerStorage_: Optional['IotSiteWiseMultiLayerStorage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html#cfn-iotanalytics-datastore-datastorestorage-iotsitewisemultilayerstorage""", alias="IotSiteWiseMultiLayerStorage")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.DatastoreStorage:
        from troposphere.iotanalytics import DatastoreStorage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FileFormatConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-fileformatconfiguration.html
    Properties:
        - Name: ParquetConfiguration
        - Name: JsonConfiguration
    
    """
    
    ParquetConfiguration_: Optional['ParquetConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-fileformatconfiguration.html#cfn-iotanalytics-datastore-fileformatconfiguration-parquetconfiguration""", alias="ParquetConfiguration")
    JsonConfiguration_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-fileformatconfiguration.html#cfn-iotanalytics-datastore-fileformatconfiguration-jsonconfiguration""", alias="JsonConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.FileFormatConfiguration:
        from troposphere.iotanalytics import FileFormatConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IotSiteWiseMultiLayerStorage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-iotsitewisemultilayerstorage.html
    Properties:
        - Name: CustomerManagedS3Storage
    
    """
    
    CustomerManagedS3Storage_: Optional['CustomerManagedS3Storage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-iotsitewisemultilayerstorage.html#cfn-iotanalytics-datastore-iotsitewisemultilayerstorage-customermanageds3storage""", alias="CustomerManagedS3Storage")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.IotSiteWiseMultiLayerStorage:
        from troposphere.iotanalytics import IotSiteWiseMultiLayerStorage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ParquetConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-parquetconfiguration.html
    Properties:
        - Name: SchemaDefinition
    
    """
    
    SchemaDefinition_: Optional['SchemaDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-parquetconfiguration.html#cfn-iotanalytics-datastore-parquetconfiguration-schemadefinition""", alias="SchemaDefinition")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.ParquetConfiguration:
        from troposphere.iotanalytics import ParquetConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Partition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-partition.html
    Properties:
        - Name: AttributeName
    
    """
    
    AttributeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-partition.html#cfn-iotanalytics-datastore-partition-attributename""", alias="AttributeName")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.Partition:
        from troposphere.iotanalytics import Partition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RetentionPeriod(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-retentionperiod.html
    Properties:
        - Name: NumberOfDays
        - Name: Unlimited
    
    """
    
    NumberOfDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-retentionperiod.html#cfn-iotanalytics-datastore-retentionperiod-numberofdays""", alias="NumberOfDays")
    Unlimited_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-retentionperiod.html#cfn-iotanalytics-datastore-retentionperiod-unlimited""", alias="Unlimited")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.RetentionPeriod:
        from troposphere.iotanalytics import RetentionPeriod as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SchemaDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-schemadefinition.html
    Properties:
        - Name: Columns
    
    """
    
    Columns_: Optional[List['Column']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-schemadefinition.html#cfn-iotanalytics-datastore-schemadefinition-columns""", alias="Columns")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.SchemaDefinition:
        from troposphere.iotanalytics import SchemaDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimestampPartition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html
    Properties:
        - Name: AttributeName
        - Name: TimestampFormat
    
    """
    
    AttributeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html#cfn-iotanalytics-datastore-timestamppartition-attributename""", alias="AttributeName")
    TimestampFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html#cfn-iotanalytics-datastore-timestamppartition-timestampformat""", alias="TimestampFormat")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.TimestampPartition:
        from troposphere.iotanalytics import TimestampPartition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Activity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html
    Properties:
        - Name: SelectAttributes
        - Name: Datastore
        - Name: Filter
        - Name: AddAttributes
        - Name: Channel
        - Name: DeviceShadowEnrich
        - Name: Math
        - Name: Lambda
        - Name: DeviceRegistryEnrich
        - Name: RemoveAttributes
    
    """
    
    SelectAttributes_: Optional['SelectAttributes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-selectattributes""", alias="SelectAttributes")
    Datastore_: Optional['ActivityDatastore'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-datastore""", alias="Datastore")
    Filter_: Optional['Filter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-filter""", alias="Filter")
    AddAttributes_: Optional['AddAttributes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-addattributes""", alias="AddAttributes")
    Channel_: Optional['ActivityChannel'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-channel""", alias="Channel")
    DeviceShadowEnrich_: Optional['DeviceShadowEnrich'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-deviceshadowenrich""", alias="DeviceShadowEnrich")
    Math_: Optional['Math'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-math""", alias="Math")
    Lambda_: Optional['Lambda'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-lambda""", alias="Lambda")
    DeviceRegistryEnrich_: Optional['DeviceRegistryEnrich'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-deviceregistryenrich""", alias="DeviceRegistryEnrich")
    RemoveAttributes_: Optional['RemoveAttributes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-removeattributes""", alias="RemoveAttributes")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.Activity:
        from troposphere.iotanalytics import Activity as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AddAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html
    Properties:
        - Name: Next
        - Name: Attributes
        - Name: Name
    
    """
    
    Next_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html#cfn-iotanalytics-pipeline-addattributes-next""", alias="Next")
    Attributes_: Dict[str, str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html#cfn-iotanalytics-pipeline-addattributes-attributes""", alias="Attributes")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html#cfn-iotanalytics-pipeline-addattributes-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.AddAttributes:
        from troposphere.iotanalytics import AddAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ActivityChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html
    Properties:
        - Name: ChannelName
        - Name: Next
        - Name: Name
    
    """
    
    ChannelName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html#cfn-iotanalytics-pipeline-channel-channelname""", alias="ChannelName")
    Next_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html#cfn-iotanalytics-pipeline-channel-next""", alias="Next")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html#cfn-iotanalytics-pipeline-channel-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.ActivityChannel:
        from troposphere.iotanalytics import ActivityChannel as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ActivityDatastore(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html
    Properties:
        - Name: DatastoreName
        - Name: Name
    
    """
    
    DatastoreName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html#cfn-iotanalytics-pipeline-datastore-datastorename""", alias="DatastoreName")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html#cfn-iotanalytics-pipeline-datastore-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.ActivityDatastore:
        from troposphere.iotanalytics import ActivityDatastore as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeviceRegistryEnrich(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html
    Properties:
        - Name: Attribute
        - Name: Next
        - Name: ThingName
        - Name: RoleArn
        - Name: Name
    
    """
    
    Attribute_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-attribute""", alias="Attribute")
    Next_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-next""", alias="Next")
    ThingName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-thingname""", alias="ThingName")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-rolearn""", alias="RoleArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.DeviceRegistryEnrich:
        from troposphere.iotanalytics import DeviceRegistryEnrich as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeviceShadowEnrich(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html
    Properties:
        - Name: Attribute
        - Name: Next
        - Name: ThingName
        - Name: RoleArn
        - Name: Name
    
    """
    
    Attribute_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-attribute""", alias="Attribute")
    Next_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-next""", alias="Next")
    ThingName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-thingname""", alias="ThingName")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-rolearn""", alias="RoleArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.DeviceShadowEnrich:
        from troposphere.iotanalytics import DeviceShadowEnrich as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Filter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html
    Properties:
        - Name: Filter
        - Name: Next
        - Name: Name
    
    """
    
    Filter_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html#cfn-iotanalytics-pipeline-filter-filter""", alias="Filter")
    Next_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html#cfn-iotanalytics-pipeline-filter-next""", alias="Next")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html#cfn-iotanalytics-pipeline-filter-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.Filter:
        from troposphere.iotanalytics import Filter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Lambda(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html
    Properties:
        - Name: BatchSize
        - Name: Next
        - Name: LambdaName
        - Name: Name
    
    """
    
    BatchSize_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html#cfn-iotanalytics-pipeline-lambda-batchsize""", alias="BatchSize")
    Next_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html#cfn-iotanalytics-pipeline-lambda-next""", alias="Next")
    LambdaName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html#cfn-iotanalytics-pipeline-lambda-lambdaname""", alias="LambdaName")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html#cfn-iotanalytics-pipeline-lambda-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.Lambda:
        from troposphere.iotanalytics import Lambda as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Math(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html
    Properties:
        - Name: Attribute
        - Name: Next
        - Name: Math
        - Name: Name
    
    """
    
    Attribute_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html#cfn-iotanalytics-pipeline-math-attribute""", alias="Attribute")
    Next_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html#cfn-iotanalytics-pipeline-math-next""", alias="Next")
    Math_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html#cfn-iotanalytics-pipeline-math-math""", alias="Math")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html#cfn-iotanalytics-pipeline-math-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.Math:
        from troposphere.iotanalytics import Math as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RemoveAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html
    Properties:
        - Name: Next
        - Name: Attributes
        - Name: Name
    
    """
    
    Next_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html#cfn-iotanalytics-pipeline-removeattributes-next""", alias="Next")
    Attributes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html#cfn-iotanalytics-pipeline-removeattributes-attributes""", alias="Attributes")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html#cfn-iotanalytics-pipeline-removeattributes-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.RemoveAttributes:
        from troposphere.iotanalytics import RemoveAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SelectAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html
    Properties:
        - Name: Next
        - Name: Attributes
        - Name: Name
    
    """
    
    Next_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html#cfn-iotanalytics-pipeline-selectattributes-next""", alias="Next")
    Attributes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html#cfn-iotanalytics-pipeline-selectattributes-attributes""", alias="Attributes")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html#cfn-iotanalytics-pipeline-selectattributes-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotanalytics.SelectAttributes:
        from troposphere.iotanalytics import SelectAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Channel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html
    Properties:
        - Name: ChannelName
        - Name: ChannelStorage
        - Name: RetentionPeriod
        - Name: Tags
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ChannelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-channelname""", alias="ChannelName")
    ChannelStorage_: Optional['ChannelStorage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-channelstorage""", alias="ChannelStorage")
    RetentionPeriod_: Optional['RetentionPeriod'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-retentionperiod""", alias="RetentionPeriod")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotanalytics.Channel:
        from troposphere.iotanalytics import Channel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotanalytics import Channel as TropoT
        return resource_to_troposphere(self, TropoT)


class Dataset(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html
    Properties:
        - Name: Actions
        - Name: LateDataRules
        - Name: DatasetName
        - Name: ContentDeliveryRules
        - Name: Triggers
        - Name: VersioningConfiguration
        - Name: RetentionPeriod
        - Name: Tags
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Actions_: List['Action'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-actions""", alias="Actions")
    LateDataRules_: Optional[List['LateDataRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-latedatarules""", alias="LateDataRules")
    DatasetName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-datasetname""", alias="DatasetName")
    ContentDeliveryRules_: Optional[List['DatasetContentDeliveryRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-contentdeliveryrules""", alias="ContentDeliveryRules")
    Triggers_: Optional[List['Trigger']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-triggers""", alias="Triggers")
    VersioningConfiguration_: Optional['VersioningConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-versioningconfiguration""", alias="VersioningConfiguration")
    RetentionPeriod_: Optional['RetentionPeriod'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-retentionperiod""", alias="RetentionPeriod")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotanalytics.Dataset:
        from troposphere.iotanalytics import Dataset as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotanalytics import Dataset as TropoT
        return resource_to_troposphere(self, TropoT)


class Datastore(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html
    Properties:
        - Name: DatastoreStorage
        - Name: FileFormatConfiguration
        - Name: DatastorePartitions
        - Name: DatastoreName
        - Name: RetentionPeriod
        - Name: Tags
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DatastoreStorage_: Optional['DatastoreStorage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-datastorestorage""", alias="DatastoreStorage")
    FileFormatConfiguration_: Optional['FileFormatConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-fileformatconfiguration""", alias="FileFormatConfiguration")
    DatastorePartitions_: Optional['DatastorePartitions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-datastorepartitions""", alias="DatastorePartitions")
    DatastoreName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-datastorename""", alias="DatastoreName")
    RetentionPeriod_: Optional['RetentionPeriod'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-retentionperiod""", alias="RetentionPeriod")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotanalytics.Datastore:
        from troposphere.iotanalytics import Datastore as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotanalytics import Datastore as TropoT
        return resource_to_troposphere(self, TropoT)


class Pipeline(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html
    Properties:
        - Name: PipelineName
        - Name: Tags
        - Name: PipelineActivities
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PipelineName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html#cfn-iotanalytics-pipeline-pipelinename""", alias="PipelineName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html#cfn-iotanalytics-pipeline-tags""", alias="Tags")
    PipelineActivities_: List['Activity'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html#cfn-iotanalytics-pipeline-pipelineactivities""", alias="PipelineActivities")
    

    @property
    def tropo_type(self) -> troposphere.iotanalytics.Pipeline:
        from troposphere.iotanalytics import Pipeline as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotanalytics import Pipeline as TropoT
        return resource_to_troposphere(self, TropoT)

