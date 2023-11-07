from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AssertionAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html
    Properties:
        - Name: Role
        - Name: Email
        - Name: Org
        - Name: Groups
        - Name: Login
        - Name: Name
    
    """
    
    Role_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html#cfn-grafana-workspace-assertionattributes-role""", alias="Role")
    Email_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html#cfn-grafana-workspace-assertionattributes-email""", alias="Email")
    Org_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html#cfn-grafana-workspace-assertionattributes-org""", alias="Org")
    Groups_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html#cfn-grafana-workspace-assertionattributes-groups""", alias="Groups")
    Login_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html#cfn-grafana-workspace-assertionattributes-login""", alias="Login")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html#cfn-grafana-workspace-assertionattributes-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.grafana.AssertionAttributes:
        from troposphere.grafana import AssertionAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IdpMetadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-idpmetadata.html
    Properties:
        - Name: Xml
        - Name: Url
    
    """
    
    Xml_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-idpmetadata.html#cfn-grafana-workspace-idpmetadata-xml""", alias="Xml")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-idpmetadata.html#cfn-grafana-workspace-idpmetadata-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.grafana.IdpMetadata:
        from troposphere.grafana import IdpMetadata as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkAccessControl(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-networkaccesscontrol.html
    Properties:
        - Name: PrefixListIds
        - Name: VpceIds
    
    """
    
    PrefixListIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-networkaccesscontrol.html#cfn-grafana-workspace-networkaccesscontrol-prefixlistids""", alias="PrefixListIds")
    VpceIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-networkaccesscontrol.html#cfn-grafana-workspace-networkaccesscontrol-vpceids""", alias="VpceIds")
    


    @property
    def tropo_type(self) -> troposphere.grafana.NetworkAccessControl:
        from troposphere.grafana import NetworkAccessControl as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RoleValues(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-rolevalues.html
    Properties:
        - Name: Editor
        - Name: Admin
    
    """
    
    Editor_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-rolevalues.html#cfn-grafana-workspace-rolevalues-editor""", alias="Editor")
    Admin_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-rolevalues.html#cfn-grafana-workspace-rolevalues-admin""", alias="Admin")
    


    @property
    def tropo_type(self) -> troposphere.grafana.RoleValues:
        from troposphere.grafana import RoleValues as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SamlConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-samlconfiguration.html
    Properties:
        - Name: LoginValidityDuration
        - Name: RoleValues
        - Name: IdpMetadata
        - Name: AssertionAttributes
        - Name: AllowedOrganizations
    
    """
    
    LoginValidityDuration_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-samlconfiguration.html#cfn-grafana-workspace-samlconfiguration-loginvalidityduration""", alias="LoginValidityDuration")
    RoleValues_: Optional['RoleValues'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-samlconfiguration.html#cfn-grafana-workspace-samlconfiguration-rolevalues""", alias="RoleValues")
    IdpMetadata_: 'IdpMetadata' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-samlconfiguration.html#cfn-grafana-workspace-samlconfiguration-idpmetadata""", alias="IdpMetadata")
    AssertionAttributes_: Optional['AssertionAttributes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-samlconfiguration.html#cfn-grafana-workspace-samlconfiguration-assertionattributes""", alias="AssertionAttributes")
    AllowedOrganizations_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-samlconfiguration.html#cfn-grafana-workspace-samlconfiguration-allowedorganizations""", alias="AllowedOrganizations")
    


    @property
    def tropo_type(self) -> troposphere.grafana.SamlConfiguration:
        from troposphere.grafana import SamlConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-vpcconfiguration.html
    Properties:
        - Name: SecurityGroupIds
        - Name: SubnetIds
    
    """
    
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-vpcconfiguration.html#cfn-grafana-workspace-vpcconfiguration-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-vpcconfiguration.html#cfn-grafana-workspace-vpcconfiguration-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.grafana.VpcConfiguration:
        from troposphere.grafana import VpcConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Workspace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html
    Properties:
        - Name: NotificationDestinations
        - Name: Description
        - Name: PermissionType
        - Name: AccountAccessType
        - Name: StackSetName
        - Name: SamlConfiguration
        - Name: OrganizationalUnits
        - Name: RoleArn
        - Name: Name
        - Name: GrafanaVersion
        - Name: DataSources
        - Name: AuthenticationProviders
        - Name: OrganizationRoleName
        - Name: VpcConfiguration
        - Name: NetworkAccessControl
        - Name: ClientToken
    Attributes:
        - Name: Status
        - Name: GrafanaVersion
        - Name: CreationTimestamp
        - Name: Endpoint
        - Name: SsoClientId
        - Name: Id
        - Name: SamlConfigurationStatus
        - Name: ModificationTimestamp
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NotificationDestinations_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-notificationdestinations""", alias="NotificationDestinations")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-description""", alias="Description")
    PermissionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-permissiontype""", alias="PermissionType")
    AccountAccessType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-accountaccesstype""", alias="AccountAccessType")
    StackSetName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-stacksetname""", alias="StackSetName")
    SamlConfiguration_: Optional['SamlConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-samlconfiguration""", alias="SamlConfiguration")
    OrganizationalUnits_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-organizationalunits""", alias="OrganizationalUnits")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-rolearn""", alias="RoleArn")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-name""", alias="Name")
    GrafanaVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-grafanaversion""", alias="GrafanaVersion")
    DataSources_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-datasources""", alias="DataSources")
    AuthenticationProviders_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-authenticationproviders""", alias="AuthenticationProviders")
    OrganizationRoleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-organizationrolename""", alias="OrganizationRoleName")
    VpcConfiguration_: Optional['VpcConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-vpcconfiguration""", alias="VpcConfiguration")
    NetworkAccessControl_: Optional['NetworkAccessControl'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-networkaccesscontrol""", alias="NetworkAccessControl")
    ClientToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html#cfn-grafana-workspace-clienttoken""", alias="ClientToken")
    

    @property
    def tropo_type(self) -> troposphere.grafana.Workspace:
        from troposphere.grafana import Workspace as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.grafana import Workspace as TropoT
        return resource_to_troposphere(self, TropoT)

