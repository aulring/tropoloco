from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AttributeMapItems(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-attributemapitems.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-attributemapitems.html#cfn-finspace-environment-attributemapitems-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-attributemapitems.html#cfn-finspace-environment-attributemapitems-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.finspace.AttributeMapItems:
        from troposphere.finspace import AttributeMapItems as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FederationParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html
    Properties:
        - Name: AttributeMap
        - Name: FederationProviderName
        - Name: SamlMetadataURL
        - Name: FederationURN
        - Name: SamlMetadataDocument
        - Name: ApplicationCallBackURL
    
    """
    
    AttributeMap_: Optional[List['AttributeMapItems']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-attributemap""", alias="AttributeMap")
    FederationProviderName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-federationprovidername""", alias="FederationProviderName")
    SamlMetadataURL_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-samlmetadataurl""", alias="SamlMetadataURL")
    FederationURN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-federationurn""", alias="FederationURN")
    SamlMetadataDocument_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-samlmetadatadocument""", alias="SamlMetadataDocument")
    ApplicationCallBackURL_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-applicationcallbackurl""", alias="ApplicationCallBackURL")
    


    @property
    def tropo_type(self) -> troposphere.finspace.FederationParameters:
        from troposphere.finspace import FederationParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SuperuserParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html
    Properties:
        - Name: FirstName
        - Name: LastName
        - Name: EmailAddress
    
    """
    
    FirstName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html#cfn-finspace-environment-superuserparameters-firstname""", alias="FirstName")
    LastName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html#cfn-finspace-environment-superuserparameters-lastname""", alias="LastName")
    EmailAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html#cfn-finspace-environment-superuserparameters-emailaddress""", alias="EmailAddress")
    


    @property
    def tropo_type(self) -> troposphere.finspace.SuperuserParameters:
        from troposphere.finspace import SuperuserParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Environment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html
    Properties:
        - Name: Description
        - Name: KmsKeyId
        - Name: FederationParameters
        - Name: FederationMode
        - Name: SuperuserParameters
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: EnvironmentId
        - Name: EnvironmentArn
        - Name: SageMakerStudioDomainUrl
        - Name: EnvironmentUrl
        - Name: AwsAccountId
        - Name: DedicatedServiceAccountId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-description""", alias="Description")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-kmskeyid""", alias="KmsKeyId")
    FederationParameters_: Optional['FederationParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-federationparameters""", alias="FederationParameters")
    FederationMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-federationmode""", alias="FederationMode")
    SuperuserParameters_: Optional['SuperuserParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-superuserparameters""", alias="SuperuserParameters")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.finspace.Environment:
        from troposphere.finspace import Environment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.finspace import Environment as TropoT
        return resource_to_troposphere(self, TropoT)

