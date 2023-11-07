from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################




######################################################################
# AWS Resource
######################################################################


class Domain(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html
    Properties:
        - Name: PermissionsPolicyDocument
        - Name: DomainName
        - Name: Tags
        - Name: EncryptionKey
    Attributes:
        - Name: Owner
        - Name: EncryptionKey
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PermissionsPolicyDocument_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html#cfn-codeartifact-domain-permissionspolicydocument""", alias="PermissionsPolicyDocument")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html#cfn-codeartifact-domain-domainname""", alias="DomainName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html#cfn-codeartifact-domain-tags""", alias="Tags")
    EncryptionKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html#cfn-codeartifact-domain-encryptionkey""", alias="EncryptionKey")
    

    @property
    def tropo_type(self) -> troposphere.codeartifact.Domain:
        from troposphere.codeartifact import Domain as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codeartifact import Domain as TropoT
        return resource_to_troposphere(self, TropoT)


class Repository(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html
    Properties:
        - Name: Description
        - Name: PermissionsPolicyDocument
        - Name: DomainName
        - Name: Upstreams
        - Name: RepositoryName
        - Name: ExternalConnections
        - Name: Tags
        - Name: DomainOwner
    Attributes:
        - Name: DomainName
        - Name: Arn
        - Name: DomainOwner
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-description""", alias="Description")
    PermissionsPolicyDocument_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-permissionspolicydocument""", alias="PermissionsPolicyDocument")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-domainname""", alias="DomainName")
    Upstreams_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-upstreams""", alias="Upstreams")
    RepositoryName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-repositoryname""", alias="RepositoryName")
    ExternalConnections_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-externalconnections""", alias="ExternalConnections")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-tags""", alias="Tags")
    DomainOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-domainowner""", alias="DomainOwner")
    

    @property
    def tropo_type(self) -> troposphere.codeartifact.Repository:
        from troposphere.codeartifact import Repository as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codeartifact import Repository as TropoT
        return resource_to_troposphere(self, TropoT)

