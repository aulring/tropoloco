from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CollectionScheme(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html
    Properties:
        - Name: TimeBasedCollectionScheme
        - Name: ConditionBasedCollectionScheme
    
    """
    
    TimeBasedCollectionScheme_: Optional['TimeBasedCollectionScheme'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html#cfn-iotfleetwise-campaign-collectionscheme-timebasedcollectionscheme""", alias="TimeBasedCollectionScheme")
    ConditionBasedCollectionScheme_: Optional['ConditionBasedCollectionScheme'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html#cfn-iotfleetwise-campaign-collectionscheme-conditionbasedcollectionscheme""", alias="ConditionBasedCollectionScheme")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.CollectionScheme:
        from troposphere.iotfleetwise import CollectionScheme as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConditionBasedCollectionScheme(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html
    Properties:
        - Name: MinimumTriggerIntervalMs
        - Name: Expression
        - Name: TriggerMode
        - Name: ConditionLanguageVersion
    
    """
    
    MinimumTriggerIntervalMs_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-minimumtriggerintervalms""", alias="MinimumTriggerIntervalMs")
    Expression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-expression""", alias="Expression")
    TriggerMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-triggermode""", alias="TriggerMode")
    ConditionLanguageVersion_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-conditionlanguageversion""", alias="ConditionLanguageVersion")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.ConditionBasedCollectionScheme:
        from troposphere.iotfleetwise import ConditionBasedCollectionScheme as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataDestinationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-datadestinationconfig.html
    Properties:
        - Name: S3Config
        - Name: TimestreamConfig
    
    """
    
    S3Config_: Optional['S3Config'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-datadestinationconfig.html#cfn-iotfleetwise-campaign-datadestinationconfig-s3config""", alias="S3Config")
    TimestreamConfig_: Optional['TimestreamConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-datadestinationconfig.html#cfn-iotfleetwise-campaign-datadestinationconfig-timestreamconfig""", alias="TimestreamConfig")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.DataDestinationConfig:
        from troposphere.iotfleetwise import DataDestinationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Config(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-s3config.html
    Properties:
        - Name: BucketArn
        - Name: DataFormat
        - Name: StorageCompressionFormat
        - Name: Prefix
    
    """
    
    BucketArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-s3config.html#cfn-iotfleetwise-campaign-s3config-bucketarn""", alias="BucketArn")
    DataFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-s3config.html#cfn-iotfleetwise-campaign-s3config-dataformat""", alias="DataFormat")
    StorageCompressionFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-s3config.html#cfn-iotfleetwise-campaign-s3config-storagecompressionformat""", alias="StorageCompressionFormat")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-s3config.html#cfn-iotfleetwise-campaign-s3config-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.S3Config:
        from troposphere.iotfleetwise import S3Config as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SignalInformation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html
    Properties:
        - Name: MaxSampleCount
        - Name: MinimumSamplingIntervalMs
        - Name: Name
    
    """
    
    MaxSampleCount_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html#cfn-iotfleetwise-campaign-signalinformation-maxsamplecount""", alias="MaxSampleCount")
    MinimumSamplingIntervalMs_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html#cfn-iotfleetwise-campaign-signalinformation-minimumsamplingintervalms""", alias="MinimumSamplingIntervalMs")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html#cfn-iotfleetwise-campaign-signalinformation-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.SignalInformation:
        from troposphere.iotfleetwise import SignalInformation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimeBasedCollectionScheme(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timebasedcollectionscheme.html
    Properties:
        - Name: PeriodMs
    
    """
    
    PeriodMs_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timebasedcollectionscheme.html#cfn-iotfleetwise-campaign-timebasedcollectionscheme-periodms""", alias="PeriodMs")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.TimeBasedCollectionScheme:
        from troposphere.iotfleetwise import TimeBasedCollectionScheme as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TimestreamConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timestreamconfig.html
    Properties:
        - Name: ExecutionRoleArn
        - Name: TimestreamTableArn
    
    """
    
    ExecutionRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timestreamconfig.html#cfn-iotfleetwise-campaign-timestreamconfig-executionrolearn""", alias="ExecutionRoleArn")
    TimestreamTableArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timestreamconfig.html#cfn-iotfleetwise-campaign-timestreamconfig-timestreamtablearn""", alias="TimestreamTableArn")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.TimestreamConfig:
        from troposphere.iotfleetwise import TimestreamConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CanInterface(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html
    Properties:
        - Name: ProtocolName
        - Name: ProtocolVersion
        - Name: Name
    
    """
    
    ProtocolName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html#cfn-iotfleetwise-decodermanifest-caninterface-protocolname""", alias="ProtocolName")
    ProtocolVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html#cfn-iotfleetwise-decodermanifest-caninterface-protocolversion""", alias="ProtocolVersion")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html#cfn-iotfleetwise-decodermanifest-caninterface-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.CanInterface:
        from troposphere.iotfleetwise import CanInterface as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CanSignal(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html
    Properties:
        - Name: IsBigEndian
        - Name: Length
        - Name: Factor
        - Name: IsSigned
        - Name: StartBit
        - Name: MessageId
        - Name: Offset
        - Name: Name
    
    """
    
    IsBigEndian_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-isbigendian""", alias="IsBigEndian")
    Length_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-length""", alias="Length")
    Factor_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-factor""", alias="Factor")
    IsSigned_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-issigned""", alias="IsSigned")
    StartBit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-startbit""", alias="StartBit")
    MessageId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-messageid""", alias="MessageId")
    Offset_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-offset""", alias="Offset")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.CanSignal:
        from troposphere.iotfleetwise import CanSignal as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkInterfacesItems(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html
    Properties:
        - Name: Type
        - Name: CanInterface
        - Name: InterfaceId
        - Name: ObdInterface
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-type""", alias="Type")
    CanInterface_: Optional['CanInterface'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-caninterface""", alias="CanInterface")
    InterfaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-interfaceid""", alias="InterfaceId")
    ObdInterface_: Optional['ObdInterface'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-obdinterface""", alias="ObdInterface")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.NetworkInterfacesItems:
        from troposphere.iotfleetwise import NetworkInterfacesItems as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ObdInterface(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html
    Properties:
        - Name: HasTransmissionEcu
        - Name: PidRequestIntervalSeconds
        - Name: UseExtendedIds
        - Name: RequestMessageId
        - Name: ObdStandard
        - Name: Name
        - Name: DtcRequestIntervalSeconds
    
    """
    
    HasTransmissionEcu_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-hastransmissionecu""", alias="HasTransmissionEcu")
    PidRequestIntervalSeconds_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-pidrequestintervalseconds""", alias="PidRequestIntervalSeconds")
    UseExtendedIds_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-useextendedids""", alias="UseExtendedIds")
    RequestMessageId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-requestmessageid""", alias="RequestMessageId")
    ObdStandard_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-obdstandard""", alias="ObdStandard")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-name""", alias="Name")
    DtcRequestIntervalSeconds_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-dtcrequestintervalseconds""", alias="DtcRequestIntervalSeconds")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.ObdInterface:
        from troposphere.iotfleetwise import ObdInterface as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ObdSignal(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html
    Properties:
        - Name: BitRightShift
        - Name: BitMaskLength
        - Name: StartByte
        - Name: ByteLength
        - Name: PidResponseLength
        - Name: Scaling
        - Name: Pid
        - Name: ServiceMode
        - Name: Offset
    
    """
    
    BitRightShift_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-bitrightshift""", alias="BitRightShift")
    BitMaskLength_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-bitmasklength""", alias="BitMaskLength")
    StartByte_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-startbyte""", alias="StartByte")
    ByteLength_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-bytelength""", alias="ByteLength")
    PidResponseLength_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-pidresponselength""", alias="PidResponseLength")
    Scaling_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-scaling""", alias="Scaling")
    Pid_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-pid""", alias="Pid")
    ServiceMode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-servicemode""", alias="ServiceMode")
    Offset_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-offset""", alias="Offset")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.ObdSignal:
        from troposphere.iotfleetwise import ObdSignal as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SignalDecodersItems(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html
    Properties:
        - Name: Type
        - Name: ObdSignal
        - Name: FullyQualifiedName
        - Name: CanSignal
        - Name: InterfaceId
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-type""", alias="Type")
    ObdSignal_: Optional['ObdSignal'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-obdsignal""", alias="ObdSignal")
    FullyQualifiedName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-fullyqualifiedname""", alias="FullyQualifiedName")
    CanSignal_: Optional['CanSignal'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-cansignal""", alias="CanSignal")
    InterfaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-interfaceid""", alias="InterfaceId")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.SignalDecodersItems:
        from troposphere.iotfleetwise import SignalDecodersItems as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Actuator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html
    Properties:
        - Name: Description
        - Name: AllowedValues
        - Name: Min
        - Name: Max
        - Name: FullyQualifiedName
        - Name: AssignedValue
        - Name: DataType
        - Name: Unit
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-description""", alias="Description")
    AllowedValues_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-allowedvalues""", alias="AllowedValues")
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-max""", alias="Max")
    FullyQualifiedName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-fullyqualifiedname""", alias="FullyQualifiedName")
    AssignedValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-assignedvalue""", alias="AssignedValue")
    DataType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-datatype""", alias="DataType")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.Actuator:
        from troposphere.iotfleetwise import Actuator as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Attribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html
    Properties:
        - Name: DefaultValue
        - Name: Description
        - Name: AllowedValues
        - Name: Min
        - Name: Max
        - Name: FullyQualifiedName
        - Name: AssignedValue
        - Name: DataType
        - Name: Unit
    
    """
    
    DefaultValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-defaultvalue""", alias="DefaultValue")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-description""", alias="Description")
    AllowedValues_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-allowedvalues""", alias="AllowedValues")
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-max""", alias="Max")
    FullyQualifiedName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-fullyqualifiedname""", alias="FullyQualifiedName")
    AssignedValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-assignedvalue""", alias="AssignedValue")
    DataType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-datatype""", alias="DataType")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.Attribute:
        from troposphere.iotfleetwise import Attribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Branch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html
    Properties:
        - Name: Description
        - Name: FullyQualifiedName
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html#cfn-iotfleetwise-signalcatalog-branch-description""", alias="Description")
    FullyQualifiedName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html#cfn-iotfleetwise-signalcatalog-branch-fullyqualifiedname""", alias="FullyQualifiedName")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.Branch:
        from troposphere.iotfleetwise import Branch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Node(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html
    Properties:
        - Name: Attribute
        - Name: Branch
        - Name: Sensor
        - Name: Actuator
    
    """
    
    Attribute_: Optional['Attribute'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-attribute""", alias="Attribute")
    Branch_: Optional['Branch'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-branch""", alias="Branch")
    Sensor_: Optional['Sensor'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-sensor""", alias="Sensor")
    Actuator_: Optional['Actuator'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-actuator""", alias="Actuator")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.Node:
        from troposphere.iotfleetwise import Node as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NodeCounts(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html
    Properties:
        - Name: TotalActuators
        - Name: TotalNodes
        - Name: TotalAttributes
        - Name: TotalBranches
        - Name: TotalSensors
    
    """
    
    TotalActuators_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalactuators""", alias="TotalActuators")
    TotalNodes_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalnodes""", alias="TotalNodes")
    TotalAttributes_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalattributes""", alias="TotalAttributes")
    TotalBranches_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalbranches""", alias="TotalBranches")
    TotalSensors_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalsensors""", alias="TotalSensors")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.NodeCounts:
        from troposphere.iotfleetwise import NodeCounts as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Sensor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html
    Properties:
        - Name: Description
        - Name: AllowedValues
        - Name: Min
        - Name: Max
        - Name: FullyQualifiedName
        - Name: DataType
        - Name: Unit
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-description""", alias="Description")
    AllowedValues_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-allowedvalues""", alias="AllowedValues")
    Min_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-min""", alias="Min")
    Max_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-max""", alias="Max")
    FullyQualifiedName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-fullyqualifiedname""", alias="FullyQualifiedName")
    DataType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-datatype""", alias="DataType")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.iotfleetwise.Sensor:
        from troposphere.iotfleetwise import Sensor as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Campaign(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html
    Properties:
        - Name: Action
        - Name: Compression
        - Name: Description
        - Name: Priority
        - Name: SignalsToCollect
        - Name: StartTime
        - Name: ExpiryTime
        - Name: SpoolingMode
        - Name: DataDestinationConfigs
        - Name: SignalCatalogArn
        - Name: Name
        - Name: PostTriggerCollectionDuration
        - Name: DataExtraDimensions
        - Name: DiagnosticsMode
        - Name: TargetArn
        - Name: CollectionScheme
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: LastModificationTime
        - Name: CreationTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-action""", alias="Action")
    Compression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-compression""", alias="Compression")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-description""", alias="Description")
    Priority_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-priority""", alias="Priority")
    SignalsToCollect_: Optional[List['SignalInformation']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-signalstocollect""", alias="SignalsToCollect")
    StartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-starttime""", alias="StartTime")
    ExpiryTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-expirytime""", alias="ExpiryTime")
    SpoolingMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-spoolingmode""", alias="SpoolingMode")
    DataDestinationConfigs_: Optional[List['DataDestinationConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-datadestinationconfigs""", alias="DataDestinationConfigs")
    SignalCatalogArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-signalcatalogarn""", alias="SignalCatalogArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-name""", alias="Name")
    PostTriggerCollectionDuration_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-posttriggercollectionduration""", alias="PostTriggerCollectionDuration")
    DataExtraDimensions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-dataextradimensions""", alias="DataExtraDimensions")
    DiagnosticsMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-diagnosticsmode""", alias="DiagnosticsMode")
    TargetArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-targetarn""", alias="TargetArn")
    CollectionScheme_: 'CollectionScheme' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-collectionscheme""", alias="CollectionScheme")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotfleetwise.Campaign:
        from troposphere.iotfleetwise import Campaign as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotfleetwise import Campaign as TropoT
        return resource_to_troposphere(self, TropoT)


class DecoderManifest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html
    Properties:
        - Name: SignalDecoders
        - Name: Status
        - Name: Description
        - Name: NetworkInterfaces
        - Name: ModelManifestArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LastModificationTime
        - Name: CreationTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SignalDecoders_: Optional[List['SignalDecodersItems']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-signaldecoders""", alias="SignalDecoders")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-status""", alias="Status")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-description""", alias="Description")
    NetworkInterfaces_: Optional[List['NetworkInterfacesItems']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-networkinterfaces""", alias="NetworkInterfaces")
    ModelManifestArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-modelmanifestarn""", alias="ModelManifestArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iotfleetwise.DecoderManifest:
        from troposphere.iotfleetwise import DecoderManifest as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotfleetwise import DecoderManifest as TropoT
        return resource_to_troposphere(self, TropoT)


class Fleet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html
    Properties:
        - Name: Description
        - Name: Id
        - Name: SignalCatalogArn
        - Name: Tags
    Attributes:
        - Name: LastModificationTime
        - Name: CreationTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-description""", alias="Description")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-id""", alias="Id")
    SignalCatalogArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-signalcatalogarn""", alias="SignalCatalogArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotfleetwise.Fleet:
        from troposphere.iotfleetwise import Fleet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotfleetwise import Fleet as TropoT
        return resource_to_troposphere(self, TropoT)


class ModelManifest(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html
    Properties:
        - Name: Status
        - Name: Description
        - Name: SignalCatalogArn
        - Name: Nodes
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LastModificationTime
        - Name: CreationTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-status""", alias="Status")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-description""", alias="Description")
    SignalCatalogArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-signalcatalogarn""", alias="SignalCatalogArn")
    Nodes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-nodes""", alias="Nodes")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iotfleetwise.ModelManifest:
        from troposphere.iotfleetwise import ModelManifest as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotfleetwise import ModelManifest as TropoT
        return resource_to_troposphere(self, TropoT)


class SignalCatalog(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html
    Properties:
        - Name: Description
        - Name: NodeCounts
        - Name: Nodes
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LastModificationTime
        - Name: NodeCounts.TotalNodes
        - Name: NodeCounts.TotalSensors
        - Name: NodeCounts.TotalAttributes
        - Name: NodeCounts.TotalBranches
        - Name: NodeCounts.TotalActuators
        - Name: CreationTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-description""", alias="Description")
    NodeCounts_: Optional['NodeCounts'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-nodecounts""", alias="NodeCounts")
    Nodes_: Optional[List['Node']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-nodes""", alias="Nodes")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iotfleetwise.SignalCatalog:
        from troposphere.iotfleetwise import SignalCatalog as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotfleetwise import SignalCatalog as TropoT
        return resource_to_troposphere(self, TropoT)


class Vehicle(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html
    Properties:
        - Name: AssociationBehavior
        - Name: Attributes
        - Name: DecoderManifestArn
        - Name: ModelManifestArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LastModificationTime
        - Name: CreationTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AssociationBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-associationbehavior""", alias="AssociationBehavior")
    Attributes_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-attributes""", alias="Attributes")
    DecoderManifestArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-decodermanifestarn""", alias="DecoderManifestArn")
    ModelManifestArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-modelmanifestarn""", alias="ModelManifestArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iotfleetwise.Vehicle:
        from troposphere.iotfleetwise import Vehicle as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotfleetwise import Vehicle as TropoT
        return resource_to_troposphere(self, TropoT)

