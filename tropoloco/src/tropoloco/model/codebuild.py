from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Artifacts(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html
    Properties:
        - Name: Path
        - Name: Type
        - Name: ArtifactIdentifier
        - Name: OverrideArtifactName
        - Name: Packaging
        - Name: EncryptionDisabled
        - Name: Location
        - Name: Name
        - Name: NamespaceType
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-path""", alias="Path")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-type""", alias="Type")
    ArtifactIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-artifactidentifier""", alias="ArtifactIdentifier")
    OverrideArtifactName_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-overrideartifactname""", alias="OverrideArtifactName")
    Packaging_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-packaging""", alias="Packaging")
    EncryptionDisabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-encryptiondisabled""", alias="EncryptionDisabled")
    Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-location""", alias="Location")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-name""", alias="Name")
    NamespaceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-namespacetype""", alias="NamespaceType")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.Artifacts:
        from troposphere.codebuild import Artifacts as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BatchRestrictions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-batchrestrictions.html
    Properties:
        - Name: ComputeTypesAllowed
        - Name: MaximumBuildsAllowed
    
    """
    
    ComputeTypesAllowed_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-batchrestrictions.html#cfn-codebuild-project-batchrestrictions-computetypesallowed""", alias="ComputeTypesAllowed")
    MaximumBuildsAllowed_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-batchrestrictions.html#cfn-codebuild-project-batchrestrictions-maximumbuildsallowed""", alias="MaximumBuildsAllowed")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.BatchRestrictions:
        from troposphere.codebuild import BatchRestrictions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BuildStatusConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-buildstatusconfig.html
    Properties:
        - Name: Context
        - Name: TargetUrl
    
    """
    
    Context_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-buildstatusconfig.html#cfn-codebuild-project-buildstatusconfig-context""", alias="Context")
    TargetUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-buildstatusconfig.html#cfn-codebuild-project-buildstatusconfig-targeturl""", alias="TargetUrl")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.BuildStatusConfig:
        from troposphere.codebuild import BuildStatusConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchLogsConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html
    Properties:
        - Name: Status
        - Name: GroupName
        - Name: StreamName
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html#cfn-codebuild-project-cloudwatchlogsconfig-status""", alias="Status")
    GroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html#cfn-codebuild-project-cloudwatchlogsconfig-groupname""", alias="GroupName")
    StreamName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html#cfn-codebuild-project-cloudwatchlogsconfig-streamname""", alias="StreamName")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.CloudWatchLogsConfig:
        from troposphere.codebuild import CloudWatchLogsConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Environment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html
    Properties:
        - Name: Type
        - Name: EnvironmentVariables
        - Name: PrivilegedMode
        - Name: ImagePullCredentialsType
        - Name: Image
        - Name: RegistryCredential
        - Name: ComputeType
        - Name: Certificate
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-type""", alias="Type")
    EnvironmentVariables_: Optional[List['EnvironmentVariable']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-environmentvariables""", alias="EnvironmentVariables")
    PrivilegedMode_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-privilegedmode""", alias="PrivilegedMode")
    ImagePullCredentialsType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-imagepullcredentialstype""", alias="ImagePullCredentialsType")
    Image_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-image""", alias="Image")
    RegistryCredential_: Optional['RegistryCredential'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-registrycredential""", alias="RegistryCredential")
    ComputeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-computetype""", alias="ComputeType")
    Certificate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-certificate""", alias="Certificate")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.Environment:
        from troposphere.codebuild import Environment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnvironmentVariable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html
    Properties:
        - Name: Type
        - Name: Value
        - Name: Name
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html#cfn-codebuild-project-environmentvariable-type""", alias="Type")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html#cfn-codebuild-project-environmentvariable-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html#cfn-codebuild-project-environmentvariable-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.EnvironmentVariable:
        from troposphere.codebuild import EnvironmentVariable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FilterGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-filtergroup.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.codebuild.FilterGroup:
        from troposphere.codebuild import FilterGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GitSubmodulesConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-gitsubmodulesconfig.html
    Properties:
        - Name: FetchSubmodules
    
    """
    
    FetchSubmodules_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-gitsubmodulesconfig.html#cfn-codebuild-project-gitsubmodulesconfig-fetchsubmodules""", alias="FetchSubmodules")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.GitSubmodulesConfig:
        from troposphere.codebuild import GitSubmodulesConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogsConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-logsconfig.html
    Properties:
        - Name: CloudWatchLogs
        - Name: S3Logs
    
    """
    
    CloudWatchLogs_: Optional['CloudWatchLogsConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-logsconfig.html#cfn-codebuild-project-logsconfig-cloudwatchlogs""", alias="CloudWatchLogs")
    S3Logs_: Optional['S3LogsConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-logsconfig.html#cfn-codebuild-project-logsconfig-s3logs""", alias="S3Logs")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.LogsConfig:
        from troposphere.codebuild import LogsConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProjectBuildBatchConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html
    Properties:
        - Name: CombineArtifacts
        - Name: ServiceRole
        - Name: BatchReportMode
        - Name: TimeoutInMins
        - Name: Restrictions
    
    """
    
    CombineArtifacts_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-combineartifacts""", alias="CombineArtifacts")
    ServiceRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-servicerole""", alias="ServiceRole")
    BatchReportMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-batchreportmode""", alias="BatchReportMode")
    TimeoutInMins_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-timeoutinmins""", alias="TimeoutInMins")
    Restrictions_: Optional['BatchRestrictions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-restrictions""", alias="Restrictions")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.ProjectBuildBatchConfig:
        from troposphere.codebuild import ProjectBuildBatchConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProjectCache(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html
    Properties:
        - Name: Modes
        - Name: Type
        - Name: Location
    
    """
    
    Modes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html#cfn-codebuild-project-projectcache-modes""", alias="Modes")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html#cfn-codebuild-project-projectcache-type""", alias="Type")
    Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html#cfn-codebuild-project-projectcache-location""", alias="Location")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.ProjectCache:
        from troposphere.codebuild import ProjectCache as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProjectFileSystemLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html
    Properties:
        - Name: MountPoint
        - Name: Type
        - Name: Identifier
        - Name: MountOptions
        - Name: Location
    
    """
    
    MountPoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-mountpoint""", alias="MountPoint")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-type""", alias="Type")
    Identifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-identifier""", alias="Identifier")
    MountOptions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-mountoptions""", alias="MountOptions")
    Location_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-location""", alias="Location")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.ProjectFileSystemLocation:
        from troposphere.codebuild import ProjectFileSystemLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProjectFleet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfleet.html
    Properties:
        - Name: FleetArn
    
    """
    
    FleetArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfleet.html#cfn-codebuild-project-projectfleet-fleetarn""", alias="FleetArn")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.ProjectFleet:
        from troposphere.codebuild import ProjectFleet as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProjectSourceVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectsourceversion.html
    Properties:
        - Name: SourceIdentifier
        - Name: SourceVersion
    
    """
    
    SourceIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectsourceversion.html#cfn-codebuild-project-projectsourceversion-sourceidentifier""", alias="SourceIdentifier")
    SourceVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectsourceversion.html#cfn-codebuild-project-projectsourceversion-sourceversion""", alias="SourceVersion")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.ProjectSourceVersion:
        from troposphere.codebuild import ProjectSourceVersion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProjectTriggers(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html
    Properties:
        - Name: FilterGroups
        - Name: BuildType
        - Name: Webhook
    
    """
    
    FilterGroups_: Optional[List['FilterGroup']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html#cfn-codebuild-project-projecttriggers-filtergroups""", alias="FilterGroups")
    BuildType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html#cfn-codebuild-project-projecttriggers-buildtype""", alias="BuildType")
    Webhook_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html#cfn-codebuild-project-projecttriggers-webhook""", alias="Webhook")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.ProjectTriggers:
        from troposphere.codebuild import ProjectTriggers as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RegistryCredential(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-registrycredential.html
    Properties:
        - Name: Credential
        - Name: CredentialProvider
    
    """
    
    Credential_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-registrycredential.html#cfn-codebuild-project-registrycredential-credential""", alias="Credential")
    CredentialProvider_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-registrycredential.html#cfn-codebuild-project-registrycredential-credentialprovider""", alias="CredentialProvider")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.RegistryCredential:
        from troposphere.codebuild import RegistryCredential as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3LogsConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html
    Properties:
        - Name: Status
        - Name: EncryptionDisabled
        - Name: Location
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html#cfn-codebuild-project-s3logsconfig-status""", alias="Status")
    EncryptionDisabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html#cfn-codebuild-project-s3logsconfig-encryptiondisabled""", alias="EncryptionDisabled")
    Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html#cfn-codebuild-project-s3logsconfig-location""", alias="Location")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.S3LogsConfig:
        from troposphere.codebuild import S3LogsConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Source(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html
    Properties:
        - Name: Type
        - Name: ReportBuildStatus
        - Name: Auth
        - Name: SourceIdentifier
        - Name: BuildSpec
        - Name: GitCloneDepth
        - Name: BuildStatusConfig
        - Name: GitSubmodulesConfig
        - Name: InsecureSsl
        - Name: Location
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-type""", alias="Type")
    ReportBuildStatus_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-reportbuildstatus""", alias="ReportBuildStatus")
    Auth_: Optional['SourceAuth'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-auth""", alias="Auth")
    SourceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-sourceidentifier""", alias="SourceIdentifier")
    BuildSpec_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-buildspec""", alias="BuildSpec")
    GitCloneDepth_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-gitclonedepth""", alias="GitCloneDepth")
    BuildStatusConfig_: Optional['BuildStatusConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-buildstatusconfig""", alias="BuildStatusConfig")
    GitSubmodulesConfig_: Optional['GitSubmodulesConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-gitsubmodulesconfig""", alias="GitSubmodulesConfig")
    InsecureSsl_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-insecuressl""", alias="InsecureSsl")
    Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-location""", alias="Location")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.Source:
        from troposphere.codebuild import Source as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceAuth(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-sourceauth.html
    Properties:
        - Name: Type
        - Name: Resource
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-sourceauth.html#cfn-codebuild-project-sourceauth-type""", alias="Type")
    Resource_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-sourceauth.html#cfn-codebuild-project-sourceauth-resource""", alias="Resource")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.SourceAuth:
        from troposphere.codebuild import SourceAuth as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html
    Properties:
        - Name: Subnets
        - Name: VpcId
        - Name: SecurityGroupIds
    
    """
    
    Subnets_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html#cfn-codebuild-project-vpcconfig-subnets""", alias="Subnets")
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html#cfn-codebuild-project-vpcconfig-vpcid""", alias="VpcId")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html#cfn-codebuild-project-vpcconfig-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.VpcConfig:
        from troposphere.codebuild import VpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WebhookFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html
    Properties:
        - Name: Pattern
        - Name: Type
        - Name: ExcludeMatchedPattern
    
    """
    
    Pattern_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html#cfn-codebuild-project-webhookfilter-pattern""", alias="Pattern")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html#cfn-codebuild-project-webhookfilter-type""", alias="Type")
    ExcludeMatchedPattern_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html#cfn-codebuild-project-webhookfilter-excludematchedpattern""", alias="ExcludeMatchedPattern")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.WebhookFilter:
        from troposphere.codebuild import WebhookFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReportExportConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html
    Properties:
        - Name: S3Destination
        - Name: ExportConfigType
    
    """
    
    S3Destination_: Optional['S3ReportExportConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html#cfn-codebuild-reportgroup-reportexportconfig-s3destination""", alias="S3Destination")
    ExportConfigType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html#cfn-codebuild-reportgroup-reportexportconfig-exportconfigtype""", alias="ExportConfigType")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.ReportExportConfig:
        from troposphere.codebuild import ReportExportConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3ReportExportConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html
    Properties:
        - Name: Path
        - Name: Bucket
        - Name: Packaging
        - Name: EncryptionKey
        - Name: BucketOwner
        - Name: EncryptionDisabled
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-path""", alias="Path")
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-bucket""", alias="Bucket")
    Packaging_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-packaging""", alias="Packaging")
    EncryptionKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-encryptionkey""", alias="EncryptionKey")
    BucketOwner_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-bucketowner""", alias="BucketOwner")
    EncryptionDisabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-encryptiondisabled""", alias="EncryptionDisabled")
    


    @property
    def tropo_type(self) -> troposphere.codebuild.S3ReportExportConfig:
        from troposphere.codebuild import S3ReportExportConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Project(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html
    Properties:
        - Name: Description
        - Name: ResourceAccessRole
        - Name: VpcConfig
        - Name: SecondarySources
        - Name: EncryptionKey
        - Name: SourceVersion
        - Name: Triggers
        - Name: SecondaryArtifacts
        - Name: Source
        - Name: Name
        - Name: Artifacts
        - Name: BadgeEnabled
        - Name: LogsConfig
        - Name: ServiceRole
        - Name: QueuedTimeoutInMinutes
        - Name: FileSystemLocations
        - Name: Environment
        - Name: SecondarySourceVersions
        - Name: ConcurrentBuildLimit
        - Name: Visibility
        - Name: BuildBatchConfig
        - Name: Tags
        - Name: TimeoutInMinutes
        - Name: Cache
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-description""", alias="Description")
    ResourceAccessRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-resourceaccessrole""", alias="ResourceAccessRole")
    VpcConfig_: Optional['VpcConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-vpcconfig""", alias="VpcConfig")
    SecondarySources_: Optional[List['Source']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-secondarysources""", alias="SecondarySources")
    EncryptionKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-encryptionkey""", alias="EncryptionKey")
    SourceVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-sourceversion""", alias="SourceVersion")
    Triggers_: Optional['ProjectTriggers'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-triggers""", alias="Triggers")
    SecondaryArtifacts_: Optional[List['Artifacts']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-secondaryartifacts""", alias="SecondaryArtifacts")
    Source_: 'Source' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-source""", alias="Source")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-name""", alias="Name")
    Artifacts_: 'Artifacts' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-artifacts""", alias="Artifacts")
    BadgeEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-badgeenabled""", alias="BadgeEnabled")
    LogsConfig_: Optional['LogsConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-logsconfig""", alias="LogsConfig")
    ServiceRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-servicerole""", alias="ServiceRole")
    QueuedTimeoutInMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-queuedtimeoutinminutes""", alias="QueuedTimeoutInMinutes")
    FileSystemLocations_: Optional[List['ProjectFileSystemLocation']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-filesystemlocations""", alias="FileSystemLocations")
    Environment_: 'Environment' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-environment""", alias="Environment")
    SecondarySourceVersions_: Optional[List['ProjectSourceVersion']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-secondarysourceversions""", alias="SecondarySourceVersions")
    ConcurrentBuildLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-concurrentbuildlimit""", alias="ConcurrentBuildLimit")
    Visibility_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-visibility""", alias="Visibility")
    BuildBatchConfig_: Optional['ProjectBuildBatchConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-buildbatchconfig""", alias="BuildBatchConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-tags""", alias="Tags")
    TimeoutInMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-timeoutinminutes""", alias="TimeoutInMinutes")
    Cache_: Optional['ProjectCache'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-cache""", alias="Cache")
    

    @property
    def tropo_type(self) -> troposphere.codebuild.Project:
        from troposphere.codebuild import Project as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codebuild import Project as TropoT
        return resource_to_troposphere(self, TropoT)


class ReportGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html
    Properties:
        - Name: Type
        - Name: ExportConfig
        - Name: DeleteReports
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-type""", alias="Type")
    ExportConfig_: 'ReportExportConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-exportconfig""", alias="ExportConfig")
    DeleteReports_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-deletereports""", alias="DeleteReports")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.codebuild.ReportGroup:
        from troposphere.codebuild import ReportGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codebuild import ReportGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class SourceCredential(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html
    Properties:
        - Name: ServerType
        - Name: Username
        - Name: Token
        - Name: AuthType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ServerType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html#cfn-codebuild-sourcecredential-servertype""", alias="ServerType")
    Username_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html#cfn-codebuild-sourcecredential-username""", alias="Username")
    Token_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html#cfn-codebuild-sourcecredential-token""", alias="Token")
    AuthType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html#cfn-codebuild-sourcecredential-authtype""", alias="AuthType")
    

    @property
    def tropo_type(self) -> troposphere.codebuild.SourceCredential:
        from troposphere.codebuild import SourceCredential as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.codebuild import SourceCredential as TropoT
        return resource_to_troposphere(self, TropoT)

