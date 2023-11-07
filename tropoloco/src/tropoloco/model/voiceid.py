from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ServerSideEncryptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-voiceid-domain-serversideencryptionconfiguration.html
    Properties:
        - Name: KmsKeyId
    
    """
    
    KmsKeyId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-voiceid-domain-serversideencryptionconfiguration.html#cfn-voiceid-domain-serversideencryptionconfiguration-kmskeyid""", alias="KmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.voiceid.ServerSideEncryptionConfiguration:
        from troposphere.voiceid import ServerSideEncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Domain(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-voiceid-domain.html
    Properties:
        - Name: Description
        - Name: ServerSideEncryptionConfiguration
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: DomainId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-voiceid-domain.html#cfn-voiceid-domain-description""", alias="Description")
    ServerSideEncryptionConfiguration_: 'ServerSideEncryptionConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-voiceid-domain.html#cfn-voiceid-domain-serversideencryptionconfiguration""", alias="ServerSideEncryptionConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-voiceid-domain.html#cfn-voiceid-domain-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-voiceid-domain.html#cfn-voiceid-domain-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.voiceid.Domain:
        from troposphere.voiceid import Domain as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.voiceid import Domain as TropoT
        return resource_to_troposphere(self, TropoT)

