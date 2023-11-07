from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ManifestOverridesPayload(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestoverridespayload.html
    Properties:
        - Name: PayloadData
    
    """
    
    PayloadData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestoverridespayload.html#cfn-panorama-applicationinstance-manifestoverridespayload-payloaddata""", alias="PayloadData")
    


    @property
    def tropo_type(self) -> troposphere.panorama.ManifestOverridesPayload:
        from troposphere.panorama import ManifestOverridesPayload as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ManifestPayload(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestpayload.html
    Properties:
        - Name: PayloadData
    
    """
    
    PayloadData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestpayload.html#cfn-panorama-applicationinstance-manifestpayload-payloaddata""", alias="PayloadData")
    


    @property
    def tropo_type(self) -> troposphere.panorama.ManifestPayload:
        from troposphere.panorama import ManifestPayload as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StorageLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html
    Properties:
        - Name: RepoPrefixLocation
        - Name: GeneratedPrefixLocation
        - Name: BinaryPrefixLocation
        - Name: Bucket
        - Name: ManifestPrefixLocation
    
    """
    
    RepoPrefixLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html#cfn-panorama-package-storagelocation-repoprefixlocation""", alias="RepoPrefixLocation")
    GeneratedPrefixLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html#cfn-panorama-package-storagelocation-generatedprefixlocation""", alias="GeneratedPrefixLocation")
    BinaryPrefixLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html#cfn-panorama-package-storagelocation-binaryprefixlocation""", alias="BinaryPrefixLocation")
    Bucket_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html#cfn-panorama-package-storagelocation-bucket""", alias="Bucket")
    ManifestPrefixLocation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html#cfn-panorama-package-storagelocation-manifestprefixlocation""", alias="ManifestPrefixLocation")
    


    @property
    def tropo_type(self) -> troposphere.panorama.StorageLocation:
        from troposphere.panorama import StorageLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ApplicationInstance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html
    Properties:
        - Name: DefaultRuntimeContextDevice
        - Name: Description
        - Name: ApplicationInstanceIdToReplace
        - Name: ManifestOverridesPayload
        - Name: RuntimeRoleArn
        - Name: ManifestPayload
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: DefaultRuntimeContextDeviceName
        - Name: Status
        - Name: ApplicationInstanceId
        - Name: CreatedTime
        - Name: StatusDescription
        - Name: HealthStatus
        - Name: LastUpdatedTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DefaultRuntimeContextDevice_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-defaultruntimecontextdevice""", alias="DefaultRuntimeContextDevice")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-description""", alias="Description")
    ApplicationInstanceIdToReplace_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-applicationinstanceidtoreplace""", alias="ApplicationInstanceIdToReplace")
    ManifestOverridesPayload_: Optional['ManifestOverridesPayload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-manifestoverridespayload""", alias="ManifestOverridesPayload")
    RuntimeRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-runtimerolearn""", alias="RuntimeRoleArn")
    ManifestPayload_: 'ManifestPayload' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-manifestpayload""", alias="ManifestPayload")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.panorama.ApplicationInstance:
        from troposphere.panorama import ApplicationInstance as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.panorama import ApplicationInstance as TropoT
        return resource_to_troposphere(self, TropoT)


class Package(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html
    Properties:
        - Name: PackageName
        - Name: StorageLocation
        - Name: Tags
    Attributes:
        - Name: CreatedTime
        - Name: StorageLocation.ManifestPrefixLocation
        - Name: StorageLocation.GeneratedPrefixLocation
        - Name: StorageLocation.BinaryPrefixLocation
        - Name: PackageId
        - Name: Arn
        - Name: StorageLocation.Bucket
        - Name: StorageLocation.RepoPrefixLocation
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PackageName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html#cfn-panorama-package-packagename""", alias="PackageName")
    StorageLocation_: Optional['StorageLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html#cfn-panorama-package-storagelocation""", alias="StorageLocation")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html#cfn-panorama-package-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.panorama.Package:
        from troposphere.panorama import Package as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.panorama import Package as TropoT
        return resource_to_troposphere(self, TropoT)


class PackageVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html
    Properties:
        - Name: UpdatedLatestPatchVersion
        - Name: PatchVersion
        - Name: MarkLatest
        - Name: PackageId
        - Name: OwnerAccount
        - Name: PackageVersion
    Attributes:
        - Name: Status
        - Name: PackageName
        - Name: StatusDescription
        - Name: PackageArn
        - Name: IsLatestPatch
        - Name: RegisteredTime
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UpdatedLatestPatchVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-updatedlatestpatchversion""", alias="UpdatedLatestPatchVersion")
    PatchVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-patchversion""", alias="PatchVersion")
    MarkLatest_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-marklatest""", alias="MarkLatest")
    PackageId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-packageid""", alias="PackageId")
    OwnerAccount_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-owneraccount""", alias="OwnerAccount")
    PackageVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-packageversion""", alias="PackageVersion")
    

    @property
    def tropo_type(self) -> troposphere.panorama.PackageVersion:
        from troposphere.panorama import PackageVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.panorama import PackageVersion as TropoT
        return resource_to_troposphere(self, TropoT)

