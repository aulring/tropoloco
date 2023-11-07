from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Criteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-criteria.html
    Properties:
        - Name: Regex
        - Name: S3WordsList
    
    """
    
    Regex_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-criteria.html#cfn-macie-allowlist-criteria-regex""", alias="Regex")
    S3WordsList_: Optional['S3WordsList'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-criteria.html#cfn-macie-allowlist-criteria-s3wordslist""", alias="S3WordsList")
    


    @property
    def tropo_type(self) -> troposphere.macie.Criteria:
        from troposphere.macie import Criteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3WordsList(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-s3wordslist.html
    Properties:
        - Name: BucketName
        - Name: ObjectKey
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-s3wordslist.html#cfn-macie-allowlist-s3wordslist-bucketname""", alias="BucketName")
    ObjectKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-s3wordslist.html#cfn-macie-allowlist-s3wordslist-objectkey""", alias="ObjectKey")
    


    @property
    def tropo_type(self) -> troposphere.macie.S3WordsList:
        from troposphere.macie import S3WordsList as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CriterionAdditionalProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html
    Properties:
        - Name: lt
        - Name: gte
        - Name: neq
        - Name: lte
        - Name: eq
        - Name: gt
    
    """
    
    lt_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-lt""", alias="lt")
    gte_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-gte""", alias="gte")
    neq_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-neq""", alias="neq")
    lte_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-lte""", alias="lte")
    eq_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-eq""", alias="eq")
    gt_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-gt""", alias="gt")
    


    @property
    def tropo_type(self) -> troposphere.macie.CriterionAdditionalProperties:
        from troposphere.macie import CriterionAdditionalProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FindingCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html
    Properties:
        - Name: Criterion
    
    """
    
    Criterion_: Optional[Dict[str, 'CriterionAdditionalProperties']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html#cfn-macie-findingsfilter-findingcriteria-criterion""", alias="Criterion")
    


    @property
    def tropo_type(self) -> troposphere.macie.FindingCriteria:
        from troposphere.macie import FindingCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AllowList(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html
    Properties:
        - Name: Description
        - Name: Criteria
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-description""", alias="Description")
    Criteria_: 'Criteria' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-criteria""", alias="Criteria")
    Tags_: Optional[Tags] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.macie.AllowList:
        from troposphere.macie import AllowList as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.macie import AllowList as TropoT
        return resource_to_troposphere(self, TropoT)


class CustomDataIdentifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html
    Properties:
        - Name: Description
        - Name: Keywords
        - Name: Regex
        - Name: IgnoreWords
        - Name: Tags
        - Name: Name
        - Name: MaximumMatchDistance
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-description""", alias="Description")
    Keywords_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-keywords""", alias="Keywords")
    Regex_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-regex""", alias="Regex")
    IgnoreWords_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-ignorewords""", alias="IgnoreWords")
    Tags_: Optional[Tags] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-name""", alias="Name")
    MaximumMatchDistance_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-maximummatchdistance""", alias="MaximumMatchDistance")
    

    @property
    def tropo_type(self) -> troposphere.macie.CustomDataIdentifier:
        from troposphere.macie import CustomDataIdentifier as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.macie import CustomDataIdentifier as TropoT
        return resource_to_troposphere(self, TropoT)


class FindingsFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html
    Properties:
        - Name: Action
        - Name: Description
        - Name: Position
        - Name: FindingCriteria
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Action_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-action""", alias="Action")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-description""", alias="Description")
    Position_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-position""", alias="Position")
    FindingCriteria_: 'FindingCriteria' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-findingcriteria""", alias="FindingCriteria")
    Tags_: Optional[Tags] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.macie.FindingsFilter:
        from troposphere.macie import FindingsFilter as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.macie import FindingsFilter as TropoT
        return resource_to_troposphere(self, TropoT)


class Session(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html
    Properties:
        - Name: Status
        - Name: FindingPublishingFrequency
    Attributes:
        - Name: ServiceRole
        - Name: AwsAccountId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-status""", alias="Status")
    FindingPublishingFrequency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-findingpublishingfrequency""", alias="FindingPublishingFrequency")
    

    @property
    def tropo_type(self) -> troposphere.macie.Session:
        from troposphere.macie import Session as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.macie import Session as TropoT
        return resource_to_troposphere(self, TropoT)

