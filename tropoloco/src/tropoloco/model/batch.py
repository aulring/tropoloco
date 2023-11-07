from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ComputeResources(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html
    Properties:
        - Name: SpotIamFleetRole
        - Name: MaxvCpus
        - Name: Ec2Configuration
        - Name: BidPercentage
        - Name: SecurityGroupIds
        - Name: AllocationStrategy
        - Name: Subnets
        - Name: Type
        - Name: MinvCpus
        - Name: UpdateToLatestImageVersion
        - Name: LaunchTemplate
        - Name: ImageId
        - Name: InstanceRole
        - Name: InstanceTypes
        - Name: Ec2KeyPair
        - Name: PlacementGroup
        - Name: Tags
        - Name: DesiredvCpus
    
    """
    
    SpotIamFleetRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-spotiamfleetrole""", alias="SpotIamFleetRole")
    MaxvCpus_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-maxvcpus""", alias="MaxvCpus")
    Ec2Configuration_: Optional[List['Ec2ConfigurationObject']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2configuration""", alias="Ec2Configuration")
    BidPercentage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-bidpercentage""", alias="BidPercentage")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-securitygroupids""", alias="SecurityGroupIds")
    AllocationStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-allocationstrategy""", alias="AllocationStrategy")
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-subnets""", alias="Subnets")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-type""", alias="Type")
    MinvCpus_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-minvcpus""", alias="MinvCpus")
    UpdateToLatestImageVersion_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-updatetolatestimageversion""", alias="UpdateToLatestImageVersion")
    LaunchTemplate_: Optional['LaunchTemplateSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-launchtemplate""", alias="LaunchTemplate")
    ImageId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-imageid""", alias="ImageId")
    InstanceRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancerole""", alias="InstanceRole")
    InstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-instancetypes""", alias="InstanceTypes")
    Ec2KeyPair_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-ec2keypair""", alias="Ec2KeyPair")
    PlacementGroup_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-placementgroup""", alias="PlacementGroup")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-tags""", alias="Tags")
    DesiredvCpus_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html#cfn-batch-computeenvironment-computeresources-desiredvcpus""", alias="DesiredvCpus")
    


    @property
    def tropo_type(self) -> troposphere.batch.ComputeResources:
        from troposphere.batch import ComputeResources as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ec2ConfigurationObject(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html
    Properties:
        - Name: ImageIdOverride
        - Name: ImageKubernetesVersion
        - Name: ImageType
    
    """
    
    ImageIdOverride_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html#cfn-batch-computeenvironment-ec2configurationobject-imageidoverride""", alias="ImageIdOverride")
    ImageKubernetesVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html#cfn-batch-computeenvironment-ec2configurationobject-imagekubernetesversion""", alias="ImageKubernetesVersion")
    ImageType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html#cfn-batch-computeenvironment-ec2configurationobject-imagetype""", alias="ImageType")
    


    @property
    def tropo_type(self) -> troposphere.batch.Ec2ConfigurationObject:
        from troposphere.batch import Ec2ConfigurationObject as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EksConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-eksconfiguration.html
    Properties:
        - Name: EksClusterArn
        - Name: KubernetesNamespace
    
    """
    
    EksClusterArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-eksconfiguration.html#cfn-batch-computeenvironment-eksconfiguration-eksclusterarn""", alias="EksClusterArn")
    KubernetesNamespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-eksconfiguration.html#cfn-batch-computeenvironment-eksconfiguration-kubernetesnamespace""", alias="KubernetesNamespace")
    


    @property
    def tropo_type(self) -> troposphere.batch.EksConfiguration:
        from troposphere.batch import EksConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchTemplateSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html
    Properties:
        - Name: LaunchTemplateName
        - Name: Version
        - Name: LaunchTemplateId
    
    """
    
    LaunchTemplateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html#cfn-batch-computeenvironment-launchtemplatespecification-launchtemplatename""", alias="LaunchTemplateName")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html#cfn-batch-computeenvironment-launchtemplatespecification-version""", alias="Version")
    LaunchTemplateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html#cfn-batch-computeenvironment-launchtemplatespecification-launchtemplateid""", alias="LaunchTemplateId")
    


    @property
    def tropo_type(self) -> troposphere.batch.LaunchTemplateSpecification:
        from troposphere.batch import LaunchTemplateSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UpdatePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-updatepolicy.html
    Properties:
        - Name: JobExecutionTimeoutMinutes
        - Name: TerminateJobsOnUpdate
    
    """
    
    JobExecutionTimeoutMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-updatepolicy.html#cfn-batch-computeenvironment-updatepolicy-jobexecutiontimeoutminutes""", alias="JobExecutionTimeoutMinutes")
    TerminateJobsOnUpdate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-updatepolicy.html#cfn-batch-computeenvironment-updatepolicy-terminatejobsonupdate""", alias="TerminateJobsOnUpdate")
    


    @property
    def tropo_type(self) -> troposphere.batch.UpdatePolicy:
        from troposphere.batch import UpdatePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuthorizationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-authorizationconfig.html
    Properties:
        - Name: Iam
        - Name: AccessPointId
    
    """
    
    Iam_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-authorizationconfig.html#cfn-batch-jobdefinition-authorizationconfig-iam""", alias="Iam")
    AccessPointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-authorizationconfig.html#cfn-batch-jobdefinition-authorizationconfig-accesspointid""", alias="AccessPointId")
    


    @property
    def tropo_type(self) -> troposphere.batch.AuthorizationConfig:
        from troposphere.batch import AuthorizationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContainerProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html
    Properties:
        - Name: User
        - Name: Secrets
        - Name: Memory
        - Name: Privileged
        - Name: LinuxParameters
        - Name: FargatePlatformConfiguration
        - Name: JobRoleArn
        - Name: ReadonlyRootFilesystem
        - Name: Vcpus
        - Name: Image
        - Name: ResourceRequirements
        - Name: LogConfiguration
        - Name: MountPoints
        - Name: ExecutionRoleArn
        - Name: RuntimePlatform
        - Name: Volumes
        - Name: Command
        - Name: Environment
        - Name: Ulimits
        - Name: NetworkConfiguration
        - Name: InstanceType
        - Name: EphemeralStorage
    
    """
    
    User_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-user""", alias="User")
    Secrets_: Optional[List['Secret']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-secrets""", alias="Secrets")
    Memory_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-memory""", alias="Memory")
    Privileged_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-privileged""", alias="Privileged")
    LinuxParameters_: Optional['LinuxParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-linuxparameters""", alias="LinuxParameters")
    FargatePlatformConfiguration_: Optional['FargatePlatformConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-fargateplatformconfiguration""", alias="FargatePlatformConfiguration")
    JobRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-jobrolearn""", alias="JobRoleArn")
    ReadonlyRootFilesystem_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-readonlyrootfilesystem""", alias="ReadonlyRootFilesystem")
    Vcpus_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-vcpus""", alias="Vcpus")
    Image_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-image""", alias="Image")
    ResourceRequirements_: Optional[List['ResourceRequirement']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-resourcerequirements""", alias="ResourceRequirements")
    LogConfiguration_: Optional['LogConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-logconfiguration""", alias="LogConfiguration")
    MountPoints_: Optional[List['MountPoints']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-mountpoints""", alias="MountPoints")
    ExecutionRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-executionrolearn""", alias="ExecutionRoleArn")
    RuntimePlatform_: Optional['RuntimePlatform'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-runtimeplatform""", alias="RuntimePlatform")
    Volumes_: Optional[List['Volumes']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-volumes""", alias="Volumes")
    Command_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-command""", alias="Command")
    Environment_: Optional[List['Environment']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-environment""", alias="Environment")
    Ulimits_: Optional[List['Ulimit']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-ulimits""", alias="Ulimits")
    NetworkConfiguration_: Optional['NetworkConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-networkconfiguration""", alias="NetworkConfiguration")
    InstanceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-instancetype""", alias="InstanceType")
    EphemeralStorage_: Optional['EphemeralStorage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html#cfn-batch-jobdefinition-containerproperties-ephemeralstorage""", alias="EphemeralStorage")
    


    @property
    def tropo_type(self) -> troposphere.batch.ContainerProperties:
        from troposphere.batch import ContainerProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Device(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html
    Properties:
        - Name: HostPath
        - Name: Permissions
        - Name: ContainerPath
    
    """
    
    HostPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html#cfn-batch-jobdefinition-device-hostpath""", alias="HostPath")
    Permissions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html#cfn-batch-jobdefinition-device-permissions""", alias="Permissions")
    ContainerPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html#cfn-batch-jobdefinition-device-containerpath""", alias="ContainerPath")
    


    @property
    def tropo_type(self) -> troposphere.batch.Device:
        from troposphere.batch import Device as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EfsVolumeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html
    Properties:
        - Name: TransitEncryption
        - Name: AuthorizationConfig
        - Name: FileSystemId
        - Name: RootDirectory
        - Name: TransitEncryptionPort
    
    """
    
    TransitEncryption_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-transitencryption""", alias="TransitEncryption")
    AuthorizationConfig_: Optional['AuthorizationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-authorizationconfig""", alias="AuthorizationConfig")
    FileSystemId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-filesystemid""", alias="FileSystemId")
    RootDirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-rootdirectory""", alias="RootDirectory")
    TransitEncryptionPort_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html#cfn-batch-jobdefinition-efsvolumeconfiguration-transitencryptionport""", alias="TransitEncryptionPort")
    


    @property
    def tropo_type(self) -> troposphere.batch.EfsVolumeConfiguration:
        from troposphere.batch import EfsVolumeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EksContainer(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html
    Properties:
        - Name: Args
        - Name: VolumeMounts
        - Name: ImagePullPolicy
        - Name: Command
        - Name: SecurityContext
        - Name: Resources
        - Name: Image
        - Name: Env
        - Name: Name
    
    """
    
    Args_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-args""", alias="Args")
    VolumeMounts_: Optional[List['EksContainerVolumeMount']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-volumemounts""", alias="VolumeMounts")
    ImagePullPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-imagepullpolicy""", alias="ImagePullPolicy")
    Command_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-command""", alias="Command")
    SecurityContext_: Optional['EksContainerSecurityContext'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-securitycontext""", alias="SecurityContext")
    Resources_: Optional['EksContainerResourceRequirements'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-resources""", alias="Resources")
    Image_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-image""", alias="Image")
    Env_: Optional[List['EksContainerEnvironmentVariable']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-env""", alias="Env")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html#cfn-batch-jobdefinition-ekscontainer-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.batch.EksContainer:
        from troposphere.batch import EksContainer as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EksContainerEnvironmentVariable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainerenvironmentvariable.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainerenvironmentvariable.html#cfn-batch-jobdefinition-ekscontainerenvironmentvariable-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainerenvironmentvariable.html#cfn-batch-jobdefinition-ekscontainerenvironmentvariable-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.batch.EksContainerEnvironmentVariable:
        from troposphere.batch import EksContainerEnvironmentVariable as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EksContainerResourceRequirements(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainerresourcerequirements.html
    Properties:
        - Name: Limits
        - Name: Requests
    
    """
    
    Limits_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainerresourcerequirements.html#cfn-batch-jobdefinition-ekscontainerresourcerequirements-limits""", alias="Limits")
    Requests_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainerresourcerequirements.html#cfn-batch-jobdefinition-ekscontainerresourcerequirements-requests""", alias="Requests")
    


    @property
    def tropo_type(self) -> troposphere.batch.EksContainerResourceRequirements:
        from troposphere.batch import EksContainerResourceRequirements as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EksContainerSecurityContext(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainersecuritycontext.html
    Properties:
        - Name: RunAsUser
        - Name: RunAsNonRoot
        - Name: Privileged
        - Name: ReadOnlyRootFilesystem
        - Name: RunAsGroup
    
    """
    
    RunAsUser_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainersecuritycontext.html#cfn-batch-jobdefinition-ekscontainersecuritycontext-runasuser""", alias="RunAsUser")
    RunAsNonRoot_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainersecuritycontext.html#cfn-batch-jobdefinition-ekscontainersecuritycontext-runasnonroot""", alias="RunAsNonRoot")
    Privileged_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainersecuritycontext.html#cfn-batch-jobdefinition-ekscontainersecuritycontext-privileged""", alias="Privileged")
    ReadOnlyRootFilesystem_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainersecuritycontext.html#cfn-batch-jobdefinition-ekscontainersecuritycontext-readonlyrootfilesystem""", alias="ReadOnlyRootFilesystem")
    RunAsGroup_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainersecuritycontext.html#cfn-batch-jobdefinition-ekscontainersecuritycontext-runasgroup""", alias="RunAsGroup")
    


    @property
    def tropo_type(self) -> troposphere.batch.EksContainerSecurityContext:
        from troposphere.batch import EksContainerSecurityContext as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EksContainerVolumeMount(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainervolumemount.html
    Properties:
        - Name: MountPath
        - Name: ReadOnly
        - Name: Name
    
    """
    
    MountPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainervolumemount.html#cfn-batch-jobdefinition-ekscontainervolumemount-mountpath""", alias="MountPath")
    ReadOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainervolumemount.html#cfn-batch-jobdefinition-ekscontainervolumemount-readonly""", alias="ReadOnly")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainervolumemount.html#cfn-batch-jobdefinition-ekscontainervolumemount-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.batch.EksContainerVolumeMount:
        from troposphere.batch import EksContainerVolumeMount as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EksEmptyDir(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksemptydir.html
    Properties:
        - Name: Medium
        - Name: SizeLimit
    
    """
    
    Medium_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksemptydir.html#cfn-batch-jobdefinition-eksemptydir-medium""", alias="Medium")
    SizeLimit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksemptydir.html#cfn-batch-jobdefinition-eksemptydir-sizelimit""", alias="SizeLimit")
    


    @property
    def tropo_type(self) -> troposphere.batch.EksEmptyDir:
        from troposphere.batch import EksEmptyDir as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EksHostPath(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekshostpath.html
    Properties:
        - Name: Path
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekshostpath.html#cfn-batch-jobdefinition-ekshostpath-path""", alias="Path")
    


    @property
    def tropo_type(self) -> troposphere.batch.EksHostPath:
        from troposphere.batch import EksHostPath as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EksProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksproperties.html
    Properties:
        - Name: PodProperties
    
    """
    
    PodProperties_: Optional['PodProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksproperties.html#cfn-batch-jobdefinition-eksproperties-podproperties""", alias="PodProperties")
    


    @property
    def tropo_type(self) -> troposphere.batch.EksProperties:
        from troposphere.batch import EksProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EksSecret(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekssecret.html
    Properties:
        - Name: SecretName
        - Name: Optional
    
    """
    
    SecretName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekssecret.html#cfn-batch-jobdefinition-ekssecret-secretname""", alias="SecretName")
    Optional_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekssecret.html#cfn-batch-jobdefinition-ekssecret-optional""", alias="Optional")
    


    @property
    def tropo_type(self) -> troposphere.batch.EksSecret:
        from troposphere.batch import EksSecret as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EksVolume(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksvolume.html
    Properties:
        - Name: Secret
        - Name: EmptyDir
        - Name: HostPath
        - Name: Name
    
    """
    
    Secret_: Optional['EksSecret'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksvolume.html#cfn-batch-jobdefinition-eksvolume-secret""", alias="Secret")
    EmptyDir_: Optional['EksEmptyDir'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksvolume.html#cfn-batch-jobdefinition-eksvolume-emptydir""", alias="EmptyDir")
    HostPath_: Optional['EksHostPath'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksvolume.html#cfn-batch-jobdefinition-eksvolume-hostpath""", alias="HostPath")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksvolume.html#cfn-batch-jobdefinition-eksvolume-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.batch.EksVolume:
        from troposphere.batch import EksVolume as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Environment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html#cfn-batch-jobdefinition-environment-value""", alias="Value")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html#cfn-batch-jobdefinition-environment-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.batch.Environment:
        from troposphere.batch import Environment as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EphemeralStorage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-ephemeralstorage.html
    Properties:
        - Name: SizeInGiB
    
    """
    
    SizeInGiB_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-ephemeralstorage.html#cfn-batch-jobdefinition-containerproperties-ephemeralstorage-sizeingib""", alias="SizeInGiB")
    


    @property
    def tropo_type(self) -> troposphere.batch.EphemeralStorage:
        from troposphere.batch import EphemeralStorage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluateOnExit(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html
    Properties:
        - Name: Action
        - Name: OnExitCode
        - Name: OnReason
        - Name: OnStatusReason
    
    """
    
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html#cfn-batch-jobdefinition-evaluateonexit-action""", alias="Action")
    OnExitCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html#cfn-batch-jobdefinition-evaluateonexit-onexitcode""", alias="OnExitCode")
    OnReason_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html#cfn-batch-jobdefinition-evaluateonexit-onreason""", alias="OnReason")
    OnStatusReason_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html#cfn-batch-jobdefinition-evaluateonexit-onstatusreason""", alias="OnStatusReason")
    


    @property
    def tropo_type(self) -> troposphere.batch.EvaluateOnExit:
        from troposphere.batch import EvaluateOnExit as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FargatePlatformConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-fargateplatformconfiguration.html
    Properties:
        - Name: PlatformVersion
    
    """
    
    PlatformVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-fargateplatformconfiguration.html#cfn-batch-jobdefinition-containerproperties-fargateplatformconfiguration-platformversion""", alias="PlatformVersion")
    


    @property
    def tropo_type(self) -> troposphere.batch.FargatePlatformConfiguration:
        from troposphere.batch import FargatePlatformConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LinuxParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html
    Properties:
        - Name: Swappiness
        - Name: Tmpfs
        - Name: SharedMemorySize
        - Name: Devices
        - Name: InitProcessEnabled
        - Name: MaxSwap
    
    """
    
    Swappiness_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html#cfn-batch-jobdefinition-containerproperties-linuxparameters-swappiness""", alias="Swappiness")
    Tmpfs_: Optional[List['Tmpfs']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html#cfn-batch-jobdefinition-containerproperties-linuxparameters-tmpfs""", alias="Tmpfs")
    SharedMemorySize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html#cfn-batch-jobdefinition-containerproperties-linuxparameters-sharedmemorysize""", alias="SharedMemorySize")
    Devices_: Optional[List['Device']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html#cfn-batch-jobdefinition-containerproperties-linuxparameters-devices""", alias="Devices")
    InitProcessEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html#cfn-batch-jobdefinition-containerproperties-linuxparameters-initprocessenabled""", alias="InitProcessEnabled")
    MaxSwap_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html#cfn-batch-jobdefinition-containerproperties-linuxparameters-maxswap""", alias="MaxSwap")
    


    @property
    def tropo_type(self) -> troposphere.batch.LinuxParameters:
        from troposphere.batch import LinuxParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LogConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html
    Properties:
        - Name: SecretOptions
        - Name: Options
        - Name: LogDriver
    
    """
    
    SecretOptions_: Optional[List['Secret']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html#cfn-batch-jobdefinition-containerproperties-logconfiguration-secretoptions""", alias="SecretOptions")
    Options_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html#cfn-batch-jobdefinition-containerproperties-logconfiguration-options""", alias="Options")
    LogDriver_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html#cfn-batch-jobdefinition-containerproperties-logconfiguration-logdriver""", alias="LogDriver")
    


    @property
    def tropo_type(self) -> troposphere.batch.LogConfiguration:
        from troposphere.batch import LogConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Metadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties-metadata.html
    Properties:
        - Name: Labels
    
    """
    
    Labels_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties-metadata.html#cfn-batch-jobdefinition-podproperties-metadata-labels""", alias="Labels")
    


    @property
    def tropo_type(self) -> troposphere.batch.Metadata:
        from troposphere.batch import Metadata as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MountPoints(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html
    Properties:
        - Name: ReadOnly
        - Name: SourceVolume
        - Name: ContainerPath
    
    """
    
    ReadOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html#cfn-batch-jobdefinition-mountpoints-readonly""", alias="ReadOnly")
    SourceVolume_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html#cfn-batch-jobdefinition-mountpoints-sourcevolume""", alias="SourceVolume")
    ContainerPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html#cfn-batch-jobdefinition-mountpoints-containerpath""", alias="ContainerPath")
    


    @property
    def tropo_type(self) -> troposphere.batch.MountPoints:
        from troposphere.batch import MountPoints as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-networkconfiguration.html
    Properties:
        - Name: AssignPublicIp
    
    """
    
    AssignPublicIp_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-networkconfiguration.html#cfn-batch-jobdefinition-containerproperties-networkconfiguration-assignpublicip""", alias="AssignPublicIp")
    


    @property
    def tropo_type(self) -> troposphere.batch.NetworkConfiguration:
        from troposphere.batch import NetworkConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NodeProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html
    Properties:
        - Name: MainNode
        - Name: NodeRangeProperties
        - Name: NumNodes
    
    """
    
    MainNode_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html#cfn-batch-jobdefinition-nodeproperties-mainnode""", alias="MainNode")
    NodeRangeProperties_: List['NodeRangeProperty'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html#cfn-batch-jobdefinition-nodeproperties-noderangeproperties""", alias="NodeRangeProperties")
    NumNodes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html#cfn-batch-jobdefinition-nodeproperties-numnodes""", alias="NumNodes")
    


    @property
    def tropo_type(self) -> troposphere.batch.NodeProperties:
        from troposphere.batch import NodeProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NodeRangeProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html
    Properties:
        - Name: Container
        - Name: TargetNodes
    
    """
    
    Container_: Optional['ContainerProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html#cfn-batch-jobdefinition-noderangeproperty-container""", alias="Container")
    TargetNodes_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html#cfn-batch-jobdefinition-noderangeproperty-targetnodes""", alias="TargetNodes")
    


    @property
    def tropo_type(self) -> troposphere.batch.NodeRangeProperty:
        from troposphere.batch import NodeRangeProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PodProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html
    Properties:
        - Name: Volumes
        - Name: DnsPolicy
        - Name: Containers
        - Name: Metadata
        - Name: ServiceAccountName
        - Name: HostNetwork
    
    """
    
    Volumes_: Optional[List['EksVolume']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html#cfn-batch-jobdefinition-podproperties-volumes""", alias="Volumes")
    DnsPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html#cfn-batch-jobdefinition-podproperties-dnspolicy""", alias="DnsPolicy")
    Containers_: Optional[List['EksContainer']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html#cfn-batch-jobdefinition-podproperties-containers""", alias="Containers")
    Metadata_: Optional['Metadata'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html#cfn-batch-jobdefinition-podproperties-metadata""", alias="Metadata")
    ServiceAccountName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html#cfn-batch-jobdefinition-podproperties-serviceaccountname""", alias="ServiceAccountName")
    HostNetwork_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html#cfn-batch-jobdefinition-podproperties-hostnetwork""", alias="HostNetwork")
    


    @property
    def tropo_type(self) -> troposphere.batch.PodProperties:
        from troposphere.batch import PodProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceRequirement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html#cfn-batch-jobdefinition-resourcerequirement-type""", alias="Type")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html#cfn-batch-jobdefinition-resourcerequirement-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.batch.ResourceRequirement:
        from troposphere.batch import ResourceRequirement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RetryStrategy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html
    Properties:
        - Name: EvaluateOnExit
        - Name: Attempts
    
    """
    
    EvaluateOnExit_: Optional[List['EvaluateOnExit']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html#cfn-batch-jobdefinition-retrystrategy-evaluateonexit""", alias="EvaluateOnExit")
    Attempts_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html#cfn-batch-jobdefinition-retrystrategy-attempts""", alias="Attempts")
    


    @property
    def tropo_type(self) -> troposphere.batch.RetryStrategy:
        from troposphere.batch import RetryStrategy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuntimePlatform(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-runtimeplatform.html
    Properties:
        - Name: OperatingSystemFamily
        - Name: CpuArchitecture
    
    """
    
    OperatingSystemFamily_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-runtimeplatform.html#cfn-batch-jobdefinition-containerproperties-runtimeplatform-operatingsystemfamily""", alias="OperatingSystemFamily")
    CpuArchitecture_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-runtimeplatform.html#cfn-batch-jobdefinition-containerproperties-runtimeplatform-cpuarchitecture""", alias="CpuArchitecture")
    


    @property
    def tropo_type(self) -> troposphere.batch.RuntimePlatform:
        from troposphere.batch import RuntimePlatform as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Secret(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html
    Properties:
        - Name: ValueFrom
        - Name: Name
    
    """
    
    ValueFrom_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html#cfn-batch-jobdefinition-secret-valuefrom""", alias="ValueFrom")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html#cfn-batch-jobdefinition-secret-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.batch.Secret:
        from troposphere.batch import Secret as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Timeout(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-timeout.html
    Properties:
        - Name: AttemptDurationSeconds
    
    """
    
    AttemptDurationSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-timeout.html#cfn-batch-jobdefinition-timeout-attemptdurationseconds""", alias="AttemptDurationSeconds")
    


    @property
    def tropo_type(self) -> troposphere.batch.Timeout:
        from troposphere.batch import Timeout as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tmpfs(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html
    Properties:
        - Name: Size
        - Name: ContainerPath
        - Name: MountOptions
    
    """
    
    Size_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html#cfn-batch-jobdefinition-tmpfs-size""", alias="Size")
    ContainerPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html#cfn-batch-jobdefinition-tmpfs-containerpath""", alias="ContainerPath")
    MountOptions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html#cfn-batch-jobdefinition-tmpfs-mountoptions""", alias="MountOptions")
    


    @property
    def tropo_type(self) -> troposphere.batch.Tmpfs:
        from troposphere.batch import Tmpfs as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Ulimit(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html
    Properties:
        - Name: SoftLimit
        - Name: HardLimit
        - Name: Name
    
    """
    
    SoftLimit_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html#cfn-batch-jobdefinition-ulimit-softlimit""", alias="SoftLimit")
    HardLimit_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html#cfn-batch-jobdefinition-ulimit-hardlimit""", alias="HardLimit")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html#cfn-batch-jobdefinition-ulimit-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.batch.Ulimit:
        from troposphere.batch import Ulimit as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Volumes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html
    Properties:
        - Name: Host
        - Name: EfsVolumeConfiguration
        - Name: Name
    
    """
    
    Host_: Optional['VolumesHost'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html#cfn-batch-jobdefinition-volumes-host""", alias="Host")
    EfsVolumeConfiguration_: Optional['EfsVolumeConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html#cfn-batch-jobdefinition-volumes-efsvolumeconfiguration""", alias="EfsVolumeConfiguration")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html#cfn-batch-jobdefinition-volumes-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.batch.Volumes:
        from troposphere.batch import Volumes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VolumesHost(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumeshost.html
    Properties:
        - Name: SourcePath
    
    """
    
    SourcePath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumeshost.html#cfn-batch-jobdefinition-volumeshost-sourcepath""", alias="SourcePath")
    


    @property
    def tropo_type(self) -> troposphere.batch.VolumesHost:
        from troposphere.batch import VolumesHost as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComputeEnvironmentOrder(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html
    Properties:
        - Name: ComputeEnvironment
        - Name: Order
    
    """
    
    ComputeEnvironment_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html#cfn-batch-jobqueue-computeenvironmentorder-computeenvironment""", alias="ComputeEnvironment")
    Order_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html#cfn-batch-jobqueue-computeenvironmentorder-order""", alias="Order")
    


    @property
    def tropo_type(self) -> troposphere.batch.ComputeEnvironmentOrder:
        from troposphere.batch import ComputeEnvironmentOrder as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FairsharePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html
    Properties:
        - Name: ShareDistribution
        - Name: ShareDecaySeconds
        - Name: ComputeReservation
    
    """
    
    ShareDistribution_: Optional[List['ShareAttributes']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html#cfn-batch-schedulingpolicy-fairsharepolicy-sharedistribution""", alias="ShareDistribution")
    ShareDecaySeconds_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html#cfn-batch-schedulingpolicy-fairsharepolicy-sharedecayseconds""", alias="ShareDecaySeconds")
    ComputeReservation_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html#cfn-batch-schedulingpolicy-fairsharepolicy-computereservation""", alias="ComputeReservation")
    


    @property
    def tropo_type(self) -> troposphere.batch.FairsharePolicy:
        from troposphere.batch import FairsharePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ShareAttributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-shareattributes.html
    Properties:
        - Name: WeightFactor
        - Name: ShareIdentifier
    
    """
    
    WeightFactor_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-shareattributes.html#cfn-batch-schedulingpolicy-shareattributes-weightfactor""", alias="WeightFactor")
    ShareIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-shareattributes.html#cfn-batch-schedulingpolicy-shareattributes-shareidentifier""", alias="ShareIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.batch.ShareAttributes:
        from troposphere.batch import ShareAttributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ComputeEnvironment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html
    Properties:
        - Name: UnmanagedvCpus
        - Name: Type
        - Name: ReplaceComputeEnvironment
        - Name: ServiceRole
        - Name: UpdatePolicy
        - Name: EksConfiguration
        - Name: ComputeEnvironmentName
        - Name: ComputeResources
        - Name: State
        - Name: Tags
    Attributes:
        - Name: ComputeEnvironmentArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UnmanagedvCpus_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-unmanagedvcpus""", alias="UnmanagedvCpus")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-type""", alias="Type")
    ReplaceComputeEnvironment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-replacecomputeenvironment""", alias="ReplaceComputeEnvironment")
    ServiceRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-servicerole""", alias="ServiceRole")
    UpdatePolicy_: Optional['UpdatePolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-updatepolicy""", alias="UpdatePolicy")
    EksConfiguration_: Optional['EksConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-eksconfiguration""", alias="EksConfiguration")
    ComputeEnvironmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-computeenvironmentname""", alias="ComputeEnvironmentName")
    ComputeResources_: Optional['ComputeResources'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-computeresources""", alias="ComputeResources")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-state""", alias="State")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html#cfn-batch-computeenvironment-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.batch.ComputeEnvironment:
        from troposphere.batch import ComputeEnvironment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.batch import ComputeEnvironment as TropoT
        return resource_to_troposphere(self, TropoT)


class JobDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html
    Properties:
        - Name: Type
        - Name: Parameters
        - Name: NodeProperties
        - Name: SchedulingPriority
        - Name: Timeout
        - Name: ContainerProperties
        - Name: JobDefinitionName
        - Name: PropagateTags
        - Name: PlatformCapabilities
        - Name: EksProperties
        - Name: RetryStrategy
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-type""", alias="Type")
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-parameters""", alias="Parameters")
    NodeProperties_: Optional['NodeProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-nodeproperties""", alias="NodeProperties")
    SchedulingPriority_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-schedulingpriority""", alias="SchedulingPriority")
    Timeout_: Optional['Timeout'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-timeout""", alias="Timeout")
    ContainerProperties_: Optional['ContainerProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-containerproperties""", alias="ContainerProperties")
    JobDefinitionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-jobdefinitionname""", alias="JobDefinitionName")
    PropagateTags_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-propagatetags""", alias="PropagateTags")
    PlatformCapabilities_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-platformcapabilities""", alias="PlatformCapabilities")
    EksProperties_: Optional['EksProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-eksproperties""", alias="EksProperties")
    RetryStrategy_: Optional['RetryStrategy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-retrystrategy""", alias="RetryStrategy")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html#cfn-batch-jobdefinition-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.batch.JobDefinition:
        from troposphere.batch import JobDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.batch import JobDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class JobQueue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html
    Properties:
        - Name: ComputeEnvironmentOrder
        - Name: Priority
        - Name: State
        - Name: SchedulingPolicyArn
        - Name: JobQueueName
        - Name: Tags
    Attributes:
        - Name: JobQueueArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ComputeEnvironmentOrder_: List['ComputeEnvironmentOrder'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-computeenvironmentorder""", alias="ComputeEnvironmentOrder")
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-priority""", alias="Priority")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-state""", alias="State")
    SchedulingPolicyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-schedulingpolicyarn""", alias="SchedulingPolicyArn")
    JobQueueName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-jobqueuename""", alias="JobQueueName")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html#cfn-batch-jobqueue-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.batch.JobQueue:
        from troposphere.batch import JobQueue as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.batch import JobQueue as TropoT
        return resource_to_troposphere(self, TropoT)


class SchedulingPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html
    Properties:
        - Name: FairsharePolicy
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FairsharePolicy_: Optional['FairsharePolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html#cfn-batch-schedulingpolicy-fairsharepolicy""", alias="FairsharePolicy")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html#cfn-batch-schedulingpolicy-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html#cfn-batch-schedulingpolicy-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.batch.SchedulingPolicy:
        from troposphere.batch import SchedulingPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.batch import SchedulingPolicy as TropoT
        return resource_to_troposphere(self, TropoT)

