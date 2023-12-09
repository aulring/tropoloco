from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ComponentConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html
    Properties:
        - Name: Parameters
        - Name: ComponentArn
    
    """
    
    Parameters_: Optional[List['ComponentParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html#cfn-imagebuilder-containerrecipe-componentconfiguration-parameters""", alias="Parameters")
    ComponentArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html#cfn-imagebuilder-containerrecipe-componentconfiguration-componentarn""", alias="ComponentArn")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.ComponentConfiguration:
        from troposphere.imagebuilder import ComponentConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentparameter.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentparameter.html#cfn-imagebuilder-containerrecipe-componentparameter-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentparameter.html#cfn-imagebuilder-containerrecipe-componentparameter-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.ComponentParameter:
        from troposphere.imagebuilder import ComponentParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EbsInstanceBlockDeviceSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html
    Properties:
        - Name: SnapshotId
        - Name: VolumeType
        - Name: KmsKeyId
        - Name: Encrypted
        - Name: Throughput
        - Name: Iops
        - Name: VolumeSize
        - Name: DeleteOnTermination
    
    """
    
    SnapshotId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-snapshotid""", alias="SnapshotId")
    VolumeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumetype""", alias="VolumeType")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-kmskeyid""", alias="KmsKeyId")
    Encrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-encrypted""", alias="Encrypted")
    Throughput_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-throughput""", alias="Throughput")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-iops""", alias="Iops")
    VolumeSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumesize""", alias="VolumeSize")
    DeleteOnTermination_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-deleteontermination""", alias="DeleteOnTermination")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.EbsInstanceBlockDeviceSpecification:
        from troposphere.imagebuilder import EbsInstanceBlockDeviceSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceBlockDeviceMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html
    Properties:
        - Name: Ebs
        - Name: NoDevice
        - Name: VirtualName
        - Name: DeviceName
    
    """
    
    Ebs_: Optional['EbsInstanceBlockDeviceSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-ebs""", alias="Ebs")
    NoDevice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-nodevice""", alias="NoDevice")
    VirtualName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-virtualname""", alias="VirtualName")
    DeviceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-devicename""", alias="DeviceName")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.InstanceBlockDeviceMapping:
        from troposphere.imagebuilder import InstanceBlockDeviceMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html
    Properties:
        - Name: BlockDeviceMappings
        - Name: Image
    
    """
    
    BlockDeviceMappings_: Optional[List['InstanceBlockDeviceMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html#cfn-imagebuilder-containerrecipe-instanceconfiguration-blockdevicemappings""", alias="BlockDeviceMappings")
    Image_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html#cfn-imagebuilder-containerrecipe-instanceconfiguration-image""", alias="Image")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.InstanceConfiguration:
        from troposphere.imagebuilder import InstanceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetContainerRepository(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html
    Properties:
        - Name: Service
        - Name: RepositoryName
    
    """
    
    Service_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html#cfn-imagebuilder-containerrecipe-targetcontainerrepository-service""", alias="Service")
    RepositoryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html#cfn-imagebuilder-containerrecipe-targetcontainerrepository-repositoryname""", alias="RepositoryName")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.TargetContainerRepository:
        from troposphere.imagebuilder import TargetContainerRepository as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AmiDistributionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html
    Properties:
        - Name: AmiTags
        - Name: Description
        - Name: KmsKeyId
        - Name: LaunchPermissionConfiguration
        - Name: TargetAccountIds
        - Name: Name
    
    """
    
    AmiTags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-amitags""", alias="AmiTags")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-description""", alias="Description")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-kmskeyid""", alias="KmsKeyId")
    LaunchPermissionConfiguration_: Optional['LaunchPermissionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-launchpermissionconfiguration""", alias="LaunchPermissionConfiguration")
    TargetAccountIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-targetaccountids""", alias="TargetAccountIds")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.AmiDistributionConfiguration:
        from troposphere.imagebuilder import AmiDistributionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContainerDistributionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html
    Properties:
        - Name: TargetRepository
        - Name: ContainerTags
        - Name: Description
    
    """
    
    TargetRepository_: Optional['TargetContainerRepository'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-targetrepository""", alias="TargetRepository")
    ContainerTags_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-containertags""", alias="ContainerTags")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-description""", alias="Description")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.ContainerDistributionConfiguration:
        from troposphere.imagebuilder import ContainerDistributionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Distribution(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html
    Properties:
        - Name: AmiDistributionConfiguration
        - Name: ContainerDistributionConfiguration
        - Name: FastLaunchConfigurations
        - Name: LaunchTemplateConfigurations
        - Name: LicenseConfigurationArns
        - Name: Region
    
    """
    
    AmiDistributionConfiguration_: Optional['AmiDistributionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-amidistributionconfiguration""", alias="AmiDistributionConfiguration")
    ContainerDistributionConfiguration_: Optional['ContainerDistributionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-containerdistributionconfiguration""", alias="ContainerDistributionConfiguration")
    FastLaunchConfigurations_: Optional[List['FastLaunchConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-fastlaunchconfigurations""", alias="FastLaunchConfigurations")
    LaunchTemplateConfigurations_: Optional[List['LaunchTemplateConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-launchtemplateconfigurations""", alias="LaunchTemplateConfigurations")
    LicenseConfigurationArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-licenseconfigurationarns""", alias="LicenseConfigurationArns")
    Region_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-region""", alias="Region")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.Distribution:
        from troposphere.imagebuilder import Distribution as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FastLaunchConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html
    Properties:
        - Name: AccountId
        - Name: LaunchTemplate
        - Name: Enabled
        - Name: MaxParallelLaunches
        - Name: SnapshotConfiguration
    
    """
    
    AccountId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-accountid""", alias="AccountId")
    LaunchTemplate_: Optional['FastLaunchLaunchTemplateSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-launchtemplate""", alias="LaunchTemplate")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-enabled""", alias="Enabled")
    MaxParallelLaunches_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-maxparallellaunches""", alias="MaxParallelLaunches")
    SnapshotConfiguration_: Optional['FastLaunchSnapshotConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-snapshotconfiguration""", alias="SnapshotConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.FastLaunchConfiguration:
        from troposphere.imagebuilder import FastLaunchConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FastLaunchLaunchTemplateSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html
    Properties:
        - Name: LaunchTemplateName
        - Name: LaunchTemplateVersion
        - Name: LaunchTemplateId
    
    """
    
    LaunchTemplateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplatename""", alias="LaunchTemplateName")
    LaunchTemplateVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplateversion""", alias="LaunchTemplateVersion")
    LaunchTemplateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplateid""", alias="LaunchTemplateId")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.FastLaunchLaunchTemplateSpecification:
        from troposphere.imagebuilder import FastLaunchLaunchTemplateSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FastLaunchSnapshotConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration.html
    Properties:
        - Name: TargetResourceCount
    
    """
    
    TargetResourceCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration-targetresourcecount""", alias="TargetResourceCount")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.FastLaunchSnapshotConfiguration:
        from troposphere.imagebuilder import FastLaunchSnapshotConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchPermissionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html
    Properties:
        - Name: OrganizationArns
        - Name: OrganizationalUnitArns
        - Name: UserIds
        - Name: UserGroups
    
    """
    
    OrganizationArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-organizationarns""", alias="OrganizationArns")
    OrganizationalUnitArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-organizationalunitarns""", alias="OrganizationalUnitArns")
    UserIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-userids""", alias="UserIds")
    UserGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-usergroups""", alias="UserGroups")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.LaunchPermissionConfiguration:
        from troposphere.imagebuilder import LaunchPermissionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchTemplateConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html
    Properties:
        - Name: SetDefaultVersion
        - Name: AccountId
        - Name: LaunchTemplateId
    
    """
    
    SetDefaultVersion_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchtemplateconfiguration-setdefaultversion""", alias="SetDefaultVersion")
    AccountId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchtemplateconfiguration-accountid""", alias="AccountId")
    LaunchTemplateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchtemplateconfiguration-launchtemplateid""", alias="LaunchTemplateId")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.LaunchTemplateConfiguration:
        from troposphere.imagebuilder import LaunchTemplateConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetContainerRepository(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository.html
    Properties:
        - Name: Service
        - Name: RepositoryName
    
    """
    
    Service_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository.html#cfn-imagebuilder-distributionconfiguration-targetcontainerrepository-service""", alias="Service")
    RepositoryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository.html#cfn-imagebuilder-distributionconfiguration-targetcontainerrepository-repositoryname""", alias="RepositoryName")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.TargetContainerRepository:
        from troposphere.imagebuilder import TargetContainerRepository as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EcrConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-ecrconfiguration.html
    Properties:
        - Name: ContainerTags
        - Name: RepositoryName
    
    """
    
    ContainerTags_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-ecrconfiguration.html#cfn-imagebuilder-image-ecrconfiguration-containertags""", alias="ContainerTags")
    RepositoryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-ecrconfiguration.html#cfn-imagebuilder-image-ecrconfiguration-repositoryname""", alias="RepositoryName")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.EcrConfiguration:
        from troposphere.imagebuilder import EcrConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImageScanningConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagescanningconfiguration.html
    Properties:
        - Name: EcrConfiguration
        - Name: ImageScanningEnabled
    
    """
    
    EcrConfiguration_: Optional['EcrConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagescanningconfiguration.html#cfn-imagebuilder-image-imagescanningconfiguration-ecrconfiguration""", alias="EcrConfiguration")
    ImageScanningEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagescanningconfiguration.html#cfn-imagebuilder-image-imagescanningconfiguration-imagescanningenabled""", alias="ImageScanningEnabled")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.ImageScanningConfiguration:
        from troposphere.imagebuilder import ImageScanningConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImageTestsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html
    Properties:
        - Name: TimeoutMinutes
        - Name: ImageTestsEnabled
    
    """
    
    TimeoutMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html#cfn-imagebuilder-image-imagetestsconfiguration-timeoutminutes""", alias="TimeoutMinutes")
    ImageTestsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html#cfn-imagebuilder-image-imagetestsconfiguration-imagetestsenabled""", alias="ImageTestsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.ImageTestsConfiguration:
        from troposphere.imagebuilder import ImageTestsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EcrConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-ecrconfiguration.html
    Properties:
        - Name: ContainerTags
        - Name: RepositoryName
    
    """
    
    ContainerTags_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-ecrconfiguration.html#cfn-imagebuilder-imagepipeline-ecrconfiguration-containertags""", alias="ContainerTags")
    RepositoryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-ecrconfiguration.html#cfn-imagebuilder-imagepipeline-ecrconfiguration-repositoryname""", alias="RepositoryName")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.EcrConfiguration:
        from troposphere.imagebuilder import EcrConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImageScanningConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration.html
    Properties:
        - Name: EcrConfiguration
        - Name: ImageScanningEnabled
    
    """
    
    EcrConfiguration_: Optional['EcrConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration.html#cfn-imagebuilder-imagepipeline-imagescanningconfiguration-ecrconfiguration""", alias="EcrConfiguration")
    ImageScanningEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration.html#cfn-imagebuilder-imagepipeline-imagescanningconfiguration-imagescanningenabled""", alias="ImageScanningEnabled")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.ImageScanningConfiguration:
        from troposphere.imagebuilder import ImageScanningConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImageTestsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html
    Properties:
        - Name: TimeoutMinutes
        - Name: ImageTestsEnabled
    
    """
    
    TimeoutMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration-timeoutminutes""", alias="TimeoutMinutes")
    ImageTestsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration-imagetestsenabled""", alias="ImageTestsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.ImageTestsConfiguration:
        from troposphere.imagebuilder import ImageTestsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Schedule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html
    Properties:
        - Name: ScheduleExpression
        - Name: PipelineExecutionStartCondition
    
    """
    
    ScheduleExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html#cfn-imagebuilder-imagepipeline-schedule-scheduleexpression""", alias="ScheduleExpression")
    PipelineExecutionStartCondition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html#cfn-imagebuilder-imagepipeline-schedule-pipelineexecutionstartcondition""", alias="PipelineExecutionStartCondition")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.Schedule:
        from troposphere.imagebuilder import Schedule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AdditionalInstanceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html
    Properties:
        - Name: UserDataOverride
        - Name: SystemsManagerAgent
    
    """
    
    UserDataOverride_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration-userdataoverride""", alias="UserDataOverride")
    SystemsManagerAgent_: Optional['SystemsManagerAgent'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration-systemsmanageragent""", alias="SystemsManagerAgent")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.AdditionalInstanceConfiguration:
        from troposphere.imagebuilder import AdditionalInstanceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html
    Properties:
        - Name: Parameters
        - Name: ComponentArn
    
    """
    
    Parameters_: Optional[List['ComponentParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html#cfn-imagebuilder-imagerecipe-componentconfiguration-parameters""", alias="Parameters")
    ComponentArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html#cfn-imagebuilder-imagerecipe-componentconfiguration-componentarn""", alias="ComponentArn")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.ComponentConfiguration:
        from troposphere.imagebuilder import ComponentConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html#cfn-imagebuilder-imagerecipe-componentparameter-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html#cfn-imagebuilder-imagerecipe-componentparameter-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.ComponentParameter:
        from troposphere.imagebuilder import ComponentParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EbsInstanceBlockDeviceSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html
    Properties:
        - Name: SnapshotId
        - Name: VolumeType
        - Name: KmsKeyId
        - Name: Encrypted
        - Name: Throughput
        - Name: Iops
        - Name: VolumeSize
        - Name: DeleteOnTermination
    
    """
    
    SnapshotId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-snapshotid""", alias="SnapshotId")
    VolumeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-volumetype""", alias="VolumeType")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-kmskeyid""", alias="KmsKeyId")
    Encrypted_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-encrypted""", alias="Encrypted")
    Throughput_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-throughput""", alias="Throughput")
    Iops_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-iops""", alias="Iops")
    VolumeSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-volumesize""", alias="VolumeSize")
    DeleteOnTermination_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-deleteontermination""", alias="DeleteOnTermination")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.EbsInstanceBlockDeviceSpecification:
        from troposphere.imagebuilder import EbsInstanceBlockDeviceSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceBlockDeviceMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html
    Properties:
        - Name: Ebs
        - Name: NoDevice
        - Name: VirtualName
        - Name: DeviceName
    
    """
    
    Ebs_: Optional['EbsInstanceBlockDeviceSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-ebs""", alias="Ebs")
    NoDevice_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-nodevice""", alias="NoDevice")
    VirtualName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-virtualname""", alias="VirtualName")
    DeviceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-devicename""", alias="DeviceName")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.InstanceBlockDeviceMapping:
        from troposphere.imagebuilder import InstanceBlockDeviceMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SystemsManagerAgent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-systemsmanageragent.html
    Properties:
        - Name: UninstallAfterBuild
    
    """
    
    UninstallAfterBuild_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-systemsmanageragent.html#cfn-imagebuilder-imagerecipe-systemsmanageragent-uninstallafterbuild""", alias="UninstallAfterBuild")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.SystemsManagerAgent:
        from troposphere.imagebuilder import SystemsManagerAgent as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InstanceMetadataOptions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions.html
    Properties:
        - Name: HttpPutResponseHopLimit
        - Name: HttpTokens
    
    """
    
    HttpPutResponseHopLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions.html#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions-httpputresponsehoplimit""", alias="HttpPutResponseHopLimit")
    HttpTokens_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions.html#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions-httptokens""", alias="HttpTokens")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.InstanceMetadataOptions:
        from troposphere.imagebuilder import InstanceMetadataOptions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Logging(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html
    Properties:
        - Name: S3Logs
    
    """
    
    S3Logs_: Optional['S3Logs'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html#cfn-imagebuilder-infrastructureconfiguration-logging-s3logs""", alias="S3Logs")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.Logging:
        from troposphere.imagebuilder import Logging as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Logs(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html
    Properties:
        - Name: S3KeyPrefix
        - Name: S3BucketName
    
    """
    
    S3KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3keyprefix""", alias="S3KeyPrefix")
    S3BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3bucketname""", alias="S3BucketName")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.S3Logs:
        from troposphere.imagebuilder import S3Logs as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-action.html
    Properties:
        - Name: Type
        - Name: IncludeResources
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-action.html#cfn-imagebuilder-lifecyclepolicy-action-type""", alias="Type")
    IncludeResources_: Optional['IncludeResources'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-action.html#cfn-imagebuilder-lifecyclepolicy-action-includeresources""", alias="IncludeResources")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.Action:
        from troposphere.imagebuilder import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AmiExclusionRules(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.html
    Properties:
        - Name: IsPublic
        - Name: LastLaunched
        - Name: Regions
        - Name: SharedAccounts
        - Name: TagMap
    
    """
    
    IsPublic_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.html#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-ispublic""", alias="IsPublic")
    LastLaunched_: Optional['LastLaunched'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.html#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-lastlaunched""", alias="LastLaunched")
    Regions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.html#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-regions""", alias="Regions")
    SharedAccounts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.html#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-sharedaccounts""", alias="SharedAccounts")
    TagMap_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.html#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-tagmap""", alias="TagMap")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.AmiExclusionRules:
        from troposphere.imagebuilder import AmiExclusionRules as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExclusionRules(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-exclusionrules.html
    Properties:
        - Name: Amis
        - Name: TagMap
    
    """
    
    Amis_: Optional['AmiExclusionRules'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-exclusionrules.html#cfn-imagebuilder-lifecyclepolicy-exclusionrules-amis""", alias="Amis")
    TagMap_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-exclusionrules.html#cfn-imagebuilder-lifecyclepolicy-exclusionrules-tagmap""", alias="TagMap")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.ExclusionRules:
        from troposphere.imagebuilder import ExclusionRules as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Filter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-filter.html
    Properties:
        - Name: Type
        - Name: Value
        - Name: RetainAtLeast
        - Name: Unit
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-filter.html#cfn-imagebuilder-lifecyclepolicy-filter-type""", alias="Type")
    Value_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-filter.html#cfn-imagebuilder-lifecyclepolicy-filter-value""", alias="Value")
    RetainAtLeast_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-filter.html#cfn-imagebuilder-lifecyclepolicy-filter-retainatleast""", alias="RetainAtLeast")
    Unit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-filter.html#cfn-imagebuilder-lifecyclepolicy-filter-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.Filter:
        from troposphere.imagebuilder import Filter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IncludeResources(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-includeresources.html
    Properties:
        - Name: Containers
        - Name: Amis
        - Name: Snapshots
    
    """
    
    Containers_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-includeresources.html#cfn-imagebuilder-lifecyclepolicy-includeresources-containers""", alias="Containers")
    Amis_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-includeresources.html#cfn-imagebuilder-lifecyclepolicy-includeresources-amis""", alias="Amis")
    Snapshots_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-includeresources.html#cfn-imagebuilder-lifecyclepolicy-includeresources-snapshots""", alias="Snapshots")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.IncludeResources:
        from troposphere.imagebuilder import IncludeResources as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LastLaunched(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-lastlaunched.html
    Properties:
        - Name: Value
        - Name: Unit
    
    """
    
    Value_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-lastlaunched.html#cfn-imagebuilder-lifecyclepolicy-lastlaunched-value""", alias="Value")
    Unit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-lastlaunched.html#cfn-imagebuilder-lifecyclepolicy-lastlaunched-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.LastLaunched:
        from troposphere.imagebuilder import LastLaunched as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PolicyDetail(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-policydetail.html
    Properties:
        - Name: Action
        - Name: ExclusionRules
        - Name: Filter
    
    """
    
    Action_: 'Action' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-policydetail.html#cfn-imagebuilder-lifecyclepolicy-policydetail-action""", alias="Action")
    ExclusionRules_: Optional['ExclusionRules'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-policydetail.html#cfn-imagebuilder-lifecyclepolicy-policydetail-exclusionrules""", alias="ExclusionRules")
    Filter_: 'Filter' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-policydetail.html#cfn-imagebuilder-lifecyclepolicy-policydetail-filter""", alias="Filter")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.PolicyDetail:
        from troposphere.imagebuilder import PolicyDetail as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecipeSelection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-recipeselection.html
    Properties:
        - Name: Name
        - Name: SemanticVersion
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-recipeselection.html#cfn-imagebuilder-lifecyclepolicy-recipeselection-name""", alias="Name")
    SemanticVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-recipeselection.html#cfn-imagebuilder-lifecyclepolicy-recipeselection-semanticversion""", alias="SemanticVersion")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.RecipeSelection:
        from troposphere.imagebuilder import RecipeSelection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceSelection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-resourceselection.html
    Properties:
        - Name: Recipes
        - Name: TagMap
    
    """
    
    Recipes_: Optional[List['RecipeSelection']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-resourceselection.html#cfn-imagebuilder-lifecyclepolicy-resourceselection-recipes""", alias="Recipes")
    TagMap_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-resourceselection.html#cfn-imagebuilder-lifecyclepolicy-resourceselection-tagmap""", alias="TagMap")
    


    @property
    def tropo_type(self) -> troposphere.imagebuilder.ResourceSelection:
        from troposphere.imagebuilder import ResourceSelection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Component(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html
    Properties:
        - Name: Description
        - Name: SupportedOsVersions
        - Name: Platform
        - Name: KmsKeyId
        - Name: Version
        - Name: ChangeDescription
        - Name: Data
        - Name: Uri
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Type
        - Name: Encrypted
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-description""", alias="Description")
    SupportedOsVersions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-supportedosversions""", alias="SupportedOsVersions")
    Platform_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-platform""", alias="Platform")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-kmskeyid""", alias="KmsKeyId")
    Version_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-version""", alias="Version")
    ChangeDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-changedescription""", alias="ChangeDescription")
    Data_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-data""", alias="Data")
    Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-uri""", alias="Uri")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.imagebuilder.Component:
        from troposphere.imagebuilder import Component as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.imagebuilder import Component as TropoT
        return resource_to_troposphere(self, TropoT)


class ContainerRecipe(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html
    Properties:
        - Name: WorkingDirectory
        - Name: ParentImage
        - Name: Description
        - Name: KmsKeyId
        - Name: InstanceConfiguration
        - Name: ContainerType
        - Name: Name
        - Name: DockerfileTemplateData
        - Name: Components
        - Name: TargetRepository
        - Name: Version
        - Name: PlatformOverride
        - Name: ImageOsVersionOverride
        - Name: Tags
        - Name: DockerfileTemplateUri
    Attributes:
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    WorkingDirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-workingdirectory""", alias="WorkingDirectory")
    ParentImage_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-parentimage""", alias="ParentImage")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-description""", alias="Description")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-kmskeyid""", alias="KmsKeyId")
    InstanceConfiguration_: Optional['InstanceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-instanceconfiguration""", alias="InstanceConfiguration")
    ContainerType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-containertype""", alias="ContainerType")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-name""", alias="Name")
    DockerfileTemplateData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-dockerfiletemplatedata""", alias="DockerfileTemplateData")
    Components_: List['ComponentConfiguration'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-components""", alias="Components")
    TargetRepository_: 'TargetContainerRepository' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-targetrepository""", alias="TargetRepository")
    Version_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-version""", alias="Version")
    PlatformOverride_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-platformoverride""", alias="PlatformOverride")
    ImageOsVersionOverride_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-imageosversionoverride""", alias="ImageOsVersionOverride")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-tags""", alias="Tags")
    DockerfileTemplateUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-dockerfiletemplateuri""", alias="DockerfileTemplateUri")
    

    @property
    def tropo_type(self) -> troposphere.imagebuilder.ContainerRecipe:
        from troposphere.imagebuilder import ContainerRecipe as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.imagebuilder import ContainerRecipe as TropoT
        return resource_to_troposphere(self, TropoT)


class DistributionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html
    Properties:
        - Name: Description
        - Name: Tags
        - Name: Name
        - Name: Distributions
    Attributes:
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-description""", alias="Description")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-name""", alias="Name")
    Distributions_: List['Distribution'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-distributions""", alias="Distributions")
    

    @property
    def tropo_type(self) -> troposphere.imagebuilder.DistributionConfiguration:
        from troposphere.imagebuilder import DistributionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.imagebuilder import DistributionConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class Image(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html
    Properties:
        - Name: ImageScanningConfiguration
        - Name: InfrastructureConfigurationArn
        - Name: ImageRecipeArn
        - Name: DistributionConfigurationArn
        - Name: ContainerRecipeArn
        - Name: ImageTestsConfiguration
        - Name: EnhancedImageMetadataEnabled
        - Name: Tags
    Attributes:
        - Name: ImageId
        - Name: ImageUri
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ImageScanningConfiguration_: Optional['ImageScanningConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagescanningconfiguration""", alias="ImageScanningConfiguration")
    InfrastructureConfigurationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-infrastructureconfigurationarn""", alias="InfrastructureConfigurationArn")
    ImageRecipeArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagerecipearn""", alias="ImageRecipeArn")
    DistributionConfigurationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-distributionconfigurationarn""", alias="DistributionConfigurationArn")
    ContainerRecipeArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-containerrecipearn""", alias="ContainerRecipeArn")
    ImageTestsConfiguration_: Optional['ImageTestsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagetestsconfiguration""", alias="ImageTestsConfiguration")
    EnhancedImageMetadataEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-enhancedimagemetadataenabled""", alias="EnhancedImageMetadataEnabled")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.imagebuilder.Image:
        from troposphere.imagebuilder import Image as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.imagebuilder import Image as TropoT
        return resource_to_troposphere(self, TropoT)


class ImagePipeline(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html
    Properties:
        - Name: Status
        - Name: ImageScanningConfiguration
        - Name: InfrastructureConfigurationArn
        - Name: ImageRecipeArn
        - Name: Description
        - Name: DistributionConfigurationArn
        - Name: ContainerRecipeArn
        - Name: Schedule
        - Name: ImageTestsConfiguration
        - Name: EnhancedImageMetadataEnabled
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-status""", alias="Status")
    ImageScanningConfiguration_: Optional['ImageScanningConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagescanningconfiguration""", alias="ImageScanningConfiguration")
    InfrastructureConfigurationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-infrastructureconfigurationarn""", alias="InfrastructureConfigurationArn")
    ImageRecipeArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagerecipearn""", alias="ImageRecipeArn")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-description""", alias="Description")
    DistributionConfigurationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-distributionconfigurationarn""", alias="DistributionConfigurationArn")
    ContainerRecipeArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-containerrecipearn""", alias="ContainerRecipeArn")
    Schedule_: Optional['Schedule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-schedule""", alias="Schedule")
    ImageTestsConfiguration_: Optional['ImageTestsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration""", alias="ImageTestsConfiguration")
    EnhancedImageMetadataEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-enhancedimagemetadataenabled""", alias="EnhancedImageMetadataEnabled")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.imagebuilder.ImagePipeline:
        from troposphere.imagebuilder import ImagePipeline as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.imagebuilder import ImagePipeline as TropoT
        return resource_to_troposphere(self, TropoT)


class ImageRecipe(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html
    Properties:
        - Name: Components
        - Name: WorkingDirectory
        - Name: ParentImage
        - Name: Description
        - Name: Version
        - Name: BlockDeviceMappings
        - Name: AdditionalInstanceConfiguration
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Components_: List['ComponentConfiguration'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-components""", alias="Components")
    WorkingDirectory_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-workingdirectory""", alias="WorkingDirectory")
    ParentImage_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-parentimage""", alias="ParentImage")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-description""", alias="Description")
    Version_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-version""", alias="Version")
    BlockDeviceMappings_: Optional[List['InstanceBlockDeviceMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-blockdevicemappings""", alias="BlockDeviceMappings")
    AdditionalInstanceConfiguration_: Optional['AdditionalInstanceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration""", alias="AdditionalInstanceConfiguration")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.imagebuilder.ImageRecipe:
        from troposphere.imagebuilder import ImageRecipe as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.imagebuilder import ImageRecipe as TropoT
        return resource_to_troposphere(self, TropoT)


class InfrastructureConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html
    Properties:
        - Name: Logging
        - Name: KeyPair
        - Name: Description
        - Name: InstanceProfileName
        - Name: ResourceTags
        - Name: TerminateInstanceOnFailure
        - Name: SubnetId
        - Name: SecurityGroupIds
        - Name: Name
        - Name: InstanceMetadataOptions
        - Name: InstanceTypes
        - Name: SnsTopicArn
        - Name: Tags
    Attributes:
        - Name: Arn
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Logging_: Optional['Logging'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-logging""", alias="Logging")
    KeyPair_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-keypair""", alias="KeyPair")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-description""", alias="Description")
    InstanceProfileName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instanceprofilename""", alias="InstanceProfileName")
    ResourceTags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-resourcetags""", alias="ResourceTags")
    TerminateInstanceOnFailure_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-terminateinstanceonfailure""", alias="TerminateInstanceOnFailure")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-subnetid""", alias="SubnetId")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-securitygroupids""", alias="SecurityGroupIds")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-name""", alias="Name")
    InstanceMetadataOptions_: Optional['InstanceMetadataOptions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions""", alias="InstanceMetadataOptions")
    InstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instancetypes""", alias="InstanceTypes")
    SnsTopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-snstopicarn""", alias="SnsTopicArn")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.imagebuilder.InfrastructureConfiguration:
        from troposphere.imagebuilder import InfrastructureConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.imagebuilder import InfrastructureConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class LifecyclePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html
    Properties:
        - Name: Status
        - Name: Description
        - Name: ResourceType
        - Name: PolicyDetails
        - Name: ExecutionRole
        - Name: ResourceSelection
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-status""", alias="Status")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-description""", alias="Description")
    ResourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-resourcetype""", alias="ResourceType")
    PolicyDetails_: List['PolicyDetail'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-policydetails""", alias="PolicyDetails")
    ExecutionRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-executionrole""", alias="ExecutionRole")
    ResourceSelection_: 'ResourceSelection' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-resourceselection""", alias="ResourceSelection")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.imagebuilder.LifecyclePolicy:
        from troposphere.imagebuilder import LifecyclePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.imagebuilder import LifecyclePolicy as TropoT
        return resource_to_troposphere(self, TropoT)

