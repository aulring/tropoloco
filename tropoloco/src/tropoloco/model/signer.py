from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class SignatureValidityPeriod(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-signer-signingprofile-signaturevalidityperiod.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-signer-signingprofile-signaturevalidityperiod.html#cfn-signer-signingprofile-signaturevalidityperiod-type""", alias="Type")
    Value_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-signer-signingprofile-signaturevalidityperiod.html#cfn-signer-signingprofile-signaturevalidityperiod-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.signer.SignatureValidityPeriod:
        from troposphere.signer import SignatureValidityPeriod as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ProfilePermission(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html
    Properties:
        - Name: Action
        - Name: StatementId
        - Name: ProfileName
        - Name: Principal
        - Name: ProfileVersion
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-action""", alias="Action")
    StatementId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-statementid""", alias="StatementId")
    ProfileName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-profilename""", alias="ProfileName")
    Principal_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-principal""", alias="Principal")
    ProfileVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-profileversion""", alias="ProfileVersion")
    

    @property
    def tropo_type(self) -> troposphere.signer.ProfilePermission:
        from troposphere.signer import ProfilePermission as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.signer import ProfilePermission as TropoT
        return resource_to_troposphere(self, TropoT)


class SigningProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html
    Properties:
        - Name: SignatureValidityPeriod
        - Name: PlatformId
        - Name: Tags
    Attributes:
        - Name: ProfileVersionArn
        - Name: ProfileName
        - Name: Arn
        - Name: ProfileVersion
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SignatureValidityPeriod_: Optional['SignatureValidityPeriod'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html#cfn-signer-signingprofile-signaturevalidityperiod""", alias="SignatureValidityPeriod")
    PlatformId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html#cfn-signer-signingprofile-platformid""", alias="PlatformId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html#cfn-signer-signingprofile-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.signer.SigningProfile:
        from troposphere.signer import SigningProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.signer import SigningProfile as TropoT
        return resource_to_troposphere(self, TropoT)

