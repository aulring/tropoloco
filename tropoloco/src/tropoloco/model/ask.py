from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AuthenticationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html
    Properties:
        - Name: RefreshToken
        - Name: ClientSecret
        - Name: ClientId
    
    """
    
    RefreshToken_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html#cfn-ask-skill-authenticationconfiguration-refreshtoken""", alias="RefreshToken")
    ClientSecret_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html#cfn-ask-skill-authenticationconfiguration-clientsecret""", alias="ClientSecret")
    ClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html#cfn-ask-skill-authenticationconfiguration-clientid""", alias="ClientId")
    


    @property
    def tropo_type(self) -> troposphere.ask.AuthenticationConfiguration:
        from troposphere.ask import AuthenticationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Overrides(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-overrides.html
    Properties:
        - Name: Manifest
    
    """
    
    Manifest_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-overrides.html#cfn-ask-skill-overrides-manifest""", alias="Manifest")
    


    @property
    def tropo_type(self) -> troposphere.ask.Overrides:
        from troposphere.ask import Overrides as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SkillPackage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html
    Properties:
        - Name: S3BucketRole
        - Name: S3ObjectVersion
        - Name: S3Bucket
        - Name: S3Key
        - Name: Overrides
    
    """
    
    S3BucketRole_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3bucketrole""", alias="S3BucketRole")
    S3ObjectVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3objectversion""", alias="S3ObjectVersion")
    S3Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3bucket""", alias="S3Bucket")
    S3Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3key""", alias="S3Key")
    Overrides_: Optional['Overrides'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-overrides""", alias="Overrides")
    


    @property
    def tropo_type(self) -> troposphere.ask.SkillPackage:
        from troposphere.ask import SkillPackage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Skill(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html
    Properties:
        - Name: AuthenticationConfiguration
        - Name: VendorId
        - Name: SkillPackage
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AuthenticationConfiguration_: 'AuthenticationConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-authenticationconfiguration""", alias="AuthenticationConfiguration")
    VendorId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-vendorid""", alias="VendorId")
    SkillPackage_: 'SkillPackage' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-skillpackage""", alias="SkillPackage")
    

    @property
    def tropo_type(self) -> troposphere.ask.Skill:
        from troposphere.ask import Skill as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ask import Skill as TropoT
        return resource_to_troposphere(self, TropoT)

