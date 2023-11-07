from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class LoRaWANDeviceProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html
    Properties:
        - Name: PingSlotPeriod
        - Name: ClassCTimeout
        - Name: RxFreq2
        - Name: RfRegion
        - Name: ClassBTimeout
        - Name: RxDelay1
        - Name: SupportsClassC
        - Name: SupportsClassB
        - Name: RxDrOffset1
        - Name: MaxEirp
        - Name: FactoryPresetFreqsList
        - Name: SupportsJoin
        - Name: PingSlotDr
        - Name: MacVersion
        - Name: PingSlotFreq
        - Name: RegParamsRevision
        - Name: RxDataRate2
        - Name: Supports32BitFCnt
        - Name: MaxDutyCycle
    
    """
    
    PingSlotPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotperiod""", alias="PingSlotPeriod")
    ClassCTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classctimeout""", alias="ClassCTimeout")
    RxFreq2_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxfreq2""", alias="RxFreq2")
    RfRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rfregion""", alias="RfRegion")
    ClassBTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classbtimeout""", alias="ClassBTimeout")
    RxDelay1_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdelay1""", alias="RxDelay1")
    SupportsClassC_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassc""", alias="SupportsClassC")
    SupportsClassB_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassb""", alias="SupportsClassB")
    RxDrOffset1_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdroffset1""", alias="RxDrOffset1")
    MaxEirp_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxeirp""", alias="MaxEirp")
    FactoryPresetFreqsList_: Optional[List[int]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-factorypresetfreqslist""", alias="FactoryPresetFreqsList")
    SupportsJoin_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsjoin""", alias="SupportsJoin")
    PingSlotDr_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotdr""", alias="PingSlotDr")
    MacVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-macversion""", alias="MacVersion")
    PingSlotFreq_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotfreq""", alias="PingSlotFreq")
    RegParamsRevision_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-regparamsrevision""", alias="RegParamsRevision")
    RxDataRate2_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdatarate2""", alias="RxDataRate2")
    Supports32BitFCnt_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supports32bitfcnt""", alias="Supports32BitFCnt")
    MaxDutyCycle_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxdutycycle""", alias="MaxDutyCycle")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.LoRaWANDeviceProfile:
        from troposphere.iotwireless import LoRaWANDeviceProfile as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoRaWAN(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html
    Properties:
        - Name: RfRegion
        - Name: StartTime
    
    """
    
    RfRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html#cfn-iotwireless-fuotatask-lorawan-rfregion""", alias="RfRegion")
    StartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html#cfn-iotwireless-fuotatask-lorawan-starttime""", alias="StartTime")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.LoRaWAN:
        from troposphere.iotwireless import LoRaWAN as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoRaWAN(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html
    Properties:
        - Name: NumberOfDevicesRequested
        - Name: NumberOfDevicesInGroup
        - Name: RfRegion
        - Name: DlClass
    
    """
    
    NumberOfDevicesRequested_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesrequested""", alias="NumberOfDevicesRequested")
    NumberOfDevicesInGroup_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesingroup""", alias="NumberOfDevicesInGroup")
    RfRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-rfregion""", alias="RfRegion")
    DlClass_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-dlclass""", alias="DlClass")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.LoRaWAN:
        from troposphere.iotwireless import LoRaWAN as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TraceContent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent.html
    Properties:
        - Name: WirelessDeviceFrameInfo
        - Name: LogLevel
    
    """
    
    WirelessDeviceFrameInfo_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent.html#cfn-iotwireless-networkanalyzerconfiguration-tracecontent-wirelessdeviceframeinfo""", alias="WirelessDeviceFrameInfo")
    LogLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent.html#cfn-iotwireless-networkanalyzerconfiguration-tracecontent-loglevel""", alias="LogLevel")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.TraceContent:
        from troposphere.iotwireless import TraceContent as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SidewalkAccountInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfo.html
    Properties:
        - Name: AppServerPrivateKey
    
    """
    
    AppServerPrivateKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfo.html#cfn-iotwireless-partneraccount-sidewalkaccountinfo-appserverprivatekey""", alias="AppServerPrivateKey")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.SidewalkAccountInfo:
        from troposphere.iotwireless import SidewalkAccountInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SidewalkAccountInfoWithFingerprint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint.html
    Properties:
        - Name: Fingerprint
        - Name: AmazonId
        - Name: Arn
    
    """
    
    Fingerprint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint.html#cfn-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint-fingerprint""", alias="Fingerprint")
    AmazonId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint.html#cfn-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint-amazonid""", alias="AmazonId")
    Arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint.html#cfn-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.SidewalkAccountInfoWithFingerprint:
        from troposphere.iotwireless import SidewalkAccountInfoWithFingerprint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SidewalkUpdateAccount(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkupdateaccount.html
    Properties:
        - Name: AppServerPrivateKey
    
    """
    
    AppServerPrivateKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkupdateaccount.html#cfn-iotwireless-partneraccount-sidewalkupdateaccount-appserverprivatekey""", alias="AppServerPrivateKey")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.SidewalkUpdateAccount:
        from troposphere.iotwireless import SidewalkUpdateAccount as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoRaWANServiceProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html
    Properties:
        - Name: DlBucketSize
        - Name: MinGwDiversity
        - Name: DrMax
        - Name: ReportDevStatusMargin
        - Name: PrAllowed
        - Name: DlRate
        - Name: UlRatePolicy
        - Name: ReportDevStatusBattery
        - Name: ChannelMask
        - Name: UlRate
        - Name: AddGwMetadata
        - Name: DlRatePolicy
        - Name: HrAllowed
        - Name: DrMin
        - Name: TargetPer
        - Name: NwkGeoLoc
        - Name: DevStatusReqFreq
        - Name: UlBucketSize
        - Name: RaAllowed
    
    """
    
    DlBucketSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlbucketsize""", alias="DlBucketSize")
    MinGwDiversity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-mingwdiversity""", alias="MinGwDiversity")
    DrMax_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmax""", alias="DrMax")
    ReportDevStatusMargin_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusmargin""", alias="ReportDevStatusMargin")
    PrAllowed_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-prallowed""", alias="PrAllowed")
    DlRate_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlrate""", alias="DlRate")
    UlRatePolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulratepolicy""", alias="UlRatePolicy")
    ReportDevStatusBattery_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusbattery""", alias="ReportDevStatusBattery")
    ChannelMask_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-channelmask""", alias="ChannelMask")
    UlRate_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulrate""", alias="UlRate")
    AddGwMetadata_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-addgwmetadata""", alias="AddGwMetadata")
    DlRatePolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlratepolicy""", alias="DlRatePolicy")
    HrAllowed_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-hrallowed""", alias="HrAllowed")
    DrMin_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmin""", alias="DrMin")
    TargetPer_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-targetper""", alias="TargetPer")
    NwkGeoLoc_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-nwkgeoloc""", alias="NwkGeoLoc")
    DevStatusReqFreq_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-devstatusreqfreq""", alias="DevStatusReqFreq")
    UlBucketSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulbucketsize""", alias="UlBucketSize")
    RaAllowed_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-raallowed""", alias="RaAllowed")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.LoRaWANServiceProfile:
        from troposphere.iotwireless import LoRaWANServiceProfile as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoRaWANGatewayVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html
    Properties:
        - Name: Station
        - Name: Model
        - Name: PackageVersion
    
    """
    
    Station_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-station""", alias="Station")
    Model_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-model""", alias="Model")
    PackageVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-packageversion""", alias="PackageVersion")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.LoRaWANGatewayVersion:
        from troposphere.iotwireless import LoRaWANGatewayVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoRaWANUpdateGatewayTaskCreate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html
    Properties:
        - Name: UpdateSignature
        - Name: SigKeyCrc
        - Name: UpdateVersion
        - Name: CurrentVersion
    
    """
    
    UpdateSignature_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-updatesignature""", alias="UpdateSignature")
    SigKeyCrc_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-sigkeycrc""", alias="SigKeyCrc")
    UpdateVersion_: Optional['LoRaWANGatewayVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-updateversion""", alias="UpdateVersion")
    CurrentVersion_: Optional['LoRaWANGatewayVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-currentversion""", alias="CurrentVersion")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.LoRaWANUpdateGatewayTaskCreate:
        from troposphere.iotwireless import LoRaWANUpdateGatewayTaskCreate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoRaWANUpdateGatewayTaskEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html
    Properties:
        - Name: UpdateVersion
        - Name: CurrentVersion
    
    """
    
    UpdateVersion_: Optional['LoRaWANGatewayVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-updateversion""", alias="UpdateVersion")
    CurrentVersion_: Optional['LoRaWANGatewayVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-currentversion""", alias="CurrentVersion")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.LoRaWANUpdateGatewayTaskEntry:
        from troposphere.iotwireless import LoRaWANUpdateGatewayTaskEntry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UpdateWirelessGatewayTaskCreate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html
    Properties:
        - Name: LoRaWAN
        - Name: UpdateDataSource
        - Name: UpdateDataRole
    
    """
    
    LoRaWAN_: Optional['LoRaWANUpdateGatewayTaskCreate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-lorawan""", alias="LoRaWAN")
    UpdateDataSource_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatasource""", alias="UpdateDataSource")
    UpdateDataRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatarole""", alias="UpdateDataRole")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.UpdateWirelessGatewayTaskCreate:
        from troposphere.iotwireless import UpdateWirelessGatewayTaskCreate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AbpV10x(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html
    Properties:
        - Name: SessionKeys
        - Name: DevAddr
    
    """
    
    SessionKeys_: 'SessionKeysAbpV10x' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-sessionkeys""", alias="SessionKeys")
    DevAddr_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-devaddr""", alias="DevAddr")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.AbpV10x:
        from troposphere.iotwireless import AbpV10x as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AbpV11(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html
    Properties:
        - Name: SessionKeys
        - Name: DevAddr
    
    """
    
    SessionKeys_: 'SessionKeysAbpV11' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-sessionkeys""", alias="SessionKeys")
    DevAddr_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-devaddr""", alias="DevAddr")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.AbpV11:
        from troposphere.iotwireless import AbpV11 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoRaWANDevice(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html
    Properties:
        - Name: AbpV10x
        - Name: OtaaV11
        - Name: AbpV11
        - Name: DeviceProfileId
        - Name: DevEui
        - Name: OtaaV10x
        - Name: ServiceProfileId
    
    """
    
    AbpV10x_: Optional['AbpV10x'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv10x""", alias="AbpV10x")
    OtaaV11_: Optional['OtaaV11'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav11""", alias="OtaaV11")
    AbpV11_: Optional['AbpV11'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv11""", alias="AbpV11")
    DeviceProfileId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deviceprofileid""", alias="DeviceProfileId")
    DevEui_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deveui""", alias="DevEui")
    OtaaV10x_: Optional['OtaaV10x'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav10x""", alias="OtaaV10x")
    ServiceProfileId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-serviceprofileid""", alias="ServiceProfileId")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.LoRaWANDevice:
        from troposphere.iotwireless import LoRaWANDevice as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OtaaV10x(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html
    Properties:
        - Name: AppEui
        - Name: AppKey
    
    """
    
    AppEui_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appeui""", alias="AppEui")
    AppKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appkey""", alias="AppKey")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.OtaaV10x:
        from troposphere.iotwireless import OtaaV10x as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OtaaV11(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html
    Properties:
        - Name: NwkKey
        - Name: AppKey
        - Name: JoinEui
    
    """
    
    NwkKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-nwkkey""", alias="NwkKey")
    AppKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-appkey""", alias="AppKey")
    JoinEui_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-joineui""", alias="JoinEui")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.OtaaV11:
        from troposphere.iotwireless import OtaaV11 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SessionKeysAbpV10x(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html
    Properties:
        - Name: AppSKey
        - Name: NwkSKey
    
    """
    
    AppSKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-appskey""", alias="AppSKey")
    NwkSKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-nwkskey""", alias="NwkSKey")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.SessionKeysAbpV10x:
        from troposphere.iotwireless import SessionKeysAbpV10x as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SessionKeysAbpV11(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html
    Properties:
        - Name: FNwkSIntKey
        - Name: AppSKey
        - Name: SNwkSIntKey
        - Name: NwkSEncKey
    
    """
    
    FNwkSIntKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-fnwksintkey""", alias="FNwkSIntKey")
    AppSKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-appskey""", alias="AppSKey")
    SNwkSIntKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-snwksintkey""", alias="SNwkSIntKey")
    NwkSEncKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-nwksenckey""", alias="NwkSEncKey")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.SessionKeysAbpV11:
        from troposphere.iotwireless import SessionKeysAbpV11 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Sidewalk(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdeviceimporttask-sidewalk.html
    Properties:
        - Name: Role
        - Name: SidewalkManufacturingSn
        - Name: DeviceCreationFile
        - Name: DeviceCreationFileList
    
    """
    
    Role_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdeviceimporttask-sidewalk.html#cfn-iotwireless-wirelessdeviceimporttask-sidewalk-role""", alias="Role")
    SidewalkManufacturingSn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdeviceimporttask-sidewalk.html#cfn-iotwireless-wirelessdeviceimporttask-sidewalk-sidewalkmanufacturingsn""", alias="SidewalkManufacturingSn")
    DeviceCreationFile_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdeviceimporttask-sidewalk.html#cfn-iotwireless-wirelessdeviceimporttask-sidewalk-devicecreationfile""", alias="DeviceCreationFile")
    DeviceCreationFileList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdeviceimporttask-sidewalk.html#cfn-iotwireless-wirelessdeviceimporttask-sidewalk-devicecreationfilelist""", alias="DeviceCreationFileList")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.Sidewalk:
        from troposphere.iotwireless import Sidewalk as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoRaWANGateway(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html
    Properties:
        - Name: RfRegion
        - Name: GatewayEui
    
    """
    
    RfRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-rfregion""", alias="RfRegion")
    GatewayEui_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-gatewayeui""", alias="GatewayEui")
    


    @property
    def tropo_type(self) -> troposphere.iotwireless.LoRaWANGateway:
        from troposphere.iotwireless import LoRaWANGateway as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Destination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html
    Properties:
        - Name: Description
        - Name: Expression
        - Name: ExpressionType
        - Name: Tags
        - Name: RoleArn
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-description""", alias="Description")
    Expression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expression""", alias="Expression")
    ExpressionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expressiontype""", alias="ExpressionType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-tags""", alias="Tags")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-rolearn""", alias="RoleArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iotwireless.Destination:
        from troposphere.iotwireless import Destination as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotwireless import Destination as TropoT
        return resource_to_troposphere(self, TropoT)


class DeviceProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html
    Properties:
        - Name: LoRaWAN
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LoRaWAN_: Optional['LoRaWANDeviceProfile'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-lorawan""", alias="LoRaWAN")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iotwireless.DeviceProfile:
        from troposphere.iotwireless import DeviceProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotwireless import DeviceProfile as TropoT
        return resource_to_troposphere(self, TropoT)


class FuotaTask(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html
    Properties:
        - Name: FirmwareUpdateImage
        - Name: Description
        - Name: LoRaWAN
        - Name: FirmwareUpdateRole
        - Name: AssociateMulticastGroup
        - Name: DisassociateWirelessDevice
        - Name: DisassociateMulticastGroup
        - Name: AssociateWirelessDevice
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: FuotaTaskStatus
        - Name: LoRaWAN.StartTime
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FirmwareUpdateImage_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-firmwareupdateimage""", alias="FirmwareUpdateImage")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-description""", alias="Description")
    LoRaWAN_: 'LoRaWAN' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-lorawan""", alias="LoRaWAN")
    FirmwareUpdateRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-firmwareupdaterole""", alias="FirmwareUpdateRole")
    AssociateMulticastGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-associatemulticastgroup""", alias="AssociateMulticastGroup")
    DisassociateWirelessDevice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-disassociatewirelessdevice""", alias="DisassociateWirelessDevice")
    DisassociateMulticastGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-disassociatemulticastgroup""", alias="DisassociateMulticastGroup")
    AssociateWirelessDevice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-associatewirelessdevice""", alias="AssociateWirelessDevice")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iotwireless.FuotaTask:
        from troposphere.iotwireless import FuotaTask as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotwireless import FuotaTask as TropoT
        return resource_to_troposphere(self, TropoT)


class MulticastGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html
    Properties:
        - Name: Description
        - Name: LoRaWAN
        - Name: DisassociateWirelessDevice
        - Name: AssociateWirelessDevice
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: LoRaWAN.NumberOfDevicesRequested
        - Name: Id
        - Name: LoRaWAN.NumberOfDevicesInGroup
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-description""", alias="Description")
    LoRaWAN_: 'LoRaWAN' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-lorawan""", alias="LoRaWAN")
    DisassociateWirelessDevice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-disassociatewirelessdevice""", alias="DisassociateWirelessDevice")
    AssociateWirelessDevice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-associatewirelessdevice""", alias="AssociateWirelessDevice")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iotwireless.MulticastGroup:
        from troposphere.iotwireless import MulticastGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotwireless import MulticastGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class NetworkAnalyzerConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html
    Properties:
        - Name: Description
        - Name: TraceContent
        - Name: WirelessGateways
        - Name: WirelessDevices
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-description""", alias="Description")
    TraceContent_: Optional['TraceContent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-tracecontent""", alias="TraceContent")
    WirelessGateways_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-wirelessgateways""", alias="WirelessGateways")
    WirelessDevices_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-wirelessdevices""", alias="WirelessDevices")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iotwireless.NetworkAnalyzerConfiguration:
        from troposphere.iotwireless import NetworkAnalyzerConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotwireless import NetworkAnalyzerConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class PartnerAccount(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html
    Properties:
        - Name: PartnerType
        - Name: SidewalkResponse
        - Name: AccountLinked
        - Name: Sidewalk
        - Name: PartnerAccountId
        - Name: SidewalkUpdate
        - Name: Tags
    Attributes:
        - Name: Fingerprint
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PartnerType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partnertype""", alias="PartnerType")
    SidewalkResponse_: Optional['SidewalkAccountInfoWithFingerprint'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalkresponse""", alias="SidewalkResponse")
    AccountLinked_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-accountlinked""", alias="AccountLinked")
    Sidewalk_: Optional['SidewalkAccountInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalk""", alias="Sidewalk")
    PartnerAccountId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partneraccountid""", alias="PartnerAccountId")
    SidewalkUpdate_: Optional['SidewalkUpdateAccount'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalkupdate""", alias="SidewalkUpdate")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotwireless.PartnerAccount:
        from troposphere.iotwireless import PartnerAccount as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotwireless import PartnerAccount as TropoT
        return resource_to_troposphere(self, TropoT)


class ServiceProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html
    Properties:
        - Name: LoRaWAN
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: LoRaWAN.DrMin
        - Name: LoRaWAN.ReportDevStatusMargin
        - Name: LoRaWAN.UlRatePolicy
        - Name: LoRaWAN.MinGwDiversity
        - Name: LoRaWAN.TargetPer
        - Name: LoRaWAN.ChannelMask
        - Name: LoRaWAN.ReportDevStatusBattery
        - Name: LoRaWAN.DlRate
        - Name: LoRaWAN.DlRatePolicy
        - Name: LoRaWAN.HrAllowed
        - Name: LoRaWAN.DlBucketSize
        - Name: LoRaWAN.DrMax
        - Name: LoRaWAN.UlBucketSize
        - Name: LoRaWAN.UlRate
        - Name: LoRaWAN.NwkGeoLoc
        - Name: LoRaWAN.DevStatusReqFreq
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LoRaWAN_: Optional['LoRaWANServiceProfile'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-lorawan""", alias="LoRaWAN")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iotwireless.ServiceProfile:
        from troposphere.iotwireless import ServiceProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotwireless import ServiceProfile as TropoT
        return resource_to_troposphere(self, TropoT)


class TaskDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html
    Properties:
        - Name: AutoCreateTasks
        - Name: LoRaWANUpdateGatewayTaskEntry
        - Name: Update
        - Name: TaskDefinitionType
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AutoCreateTasks_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-autocreatetasks""", alias="AutoCreateTasks")
    LoRaWANUpdateGatewayTaskEntry_: Optional['LoRaWANUpdateGatewayTaskEntry'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry""", alias="LoRaWANUpdateGatewayTaskEntry")
    Update_: Optional['UpdateWirelessGatewayTaskCreate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-update""", alias="Update")
    TaskDefinitionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-taskdefinitiontype""", alias="TaskDefinitionType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iotwireless.TaskDefinition:
        from troposphere.iotwireless import TaskDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotwireless import TaskDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class WirelessDevice(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html
    Properties:
        - Name: LastUplinkReceivedAt
        - Name: Type
        - Name: Description
        - Name: LoRaWAN
        - Name: DestinationName
        - Name: ThingArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: ThingName
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LastUplinkReceivedAt_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lastuplinkreceivedat""", alias="LastUplinkReceivedAt")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-description""", alias="Description")
    LoRaWAN_: Optional['LoRaWANDevice'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lorawan""", alias="LoRaWAN")
    DestinationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-destinationname""", alias="DestinationName")
    ThingArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-thingarn""", alias="ThingArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iotwireless.WirelessDevice:
        from troposphere.iotwireless import WirelessDevice as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotwireless import WirelessDevice as TropoT
        return resource_to_troposphere(self, TropoT)


class WirelessDeviceImportTask(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdeviceimporttask.html
    Properties:
        - Name: DestinationName
        - Name: Sidewalk
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: CreationDate
        - Name: Sidewalk.DeviceCreationFileList
        - Name: InitializedImportedDevicesCount
        - Name: StatusReason
        - Name: OnboardedImportedDevicesCount
        - Name: FailedImportedDevicesCount
        - Name: Id
        - Name: PendingImportedDevicesCount
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DestinationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdeviceimporttask.html#cfn-iotwireless-wirelessdeviceimporttask-destinationname""", alias="DestinationName")
    Sidewalk_: 'Sidewalk' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdeviceimporttask.html#cfn-iotwireless-wirelessdeviceimporttask-sidewalk""", alias="Sidewalk")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdeviceimporttask.html#cfn-iotwireless-wirelessdeviceimporttask-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotwireless.WirelessDeviceImportTask:
        from troposphere.iotwireless import WirelessDeviceImportTask as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotwireless import WirelessDeviceImportTask as TropoT
        return resource_to_troposphere(self, TropoT)


class WirelessGateway(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html
    Properties:
        - Name: LastUplinkReceivedAt
        - Name: Description
        - Name: LoRaWAN
        - Name: ThingArn
        - Name: ThingName
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LastUplinkReceivedAt_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lastuplinkreceivedat""", alias="LastUplinkReceivedAt")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-description""", alias="Description")
    LoRaWAN_: 'LoRaWANGateway' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lorawan""", alias="LoRaWAN")
    ThingArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingarn""", alias="ThingArn")
    ThingName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingname""", alias="ThingName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.iotwireless.WirelessGateway:
        from troposphere.iotwireless import WirelessGateway as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotwireless import WirelessGateway as TropoT
        return resource_to_troposphere(self, TropoT)

