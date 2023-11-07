from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Tags(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html#cfn-appconfig-application-tags-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html#cfn-appconfig-application-tags-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.appconfig.Tags:
        from troposphere.appconfig import Tags as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tags(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html#cfn-appconfig-configurationprofile-tags-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html#cfn-appconfig-configurationprofile-tags-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.appconfig.Tags:
        from troposphere.appconfig import Tags as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Validators(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html
    Properties:
        - Name: Type
        - Name: Content
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html#cfn-appconfig-configurationprofile-validators-type""", alias="Type")
    Content_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html#cfn-appconfig-configurationprofile-validators-content""", alias="Content")
    


    @property
    def tropo_type(self) -> troposphere.appconfig.Validators:
        from troposphere.appconfig import Validators as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tags(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html#cfn-appconfig-deployment-tags-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html#cfn-appconfig-deployment-tags-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.appconfig.Tags:
        from troposphere.appconfig import Tags as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tags(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html#cfn-appconfig-deploymentstrategy-tags-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html#cfn-appconfig-deploymentstrategy-tags-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.appconfig.Tags:
        from troposphere.appconfig import Tags as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Monitors(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html
    Properties:
        - Name: AlarmArn
        - Name: AlarmRoleArn
    
    """
    
    AlarmArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html#cfn-appconfig-environment-monitors-alarmarn""", alias="AlarmArn")
    AlarmRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html#cfn-appconfig-environment-monitors-alarmrolearn""", alias="AlarmRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.appconfig.Monitors:
        from troposphere.appconfig import Monitors as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tags(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html#cfn-appconfig-environment-tags-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html#cfn-appconfig-environment-tags-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.appconfig.Tags:
        from troposphere.appconfig import Tags as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Parameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-parameter.html
    Properties:
        - Name: Description
        - Name: Required
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-parameter.html#cfn-appconfig-extension-parameter-description""", alias="Description")
    Required_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-parameter.html#cfn-appconfig-extension-parameter-required""", alias="Required")
    


    @property
    def tropo_type(self) -> troposphere.appconfig.Parameter:
        from troposphere.appconfig import Parameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Application(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html
    Properties:
        - Name: Description
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ApplicationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-description""", alias="Description")
    Tags_: Optional[List['Tags']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.appconfig.Application:
        from troposphere.appconfig import Application as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appconfig import Application as TropoT
        return resource_to_troposphere(self, TropoT)


class ConfigurationProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html
    Properties:
        - Name: LocationUri
        - Name: Type
        - Name: KmsKeyIdentifier
        - Name: Description
        - Name: Validators
        - Name: RetrievalRoleArn
        - Name: ApplicationId
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ConfigurationProfileId
        - Name: KmsKeyArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LocationUri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-locationuri""", alias="LocationUri")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-type""", alias="Type")
    KmsKeyIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-kmskeyidentifier""", alias="KmsKeyIdentifier")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-description""", alias="Description")
    Validators_: Optional[List['Validators']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-validators""", alias="Validators")
    RetrievalRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-retrievalrolearn""", alias="RetrievalRoleArn")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-applicationid""", alias="ApplicationId")
    Tags_: Optional[List['Tags']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.appconfig.ConfigurationProfile:
        from troposphere.appconfig import ConfigurationProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appconfig import ConfigurationProfile as TropoT
        return resource_to_troposphere(self, TropoT)


class Deployment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html
    Properties:
        - Name: DeploymentStrategyId
        - Name: ConfigurationProfileId
        - Name: EnvironmentId
        - Name: KmsKeyIdentifier
        - Name: Description
        - Name: ConfigurationVersion
        - Name: ApplicationId
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DeploymentStrategyId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-deploymentstrategyid""", alias="DeploymentStrategyId")
    ConfigurationProfileId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationprofileid""", alias="ConfigurationProfileId")
    EnvironmentId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-environmentid""", alias="EnvironmentId")
    KmsKeyIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-kmskeyidentifier""", alias="KmsKeyIdentifier")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-description""", alias="Description")
    ConfigurationVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationversion""", alias="ConfigurationVersion")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-applicationid""", alias="ApplicationId")
    Tags_: Optional[List['Tags']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.appconfig.Deployment:
        from troposphere.appconfig import Deployment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appconfig import Deployment as TropoT
        return resource_to_troposphere(self, TropoT)


class DeploymentStrategy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html
    Properties:
        - Name: ReplicateTo
        - Name: GrowthType
        - Name: Description
        - Name: DeploymentDurationInMinutes
        - Name: GrowthFactor
        - Name: FinalBakeTimeInMinutes
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ReplicateTo_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-replicateto""", alias="ReplicateTo")
    GrowthType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthtype""", alias="GrowthType")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-description""", alias="Description")
    DeploymentDurationInMinutes_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-deploymentdurationinminutes""", alias="DeploymentDurationInMinutes")
    GrowthFactor_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthfactor""", alias="GrowthFactor")
    FinalBakeTimeInMinutes_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-finalbaketimeinminutes""", alias="FinalBakeTimeInMinutes")
    Tags_: Optional[List['Tags']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.appconfig.DeploymentStrategy:
        from troposphere.appconfig import DeploymentStrategy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appconfig import DeploymentStrategy as TropoT
        return resource_to_troposphere(self, TropoT)


class Environment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html
    Properties:
        - Name: Description
        - Name: Monitors
        - Name: ApplicationId
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-description""", alias="Description")
    Monitors_: Optional[List['Monitors']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-monitors""", alias="Monitors")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-applicationid""", alias="ApplicationId")
    Tags_: Optional[List['Tags']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.appconfig.Environment:
        from troposphere.appconfig import Environment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appconfig import Environment as TropoT
        return resource_to_troposphere(self, TropoT)


class Extension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html
    Properties:
        - Name: Description
        - Name: Parameters
        - Name: Actions
        - Name: LatestVersionNumber
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
        - Name: VersionNumber
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-description""", alias="Description")
    Parameters_: Optional[Dict[str, 'Parameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-parameters""", alias="Parameters")
    Actions_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-actions""", alias="Actions")
    LatestVersionNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-latestversionnumber""", alias="LatestVersionNumber")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.appconfig.Extension:
        from troposphere.appconfig import Extension as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appconfig import Extension as TropoT
        return resource_to_troposphere(self, TropoT)


class ExtensionAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html
    Properties:
        - Name: ResourceIdentifier
        - Name: Parameters
        - Name: ExtensionIdentifier
        - Name: ExtensionVersionNumber
        - Name: Tags
    Attributes:
        - Name: ResourceArn
        - Name: ExtensionArn
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-resourceidentifier""", alias="ResourceIdentifier")
    Parameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-parameters""", alias="Parameters")
    ExtensionIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-extensionidentifier""", alias="ExtensionIdentifier")
    ExtensionVersionNumber_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-extensionversionnumber""", alias="ExtensionVersionNumber")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.appconfig.ExtensionAssociation:
        from troposphere.appconfig import ExtensionAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appconfig import ExtensionAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class HostedConfigurationVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html
    Properties:
        - Name: ConfigurationProfileId
        - Name: Description
        - Name: ContentType
        - Name: LatestVersionNumber
        - Name: Content
        - Name: VersionLabel
        - Name: ApplicationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConfigurationProfileId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-configurationprofileid""", alias="ConfigurationProfileId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-description""", alias="Description")
    ContentType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-contenttype""", alias="ContentType")
    LatestVersionNumber_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-latestversionnumber""", alias="LatestVersionNumber")
    Content_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-content""", alias="Content")
    VersionLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-versionlabel""", alias="VersionLabel")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-applicationid""", alias="ApplicationId")
    

    @property
    def tropo_type(self) -> troposphere.appconfig.HostedConfigurationVersion:
        from troposphere.appconfig import HostedConfigurationVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.appconfig import HostedConfigurationVersion as TropoT
        return resource_to_troposphere(self, TropoT)

