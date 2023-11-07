from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CapacityAssignment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-capacityreservation-capacityassignment.html
    Properties:
        - Name: WorkgroupNames
    
    """
    
    WorkgroupNames_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-capacityreservation-capacityassignment.html#cfn-athena-capacityreservation-capacityassignment-workgroupnames""", alias="WorkgroupNames")
    


    @property
    def tropo_type(self) -> troposphere.athena.CapacityAssignment:
        from troposphere.athena import CapacityAssignment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CapacityAssignmentConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-capacityreservation-capacityassignmentconfiguration.html
    Properties:
        - Name: CapacityAssignments
    
    """
    
    CapacityAssignments_: List['CapacityAssignment'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-capacityreservation-capacityassignmentconfiguration.html#cfn-athena-capacityreservation-capacityassignmentconfiguration-capacityassignments""", alias="CapacityAssignments")
    


    @property
    def tropo_type(self) -> troposphere.athena.CapacityAssignmentConfiguration:
        from troposphere.athena import CapacityAssignmentConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AclConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-aclconfiguration.html
    Properties:
        - Name: S3AclOption
    
    """
    
    S3AclOption_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-aclconfiguration.html#cfn-athena-workgroup-aclconfiguration-s3acloption""", alias="S3AclOption")
    


    @property
    def tropo_type(self) -> troposphere.athena.AclConfiguration:
        from troposphere.athena import AclConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomerContentEncryptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-customercontentencryptionconfiguration.html
    Properties:
        - Name: KmsKey
    
    """
    
    KmsKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-customercontentencryptionconfiguration.html#cfn-athena-workgroup-customercontentencryptionconfiguration-kmskey""", alias="KmsKey")
    


    @property
    def tropo_type(self) -> troposphere.athena.CustomerContentEncryptionConfiguration:
        from troposphere.athena import CustomerContentEncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html
    Properties:
        - Name: EncryptionOption
        - Name: KmsKey
    
    """
    
    EncryptionOption_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html#cfn-athena-workgroup-encryptionconfiguration-encryptionoption""", alias="EncryptionOption")
    KmsKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html#cfn-athena-workgroup-encryptionconfiguration-kmskey""", alias="KmsKey")
    


    @property
    def tropo_type(self) -> troposphere.athena.EncryptionConfiguration:
        from troposphere.athena import EncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EngineVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html
    Properties:
        - Name: SelectedEngineVersion
        - Name: EffectiveEngineVersion
    
    """
    
    SelectedEngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html#cfn-athena-workgroup-engineversion-selectedengineversion""", alias="SelectedEngineVersion")
    EffectiveEngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html#cfn-athena-workgroup-engineversion-effectiveengineversion""", alias="EffectiveEngineVersion")
    


    @property
    def tropo_type(self) -> troposphere.athena.EngineVersion:
        from troposphere.athena import EngineVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResultConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html
    Properties:
        - Name: EncryptionConfiguration
        - Name: OutputLocation
        - Name: AclConfiguration
        - Name: ExpectedBucketOwner
    
    """
    
    EncryptionConfiguration_: Optional['EncryptionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-encryptionconfiguration""", alias="EncryptionConfiguration")
    OutputLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-outputlocation""", alias="OutputLocation")
    AclConfiguration_: Optional['AclConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-aclconfiguration""", alias="AclConfiguration")
    ExpectedBucketOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-expectedbucketowner""", alias="ExpectedBucketOwner")
    


    @property
    def tropo_type(self) -> troposphere.athena.ResultConfiguration:
        from troposphere.athena import ResultConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WorkGroupConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html
    Properties:
        - Name: EnforceWorkGroupConfiguration
        - Name: EngineVersion
        - Name: PublishCloudWatchMetricsEnabled
        - Name: ResultConfiguration
        - Name: AdditionalConfiguration
        - Name: CustomerContentEncryptionConfiguration
        - Name: BytesScannedCutoffPerQuery
        - Name: RequesterPaysEnabled
        - Name: ExecutionRole
    
    """
    
    EnforceWorkGroupConfiguration_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-enforceworkgroupconfiguration""", alias="EnforceWorkGroupConfiguration")
    EngineVersion_: Optional['EngineVersion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-engineversion""", alias="EngineVersion")
    PublishCloudWatchMetricsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-publishcloudwatchmetricsenabled""", alias="PublishCloudWatchMetricsEnabled")
    ResultConfiguration_: Optional['ResultConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-resultconfiguration""", alias="ResultConfiguration")
    AdditionalConfiguration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-additionalconfiguration""", alias="AdditionalConfiguration")
    CustomerContentEncryptionConfiguration_: Optional['CustomerContentEncryptionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-customercontentencryptionconfiguration""", alias="CustomerContentEncryptionConfiguration")
    BytesScannedCutoffPerQuery_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-bytesscannedcutoffperquery""", alias="BytesScannedCutoffPerQuery")
    RequesterPaysEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-requesterpaysenabled""", alias="RequesterPaysEnabled")
    ExecutionRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-executionrole""", alias="ExecutionRole")
    


    @property
    def tropo_type(self) -> troposphere.athena.WorkGroupConfiguration:
        from troposphere.athena import WorkGroupConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class CapacityReservation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.html
    Properties:
        - Name: TargetDpus
        - Name: CapacityAssignmentConfiguration
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: AllocatedDpus
        - Name: CreationTime
        - Name: LastSuccessfulAllocationTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TargetDpus_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.html#cfn-athena-capacityreservation-targetdpus""", alias="TargetDpus")
    CapacityAssignmentConfiguration_: Optional['CapacityAssignmentConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.html#cfn-athena-capacityreservation-capacityassignmentconfiguration""", alias="CapacityAssignmentConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.html#cfn-athena-capacityreservation-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.html#cfn-athena-capacityreservation-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.athena.CapacityReservation:
        from troposphere.athena import CapacityReservation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.athena import CapacityReservation as TropoT
        return resource_to_troposphere(self, TropoT)


class DataCatalog(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: Parameters
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-description""", alias="Description")
    Parameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-parameters""", alias="Parameters")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.athena.DataCatalog:
        from troposphere.athena import DataCatalog as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.athena import DataCatalog as TropoT
        return resource_to_troposphere(self, TropoT)


class NamedQuery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html
    Properties:
        - Name: WorkGroup
        - Name: Description
        - Name: QueryString
        - Name: Database
        - Name: Name
    Attributes:
        - Name: NamedQueryId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    WorkGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-workgroup""", alias="WorkGroup")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-description""", alias="Description")
    QueryString_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-querystring""", alias="QueryString")
    Database_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-database""", alias="Database")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.athena.NamedQuery:
        from troposphere.athena import NamedQuery as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.athena import NamedQuery as TropoT
        return resource_to_troposphere(self, TropoT)


class PreparedStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html
    Properties:
        - Name: StatementName
        - Name: WorkGroup
        - Name: Description
        - Name: QueryStatement
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StatementName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-statementname""", alias="StatementName")
    WorkGroup_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-workgroup""", alias="WorkGroup")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-description""", alias="Description")
    QueryStatement_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-querystatement""", alias="QueryStatement")
    

    @property
    def tropo_type(self) -> troposphere.athena.PreparedStatement:
        from troposphere.athena import PreparedStatement as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.athena import PreparedStatement as TropoT
        return resource_to_troposphere(self, TropoT)


class WorkGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html
    Properties:
        - Name: RecursiveDeleteOption
        - Name: WorkGroupConfiguration
        - Name: Description
        - Name: State
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: CreationTime
        - Name: WorkGroupConfiguration.EngineVersion.EffectiveEngineVersion
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RecursiveDeleteOption_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-recursivedeleteoption""", alias="RecursiveDeleteOption")
    WorkGroupConfiguration_: Optional['WorkGroupConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfiguration""", alias="WorkGroupConfiguration")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-description""", alias="Description")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-state""", alias="State")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.athena.WorkGroup:
        from troposphere.athena import WorkGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.athena import WorkGroup as TropoT
        return resource_to_troposphere(self, TropoT)

