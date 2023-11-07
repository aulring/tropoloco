from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ArtifactDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-artifactdetails.html
    Properties:
        - Name: MinimumCount
        - Name: MaximumCount
    
    """
    
    MinimumCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-artifactdetails.html#cfn-codepipeline-customactiontype-artifactdetails-minimumcount""", alias="MinimumCount")
    MaximumCount_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-artifactdetails.html#cfn-codepipeline-customactiontype-artifactdetails-maximumcount""", alias="MaximumCount")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.ArtifactDetails:
        from troposphere.codepipeline import ArtifactDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfigurationProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-configurationproperties.html
    Properties:
        - Name: Secret
        - Name: Type
        - Name: Description
        - Name: Required
        - Name: Queryable
        - Name: Key
        - Name: Name
    
    """
    
    Secret_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-configurationproperties.html#cfn-codepipeline-customactiontype-configurationproperties-secret""", alias="Secret")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-configurationproperties.html#cfn-codepipeline-customactiontype-configurationproperties-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-configurationproperties.html#cfn-codepipeline-customactiontype-configurationproperties-description""", alias="Description")
    Required_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-configurationproperties.html#cfn-codepipeline-customactiontype-configurationproperties-required""", alias="Required")
    Queryable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-configurationproperties.html#cfn-codepipeline-customactiontype-configurationproperties-queryable""", alias="Queryable")
    Key_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-configurationproperties.html#cfn-codepipeline-customactiontype-configurationproperties-key""", alias="Key")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-configurationproperties.html#cfn-codepipeline-customactiontype-configurationproperties-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.ConfigurationProperties:
        from troposphere.codepipeline import ConfigurationProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Settings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-settings.html
    Properties:
        - Name: EntityUrlTemplate
        - Name: ExecutionUrlTemplate
        - Name: RevisionUrlTemplate
        - Name: ThirdPartyConfigurationUrl
    
    """
    
    EntityUrlTemplate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-settings.html#cfn-codepipeline-customactiontype-settings-entityurltemplate""", alias="EntityUrlTemplate")
    ExecutionUrlTemplate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-settings.html#cfn-codepipeline-customactiontype-settings-executionurltemplate""", alias="ExecutionUrlTemplate")
    RevisionUrlTemplate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-settings.html#cfn-codepipeline-customactiontype-settings-revisionurltemplate""", alias="RevisionUrlTemplate")
    ThirdPartyConfigurationUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-customactiontype-settings.html#cfn-codepipeline-customactiontype-settings-thirdpartyconfigurationurl""", alias="ThirdPartyConfigurationUrl")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.Settings:
        from troposphere.codepipeline import Settings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ActionDeclaration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html
    Properties:
        - Name: ActionTypeId
        - Name: Configuration
        - Name: InputArtifacts
        - Name: Name
        - Name: Namespace
        - Name: OutputArtifacts
        - Name: Region
        - Name: RoleArn
        - Name: RunOrder
    
    """
    
    ActionTypeId_: 'ActionTypeId' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html#cfn-codepipeline-pipeline-stages-actions-actiontypeid""", alias="ActionTypeId")
    Configuration_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html#cfn-codepipeline-pipeline-stages-actions-configuration""", alias="Configuration")
    InputArtifacts_: Optional[List['InputArtifact']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html#cfn-codepipeline-pipeline-stages-actions-inputartifacts""", alias="InputArtifacts")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html#cfn-codepipeline-pipeline-stages-actions-name""", alias="Name")
    Namespace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html#cfn-codepipeline-pipeline-actiondeclaration-namespace""", alias="Namespace")
    OutputArtifacts_: Optional[List['OutputArtifact']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html#cfn-codepipeline-pipeline-stages-actions-outputartifacts""", alias="OutputArtifacts")
    Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html#cfn-codepipeline-pipeline-stages-actions-region""", alias="Region")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html#cfn-codepipeline-pipeline-stages-actions-rolearn""", alias="RoleArn")
    RunOrder_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html#cfn-codepipeline-pipeline-stages-actions-runorder""", alias="RunOrder")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.ActionDeclaration:
        from troposphere.codepipeline import ActionDeclaration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ActionTypeId(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions-actiontypeid.html
    Properties:
        - Name: Category
        - Name: Owner
        - Name: Provider
        - Name: Version
    
    """
    
    Category_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions-actiontypeid.html#cfn-codepipeline-pipeline-stages-actions-actiontypeid-category""", alias="Category")
    Owner_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions-actiontypeid.html#cfn-codepipeline-pipeline-stages-actions-actiontypeid-owner""", alias="Owner")
    Provider_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions-actiontypeid.html#cfn-codepipeline-pipeline-stages-actions-actiontypeid-provider""", alias="Provider")
    Version_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions-actiontypeid.html#cfn-codepipeline-pipeline-stages-actions-actiontypeid-version""", alias="Version")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.ActionTypeId:
        from troposphere.codepipeline import ActionTypeId as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ArtifactStore(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-artifactstore.html
    Properties:
        - Name: EncryptionKey
        - Name: Location
        - Name: Type
    
    """
    
    EncryptionKey_: Optional['EncryptionKey'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-artifactstore.html#cfn-codepipeline-pipeline-artifactstore-encryptionkey""", alias="EncryptionKey")
    Location_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-artifactstore.html#cfn-codepipeline-pipeline-artifactstore-location""", alias="Location")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-artifactstore.html#cfn-codepipeline-pipeline-artifactstore-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.ArtifactStore:
        from troposphere.codepipeline import ArtifactStore as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ArtifactStoreMap(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-artifactstoremap.html
    Properties:
        - Name: ArtifactStore
        - Name: Region
    
    """
    
    ArtifactStore_: 'ArtifactStore' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-artifactstoremap.html#cfn-codepipeline-pipeline-artifactstoremap-artifactstore""", alias="ArtifactStore")
    Region_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-artifactstoremap.html#cfn-codepipeline-pipeline-artifactstoremap-region""", alias="Region")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.ArtifactStoreMap:
        from troposphere.codepipeline import ArtifactStoreMap as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BlockerDeclaration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-blockers.html
    Properties:
        - Name: Name
        - Name: Type
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-blockers.html#cfn-codepipeline-pipeline-stages-blockers-name""", alias="Name")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-blockers.html#cfn-codepipeline-pipeline-stages-blockers-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.BlockerDeclaration:
        from troposphere.codepipeline import BlockerDeclaration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-artifactstore-encryptionkey.html
    Properties:
        - Name: Id
        - Name: Type
    
    """
    
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-artifactstore-encryptionkey.html#cfn-codepipeline-pipeline-artifactstore-encryptionkey-id""", alias="Id")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-artifactstore-encryptionkey.html#cfn-codepipeline-pipeline-artifactstore-encryptionkey-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.EncryptionKey:
        from troposphere.codepipeline import EncryptionKey as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputArtifact(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions-inputartifacts.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions-inputartifacts.html#cfn-codepipeline-pipeline-stages-actions-inputartifacts-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.InputArtifact:
        from troposphere.codepipeline import InputArtifact as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputArtifact(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions-outputartifacts.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions-outputartifacts.html#cfn-codepipeline-pipeline-stages-actions-outputartifacts-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.OutputArtifact:
        from troposphere.codepipeline import OutputArtifact as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StageDeclaration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages.html
    Properties:
        - Name: Actions
        - Name: Blockers
        - Name: Name
    
    """
    
    Actions_: List['ActionDeclaration'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages.html#cfn-codepipeline-pipeline-stages-actions""", alias="Actions")
    Blockers_: Optional[List['BlockerDeclaration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages.html#cfn-codepipeline-pipeline-stages-blockers""", alias="Blockers")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages.html#cfn-codepipeline-pipeline-stages-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.StageDeclaration:
        from troposphere.codepipeline import StageDeclaration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StageTransition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-disableinboundstagetransitions.html
    Properties:
        - Name: Reason
        - Name: StageName
    
    """
    
    Reason_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-disableinboundstagetransitions.html#cfn-codepipeline-pipeline-disableinboundstagetransitions-reason""", alias="Reason")
    StageName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-disableinboundstagetransitions.html#cfn-codepipeline-pipeline-disableinboundstagetransitions-stagename""", alias="StageName")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.StageTransition:
        from troposphere.codepipeline import StageTransition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WebhookAuthConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-webhook-webhookauthconfiguration.html
    Properties:
        - Name: AllowedIPRange
        - Name: SecretToken
    
    """
    
    AllowedIPRange_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-webhook-webhookauthconfiguration.html#cfn-codepipeline-webhook-webhookauthconfiguration-allowediprange""", alias="AllowedIPRange")
    SecretToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-webhook-webhookauthconfiguration.html#cfn-codepipeline-webhook-webhookauthconfiguration-secrettoken""", alias="SecretToken")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.WebhookAuthConfiguration:
        from troposphere.codepipeline import WebhookAuthConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WebhookFilterRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-webhook-webhookfilterrule.html
    Properties:
        - Name: JsonPath
        - Name: MatchEquals
    
    """
    
    JsonPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-webhook-webhookfilterrule.html#cfn-codepipeline-webhook-webhookfilterrule-jsonpath""", alias="JsonPath")
    MatchEquals_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-webhook-webhookfilterrule.html#cfn-codepipeline-webhook-webhookfilterrule-matchequals""", alias="MatchEquals")
    


    @property
    def tropo_type(self) -> troposphere.codepipeline.WebhookFilterRule:
        from troposphere.codepipeline import WebhookFilterRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class CustomActionType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-customactiontype.html
    Properties:
        - Name: Category
        - Name: InputArtifactDetails
        - Name: Version
        - Name: OutputArtifactDetails
        - Name: ConfigurationProperties
        - Name: Settings
        - Name: Tags
        - Name: Provider
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Category_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-customactiontype.html#cfn-codepipeline-customactiontype-category""", alias="Category")
    InputArtifactDetails_: 'ArtifactDetails' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-customactiontype.html#cfn-codepipeline-customactiontype-inputartifactdetails""", alias="InputArtifactDetails")
    Version_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-customactiontype.html#cfn-codepipeline-customactiontype-version""", alias="Version")
    OutputArtifactDetails_: 'ArtifactDetails' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-customactiontype.html#cfn-codepipeline-customactiontype-outputartifactdetails""", alias="OutputArtifactDetails")
    ConfigurationProperties_: Optional[List['ConfigurationProperties']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-customactiontype.html#cfn-codepipeline-customactiontype-configurationproperties""", alias="ConfigurationProperties")
    Settings_: Optional['Settings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-customactiontype.html#cfn-codepipeline-customactiontype-settings""", alias="Settings")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-customactiontype.html#cfn-codepipeline-customactiontype-tags""", alias="Tags")
    Provider_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-customactiontype.html#cfn-codepipeline-customactiontype-provider""", alias="Provider")
    

    @property
    def tropo_type(self) -> troposphere.codepipeline.CustomActionType:
        from troposphere.codepipeline import CustomActionType as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codepipeline import CustomActionType as TropoT
        return resource_to_troposphere(self, TropoT)


class Pipeline(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html
    Properties:
        - Name: ArtifactStore
        - Name: ArtifactStores
        - Name: DisableInboundStageTransitions
        - Name: Name
        - Name: RestartExecutionOnUpdate
        - Name: RoleArn
        - Name: Stages
        - Name: Tags
    Attributes:
        - Name: Version
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ArtifactStore_: Optional['ArtifactStore'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html#cfn-codepipeline-pipeline-artifactstore""", alias="ArtifactStore")
    ArtifactStores_: Optional[List['ArtifactStoreMap']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html#cfn-codepipeline-pipeline-artifactstores""", alias="ArtifactStores")
    DisableInboundStageTransitions_: Optional[List['StageTransition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html#cfn-codepipeline-pipeline-disableinboundstagetransitions""", alias="DisableInboundStageTransitions")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html#cfn-codepipeline-pipeline-name""", alias="Name")
    RestartExecutionOnUpdate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html#cfn-codepipeline-pipeline-restartexecutiononupdate""", alias="RestartExecutionOnUpdate")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html#cfn-codepipeline-pipeline-rolearn""", alias="RoleArn")
    Stages_: List['StageDeclaration'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html#cfn-codepipeline-pipeline-stages""", alias="Stages")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html#cfn-codepipeline-pipeline-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.codepipeline.Pipeline:
        from troposphere.codepipeline import Pipeline as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codepipeline import Pipeline as TropoT
        return resource_to_troposphere(self, TropoT)


class Webhook(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html
    Properties:
        - Name: AuthenticationConfiguration
        - Name: Filters
        - Name: Authentication
        - Name: TargetPipeline
        - Name: TargetAction
        - Name: Name
        - Name: TargetPipelineVersion
        - Name: RegisterWithThirdParty
    Attributes:
        - Name: Url
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AuthenticationConfiguration_: 'WebhookAuthConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html#cfn-codepipeline-webhook-authenticationconfiguration""", alias="AuthenticationConfiguration")
    Filters_: List['WebhookFilterRule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html#cfn-codepipeline-webhook-filters""", alias="Filters")
    Authentication_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html#cfn-codepipeline-webhook-authentication""", alias="Authentication")
    TargetPipeline_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html#cfn-codepipeline-webhook-targetpipeline""", alias="TargetPipeline")
    TargetAction_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html#cfn-codepipeline-webhook-targetaction""", alias="TargetAction")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html#cfn-codepipeline-webhook-name""", alias="Name")
    TargetPipelineVersion_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html#cfn-codepipeline-webhook-targetpipelineversion""", alias="TargetPipelineVersion")
    RegisterWithThirdParty_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html#cfn-codepipeline-webhook-registerwiththirdparty""", alias="RegisterWithThirdParty")
    

    @property
    def tropo_type(self) -> troposphere.codepipeline.Webhook:
        from troposphere.codepipeline import Webhook as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codepipeline import Webhook as TropoT
        return resource_to_troposphere(self, TropoT)

