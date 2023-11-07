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
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestar-githubrepository-code.html
    Properties:
        - Name: S3
    
    """
    
    S3_: 'S3' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestar-githubrepository-code.html#cfn-codestar-githubrepository-code-s3""", alias="S3")
    


    @property
    def tropo_type(self) -> troposphere.codestar.Code:
        from troposphere.codestar import Code as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestar-githubrepository-s3.html
    Properties:
        - Name: ObjectVersion
        - Name: Bucket
        - Name: Key
    
    """
    
    ObjectVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestar-githubrepository-s3.html#cfn-codestar-githubrepository-s3-objectversion""", alias="ObjectVersion")
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestar-githubrepository-s3.html#cfn-codestar-githubrepository-s3-bucket""", alias="Bucket")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestar-githubrepository-s3.html#cfn-codestar-githubrepository-s3-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.codestar.S3:
        from troposphere.codestar import S3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class GitHubRepository(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.html
    Properties:
        - Name: EnableIssues
        - Name: ConnectionArn
        - Name: RepositoryName
        - Name: RepositoryAccessToken
        - Name: RepositoryOwner
        - Name: IsPrivate
        - Name: Code
        - Name: RepositoryDescription
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EnableIssues_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.html#cfn-codestar-githubrepository-enableissues""", alias="EnableIssues")
    ConnectionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.html#cfn-codestar-githubrepository-connectionarn""", alias="ConnectionArn")
    RepositoryName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.html#cfn-codestar-githubrepository-repositoryname""", alias="RepositoryName")
    RepositoryAccessToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.html#cfn-codestar-githubrepository-repositoryaccesstoken""", alias="RepositoryAccessToken")
    RepositoryOwner_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.html#cfn-codestar-githubrepository-repositoryowner""", alias="RepositoryOwner")
    IsPrivate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.html#cfn-codestar-githubrepository-isprivate""", alias="IsPrivate")
    Code_: Optional['Code'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.html#cfn-codestar-githubrepository-code""", alias="Code")
    RepositoryDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.html#cfn-codestar-githubrepository-repositorydescription""", alias="RepositoryDescription")
    

    @property
    def tropo_type(self) -> troposphere.codestar.GitHubRepository:
        from troposphere.codestar import GitHubRepository as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codestar import GitHubRepository as TropoT
        return resource_to_troposphere(self, TropoT)

