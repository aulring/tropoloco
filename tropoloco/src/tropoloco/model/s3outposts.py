from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class VpcConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-accesspoint-vpcconfiguration.html
    Properties:
        - Name: VpcId
    
    """
    
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-accesspoint-vpcconfiguration.html#cfn-s3outposts-accesspoint-vpcconfiguration-vpcid""", alias="VpcId")
    


    @property
    def tropo_type(self) -> troposphere.s3outposts.VpcConfiguration:
        from troposphere.s3outposts import VpcConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AbortIncompleteMultipartUpload(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-abortincompletemultipartupload.html
    Properties:
        - Name: DaysAfterInitiation
    
    """
    
    DaysAfterInitiation_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-abortincompletemultipartupload.html#cfn-s3outposts-bucket-abortincompletemultipartupload-daysafterinitiation""", alias="DaysAfterInitiation")
    


    @property
    def tropo_type(self) -> troposphere.s3outposts.AbortIncompleteMultipartUpload:
        from troposphere.s3outposts import AbortIncompleteMultipartUpload as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Filter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filter.html
    Properties:
        - Name: AndOperator
        - Name: Prefix
        - Name: Tag
    
    """
    
    AndOperator_: Optional['FilterAndOperator'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filter.html#cfn-s3outposts-bucket-filter-andoperator""", alias="AndOperator")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filter.html#cfn-s3outposts-bucket-filter-prefix""", alias="Prefix")
    Tag_: Optional['FilterTag'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filter.html#cfn-s3outposts-bucket-filter-tag""", alias="Tag")
    


    @property
    def tropo_type(self) -> troposphere.s3outposts.Filter:
        from troposphere.s3outposts import Filter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FilterAndOperator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filterandoperator.html
    Properties:
        - Name: Prefix
        - Name: Tags
    
    """
    
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filterandoperator.html#cfn-s3outposts-bucket-filterandoperator-prefix""", alias="Prefix")
    Tags_: List['FilterTag'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filterandoperator.html#cfn-s3outposts-bucket-filterandoperator-tags""", alias="Tags")
    


    @property
    def tropo_type(self) -> troposphere.s3outposts.FilterAndOperator:
        from troposphere.s3outposts import FilterAndOperator as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FilterTag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filtertag.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filtertag.html#cfn-s3outposts-bucket-filtertag-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filtertag.html#cfn-s3outposts-bucket-filtertag-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.s3outposts.FilterTag:
        from troposphere.s3outposts import FilterTag as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LifecycleConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-lifecycleconfiguration.html
    Properties:
        - Name: Rules
    
    """
    
    Rules_: List['Rule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-lifecycleconfiguration.html#cfn-s3outposts-bucket-lifecycleconfiguration-rules""", alias="Rules")
    


    @property
    def tropo_type(self) -> troposphere.s3outposts.LifecycleConfiguration:
        from troposphere.s3outposts import LifecycleConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html
    Properties:
        - Name: Status
        - Name: ExpirationDate
        - Name: Filter
        - Name: ExpirationInDays
        - Name: Id
        - Name: AbortIncompleteMultipartUpload
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-status""", alias="Status")
    ExpirationDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-expirationdate""", alias="ExpirationDate")
    Filter_: Optional['Filter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-filter""", alias="Filter")
    ExpirationInDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-expirationindays""", alias="ExpirationInDays")
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-id""", alias="Id")
    AbortIncompleteMultipartUpload_: Optional['AbortIncompleteMultipartUpload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-abortincompletemultipartupload""", alias="AbortIncompleteMultipartUpload")
    


    @property
    def tropo_type(self) -> troposphere.s3outposts.Rule:
        from troposphere.s3outposts import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FailedReason(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-failedreason.html
    Properties:
        - Name: Message
        - Name: ErrorCode
    
    """
    
    Message_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-failedreason.html#cfn-s3outposts-endpoint-failedreason-message""", alias="Message")
    ErrorCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-failedreason.html#cfn-s3outposts-endpoint-failedreason-errorcode""", alias="ErrorCode")
    


    @property
    def tropo_type(self) -> troposphere.s3outposts.FailedReason:
        from troposphere.s3outposts import FailedReason as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkInterface(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-networkinterface.html
    Properties:
        - Name: NetworkInterfaceId
    
    """
    
    NetworkInterfaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-networkinterface.html#cfn-s3outposts-endpoint-networkinterface-networkinterfaceid""", alias="NetworkInterfaceId")
    


    @property
    def tropo_type(self) -> troposphere.s3outposts.NetworkInterface:
        from troposphere.s3outposts import NetworkInterface as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AccessPoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html
    Properties:
        - Name: Policy
        - Name: Bucket
        - Name: VpcConfiguration
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-policy""", alias="Policy")
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-bucket""", alias="Bucket")
    VpcConfiguration_: 'VpcConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-vpcconfiguration""", alias="VpcConfiguration")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.s3outposts.AccessPoint:
        from troposphere.s3outposts import AccessPoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3outposts import AccessPoint as TropoT
        return resource_to_troposphere(self, TropoT)


class Bucket(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html
    Properties:
        - Name: OutpostId
        - Name: BucketName
        - Name: LifecycleConfiguration
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OutpostId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-outpostid""", alias="OutpostId")
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-bucketname""", alias="BucketName")
    LifecycleConfiguration_: Optional['LifecycleConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-lifecycleconfiguration""", alias="LifecycleConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.s3outposts.Bucket:
        from troposphere.s3outposts import Bucket as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3outposts import Bucket as TropoT
        return resource_to_troposphere(self, TropoT)


class BucketPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html
    Properties:
        - Name: Bucket
        - Name: PolicyDocument
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html#cfn-s3outposts-bucketpolicy-bucket""", alias="Bucket")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html#cfn-s3outposts-bucketpolicy-policydocument""", alias="PolicyDocument")
    

    @property
    def tropo_type(self) -> troposphere.s3outposts.BucketPolicy:
        from troposphere.s3outposts import BucketPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3outposts import BucketPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class Endpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html
    Properties:
        - Name: OutpostId
        - Name: SecurityGroupId
        - Name: FailedReason
        - Name: SubnetId
        - Name: AccessType
        - Name: CustomerOwnedIpv4Pool
    Attributes:
        - Name: Status
        - Name: NetworkInterfaces
        - Name: CreationTime
        - Name: CidrBlock
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OutpostId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-outpostid""", alias="OutpostId")
    SecurityGroupId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-securitygroupid""", alias="SecurityGroupId")
    FailedReason_: Optional['FailedReason'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-failedreason""", alias="FailedReason")
    SubnetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-subnetid""", alias="SubnetId")
    AccessType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-accesstype""", alias="AccessType")
    CustomerOwnedIpv4Pool_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-customerownedipv4pool""", alias="CustomerOwnedIpv4Pool")
    

    @property
    def tropo_type(self) -> troposphere.s3outposts.Endpoint:
        from troposphere.s3outposts import Endpoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3outposts import Endpoint as TropoT
        return resource_to_troposphere(self, TropoT)

