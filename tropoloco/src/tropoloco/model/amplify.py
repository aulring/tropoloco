from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AutoBranchCreationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html
    Properties:
        - Name: EnvironmentVariables
        - Name: AutoBranchCreationPatterns
        - Name: EnableAutoBranchCreation
        - Name: PullRequestEnvironmentName
        - Name: EnablePullRequestPreview
        - Name: EnableAutoBuild
        - Name: EnablePerformanceMode
        - Name: BuildSpec
        - Name: Stage
        - Name: BasicAuthConfig
        - Name: Framework
    
    """
    
    EnvironmentVariables_: Optional[List['EnvironmentVariable']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-environmentvariables""", alias="EnvironmentVariables")
    AutoBranchCreationPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-autobranchcreationpatterns""", alias="AutoBranchCreationPatterns")
    EnableAutoBranchCreation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableautobranchcreation""", alias="EnableAutoBranchCreation")
    PullRequestEnvironmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-pullrequestenvironmentname""", alias="PullRequestEnvironmentName")
    EnablePullRequestPreview_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enablepullrequestpreview""", alias="EnablePullRequestPreview")
    EnableAutoBuild_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableautobuild""", alias="EnableAutoBuild")
    EnablePerformanceMode_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableperformancemode""", alias="EnablePerformanceMode")
    BuildSpec_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-buildspec""", alias="BuildSpec")
    Stage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-stage""", alias="Stage")
    BasicAuthConfig_: Optional['BasicAuthConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-basicauthconfig""", alias="BasicAuthConfig")
    Framework_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-framework""", alias="Framework")
    


    @property
    def tropo_type(self) -> troposphere.amplify.AutoBranchCreationConfig:
        from troposphere.amplify import AutoBranchCreationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BasicAuthConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html
    Properties:
        - Name: Username
        - Name: EnableBasicAuth
        - Name: Password
    
    """
    
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-username""", alias="Username")
    EnableBasicAuth_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-enablebasicauth""", alias="EnableBasicAuth")
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.amplify.BasicAuthConfig:
        from troposphere.amplify import BasicAuthConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html
    Properties:
        - Name: Condition
        - Name: Status
        - Name: Target
        - Name: Source
    
    """
    
    Condition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-condition""", alias="Condition")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-status""", alias="Status")
    Target_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-target""", alias="Target")
    Source_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-source""", alias="Source")
    


    @property
    def tropo_type(self) -> troposphere.amplify.CustomRule:
        from troposphere.amplify import CustomRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnvironmentVariable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html#cfn-amplify-app-environmentvariable-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html#cfn-amplify-app-environmentvariable-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.amplify.EnvironmentVariable:
        from troposphere.amplify import EnvironmentVariable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Backend(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-backend.html
    Properties:
        - Name: StackArn
    
    """
    
    StackArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-backend.html#cfn-amplify-branch-backend-stackarn""", alias="StackArn")
    


    @property
    def tropo_type(self) -> troposphere.amplify.Backend:
        from troposphere.amplify import Backend as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BasicAuthConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html
    Properties:
        - Name: Username
        - Name: EnableBasicAuth
        - Name: Password
    
    """
    
    Username_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-username""", alias="Username")
    EnableBasicAuth_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-enablebasicauth""", alias="EnableBasicAuth")
    Password_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-password""", alias="Password")
    


    @property
    def tropo_type(self) -> troposphere.amplify.BasicAuthConfig:
        from troposphere.amplify import BasicAuthConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnvironmentVariable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html#cfn-amplify-branch-environmentvariable-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html#cfn-amplify-branch-environmentvariable-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.amplify.EnvironmentVariable:
        from troposphere.amplify import EnvironmentVariable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SubDomainSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html
    Properties:
        - Name: Prefix
        - Name: BranchName
    
    """
    
    Prefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html#cfn-amplify-domain-subdomainsetting-prefix""", alias="Prefix")
    BranchName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html#cfn-amplify-domain-subdomainsetting-branchname""", alias="BranchName")
    


    @property
    def tropo_type(self) -> troposphere.amplify.SubDomainSetting:
        from troposphere.amplify import SubDomainSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class App(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html
    Properties:
        - Name: AutoBranchCreationConfig
        - Name: OauthToken
        - Name: Description
        - Name: Platform
        - Name: EnableBranchAutoDeletion
        - Name: Name
        - Name: Repository
        - Name: EnvironmentVariables
        - Name: AccessToken
        - Name: BuildSpec
        - Name: CustomRules
        - Name: BasicAuthConfig
        - Name: CustomHeaders
        - Name: Tags
        - Name: IAMServiceRole
    Attributes:
        - Name: AppId
        - Name: Arn
        - Name: DefaultDomain
        - Name: AppName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AutoBranchCreationConfig_: Optional['AutoBranchCreationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-autobranchcreationconfig""", alias="AutoBranchCreationConfig")
    OauthToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-oauthtoken""", alias="OauthToken")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-description""", alias="Description")
    Platform_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-platform""", alias="Platform")
    EnableBranchAutoDeletion_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-enablebranchautodeletion""", alias="EnableBranchAutoDeletion")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-name""", alias="Name")
    Repository_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-repository""", alias="Repository")
    EnvironmentVariables_: Optional[List['EnvironmentVariable']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-environmentvariables""", alias="EnvironmentVariables")
    AccessToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-accesstoken""", alias="AccessToken")
    BuildSpec_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-buildspec""", alias="BuildSpec")
    CustomRules_: Optional[List['CustomRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-customrules""", alias="CustomRules")
    BasicAuthConfig_: Optional['BasicAuthConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-basicauthconfig""", alias="BasicAuthConfig")
    CustomHeaders_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-customheaders""", alias="CustomHeaders")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-tags""", alias="Tags")
    IAMServiceRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-iamservicerole""", alias="IAMServiceRole")
    

    @property
    def tropo_type(self) -> troposphere.amplify.App:
        from troposphere.amplify import App as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.amplify import App as TropoT
        return resource_to_troposphere(self, TropoT)


class Branch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html
    Properties:
        - Name: Description
        - Name: EnablePerformanceMode
        - Name: Backend
        - Name: EnvironmentVariables
        - Name: AppId
        - Name: PullRequestEnvironmentName
        - Name: EnablePullRequestPreview
        - Name: EnableAutoBuild
        - Name: BuildSpec
        - Name: Stage
        - Name: BranchName
        - Name: BasicAuthConfig
        - Name: Framework
        - Name: Tags
    Attributes:
        - Name: BranchName
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-description""", alias="Description")
    EnablePerformanceMode_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enableperformancemode""", alias="EnablePerformanceMode")
    Backend_: Optional['Backend'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-backend""", alias="Backend")
    EnvironmentVariables_: Optional[List['EnvironmentVariable']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-environmentvariables""", alias="EnvironmentVariables")
    AppId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-appid""", alias="AppId")
    PullRequestEnvironmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-pullrequestenvironmentname""", alias="PullRequestEnvironmentName")
    EnablePullRequestPreview_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enablepullrequestpreview""", alias="EnablePullRequestPreview")
    EnableAutoBuild_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enableautobuild""", alias="EnableAutoBuild")
    BuildSpec_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-buildspec""", alias="BuildSpec")
    Stage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-stage""", alias="Stage")
    BranchName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-branchname""", alias="BranchName")
    BasicAuthConfig_: Optional['BasicAuthConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-basicauthconfig""", alias="BasicAuthConfig")
    Framework_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-framework""", alias="Framework")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.amplify.Branch:
        from troposphere.amplify import Branch as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.amplify import Branch as TropoT
        return resource_to_troposphere(self, TropoT)


class Domain(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html
    Properties:
        - Name: SubDomainSettings
        - Name: AppId
        - Name: AutoSubDomainIAMRole
        - Name: DomainName
        - Name: EnableAutoSubDomain
        - Name: AutoSubDomainCreationPatterns
    Attributes:
        - Name: AutoSubDomainIAMRole
        - Name: DomainName
        - Name: EnableAutoSubDomain
        - Name: StatusReason
        - Name: Arn
        - Name: AutoSubDomainCreationPatterns
        - Name: DomainStatus
        - Name: CertificateRecord
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SubDomainSettings_: List['SubDomainSetting'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-subdomainsettings""", alias="SubDomainSettings")
    AppId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-appid""", alias="AppId")
    AutoSubDomainIAMRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-autosubdomainiamrole""", alias="AutoSubDomainIAMRole")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-domainname""", alias="DomainName")
    EnableAutoSubDomain_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-enableautosubdomain""", alias="EnableAutoSubDomain")
    AutoSubDomainCreationPatterns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-autosubdomaincreationpatterns""", alias="AutoSubDomainCreationPatterns")
    

    @property
    def tropo_type(self) -> troposphere.amplify.Domain:
        from troposphere.amplify import Domain as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.amplify import Domain as TropoT
        return resource_to_troposphere(self, TropoT)

