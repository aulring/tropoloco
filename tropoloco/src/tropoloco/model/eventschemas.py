from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class TagsEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html#cfn-eventschemas-discoverer-tagsentry-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html#cfn-eventschemas-discoverer-tagsentry-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.eventschemas.TagsEntry:
        from troposphere.eventschemas import TagsEntry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagsEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html#cfn-eventschemas-registry-tagsentry-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html#cfn-eventschemas-registry-tagsentry-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.eventschemas.TagsEntry:
        from troposphere.eventschemas import TagsEntry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagsEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html#cfn-eventschemas-schema-tagsentry-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html#cfn-eventschemas-schema-tagsentry-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.eventschemas.TagsEntry:
        from troposphere.eventschemas import TagsEntry as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Discoverer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html
    Properties:
        - Name: CrossAccount
        - Name: Description
        - Name: SourceArn
        - Name: Tags
    Attributes:
        - Name: DiscovererArn
        - Name: DiscovererId
        - Name: CrossAccount
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CrossAccount_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-crossaccount""", alias="CrossAccount")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-description""", alias="Description")
    SourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-sourcearn""", alias="SourceArn")
    Tags_: Optional[List['TagsEntry']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.eventschemas.Discoverer:
        from troposphere.eventschemas import Discoverer as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.eventschemas import Discoverer as TropoT
        return resource_to_troposphere(self, TropoT)


class Registry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html
    Properties:
        - Name: Description
        - Name: RegistryName
        - Name: Tags
    Attributes:
        - Name: RegistryName
        - Name: RegistryArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-description""", alias="Description")
    RegistryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-registryname""", alias="RegistryName")
    Tags_: Optional[List['TagsEntry']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.eventschemas.Registry:
        from troposphere.eventschemas import Registry as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.eventschemas import Registry as TropoT
        return resource_to_troposphere(self, TropoT)


class RegistryPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html
    Properties:
        - Name: Policy
        - Name: RegistryName
        - Name: RevisionId
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-policy""", alias="Policy")
    RegistryName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-registryname""", alias="RegistryName")
    RevisionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-revisionid""", alias="RevisionId")
    

    @property
    def tropo_type(self) -> troposphere.eventschemas.RegistryPolicy:
        from troposphere.eventschemas import RegistryPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.eventschemas import RegistryPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class Schema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: Content
        - Name: RegistryName
        - Name: SchemaName
        - Name: Tags
    Attributes:
        - Name: SchemaVersion
        - Name: SchemaArn
        - Name: SchemaName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-description""", alias="Description")
    Content_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-content""", alias="Content")
    RegistryName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-registryname""", alias="RegistryName")
    SchemaName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-schemaname""", alias="SchemaName")
    Tags_: Optional[List['TagsEntry']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.eventschemas.Schema:
        from troposphere.eventschemas import Schema as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.eventschemas import Schema as TropoT
        return resource_to_troposphere(self, TropoT)

