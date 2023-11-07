from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DocDbSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html
    Properties:
        - Name: DocsToInvestigate
        - Name: ExtractDocId
        - Name: SecretsManagerSecretId
        - Name: SecretsManagerAccessRoleArn
        - Name: NestingLevel
    
    """
    
    DocsToInvestigate_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-docstoinvestigate""", alias="DocsToInvestigate")
    ExtractDocId_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-extractdocid""", alias="ExtractDocId")
    SecretsManagerSecretId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-secretsmanagersecretid""", alias="SecretsManagerSecretId")
    SecretsManagerAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-secretsmanageraccessrolearn""", alias="SecretsManagerAccessRoleArn")
    NestingLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-nestinglevel""", alias="NestingLevel")
    


    @property
    def tropo_type(self) -> troposphere.dms.DocDbSettings:
        from troposphere.dms import DocDbSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynamoDbSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-dynamodbsettings.html
    Properties:
        - Name: ServiceAccessRoleArn
    
    """
    
    ServiceAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-dynamodbsettings.html#cfn-dms-endpoint-dynamodbsettings-serviceaccessrolearn""", alias="ServiceAccessRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.dms.DynamoDbSettings:
        from troposphere.dms import DynamoDbSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ElasticsearchSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html
    Properties:
        - Name: EndpointUri
        - Name: FullLoadErrorPercentage
        - Name: ErrorRetryDuration
        - Name: ServiceAccessRoleArn
    
    """
    
    EndpointUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html#cfn-dms-endpoint-elasticsearchsettings-endpointuri""", alias="EndpointUri")
    FullLoadErrorPercentage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html#cfn-dms-endpoint-elasticsearchsettings-fullloaderrorpercentage""", alias="FullLoadErrorPercentage")
    ErrorRetryDuration_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html#cfn-dms-endpoint-elasticsearchsettings-errorretryduration""", alias="ErrorRetryDuration")
    ServiceAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html#cfn-dms-endpoint-elasticsearchsettings-serviceaccessrolearn""", alias="ServiceAccessRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.dms.ElasticsearchSettings:
        from troposphere.dms import ElasticsearchSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GcpMySQLSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html
    Properties:
        - Name: AfterConnectScript
        - Name: Port
        - Name: DatabaseName
        - Name: CleanSourceMetadataOnMismatch
        - Name: ServerTimezone
        - Name: EventsPollInterval
        - Name: ParallelLoadThreads
        - Name: Username
        - Name: MaxFileSize
        - Name: ServerName
        - Name: SecretsManagerSecretId
        - Name: SecretsManagerAccessRoleArn
        - Name: Password
    
    """
    
    AfterConnectScript_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-afterconnectscript""", alias="AfterConnectScript")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-port""", alias="Port")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-databasename""", alias="DatabaseName")
    CleanSourceMetadataOnMismatch_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-cleansourcemetadataonmismatch""", alias="CleanSourceMetadataOnMismatch")
    ServerTimezone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-servertimezone""", alias="ServerTimezone")
    EventsPollInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-eventspollinterval""", alias="EventsPollInterval")
    ParallelLoadThreads_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-parallelloadthreads""", alias="ParallelLoadThreads")
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-username""", alias="Username")
    MaxFileSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-maxfilesize""", alias="MaxFileSize")
    ServerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-servername""", alias="ServerName")
    SecretsManagerSecretId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-secretsmanagersecretid""", alias="SecretsManagerSecretId")
    SecretsManagerAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-secretsmanageraccessrolearn""", alias="SecretsManagerAccessRoleArn")
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.dms.GcpMySQLSettings:
        from troposphere.dms import GcpMySQLSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IbmDb2Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html
    Properties:
        - Name: SetDataCaptureChanges
        - Name: CurrentLsn
        - Name: MaxKBytesPerRead
        - Name: SecretsManagerSecretId
        - Name: SecretsManagerAccessRoleArn
    
    """
    
    SetDataCaptureChanges_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-setdatacapturechanges""", alias="SetDataCaptureChanges")
    CurrentLsn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-currentlsn""", alias="CurrentLsn")
    MaxKBytesPerRead_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-maxkbytesperread""", alias="MaxKBytesPerRead")
    SecretsManagerSecretId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-secretsmanagersecretid""", alias="SecretsManagerSecretId")
    SecretsManagerAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-secretsmanageraccessrolearn""", alias="SecretsManagerAccessRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.dms.IbmDb2Settings:
        from troposphere.dms import IbmDb2Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KafkaSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html
    Properties:
        - Name: Broker
        - Name: SaslPassword
        - Name: MessageFormat
        - Name: SslClientCertificateArn
        - Name: IncludeTransactionDetails
        - Name: SecurityProtocol
        - Name: IncludeTableAlterOperations
        - Name: SslCaCertificateArn
        - Name: IncludeControlDetails
        - Name: IncludePartitionValue
        - Name: NoHexPrefix
        - Name: SslClientKeyArn
        - Name: SslClientKeyPassword
        - Name: SaslUserName
        - Name: MessageMaxBytes
        - Name: Topic
        - Name: PartitionIncludeSchemaTable
        - Name: IncludeNullAndEmpty
    
    """
    
    Broker_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-broker""", alias="Broker")
    SaslPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-saslpassword""", alias="SaslPassword")
    MessageFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-messageformat""", alias="MessageFormat")
    SslClientCertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-sslclientcertificatearn""", alias="SslClientCertificateArn")
    IncludeTransactionDetails_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includetransactiondetails""", alias="IncludeTransactionDetails")
    SecurityProtocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-securityprotocol""", alias="SecurityProtocol")
    IncludeTableAlterOperations_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includetablealteroperations""", alias="IncludeTableAlterOperations")
    SslCaCertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-sslcacertificatearn""", alias="SslCaCertificateArn")
    IncludeControlDetails_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includecontroldetails""", alias="IncludeControlDetails")
    IncludePartitionValue_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includepartitionvalue""", alias="IncludePartitionValue")
    NoHexPrefix_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-nohexprefix""", alias="NoHexPrefix")
    SslClientKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-sslclientkeyarn""", alias="SslClientKeyArn")
    SslClientKeyPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-sslclientkeypassword""", alias="SslClientKeyPassword")
    SaslUserName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-saslusername""", alias="SaslUserName")
    MessageMaxBytes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-messagemaxbytes""", alias="MessageMaxBytes")
    Topic_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-topic""", alias="Topic")
    PartitionIncludeSchemaTable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-partitionincludeschematable""", alias="PartitionIncludeSchemaTable")
    IncludeNullAndEmpty_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includenullandempty""", alias="IncludeNullAndEmpty")
    


    @property
    def tropo_type(self) -> troposphere.dms.KafkaSettings:
        from troposphere.dms import KafkaSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html
    Properties:
        - Name: MessageFormat
        - Name: IncludeTransactionDetails
        - Name: IncludeTableAlterOperations
        - Name: IncludeControlDetails
        - Name: IncludePartitionValue
        - Name: StreamArn
        - Name: ServiceAccessRoleArn
        - Name: NoHexPrefix
        - Name: PartitionIncludeSchemaTable
        - Name: IncludeNullAndEmpty
    
    """
    
    MessageFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-messageformat""", alias="MessageFormat")
    IncludeTransactionDetails_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includetransactiondetails""", alias="IncludeTransactionDetails")
    IncludeTableAlterOperations_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includetablealteroperations""", alias="IncludeTableAlterOperations")
    IncludeControlDetails_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includecontroldetails""", alias="IncludeControlDetails")
    IncludePartitionValue_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includepartitionvalue""", alias="IncludePartitionValue")
    StreamArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-streamarn""", alias="StreamArn")
    ServiceAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-serviceaccessrolearn""", alias="ServiceAccessRoleArn")
    NoHexPrefix_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-nohexprefix""", alias="NoHexPrefix")
    PartitionIncludeSchemaTable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-partitionincludeschematable""", alias="PartitionIncludeSchemaTable")
    IncludeNullAndEmpty_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includenullandempty""", alias="IncludeNullAndEmpty")
    


    @property
    def tropo_type(self) -> troposphere.dms.KinesisSettings:
        from troposphere.dms import KinesisSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MicrosoftSqlServerSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html
    Properties:
        - Name: ReadBackupOnly
        - Name: TlogAccessMode
        - Name: BcpPacketSize
        - Name: Port
        - Name: SafeguardPolicy
        - Name: UseThirdPartyBackupDevice
        - Name: DatabaseName
        - Name: UseBcpFullLoad
        - Name: Username
        - Name: QuerySingleAlwaysOnNode
        - Name: ServerName
        - Name: SecretsManagerSecretId
        - Name: ControlTablesFileGroup
        - Name: ForceLobLookup
        - Name: SecretsManagerAccessRoleArn
        - Name: TrimSpaceInChar
        - Name: Password
    
    """
    
    ReadBackupOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-readbackuponly""", alias="ReadBackupOnly")
    TlogAccessMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-tlogaccessmode""", alias="TlogAccessMode")
    BcpPacketSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-bcppacketsize""", alias="BcpPacketSize")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-port""", alias="Port")
    SafeguardPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-safeguardpolicy""", alias="SafeguardPolicy")
    UseThirdPartyBackupDevice_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-usethirdpartybackupdevice""", alias="UseThirdPartyBackupDevice")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-databasename""", alias="DatabaseName")
    UseBcpFullLoad_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-usebcpfullload""", alias="UseBcpFullLoad")
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-username""", alias="Username")
    QuerySingleAlwaysOnNode_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-querysinglealwaysonnode""", alias="QuerySingleAlwaysOnNode")
    ServerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-servername""", alias="ServerName")
    SecretsManagerSecretId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-secretsmanagersecretid""", alias="SecretsManagerSecretId")
    ControlTablesFileGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-controltablesfilegroup""", alias="ControlTablesFileGroup")
    ForceLobLookup_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-forceloblookup""", alias="ForceLobLookup")
    SecretsManagerAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-secretsmanageraccessrolearn""", alias="SecretsManagerAccessRoleArn")
    TrimSpaceInChar_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-trimspaceinchar""", alias="TrimSpaceInChar")
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.dms.MicrosoftSqlServerSettings:
        from troposphere.dms import MicrosoftSqlServerSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MongoDbSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html
    Properties:
        - Name: Port
        - Name: ExtractDocId
        - Name: DatabaseName
        - Name: AuthSource
        - Name: AuthMechanism
        - Name: Username
        - Name: DocsToInvestigate
        - Name: ServerName
        - Name: SecretsManagerSecretId
        - Name: AuthType
        - Name: SecretsManagerAccessRoleArn
        - Name: Password
        - Name: NestingLevel
    
    """
    
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-port""", alias="Port")
    ExtractDocId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-extractdocid""", alias="ExtractDocId")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-databasename""", alias="DatabaseName")
    AuthSource_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-authsource""", alias="AuthSource")
    AuthMechanism_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-authmechanism""", alias="AuthMechanism")
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-username""", alias="Username")
    DocsToInvestigate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-docstoinvestigate""", alias="DocsToInvestigate")
    ServerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-servername""", alias="ServerName")
    SecretsManagerSecretId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-secretsmanagersecretid""", alias="SecretsManagerSecretId")
    AuthType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-authtype""", alias="AuthType")
    SecretsManagerAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-secretsmanageraccessrolearn""", alias="SecretsManagerAccessRoleArn")
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-password""", alias="Password")
    NestingLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-nestinglevel""", alias="NestingLevel")
    


    @property
    def tropo_type(self) -> troposphere.dms.MongoDbSettings:
        from troposphere.dms import MongoDbSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MySqlSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html
    Properties:
        - Name: ServerTimezone
        - Name: EventsPollInterval
        - Name: ParallelLoadThreads
        - Name: AfterConnectScript
        - Name: MaxFileSize
        - Name: TargetDbType
        - Name: SecretsManagerSecretId
        - Name: SecretsManagerAccessRoleArn
        - Name: CleanSourceMetadataOnMismatch
    
    """
    
    ServerTimezone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-servertimezone""", alias="ServerTimezone")
    EventsPollInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-eventspollinterval""", alias="EventsPollInterval")
    ParallelLoadThreads_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-parallelloadthreads""", alias="ParallelLoadThreads")
    AfterConnectScript_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-afterconnectscript""", alias="AfterConnectScript")
    MaxFileSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-maxfilesize""", alias="MaxFileSize")
    TargetDbType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-targetdbtype""", alias="TargetDbType")
    SecretsManagerSecretId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-secretsmanagersecretid""", alias="SecretsManagerSecretId")
    SecretsManagerAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-secretsmanageraccessrolearn""", alias="SecretsManagerAccessRoleArn")
    CleanSourceMetadataOnMismatch_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-cleansourcemetadataonmismatch""", alias="CleanSourceMetadataOnMismatch")
    


    @property
    def tropo_type(self) -> troposphere.dms.MySqlSettings:
        from troposphere.dms import MySqlSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NeptuneSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html
    Properties:
        - Name: MaxRetryCount
        - Name: MaxFileSize
        - Name: S3BucketFolder
        - Name: ErrorRetryDuration
        - Name: IamAuthEnabled
        - Name: S3BucketName
        - Name: ServiceAccessRoleArn
    
    """
    
    MaxRetryCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-maxretrycount""", alias="MaxRetryCount")
    MaxFileSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-maxfilesize""", alias="MaxFileSize")
    S3BucketFolder_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-s3bucketfolder""", alias="S3BucketFolder")
    ErrorRetryDuration_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-errorretryduration""", alias="ErrorRetryDuration")
    IamAuthEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-iamauthenabled""", alias="IamAuthEnabled")
    S3BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-s3bucketname""", alias="S3BucketName")
    ServiceAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-serviceaccessrolearn""", alias="ServiceAccessRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.dms.NeptuneSettings:
        from troposphere.dms import NeptuneSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OracleSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html
    Properties:
        - Name: AsmPassword
        - Name: DirectPathParallelLoad
        - Name: AdditionalArchivedLogDestId
        - Name: SpatialDataOptionToGeoJsonFunctionName
        - Name: ReplacePathPrefix
        - Name: FailTasksOnLobTruncation
        - Name: AsmServer
        - Name: SecretsManagerOracleAsmAccessRoleArn
        - Name: OraclePathPrefix
        - Name: ReadAheadBlocks
        - Name: StandbyDelayTime
        - Name: AllowSelectNestedTables
        - Name: AddSupplementalLogging
        - Name: SecretsManagerSecretId
        - Name: UseBFile
        - Name: EnableHomogenousTablespace
        - Name: AsmUser
        - Name: UseDirectPathFullLoad
        - Name: SecurityDbEncryption
        - Name: ParallelAsmReadThreads
        - Name: ArchivedLogDestId
        - Name: UsePathPrefix
        - Name: UseLogminerReader
        - Name: SecurityDbEncryptionName
        - Name: DirectPathNoLog
        - Name: SecretsManagerOracleAsmSecretId
        - Name: CharLengthSemantics
        - Name: NumberDatatypeScale
        - Name: ReadTableSpaceName
        - Name: AccessAlternateDirectly
        - Name: UseAlternateFolderForOnline
        - Name: ArchivedLogsOnly
        - Name: ExtraArchivedLogDestIds
        - Name: RetryInterval
        - Name: SecretsManagerAccessRoleArn
    
    """
    
    AsmPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-asmpassword""", alias="AsmPassword")
    DirectPathParallelLoad_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-directpathparallelload""", alias="DirectPathParallelLoad")
    AdditionalArchivedLogDestId_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-additionalarchivedlogdestid""", alias="AdditionalArchivedLogDestId")
    SpatialDataOptionToGeoJsonFunctionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-spatialdataoptiontogeojsonfunctionname""", alias="SpatialDataOptionToGeoJsonFunctionName")
    ReplacePathPrefix_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-replacepathprefix""", alias="ReplacePathPrefix")
    FailTasksOnLobTruncation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-failtasksonlobtruncation""", alias="FailTasksOnLobTruncation")
    AsmServer_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-asmserver""", alias="AsmServer")
    SecretsManagerOracleAsmAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-secretsmanageroracleasmaccessrolearn""", alias="SecretsManagerOracleAsmAccessRoleArn")
    OraclePathPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-oraclepathprefix""", alias="OraclePathPrefix")
    ReadAheadBlocks_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-readaheadblocks""", alias="ReadAheadBlocks")
    StandbyDelayTime_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-standbydelaytime""", alias="StandbyDelayTime")
    AllowSelectNestedTables_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-allowselectnestedtables""", alias="AllowSelectNestedTables")
    AddSupplementalLogging_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-addsupplementallogging""", alias="AddSupplementalLogging")
    SecretsManagerSecretId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-secretsmanagersecretid""", alias="SecretsManagerSecretId")
    UseBFile_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-usebfile""", alias="UseBFile")
    EnableHomogenousTablespace_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-enablehomogenoustablespace""", alias="EnableHomogenousTablespace")
    AsmUser_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-asmuser""", alias="AsmUser")
    UseDirectPathFullLoad_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-usedirectpathfullload""", alias="UseDirectPathFullLoad")
    SecurityDbEncryption_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-securitydbencryption""", alias="SecurityDbEncryption")
    ParallelAsmReadThreads_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-parallelasmreadthreads""", alias="ParallelAsmReadThreads")
    ArchivedLogDestId_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-archivedlogdestid""", alias="ArchivedLogDestId")
    UsePathPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-usepathprefix""", alias="UsePathPrefix")
    UseLogminerReader_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-uselogminerreader""", alias="UseLogminerReader")
    SecurityDbEncryptionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-securitydbencryptionname""", alias="SecurityDbEncryptionName")
    DirectPathNoLog_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-directpathnolog""", alias="DirectPathNoLog")
    SecretsManagerOracleAsmSecretId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-secretsmanageroracleasmsecretid""", alias="SecretsManagerOracleAsmSecretId")
    CharLengthSemantics_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-charlengthsemantics""", alias="CharLengthSemantics")
    NumberDatatypeScale_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-numberdatatypescale""", alias="NumberDatatypeScale")
    ReadTableSpaceName_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-readtablespacename""", alias="ReadTableSpaceName")
    AccessAlternateDirectly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-accessalternatedirectly""", alias="AccessAlternateDirectly")
    UseAlternateFolderForOnline_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-usealternatefolderforonline""", alias="UseAlternateFolderForOnline")
    ArchivedLogsOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-archivedlogsonly""", alias="ArchivedLogsOnly")
    ExtraArchivedLogDestIds_: Optional[List[int]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-extraarchivedlogdestids""", alias="ExtraArchivedLogDestIds")
    RetryInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-retryinterval""", alias="RetryInterval")
    SecretsManagerAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-secretsmanageraccessrolearn""", alias="SecretsManagerAccessRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.dms.OracleSettings:
        from troposphere.dms import OracleSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PostgreSqlSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html
    Properties:
        - Name: PluginName
        - Name: MapBooleanAsBoolean
        - Name: AfterConnectScript
        - Name: ExecuteTimeout
        - Name: DdlArtifactsSchema
        - Name: FailTasksOnLobTruncation
        - Name: HeartbeatEnable
        - Name: BabelfishDatabaseName
        - Name: DatabaseMode
        - Name: CaptureDdls
        - Name: MaxFileSize
        - Name: HeartbeatFrequency
        - Name: SecretsManagerSecretId
        - Name: SecretsManagerAccessRoleArn
        - Name: HeartbeatSchema
        - Name: SlotName
    
    """
    
    PluginName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-pluginname""", alias="PluginName")
    MapBooleanAsBoolean_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-mapbooleanasboolean""", alias="MapBooleanAsBoolean")
    AfterConnectScript_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-afterconnectscript""", alias="AfterConnectScript")
    ExecuteTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-executetimeout""", alias="ExecuteTimeout")
    DdlArtifactsSchema_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-ddlartifactsschema""", alias="DdlArtifactsSchema")
    FailTasksOnLobTruncation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-failtasksonlobtruncation""", alias="FailTasksOnLobTruncation")
    HeartbeatEnable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-heartbeatenable""", alias="HeartbeatEnable")
    BabelfishDatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-babelfishdatabasename""", alias="BabelfishDatabaseName")
    DatabaseMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-databasemode""", alias="DatabaseMode")
    CaptureDdls_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-captureddls""", alias="CaptureDdls")
    MaxFileSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-maxfilesize""", alias="MaxFileSize")
    HeartbeatFrequency_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-heartbeatfrequency""", alias="HeartbeatFrequency")
    SecretsManagerSecretId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-secretsmanagersecretid""", alias="SecretsManagerSecretId")
    SecretsManagerAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-secretsmanageraccessrolearn""", alias="SecretsManagerAccessRoleArn")
    HeartbeatSchema_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-heartbeatschema""", alias="HeartbeatSchema")
    SlotName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-slotname""", alias="SlotName")
    


    @property
    def tropo_type(self) -> troposphere.dms.PostgreSqlSettings:
        from troposphere.dms import PostgreSqlSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RedisSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html
    Properties:
        - Name: SslSecurityProtocol
        - Name: AuthUserName
        - Name: ServerName
        - Name: Port
        - Name: SslCaCertificateArn
        - Name: AuthPassword
        - Name: AuthType
    
    """
    
    SslSecurityProtocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-sslsecurityprotocol""", alias="SslSecurityProtocol")
    AuthUserName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-authusername""", alias="AuthUserName")
    ServerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-servername""", alias="ServerName")
    Port_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-port""", alias="Port")
    SslCaCertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-sslcacertificatearn""", alias="SslCaCertificateArn")
    AuthPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-authpassword""", alias="AuthPassword")
    AuthType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-authtype""", alias="AuthType")
    


    @property
    def tropo_type(self) -> troposphere.dms.RedisSettings:
        from troposphere.dms import RedisSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RedshiftSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html
    Properties:
        - Name: ConnectionTimeout
        - Name: MapBooleanAsBoolean
        - Name: AfterConnectScript
        - Name: FileTransferUploadStreams
        - Name: BucketName
        - Name: ServerSideEncryptionKmsKeyId
        - Name: ExplicitIds
        - Name: SecretsManagerSecretId
        - Name: TruncateColumns
        - Name: ServiceAccessRoleArn
        - Name: ReplaceChars
        - Name: TimeFormat
        - Name: BucketFolder
        - Name: ReplaceInvalidChars
        - Name: RemoveQuotes
        - Name: LoadTimeout
        - Name: MaxFileSize
        - Name: TrimBlanks
        - Name: DateFormat
        - Name: CompUpdate
        - Name: AcceptAnyDate
        - Name: WriteBufferSize
        - Name: SecretsManagerAccessRoleArn
        - Name: CaseSensitiveNames
        - Name: EmptyAsNull
        - Name: EncryptionMode
    
    """
    
    ConnectionTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-connectiontimeout""", alias="ConnectionTimeout")
    MapBooleanAsBoolean_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-mapbooleanasboolean""", alias="MapBooleanAsBoolean")
    AfterConnectScript_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-afterconnectscript""", alias="AfterConnectScript")
    FileTransferUploadStreams_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-filetransferuploadstreams""", alias="FileTransferUploadStreams")
    BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-bucketname""", alias="BucketName")
    ServerSideEncryptionKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-serversideencryptionkmskeyid""", alias="ServerSideEncryptionKmsKeyId")
    ExplicitIds_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-explicitids""", alias="ExplicitIds")
    SecretsManagerSecretId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-secretsmanagersecretid""", alias="SecretsManagerSecretId")
    TruncateColumns_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-truncatecolumns""", alias="TruncateColumns")
    ServiceAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-serviceaccessrolearn""", alias="ServiceAccessRoleArn")
    ReplaceChars_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-replacechars""", alias="ReplaceChars")
    TimeFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-timeformat""", alias="TimeFormat")
    BucketFolder_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-bucketfolder""", alias="BucketFolder")
    ReplaceInvalidChars_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-replaceinvalidchars""", alias="ReplaceInvalidChars")
    RemoveQuotes_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-removequotes""", alias="RemoveQuotes")
    LoadTimeout_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-loadtimeout""", alias="LoadTimeout")
    MaxFileSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-maxfilesize""", alias="MaxFileSize")
    TrimBlanks_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-trimblanks""", alias="TrimBlanks")
    DateFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-dateformat""", alias="DateFormat")
    CompUpdate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-compupdate""", alias="CompUpdate")
    AcceptAnyDate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-acceptanydate""", alias="AcceptAnyDate")
    WriteBufferSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-writebuffersize""", alias="WriteBufferSize")
    SecretsManagerAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-secretsmanageraccessrolearn""", alias="SecretsManagerAccessRoleArn")
    CaseSensitiveNames_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-casesensitivenames""", alias="CaseSensitiveNames")
    EmptyAsNull_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-emptyasnull""", alias="EmptyAsNull")
    EncryptionMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-encryptionmode""", alias="EncryptionMode")
    


    @property
    def tropo_type(self) -> troposphere.dms.RedshiftSettings:
        from troposphere.dms import RedshiftSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html
    Properties:
        - Name: TimestampColumnName
        - Name: EnableStatistics
        - Name: DatePartitionSequence
        - Name: IncludeOpForFullLoad
        - Name: CsvNullValue
        - Name: CdcInsertsAndUpdates
        - Name: BucketName
        - Name: ServerSideEncryptionKmsKeyId
        - Name: UseTaskStartTimeForFullLoadTimestamp
        - Name: DataFormat
        - Name: CsvDelimiter
        - Name: IgnoreHeaderRows
        - Name: CannedAclForObjects
        - Name: Rfc4180
        - Name: ServiceAccessRoleArn
        - Name: ParquetTimestampInMillisecond
        - Name: PreserveTransactions
        - Name: BucketFolder
        - Name: DatePartitionDelimiter
        - Name: EncodingType
        - Name: ParquetVersion
        - Name: AddColumnName
        - Name: CdcMinFileSize
        - Name: ExternalTableDefinition
        - Name: UseCsvNoSupValue
        - Name: MaxFileSize
        - Name: CsvNoSupValue
        - Name: CdcPath
        - Name: CsvRowDelimiter
        - Name: RowGroupLength
        - Name: CdcMaxBatchInterval
        - Name: DataPageSize
        - Name: DictPageSizeLimit
        - Name: DatePartitionEnabled
        - Name: CompressionType
        - Name: DatePartitionTimezone
        - Name: CdcInsertsOnly
        - Name: EncryptionMode
    
    """
    
    TimestampColumnName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-timestampcolumnname""", alias="TimestampColumnName")
    EnableStatistics_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-enablestatistics""", alias="EnableStatistics")
    DatePartitionSequence_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datepartitionsequence""", alias="DatePartitionSequence")
    IncludeOpForFullLoad_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-includeopforfullload""", alias="IncludeOpForFullLoad")
    CsvNullValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-csvnullvalue""", alias="CsvNullValue")
    CdcInsertsAndUpdates_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcinsertsandupdates""", alias="CdcInsertsAndUpdates")
    BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-bucketname""", alias="BucketName")
    ServerSideEncryptionKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-serversideencryptionkmskeyid""", alias="ServerSideEncryptionKmsKeyId")
    UseTaskStartTimeForFullLoadTimestamp_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-usetaskstarttimeforfullloadtimestamp""", alias="UseTaskStartTimeForFullLoadTimestamp")
    DataFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-dataformat""", alias="DataFormat")
    CsvDelimiter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-csvdelimiter""", alias="CsvDelimiter")
    IgnoreHeaderRows_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-ignoreheaderrows""", alias="IgnoreHeaderRows")
    CannedAclForObjects_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cannedaclforobjects""", alias="CannedAclForObjects")
    Rfc4180_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-rfc4180""", alias="Rfc4180")
    ServiceAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-serviceaccessrolearn""", alias="ServiceAccessRoleArn")
    ParquetTimestampInMillisecond_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-parquettimestampinmillisecond""", alias="ParquetTimestampInMillisecond")
    PreserveTransactions_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-preservetransactions""", alias="PreserveTransactions")
    BucketFolder_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-bucketfolder""", alias="BucketFolder")
    DatePartitionDelimiter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datepartitiondelimiter""", alias="DatePartitionDelimiter")
    EncodingType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-encodingtype""", alias="EncodingType")
    ParquetVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-parquetversion""", alias="ParquetVersion")
    AddColumnName_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-addcolumnname""", alias="AddColumnName")
    CdcMinFileSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcminfilesize""", alias="CdcMinFileSize")
    ExternalTableDefinition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-externaltabledefinition""", alias="ExternalTableDefinition")
    UseCsvNoSupValue_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-usecsvnosupvalue""", alias="UseCsvNoSupValue")
    MaxFileSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-maxfilesize""", alias="MaxFileSize")
    CsvNoSupValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-csvnosupvalue""", alias="CsvNoSupValue")
    CdcPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcpath""", alias="CdcPath")
    CsvRowDelimiter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-csvrowdelimiter""", alias="CsvRowDelimiter")
    RowGroupLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-rowgrouplength""", alias="RowGroupLength")
    CdcMaxBatchInterval_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcmaxbatchinterval""", alias="CdcMaxBatchInterval")
    DataPageSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datapagesize""", alias="DataPageSize")
    DictPageSizeLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-dictpagesizelimit""", alias="DictPageSizeLimit")
    DatePartitionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datepartitionenabled""", alias="DatePartitionEnabled")
    CompressionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-compressiontype""", alias="CompressionType")
    DatePartitionTimezone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datepartitiontimezone""", alias="DatePartitionTimezone")
    CdcInsertsOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcinsertsonly""", alias="CdcInsertsOnly")
    EncryptionMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-encryptionmode""", alias="EncryptionMode")
    


    @property
    def tropo_type(self) -> troposphere.dms.S3Settings:
        from troposphere.dms import S3Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SybaseSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-sybasesettings.html
    Properties:
        - Name: SecretsManagerSecretId
        - Name: SecretsManagerAccessRoleArn
    
    """
    
    SecretsManagerSecretId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-sybasesettings.html#cfn-dms-endpoint-sybasesettings-secretsmanagersecretid""", alias="SecretsManagerSecretId")
    SecretsManagerAccessRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-sybasesettings.html#cfn-dms-endpoint-sybasesettings-secretsmanageraccessrolearn""", alias="SecretsManagerAccessRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.dms.SybaseSettings:
        from troposphere.dms import SybaseSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComputeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html
    Properties:
        - Name: DnsNameServers
        - Name: KmsKeyId
        - Name: VpcSecurityGroupIds
        - Name: MaxCapacityUnits
        - Name: ReplicationSubnetGroupId
        - Name: AvailabilityZone
        - Name: PreferredMaintenanceWindow
        - Name: MinCapacityUnits
        - Name: MultiAZ
    
    """
    
    DnsNameServers_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-dnsnameservers""", alias="DnsNameServers")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-kmskeyid""", alias="KmsKeyId")
    VpcSecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-vpcsecuritygroupids""", alias="VpcSecurityGroupIds")
    MaxCapacityUnits_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-maxcapacityunits""", alias="MaxCapacityUnits")
    ReplicationSubnetGroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-replicationsubnetgroupid""", alias="ReplicationSubnetGroupId")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-availabilityzone""", alias="AvailabilityZone")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    MinCapacityUnits_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-mincapacityunits""", alias="MinCapacityUnits")
    MultiAZ_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-multiaz""", alias="MultiAZ")
    


    @property
    def tropo_type(self) -> troposphere.dms.ComputeConfig:
        from troposphere.dms import ComputeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Certificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html
    Properties:
        - Name: CertificateIdentifier
        - Name: CertificatePem
        - Name: CertificateWallet
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CertificateIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html#cfn-dms-certificate-certificateidentifier""", alias="CertificateIdentifier")
    CertificatePem_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html#cfn-dms-certificate-certificatepem""", alias="CertificatePem")
    CertificateWallet_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html#cfn-dms-certificate-certificatewallet""", alias="CertificateWallet")
    

    @property
    def tropo_type(self) -> troposphere.dms.Certificate:
        from troposphere.dms import Certificate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.dms import Certificate as TropoT
        return resource_to_troposphere(self, TropoT)


class Endpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html
    Properties:
        - Name: SybaseSettings
        - Name: RedisSettings
        - Name: OracleSettings
        - Name: KafkaSettings
        - Name: Port
        - Name: MySqlSettings
        - Name: S3Settings
        - Name: ResourceIdentifier
        - Name: KinesisSettings
        - Name: SslMode
        - Name: RedshiftSettings
        - Name: EndpointType
        - Name: Tags
        - Name: Password
        - Name: MongoDbSettings
        - Name: IbmDb2Settings
        - Name: KmsKeyId
        - Name: DatabaseName
        - Name: NeptuneSettings
        - Name: ElasticsearchSettings
        - Name: EngineName
        - Name: DocDbSettings
        - Name: DynamoDbSettings
        - Name: Username
        - Name: MicrosoftSqlServerSettings
        - Name: GcpMySQLSettings
        - Name: ServerName
        - Name: ExtraConnectionAttributes
        - Name: EndpointIdentifier
        - Name: CertificateArn
        - Name: PostgreSqlSettings
    Attributes:
        - Name: ExternalId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SybaseSettings_: Optional['SybaseSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-sybasesettings""", alias="SybaseSettings")
    RedisSettings_: Optional['RedisSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-redissettings""", alias="RedisSettings")
    OracleSettings_: Optional['OracleSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-oraclesettings""", alias="OracleSettings")
    KafkaSettings_: Optional['KafkaSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-kafkasettings""", alias="KafkaSettings")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-port""", alias="Port")
    MySqlSettings_: Optional['MySqlSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-mysqlsettings""", alias="MySqlSettings")
    S3Settings_: Optional['S3Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-s3settings""", alias="S3Settings")
    ResourceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-resourceidentifier""", alias="ResourceIdentifier")
    KinesisSettings_: Optional['KinesisSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-kinesissettings""", alias="KinesisSettings")
    SslMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-sslmode""", alias="SslMode")
    RedshiftSettings_: Optional['RedshiftSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-redshiftsettings""", alias="RedshiftSettings")
    EndpointType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-endpointtype""", alias="EndpointType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-tags""", alias="Tags")
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-password""", alias="Password")
    MongoDbSettings_: Optional['MongoDbSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-mongodbsettings""", alias="MongoDbSettings")
    IbmDb2Settings_: Optional['IbmDb2Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-ibmdb2settings""", alias="IbmDb2Settings")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-kmskeyid""", alias="KmsKeyId")
    DatabaseName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-databasename""", alias="DatabaseName")
    NeptuneSettings_: Optional['NeptuneSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-neptunesettings""", alias="NeptuneSettings")
    ElasticsearchSettings_: Optional['ElasticsearchSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-elasticsearchsettings""", alias="ElasticsearchSettings")
    EngineName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-enginename""", alias="EngineName")
    DocDbSettings_: Optional['DocDbSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-docdbsettings""", alias="DocDbSettings")
    DynamoDbSettings_: Optional['DynamoDbSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-dynamodbsettings""", alias="DynamoDbSettings")
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-username""", alias="Username")
    MicrosoftSqlServerSettings_: Optional['MicrosoftSqlServerSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-microsoftsqlserversettings""", alias="MicrosoftSqlServerSettings")
    GcpMySQLSettings_: Optional['GcpMySQLSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-gcpmysqlsettings""", alias="GcpMySQLSettings")
    ServerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-servername""", alias="ServerName")
    ExtraConnectionAttributes_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-extraconnectionattributes""", alias="ExtraConnectionAttributes")
    EndpointIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-endpointidentifier""", alias="EndpointIdentifier")
    CertificateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-certificatearn""", alias="CertificateArn")
    PostgreSqlSettings_: Optional['PostgreSqlSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-postgresqlsettings""", alias="PostgreSqlSettings")
    

    @property
    def tropo_type(self) -> troposphere.dms.Endpoint:
        from troposphere.dms import Endpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.dms import Endpoint as TropoT
        return resource_to_troposphere(self, TropoT)


class EventSubscription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html
    Properties:
        - Name: SourceType
        - Name: EventCategories
        - Name: Enabled
        - Name: SubscriptionName
        - Name: SnsTopicArn
        - Name: SourceIds
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-sourcetype""", alias="SourceType")
    EventCategories_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-eventcategories""", alias="EventCategories")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-enabled""", alias="Enabled")
    SubscriptionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-subscriptionname""", alias="SubscriptionName")
    SnsTopicArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-snstopicarn""", alias="SnsTopicArn")
    SourceIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-sourceids""", alias="SourceIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.dms.EventSubscription:
        from troposphere.dms import EventSubscription as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.dms import EventSubscription as TropoT
        return resource_to_troposphere(self, TropoT)


class ReplicationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html
    Properties:
        - Name: ReplicationSettings
        - Name: ResourceIdentifier
        - Name: ReplicationConfigIdentifier
        - Name: ComputeConfig
        - Name: ReplicationType
        - Name: TableMappings
        - Name: SourceEndpointArn
        - Name: ReplicationConfigArn
        - Name: SupplementalSettings
        - Name: TargetEndpointArn
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ReplicationSettings_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-replicationsettings""", alias="ReplicationSettings")
    ResourceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-resourceidentifier""", alias="ResourceIdentifier")
    ReplicationConfigIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-replicationconfigidentifier""", alias="ReplicationConfigIdentifier")
    ComputeConfig_: Optional['ComputeConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-computeconfig""", alias="ComputeConfig")
    ReplicationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-replicationtype""", alias="ReplicationType")
    TableMappings_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-tablemappings""", alias="TableMappings")
    SourceEndpointArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-sourceendpointarn""", alias="SourceEndpointArn")
    ReplicationConfigArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-replicationconfigarn""", alias="ReplicationConfigArn")
    SupplementalSettings_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-supplementalsettings""", alias="SupplementalSettings")
    TargetEndpointArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-targetendpointarn""", alias="TargetEndpointArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.dms.ReplicationConfig:
        from troposphere.dms import ReplicationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.dms import ReplicationConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class ReplicationInstance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html
    Properties:
        - Name: ReplicationInstanceIdentifier
        - Name: EngineVersion
        - Name: KmsKeyId
        - Name: AvailabilityZone
        - Name: PreferredMaintenanceWindow
        - Name: AutoMinorVersionUpgrade
        - Name: ReplicationSubnetGroupIdentifier
        - Name: AllocatedStorage
        - Name: ResourceIdentifier
        - Name: VpcSecurityGroupIds
        - Name: AllowMajorVersionUpgrade
        - Name: ReplicationInstanceClass
        - Name: PubliclyAccessible
        - Name: MultiAZ
        - Name: Tags
    Attributes:
        - Name: ReplicationInstancePublicIpAddresses
        - Name: ReplicationInstancePrivateIpAddresses
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ReplicationInstanceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-replicationinstanceidentifier""", alias="ReplicationInstanceIdentifier")
    EngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-engineversion""", alias="EngineVersion")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-kmskeyid""", alias="KmsKeyId")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-availabilityzone""", alias="AvailabilityZone")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    AutoMinorVersionUpgrade_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-autominorversionupgrade""", alias="AutoMinorVersionUpgrade")
    ReplicationSubnetGroupIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-replicationsubnetgroupidentifier""", alias="ReplicationSubnetGroupIdentifier")
    AllocatedStorage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-allocatedstorage""", alias="AllocatedStorage")
    ResourceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-resourceidentifier""", alias="ResourceIdentifier")
    VpcSecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-vpcsecuritygroupids""", alias="VpcSecurityGroupIds")
    AllowMajorVersionUpgrade_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-allowmajorversionupgrade""", alias="AllowMajorVersionUpgrade")
    ReplicationInstanceClass_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-replicationinstanceclass""", alias="ReplicationInstanceClass")
    PubliclyAccessible_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-publiclyaccessible""", alias="PubliclyAccessible")
    MultiAZ_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-multiaz""", alias="MultiAZ")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.dms.ReplicationInstance:
        from troposphere.dms import ReplicationInstance as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.dms import ReplicationInstance as TropoT
        return resource_to_troposphere(self, TropoT)


class ReplicationSubnetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html
    Properties:
        - Name: ReplicationSubnetGroupDescription
        - Name: ReplicationSubnetGroupIdentifier
        - Name: SubnetIds
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ReplicationSubnetGroupDescription_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-replicationsubnetgroupdescription""", alias="ReplicationSubnetGroupDescription")
    ReplicationSubnetGroupIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-replicationsubnetgroupidentifier""", alias="ReplicationSubnetGroupIdentifier")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-subnetids""", alias="SubnetIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.dms.ReplicationSubnetGroup:
        from troposphere.dms import ReplicationSubnetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.dms import ReplicationSubnetGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class ReplicationTask(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html
    Properties:
        - Name: ReplicationTaskSettings
        - Name: CdcStartPosition
        - Name: CdcStopPosition
        - Name: MigrationType
        - Name: TargetEndpointArn
        - Name: ReplicationInstanceArn
        - Name: TaskData
        - Name: CdcStartTime
        - Name: ResourceIdentifier
        - Name: TableMappings
        - Name: ReplicationTaskIdentifier
        - Name: SourceEndpointArn
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ReplicationTaskSettings_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-replicationtasksettings""", alias="ReplicationTaskSettings")
    CdcStartPosition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-cdcstartposition""", alias="CdcStartPosition")
    CdcStopPosition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-cdcstopposition""", alias="CdcStopPosition")
    MigrationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-migrationtype""", alias="MigrationType")
    TargetEndpointArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-targetendpointarn""", alias="TargetEndpointArn")
    ReplicationInstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-replicationinstancearn""", alias="ReplicationInstanceArn")
    TaskData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-taskdata""", alias="TaskData")
    CdcStartTime_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-cdcstarttime""", alias="CdcStartTime")
    ResourceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-resourceidentifier""", alias="ResourceIdentifier")
    TableMappings_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-tablemappings""", alias="TableMappings")
    ReplicationTaskIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-replicationtaskidentifier""", alias="ReplicationTaskIdentifier")
    SourceEndpointArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-sourceendpointarn""", alias="SourceEndpointArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.dms.ReplicationTask:
        from troposphere.dms import ReplicationTask as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.dms import ReplicationTask as TropoT
        return resource_to_troposphere(self, TropoT)

