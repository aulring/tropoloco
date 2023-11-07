from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Definition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-application-definition.html
    Properties:
        - Name: Content
        - Name: S3Location
    
    """
    
    Content_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-application-definition.html#cfn-m2-application-definition-content""", alias="Content")
    S3Location_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-application-definition.html#cfn-m2-application-definition-s3location""", alias="S3Location")
    


    @property
    def tropo_type(self) -> troposphere.m2.Definition:
        from troposphere.m2 import Definition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EfsStorageConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-efsstorageconfiguration.html
    Properties:
        - Name: MountPoint
        - Name: FileSystemId
    
    """
    
    MountPoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-efsstorageconfiguration.html#cfn-m2-environment-efsstorageconfiguration-mountpoint""", alias="MountPoint")
    FileSystemId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-efsstorageconfiguration.html#cfn-m2-environment-efsstorageconfiguration-filesystemid""", alias="FileSystemId")
    


    @property
    def tropo_type(self) -> troposphere.m2.EfsStorageConfiguration:
        from troposphere.m2 import EfsStorageConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FsxStorageConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-fsxstorageconfiguration.html
    Properties:
        - Name: MountPoint
        - Name: FileSystemId
    
    """
    
    MountPoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-fsxstorageconfiguration.html#cfn-m2-environment-fsxstorageconfiguration-mountpoint""", alias="MountPoint")
    FileSystemId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-fsxstorageconfiguration.html#cfn-m2-environment-fsxstorageconfiguration-filesystemid""", alias="FileSystemId")
    


    @property
    def tropo_type(self) -> troposphere.m2.FsxStorageConfiguration:
        from troposphere.m2 import FsxStorageConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HighAvailabilityConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-highavailabilityconfig.html
    Properties:
        - Name: DesiredCapacity
    
    """
    
    DesiredCapacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-highavailabilityconfig.html#cfn-m2-environment-highavailabilityconfig-desiredcapacity""", alias="DesiredCapacity")
    


    @property
    def tropo_type(self) -> troposphere.m2.HighAvailabilityConfig:
        from troposphere.m2 import HighAvailabilityConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StorageConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-storageconfiguration.html
    Properties:
        - Name: Efs
        - Name: Fsx
    
    """
    
    Efs_: Optional['EfsStorageConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-storageconfiguration.html#cfn-m2-environment-storageconfiguration-efs""", alias="Efs")
    Fsx_: Optional['FsxStorageConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-storageconfiguration.html#cfn-m2-environment-storageconfiguration-fsx""", alias="Fsx")
    


    @property
    def tropo_type(self) -> troposphere.m2.StorageConfiguration:
        from troposphere.m2 import StorageConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Application(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html
    Properties:
        - Name: Description
        - Name: KmsKeyId
        - Name: Definition
        - Name: EngineType
        - Name: RoleArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ApplicationArn
        - Name: ApplicationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-description""", alias="Description")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-kmskeyid""", alias="KmsKeyId")
    Definition_: 'Definition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-definition""", alias="Definition")
    EngineType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-enginetype""", alias="EngineType")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-rolearn""", alias="RoleArn")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.m2.Application:
        from troposphere.m2 import Application as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.m2 import Application as TropoT
        return resource_to_troposphere(self, TropoT)


class Environment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html
    Properties:
        - Name: Description
        - Name: EngineVersion
        - Name: KmsKeyId
        - Name: HighAvailabilityConfig
        - Name: PreferredMaintenanceWindow
        - Name: SecurityGroupIds
        - Name: SubnetIds
        - Name: Name
        - Name: EngineType
        - Name: PubliclyAccessible
        - Name: InstanceType
        - Name: StorageConfigurations
        - Name: Tags
    Attributes:
        - Name: EnvironmentId
        - Name: EnvironmentArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-description""", alias="Description")
    EngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-engineversion""", alias="EngineVersion")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-kmskeyid""", alias="KmsKeyId")
    HighAvailabilityConfig_: Optional['HighAvailabilityConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-highavailabilityconfig""", alias="HighAvailabilityConfig")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-subnetids""", alias="SubnetIds")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-name""", alias="Name")
    EngineType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-enginetype""", alias="EngineType")
    PubliclyAccessible_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-publiclyaccessible""", alias="PubliclyAccessible")
    InstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-instancetype""", alias="InstanceType")
    StorageConfigurations_: Optional[List['StorageConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-storageconfigurations""", alias="StorageConfigurations")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.m2.Environment:
        from troposphere.m2 import Environment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.m2 import Environment as TropoT
        return resource_to_troposphere(self, TropoT)

