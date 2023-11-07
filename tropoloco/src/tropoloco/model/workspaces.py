from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ConnectionAliasAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html
    Properties:
        - Name: AssociatedAccountId
        - Name: ResourceId
        - Name: ConnectionIdentifier
        - Name: AssociationStatus
    
    """
    
    AssociatedAccountId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-associatedaccountid""", alias="AssociatedAccountId")
    ResourceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-resourceid""", alias="ResourceId")
    ConnectionIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-connectionidentifier""", alias="ConnectionIdentifier")
    AssociationStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-associationstatus""", alias="AssociationStatus")
    


    @property
    def tropo_type(self) -> troposphere.workspaces.ConnectionAliasAssociation:
        from troposphere.workspaces import ConnectionAliasAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WorkspaceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html
    Properties:
        - Name: ComputeTypeName
        - Name: RootVolumeSizeGib
        - Name: RunningMode
        - Name: RunningModeAutoStopTimeoutInMinutes
        - Name: UserVolumeSizeGib
    
    """
    
    ComputeTypeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-computetypename""", alias="ComputeTypeName")
    RootVolumeSizeGib_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-rootvolumesizegib""", alias="RootVolumeSizeGib")
    RunningMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-runningmode""", alias="RunningMode")
    RunningModeAutoStopTimeoutInMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-runningmodeautostoptimeoutinminutes""", alias="RunningModeAutoStopTimeoutInMinutes")
    UserVolumeSizeGib_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-uservolumesizegib""", alias="UserVolumeSizeGib")
    


    @property
    def tropo_type(self) -> troposphere.workspaces.WorkspaceProperties:
        from troposphere.workspaces import WorkspaceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ConnectionAlias(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html
    Properties:
        - Name: ConnectionString
        - Name: Tags
    Attributes:
        - Name: ConnectionAliasState
        - Name: Associations
        - Name: AliasId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConnectionString_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#cfn-workspaces-connectionalias-connectionstring""", alias="ConnectionString")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#cfn-workspaces-connectionalias-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.workspaces.ConnectionAlias:
        from troposphere.workspaces import ConnectionAlias as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.workspaces import ConnectionAlias as TropoT
        return resource_to_troposphere(self, TropoT)


class Workspace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html
    Properties:
        - Name: BundleId
        - Name: DirectoryId
        - Name: RootVolumeEncryptionEnabled
        - Name: Tags
        - Name: UserName
        - Name: UserVolumeEncryptionEnabled
        - Name: VolumeEncryptionKey
        - Name: WorkspaceProperties
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BundleId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-bundleid""", alias="BundleId")
    DirectoryId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-directoryid""", alias="DirectoryId")
    RootVolumeEncryptionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-rootvolumeencryptionenabled""", alias="RootVolumeEncryptionEnabled")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-tags""", alias="Tags")
    UserName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-username""", alias="UserName")
    UserVolumeEncryptionEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-uservolumeencryptionenabled""", alias="UserVolumeEncryptionEnabled")
    VolumeEncryptionKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-volumeencryptionkey""", alias="VolumeEncryptionKey")
    WorkspaceProperties_: Optional['WorkspaceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-workspaceproperties""", alias="WorkspaceProperties")
    

    @property
    def tropo_type(self) -> troposphere.workspaces.Workspace:
        from troposphere.workspaces import Workspace as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.workspaces import Workspace as TropoT
        return resource_to_troposphere(self, TropoT)

