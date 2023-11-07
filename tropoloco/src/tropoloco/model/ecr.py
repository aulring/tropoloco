from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class RepositoryCatalogData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-publicrepository-repositorycatalogdata.html
    Properties:
        - Name: AboutText
        - Name: OperatingSystems
        - Name: UsageText
        - Name: RepositoryDescription
        - Name: Architectures
    
    """
    
    AboutText_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-publicrepository-repositorycatalogdata.html#cfn-ecr-publicrepository-repositorycatalogdata-abouttext""", alias="AboutText")
    OperatingSystems_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-publicrepository-repositorycatalogdata.html#cfn-ecr-publicrepository-repositorycatalogdata-operatingsystems""", alias="OperatingSystems")
    UsageText_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-publicrepository-repositorycatalogdata.html#cfn-ecr-publicrepository-repositorycatalogdata-usagetext""", alias="UsageText")
    RepositoryDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-publicrepository-repositorycatalogdata.html#cfn-ecr-publicrepository-repositorycatalogdata-repositorydescription""", alias="RepositoryDescription")
    Architectures_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-publicrepository-repositorycatalogdata.html#cfn-ecr-publicrepository-repositorycatalogdata-architectures""", alias="Architectures")
    


    @property
    def tropo_type(self) -> troposphere.ecr.RepositoryCatalogData:
        from troposphere.ecr import RepositoryCatalogData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationConfigurationProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationconfiguration.html
    Properties:
        - Name: Rules
    
    """
    
    Rules_: List['ReplicationRule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationconfiguration.html#cfn-ecr-replicationconfiguration-replicationconfiguration-rules""", alias="Rules")
    


    @property
    def tropo_type(self) -> troposphere.ecr.ReplicationConfigurationProperty:
        from troposphere.ecr import ReplicationConfigurationProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationdestination.html
    Properties:
        - Name: Region
        - Name: RegistryId
    
    """
    
    Region_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationdestination.html#cfn-ecr-replicationconfiguration-replicationdestination-region""", alias="Region")
    RegistryId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationdestination.html#cfn-ecr-replicationconfiguration-replicationdestination-registryid""", alias="RegistryId")
    


    @property
    def tropo_type(self) -> troposphere.ecr.ReplicationDestination:
        from troposphere.ecr import ReplicationDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationrule.html
    Properties:
        - Name: RepositoryFilters
        - Name: Destinations
    
    """
    
    RepositoryFilters_: Optional[List['RepositoryFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationrule.html#cfn-ecr-replicationconfiguration-replicationrule-repositoryfilters""", alias="RepositoryFilters")
    Destinations_: List['ReplicationDestination'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationrule.html#cfn-ecr-replicationconfiguration-replicationrule-destinations""", alias="Destinations")
    


    @property
    def tropo_type(self) -> troposphere.ecr.ReplicationRule:
        from troposphere.ecr import ReplicationRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RepositoryFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-repositoryfilter.html
    Properties:
        - Name: FilterType
        - Name: Filter
    
    """
    
    FilterType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-repositoryfilter.html#cfn-ecr-replicationconfiguration-repositoryfilter-filtertype""", alias="FilterType")
    Filter_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-repositoryfilter.html#cfn-ecr-replicationconfiguration-repositoryfilter-filter""", alias="Filter")
    


    @property
    def tropo_type(self) -> troposphere.ecr.RepositoryFilter:
        from troposphere.ecr import RepositoryFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-encryptionconfiguration.html
    Properties:
        - Name: EncryptionType
        - Name: KmsKey
    
    """
    
    EncryptionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-encryptionconfiguration.html#cfn-ecr-repository-encryptionconfiguration-encryptiontype""", alias="EncryptionType")
    KmsKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-encryptionconfiguration.html#cfn-ecr-repository-encryptionconfiguration-kmskey""", alias="KmsKey")
    


    @property
    def tropo_type(self) -> troposphere.ecr.EncryptionConfiguration:
        from troposphere.ecr import EncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImageScanningConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-imagescanningconfiguration.html
    Properties:
        - Name: ScanOnPush
    
    """
    
    ScanOnPush_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-imagescanningconfiguration.html#cfn-ecr-repository-imagescanningconfiguration-scanonpush""", alias="ScanOnPush")
    


    @property
    def tropo_type(self) -> troposphere.ecr.ImageScanningConfiguration:
        from troposphere.ecr import ImageScanningConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LifecyclePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html
    Properties:
        - Name: LifecyclePolicyText
        - Name: RegistryId
    
    """
    
    LifecyclePolicyText_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html#cfn-ecr-repository-lifecyclepolicy-lifecyclepolicytext""", alias="LifecyclePolicyText")
    RegistryId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html#cfn-ecr-repository-lifecyclepolicy-registryid""", alias="RegistryId")
    


    @property
    def tropo_type(self) -> troposphere.ecr.LifecyclePolicy:
        from troposphere.ecr import LifecyclePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class PublicRepository(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-publicrepository.html
    Properties:
        - Name: RepositoryPolicyText
        - Name: RepositoryName
        - Name: RepositoryCatalogData
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RepositoryPolicyText_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-publicrepository.html#cfn-ecr-publicrepository-repositorypolicytext""", alias="RepositoryPolicyText")
    RepositoryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-publicrepository.html#cfn-ecr-publicrepository-repositoryname""", alias="RepositoryName")
    RepositoryCatalogData_: Optional['RepositoryCatalogData'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-publicrepository.html#cfn-ecr-publicrepository-repositorycatalogdata""", alias="RepositoryCatalogData")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-publicrepository.html#cfn-ecr-publicrepository-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ecr.PublicRepository:
        from troposphere.ecr import PublicRepository as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ecr import PublicRepository as TropoT
        return resource_to_troposphere(self, TropoT)


class PullThroughCacheRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-pullthroughcacherule.html
    Properties:
        - Name: UpstreamRegistryUrl
        - Name: EcrRepositoryPrefix
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UpstreamRegistryUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-pullthroughcacherule.html#cfn-ecr-pullthroughcacherule-upstreamregistryurl""", alias="UpstreamRegistryUrl")
    EcrRepositoryPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-pullthroughcacherule.html#cfn-ecr-pullthroughcacherule-ecrrepositoryprefix""", alias="EcrRepositoryPrefix")
    

    @property
    def tropo_type(self) -> troposphere.ecr.PullThroughCacheRule:
        from troposphere.ecr import PullThroughCacheRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ecr import PullThroughCacheRule as TropoT
        return resource_to_troposphere(self, TropoT)


class RegistryPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-registrypolicy.html
    Properties:
        - Name: PolicyText
    Attributes:
        - Name: RegistryId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PolicyText_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-registrypolicy.html#cfn-ecr-registrypolicy-policytext""", alias="PolicyText")
    

    @property
    def tropo_type(self) -> troposphere.ecr.RegistryPolicy:
        from troposphere.ecr import RegistryPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ecr import RegistryPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class ReplicationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-replicationconfiguration.html
    Properties:
        - Name: ReplicationConfiguration
    Attributes:
        - Name: RegistryId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ReplicationConfiguration_: 'ReplicationConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-replicationconfiguration.html#cfn-ecr-replicationconfiguration-replicationconfiguration""", alias="ReplicationConfiguration")
    

    @property
    def tropo_type(self) -> troposphere.ecr.ReplicationConfiguration:
        from troposphere.ecr import ReplicationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ecr import ReplicationConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class Repository(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html
    Properties:
        - Name: EmptyOnDelete
        - Name: ImageScanningConfiguration
        - Name: EncryptionConfiguration
        - Name: RepositoryPolicyText
        - Name: LifecyclePolicy
        - Name: RepositoryName
        - Name: Tags
        - Name: ImageTagMutability
    Attributes:
        - Name: RepositoryUri
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EmptyOnDelete_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-emptyondelete""", alias="EmptyOnDelete")
    ImageScanningConfiguration_: Optional['ImageScanningConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-imagescanningconfiguration""", alias="ImageScanningConfiguration")
    EncryptionConfiguration_: Optional['EncryptionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-encryptionconfiguration""", alias="EncryptionConfiguration")
    RepositoryPolicyText_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-repositorypolicytext""", alias="RepositoryPolicyText")
    LifecyclePolicy_: Optional['LifecyclePolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-lifecyclepolicy""", alias="LifecyclePolicy")
    RepositoryName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-repositoryname""", alias="RepositoryName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-tags""", alias="Tags")
    ImageTagMutability_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-imagetagmutability""", alias="ImageTagMutability")
    

    @property
    def tropo_type(self) -> troposphere.ecr.Repository:
        from troposphere.ecr import Repository as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ecr import Repository as TropoT
        return resource_to_troposphere(self, TropoT)

