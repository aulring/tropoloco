from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CognitoUserPoolConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration.html
    Properties:
        - Name: UserPoolArn
        - Name: ClientIds
    
    """
    
    UserPoolArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration.html#cfn-verifiedpermissions-identitysource-cognitouserpoolconfiguration-userpoolarn""", alias="UserPoolArn")
    ClientIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration.html#cfn-verifiedpermissions-identitysource-cognitouserpoolconfiguration-clientids""", alias="ClientIds")
    


    @property
    def tropo_type(self) -> troposphere.verifiedpermissions.CognitoUserPoolConfiguration:
        from troposphere.verifiedpermissions import CognitoUserPoolConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IdentitySourceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourceconfiguration.html
    Properties:
        - Name: CognitoUserPoolConfiguration
    
    """
    
    CognitoUserPoolConfiguration_: 'CognitoUserPoolConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourceconfiguration.html#cfn-verifiedpermissions-identitysource-identitysourceconfiguration-cognitouserpoolconfiguration""", alias="CognitoUserPoolConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.verifiedpermissions.IdentitySourceConfiguration:
        from troposphere.verifiedpermissions import IdentitySourceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IdentitySourceDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourcedetails.html
    Properties:
        - Name: DiscoveryUrl
        - Name: UserPoolArn
        - Name: OpenIdIssuer
        - Name: ClientIds
    
    """
    
    DiscoveryUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourcedetails.html#cfn-verifiedpermissions-identitysource-identitysourcedetails-discoveryurl""", alias="DiscoveryUrl")
    UserPoolArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourcedetails.html#cfn-verifiedpermissions-identitysource-identitysourcedetails-userpoolarn""", alias="UserPoolArn")
    OpenIdIssuer_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourcedetails.html#cfn-verifiedpermissions-identitysource-identitysourcedetails-openidissuer""", alias="OpenIdIssuer")
    ClientIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourcedetails.html#cfn-verifiedpermissions-identitysource-identitysourcedetails-clientids""", alias="ClientIds")
    


    @property
    def tropo_type(self) -> troposphere.verifiedpermissions.IdentitySourceDetails:
        from troposphere.verifiedpermissions import IdentitySourceDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EntityIdentifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-entityidentifier.html
    Properties:
        - Name: EntityType
        - Name: EntityId
    
    """
    
    EntityType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-entityidentifier.html#cfn-verifiedpermissions-policy-entityidentifier-entitytype""", alias="EntityType")
    EntityId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-entityidentifier.html#cfn-verifiedpermissions-policy-entityidentifier-entityid""", alias="EntityId")
    


    @property
    def tropo_type(self) -> troposphere.verifiedpermissions.EntityIdentifier:
        from troposphere.verifiedpermissions import EntityIdentifier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PolicyDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-policydefinition.html
    Properties:
        - Name: Static
        - Name: TemplateLinked
    
    """
    
    Static_: Optional['StaticPolicyDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-policydefinition.html#cfn-verifiedpermissions-policy-policydefinition-static""", alias="Static")
    TemplateLinked_: Optional['TemplateLinkedPolicyDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-policydefinition.html#cfn-verifiedpermissions-policy-policydefinition-templatelinked""", alias="TemplateLinked")
    


    @property
    def tropo_type(self) -> troposphere.verifiedpermissions.PolicyDefinition:
        from troposphere.verifiedpermissions import PolicyDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StaticPolicyDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-staticpolicydefinition.html
    Properties:
        - Name: Description
        - Name: Statement
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-staticpolicydefinition.html#cfn-verifiedpermissions-policy-staticpolicydefinition-description""", alias="Description")
    Statement_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-staticpolicydefinition.html#cfn-verifiedpermissions-policy-staticpolicydefinition-statement""", alias="Statement")
    


    @property
    def tropo_type(self) -> troposphere.verifiedpermissions.StaticPolicyDefinition:
        from troposphere.verifiedpermissions import StaticPolicyDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TemplateLinkedPolicyDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition.html
    Properties:
        - Name: Resource
        - Name: PolicyTemplateId
        - Name: Principal
    
    """
    
    Resource_: Optional['EntityIdentifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition.html#cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-resource""", alias="Resource")
    PolicyTemplateId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition.html#cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-policytemplateid""", alias="PolicyTemplateId")
    Principal_: Optional['EntityIdentifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition.html#cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-principal""", alias="Principal")
    


    @property
    def tropo_type(self) -> troposphere.verifiedpermissions.TemplateLinkedPolicyDefinition:
        from troposphere.verifiedpermissions import TemplateLinkedPolicyDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SchemaDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policystore-schemadefinition.html
    Properties:
        - Name: CedarJson
    
    """
    
    CedarJson_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policystore-schemadefinition.html#cfn-verifiedpermissions-policystore-schemadefinition-cedarjson""", alias="CedarJson")
    


    @property
    def tropo_type(self) -> troposphere.verifiedpermissions.SchemaDefinition:
        from troposphere.verifiedpermissions import SchemaDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ValidationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policystore-validationsettings.html
    Properties:
        - Name: Mode
    
    """
    
    Mode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policystore-validationsettings.html#cfn-verifiedpermissions-policystore-validationsettings-mode""", alias="Mode")
    


    @property
    def tropo_type(self) -> troposphere.verifiedpermissions.ValidationSettings:
        from troposphere.verifiedpermissions import ValidationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class IdentitySource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-identitysource.html
    Properties:
        - Name: PrincipalEntityType
        - Name: Configuration
        - Name: PolicyStoreId
    Attributes:
        - Name: Details.DiscoveryUrl
        - Name: Details
        - Name: Details.ClientIds
        - Name: Details.UserPoolArn
        - Name: Details.OpenIdIssuer
        - Name: IdentitySourceId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PrincipalEntityType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-identitysource.html#cfn-verifiedpermissions-identitysource-principalentitytype""", alias="PrincipalEntityType")
    Configuration_: 'IdentitySourceConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-identitysource.html#cfn-verifiedpermissions-identitysource-configuration""", alias="Configuration")
    PolicyStoreId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-identitysource.html#cfn-verifiedpermissions-identitysource-policystoreid""", alias="PolicyStoreId")
    

    @property
    def tropo_type(self) -> troposphere.verifiedpermissions.IdentitySource:
        from troposphere.verifiedpermissions import IdentitySource as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.verifiedpermissions import IdentitySource as TropoT
        return resource_to_troposphere(self, TropoT)


class Policy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policy.html
    Properties:
        - Name: Definition
        - Name: PolicyStoreId
    Attributes:
        - Name: PolicyType
        - Name: PolicyId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Definition_: 'PolicyDefinition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policy.html#cfn-verifiedpermissions-policy-definition""", alias="Definition")
    PolicyStoreId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policy.html#cfn-verifiedpermissions-policy-policystoreid""", alias="PolicyStoreId")
    

    @property
    def tropo_type(self) -> troposphere.verifiedpermissions.Policy:
        from troposphere.verifiedpermissions import Policy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.verifiedpermissions import Policy as TropoT
        return resource_to_troposphere(self, TropoT)


class PolicyStore(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policystore.html
    Properties:
        - Name: ValidationSettings
        - Name: Schema
    Attributes:
        - Name: PolicyStoreId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ValidationSettings_: 'ValidationSettings' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policystore.html#cfn-verifiedpermissions-policystore-validationsettings""", alias="ValidationSettings")
    Schema_: Optional['SchemaDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policystore.html#cfn-verifiedpermissions-policystore-schema""", alias="Schema")
    

    @property
    def tropo_type(self) -> troposphere.verifiedpermissions.PolicyStore:
        from troposphere.verifiedpermissions import PolicyStore as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.verifiedpermissions import PolicyStore as TropoT
        return resource_to_troposphere(self, TropoT)


class PolicyTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policytemplate.html
    Properties:
        - Name: Description
        - Name: Statement
        - Name: PolicyStoreId
    Attributes:
        - Name: PolicyTemplateId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policytemplate.html#cfn-verifiedpermissions-policytemplate-description""", alias="Description")
    Statement_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policytemplate.html#cfn-verifiedpermissions-policytemplate-statement""", alias="Statement")
    PolicyStoreId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policytemplate.html#cfn-verifiedpermissions-policytemplate-policystoreid""", alias="PolicyStoreId")
    

    @property
    def tropo_type(self) -> troposphere.verifiedpermissions.PolicyTemplate:
        from troposphere.verifiedpermissions import PolicyTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.verifiedpermissions import PolicyTemplate as TropoT
        return resource_to_troposphere(self, TropoT)

