from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AntennaDownlinkConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.html
    Properties:
        - Name: SpectrumConfig
    
    """
    
    SpectrumConfig_: Optional['SpectrumConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.html#cfn-groundstation-config-antennadownlinkconfig-spectrumconfig""", alias="SpectrumConfig")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.AntennaDownlinkConfig:
        from troposphere.groundstation import AntennaDownlinkConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AntennaDownlinkDemodDecodeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html
    Properties:
        - Name: DemodulationConfig
        - Name: SpectrumConfig
        - Name: DecodeConfig
    
    """
    
    DemodulationConfig_: Optional['DemodulationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html#cfn-groundstation-config-antennadownlinkdemoddecodeconfig-demodulationconfig""", alias="DemodulationConfig")
    SpectrumConfig_: Optional['SpectrumConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html#cfn-groundstation-config-antennadownlinkdemoddecodeconfig-spectrumconfig""", alias="SpectrumConfig")
    DecodeConfig_: Optional['DecodeConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html#cfn-groundstation-config-antennadownlinkdemoddecodeconfig-decodeconfig""", alias="DecodeConfig")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.AntennaDownlinkDemodDecodeConfig:
        from troposphere.groundstation import AntennaDownlinkDemodDecodeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AntennaUplinkConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html
    Properties:
        - Name: TransmitDisabled
        - Name: SpectrumConfig
        - Name: TargetEirp
    
    """
    
    TransmitDisabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html#cfn-groundstation-config-antennauplinkconfig-transmitdisabled""", alias="TransmitDisabled")
    SpectrumConfig_: Optional['UplinkSpectrumConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html#cfn-groundstation-config-antennauplinkconfig-spectrumconfig""", alias="SpectrumConfig")
    TargetEirp_: Optional['Eirp'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html#cfn-groundstation-config-antennauplinkconfig-targeteirp""", alias="TargetEirp")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.AntennaUplinkConfig:
        from troposphere.groundstation import AntennaUplinkConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfigData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html
    Properties:
        - Name: DataflowEndpointConfig
        - Name: UplinkEchoConfig
        - Name: AntennaDownlinkConfig
        - Name: AntennaDownlinkDemodDecodeConfig
        - Name: TrackingConfig
        - Name: AntennaUplinkConfig
        - Name: S3RecordingConfig
    
    """
    
    DataflowEndpointConfig_: Optional['DataflowEndpointConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-dataflowendpointconfig""", alias="DataflowEndpointConfig")
    UplinkEchoConfig_: Optional['UplinkEchoConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-uplinkechoconfig""", alias="UplinkEchoConfig")
    AntennaDownlinkConfig_: Optional['AntennaDownlinkConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-antennadownlinkconfig""", alias="AntennaDownlinkConfig")
    AntennaDownlinkDemodDecodeConfig_: Optional['AntennaDownlinkDemodDecodeConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-antennadownlinkdemoddecodeconfig""", alias="AntennaDownlinkDemodDecodeConfig")
    TrackingConfig_: Optional['TrackingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-trackingconfig""", alias="TrackingConfig")
    AntennaUplinkConfig_: Optional['AntennaUplinkConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-antennauplinkconfig""", alias="AntennaUplinkConfig")
    S3RecordingConfig_: Optional['S3RecordingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html#cfn-groundstation-config-configdata-s3recordingconfig""", alias="S3RecordingConfig")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.ConfigData:
        from troposphere.groundstation import ConfigData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataflowEndpointConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html
    Properties:
        - Name: DataflowEndpointName
        - Name: DataflowEndpointRegion
    
    """
    
    DataflowEndpointName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html#cfn-groundstation-config-dataflowendpointconfig-dataflowendpointname""", alias="DataflowEndpointName")
    DataflowEndpointRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html#cfn-groundstation-config-dataflowendpointconfig-dataflowendpointregion""", alias="DataflowEndpointRegion")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.DataflowEndpointConfig:
        from troposphere.groundstation import DataflowEndpointConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DecodeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-decodeconfig.html
    Properties:
        - Name: UnvalidatedJSON
    
    """
    
    UnvalidatedJSON_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-decodeconfig.html#cfn-groundstation-config-decodeconfig-unvalidatedjson""", alias="UnvalidatedJSON")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.DecodeConfig:
        from troposphere.groundstation import DecodeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DemodulationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-demodulationconfig.html
    Properties:
        - Name: UnvalidatedJSON
    
    """
    
    UnvalidatedJSON_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-demodulationconfig.html#cfn-groundstation-config-demodulationconfig-unvalidatedjson""", alias="UnvalidatedJSON")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.DemodulationConfig:
        from troposphere.groundstation import DemodulationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Eirp(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html
    Properties:
        - Name: Value
        - Name: Units
    
    """
    
    Value_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html#cfn-groundstation-config-eirp-value""", alias="Value")
    Units_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html#cfn-groundstation-config-eirp-units""", alias="Units")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.Eirp:
        from troposphere.groundstation import Eirp as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Frequency(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html
    Properties:
        - Name: Value
        - Name: Units
    
    """
    
    Value_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html#cfn-groundstation-config-frequency-value""", alias="Value")
    Units_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html#cfn-groundstation-config-frequency-units""", alias="Units")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.Frequency:
        from troposphere.groundstation import Frequency as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FrequencyBandwidth(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html
    Properties:
        - Name: Value
        - Name: Units
    
    """
    
    Value_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html#cfn-groundstation-config-frequencybandwidth-value""", alias="Value")
    Units_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html#cfn-groundstation-config-frequencybandwidth-units""", alias="Units")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.FrequencyBandwidth:
        from troposphere.groundstation import FrequencyBandwidth as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3RecordingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html
    Properties:
        - Name: BucketArn
        - Name: Prefix
        - Name: RoleArn
    
    """
    
    BucketArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html#cfn-groundstation-config-s3recordingconfig-bucketarn""", alias="BucketArn")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html#cfn-groundstation-config-s3recordingconfig-prefix""", alias="Prefix")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html#cfn-groundstation-config-s3recordingconfig-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.S3RecordingConfig:
        from troposphere.groundstation import S3RecordingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SpectrumConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html
    Properties:
        - Name: Polarization
        - Name: Bandwidth
        - Name: CenterFrequency
    
    """
    
    Polarization_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html#cfn-groundstation-config-spectrumconfig-polarization""", alias="Polarization")
    Bandwidth_: Optional['FrequencyBandwidth'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html#cfn-groundstation-config-spectrumconfig-bandwidth""", alias="Bandwidth")
    CenterFrequency_: Optional['Frequency'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html#cfn-groundstation-config-spectrumconfig-centerfrequency""", alias="CenterFrequency")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.SpectrumConfig:
        from troposphere.groundstation import SpectrumConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TrackingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.html
    Properties:
        - Name: Autotrack
    
    """
    
    Autotrack_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.html#cfn-groundstation-config-trackingconfig-autotrack""", alias="Autotrack")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.TrackingConfig:
        from troposphere.groundstation import TrackingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UplinkEchoConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html
    Properties:
        - Name: Enabled
        - Name: AntennaUplinkConfigArn
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html#cfn-groundstation-config-uplinkechoconfig-enabled""", alias="Enabled")
    AntennaUplinkConfigArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html#cfn-groundstation-config-uplinkechoconfig-antennauplinkconfigarn""", alias="AntennaUplinkConfigArn")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.UplinkEchoConfig:
        from troposphere.groundstation import UplinkEchoConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UplinkSpectrumConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html
    Properties:
        - Name: Polarization
        - Name: CenterFrequency
    
    """
    
    Polarization_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html#cfn-groundstation-config-uplinkspectrumconfig-polarization""", alias="Polarization")
    CenterFrequency_: Optional['Frequency'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html#cfn-groundstation-config-uplinkspectrumconfig-centerfrequency""", alias="CenterFrequency")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.UplinkSpectrumConfig:
        from troposphere.groundstation import UplinkSpectrumConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AwsGroundStationAgentEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html
    Properties:
        - Name: AgentStatus
        - Name: IngressAddress
        - Name: AuditResults
        - Name: Name
        - Name: EgressAddress
    
    """
    
    AgentStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-agentstatus""", alias="AgentStatus")
    IngressAddress_: Optional['RangedConnectionDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-ingressaddress""", alias="IngressAddress")
    AuditResults_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-auditresults""", alias="AuditResults")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-name""", alias="Name")
    EgressAddress_: Optional['ConnectionDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.html#cfn-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint-egressaddress""", alias="EgressAddress")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.AwsGroundStationAgentEndpoint:
        from troposphere.groundstation import AwsGroundStationAgentEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectionDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-connectiondetails.html
    Properties:
        - Name: SocketAddress
        - Name: Mtu
    
    """
    
    SocketAddress_: Optional['SocketAddress'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-connectiondetails.html#cfn-groundstation-dataflowendpointgroup-connectiondetails-socketaddress""", alias="SocketAddress")
    Mtu_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-connectiondetails.html#cfn-groundstation-dataflowendpointgroup-connectiondetails-mtu""", alias="Mtu")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.ConnectionDetails:
        from troposphere.groundstation import ConnectionDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataflowEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html
    Properties:
        - Name: Address
        - Name: Name
        - Name: Mtu
    
    """
    
    Address_: Optional['SocketAddress'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-address""", alias="Address")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-name""", alias="Name")
    Mtu_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-mtu""", alias="Mtu")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.DataflowEndpoint:
        from troposphere.groundstation import DataflowEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EndpointDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html
    Properties:
        - Name: Endpoint
        - Name: AwsGroundStationAgentEndpoint
        - Name: SecurityDetails
    
    """
    
    Endpoint_: Optional['DataflowEndpoint'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html#cfn-groundstation-dataflowendpointgroup-endpointdetails-endpoint""", alias="Endpoint")
    AwsGroundStationAgentEndpoint_: Optional['AwsGroundStationAgentEndpoint'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html#cfn-groundstation-dataflowendpointgroup-endpointdetails-awsgroundstationagentendpoint""", alias="AwsGroundStationAgentEndpoint")
    SecurityDetails_: Optional['SecurityDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html#cfn-groundstation-dataflowendpointgroup-endpointdetails-securitydetails""", alias="SecurityDetails")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.EndpointDetails:
        from troposphere.groundstation import EndpointDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IntegerRange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-integerrange.html
    Properties:
        - Name: Minimum
        - Name: Maximum
    
    """
    
    Minimum_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-integerrange.html#cfn-groundstation-dataflowendpointgroup-integerrange-minimum""", alias="Minimum")
    Maximum_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-integerrange.html#cfn-groundstation-dataflowendpointgroup-integerrange-maximum""", alias="Maximum")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.IntegerRange:
        from troposphere.groundstation import IntegerRange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RangedConnectionDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedconnectiondetails.html
    Properties:
        - Name: SocketAddress
        - Name: Mtu
    
    """
    
    SocketAddress_: Optional['RangedSocketAddress'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedconnectiondetails.html#cfn-groundstation-dataflowendpointgroup-rangedconnectiondetails-socketaddress""", alias="SocketAddress")
    Mtu_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedconnectiondetails.html#cfn-groundstation-dataflowendpointgroup-rangedconnectiondetails-mtu""", alias="Mtu")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.RangedConnectionDetails:
        from troposphere.groundstation import RangedConnectionDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RangedSocketAddress(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedsocketaddress.html
    Properties:
        - Name: PortRange
        - Name: Name
    
    """
    
    PortRange_: Optional['IntegerRange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedsocketaddress.html#cfn-groundstation-dataflowendpointgroup-rangedsocketaddress-portrange""", alias="PortRange")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-rangedsocketaddress.html#cfn-groundstation-dataflowendpointgroup-rangedsocketaddress-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.RangedSocketAddress:
        from troposphere.groundstation import RangedSocketAddress as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SecurityDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html
    Properties:
        - Name: SubnetIds
        - Name: SecurityGroupIds
        - Name: RoleArn
    
    """
    
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html#cfn-groundstation-dataflowendpointgroup-securitydetails-subnetids""", alias="SubnetIds")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html#cfn-groundstation-dataflowendpointgroup-securitydetails-securitygroupids""", alias="SecurityGroupIds")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html#cfn-groundstation-dataflowendpointgroup-securitydetails-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.SecurityDetails:
        from troposphere.groundstation import SecurityDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SocketAddress(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html
    Properties:
        - Name: Port
        - Name: Name
    
    """
    
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html#cfn-groundstation-dataflowendpointgroup-socketaddress-port""", alias="Port")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html#cfn-groundstation-dataflowendpointgroup-socketaddress-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.SocketAddress:
        from troposphere.groundstation import SocketAddress as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataflowEdge(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html
    Properties:
        - Name: Destination
        - Name: Source
    
    """
    
    Destination_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html#cfn-groundstation-missionprofile-dataflowedge-destination""", alias="Destination")
    Source_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html#cfn-groundstation-missionprofile-dataflowedge-source""", alias="Source")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.DataflowEdge:
        from troposphere.groundstation import DataflowEdge as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StreamsKmsKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-streamskmskey.html
    Properties:
        - Name: KmsKeyArn
        - Name: KmsAliasArn
    
    """
    
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-streamskmskey.html#cfn-groundstation-missionprofile-streamskmskey-kmskeyarn""", alias="KmsKeyArn")
    KmsAliasArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-streamskmskey.html#cfn-groundstation-missionprofile-streamskmskey-kmsaliasarn""", alias="KmsAliasArn")
    


    @property
    def tropo_type(self) -> troposphere.groundstation.StreamsKmsKey:
        from troposphere.groundstation import StreamsKmsKey as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Config(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html
    Properties:
        - Name: ConfigData
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Type
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConfigData_: 'ConfigData' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-configdata""", alias="ConfigData")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html#cfn-groundstation-config-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.groundstation.Config:
        from troposphere.groundstation import Config as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.groundstation import Config as TropoT
        return resource_to_troposphere(self, TropoT)


class DataflowEndpointGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html
    Properties:
        - Name: ContactPostPassDurationSeconds
        - Name: EndpointDetails
        - Name: Tags
        - Name: ContactPrePassDurationSeconds
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ContactPostPassDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-contactpostpassdurationseconds""", alias="ContactPostPassDurationSeconds")
    EndpointDetails_: List['EndpointDetails'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-endpointdetails""", alias="EndpointDetails")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-tags""", alias="Tags")
    ContactPrePassDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html#cfn-groundstation-dataflowendpointgroup-contactprepassdurationseconds""", alias="ContactPrePassDurationSeconds")
    

    @property
    def tropo_type(self) -> troposphere.groundstation.DataflowEndpointGroup:
        from troposphere.groundstation import DataflowEndpointGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.groundstation import DataflowEndpointGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class MissionProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html
    Properties:
        - Name: StreamsKmsKey
        - Name: ContactPostPassDurationSeconds
        - Name: MinimumViableContactDurationSeconds
        - Name: DataflowEdges
        - Name: StreamsKmsRole
        - Name: TrackingConfigArn
        - Name: Tags
        - Name: Name
        - Name: ContactPrePassDurationSeconds
    Attributes:
        - Name: Region
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StreamsKmsKey_: Optional['StreamsKmsKey'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-streamskmskey""", alias="StreamsKmsKey")
    ContactPostPassDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-contactpostpassdurationseconds""", alias="ContactPostPassDurationSeconds")
    MinimumViableContactDurationSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-minimumviablecontactdurationseconds""", alias="MinimumViableContactDurationSeconds")
    DataflowEdges_: List['DataflowEdge'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-dataflowedges""", alias="DataflowEdges")
    StreamsKmsRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-streamskmsrole""", alias="StreamsKmsRole")
    TrackingConfigArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-trackingconfigarn""", alias="TrackingConfigArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-name""", alias="Name")
    ContactPrePassDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html#cfn-groundstation-missionprofile-contactprepassdurationseconds""", alias="ContactPrePassDurationSeconds")
    

    @property
    def tropo_type(self) -> troposphere.groundstation.MissionProfile:
        from troposphere.groundstation import MissionProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.groundstation import MissionProfile as TropoT
        return resource_to_troposphere(self, TropoT)

