from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class LoggingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-hookversion-loggingconfig.html
    Properties:
        - Name: LogGroupName
        - Name: LogRoleArn
    
    """
    
    LogGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-hookversion-loggingconfig.html#cfn-cloudformation-hookversion-loggingconfig-loggroupname""", alias="LogGroupName")
    LogRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-hookversion-loggingconfig.html#cfn-cloudformation-hookversion-loggingconfig-logrolearn""", alias="LogRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.cloudformation.LoggingConfig:
        from troposphere.cloudformation import LoggingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-resourceversion-loggingconfig.html
    Properties:
        - Name: LogGroupName
        - Name: LogRoleArn
    
    """
    
    LogGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-resourceversion-loggingconfig.html#cfn-cloudformation-resourceversion-loggingconfig-loggroupname""", alias="LogGroupName")
    LogRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-resourceversion-loggingconfig.html#cfn-cloudformation-resourceversion-loggingconfig-logrolearn""", alias="LogRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.cloudformation.LoggingConfig:
        from troposphere.cloudformation import LoggingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoDeployment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html
    Properties:
        - Name: Enabled
        - Name: RetainStacksOnAccountRemoval
    
    """
    
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html#cfn-cloudformation-stackset-autodeployment-enabled""", alias="Enabled")
    RetainStacksOnAccountRemoval_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html#cfn-cloudformation-stackset-autodeployment-retainstacksonaccountremoval""", alias="RetainStacksOnAccountRemoval")
    


    @property
    def tropo_type(self) -> troposphere.cloudformation.AutoDeployment:
        from troposphere.cloudformation import AutoDeployment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentTargets(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html
    Properties:
        - Name: AccountFilterType
        - Name: Accounts
        - Name: AccountsUrl
        - Name: OrganizationalUnitIds
    
    """
    
    AccountFilterType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html#cfn-cloudformation-stackset-deploymenttargets-accountfiltertype""", alias="AccountFilterType")
    Accounts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html#cfn-cloudformation-stackset-deploymenttargets-accounts""", alias="Accounts")
    AccountsUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html#cfn-cloudformation-stackset-deploymenttargets-accountsurl""", alias="AccountsUrl")
    OrganizationalUnitIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html#cfn-cloudformation-stackset-deploymenttargets-organizationalunitids""", alias="OrganizationalUnitIds")
    


    @property
    def tropo_type(self) -> troposphere.cloudformation.DeploymentTargets:
        from troposphere.cloudformation import DeploymentTargets as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ManagedExecution(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-managedexecution.html
    Properties:
        - Name: Active
    
    """
    
    Active_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-managedexecution.html#cfn-cloudformation-stackset-managedexecution-active""", alias="Active")
    


    @property
    def tropo_type(self) -> troposphere.cloudformation.ManagedExecution:
        from troposphere.cloudformation import ManagedExecution as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OperationPreferences(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html
    Properties:
        - Name: MaxConcurrentPercentage
        - Name: RegionConcurrencyType
        - Name: MaxConcurrentCount
        - Name: FailureTolerancePercentage
        - Name: FailureToleranceCount
        - Name: RegionOrder
    
    """
    
    MaxConcurrentPercentage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-maxconcurrentpercentage""", alias="MaxConcurrentPercentage")
    RegionConcurrencyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-regionconcurrencytype""", alias="RegionConcurrencyType")
    MaxConcurrentCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-maxconcurrentcount""", alias="MaxConcurrentCount")
    FailureTolerancePercentage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-failuretolerancepercentage""", alias="FailureTolerancePercentage")
    FailureToleranceCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-failuretolerancecount""", alias="FailureToleranceCount")
    RegionOrder_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-regionorder""", alias="RegionOrder")
    


    @property
    def tropo_type(self) -> troposphere.cloudformation.OperationPreferences:
        from troposphere.cloudformation import OperationPreferences as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Parameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html
    Properties:
        - Name: ParameterValue
        - Name: ParameterKey
    
    """
    
    ParameterValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html#cfn-cloudformation-stackset-parameter-parametervalue""", alias="ParameterValue")
    ParameterKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html#cfn-cloudformation-stackset-parameter-parameterkey""", alias="ParameterKey")
    


    @property
    def tropo_type(self) -> troposphere.cloudformation.Parameter:
        from troposphere.cloudformation import Parameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StackInstances(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html
    Properties:
        - Name: ParameterOverrides
        - Name: DeploymentTargets
        - Name: Regions
    
    """
    
    ParameterOverrides_: Optional[List['Parameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html#cfn-cloudformation-stackset-stackinstances-parameteroverrides""", alias="ParameterOverrides")
    DeploymentTargets_: 'DeploymentTargets' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html#cfn-cloudformation-stackset-stackinstances-deploymenttargets""", alias="DeploymentTargets")
    Regions_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html#cfn-cloudformation-stackset-stackinstances-regions""", alias="Regions")
    


    @property
    def tropo_type(self) -> troposphere.cloudformation.StackInstances:
        from troposphere.cloudformation import StackInstances as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-typeactivation-loggingconfig.html
    Properties:
        - Name: LogGroupName
        - Name: LogRoleArn
    
    """
    
    LogGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-typeactivation-loggingconfig.html#cfn-cloudformation-typeactivation-loggingconfig-loggroupname""", alias="LogGroupName")
    LogRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-typeactivation-loggingconfig.html#cfn-cloudformation-typeactivation-loggingconfig-logrolearn""", alias="LogRoleArn")
    


    @property
    def tropo_type(self) -> troposphere.cloudformation.LoggingConfig:
        from troposphere.cloudformation import LoggingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class CustomResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html
    Properties:
        - Name: ServiceToken
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ServiceToken_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#cfn-customresource-servicetoken""", alias="ServiceToken")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.CustomResource:
        from troposphere.cloudformation import CustomResource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import CustomResource as TropoT
        return resource_to_troposphere(self, TropoT)


class HookDefaultVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html
    Properties:
        - Name: VersionId
        - Name: TypeName
        - Name: TypeVersionArn
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VersionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html#cfn-cloudformation-hookdefaultversion-versionid""", alias="VersionId")
    TypeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html#cfn-cloudformation-hookdefaultversion-typename""", alias="TypeName")
    TypeVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html#cfn-cloudformation-hookdefaultversion-typeversionarn""", alias="TypeVersionArn")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.HookDefaultVersion:
        from troposphere.cloudformation import HookDefaultVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import HookDefaultVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class HookTypeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html
    Properties:
        - Name: TypeName
        - Name: Configuration
        - Name: TypeArn
        - Name: ConfigurationAlias
    Attributes:
        - Name: ConfigurationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TypeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html#cfn-cloudformation-hooktypeconfig-typename""", alias="TypeName")
    Configuration_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html#cfn-cloudformation-hooktypeconfig-configuration""", alias="Configuration")
    TypeArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html#cfn-cloudformation-hooktypeconfig-typearn""", alias="TypeArn")
    ConfigurationAlias_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html#cfn-cloudformation-hooktypeconfig-configurationalias""", alias="ConfigurationAlias")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.HookTypeConfig:
        from troposphere.cloudformation import HookTypeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import HookTypeConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class HookVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookversion.html
    Properties:
        - Name: ExecutionRoleArn
        - Name: TypeName
        - Name: LoggingConfig
        - Name: SchemaHandlerPackage
    Attributes:
        - Name: VersionId
        - Name: IsDefaultVersion
        - Name: Visibility
        - Name: Arn
        - Name: TypeArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ExecutionRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookversion.html#cfn-cloudformation-hookversion-executionrolearn""", alias="ExecutionRoleArn")
    TypeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookversion.html#cfn-cloudformation-hookversion-typename""", alias="TypeName")
    LoggingConfig_: Optional['LoggingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookversion.html#cfn-cloudformation-hookversion-loggingconfig""", alias="LoggingConfig")
    SchemaHandlerPackage_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookversion.html#cfn-cloudformation-hookversion-schemahandlerpackage""", alias="SchemaHandlerPackage")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.HookVersion:
        from troposphere.cloudformation import HookVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import HookVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class Macro(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html
    Properties:
        - Name: Description
        - Name: FunctionName
        - Name: LogGroupName
        - Name: LogRoleARN
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-description""", alias="Description")
    FunctionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-functionname""", alias="FunctionName")
    LogGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-loggroupname""", alias="LogGroupName")
    LogRoleARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-logrolearn""", alias="LogRoleARN")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.Macro:
        from troposphere.cloudformation import Macro as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import Macro as TropoT
        return resource_to_troposphere(self, TropoT)


class ModuleDefaultVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html
    Properties:
        - Name: VersionId
        - Name: ModuleName
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VersionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-versionid""", alias="VersionId")
    ModuleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-modulename""", alias="ModuleName")
    Arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-arn""", alias="Arn")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.ModuleDefaultVersion:
        from troposphere.cloudformation import ModuleDefaultVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import ModuleDefaultVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class ModuleVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html
    Properties:
        - Name: ModulePackage
        - Name: ModuleName
    Attributes:
        - Name: TimeCreated
        - Name: VersionId
        - Name: Description
        - Name: Schema
        - Name: IsDefaultVersion
        - Name: Visibility
        - Name: Arn
        - Name: DocumentationUrl
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ModulePackage_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulepackage""", alias="ModulePackage")
    ModuleName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulename""", alias="ModuleName")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.ModuleVersion:
        from troposphere.cloudformation import ModuleVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import ModuleVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class PublicTypeVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html
    Properties:
        - Name: TypeName
        - Name: LogDeliveryBucket
        - Name: Type
        - Name: PublicVersionNumber
        - Name: Arn
    Attributes:
        - Name: PublicTypeArn
        - Name: PublisherId
        - Name: TypeVersionArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TypeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-typename""", alias="TypeName")
    LogDeliveryBucket_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-logdeliverybucket""", alias="LogDeliveryBucket")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-type""", alias="Type")
    PublicVersionNumber_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-publicversionnumber""", alias="PublicVersionNumber")
    Arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-arn""", alias="Arn")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.PublicTypeVersion:
        from troposphere.cloudformation import PublicTypeVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import PublicTypeVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class Publisher(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html
    Properties:
        - Name: AcceptTermsAndConditions
        - Name: ConnectionArn
    Attributes:
        - Name: PublisherId
        - Name: IdentityProvider
        - Name: PublisherProfile
        - Name: PublisherStatus
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AcceptTermsAndConditions_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-accepttermsandconditions""", alias="AcceptTermsAndConditions")
    ConnectionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-connectionarn""", alias="ConnectionArn")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.Publisher:
        from troposphere.cloudformation import Publisher as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import Publisher as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourceDefaultVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html
    Properties:
        - Name: VersionId
        - Name: TypeName
        - Name: TypeVersionArn
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VersionId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-versionid""", alias="VersionId")
    TypeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-typename""", alias="TypeName")
    TypeVersionArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-typeversionarn""", alias="TypeVersionArn")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.ResourceDefaultVersion:
        from troposphere.cloudformation import ResourceDefaultVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import ResourceDefaultVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourceVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html
    Properties:
        - Name: ExecutionRoleArn
        - Name: TypeName
        - Name: LoggingConfig
        - Name: SchemaHandlerPackage
    Attributes:
        - Name: VersionId
        - Name: ProvisioningType
        - Name: IsDefaultVersion
        - Name: Visibility
        - Name: Arn
        - Name: TypeArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ExecutionRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-executionrolearn""", alias="ExecutionRoleArn")
    TypeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-typename""", alias="TypeName")
    LoggingConfig_: Optional['LoggingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-loggingconfig""", alias="LoggingConfig")
    SchemaHandlerPackage_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-schemahandlerpackage""", alias="SchemaHandlerPackage")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.ResourceVersion:
        from troposphere.cloudformation import ResourceVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import ResourceVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class Stack(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html
    Properties:
        - Name: NotificationARNs
        - Name: Parameters
        - Name: Tags
        - Name: TemplateURL
        - Name: TimeoutInMinutes
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NotificationARNs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-notificationarns""", alias="NotificationARNs")
    Parameters_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-parameters""", alias="Parameters")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-tags""", alias="Tags")
    TemplateURL_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-templateurl""", alias="TemplateURL")
    TimeoutInMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-timeoutinminutes""", alias="TimeoutInMinutes")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.Stack:
        from troposphere.cloudformation import Stack as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import Stack as TropoT
        return resource_to_troposphere(self, TropoT)


class StackSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html
    Properties:
        - Name: Description
        - Name: Parameters
        - Name: StackInstancesGroup
        - Name: TemplateBody
        - Name: StackSetName
        - Name: CallAs
        - Name: OperationPreferences
        - Name: TemplateURL
        - Name: AutoDeployment
        - Name: Capabilities
        - Name: PermissionModel
        - Name: AdministrationRoleARN
        - Name: ExecutionRoleName
        - Name: ManagedExecution
        - Name: Tags
    Attributes:
        - Name: StackSetId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-description""", alias="Description")
    Parameters_: Optional[List['Parameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-parameters""", alias="Parameters")
    StackInstancesGroup_: Optional[List['StackInstances']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-stackinstancesgroup""", alias="StackInstancesGroup")
    TemplateBody_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-templatebody""", alias="TemplateBody")
    StackSetName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-stacksetname""", alias="StackSetName")
    CallAs_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-callas""", alias="CallAs")
    OperationPreferences_: Optional['OperationPreferences'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-operationpreferences""", alias="OperationPreferences")
    TemplateURL_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-templateurl""", alias="TemplateURL")
    AutoDeployment_: Optional['AutoDeployment'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-autodeployment""", alias="AutoDeployment")
    Capabilities_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-capabilities""", alias="Capabilities")
    PermissionModel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-permissionmodel""", alias="PermissionModel")
    AdministrationRoleARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-administrationrolearn""", alias="AdministrationRoleARN")
    ExecutionRoleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-executionrolename""", alias="ExecutionRoleName")
    ManagedExecution_: Optional['ManagedExecution'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-managedexecution""", alias="ManagedExecution")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.StackSet:
        from troposphere.cloudformation import StackSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import StackSet as TropoT
        return resource_to_troposphere(self, TropoT)


class TypeActivation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html
    Properties:
        - Name: MajorVersion
        - Name: ExecutionRoleArn
        - Name: TypeName
        - Name: Type
        - Name: PublicTypeArn
        - Name: AutoUpdate
        - Name: LoggingConfig
        - Name: PublisherId
        - Name: VersionBump
        - Name: TypeNameAlias
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MajorVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-majorversion""", alias="MajorVersion")
    ExecutionRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-executionrolearn""", alias="ExecutionRoleArn")
    TypeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-typename""", alias="TypeName")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-type""", alias="Type")
    PublicTypeArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-publictypearn""", alias="PublicTypeArn")
    AutoUpdate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-autoupdate""", alias="AutoUpdate")
    LoggingConfig_: Optional['LoggingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-loggingconfig""", alias="LoggingConfig")
    PublisherId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-publisherid""", alias="PublisherId")
    VersionBump_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-versionbump""", alias="VersionBump")
    TypeNameAlias_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-typenamealias""", alias="TypeNameAlias")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.TypeActivation:
        from troposphere.cloudformation import TypeActivation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import TypeActivation as TropoT
        return resource_to_troposphere(self, TropoT)


class WaitCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html
    Properties:
        - Name: Count
        - Name: Handle
        - Name: Timeout
    Attributes:
        - Name: Data
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Count_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-count""", alias="Count")
    Handle_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-handle""", alias="Handle")
    Timeout_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-timeout""", alias="Timeout")
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.WaitCondition:
        from troposphere.cloudformation import WaitCondition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import WaitCondition as TropoT
        return resource_to_troposphere(self, TropoT)


class WaitConditionHandle(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitconditionhandle.html
    """
    
    pass
    

    @property
    def tropo_type(self) -> troposphere.cloudformation.WaitConditionHandle:
        from troposphere.cloudformation import WaitConditionHandle as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cloudformation import WaitConditionHandle as TropoT
        return resource_to_troposphere(self, TropoT)

