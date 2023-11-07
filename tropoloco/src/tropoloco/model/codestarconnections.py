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

