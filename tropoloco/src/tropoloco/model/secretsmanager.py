from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class HostedRotationLambda(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html
    Properties:
        - Name: Runtime
        - Name: RotationType
        - Name: RotationLambdaName
        - Name: KmsKeyArn
        - Name: MasterSecretArn
        - Name: VpcSecurityGroupIds
        - Name: ExcludeCharacters
        - Name: MasterSecretKmsKeyArn
        - Name: SuperuserSecretArn
        - Name: SuperuserSecretKmsKeyArn
        - Name: VpcSubnetIds
    
    """
    
    Runtime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html#cfn-secretsmanager-rotationschedule-hostedrotationlambda-runtime""", alias="Runtime")
    RotationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html#cfn-secretsmanager-rotationschedule-hostedrotationlambda-rotationtype""", alias="RotationType")
    RotationLambdaName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html#cfn-secretsmanager-rotationschedule-hostedrotationlambda-rotationlambdaname""", alias="RotationLambdaName")
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html#cfn-secretsmanager-rotationschedule-hostedrotationlambda-kmskeyarn""", alias="KmsKeyArn")
    MasterSecretArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html#cfn-secretsmanager-rotationschedule-hostedrotationlambda-mastersecretarn""", alias="MasterSecretArn")
    VpcSecurityGroupIds_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html#cfn-secretsmanager-rotationschedule-hostedrotationlambda-vpcsecuritygroupids""", alias="VpcSecurityGroupIds")
    ExcludeCharacters_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html#cfn-secretsmanager-rotationschedule-hostedrotationlambda-excludecharacters""", alias="ExcludeCharacters")
    MasterSecretKmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html#cfn-secretsmanager-rotationschedule-hostedrotationlambda-mastersecretkmskeyarn""", alias="MasterSecretKmsKeyArn")
    SuperuserSecretArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html#cfn-secretsmanager-rotationschedule-hostedrotationlambda-superusersecretarn""", alias="SuperuserSecretArn")
    SuperuserSecretKmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html#cfn-secretsmanager-rotationschedule-hostedrotationlambda-superusersecretkmskeyarn""", alias="SuperuserSecretKmsKeyArn")
    VpcSubnetIds_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html#cfn-secretsmanager-rotationschedule-hostedrotationlambda-vpcsubnetids""", alias="VpcSubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.secretsmanager.HostedRotationLambda:
        from troposphere.secretsmanager import HostedRotationLambda as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RotationRules(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-rotationrules.html
    Properties:
        - Name: ScheduleExpression
        - Name: Duration
        - Name: AutomaticallyAfterDays
    
    """
    
    ScheduleExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-rotationrules.html#cfn-secretsmanager-rotationschedule-rotationrules-scheduleexpression""", alias="ScheduleExpression")
    Duration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-rotationrules.html#cfn-secretsmanager-rotationschedule-rotationrules-duration""", alias="Duration")
    AutomaticallyAfterDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-rotationrules.html#cfn-secretsmanager-rotationschedule-rotationrules-automaticallyafterdays""", alias="AutomaticallyAfterDays")
    


    @property
    def tropo_type(self) -> troposphere.secretsmanager.RotationRules:
        from troposphere.secretsmanager import RotationRules as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GenerateSecretString(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html
    Properties:
        - Name: ExcludeUppercase
        - Name: RequireEachIncludedType
        - Name: IncludeSpace
        - Name: ExcludeCharacters
        - Name: GenerateStringKey
        - Name: PasswordLength
        - Name: ExcludePunctuation
        - Name: ExcludeLowercase
        - Name: SecretStringTemplate
        - Name: ExcludeNumbers
    
    """
    
    ExcludeUppercase_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html#cfn-secretsmanager-secret-generatesecretstring-excludeuppercase""", alias="ExcludeUppercase")
    RequireEachIncludedType_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html#cfn-secretsmanager-secret-generatesecretstring-requireeachincludedtype""", alias="RequireEachIncludedType")
    IncludeSpace_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html#cfn-secretsmanager-secret-generatesecretstring-includespace""", alias="IncludeSpace")
    ExcludeCharacters_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html#cfn-secretsmanager-secret-generatesecretstring-excludecharacters""", alias="ExcludeCharacters")
    GenerateStringKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html#cfn-secretsmanager-secret-generatesecretstring-generatestringkey""", alias="GenerateStringKey")
    PasswordLength_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html#cfn-secretsmanager-secret-generatesecretstring-passwordlength""", alias="PasswordLength")
    ExcludePunctuation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html#cfn-secretsmanager-secret-generatesecretstring-excludepunctuation""", alias="ExcludePunctuation")
    ExcludeLowercase_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html#cfn-secretsmanager-secret-generatesecretstring-excludelowercase""", alias="ExcludeLowercase")
    SecretStringTemplate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html#cfn-secretsmanager-secret-generatesecretstring-secretstringtemplate""", alias="SecretStringTemplate")
    ExcludeNumbers_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html#cfn-secretsmanager-secret-generatesecretstring-excludenumbers""", alias="ExcludeNumbers")
    


    @property
    def tropo_type(self) -> troposphere.secretsmanager.GenerateSecretString:
        from troposphere.secretsmanager import GenerateSecretString as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicaRegion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-replicaregion.html
    Properties:
        - Name: KmsKeyId
        - Name: Region
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-replicaregion.html#cfn-secretsmanager-secret-replicaregion-kmskeyid""", alias="KmsKeyId")
    Region_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-replicaregion.html#cfn-secretsmanager-secret-replicaregion-region""", alias="Region")
    


    @property
    def tropo_type(self) -> troposphere.secretsmanager.ReplicaRegion:
        from troposphere.secretsmanager import ReplicaRegion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ResourcePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-resourcepolicy.html
    Properties:
        - Name: BlockPublicPolicy
        - Name: SecretId
        - Name: ResourcePolicy
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BlockPublicPolicy_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-resourcepolicy.html#cfn-secretsmanager-resourcepolicy-blockpublicpolicy""", alias="BlockPublicPolicy")
    SecretId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-resourcepolicy.html#cfn-secretsmanager-resourcepolicy-secretid""", alias="SecretId")
    ResourcePolicy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-resourcepolicy.html#cfn-secretsmanager-resourcepolicy-resourcepolicy""", alias="ResourcePolicy")
    

    @property
    def tropo_type(self) -> troposphere.secretsmanager.ResourcePolicy:
        from troposphere.secretsmanager import ResourcePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.secretsmanager import ResourcePolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class RotationSchedule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html
    Properties:
        - Name: SecretId
        - Name: HostedRotationLambda
        - Name: RotationLambdaARN
        - Name: RotationRules
        - Name: RotateImmediatelyOnUpdate
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SecretId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html#cfn-secretsmanager-rotationschedule-secretid""", alias="SecretId")
    HostedRotationLambda_: Optional['HostedRotationLambda'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html#cfn-secretsmanager-rotationschedule-hostedrotationlambda""", alias="HostedRotationLambda")
    RotationLambdaARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html#cfn-secretsmanager-rotationschedule-rotationlambdaarn""", alias="RotationLambdaARN")
    RotationRules_: Optional['RotationRules'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html#cfn-secretsmanager-rotationschedule-rotationrules""", alias="RotationRules")
    RotateImmediatelyOnUpdate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html#cfn-secretsmanager-rotationschedule-rotateimmediatelyonupdate""", alias="RotateImmediatelyOnUpdate")
    

    @property
    def tropo_type(self) -> troposphere.secretsmanager.RotationSchedule:
        from troposphere.secretsmanager import RotationSchedule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.secretsmanager import RotationSchedule as TropoT
        return resource_to_troposphere(self, TropoT)


class Secret(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html
    Properties:
        - Name: Description
        - Name: KmsKeyId
        - Name: SecretString
        - Name: GenerateSecretString
        - Name: ReplicaRegions
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html#cfn-secretsmanager-secret-description""", alias="Description")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html#cfn-secretsmanager-secret-kmskeyid""", alias="KmsKeyId")
    SecretString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html#cfn-secretsmanager-secret-secretstring""", alias="SecretString")
    GenerateSecretString_: Optional['GenerateSecretString'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html#cfn-secretsmanager-secret-generatesecretstring""", alias="GenerateSecretString")
    ReplicaRegions_: Optional[List['ReplicaRegion']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html#cfn-secretsmanager-secret-replicaregions""", alias="ReplicaRegions")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html#cfn-secretsmanager-secret-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html#cfn-secretsmanager-secret-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.secretsmanager.Secret:
        from troposphere.secretsmanager import Secret as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.secretsmanager import Secret as TropoT
        return resource_to_troposphere(self, TropoT)


class SecretTargetAttachment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secrettargetattachment.html
    Properties:
        - Name: SecretId
        - Name: TargetType
        - Name: TargetId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SecretId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secrettargetattachment.html#cfn-secretsmanager-secrettargetattachment-secretid""", alias="SecretId")
    TargetType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secrettargetattachment.html#cfn-secretsmanager-secrettargetattachment-targettype""", alias="TargetType")
    TargetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secrettargetattachment.html#cfn-secretsmanager-secrettargetattachment-targetid""", alias="TargetId")
    

    @property
    def tropo_type(self) -> troposphere.secretsmanager.SecretTargetAttachment:
        from troposphere.secretsmanager import SecretTargetAttachment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.secretsmanager import SecretTargetAttachment as TropoT
        return resource_to_troposphere(self, TropoT)

