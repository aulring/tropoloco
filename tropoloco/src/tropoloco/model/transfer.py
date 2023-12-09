from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class As2Config(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html
    Properties:
        - Name: Compression
        - Name: MessageSubject
        - Name: BasicAuthSecretId
        - Name: PartnerProfileId
        - Name: EncryptionAlgorithm
        - Name: SigningAlgorithm
        - Name: LocalProfileId
        - Name: MdnResponse
        - Name: MdnSigningAlgorithm
    
    """
    
    Compression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-compression""", alias="Compression")
    MessageSubject_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-messagesubject""", alias="MessageSubject")
    BasicAuthSecretId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-basicauthsecretid""", alias="BasicAuthSecretId")
    PartnerProfileId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-partnerprofileid""", alias="PartnerProfileId")
    EncryptionAlgorithm_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-encryptionalgorithm""", alias="EncryptionAlgorithm")
    SigningAlgorithm_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-signingalgorithm""", alias="SigningAlgorithm")
    LocalProfileId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-localprofileid""", alias="LocalProfileId")
    MdnResponse_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-mdnresponse""", alias="MdnResponse")
    MdnSigningAlgorithm_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-mdnsigningalgorithm""", alias="MdnSigningAlgorithm")
    


    @property
    def tropo_type(self) -> troposphere.transfer.As2Config:
        from troposphere.transfer import As2Config as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SftpConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-sftpconfig.html
    Properties:
        - Name: TrustedHostKeys
        - Name: UserSecretId
    
    """
    
    TrustedHostKeys_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-sftpconfig.html#cfn-transfer-connector-sftpconfig-trustedhostkeys""", alias="TrustedHostKeys")
    UserSecretId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-sftpconfig.html#cfn-transfer-connector-sftpconfig-usersecretid""", alias="UserSecretId")
    


    @property
    def tropo_type(self) -> troposphere.transfer.SftpConfig:
        from troposphere.transfer import SftpConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class As2Transport(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-as2transport.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.transfer.As2Transport:
        from troposphere.transfer import As2Transport as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EndpointDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html
    Properties:
        - Name: AddressAllocationIds
        - Name: VpcId
        - Name: VpcEndpointId
        - Name: SecurityGroupIds
        - Name: SubnetIds
    
    """
    
    AddressAllocationIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-addressallocationids""", alias="AddressAllocationIds")
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-vpcid""", alias="VpcId")
    VpcEndpointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-vpcendpointid""", alias="VpcEndpointId")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.transfer.EndpointDetails:
        from troposphere.transfer import EndpointDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IdentityProviderDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html
    Properties:
        - Name: Function
        - Name: DirectoryId
        - Name: InvocationRole
        - Name: Url
        - Name: SftpAuthenticationMethods
    
    """
    
    Function_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-function""", alias="Function")
    DirectoryId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-directoryid""", alias="DirectoryId")
    InvocationRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-invocationrole""", alias="InvocationRole")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-url""", alias="Url")
    SftpAuthenticationMethods_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-sftpauthenticationmethods""", alias="SftpAuthenticationMethods")
    


    @property
    def tropo_type(self) -> troposphere.transfer.IdentityProviderDetails:
        from troposphere.transfer import IdentityProviderDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Protocol(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocol.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.transfer.Protocol:
        from troposphere.transfer import Protocol as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProtocolDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html
    Properties:
        - Name: As2Transports
        - Name: PassiveIp
        - Name: SetStatOption
        - Name: TlsSessionResumptionMode
    
    """
    
    As2Transports_: Optional[List['As2Transport']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html#cfn-transfer-server-protocoldetails-as2transports""", alias="As2Transports")
    PassiveIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html#cfn-transfer-server-protocoldetails-passiveip""", alias="PassiveIp")
    SetStatOption_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html#cfn-transfer-server-protocoldetails-setstatoption""", alias="SetStatOption")
    TlsSessionResumptionMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html#cfn-transfer-server-protocoldetails-tlssessionresumptionmode""", alias="TlsSessionResumptionMode")
    


    @property
    def tropo_type(self) -> troposphere.transfer.ProtocolDetails:
        from troposphere.transfer import ProtocolDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3StorageOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-s3storageoptions.html
    Properties:
        - Name: DirectoryListingOptimization
    
    """
    
    DirectoryListingOptimization_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-s3storageoptions.html#cfn-transfer-server-s3storageoptions-directorylistingoptimization""", alias="DirectoryListingOptimization")
    


    @property
    def tropo_type(self) -> troposphere.transfer.S3StorageOptions:
        from troposphere.transfer import S3StorageOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StructuredLogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-structuredlogdestination.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.transfer.StructuredLogDestination:
        from troposphere.transfer import StructuredLogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WorkflowDetail(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html
    Properties:
        - Name: WorkflowId
        - Name: ExecutionRole
    
    """
    
    WorkflowId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html#cfn-transfer-server-workflowdetail-workflowid""", alias="WorkflowId")
    ExecutionRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html#cfn-transfer-server-workflowdetail-executionrole""", alias="ExecutionRole")
    


    @property
    def tropo_type(self) -> troposphere.transfer.WorkflowDetail:
        from troposphere.transfer import WorkflowDetail as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WorkflowDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html
    Properties:
        - Name: OnUpload
        - Name: OnPartialUpload
    
    """
    
    OnUpload_: Optional[List['WorkflowDetail']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html#cfn-transfer-server-workflowdetails-onupload""", alias="OnUpload")
    OnPartialUpload_: Optional[List['WorkflowDetail']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html#cfn-transfer-server-workflowdetails-onpartialupload""", alias="OnPartialUpload")
    


    @property
    def tropo_type(self) -> troposphere.transfer.WorkflowDetails:
        from troposphere.transfer import WorkflowDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HomeDirectoryMapEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html
    Properties:
        - Name: Entry
        - Name: Target
        - Name: Type
    
    """
    
    Entry_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html#cfn-transfer-user-homedirectorymapentry-entry""", alias="Entry")
    Target_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html#cfn-transfer-user-homedirectorymapentry-target""", alias="Target")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html#cfn-transfer-user-homedirectorymapentry-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.transfer.HomeDirectoryMapEntry:
        from troposphere.transfer import HomeDirectoryMapEntry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PosixProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html
    Properties:
        - Name: Uid
        - Name: SecondaryGids
        - Name: Gid
    
    """
    
    Uid_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html#cfn-transfer-user-posixprofile-uid""", alias="Uid")
    SecondaryGids_: Optional[List[float]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html#cfn-transfer-user-posixprofile-secondarygids""", alias="SecondaryGids")
    Gid_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html#cfn-transfer-user-posixprofile-gid""", alias="Gid")
    


    @property
    def tropo_type(self) -> troposphere.transfer.PosixProfile:
        from troposphere.transfer import PosixProfile as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SshPublicKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-sshpublickey.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.transfer.SshPublicKey:
        from troposphere.transfer import SshPublicKey as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CopyStepDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-copystepdetails.html
    Properties:
        - Name: DestinationFileLocation
        - Name: SourceFileLocation
        - Name: Name
        - Name: OverwriteExisting
    
    """
    
    DestinationFileLocation_: Optional['S3FileLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-copystepdetails.html#cfn-transfer-workflow-copystepdetails-destinationfilelocation""", alias="DestinationFileLocation")
    SourceFileLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-copystepdetails.html#cfn-transfer-workflow-copystepdetails-sourcefilelocation""", alias="SourceFileLocation")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-copystepdetails.html#cfn-transfer-workflow-copystepdetails-name""", alias="Name")
    OverwriteExisting_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-copystepdetails.html#cfn-transfer-workflow-copystepdetails-overwriteexisting""", alias="OverwriteExisting")
    


    @property
    def tropo_type(self) -> troposphere.transfer.CopyStepDetails:
        from troposphere.transfer import CopyStepDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomStepDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-customstepdetails.html
    Properties:
        - Name: TimeoutSeconds
        - Name: Target
        - Name: SourceFileLocation
        - Name: Name
    
    """
    
    TimeoutSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-customstepdetails.html#cfn-transfer-workflow-customstepdetails-timeoutseconds""", alias="TimeoutSeconds")
    Target_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-customstepdetails.html#cfn-transfer-workflow-customstepdetails-target""", alias="Target")
    SourceFileLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-customstepdetails.html#cfn-transfer-workflow-customstepdetails-sourcefilelocation""", alias="SourceFileLocation")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-customstepdetails.html#cfn-transfer-workflow-customstepdetails-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.transfer.CustomStepDetails:
        from troposphere.transfer import CustomStepDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DecryptStepDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-decryptstepdetails.html
    Properties:
        - Name: DestinationFileLocation
        - Name: Type
        - Name: SourceFileLocation
        - Name: Name
        - Name: OverwriteExisting
    
    """
    
    DestinationFileLocation_: Optional['InputFileLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-decryptstepdetails.html#cfn-transfer-workflow-decryptstepdetails-destinationfilelocation""", alias="DestinationFileLocation")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-decryptstepdetails.html#cfn-transfer-workflow-decryptstepdetails-type""", alias="Type")
    SourceFileLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-decryptstepdetails.html#cfn-transfer-workflow-decryptstepdetails-sourcefilelocation""", alias="SourceFileLocation")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-decryptstepdetails.html#cfn-transfer-workflow-decryptstepdetails-name""", alias="Name")
    OverwriteExisting_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-decryptstepdetails.html#cfn-transfer-workflow-decryptstepdetails-overwriteexisting""", alias="OverwriteExisting")
    


    @property
    def tropo_type(self) -> troposphere.transfer.DecryptStepDetails:
        from troposphere.transfer import DecryptStepDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeleteStepDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-deletestepdetails.html
    Properties:
        - Name: SourceFileLocation
        - Name: Name
    
    """
    
    SourceFileLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-deletestepdetails.html#cfn-transfer-workflow-deletestepdetails-sourcefilelocation""", alias="SourceFileLocation")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-deletestepdetails.html#cfn-transfer-workflow-deletestepdetails-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.transfer.DeleteStepDetails:
        from troposphere.transfer import DeleteStepDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EfsInputFileLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-efsinputfilelocation.html
    Properties:
        - Name: Path
        - Name: FileSystemId
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-efsinputfilelocation.html#cfn-transfer-workflow-efsinputfilelocation-path""", alias="Path")
    FileSystemId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-efsinputfilelocation.html#cfn-transfer-workflow-efsinputfilelocation-filesystemid""", alias="FileSystemId")
    


    @property
    def tropo_type(self) -> troposphere.transfer.EfsInputFileLocation:
        from troposphere.transfer import EfsInputFileLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputFileLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-inputfilelocation.html
    Properties:
        - Name: EfsFileLocation
        - Name: S3FileLocation
    
    """
    
    EfsFileLocation_: Optional['EfsInputFileLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-inputfilelocation.html#cfn-transfer-workflow-inputfilelocation-efsfilelocation""", alias="EfsFileLocation")
    S3FileLocation_: Optional['S3InputFileLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-inputfilelocation.html#cfn-transfer-workflow-inputfilelocation-s3filelocation""", alias="S3FileLocation")
    


    @property
    def tropo_type(self) -> troposphere.transfer.InputFileLocation:
        from troposphere.transfer import InputFileLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3FileLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3filelocation.html
    Properties:
        - Name: S3FileLocation
    
    """
    
    S3FileLocation_: Optional['S3InputFileLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3filelocation.html#cfn-transfer-workflow-s3filelocation-s3filelocation""", alias="S3FileLocation")
    


    @property
    def tropo_type(self) -> troposphere.transfer.S3FileLocation:
        from troposphere.transfer import S3FileLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3InputFileLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3inputfilelocation.html
    Properties:
        - Name: Bucket
        - Name: Key
    
    """
    
    Bucket_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3inputfilelocation.html#cfn-transfer-workflow-s3inputfilelocation-bucket""", alias="Bucket")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3inputfilelocation.html#cfn-transfer-workflow-s3inputfilelocation-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.transfer.S3InputFileLocation:
        from troposphere.transfer import S3InputFileLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Tag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3tag.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3tag.html#cfn-transfer-workflow-s3tag-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3tag.html#cfn-transfer-workflow-s3tag-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.transfer.S3Tag:
        from troposphere.transfer import S3Tag as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagStepDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-tagstepdetails.html
    Properties:
        - Name: SourceFileLocation
        - Name: Tags
        - Name: Name
    
    """
    
    SourceFileLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-tagstepdetails.html#cfn-transfer-workflow-tagstepdetails-sourcefilelocation""", alias="SourceFileLocation")
    Tags_: Optional[List['S3Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-tagstepdetails.html#cfn-transfer-workflow-tagstepdetails-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-tagstepdetails.html#cfn-transfer-workflow-tagstepdetails-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.transfer.TagStepDetails:
        from troposphere.transfer import TagStepDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WorkflowStep(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html
    Properties:
        - Name: CustomStepDetails
        - Name: CopyStepDetails
        - Name: DecryptStepDetails
        - Name: Type
        - Name: TagStepDetails
        - Name: DeleteStepDetails
    
    """
    
    CustomStepDetails_: Optional['CustomStepDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-customstepdetails""", alias="CustomStepDetails")
    CopyStepDetails_: Optional['CopyStepDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-copystepdetails""", alias="CopyStepDetails")
    DecryptStepDetails_: Optional['DecryptStepDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-decryptstepdetails""", alias="DecryptStepDetails")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-type""", alias="Type")
    TagStepDetails_: Optional['TagStepDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-tagstepdetails""", alias="TagStepDetails")
    DeleteStepDetails_: Optional['DeleteStepDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-deletestepdetails""", alias="DeleteStepDetails")
    


    @property
    def tropo_type(self) -> troposphere.transfer.WorkflowStep:
        from troposphere.transfer import WorkflowStep as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Agreement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html
    Properties:
        - Name: Status
        - Name: Description
        - Name: ServerId
        - Name: BaseDirectory
        - Name: AccessRole
        - Name: PartnerProfileId
        - Name: LocalProfileId
        - Name: Tags
    Attributes:
        - Name: AgreementId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-status""", alias="Status")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-description""", alias="Description")
    ServerId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-serverid""", alias="ServerId")
    BaseDirectory_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-basedirectory""", alias="BaseDirectory")
    AccessRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-accessrole""", alias="AccessRole")
    PartnerProfileId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-partnerprofileid""", alias="PartnerProfileId")
    LocalProfileId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-localprofileid""", alias="LocalProfileId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.transfer.Agreement:
        from troposphere.transfer import Agreement as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.transfer import Agreement as TropoT
        return resource_to_troposphere(self, TropoT)


class Certificate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html
    Properties:
        - Name: InactiveDate
        - Name: Usage
        - Name: PrivateKey
        - Name: Description
        - Name: CertificateChain
        - Name: ActiveDate
        - Name: Tags
        - Name: Certificate
    Attributes:
        - Name: Status
        - Name: Type
        - Name: Serial
        - Name: CertificateId
        - Name: NotBeforeDate
        - Name: NotAfterDate
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InactiveDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-inactivedate""", alias="InactiveDate")
    Usage_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-usage""", alias="Usage")
    PrivateKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-privatekey""", alias="PrivateKey")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-description""", alias="Description")
    CertificateChain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-certificatechain""", alias="CertificateChain")
    ActiveDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-activedate""", alias="ActiveDate")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-tags""", alias="Tags")
    Certificate_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-certificate""", alias="Certificate")
    

    @property
    def tropo_type(self) -> troposphere.transfer.Certificate:
        from troposphere.transfer import Certificate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.transfer import Certificate as TropoT
        return resource_to_troposphere(self, TropoT)


class Connector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html
    Properties:
        - Name: As2Config
        - Name: LoggingRole
        - Name: AccessRole
        - Name: SftpConfig
        - Name: Tags
        - Name: Url
    Attributes:
        - Name: Arn
        - Name: ConnectorId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    As2Config_: Optional['As2Config'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html#cfn-transfer-connector-as2config""", alias="As2Config")
    LoggingRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html#cfn-transfer-connector-loggingrole""", alias="LoggingRole")
    AccessRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html#cfn-transfer-connector-accessrole""", alias="AccessRole")
    SftpConfig_: Optional['SftpConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html#cfn-transfer-connector-sftpconfig""", alias="SftpConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html#cfn-transfer-connector-tags""", alias="Tags")
    Url_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html#cfn-transfer-connector-url""", alias="Url")
    

    @property
    def tropo_type(self) -> troposphere.transfer.Connector:
        from troposphere.transfer import Connector as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.transfer import Connector as TropoT
        return resource_to_troposphere(self, TropoT)


class Profile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-profile.html
    Properties:
        - Name: As2Id
        - Name: ProfileType
        - Name: CertificateIds
        - Name: Tags
    Attributes:
        - Name: ProfileId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    As2Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-profile.html#cfn-transfer-profile-as2id""", alias="As2Id")
    ProfileType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-profile.html#cfn-transfer-profile-profiletype""", alias="ProfileType")
    CertificateIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-profile.html#cfn-transfer-profile-certificateids""", alias="CertificateIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-profile.html#cfn-transfer-profile-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.transfer.Profile:
        from troposphere.transfer import Profile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.transfer import Profile as TropoT
        return resource_to_troposphere(self, TropoT)


class Server(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html
    Properties:
        - Name: LoggingRole
        - Name: Protocols
        - Name: IdentityProviderDetails
        - Name: EndpointDetails
        - Name: StructuredLogDestinations
        - Name: PreAuthenticationLoginBanner
        - Name: PostAuthenticationLoginBanner
        - Name: EndpointType
        - Name: SecurityPolicyName
        - Name: ProtocolDetails
        - Name: S3StorageOptions
        - Name: WorkflowDetails
        - Name: Domain
        - Name: IdentityProviderType
        - Name: Tags
        - Name: Certificate
    Attributes:
        - Name: ServerId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LoggingRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-loggingrole""", alias="LoggingRole")
    Protocols_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-protocols""", alias="Protocols")
    IdentityProviderDetails_: Optional['IdentityProviderDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityproviderdetails""", alias="IdentityProviderDetails")
    EndpointDetails_: Optional['EndpointDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointdetails""", alias="EndpointDetails")
    StructuredLogDestinations_: Optional[List['StructuredLogDestination']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-structuredlogdestinations""", alias="StructuredLogDestinations")
    PreAuthenticationLoginBanner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-preauthenticationloginbanner""", alias="PreAuthenticationLoginBanner")
    PostAuthenticationLoginBanner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-postauthenticationloginbanner""", alias="PostAuthenticationLoginBanner")
    EndpointType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointtype""", alias="EndpointType")
    SecurityPolicyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-securitypolicyname""", alias="SecurityPolicyName")
    ProtocolDetails_: Optional['ProtocolDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-protocoldetails""", alias="ProtocolDetails")
    S3StorageOptions_: Optional['S3StorageOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-s3storageoptions""", alias="S3StorageOptions")
    WorkflowDetails_: Optional['WorkflowDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-workflowdetails""", alias="WorkflowDetails")
    Domain_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-domain""", alias="Domain")
    IdentityProviderType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityprovidertype""", alias="IdentityProviderType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-tags""", alias="Tags")
    Certificate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-certificate""", alias="Certificate")
    

    @property
    def tropo_type(self) -> troposphere.transfer.Server:
        from troposphere.transfer import Server as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.transfer import Server as TropoT
        return resource_to_troposphere(self, TropoT)


class User(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html
    Properties:
        - Name: Policy
        - Name: Role
        - Name: HomeDirectory
        - Name: HomeDirectoryType
        - Name: ServerId
        - Name: UserName
        - Name: HomeDirectoryMappings
        - Name: PosixProfile
        - Name: SshPublicKeys
        - Name: Tags
    Attributes:
        - Name: ServerId
        - Name: UserName
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-policy""", alias="Policy")
    Role_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-role""", alias="Role")
    HomeDirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectory""", alias="HomeDirectory")
    HomeDirectoryType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorytype""", alias="HomeDirectoryType")
    ServerId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-serverid""", alias="ServerId")
    UserName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-username""", alias="UserName")
    HomeDirectoryMappings_: Optional[List['HomeDirectoryMapEntry']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorymappings""", alias="HomeDirectoryMappings")
    PosixProfile_: Optional['PosixProfile'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-posixprofile""", alias="PosixProfile")
    SshPublicKeys_: Optional[List['SshPublicKey']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-sshpublickeys""", alias="SshPublicKeys")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.transfer.User:
        from troposphere.transfer import User as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.transfer import User as TropoT
        return resource_to_troposphere(self, TropoT)


class Workflow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html
    Properties:
        - Name: Steps
        - Name: Description
        - Name: OnExceptionSteps
        - Name: Tags
    Attributes:
        - Name: WorkflowId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Steps_: List['WorkflowStep'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-steps""", alias="Steps")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-description""", alias="Description")
    OnExceptionSteps_: Optional[List['WorkflowStep']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-onexceptionsteps""", alias="OnExceptionSteps")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.transfer.Workflow:
        from troposphere.transfer import Workflow as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.transfer import Workflow as TropoT
        return resource_to_troposphere(self, TropoT)

