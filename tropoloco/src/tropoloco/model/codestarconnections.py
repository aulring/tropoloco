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


class Connection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html
    Properties:
        - Name: ConnectionName
        - Name: HostArn
        - Name: ProviderType
        - Name: Tags
    Attributes:
        - Name: ConnectionArn
        - Name: ConnectionStatus
        - Name: OwnerAccountId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConnectionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html#cfn-codestarconnections-connection-connectionname""", alias="ConnectionName")
    HostArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html#cfn-codestarconnections-connection-hostarn""", alias="HostArn")
    ProviderType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html#cfn-codestarconnections-connection-providertype""", alias="ProviderType")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html#cfn-codestarconnections-connection-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.codestarconnections.Connection:
        from troposphere.codestarconnections import Connection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codestarconnections import Connection as TropoT
        return resource_to_troposphere(self, TropoT)


class RepositoryLink(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-repositorylink.html
    Properties:
        - Name: OwnerId
        - Name: EncryptionKeyArn
        - Name: ConnectionArn
        - Name: RepositoryName
        - Name: Tags
    Attributes:
        - Name: RepositoryLinkArn
        - Name: ProviderType
        - Name: RepositoryLinkId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OwnerId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-repositorylink.html#cfn-codestarconnections-repositorylink-ownerid""", alias="OwnerId")
    EncryptionKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-repositorylink.html#cfn-codestarconnections-repositorylink-encryptionkeyarn""", alias="EncryptionKeyArn")
    ConnectionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-repositorylink.html#cfn-codestarconnections-repositorylink-connectionarn""", alias="ConnectionArn")
    RepositoryName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-repositorylink.html#cfn-codestarconnections-repositorylink-repositoryname""", alias="RepositoryName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-repositorylink.html#cfn-codestarconnections-repositorylink-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.codestarconnections.RepositoryLink:
        from troposphere.codestarconnections import RepositoryLink as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codestarconnections import RepositoryLink as TropoT
        return resource_to_troposphere(self, TropoT)


class SyncConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html
    Properties:
        - Name: ConfigFile
        - Name: ResourceName
        - Name: Branch
        - Name: SyncType
        - Name: RepositoryLinkId
        - Name: RoleArn
    Attributes:
        - Name: OwnerId
        - Name: RepositoryName
        - Name: ProviderType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConfigFile_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-configfile""", alias="ConfigFile")
    ResourceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-resourcename""", alias="ResourceName")
    Branch_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-branch""", alias="Branch")
    SyncType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-synctype""", alias="SyncType")
    RepositoryLinkId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-repositorylinkid""", alias="RepositoryLinkId")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-rolearn""", alias="RoleArn")
    

    @property
    def tropo_type(self) -> troposphere.codestarconnections.SyncConfiguration:
        from troposphere.codestarconnections import SyncConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codestarconnections import SyncConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)

