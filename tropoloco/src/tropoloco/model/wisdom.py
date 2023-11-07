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
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistant-serversideencryptionconfiguration.html
    Properties:
        - Name: KmsKeyId
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistant-serversideencryptionconfiguration.html#cfn-wisdom-assistant-serversideencryptionconfiguration-kmskeyid""", alias="KmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.wisdom.ServerSideEncryptionConfiguration:
        from troposphere.wisdom import ServerSideEncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssociationData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistantassociation-associationdata.html
    Properties:
        - Name: KnowledgeBaseId
    
    """
    
    KnowledgeBaseId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistantassociation-associationdata.html#cfn-wisdom-assistantassociation-associationdata-knowledgebaseid""", alias="KnowledgeBaseId")
    


    @property
    def tropo_type(self) -> troposphere.wisdom.AssociationData:
        from troposphere.wisdom import AssociationData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AppIntegrationsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html
    Properties:
        - Name: ObjectFields
        - Name: AppIntegrationArn
    
    """
    
    ObjectFields_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html#cfn-wisdom-knowledgebase-appintegrationsconfiguration-objectfields""", alias="ObjectFields")
    AppIntegrationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html#cfn-wisdom-knowledgebase-appintegrationsconfiguration-appintegrationarn""", alias="AppIntegrationArn")
    


    @property
    def tropo_type(self) -> troposphere.wisdom.AppIntegrationsConfiguration:
        from troposphere.wisdom import AppIntegrationsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RenderingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-renderingconfiguration.html
    Properties:
        - Name: TemplateUri
    
    """
    
    TemplateUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-renderingconfiguration.html#cfn-wisdom-knowledgebase-renderingconfiguration-templateuri""", alias="TemplateUri")
    


    @property
    def tropo_type(self) -> troposphere.wisdom.RenderingConfiguration:
        from troposphere.wisdom import RenderingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServerSideEncryptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.html
    Properties:
        - Name: KmsKeyId
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.html#cfn-wisdom-knowledgebase-serversideencryptionconfiguration-kmskeyid""", alias="KmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.wisdom.ServerSideEncryptionConfiguration:
        from troposphere.wisdom import ServerSideEncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-sourceconfiguration.html
    Properties:
        - Name: AppIntegrations
    
    """
    
    AppIntegrations_: 'AppIntegrationsConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-sourceconfiguration.html#cfn-wisdom-knowledgebase-sourceconfiguration-appintegrations""", alias="AppIntegrations")
    


    @property
    def tropo_type(self) -> troposphere.wisdom.SourceConfiguration:
        from troposphere.wisdom import SourceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Assistant(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: ServerSideEncryptionConfiguration
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: AssistantArn
        - Name: AssistantId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-description""", alias="Description")
    ServerSideEncryptionConfiguration_: Optional['ServerSideEncryptionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-serversideencryptionconfiguration""", alias="ServerSideEncryptionConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wisdom.Assistant:
        from troposphere.wisdom import Assistant as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wisdom import Assistant as TropoT
        return resource_to_troposphere(self, TropoT)


class AssistantAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html
    Properties:
        - Name: Association
        - Name: AssociationType
        - Name: AssistantId
        - Name: Tags
    Attributes:
        - Name: AssistantAssociationArn
        - Name: AssistantArn
        - Name: AssistantAssociationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Association_: 'AssociationData' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-association""", alias="Association")
    AssociationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-associationtype""", alias="AssociationType")
    AssistantId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-assistantid""", alias="AssistantId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.wisdom.AssistantAssociation:
        from troposphere.wisdom import AssistantAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wisdom import AssistantAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class KnowledgeBase(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html
    Properties:
        - Name: Description
        - Name: KnowledgeBaseType
        - Name: SourceConfiguration
        - Name: ServerSideEncryptionConfiguration
        - Name: RenderingConfiguration
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: KnowledgeBaseArn
        - Name: KnowledgeBaseId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-description""", alias="Description")
    KnowledgeBaseType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-knowledgebasetype""", alias="KnowledgeBaseType")
    SourceConfiguration_: Optional['SourceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-sourceconfiguration""", alias="SourceConfiguration")
    ServerSideEncryptionConfiguration_: Optional['ServerSideEncryptionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-serversideencryptionconfiguration""", alias="ServerSideEncryptionConfiguration")
    RenderingConfiguration_: Optional['RenderingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-renderingconfiguration""", alias="RenderingConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wisdom.KnowledgeBase:
        from troposphere.wisdom import KnowledgeBase as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wisdom import KnowledgeBase as TropoT
        return resource_to_troposphere(self, TropoT)

