from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ComponentDependencyRequirement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentdependencyrequirement.html
    Properties:
        - Name: VersionRequirement
        - Name: DependencyType
    
    """
    
    VersionRequirement_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentdependencyrequirement.html#cfn-greengrassv2-componentversion-componentdependencyrequirement-versionrequirement""", alias="VersionRequirement")
    DependencyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentdependencyrequirement.html#cfn-greengrassv2-componentversion-componentdependencyrequirement-dependencytype""", alias="DependencyType")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.ComponentDependencyRequirement:
        from troposphere.greengrassv2 import ComponentDependencyRequirement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentPlatform(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentplatform.html
    Properties:
        - Name: Attributes
        - Name: Name
    
    """
    
    Attributes_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentplatform.html#cfn-greengrassv2-componentversion-componentplatform-attributes""", alias="Attributes")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentplatform.html#cfn-greengrassv2-componentversion-componentplatform-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.ComponentPlatform:
        from troposphere.greengrassv2 import ComponentPlatform as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaContainerParams(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html
    Properties:
        - Name: Volumes
        - Name: MountROSysfs
        - Name: MemorySizeInKB
        - Name: Devices
    
    """
    
    Volumes_: Optional[List['LambdaVolumeMount']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html#cfn-greengrassv2-componentversion-lambdacontainerparams-volumes""", alias="Volumes")
    MountROSysfs_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html#cfn-greengrassv2-componentversion-lambdacontainerparams-mountrosysfs""", alias="MountROSysfs")
    MemorySizeInKB_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html#cfn-greengrassv2-componentversion-lambdacontainerparams-memorysizeinkb""", alias="MemorySizeInKB")
    Devices_: Optional[List['LambdaDeviceMount']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html#cfn-greengrassv2-componentversion-lambdacontainerparams-devices""", alias="Devices")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.LambdaContainerParams:
        from troposphere.greengrassv2 import LambdaContainerParams as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaDeviceMount(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdadevicemount.html
    Properties:
        - Name: Path
        - Name: AddGroupOwner
        - Name: Permission
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdadevicemount.html#cfn-greengrassv2-componentversion-lambdadevicemount-path""", alias="Path")
    AddGroupOwner_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdadevicemount.html#cfn-greengrassv2-componentversion-lambdadevicemount-addgroupowner""", alias="AddGroupOwner")
    Permission_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdadevicemount.html#cfn-greengrassv2-componentversion-lambdadevicemount-permission""", alias="Permission")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.LambdaDeviceMount:
        from troposphere.greengrassv2 import LambdaDeviceMount as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaEventSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaeventsource.html
    Properties:
        - Name: Type
        - Name: Topic
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaeventsource.html#cfn-greengrassv2-componentversion-lambdaeventsource-type""", alias="Type")
    Topic_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaeventsource.html#cfn-greengrassv2-componentversion-lambdaeventsource-topic""", alias="Topic")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.LambdaEventSource:
        from troposphere.greengrassv2 import LambdaEventSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaExecutionParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html
    Properties:
        - Name: MaxInstancesCount
        - Name: TimeoutInSeconds
        - Name: EnvironmentVariables
        - Name: EventSources
        - Name: Pinned
        - Name: ExecArgs
        - Name: LinuxProcessParams
        - Name: InputPayloadEncodingType
        - Name: MaxQueueSize
        - Name: StatusTimeoutInSeconds
        - Name: MaxIdleTimeInSeconds
    
    """
    
    MaxInstancesCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-maxinstancescount""", alias="MaxInstancesCount")
    TimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-timeoutinseconds""", alias="TimeoutInSeconds")
    EnvironmentVariables_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-environmentvariables""", alias="EnvironmentVariables")
    EventSources_: Optional[List['LambdaEventSource']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-eventsources""", alias="EventSources")
    Pinned_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-pinned""", alias="Pinned")
    ExecArgs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-execargs""", alias="ExecArgs")
    LinuxProcessParams_: Optional['LambdaLinuxProcessParams'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-linuxprocessparams""", alias="LinuxProcessParams")
    InputPayloadEncodingType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-inputpayloadencodingtype""", alias="InputPayloadEncodingType")
    MaxQueueSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-maxqueuesize""", alias="MaxQueueSize")
    StatusTimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-statustimeoutinseconds""", alias="StatusTimeoutInSeconds")
    MaxIdleTimeInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html#cfn-greengrassv2-componentversion-lambdaexecutionparameters-maxidletimeinseconds""", alias="MaxIdleTimeInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.LambdaExecutionParameters:
        from troposphere.greengrassv2 import LambdaExecutionParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaFunctionRecipeSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html
    Properties:
        - Name: ComponentDependencies
        - Name: ComponentLambdaParameters
        - Name: LambdaArn
        - Name: ComponentPlatforms
        - Name: ComponentName
        - Name: ComponentVersion
    
    """
    
    ComponentDependencies_: Optional[Dict[str, 'ComponentDependencyRequirement']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentdependencies""", alias="ComponentDependencies")
    ComponentLambdaParameters_: Optional['LambdaExecutionParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentlambdaparameters""", alias="ComponentLambdaParameters")
    LambdaArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-lambdaarn""", alias="LambdaArn")
    ComponentPlatforms_: Optional[List['ComponentPlatform']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentplatforms""", alias="ComponentPlatforms")
    ComponentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentname""", alias="ComponentName")
    ComponentVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentversion""", alias="ComponentVersion")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.LambdaFunctionRecipeSource:
        from troposphere.greengrassv2 import LambdaFunctionRecipeSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaLinuxProcessParams(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdalinuxprocessparams.html
    Properties:
        - Name: IsolationMode
        - Name: ContainerParams
    
    """
    
    IsolationMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdalinuxprocessparams.html#cfn-greengrassv2-componentversion-lambdalinuxprocessparams-isolationmode""", alias="IsolationMode")
    ContainerParams_: Optional['LambdaContainerParams'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdalinuxprocessparams.html#cfn-greengrassv2-componentversion-lambdalinuxprocessparams-containerparams""", alias="ContainerParams")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.LambdaLinuxProcessParams:
        from troposphere.greengrassv2 import LambdaLinuxProcessParams as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaVolumeMount(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html
    Properties:
        - Name: SourcePath
        - Name: DestinationPath
        - Name: AddGroupOwner
        - Name: Permission
    
    """
    
    SourcePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html#cfn-greengrassv2-componentversion-lambdavolumemount-sourcepath""", alias="SourcePath")
    DestinationPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html#cfn-greengrassv2-componentversion-lambdavolumemount-destinationpath""", alias="DestinationPath")
    AddGroupOwner_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html#cfn-greengrassv2-componentversion-lambdavolumemount-addgroupowner""", alias="AddGroupOwner")
    Permission_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html#cfn-greengrassv2-componentversion-lambdavolumemount-permission""", alias="Permission")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.LambdaVolumeMount:
        from troposphere.greengrassv2 import LambdaVolumeMount as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentConfigurationUpdate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentconfigurationupdate.html
    Properties:
        - Name: Merge
        - Name: Reset
    
    """
    
    Merge_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentconfigurationupdate.html#cfn-greengrassv2-deployment-componentconfigurationupdate-merge""", alias="Merge")
    Reset_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentconfigurationupdate.html#cfn-greengrassv2-deployment-componentconfigurationupdate-reset""", alias="Reset")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.ComponentConfigurationUpdate:
        from troposphere.greengrassv2 import ComponentConfigurationUpdate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentDeploymentSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentdeploymentspecification.html
    Properties:
        - Name: RunWith
        - Name: ConfigurationUpdate
        - Name: ComponentVersion
    
    """
    
    RunWith_: Optional['ComponentRunWith'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentdeploymentspecification.html#cfn-greengrassv2-deployment-componentdeploymentspecification-runwith""", alias="RunWith")
    ConfigurationUpdate_: Optional['ComponentConfigurationUpdate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentdeploymentspecification.html#cfn-greengrassv2-deployment-componentdeploymentspecification-configurationupdate""", alias="ConfigurationUpdate")
    ComponentVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentdeploymentspecification.html#cfn-greengrassv2-deployment-componentdeploymentspecification-componentversion""", alias="ComponentVersion")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.ComponentDeploymentSpecification:
        from troposphere.greengrassv2 import ComponentDeploymentSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentRunWith(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentrunwith.html
    Properties:
        - Name: WindowsUser
        - Name: SystemResourceLimits
        - Name: PosixUser
    
    """
    
    WindowsUser_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentrunwith.html#cfn-greengrassv2-deployment-componentrunwith-windowsuser""", alias="WindowsUser")
    SystemResourceLimits_: Optional['SystemResourceLimits'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentrunwith.html#cfn-greengrassv2-deployment-componentrunwith-systemresourcelimits""", alias="SystemResourceLimits")
    PosixUser_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-componentrunwith.html#cfn-greengrassv2-deployment-componentrunwith-posixuser""", alias="PosixUser")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.ComponentRunWith:
        from troposphere.greengrassv2 import ComponentRunWith as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentComponentUpdatePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentcomponentupdatepolicy.html
    Properties:
        - Name: Action
        - Name: TimeoutInSeconds
    
    """
    
    Action_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentcomponentupdatepolicy.html#cfn-greengrassv2-deployment-deploymentcomponentupdatepolicy-action""", alias="Action")
    TimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentcomponentupdatepolicy.html#cfn-greengrassv2-deployment-deploymentcomponentupdatepolicy-timeoutinseconds""", alias="TimeoutInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.DeploymentComponentUpdatePolicy:
        from troposphere.greengrassv2 import DeploymentComponentUpdatePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentConfigurationValidationPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentconfigurationvalidationpolicy.html
    Properties:
        - Name: TimeoutInSeconds
    
    """
    
    TimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentconfigurationvalidationpolicy.html#cfn-greengrassv2-deployment-deploymentconfigurationvalidationpolicy-timeoutinseconds""", alias="TimeoutInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.DeploymentConfigurationValidationPolicy:
        from troposphere.greengrassv2 import DeploymentConfigurationValidationPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentIoTJobConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration.html
    Properties:
        - Name: JobExecutionsRolloutConfig
        - Name: TimeoutConfig
        - Name: AbortConfig
    
    """
    
    JobExecutionsRolloutConfig_: Optional['IoTJobExecutionsRolloutConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration.html#cfn-greengrassv2-deployment-deploymentiotjobconfiguration-jobexecutionsrolloutconfig""", alias="JobExecutionsRolloutConfig")
    TimeoutConfig_: Optional['IoTJobTimeoutConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration.html#cfn-greengrassv2-deployment-deploymentiotjobconfiguration-timeoutconfig""", alias="TimeoutConfig")
    AbortConfig_: Optional['IoTJobAbortConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration.html#cfn-greengrassv2-deployment-deploymentiotjobconfiguration-abortconfig""", alias="AbortConfig")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.DeploymentIoTJobConfiguration:
        from troposphere.greengrassv2 import DeploymentIoTJobConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeploymentPolicies(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentpolicies.html
    Properties:
        - Name: ComponentUpdatePolicy
        - Name: ConfigurationValidationPolicy
        - Name: FailureHandlingPolicy
    
    """
    
    ComponentUpdatePolicy_: Optional['DeploymentComponentUpdatePolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentpolicies.html#cfn-greengrassv2-deployment-deploymentpolicies-componentupdatepolicy""", alias="ComponentUpdatePolicy")
    ConfigurationValidationPolicy_: Optional['DeploymentConfigurationValidationPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentpolicies.html#cfn-greengrassv2-deployment-deploymentpolicies-configurationvalidationpolicy""", alias="ConfigurationValidationPolicy")
    FailureHandlingPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-deploymentpolicies.html#cfn-greengrassv2-deployment-deploymentpolicies-failurehandlingpolicy""", alias="FailureHandlingPolicy")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.DeploymentPolicies:
        from troposphere.greengrassv2 import DeploymentPolicies as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IoTJobAbortConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortconfig.html
    Properties:
        - Name: CriteriaList
    
    """
    
    CriteriaList_: List['IoTJobAbortCriteria'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortconfig.html#cfn-greengrassv2-deployment-iotjobabortconfig-criterialist""", alias="CriteriaList")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.IoTJobAbortConfig:
        from troposphere.greengrassv2 import IoTJobAbortConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IoTJobAbortCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortcriteria.html
    Properties:
        - Name: FailureType
        - Name: Action
        - Name: ThresholdPercentage
        - Name: MinNumberOfExecutedThings
    
    """
    
    FailureType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortcriteria.html#cfn-greengrassv2-deployment-iotjobabortcriteria-failuretype""", alias="FailureType")
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortcriteria.html#cfn-greengrassv2-deployment-iotjobabortcriteria-action""", alias="Action")
    ThresholdPercentage_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortcriteria.html#cfn-greengrassv2-deployment-iotjobabortcriteria-thresholdpercentage""", alias="ThresholdPercentage")
    MinNumberOfExecutedThings_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobabortcriteria.html#cfn-greengrassv2-deployment-iotjobabortcriteria-minnumberofexecutedthings""", alias="MinNumberOfExecutedThings")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.IoTJobAbortCriteria:
        from troposphere.greengrassv2 import IoTJobAbortCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IoTJobExecutionsRolloutConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexecutionsrolloutconfig.html
    Properties:
        - Name: MaximumPerMinute
        - Name: ExponentialRate
    
    """
    
    MaximumPerMinute_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexecutionsrolloutconfig.html#cfn-greengrassv2-deployment-iotjobexecutionsrolloutconfig-maximumperminute""", alias="MaximumPerMinute")
    ExponentialRate_: Optional['IoTJobExponentialRolloutRate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexecutionsrolloutconfig.html#cfn-greengrassv2-deployment-iotjobexecutionsrolloutconfig-exponentialrate""", alias="ExponentialRate")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.IoTJobExecutionsRolloutConfig:
        from troposphere.greengrassv2 import IoTJobExecutionsRolloutConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IoTJobExponentialRolloutRate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate.html
    Properties:
        - Name: RateIncreaseCriteria
        - Name: BaseRatePerMinute
        - Name: IncrementFactor
    
    """
    
    RateIncreaseCriteria_: 'IoTJobRateIncreaseCriteria' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate.html#cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-rateincreasecriteria""", alias="RateIncreaseCriteria")
    BaseRatePerMinute_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate.html#cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-baserateperminute""", alias="BaseRatePerMinute")
    IncrementFactor_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate.html#cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-incrementfactor""", alias="IncrementFactor")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.IoTJobExponentialRolloutRate:
        from troposphere.greengrassv2 import IoTJobExponentialRolloutRate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IoTJobRateIncreaseCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobrateincreasecriteria.html
    Properties:
        - Name: NumberOfSucceededThings
        - Name: NumberOfNotifiedThings
    
    """
    
    NumberOfSucceededThings_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobrateincreasecriteria.html#cfn-greengrassv2-deployment-iotjobrateincreasecriteria-numberofsucceededthings""", alias="NumberOfSucceededThings")
    NumberOfNotifiedThings_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobrateincreasecriteria.html#cfn-greengrassv2-deployment-iotjobrateincreasecriteria-numberofnotifiedthings""", alias="NumberOfNotifiedThings")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.IoTJobRateIncreaseCriteria:
        from troposphere.greengrassv2 import IoTJobRateIncreaseCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IoTJobTimeoutConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobtimeoutconfig.html
    Properties:
        - Name: InProgressTimeoutInMinutes
    
    """
    
    InProgressTimeoutInMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-iotjobtimeoutconfig.html#cfn-greengrassv2-deployment-iotjobtimeoutconfig-inprogresstimeoutinminutes""", alias="InProgressTimeoutInMinutes")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.IoTJobTimeoutConfig:
        from troposphere.greengrassv2 import IoTJobTimeoutConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SystemResourceLimits(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-systemresourcelimits.html
    Properties:
        - Name: Memory
        - Name: Cpus
    
    """
    
    Memory_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-systemresourcelimits.html#cfn-greengrassv2-deployment-systemresourcelimits-memory""", alias="Memory")
    Cpus_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-deployment-systemresourcelimits.html#cfn-greengrassv2-deployment-systemresourcelimits-cpus""", alias="Cpus")
    


    @property
    def tropo_type(self) -> troposphere.greengrassv2.SystemResourceLimits:
        from troposphere.greengrassv2 import SystemResourceLimits as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ComponentVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html
    Properties:
        - Name: LambdaFunction
        - Name: InlineRecipe
        - Name: Tags
    Attributes:
        - Name: ComponentName
        - Name: Arn
        - Name: ComponentVersion
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    LambdaFunction_: Optional['LambdaFunctionRecipeSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html#cfn-greengrassv2-componentversion-lambdafunction""", alias="LambdaFunction")
    InlineRecipe_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html#cfn-greengrassv2-componentversion-inlinerecipe""", alias="InlineRecipe")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html#cfn-greengrassv2-componentversion-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.greengrassv2.ComponentVersion:
        from troposphere.greengrassv2 import ComponentVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrassv2 import ComponentVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class Deployment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html
    Properties:
        - Name: Components
        - Name: DeploymentName
        - Name: IotJobConfiguration
        - Name: DeploymentPolicies
        - Name: TargetArn
        - Name: ParentTargetArn
        - Name: Tags
    Attributes:
        - Name: DeploymentId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Components_: Optional[Dict[str, 'ComponentDeploymentSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-components""", alias="Components")
    DeploymentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-deploymentname""", alias="DeploymentName")
    IotJobConfiguration_: Optional['DeploymentIoTJobConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-iotjobconfiguration""", alias="IotJobConfiguration")
    DeploymentPolicies_: Optional['DeploymentPolicies'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-deploymentpolicies""", alias="DeploymentPolicies")
    TargetArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-targetarn""", alias="TargetArn")
    ParentTargetArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-parenttargetarn""", alias="ParentTargetArn")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-deployment.html#cfn-greengrassv2-deployment-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.greengrassv2.Deployment:
        from troposphere.greengrassv2 import Deployment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.greengrassv2 import Deployment as TropoT
        return resource_to_troposphere(self, TropoT)

