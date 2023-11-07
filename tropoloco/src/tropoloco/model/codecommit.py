from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Code(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.html
    Properties:
        - Name: S3
        - Name: BranchName
    
    """
    
    S3_: 'S3' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.html#cfn-codecommit-repository-code-s3""", alias="S3")
    BranchName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.html#cfn-codecommit-repository-code-branchname""", alias="BranchName")
    


    @property
    def tropo_type(self) -> troposphere.codecommit.Code:
        from troposphere.codecommit import Code as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RepositoryTrigger(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html
    Properties:
        - Name: Events
        - Name: Branches
        - Name: CustomData
        - Name: DestinationArn
        - Name: Name
    
    """
    
    Events_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-events""", alias="Events")
    Branches_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-branches""", alias="Branches")
    CustomData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-customdata""", alias="CustomData")
    DestinationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-destinationarn""", alias="DestinationArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.codecommit.RepositoryTrigger:
        from troposphere.codecommit import RepositoryTrigger as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html
    Properties:
        - Name: ObjectVersion
        - Name: Bucket
        - Name: Key
    
    """
    
    ObjectVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html#cfn-codecommit-repository-s3-objectversion""", alias="ObjectVersion")
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html#cfn-codecommit-repository-s3-bucket""", alias="Bucket")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html#cfn-codecommit-repository-s3-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.codecommit.S3:
        from troposphere.codecommit import S3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Repository(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html
    Properties:
        - Name: RepositoryName
        - Name: Triggers
        - Name: Code
        - Name: RepositoryDescription
        - Name: Tags
    Attributes:
        - Name: CloneUrlHttp
        - Name: CloneUrlSsh
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RepositoryName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-repositoryname""", alias="RepositoryName")
    Triggers_: Optional[List['RepositoryTrigger']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-triggers""", alias="Triggers")
    Code_: Optional['Code'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-code""", alias="Code")
    RepositoryDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-repositorydescription""", alias="RepositoryDescription")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.codecommit.Repository:
        from troposphere.codecommit import Repository as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codecommit import Repository as TropoT
        return resource_to_troposphere(self, TropoT)

