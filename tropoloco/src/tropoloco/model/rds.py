from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DBClusterRole(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-dbclusterrole.html
    Properties:
        - Name: RoleArn
        - Name: FeatureName
    
    """
    
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-dbclusterrole.html#cfn-rds-dbcluster-dbclusterrole-rolearn""", alias="RoleArn")
    FeatureName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-dbclusterrole.html#cfn-rds-dbcluster-dbclusterrole-featurename""", alias="FeatureName")
    


    @property
    def tropo_type(self) -> troposphere.rds.DBClusterRole:
        from troposphere.rds import DBClusterRole as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Endpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-endpoint.html
    Properties:
        - Name: Address
        - Name: Port
    
    """
    
    Address_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-endpoint.html#cfn-rds-dbcluster-endpoint-address""", alias="Address")
    Port_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-endpoint.html#cfn-rds-dbcluster-endpoint-port""", alias="Port")
    


    @property
    def tropo_type(self) -> troposphere.rds.Endpoint:
        from troposphere.rds import Endpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MasterUserSecret(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-masterusersecret.html
    Properties:
        - Name: SecretArn
        - Name: KmsKeyId
    
    """
    
    SecretArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-masterusersecret.html#cfn-rds-dbcluster-masterusersecret-secretarn""", alias="SecretArn")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-masterusersecret.html#cfn-rds-dbcluster-masterusersecret-kmskeyid""", alias="KmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.rds.MasterUserSecret:
        from troposphere.rds import MasterUserSecret as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReadEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-readendpoint.html
    Properties:
        - Name: Address
    
    """
    
    Address_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-readendpoint.html#cfn-rds-dbcluster-readendpoint-address""", alias="Address")
    


    @property
    def tropo_type(self) -> troposphere.rds.ReadEndpoint:
        from troposphere.rds import ReadEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScalingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-scalingconfiguration.html
    Properties:
        - Name: TimeoutAction
        - Name: SecondsBeforeTimeout
        - Name: SecondsUntilAutoPause
        - Name: AutoPause
        - Name: MinCapacity
        - Name: MaxCapacity
    
    """
    
    TimeoutAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-scalingconfiguration.html#cfn-rds-dbcluster-scalingconfiguration-timeoutaction""", alias="TimeoutAction")
    SecondsBeforeTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-scalingconfiguration.html#cfn-rds-dbcluster-scalingconfiguration-secondsbeforetimeout""", alias="SecondsBeforeTimeout")
    SecondsUntilAutoPause_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-scalingconfiguration.html#cfn-rds-dbcluster-scalingconfiguration-secondsuntilautopause""", alias="SecondsUntilAutoPause")
    AutoPause_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-scalingconfiguration.html#cfn-rds-dbcluster-scalingconfiguration-autopause""", alias="AutoPause")
    MinCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-scalingconfiguration.html#cfn-rds-dbcluster-scalingconfiguration-mincapacity""", alias="MinCapacity")
    MaxCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-scalingconfiguration.html#cfn-rds-dbcluster-scalingconfiguration-maxcapacity""", alias="MaxCapacity")
    


    @property
    def tropo_type(self) -> troposphere.rds.ScalingConfiguration:
        from troposphere.rds import ScalingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServerlessV2ScalingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-serverlessv2scalingconfiguration.html
    Properties:
        - Name: MinCapacity
        - Name: MaxCapacity
    
    """
    
    MinCapacity_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-serverlessv2scalingconfiguration.html#cfn-rds-dbcluster-serverlessv2scalingconfiguration-mincapacity""", alias="MinCapacity")
    MaxCapacity_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-serverlessv2scalingconfiguration.html#cfn-rds-dbcluster-serverlessv2scalingconfiguration-maxcapacity""", alias="MaxCapacity")
    


    @property
    def tropo_type(self) -> troposphere.rds.ServerlessV2ScalingConfiguration:
        from troposphere.rds import ServerlessV2ScalingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CertificateDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-certificatedetails.html
    Properties:
        - Name: ValidTill
        - Name: CAIdentifier
    
    """
    
    ValidTill_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-certificatedetails.html#cfn-rds-dbinstance-certificatedetails-validtill""", alias="ValidTill")
    CAIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-certificatedetails.html#cfn-rds-dbinstance-certificatedetails-caidentifier""", alias="CAIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.rds.CertificateDetails:
        from troposphere.rds import CertificateDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DBInstanceRole(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-dbinstancerole.html
    Properties:
        - Name: RoleArn
        - Name: FeatureName
    
    """
    
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-dbinstancerole.html#cfn-rds-dbinstance-dbinstancerole-rolearn""", alias="RoleArn")
    FeatureName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-dbinstancerole.html#cfn-rds-dbinstance-dbinstancerole-featurename""", alias="FeatureName")
    


    @property
    def tropo_type(self) -> troposphere.rds.DBInstanceRole:
        from troposphere.rds import DBInstanceRole as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Endpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-endpoint.html
    Properties:
        - Name: Address
        - Name: Port
        - Name: HostedZoneId
    
    """
    
    Address_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-endpoint.html#cfn-rds-dbinstance-endpoint-address""", alias="Address")
    Port_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-endpoint.html#cfn-rds-dbinstance-endpoint-port""", alias="Port")
    HostedZoneId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-endpoint.html#cfn-rds-dbinstance-endpoint-hostedzoneid""", alias="HostedZoneId")
    


    @property
    def tropo_type(self) -> troposphere.rds.Endpoint:
        from troposphere.rds import Endpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MasterUserSecret(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-masterusersecret.html
    Properties:
        - Name: SecretArn
        - Name: KmsKeyId
    
    """
    
    SecretArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-masterusersecret.html#cfn-rds-dbinstance-masterusersecret-secretarn""", alias="SecretArn")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-masterusersecret.html#cfn-rds-dbinstance-masterusersecret-kmskeyid""", alias="KmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.rds.MasterUserSecret:
        from troposphere.rds import MasterUserSecret as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProcessorFeature(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-processorfeature.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-processorfeature.html#cfn-rds-dbinstance-processorfeature-value""", alias="Value")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-processorfeature.html#cfn-rds-dbinstance-processorfeature-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.rds.ProcessorFeature:
        from troposphere.rds import ProcessorFeature as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuthFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxy-authformat.html
    Properties:
        - Name: SecretArn
        - Name: Description
        - Name: IAMAuth
        - Name: ClientPasswordAuthType
        - Name: AuthScheme
    
    """
    
    SecretArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxy-authformat.html#cfn-rds-dbproxy-authformat-secretarn""", alias="SecretArn")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxy-authformat.html#cfn-rds-dbproxy-authformat-description""", alias="Description")
    IAMAuth_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxy-authformat.html#cfn-rds-dbproxy-authformat-iamauth""", alias="IAMAuth")
    ClientPasswordAuthType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxy-authformat.html#cfn-rds-dbproxy-authformat-clientpasswordauthtype""", alias="ClientPasswordAuthType")
    AuthScheme_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxy-authformat.html#cfn-rds-dbproxy-authformat-authscheme""", alias="AuthScheme")
    


    @property
    def tropo_type(self) -> troposphere.rds.AuthFormat:
        from troposphere.rds import AuthFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxy-tagformat.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxy-tagformat.html#cfn-rds-dbproxy-tagformat-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxy-tagformat.html#cfn-rds-dbproxy-tagformat-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.rds.TagFormat:
        from troposphere.rds import TagFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxyendpoint-tagformat.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxyendpoint-tagformat.html#cfn-rds-dbproxyendpoint-tagformat-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxyendpoint-tagformat.html#cfn-rds-dbproxyendpoint-tagformat-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.rds.TagFormat:
        from troposphere.rds import TagFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectionPoolConfigurationInfoFormat(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxytargetgroup-connectionpoolconfigurationinfoformat.html
    Properties:
        - Name: MaxIdleConnectionsPercent
        - Name: MaxConnectionsPercent
        - Name: InitQuery
        - Name: ConnectionBorrowTimeout
        - Name: SessionPinningFilters
    
    """
    
    MaxIdleConnectionsPercent_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxytargetgroup-connectionpoolconfigurationinfoformat.html#cfn-rds-dbproxytargetgroup-connectionpoolconfigurationinfoformat-maxidleconnectionspercent""", alias="MaxIdleConnectionsPercent")
    MaxConnectionsPercent_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxytargetgroup-connectionpoolconfigurationinfoformat.html#cfn-rds-dbproxytargetgroup-connectionpoolconfigurationinfoformat-maxconnectionspercent""", alias="MaxConnectionsPercent")
    InitQuery_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxytargetgroup-connectionpoolconfigurationinfoformat.html#cfn-rds-dbproxytargetgroup-connectionpoolconfigurationinfoformat-initquery""", alias="InitQuery")
    ConnectionBorrowTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxytargetgroup-connectionpoolconfigurationinfoformat.html#cfn-rds-dbproxytargetgroup-connectionpoolconfigurationinfoformat-connectionborrowtimeout""", alias="ConnectionBorrowTimeout")
    SessionPinningFilters_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxytargetgroup-connectionpoolconfigurationinfoformat.html#cfn-rds-dbproxytargetgroup-connectionpoolconfigurationinfoformat-sessionpinningfilters""", alias="SessionPinningFilters")
    


    @property
    def tropo_type(self) -> troposphere.rds.ConnectionPoolConfigurationInfoFormat:
        from troposphere.rds import ConnectionPoolConfigurationInfoFormat as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ingress(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html
    Properties:
        - Name: CIDRIP
        - Name: EC2SecurityGroupId
        - Name: EC2SecurityGroupName
        - Name: EC2SecurityGroupOwnerId
    
    """
    
    CIDRIP_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html#cfn-rds-securitygroup-cidrip""", alias="CIDRIP")
    EC2SecurityGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html#cfn-rds-securitygroup-ec2securitygroupid""", alias="EC2SecurityGroupId")
    EC2SecurityGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html#cfn-rds-securitygroup-ec2securitygroupname""", alias="EC2SecurityGroupName")
    EC2SecurityGroupOwnerId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html#cfn-rds-securitygroup-ec2securitygroupownerid""", alias="EC2SecurityGroupOwnerId")
    


    @property
    def tropo_type(self) -> troposphere.rds.Ingress:
        from troposphere.rds import Ingress as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfiguration.html
    Properties:
        - Name: OptionVersion
        - Name: VpcSecurityGroupMemberships
        - Name: OptionSettings
        - Name: Port
        - Name: OptionName
        - Name: DBSecurityGroupMemberships
    
    """
    
    OptionVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfiguration.html#cfn-rds-optiongroup-optionconfiguration-optionversion""", alias="OptionVersion")
    VpcSecurityGroupMemberships_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfiguration.html#cfn-rds-optiongroup-optionconfiguration-vpcsecuritygroupmemberships""", alias="VpcSecurityGroupMemberships")
    OptionSettings_: Optional[List['OptionSetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfiguration.html#cfn-rds-optiongroup-optionconfiguration-optionsettings""", alias="OptionSettings")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfiguration.html#cfn-rds-optiongroup-optionconfiguration-port""", alias="Port")
    OptionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfiguration.html#cfn-rds-optiongroup-optionconfiguration-optionname""", alias="OptionName")
    DBSecurityGroupMemberships_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfiguration.html#cfn-rds-optiongroup-optionconfiguration-dbsecuritygroupmemberships""", alias="DBSecurityGroupMemberships")
    


    @property
    def tropo_type(self) -> troposphere.rds.OptionConfiguration:
        from troposphere.rds import OptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OptionSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionsetting.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionsetting.html#cfn-rds-optiongroup-optionsetting-value""", alias="Value")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionsetting.html#cfn-rds-optiongroup-optionsetting-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.rds.OptionSetting:
        from troposphere.rds import OptionSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class CustomDBEngineVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-customdbengineversion.html
    Properties:
        - Name: Status
        - Name: DatabaseInstallationFilesS3BucketName
        - Name: Description
        - Name: EngineVersion
        - Name: KMSKeyId
        - Name: DatabaseInstallationFilesS3Prefix
        - Name: Manifest
        - Name: Engine
        - Name: Tags
    Attributes:
        - Name: DBEngineVersionArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-customdbengineversion.html#cfn-rds-customdbengineversion-status""", alias="Status")
    DatabaseInstallationFilesS3BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-customdbengineversion.html#cfn-rds-customdbengineversion-databaseinstallationfiless3bucketname""", alias="DatabaseInstallationFilesS3BucketName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-customdbengineversion.html#cfn-rds-customdbengineversion-description""", alias="Description")
    EngineVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-customdbengineversion.html#cfn-rds-customdbengineversion-engineversion""", alias="EngineVersion")
    KMSKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-customdbengineversion.html#cfn-rds-customdbengineversion-kmskeyid""", alias="KMSKeyId")
    DatabaseInstallationFilesS3Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-customdbengineversion.html#cfn-rds-customdbengineversion-databaseinstallationfiless3prefix""", alias="DatabaseInstallationFilesS3Prefix")
    Manifest_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-customdbengineversion.html#cfn-rds-customdbengineversion-manifest""", alias="Manifest")
    Engine_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-customdbengineversion.html#cfn-rds-customdbengineversion-engine""", alias="Engine")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-customdbengineversion.html#cfn-rds-customdbengineversion-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.rds.CustomDBEngineVersion:
        from troposphere.rds import CustomDBEngineVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import CustomDBEngineVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class DBCluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html
    Properties:
        - Name: StorageEncrypted
        - Name: DBSystemId
        - Name: RestoreToTime
        - Name: EngineMode
        - Name: Port
        - Name: DBClusterIdentifier
        - Name: MonitoringInterval
        - Name: ReplicationSourceIdentifier
        - Name: Engine
        - Name: Tags
        - Name: EngineVersion
        - Name: StorageType
        - Name: KmsKeyId
        - Name: ServerlessV2ScalingConfiguration
        - Name: PerformanceInsightsRetentionPeriod
        - Name: DatabaseName
        - Name: AutoMinorVersionUpgrade
        - Name: DBSubnetGroupName
        - Name: DeletionProtection
        - Name: AllocatedStorage
        - Name: MasterUserPassword
        - Name: MasterUserSecret
        - Name: SourceDBClusterIdentifier
        - Name: MasterUsername
        - Name: ScalingConfiguration
        - Name: PerformanceInsightsKmsKeyId
        - Name: PubliclyAccessible
        - Name: Domain
        - Name: BacktrackWindow
        - Name: DBInstanceParameterGroupName
        - Name: MonitoringRoleArn
        - Name: AssociatedRoles
        - Name: EnableHttpEndpoint
        - Name: SnapshotIdentifier
        - Name: PreferredBackupWindow
        - Name: NetworkType
        - Name: VpcSecurityGroupIds
        - Name: CopyTagsToSnapshot
        - Name: GlobalClusterIdentifier
        - Name: RestoreType
        - Name: DomainIAMRoleName
        - Name: DBClusterInstanceClass
        - Name: AvailabilityZones
        - Name: PreferredMaintenanceWindow
        - Name: Iops
        - Name: SourceRegion
        - Name: UseLatestRestorableTime
        - Name: ManageMasterUserPassword
        - Name: EnableIAMDatabaseAuthentication
        - Name: DBClusterParameterGroupName
        - Name: PerformanceInsightsEnabled
        - Name: BackupRetentionPeriod
        - Name: EnableCloudwatchLogsExports
    Attributes:
        - Name: Endpoint.Address
        - Name: Endpoint
        - Name: DBClusterArn
        - Name: Endpoint.Port
        - Name: ReadEndpoint.Address
        - Name: DBClusterResourceId
        - Name: MasterUserSecret.SecretArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StorageEncrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-storageencrypted""", alias="StorageEncrypted")
    DBSystemId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-dbsystemid""", alias="DBSystemId")
    RestoreToTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-restoretotime""", alias="RestoreToTime")
    EngineMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-enginemode""", alias="EngineMode")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-port""", alias="Port")
    DBClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-dbclusteridentifier""", alias="DBClusterIdentifier")
    MonitoringInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-monitoringinterval""", alias="MonitoringInterval")
    ReplicationSourceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-replicationsourceidentifier""", alias="ReplicationSourceIdentifier")
    Engine_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-engine""", alias="Engine")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-tags""", alias="Tags")
    EngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-engineversion""", alias="EngineVersion")
    StorageType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-storagetype""", alias="StorageType")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-kmskeyid""", alias="KmsKeyId")
    ServerlessV2ScalingConfiguration_: Optional['ServerlessV2ScalingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-serverlessv2scalingconfiguration""", alias="ServerlessV2ScalingConfiguration")
    PerformanceInsightsRetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-performanceinsightsretentionperiod""", alias="PerformanceInsightsRetentionPeriod")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-databasename""", alias="DatabaseName")
    AutoMinorVersionUpgrade_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-autominorversionupgrade""", alias="AutoMinorVersionUpgrade")
    DBSubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-dbsubnetgroupname""", alias="DBSubnetGroupName")
    DeletionProtection_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-deletionprotection""", alias="DeletionProtection")
    AllocatedStorage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-allocatedstorage""", alias="AllocatedStorage")
    MasterUserPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-masteruserpassword""", alias="MasterUserPassword")
    MasterUserSecret_: Optional['MasterUserSecret'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-masterusersecret""", alias="MasterUserSecret")
    SourceDBClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-sourcedbclusteridentifier""", alias="SourceDBClusterIdentifier")
    MasterUsername_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-masterusername""", alias="MasterUsername")
    ScalingConfiguration_: Optional['ScalingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-scalingconfiguration""", alias="ScalingConfiguration")
    PerformanceInsightsKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-performanceinsightskmskeyid""", alias="PerformanceInsightsKmsKeyId")
    PubliclyAccessible_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-publiclyaccessible""", alias="PubliclyAccessible")
    Domain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-domain""", alias="Domain")
    BacktrackWindow_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-backtrackwindow""", alias="BacktrackWindow")
    DBInstanceParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-dbinstanceparametergroupname""", alias="DBInstanceParameterGroupName")
    MonitoringRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-monitoringrolearn""", alias="MonitoringRoleArn")
    AssociatedRoles_: Optional[List['DBClusterRole']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-associatedroles""", alias="AssociatedRoles")
    EnableHttpEndpoint_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-enablehttpendpoint""", alias="EnableHttpEndpoint")
    SnapshotIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-snapshotidentifier""", alias="SnapshotIdentifier")
    PreferredBackupWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-preferredbackupwindow""", alias="PreferredBackupWindow")
    NetworkType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-networktype""", alias="NetworkType")
    VpcSecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-vpcsecuritygroupids""", alias="VpcSecurityGroupIds")
    CopyTagsToSnapshot_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-copytagstosnapshot""", alias="CopyTagsToSnapshot")
    GlobalClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-globalclusteridentifier""", alias="GlobalClusterIdentifier")
    RestoreType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-restoretype""", alias="RestoreType")
    DomainIAMRoleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-domainiamrolename""", alias="DomainIAMRoleName")
    DBClusterInstanceClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-dbclusterinstanceclass""", alias="DBClusterInstanceClass")
    AvailabilityZones_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-availabilityzones""", alias="AvailabilityZones")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-iops""", alias="Iops")
    SourceRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-sourceregion""", alias="SourceRegion")
    UseLatestRestorableTime_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-uselatestrestorabletime""", alias="UseLatestRestorableTime")
    ManageMasterUserPassword_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-managemasteruserpassword""", alias="ManageMasterUserPassword")
    EnableIAMDatabaseAuthentication_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-enableiamdatabaseauthentication""", alias="EnableIAMDatabaseAuthentication")
    DBClusterParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-dbclusterparametergroupname""", alias="DBClusterParameterGroupName")
    PerformanceInsightsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-performanceinsightsenabled""", alias="PerformanceInsightsEnabled")
    BackupRetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-backupretentionperiod""", alias="BackupRetentionPeriod")
    EnableCloudwatchLogsExports_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-enablecloudwatchlogsexports""", alias="EnableCloudwatchLogsExports")
    

    @property
    def tropo_type(self) -> troposphere.rds.DBCluster:
        from troposphere.rds import DBCluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import DBCluster as TropoT
        return resource_to_troposphere(self, TropoT)


class DBClusterParameterGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html
    Properties:
        - Name: Description
        - Name: Parameters
        - Name: Family
        - Name: DBClusterParameterGroupName
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html#cfn-rds-dbclusterparametergroup-description""", alias="Description")
    Parameters_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html#cfn-rds-dbclusterparametergroup-parameters""", alias="Parameters")
    Family_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html#cfn-rds-dbclusterparametergroup-family""", alias="Family")
    DBClusterParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html#cfn-rds-dbclusterparametergroup-dbclusterparametergroupname""", alias="DBClusterParameterGroupName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html#cfn-rds-dbclusterparametergroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.rds.DBClusterParameterGroup:
        from troposphere.rds import DBClusterParameterGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import DBClusterParameterGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class DBInstance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html
    Properties:
        - Name: StorageEncrypted
        - Name: Timezone
        - Name: CertificateDetails
        - Name: Port
        - Name: DBClusterIdentifier
        - Name: StorageThroughput
        - Name: MonitoringInterval
        - Name: DBParameterGroupName
        - Name: Endpoint
        - Name: MultiAZ
        - Name: Engine
        - Name: Tags
        - Name: PerformanceInsightsKMSKeyId
        - Name: SourceDBInstanceIdentifier
        - Name: EngineVersion
        - Name: StorageType
        - Name: KmsKeyId
        - Name: DBInstanceClass
        - Name: DeleteAutomatedBackups
        - Name: PerformanceInsightsRetentionPeriod
        - Name: AvailabilityZone
        - Name: OptionGroupName
        - Name: EnablePerformanceInsights
        - Name: AutoMinorVersionUpgrade
        - Name: DBSubnetGroupName
        - Name: DeletionProtection
        - Name: DBInstanceIdentifier
        - Name: AllocatedStorage
        - Name: MasterUserPassword
        - Name: MasterUserSecret
        - Name: NcharCharacterSetName
        - Name: SourceDBClusterIdentifier
        - Name: DBSecurityGroups
        - Name: MasterUsername
        - Name: MaxAllocatedStorage
        - Name: PromotionTier
        - Name: PubliclyAccessible
        - Name: Domain
        - Name: DomainFqdn
        - Name: CharacterSetName
        - Name: MonitoringRoleArn
        - Name: AssociatedRoles
        - Name: DomainOu
        - Name: DBClusterSnapshotIdentifier
        - Name: SourceDBInstanceAutomatedBackupsArn
        - Name: ProcessorFeatures
        - Name: PreferredBackupWindow
        - Name: RestoreTime
        - Name: CertificateRotationRestart
        - Name: NetworkType
        - Name: CopyTagsToSnapshot
        - Name: DomainIAMRoleName
        - Name: ReplicaMode
        - Name: LicenseModel
        - Name: DomainDnsIps
        - Name: PreferredMaintenanceWindow
        - Name: Iops
        - Name: SourceRegion
        - Name: UseLatestRestorableTime
        - Name: CACertificateIdentifier
        - Name: ManageMasterUserPassword
        - Name: SourceDbiResourceId
        - Name: DomainAuthSecretArn
        - Name: AutomaticBackupReplicationRegion
        - Name: VPCSecurityGroups
        - Name: AllowMajorVersionUpgrade
        - Name: DBName
        - Name: EnableIAMDatabaseAuthentication
        - Name: BackupRetentionPeriod
        - Name: CustomIAMInstanceProfile
        - Name: DBSnapshotIdentifier
        - Name: EnableCloudwatchLogsExports
        - Name: UseDefaultProcessorFeatures
    Attributes:
        - Name: DBSystemId
        - Name: Endpoint.Address
        - Name: DBInstanceArn
        - Name: CertificateDetails.ValidTill
        - Name: CertificateDetails.CAIdentifier
        - Name: Endpoint.Port
        - Name: Endpoint.HostedZoneId
        - Name: DbiResourceId
        - Name: MasterUserSecret.SecretArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StorageEncrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-storageencrypted""", alias="StorageEncrypted")
    Timezone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-timezone""", alias="Timezone")
    CertificateDetails_: Optional['CertificateDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-certificatedetails""", alias="CertificateDetails")
    Port_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-port""", alias="Port")
    DBClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-dbclusteridentifier""", alias="DBClusterIdentifier")
    StorageThroughput_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-storagethroughput""", alias="StorageThroughput")
    MonitoringInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-monitoringinterval""", alias="MonitoringInterval")
    DBParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-dbparametergroupname""", alias="DBParameterGroupName")
    Endpoint_: Optional['Endpoint'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-endpoint""", alias="Endpoint")
    MultiAZ_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-multiaz""", alias="MultiAZ")
    Engine_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-engine""", alias="Engine")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-tags""", alias="Tags")
    PerformanceInsightsKMSKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-performanceinsightskmskeyid""", alias="PerformanceInsightsKMSKeyId")
    SourceDBInstanceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-sourcedbinstanceidentifier""", alias="SourceDBInstanceIdentifier")
    EngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-engineversion""", alias="EngineVersion")
    StorageType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-storagetype""", alias="StorageType")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-kmskeyid""", alias="KmsKeyId")
    DBInstanceClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-dbinstanceclass""", alias="DBInstanceClass")
    DeleteAutomatedBackups_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-deleteautomatedbackups""", alias="DeleteAutomatedBackups")
    PerformanceInsightsRetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-performanceinsightsretentionperiod""", alias="PerformanceInsightsRetentionPeriod")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-availabilityzone""", alias="AvailabilityZone")
    OptionGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-optiongroupname""", alias="OptionGroupName")
    EnablePerformanceInsights_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-enableperformanceinsights""", alias="EnablePerformanceInsights")
    AutoMinorVersionUpgrade_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-autominorversionupgrade""", alias="AutoMinorVersionUpgrade")
    DBSubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-dbsubnetgroupname""", alias="DBSubnetGroupName")
    DeletionProtection_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-deletionprotection""", alias="DeletionProtection")
    DBInstanceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-dbinstanceidentifier""", alias="DBInstanceIdentifier")
    AllocatedStorage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-allocatedstorage""", alias="AllocatedStorage")
    MasterUserPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-masteruserpassword""", alias="MasterUserPassword")
    MasterUserSecret_: Optional['MasterUserSecret'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-masterusersecret""", alias="MasterUserSecret")
    NcharCharacterSetName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-ncharcharactersetname""", alias="NcharCharacterSetName")
    SourceDBClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-sourcedbclusteridentifier""", alias="SourceDBClusterIdentifier")
    DBSecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-dbsecuritygroups""", alias="DBSecurityGroups")
    MasterUsername_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-masterusername""", alias="MasterUsername")
    MaxAllocatedStorage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-maxallocatedstorage""", alias="MaxAllocatedStorage")
    PromotionTier_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-promotiontier""", alias="PromotionTier")
    PubliclyAccessible_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-publiclyaccessible""", alias="PubliclyAccessible")
    Domain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-domain""", alias="Domain")
    DomainFqdn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-domainfqdn""", alias="DomainFqdn")
    CharacterSetName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-charactersetname""", alias="CharacterSetName")
    MonitoringRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-monitoringrolearn""", alias="MonitoringRoleArn")
    AssociatedRoles_: Optional[List['DBInstanceRole']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-associatedroles""", alias="AssociatedRoles")
    DomainOu_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-domainou""", alias="DomainOu")
    DBClusterSnapshotIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-dbclustersnapshotidentifier""", alias="DBClusterSnapshotIdentifier")
    SourceDBInstanceAutomatedBackupsArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-sourcedbinstanceautomatedbackupsarn""", alias="SourceDBInstanceAutomatedBackupsArn")
    ProcessorFeatures_: Optional[List['ProcessorFeature']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-processorfeatures""", alias="ProcessorFeatures")
    PreferredBackupWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-preferredbackupwindow""", alias="PreferredBackupWindow")
    RestoreTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-restoretime""", alias="RestoreTime")
    CertificateRotationRestart_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-certificaterotationrestart""", alias="CertificateRotationRestart")
    NetworkType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-networktype""", alias="NetworkType")
    CopyTagsToSnapshot_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-copytagstosnapshot""", alias="CopyTagsToSnapshot")
    DomainIAMRoleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-domainiamrolename""", alias="DomainIAMRoleName")
    ReplicaMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-replicamode""", alias="ReplicaMode")
    LicenseModel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-licensemodel""", alias="LicenseModel")
    DomainDnsIps_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-domaindnsips""", alias="DomainDnsIps")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-iops""", alias="Iops")
    SourceRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-sourceregion""", alias="SourceRegion")
    UseLatestRestorableTime_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-uselatestrestorabletime""", alias="UseLatestRestorableTime")
    CACertificateIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-cacertificateidentifier""", alias="CACertificateIdentifier")
    ManageMasterUserPassword_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-managemasteruserpassword""", alias="ManageMasterUserPassword")
    SourceDbiResourceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-sourcedbiresourceid""", alias="SourceDbiResourceId")
    DomainAuthSecretArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-domainauthsecretarn""", alias="DomainAuthSecretArn")
    AutomaticBackupReplicationRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-automaticbackupreplicationregion""", alias="AutomaticBackupReplicationRegion")
    VPCSecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-vpcsecuritygroups""", alias="VPCSecurityGroups")
    AllowMajorVersionUpgrade_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-allowmajorversionupgrade""", alias="AllowMajorVersionUpgrade")
    DBName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-dbname""", alias="DBName")
    EnableIAMDatabaseAuthentication_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-enableiamdatabaseauthentication""", alias="EnableIAMDatabaseAuthentication")
    BackupRetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-backupretentionperiod""", alias="BackupRetentionPeriod")
    CustomIAMInstanceProfile_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-customiaminstanceprofile""", alias="CustomIAMInstanceProfile")
    DBSnapshotIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-dbsnapshotidentifier""", alias="DBSnapshotIdentifier")
    EnableCloudwatchLogsExports_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-enablecloudwatchlogsexports""", alias="EnableCloudwatchLogsExports")
    UseDefaultProcessorFeatures_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-usedefaultprocessorfeatures""", alias="UseDefaultProcessorFeatures")
    

    @property
    def tropo_type(self) -> troposphere.rds.DBInstance:
        from troposphere.rds import DBInstance as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import DBInstance as TropoT
        return resource_to_troposphere(self, TropoT)


class DBParameterGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbparametergroup.html
    Properties:
        - Name: DBParameterGroupName
        - Name: Description
        - Name: Parameters
        - Name: Family
        - Name: Tags
    Attributes:
        - Name: DBParameterGroupName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DBParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbparametergroup.html#cfn-rds-dbparametergroup-dbparametergroupname""", alias="DBParameterGroupName")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbparametergroup.html#cfn-rds-dbparametergroup-description""", alias="Description")
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbparametergroup.html#cfn-rds-dbparametergroup-parameters""", alias="Parameters")
    Family_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbparametergroup.html#cfn-rds-dbparametergroup-family""", alias="Family")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbparametergroup.html#cfn-rds-dbparametergroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.rds.DBParameterGroup:
        from troposphere.rds import DBParameterGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import DBParameterGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class DBProxy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html
    Properties:
        - Name: RequireTLS
        - Name: DBProxyName
        - Name: IdleClientTimeout
        - Name: VpcSecurityGroupIds
        - Name: Auth
        - Name: DebugLogging
        - Name: VpcSubnetIds
        - Name: RoleArn
        - Name: EngineFamily
        - Name: Tags
    Attributes:
        - Name: Endpoint
        - Name: VpcId
        - Name: DBProxyArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RequireTLS_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html#cfn-rds-dbproxy-requiretls""", alias="RequireTLS")
    DBProxyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html#cfn-rds-dbproxy-dbproxyname""", alias="DBProxyName")
    IdleClientTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html#cfn-rds-dbproxy-idleclienttimeout""", alias="IdleClientTimeout")
    VpcSecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html#cfn-rds-dbproxy-vpcsecuritygroupids""", alias="VpcSecurityGroupIds")
    Auth_: List['AuthFormat'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html#cfn-rds-dbproxy-auth""", alias="Auth")
    DebugLogging_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html#cfn-rds-dbproxy-debuglogging""", alias="DebugLogging")
    VpcSubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html#cfn-rds-dbproxy-vpcsubnetids""", alias="VpcSubnetIds")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html#cfn-rds-dbproxy-rolearn""", alias="RoleArn")
    EngineFamily_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html#cfn-rds-dbproxy-enginefamily""", alias="EngineFamily")
    Tags_: Optional[List['TagFormat']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html#cfn-rds-dbproxy-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.rds.DBProxy:
        from troposphere.rds import DBProxy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import DBProxy as TropoT
        return resource_to_troposphere(self, TropoT)


class DBProxyEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxyendpoint.html
    Properties:
        - Name: DBProxyEndpointName
        - Name: DBProxyName
        - Name: TargetRole
        - Name: VpcSecurityGroupIds
        - Name: VpcSubnetIds
        - Name: Tags
    Attributes:
        - Name: DBProxyEndpointArn
        - Name: IsDefault
        - Name: VpcId
        - Name: Endpoint
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DBProxyEndpointName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxyendpoint.html#cfn-rds-dbproxyendpoint-dbproxyendpointname""", alias="DBProxyEndpointName")
    DBProxyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxyendpoint.html#cfn-rds-dbproxyendpoint-dbproxyname""", alias="DBProxyName")
    TargetRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxyendpoint.html#cfn-rds-dbproxyendpoint-targetrole""", alias="TargetRole")
    VpcSecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxyendpoint.html#cfn-rds-dbproxyendpoint-vpcsecuritygroupids""", alias="VpcSecurityGroupIds")
    VpcSubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxyendpoint.html#cfn-rds-dbproxyendpoint-vpcsubnetids""", alias="VpcSubnetIds")
    Tags_: Optional[List['TagFormat']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxyendpoint.html#cfn-rds-dbproxyendpoint-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.rds.DBProxyEndpoint:
        from troposphere.rds import DBProxyEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import DBProxyEndpoint as TropoT
        return resource_to_troposphere(self, TropoT)


class DBProxyTargetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.html
    Properties:
        - Name: DBProxyName
        - Name: DBInstanceIdentifiers
        - Name: TargetGroupName
        - Name: ConnectionPoolConfigurationInfo
        - Name: DBClusterIdentifiers
    Attributes:
        - Name: TargetGroupArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DBProxyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.html#cfn-rds-dbproxytargetgroup-dbproxyname""", alias="DBProxyName")
    DBInstanceIdentifiers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.html#cfn-rds-dbproxytargetgroup-dbinstanceidentifiers""", alias="DBInstanceIdentifiers")
    TargetGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.html#cfn-rds-dbproxytargetgroup-targetgroupname""", alias="TargetGroupName")
    ConnectionPoolConfigurationInfo_: Optional['ConnectionPoolConfigurationInfoFormat'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.html#cfn-rds-dbproxytargetgroup-connectionpoolconfigurationinfo""", alias="ConnectionPoolConfigurationInfo")
    DBClusterIdentifiers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.html#cfn-rds-dbproxytargetgroup-dbclusteridentifiers""", alias="DBClusterIdentifiers")
    

    @property
    def tropo_type(self) -> troposphere.rds.DBProxyTargetGroup:
        from troposphere.rds import DBProxyTargetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import DBProxyTargetGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class DBSecurityGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html
    Properties:
        - Name: DBSecurityGroupIngress
        - Name: EC2VpcId
        - Name: GroupDescription
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DBSecurityGroupIngress_: List['Ingress'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html#cfn-rds-dbsecuritygroup-dbsecuritygroupingress""", alias="DBSecurityGroupIngress")
    EC2VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html#cfn-rds-dbsecuritygroup-ec2vpcid""", alias="EC2VpcId")
    GroupDescription_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html#cfn-rds-dbsecuritygroup-groupdescription""", alias="GroupDescription")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html#cfn-rds-dbsecuritygroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.rds.DBSecurityGroup:
        from troposphere.rds import DBSecurityGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import DBSecurityGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class DBSecurityGroupIngress(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html
    Properties:
        - Name: CIDRIP
        - Name: DBSecurityGroupName
        - Name: EC2SecurityGroupId
        - Name: EC2SecurityGroupName
        - Name: EC2SecurityGroupOwnerId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CIDRIP_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-cidrip""", alias="CIDRIP")
    DBSecurityGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-dbsecuritygroupname""", alias="DBSecurityGroupName")
    EC2SecurityGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-ec2securitygroupid""", alias="EC2SecurityGroupId")
    EC2SecurityGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-ec2securitygroupname""", alias="EC2SecurityGroupName")
    EC2SecurityGroupOwnerId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-ec2securitygroupownerid""", alias="EC2SecurityGroupOwnerId")
    

    @property
    def tropo_type(self) -> troposphere.rds.DBSecurityGroupIngress:
        from troposphere.rds import DBSecurityGroupIngress as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import DBSecurityGroupIngress as TropoT
        return resource_to_troposphere(self, TropoT)


class DBSubnetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnetgroup.html
    Properties:
        - Name: DBSubnetGroupName
        - Name: DBSubnetGroupDescription
        - Name: SubnetIds
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DBSubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnetgroup.html#cfn-rds-dbsubnetgroup-dbsubnetgroupname""", alias="DBSubnetGroupName")
    DBSubnetGroupDescription_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnetgroup.html#cfn-rds-dbsubnetgroup-dbsubnetgroupdescription""", alias="DBSubnetGroupDescription")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnetgroup.html#cfn-rds-dbsubnetgroup-subnetids""", alias="SubnetIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnetgroup.html#cfn-rds-dbsubnetgroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.rds.DBSubnetGroup:
        from troposphere.rds import DBSubnetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import DBSubnetGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class EventSubscription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html
    Properties:
        - Name: SourceType
        - Name: Enabled
        - Name: EventCategories
        - Name: SubscriptionName
        - Name: SnsTopicArn
        - Name: SourceIds
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-sourcetype""", alias="SourceType")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-enabled""", alias="Enabled")
    EventCategories_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-eventcategories""", alias="EventCategories")
    SubscriptionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-subscriptionname""", alias="SubscriptionName")
    SnsTopicArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-snstopicarn""", alias="SnsTopicArn")
    SourceIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-sourceids""", alias="SourceIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.rds.EventSubscription:
        from troposphere.rds import EventSubscription as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import EventSubscription as TropoT
        return resource_to_troposphere(self, TropoT)


class GlobalCluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html
    Properties:
        - Name: StorageEncrypted
        - Name: EngineVersion
        - Name: SourceDBClusterIdentifier
        - Name: DeletionProtection
        - Name: GlobalClusterIdentifier
        - Name: Engine
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StorageEncrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-storageencrypted""", alias="StorageEncrypted")
    EngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engineversion""", alias="EngineVersion")
    SourceDBClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-sourcedbclusteridentifier""", alias="SourceDBClusterIdentifier")
    DeletionProtection_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-deletionprotection""", alias="DeletionProtection")
    GlobalClusterIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-globalclusteridentifier""", alias="GlobalClusterIdentifier")
    Engine_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engine""", alias="Engine")
    

    @property
    def tropo_type(self) -> troposphere.rds.GlobalCluster:
        from troposphere.rds import GlobalCluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import GlobalCluster as TropoT
        return resource_to_troposphere(self, TropoT)


class OptionGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html
    Properties:
        - Name: OptionGroupDescription
        - Name: OptionGroupName
        - Name: OptionConfigurations
        - Name: MajorEngineVersion
        - Name: EngineName
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OptionGroupDescription_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-optiongroupdescription""", alias="OptionGroupDescription")
    OptionGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-optiongroupname""", alias="OptionGroupName")
    OptionConfigurations_: Optional[List['OptionConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-optionconfigurations""", alias="OptionConfigurations")
    MajorEngineVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-majorengineversion""", alias="MajorEngineVersion")
    EngineName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-enginename""", alias="EngineName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.rds.OptionGroup:
        from troposphere.rds import OptionGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.rds import OptionGroup as TropoT
        return resource_to_troposphere(self, TropoT)

