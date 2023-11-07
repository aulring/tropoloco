from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CreatedAt(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-createdat.html
    Properties:
        - Name: Nanos
        - Name: Seconds
    
    """
    
    Nanos_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-createdat.html#cfn-healthlake-fhirdatastore-createdat-nanos""", alias="Nanos")
    Seconds_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-createdat.html#cfn-healthlake-fhirdatastore-createdat-seconds""", alias="Seconds")
    


    @property
    def tropo_type(self) -> troposphere.healthlake.CreatedAt:
        from troposphere.healthlake import CreatedAt as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IdentityProviderConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html
    Properties:
        - Name: AuthorizationStrategy
        - Name: IdpLambdaArn
        - Name: FineGrainedAuthorizationEnabled
        - Name: Metadata
    
    """
    
    AuthorizationStrategy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration-authorizationstrategy""", alias="AuthorizationStrategy")
    IdpLambdaArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration-idplambdaarn""", alias="IdpLambdaArn")
    FineGrainedAuthorizationEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration-finegrainedauthorizationenabled""", alias="FineGrainedAuthorizationEnabled")
    Metadata_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration-metadata""", alias="Metadata")
    


    @property
    def tropo_type(self) -> troposphere.healthlake.IdentityProviderConfiguration:
        from troposphere.healthlake import IdentityProviderConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KmsEncryptionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html
    Properties:
        - Name: KmsKeyId
        - Name: CmkType
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html#cfn-healthlake-fhirdatastore-kmsencryptionconfig-kmskeyid""", alias="KmsKeyId")
    CmkType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html#cfn-healthlake-fhirdatastore-kmsencryptionconfig-cmktype""", alias="CmkType")
    


    @property
    def tropo_type(self) -> troposphere.healthlake.KmsEncryptionConfig:
        from troposphere.healthlake import KmsEncryptionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PreloadDataConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html
    Properties:
        - Name: PreloadDataType
    
    """
    
    PreloadDataType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html#cfn-healthlake-fhirdatastore-preloaddataconfig-preloaddatatype""", alias="PreloadDataType")
    


    @property
    def tropo_type(self) -> troposphere.healthlake.PreloadDataConfig:
        from troposphere.healthlake import PreloadDataConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SseConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html
    Properties:
        - Name: KmsEncryptionConfig
    
    """
    
    KmsEncryptionConfig_: 'KmsEncryptionConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html#cfn-healthlake-fhirdatastore-sseconfiguration-kmsencryptionconfig""", alias="KmsEncryptionConfig")
    


    @property
    def tropo_type(self) -> troposphere.healthlake.SseConfiguration:
        from troposphere.healthlake import SseConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class FHIRDatastore(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html
    Properties:
        - Name: DatastoreTypeVersion
        - Name: DatastoreName
        - Name: IdentityProviderConfiguration
        - Name: Tags
        - Name: PreloadDataConfig
        - Name: SseConfiguration
    Attributes:
        - Name: DatastoreArn
        - Name: CreatedAt.Nanos
        - Name: DatastoreId
        - Name: CreatedAt
        - Name: DatastoreStatus
        - Name: DatastoreEndpoint
        - Name: CreatedAt.Seconds
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DatastoreTypeVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastoretypeversion""", alias="DatastoreTypeVersion")
    DatastoreName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastorename""", alias="DatastoreName")
    IdentityProviderConfiguration_: Optional['IdentityProviderConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration""", alias="IdentityProviderConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-tags""", alias="Tags")
    PreloadDataConfig_: Optional['PreloadDataConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-preloaddataconfig""", alias="PreloadDataConfig")
    SseConfiguration_: Optional['SseConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-sseconfiguration""", alias="SseConfiguration")
    

    @property
    def tropo_type(self) -> troposphere.healthlake.FHIRDatastore:
        from troposphere.healthlake import FHIRDatastore as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.healthlake import FHIRDatastore as TropoT
        return resource_to_troposphere(self, TropoT)

