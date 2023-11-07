from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################




######################################################################
# AWS Resource
######################################################################


class Alias(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html
    Properties:
        - Name: TargetKeyId
        - Name: AliasName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TargetKeyId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html#cfn-kms-alias-targetkeyid""", alias="TargetKeyId")
    AliasName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html#cfn-kms-alias-aliasname""", alias="AliasName")
    

    @property
    def tropo_type(self) -> troposphere.kms.Alias:
        from troposphere.kms import Alias as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kms import Alias as TropoT
        return resource_to_troposphere(self, TropoT)


class Key(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html
    Properties:
        - Name: Origin
        - Name: MultiRegion
        - Name: Description
        - Name: PendingWindowInDays
        - Name: BypassPolicyLockoutSafetyCheck
        - Name: KeyPolicy
        - Name: KeySpec
        - Name: Enabled
        - Name: KeyUsage
        - Name: EnableKeyRotation
        - Name: Tags
    Attributes:
        - Name: KeyId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Origin_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-origin""", alias="Origin")
    MultiRegion_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-multiregion""", alias="MultiRegion")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-description""", alias="Description")
    PendingWindowInDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-pendingwindowindays""", alias="PendingWindowInDays")
    BypassPolicyLockoutSafetyCheck_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-bypasspolicylockoutsafetycheck""", alias="BypassPolicyLockoutSafetyCheck")
    KeyPolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keypolicy""", alias="KeyPolicy")
    KeySpec_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyspec""", alias="KeySpec")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enabled""", alias="Enabled")
    KeyUsage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyusage""", alias="KeyUsage")
    EnableKeyRotation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enablekeyrotation""", alias="EnableKeyRotation")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.kms.Key:
        from troposphere.kms import Key as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kms import Key as TropoT
        return resource_to_troposphere(self, TropoT)


class ReplicaKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html
    Properties:
        - Name: Description
        - Name: PendingWindowInDays
        - Name: KeyPolicy
        - Name: PrimaryKeyArn
        - Name: Enabled
        - Name: Tags
    Attributes:
        - Name: KeyId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html#cfn-kms-replicakey-description""", alias="Description")
    PendingWindowInDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html#cfn-kms-replicakey-pendingwindowindays""", alias="PendingWindowInDays")
    KeyPolicy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html#cfn-kms-replicakey-keypolicy""", alias="KeyPolicy")
    PrimaryKeyArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html#cfn-kms-replicakey-primarykeyarn""", alias="PrimaryKeyArn")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html#cfn-kms-replicakey-enabled""", alias="Enabled")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html#cfn-kms-replicakey-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.kms.ReplicaKey:
        from troposphere.kms import ReplicaKey as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.kms import ReplicaKey as TropoT
        return resource_to_troposphere(self, TropoT)

