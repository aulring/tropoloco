from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ApplicationResourceLifecycleConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html
    Properties:
        - Name: ServiceRole
        - Name: VersionLifecycleConfig
    
    """
    
    ServiceRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-servicerole""", alias="ServiceRole")
    VersionLifecycleConfig_: Optional['ApplicationVersionLifecycleConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-versionlifecycleconfig""", alias="VersionLifecycleConfig")
    


    @property
    def tropo_type(self) -> troposphere.elasticbeanstalk.ApplicationResourceLifecycleConfig:
        from troposphere.elasticbeanstalk import ApplicationResourceLifecycleConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ApplicationVersionLifecycleConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html
    Properties:
        - Name: MaxCountRule
        - Name: MaxAgeRule
    
    """
    
    MaxCountRule_: Optional['MaxCountRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html#cfn-elasticbeanstalk-application-applicationversionlifecycleconfig-maxcountrule""", alias="MaxCountRule")
    MaxAgeRule_: Optional['MaxAgeRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html#cfn-elasticbeanstalk-application-applicationversionlifecycleconfig-maxagerule""", alias="MaxAgeRule")
    


    @property
    def tropo_type(self) -> troposphere.elasticbeanstalk.ApplicationVersionLifecycleConfig:
        from troposphere.elasticbeanstalk import ApplicationVersionLifecycleConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MaxAgeRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html
    Properties:
        - Name: DeleteSourceFromS3
        - Name: MaxAgeInDays
        - Name: Enabled
    
    """
    
    DeleteSourceFromS3_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-deletesourcefroms3""", alias="DeleteSourceFromS3")
    MaxAgeInDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-maxageindays""", alias="MaxAgeInDays")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.elasticbeanstalk.MaxAgeRule:
        from troposphere.elasticbeanstalk import MaxAgeRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MaxCountRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html
    Properties:
        - Name: DeleteSourceFromS3
        - Name: Enabled
        - Name: MaxCount
    
    """
    
    DeleteSourceFromS3_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-deletesourcefroms3""", alias="DeleteSourceFromS3")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-enabled""", alias="Enabled")
    MaxCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-maxcount""", alias="MaxCount")
    


    @property
    def tropo_type(self) -> troposphere.elasticbeanstalk.MaxCountRule:
        from troposphere.elasticbeanstalk import MaxCountRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceBundle(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-applicationversion-sourcebundle.html
    Properties:
        - Name: S3Bucket
        - Name: S3Key
    
    """
    
    S3Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-applicationversion-sourcebundle.html#cfn-elasticbeanstalk-applicationversion-sourcebundle-s3bucket""", alias="S3Bucket")
    S3Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-applicationversion-sourcebundle.html#cfn-elasticbeanstalk-applicationversion-sourcebundle-s3key""", alias="S3Key")
    


    @property
    def tropo_type(self) -> troposphere.elasticbeanstalk.SourceBundle:
        from troposphere.elasticbeanstalk import SourceBundle as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfigurationOptionSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html
    Properties:
        - Name: ResourceName
        - Name: Value
        - Name: Namespace
        - Name: OptionName
    
    """
    
    ResourceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-resourcename""", alias="ResourceName")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-value""", alias="Value")
    Namespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-namespace""", alias="Namespace")
    OptionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-optionname""", alias="OptionName")
    


    @property
    def tropo_type(self) -> troposphere.elasticbeanstalk.ConfigurationOptionSetting:
        from troposphere.elasticbeanstalk import ConfigurationOptionSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html
    Properties:
        - Name: ApplicationName
        - Name: TemplateName
    
    """
    
    ApplicationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-applicationname""", alias="ApplicationName")
    TemplateName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-templatename""", alias="TemplateName")
    


    @property
    def tropo_type(self) -> troposphere.elasticbeanstalk.SourceConfiguration:
        from troposphere.elasticbeanstalk import SourceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OptionSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-optionsetting.html
    Properties:
        - Name: ResourceName
        - Name: Value
        - Name: Namespace
        - Name: OptionName
    
    """
    
    ResourceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-optionsetting.html#cfn-elasticbeanstalk-environment-optionsetting-resourcename""", alias="ResourceName")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-optionsetting.html#cfn-elasticbeanstalk-environment-optionsetting-value""", alias="Value")
    Namespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-optionsetting.html#cfn-elasticbeanstalk-environment-optionsetting-namespace""", alias="Namespace")
    OptionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-optionsetting.html#cfn-elasticbeanstalk-environment-optionsetting-optionname""", alias="OptionName")
    


    @property
    def tropo_type(self) -> troposphere.elasticbeanstalk.OptionSetting:
        from troposphere.elasticbeanstalk import OptionSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-tier.html
    Properties:
        - Name: Type
        - Name: Version
        - Name: Name
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-tier.html#cfn-elasticbeanstalk-environment-tier-type""", alias="Type")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-tier.html#cfn-elasticbeanstalk-environment-tier-version""", alias="Version")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-environment-tier.html#cfn-elasticbeanstalk-environment-tier-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.elasticbeanstalk.Tier:
        from troposphere.elasticbeanstalk import Tier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Application(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-application.html
    Properties:
        - Name: ApplicationName
        - Name: Description
        - Name: ResourceLifecycleConfig
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApplicationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-application.html#cfn-elasticbeanstalk-application-applicationname""", alias="ApplicationName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-application.html#cfn-elasticbeanstalk-application-description""", alias="Description")
    ResourceLifecycleConfig_: Optional['ApplicationResourceLifecycleConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-application.html#cfn-elasticbeanstalk-application-resourcelifecycleconfig""", alias="ResourceLifecycleConfig")
    

    @property
    def tropo_type(self) -> troposphere.elasticbeanstalk.Application:
        from troposphere.elasticbeanstalk import Application as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticbeanstalk import Application as TropoT
        return resource_to_troposphere(self, TropoT)


class ApplicationVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-applicationversion.html
    Properties:
        - Name: ApplicationName
        - Name: Description
        - Name: SourceBundle
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApplicationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-applicationversion.html#cfn-elasticbeanstalk-applicationversion-applicationname""", alias="ApplicationName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-applicationversion.html#cfn-elasticbeanstalk-applicationversion-description""", alias="Description")
    SourceBundle_: 'SourceBundle' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-applicationversion.html#cfn-elasticbeanstalk-applicationversion-sourcebundle""", alias="SourceBundle")
    

    @property
    def tropo_type(self) -> troposphere.elasticbeanstalk.ApplicationVersion:
        from troposphere.elasticbeanstalk import ApplicationVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticbeanstalk import ApplicationVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class ConfigurationTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html
    Properties:
        - Name: EnvironmentId
        - Name: PlatformArn
        - Name: ApplicationName
        - Name: Description
        - Name: OptionSettings
        - Name: SourceConfiguration
        - Name: SolutionStackName
    Attributes:
        - Name: TemplateName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EnvironmentId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-environmentid""", alias="EnvironmentId")
    PlatformArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-platformarn""", alias="PlatformArn")
    ApplicationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-applicationname""", alias="ApplicationName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-description""", alias="Description")
    OptionSettings_: Optional[List['ConfigurationOptionSetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-optionsettings""", alias="OptionSettings")
    SourceConfiguration_: Optional['SourceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration""", alias="SourceConfiguration")
    SolutionStackName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-solutionstackname""", alias="SolutionStackName")
    

    @property
    def tropo_type(self) -> troposphere.elasticbeanstalk.ConfigurationTemplate:
        from troposphere.elasticbeanstalk import ConfigurationTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticbeanstalk import ConfigurationTemplate as TropoT
        return resource_to_troposphere(self, TropoT)


class Environment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html
    Properties:
        - Name: PlatformArn
        - Name: ApplicationName
        - Name: Description
        - Name: EnvironmentName
        - Name: OperationsRole
        - Name: Tier
        - Name: OptionSettings
        - Name: VersionLabel
        - Name: TemplateName
        - Name: SolutionStackName
        - Name: CNAMEPrefix
        - Name: Tags
    Attributes:
        - Name: EndpointURL
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PlatformArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-platformarn""", alias="PlatformArn")
    ApplicationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-applicationname""", alias="ApplicationName")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-description""", alias="Description")
    EnvironmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-environmentname""", alias="EnvironmentName")
    OperationsRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-operationsrole""", alias="OperationsRole")
    Tier_: Optional['Tier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-tier""", alias="Tier")
    OptionSettings_: Optional[List['OptionSetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-optionsettings""", alias="OptionSettings")
    VersionLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-versionlabel""", alias="VersionLabel")
    TemplateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-templatename""", alias="TemplateName")
    SolutionStackName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-solutionstackname""", alias="SolutionStackName")
    CNAMEPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-cnameprefix""", alias="CNAMEPrefix")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-environment.html#cfn-elasticbeanstalk-environment-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.elasticbeanstalk.Environment:
        from troposphere.elasticbeanstalk import Environment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.elasticbeanstalk import Environment as TropoT
        return resource_to_troposphere(self, TropoT)

