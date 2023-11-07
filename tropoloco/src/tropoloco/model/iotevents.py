from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AcknowledgeFlow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-acknowledgeflow.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-acknowledgeflow.html#cfn-iotevents-alarmmodel-acknowledgeflow-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.AcknowledgeFlow:
        from troposphere.iotevents import AcknowledgeFlow as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AlarmAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html
    Properties:
        - Name: DynamoDBv2
        - Name: IotEvents
        - Name: IotSiteWise
        - Name: Sqs
        - Name: Firehose
        - Name: DynamoDB
        - Name: IotTopicPublish
        - Name: Sns
        - Name: Lambda
    
    """
    
    DynamoDBv2_: Optional['DynamoDBv2'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-dynamodbv2""", alias="DynamoDBv2")
    IotEvents_: Optional['IotEvents'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-iotevents""", alias="IotEvents")
    IotSiteWise_: Optional['IotSiteWise'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-iotsitewise""", alias="IotSiteWise")
    Sqs_: Optional['Sqs'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-sqs""", alias="Sqs")
    Firehose_: Optional['Firehose'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-firehose""", alias="Firehose")
    DynamoDB_: Optional['DynamoDB'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-dynamodb""", alias="DynamoDB")
    IotTopicPublish_: Optional['IotTopicPublish'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-iottopicpublish""", alias="IotTopicPublish")
    Sns_: Optional['Sns'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-sns""", alias="Sns")
    Lambda_: Optional['Lambda'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-lambda""", alias="Lambda")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.AlarmAction:
        from troposphere.iotevents import AlarmAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AlarmCapabilities(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmcapabilities.html
    Properties:
        - Name: AcknowledgeFlow
        - Name: InitializationConfiguration
    
    """
    
    AcknowledgeFlow_: Optional['AcknowledgeFlow'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmcapabilities.html#cfn-iotevents-alarmmodel-alarmcapabilities-acknowledgeflow""", alias="AcknowledgeFlow")
    InitializationConfiguration_: Optional['InitializationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmcapabilities.html#cfn-iotevents-alarmmodel-alarmcapabilities-initializationconfiguration""", alias="InitializationConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.AlarmCapabilities:
        from troposphere.iotevents import AlarmCapabilities as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AlarmEventActions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmeventactions.html
    Properties:
        - Name: AlarmActions
    
    """
    
    AlarmActions_: Optional[List['AlarmAction']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmeventactions.html#cfn-iotevents-alarmmodel-alarmeventactions-alarmactions""", alias="AlarmActions")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.AlarmEventActions:
        from troposphere.iotevents import AlarmEventActions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AlarmRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmrule.html
    Properties:
        - Name: SimpleRule
    
    """
    
    SimpleRule_: Optional['SimpleRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmrule.html#cfn-iotevents-alarmmodel-alarmrule-simplerule""", alias="SimpleRule")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.AlarmRule:
        from troposphere.iotevents import AlarmRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetPropertyTimestamp(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertytimestamp.html
    Properties:
        - Name: TimeInSeconds
        - Name: OffsetInNanos
    
    """
    
    TimeInSeconds_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertytimestamp.html#cfn-iotevents-alarmmodel-assetpropertytimestamp-timeinseconds""", alias="TimeInSeconds")
    OffsetInNanos_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertytimestamp.html#cfn-iotevents-alarmmodel-assetpropertytimestamp-offsetinnanos""", alias="OffsetInNanos")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.AssetPropertyTimestamp:
        from troposphere.iotevents import AssetPropertyTimestamp as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetPropertyValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvalue.html
    Properties:
        - Name: Quality
        - Name: Value
        - Name: Timestamp
    
    """
    
    Quality_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvalue.html#cfn-iotevents-alarmmodel-assetpropertyvalue-quality""", alias="Quality")
    Value_: 'AssetPropertyVariant' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvalue.html#cfn-iotevents-alarmmodel-assetpropertyvalue-value""", alias="Value")
    Timestamp_: Optional['AssetPropertyTimestamp'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvalue.html#cfn-iotevents-alarmmodel-assetpropertyvalue-timestamp""", alias="Timestamp")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.AssetPropertyValue:
        from troposphere.iotevents import AssetPropertyValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetPropertyVariant(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvariant.html
    Properties:
        - Name: DoubleValue
        - Name: BooleanValue
        - Name: IntegerValue
        - Name: StringValue
    
    """
    
    DoubleValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvariant.html#cfn-iotevents-alarmmodel-assetpropertyvariant-doublevalue""", alias="DoubleValue")
    BooleanValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvariant.html#cfn-iotevents-alarmmodel-assetpropertyvariant-booleanvalue""", alias="BooleanValue")
    IntegerValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvariant.html#cfn-iotevents-alarmmodel-assetpropertyvariant-integervalue""", alias="IntegerValue")
    StringValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvariant.html#cfn-iotevents-alarmmodel-assetpropertyvariant-stringvalue""", alias="StringValue")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.AssetPropertyVariant:
        from troposphere.iotevents import AssetPropertyVariant as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynamoDB(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html
    Properties:
        - Name: TableName
        - Name: PayloadField
        - Name: RangeKeyField
        - Name: HashKeyField
        - Name: RangeKeyValue
        - Name: RangeKeyType
        - Name: HashKeyType
        - Name: HashKeyValue
        - Name: Payload
        - Name: Operation
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-tablename""", alias="TableName")
    PayloadField_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-payloadfield""", alias="PayloadField")
    RangeKeyField_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-rangekeyfield""", alias="RangeKeyField")
    HashKeyField_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-hashkeyfield""", alias="HashKeyField")
    RangeKeyValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-rangekeyvalue""", alias="RangeKeyValue")
    RangeKeyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-rangekeytype""", alias="RangeKeyType")
    HashKeyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-hashkeytype""", alias="HashKeyType")
    HashKeyValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-hashkeyvalue""", alias="HashKeyValue")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-payload""", alias="Payload")
    Operation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-operation""", alias="Operation")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.DynamoDB:
        from troposphere.iotevents import DynamoDB as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynamoDBv2(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodbv2.html
    Properties:
        - Name: TableName
        - Name: Payload
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodbv2.html#cfn-iotevents-alarmmodel-dynamodbv2-tablename""", alias="TableName")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodbv2.html#cfn-iotevents-alarmmodel-dynamodbv2-payload""", alias="Payload")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.DynamoDBv2:
        from troposphere.iotevents import DynamoDBv2 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Firehose(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-firehose.html
    Properties:
        - Name: DeliveryStreamName
        - Name: Payload
        - Name: Separator
    
    """
    
    DeliveryStreamName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-firehose.html#cfn-iotevents-alarmmodel-firehose-deliverystreamname""", alias="DeliveryStreamName")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-firehose.html#cfn-iotevents-alarmmodel-firehose-payload""", alias="Payload")
    Separator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-firehose.html#cfn-iotevents-alarmmodel-firehose-separator""", alias="Separator")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.Firehose:
        from troposphere.iotevents import Firehose as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InitializationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-initializationconfiguration.html
    Properties:
        - Name: DisabledOnInitialization
    
    """
    
    DisabledOnInitialization_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-initializationconfiguration.html#cfn-iotevents-alarmmodel-initializationconfiguration-disabledoninitialization""", alias="DisabledOnInitialization")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.InitializationConfiguration:
        from troposphere.iotevents import InitializationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IotEvents(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotevents.html
    Properties:
        - Name: InputName
        - Name: Payload
    
    """
    
    InputName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotevents.html#cfn-iotevents-alarmmodel-iotevents-inputname""", alias="InputName")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotevents.html#cfn-iotevents-alarmmodel-iotevents-payload""", alias="Payload")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.IotEvents:
        from troposphere.iotevents import IotEvents as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IotSiteWise(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotsitewise.html
    Properties:
        - Name: EntryId
        - Name: PropertyAlias
        - Name: PropertyValue
        - Name: AssetId
        - Name: PropertyId
    
    """
    
    EntryId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotsitewise.html#cfn-iotevents-alarmmodel-iotsitewise-entryid""", alias="EntryId")
    PropertyAlias_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotsitewise.html#cfn-iotevents-alarmmodel-iotsitewise-propertyalias""", alias="PropertyAlias")
    PropertyValue_: Optional['AssetPropertyValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotsitewise.html#cfn-iotevents-alarmmodel-iotsitewise-propertyvalue""", alias="PropertyValue")
    AssetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotsitewise.html#cfn-iotevents-alarmmodel-iotsitewise-assetid""", alias="AssetId")
    PropertyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotsitewise.html#cfn-iotevents-alarmmodel-iotsitewise-propertyid""", alias="PropertyId")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.IotSiteWise:
        from troposphere.iotevents import IotSiteWise as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IotTopicPublish(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iottopicpublish.html
    Properties:
        - Name: MqttTopic
        - Name: Payload
    
    """
    
    MqttTopic_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iottopicpublish.html#cfn-iotevents-alarmmodel-iottopicpublish-mqtttopic""", alias="MqttTopic")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iottopicpublish.html#cfn-iotevents-alarmmodel-iottopicpublish-payload""", alias="Payload")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.IotTopicPublish:
        from troposphere.iotevents import IotTopicPublish as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Lambda(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-lambda.html
    Properties:
        - Name: FunctionArn
        - Name: Payload
    
    """
    
    FunctionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-lambda.html#cfn-iotevents-alarmmodel-lambda-functionarn""", alias="FunctionArn")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-lambda.html#cfn-iotevents-alarmmodel-lambda-payload""", alias="Payload")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.Lambda:
        from troposphere.iotevents import Lambda as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Payload(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-payload.html
    Properties:
        - Name: ContentExpression
        - Name: Type
    
    """
    
    ContentExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-payload.html#cfn-iotevents-alarmmodel-payload-contentexpression""", alias="ContentExpression")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-payload.html#cfn-iotevents-alarmmodel-payload-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.Payload:
        from troposphere.iotevents import Payload as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SimpleRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-simplerule.html
    Properties:
        - Name: ComparisonOperator
        - Name: InputProperty
        - Name: Threshold
    
    """
    
    ComparisonOperator_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-simplerule.html#cfn-iotevents-alarmmodel-simplerule-comparisonoperator""", alias="ComparisonOperator")
    InputProperty_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-simplerule.html#cfn-iotevents-alarmmodel-simplerule-inputproperty""", alias="InputProperty")
    Threshold_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-simplerule.html#cfn-iotevents-alarmmodel-simplerule-threshold""", alias="Threshold")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.SimpleRule:
        from troposphere.iotevents import SimpleRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Sns(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sns.html
    Properties:
        - Name: TargetArn
        - Name: Payload
    
    """
    
    TargetArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sns.html#cfn-iotevents-alarmmodel-sns-targetarn""", alias="TargetArn")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sns.html#cfn-iotevents-alarmmodel-sns-payload""", alias="Payload")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.Sns:
        from troposphere.iotevents import Sns as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Sqs(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sqs.html
    Properties:
        - Name: UseBase64
        - Name: Payload
        - Name: QueueUrl
    
    """
    
    UseBase64_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sqs.html#cfn-iotevents-alarmmodel-sqs-usebase64""", alias="UseBase64")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sqs.html#cfn-iotevents-alarmmodel-sqs-payload""", alias="Payload")
    QueueUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sqs.html#cfn-iotevents-alarmmodel-sqs-queueurl""", alias="QueueUrl")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.Sqs:
        from troposphere.iotevents import Sqs as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html
    Properties:
        - Name: IotEvents
        - Name: Firehose
        - Name: DynamoDB
        - Name: IotTopicPublish
        - Name: DynamoDBv2
        - Name: IotSiteWise
        - Name: ResetTimer
        - Name: Sqs
        - Name: SetTimer
        - Name: Sns
        - Name: ClearTimer
        - Name: Lambda
        - Name: SetVariable
    
    """
    
    IotEvents_: Optional['IotEvents'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-iotevents""", alias="IotEvents")
    Firehose_: Optional['Firehose'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-firehose""", alias="Firehose")
    DynamoDB_: Optional['DynamoDB'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-dynamodb""", alias="DynamoDB")
    IotTopicPublish_: Optional['IotTopicPublish'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-iottopicpublish""", alias="IotTopicPublish")
    DynamoDBv2_: Optional['DynamoDBv2'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-dynamodbv2""", alias="DynamoDBv2")
    IotSiteWise_: Optional['IotSiteWise'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-iotsitewise""", alias="IotSiteWise")
    ResetTimer_: Optional['ResetTimer'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-resettimer""", alias="ResetTimer")
    Sqs_: Optional['Sqs'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-sqs""", alias="Sqs")
    SetTimer_: Optional['SetTimer'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-settimer""", alias="SetTimer")
    Sns_: Optional['Sns'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-sns""", alias="Sns")
    ClearTimer_: Optional['ClearTimer'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-cleartimer""", alias="ClearTimer")
    Lambda_: Optional['Lambda'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-lambda""", alias="Lambda")
    SetVariable_: Optional['SetVariable'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-setvariable""", alias="SetVariable")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.Action:
        from troposphere.iotevents import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetPropertyTimestamp(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html
    Properties:
        - Name: TimeInSeconds
        - Name: OffsetInNanos
    
    """
    
    TimeInSeconds_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html#cfn-iotevents-detectormodel-assetpropertytimestamp-timeinseconds""", alias="TimeInSeconds")
    OffsetInNanos_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html#cfn-iotevents-detectormodel-assetpropertytimestamp-offsetinnanos""", alias="OffsetInNanos")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.AssetPropertyTimestamp:
        from troposphere.iotevents import AssetPropertyTimestamp as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetPropertyValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html
    Properties:
        - Name: Quality
        - Name: Value
        - Name: Timestamp
    
    """
    
    Quality_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html#cfn-iotevents-detectormodel-assetpropertyvalue-quality""", alias="Quality")
    Value_: 'AssetPropertyVariant' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html#cfn-iotevents-detectormodel-assetpropertyvalue-value""", alias="Value")
    Timestamp_: Optional['AssetPropertyTimestamp'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html#cfn-iotevents-detectormodel-assetpropertyvalue-timestamp""", alias="Timestamp")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.AssetPropertyValue:
        from troposphere.iotevents import AssetPropertyValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssetPropertyVariant(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html
    Properties:
        - Name: DoubleValue
        - Name: BooleanValue
        - Name: IntegerValue
        - Name: StringValue
    
    """
    
    DoubleValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html#cfn-iotevents-detectormodel-assetpropertyvariant-doublevalue""", alias="DoubleValue")
    BooleanValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html#cfn-iotevents-detectormodel-assetpropertyvariant-booleanvalue""", alias="BooleanValue")
    IntegerValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html#cfn-iotevents-detectormodel-assetpropertyvariant-integervalue""", alias="IntegerValue")
    StringValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html#cfn-iotevents-detectormodel-assetpropertyvariant-stringvalue""", alias="StringValue")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.AssetPropertyVariant:
        from troposphere.iotevents import AssetPropertyVariant as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ClearTimer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-cleartimer.html
    Properties:
        - Name: TimerName
    
    """
    
    TimerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-cleartimer.html#cfn-iotevents-detectormodel-cleartimer-timername""", alias="TimerName")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.ClearTimer:
        from troposphere.iotevents import ClearTimer as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DetectorModelDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html
    Properties:
        - Name: States
        - Name: InitialStateName
    
    """
    
    States_: List['State'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html#cfn-iotevents-detectormodel-detectormodeldefinition-states""", alias="States")
    InitialStateName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html#cfn-iotevents-detectormodel-detectormodeldefinition-initialstatename""", alias="InitialStateName")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.DetectorModelDefinition:
        from troposphere.iotevents import DetectorModelDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynamoDB(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html
    Properties:
        - Name: TableName
        - Name: PayloadField
        - Name: RangeKeyField
        - Name: HashKeyField
        - Name: RangeKeyValue
        - Name: RangeKeyType
        - Name: HashKeyType
        - Name: HashKeyValue
        - Name: Payload
        - Name: Operation
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-tablename""", alias="TableName")
    PayloadField_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-payloadfield""", alias="PayloadField")
    RangeKeyField_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-rangekeyfield""", alias="RangeKeyField")
    HashKeyField_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-hashkeyfield""", alias="HashKeyField")
    RangeKeyValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-rangekeyvalue""", alias="RangeKeyValue")
    RangeKeyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-rangekeytype""", alias="RangeKeyType")
    HashKeyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-hashkeytype""", alias="HashKeyType")
    HashKeyValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-hashkeyvalue""", alias="HashKeyValue")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-payload""", alias="Payload")
    Operation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-operation""", alias="Operation")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.DynamoDB:
        from troposphere.iotevents import DynamoDB as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynamoDBv2(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html
    Properties:
        - Name: TableName
        - Name: Payload
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html#cfn-iotevents-detectormodel-dynamodbv2-tablename""", alias="TableName")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html#cfn-iotevents-detectormodel-dynamodbv2-payload""", alias="Payload")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.DynamoDBv2:
        from troposphere.iotevents import DynamoDBv2 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Event(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html
    Properties:
        - Name: Condition
        - Name: Actions
        - Name: EventName
    
    """
    
    Condition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html#cfn-iotevents-detectormodel-event-condition""", alias="Condition")
    Actions_: Optional[List['Action']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html#cfn-iotevents-detectormodel-event-actions""", alias="Actions")
    EventName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html#cfn-iotevents-detectormodel-event-eventname""", alias="EventName")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.Event:
        from troposphere.iotevents import Event as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Firehose(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html
    Properties:
        - Name: DeliveryStreamName
        - Name: Payload
        - Name: Separator
    
    """
    
    DeliveryStreamName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html#cfn-iotevents-detectormodel-firehose-deliverystreamname""", alias="DeliveryStreamName")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html#cfn-iotevents-detectormodel-firehose-payload""", alias="Payload")
    Separator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html#cfn-iotevents-detectormodel-firehose-separator""", alias="Separator")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.Firehose:
        from troposphere.iotevents import Firehose as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IotEvents(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html
    Properties:
        - Name: InputName
        - Name: Payload
    
    """
    
    InputName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html#cfn-iotevents-detectormodel-iotevents-inputname""", alias="InputName")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html#cfn-iotevents-detectormodel-iotevents-payload""", alias="Payload")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.IotEvents:
        from troposphere.iotevents import IotEvents as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IotSiteWise(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html
    Properties:
        - Name: EntryId
        - Name: PropertyAlias
        - Name: PropertyValue
        - Name: AssetId
        - Name: PropertyId
    
    """
    
    EntryId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-entryid""", alias="EntryId")
    PropertyAlias_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-propertyalias""", alias="PropertyAlias")
    PropertyValue_: 'AssetPropertyValue' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-propertyvalue""", alias="PropertyValue")
    AssetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-assetid""", alias="AssetId")
    PropertyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-propertyid""", alias="PropertyId")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.IotSiteWise:
        from troposphere.iotevents import IotSiteWise as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IotTopicPublish(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html
    Properties:
        - Name: MqttTopic
        - Name: Payload
    
    """
    
    MqttTopic_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html#cfn-iotevents-detectormodel-iottopicpublish-mqtttopic""", alias="MqttTopic")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html#cfn-iotevents-detectormodel-iottopicpublish-payload""", alias="Payload")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.IotTopicPublish:
        from troposphere.iotevents import IotTopicPublish as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Lambda(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html
    Properties:
        - Name: FunctionArn
        - Name: Payload
    
    """
    
    FunctionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html#cfn-iotevents-detectormodel-lambda-functionarn""", alias="FunctionArn")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html#cfn-iotevents-detectormodel-lambda-payload""", alias="Payload")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.Lambda:
        from troposphere.iotevents import Lambda as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnEnter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onenter.html
    Properties:
        - Name: Events
    
    """
    
    Events_: Optional[List['Event']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onenter.html#cfn-iotevents-detectormodel-onenter-events""", alias="Events")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.OnEnter:
        from troposphere.iotevents import OnEnter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnExit(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onexit.html
    Properties:
        - Name: Events
    
    """
    
    Events_: Optional[List['Event']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onexit.html#cfn-iotevents-detectormodel-onexit-events""", alias="Events")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.OnExit:
        from troposphere.iotevents import OnExit as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OnInput(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html
    Properties:
        - Name: Events
        - Name: TransitionEvents
    
    """
    
    Events_: Optional[List['Event']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html#cfn-iotevents-detectormodel-oninput-events""", alias="Events")
    TransitionEvents_: Optional[List['TransitionEvent']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html#cfn-iotevents-detectormodel-oninput-transitionevents""", alias="TransitionEvents")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.OnInput:
        from troposphere.iotevents import OnInput as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Payload(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html
    Properties:
        - Name: ContentExpression
        - Name: Type
    
    """
    
    ContentExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html#cfn-iotevents-detectormodel-payload-contentexpression""", alias="ContentExpression")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html#cfn-iotevents-detectormodel-payload-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.Payload:
        from troposphere.iotevents import Payload as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResetTimer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-resettimer.html
    Properties:
        - Name: TimerName
    
    """
    
    TimerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-resettimer.html#cfn-iotevents-detectormodel-resettimer-timername""", alias="TimerName")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.ResetTimer:
        from troposphere.iotevents import ResetTimer as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SetTimer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html
    Properties:
        - Name: Seconds
        - Name: TimerName
        - Name: DurationExpression
    
    """
    
    Seconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html#cfn-iotevents-detectormodel-settimer-seconds""", alias="Seconds")
    TimerName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html#cfn-iotevents-detectormodel-settimer-timername""", alias="TimerName")
    DurationExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html#cfn-iotevents-detectormodel-settimer-durationexpression""", alias="DurationExpression")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.SetTimer:
        from troposphere.iotevents import SetTimer as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SetVariable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html
    Properties:
        - Name: Value
        - Name: VariableName
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html#cfn-iotevents-detectormodel-setvariable-value""", alias="Value")
    VariableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html#cfn-iotevents-detectormodel-setvariable-variablename""", alias="VariableName")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.SetVariable:
        from troposphere.iotevents import SetVariable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Sns(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html
    Properties:
        - Name: TargetArn
        - Name: Payload
    
    """
    
    TargetArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html#cfn-iotevents-detectormodel-sns-targetarn""", alias="TargetArn")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html#cfn-iotevents-detectormodel-sns-payload""", alias="Payload")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.Sns:
        from troposphere.iotevents import Sns as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Sqs(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html
    Properties:
        - Name: UseBase64
        - Name: Payload
        - Name: QueueUrl
    
    """
    
    UseBase64_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html#cfn-iotevents-detectormodel-sqs-usebase64""", alias="UseBase64")
    Payload_: Optional['Payload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html#cfn-iotevents-detectormodel-sqs-payload""", alias="Payload")
    QueueUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html#cfn-iotevents-detectormodel-sqs-queueurl""", alias="QueueUrl")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.Sqs:
        from troposphere.iotevents import Sqs as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class State(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html
    Properties:
        - Name: OnInput
        - Name: OnExit
        - Name: StateName
        - Name: OnEnter
    
    """
    
    OnInput_: Optional['OnInput'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html#cfn-iotevents-detectormodel-state-oninput""", alias="OnInput")
    OnExit_: Optional['OnExit'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html#cfn-iotevents-detectormodel-state-onexit""", alias="OnExit")
    StateName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html#cfn-iotevents-detectormodel-state-statename""", alias="StateName")
    OnEnter_: Optional['OnEnter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html#cfn-iotevents-detectormodel-state-onenter""", alias="OnEnter")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.State:
        from troposphere.iotevents import State as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TransitionEvent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html
    Properties:
        - Name: Condition
        - Name: Actions
        - Name: NextState
        - Name: EventName
    
    """
    
    Condition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html#cfn-iotevents-detectormodel-transitionevent-condition""", alias="Condition")
    Actions_: Optional[List['Action']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html#cfn-iotevents-detectormodel-transitionevent-actions""", alias="Actions")
    NextState_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html#cfn-iotevents-detectormodel-transitionevent-nextstate""", alias="NextState")
    EventName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html#cfn-iotevents-detectormodel-transitionevent-eventname""", alias="EventName")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.TransitionEvent:
        from troposphere.iotevents import TransitionEvent as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Attribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-attribute.html
    Properties:
        - Name: JsonPath
    
    """
    
    JsonPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-attribute.html#cfn-iotevents-input-attribute-jsonpath""", alias="JsonPath")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.Attribute:
        from troposphere.iotevents import Attribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-inputdefinition.html
    Properties:
        - Name: Attributes
    
    """
    
    Attributes_: List['Attribute'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-inputdefinition.html#cfn-iotevents-input-inputdefinition-attributes""", alias="Attributes")
    


    @property
    def tropo_type(self) -> troposphere.iotevents.InputDefinition:
        from troposphere.iotevents import InputDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AlarmModel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html
    Properties:
        - Name: AlarmRule
        - Name: AlarmModelName
        - Name: AlarmModelDescription
        - Name: Severity
        - Name: AlarmCapabilities
        - Name: RoleArn
        - Name: Key
        - Name: AlarmEventActions
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AlarmRule_: 'AlarmRule' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-alarmrule""", alias="AlarmRule")
    AlarmModelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-alarmmodelname""", alias="AlarmModelName")
    AlarmModelDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-alarmmodeldescription""", alias="AlarmModelDescription")
    Severity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-severity""", alias="Severity")
    AlarmCapabilities_: Optional['AlarmCapabilities'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-alarmcapabilities""", alias="AlarmCapabilities")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-rolearn""", alias="RoleArn")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-key""", alias="Key")
    AlarmEventActions_: Optional['AlarmEventActions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-alarmeventactions""", alias="AlarmEventActions")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotevents.AlarmModel:
        from troposphere.iotevents import AlarmModel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotevents import AlarmModel as TropoT
        return resource_to_troposphere(self, TropoT)


class DetectorModel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html
    Properties:
        - Name: DetectorModelDefinition
        - Name: EvaluationMethod
        - Name: DetectorModelName
        - Name: DetectorModelDescription
        - Name: Key
        - Name: RoleArn
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DetectorModelDefinition_: 'DetectorModelDefinition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-detectormodeldefinition""", alias="DetectorModelDefinition")
    EvaluationMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-evaluationmethod""", alias="EvaluationMethod")
    DetectorModelName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-detectormodelname""", alias="DetectorModelName")
    DetectorModelDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-detectormodeldescription""", alias="DetectorModelDescription")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-key""", alias="Key")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotevents.DetectorModel:
        from troposphere.iotevents import DetectorModel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotevents import DetectorModel as TropoT
        return resource_to_troposphere(self, TropoT)


class Input(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html
    Properties:
        - Name: InputDefinition
        - Name: InputName
        - Name: InputDescription
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InputDefinition_: 'InputDefinition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-inputdefinition""", alias="InputDefinition")
    InputName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-inputname""", alias="InputName")
    InputDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-inputdescription""", alias="InputDescription")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotevents.Input:
        from troposphere.iotevents import Input as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotevents import Input as TropoT
        return resource_to_troposphere(self, TropoT)

