from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class IdMappingTechniques(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-idmappingtechniques.html
    Properties:
        - Name: ProviderProperties
        - Name: IdMappingType
    
    """
    
    ProviderProperties_: Optional['ProviderProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-idmappingtechniques.html#cfn-entityresolution-idmappingworkflow-idmappingtechniques-providerproperties""", alias="ProviderProperties")
    IdMappingType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-idmappingtechniques.html#cfn-entityresolution-idmappingworkflow-idmappingtechniques-idmappingtype""", alias="IdMappingType")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.IdMappingTechniques:
        from troposphere.entityresolution import IdMappingTechniques as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IdMappingWorkflowInputSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-idmappingworkflowinputsource.html
    Properties:
        - Name: InputSourceARN
        - Name: SchemaArn
    
    """
    
    InputSourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-idmappingworkflowinputsource.html#cfn-entityresolution-idmappingworkflow-idmappingworkflowinputsource-inputsourcearn""", alias="InputSourceARN")
    SchemaArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-idmappingworkflowinputsource.html#cfn-entityresolution-idmappingworkflow-idmappingworkflowinputsource-schemaarn""", alias="SchemaArn")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.IdMappingWorkflowInputSource:
        from troposphere.entityresolution import IdMappingWorkflowInputSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IdMappingWorkflowOutputSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-idmappingworkflowoutputsource.html
    Properties:
        - Name: KMSArn
        - Name: OutputS3Path
    
    """
    
    KMSArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-idmappingworkflowoutputsource.html#cfn-entityresolution-idmappingworkflow-idmappingworkflowoutputsource-kmsarn""", alias="KMSArn")
    OutputS3Path_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-idmappingworkflowoutputsource.html#cfn-entityresolution-idmappingworkflow-idmappingworkflowoutputsource-outputs3path""", alias="OutputS3Path")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.IdMappingWorkflowOutputSource:
        from troposphere.entityresolution import IdMappingWorkflowOutputSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IntermediateSourceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-intermediatesourceconfiguration.html
    Properties:
        - Name: IntermediateS3Path
    
    """
    
    IntermediateS3Path_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-intermediatesourceconfiguration.html#cfn-entityresolution-idmappingworkflow-intermediatesourceconfiguration-intermediates3path""", alias="IntermediateS3Path")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.IntermediateSourceConfiguration:
        from troposphere.entityresolution import IntermediateSourceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProviderProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-providerproperties.html
    Properties:
        - Name: IntermediateSourceConfiguration
        - Name: ProviderServiceArn
        - Name: ProviderConfiguration
    
    """
    
    IntermediateSourceConfiguration_: Optional['IntermediateSourceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-providerproperties.html#cfn-entityresolution-idmappingworkflow-providerproperties-intermediatesourceconfiguration""", alias="IntermediateSourceConfiguration")
    ProviderServiceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-providerproperties.html#cfn-entityresolution-idmappingworkflow-providerproperties-providerservicearn""", alias="ProviderServiceArn")
    ProviderConfiguration_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-idmappingworkflow-providerproperties.html#cfn-entityresolution-idmappingworkflow-providerproperties-providerconfiguration""", alias="ProviderConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.ProviderProperties:
        from troposphere.entityresolution import ProviderProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-inputsource.html
    Properties:
        - Name: ApplyNormalization
        - Name: InputSourceARN
        - Name: SchemaArn
    
    """
    
    ApplyNormalization_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-inputsource.html#cfn-entityresolution-matchingworkflow-inputsource-applynormalization""", alias="ApplyNormalization")
    InputSourceARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-inputsource.html#cfn-entityresolution-matchingworkflow-inputsource-inputsourcearn""", alias="InputSourceARN")
    SchemaArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-inputsource.html#cfn-entityresolution-matchingworkflow-inputsource-schemaarn""", alias="SchemaArn")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.InputSource:
        from troposphere.entityresolution import InputSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IntermediateSourceConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-intermediatesourceconfiguration.html
    Properties:
        - Name: IntermediateS3Path
    
    """
    
    IntermediateS3Path_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-intermediatesourceconfiguration.html#cfn-entityresolution-matchingworkflow-intermediatesourceconfiguration-intermediates3path""", alias="IntermediateS3Path")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.IntermediateSourceConfiguration:
        from troposphere.entityresolution import IntermediateSourceConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputAttribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputattribute.html
    Properties:
        - Name: Hashed
        - Name: Name
    
    """
    
    Hashed_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputattribute.html#cfn-entityresolution-matchingworkflow-outputattribute-hashed""", alias="Hashed")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputattribute.html#cfn-entityresolution-matchingworkflow-outputattribute-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.OutputAttribute:
        from troposphere.entityresolution import OutputAttribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputsource.html
    Properties:
        - Name: KMSArn
        - Name: OutputS3Path
        - Name: Output
        - Name: ApplyNormalization
    
    """
    
    KMSArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputsource.html#cfn-entityresolution-matchingworkflow-outputsource-kmsarn""", alias="KMSArn")
    OutputS3Path_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputsource.html#cfn-entityresolution-matchingworkflow-outputsource-outputs3path""", alias="OutputS3Path")
    Output_: List['OutputAttribute'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputsource.html#cfn-entityresolution-matchingworkflow-outputsource-output""", alias="Output")
    ApplyNormalization_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-outputsource.html#cfn-entityresolution-matchingworkflow-outputsource-applynormalization""", alias="ApplyNormalization")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.OutputSource:
        from troposphere.entityresolution import OutputSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProviderProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-providerproperties.html
    Properties:
        - Name: IntermediateSourceConfiguration
        - Name: ProviderServiceArn
        - Name: ProviderConfiguration
    
    """
    
    IntermediateSourceConfiguration_: Optional['IntermediateSourceConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-providerproperties.html#cfn-entityresolution-matchingworkflow-providerproperties-intermediatesourceconfiguration""", alias="IntermediateSourceConfiguration")
    ProviderServiceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-providerproperties.html#cfn-entityresolution-matchingworkflow-providerproperties-providerservicearn""", alias="ProviderServiceArn")
    ProviderConfiguration_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-providerproperties.html#cfn-entityresolution-matchingworkflow-providerproperties-providerconfiguration""", alias="ProviderConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.ProviderProperties:
        from troposphere.entityresolution import ProviderProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResolutionTechniques(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-resolutiontechniques.html
    Properties:
        - Name: RuleBasedProperties
        - Name: ProviderProperties
        - Name: ResolutionType
    
    """
    
    RuleBasedProperties_: Optional['RuleBasedProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-resolutiontechniques.html#cfn-entityresolution-matchingworkflow-resolutiontechniques-rulebasedproperties""", alias="RuleBasedProperties")
    ProviderProperties_: Optional['ProviderProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-resolutiontechniques.html#cfn-entityresolution-matchingworkflow-resolutiontechniques-providerproperties""", alias="ProviderProperties")
    ResolutionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-resolutiontechniques.html#cfn-entityresolution-matchingworkflow-resolutiontechniques-resolutiontype""", alias="ResolutionType")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.ResolutionTechniques:
        from troposphere.entityresolution import ResolutionTechniques as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rule.html
    Properties:
        - Name: MatchingKeys
        - Name: RuleName
    
    """
    
    MatchingKeys_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rule.html#cfn-entityresolution-matchingworkflow-rule-matchingkeys""", alias="MatchingKeys")
    RuleName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rule.html#cfn-entityresolution-matchingworkflow-rule-rulename""", alias="RuleName")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.Rule:
        from troposphere.entityresolution import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleBasedProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rulebasedproperties.html
    Properties:
        - Name: AttributeMatchingModel
        - Name: Rules
    
    """
    
    AttributeMatchingModel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rulebasedproperties.html#cfn-entityresolution-matchingworkflow-rulebasedproperties-attributematchingmodel""", alias="AttributeMatchingModel")
    Rules_: List['Rule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-matchingworkflow-rulebasedproperties.html#cfn-entityresolution-matchingworkflow-rulebasedproperties-rules""", alias="Rules")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.RuleBasedProperties:
        from troposphere.entityresolution import RuleBasedProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SchemaInputAttribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-schemamapping-schemainputattribute.html
    Properties:
        - Name: GroupName
        - Name: Type
        - Name: SubType
        - Name: MatchKey
        - Name: FieldName
    
    """
    
    GroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-schemamapping-schemainputattribute.html#cfn-entityresolution-schemamapping-schemainputattribute-groupname""", alias="GroupName")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-schemamapping-schemainputattribute.html#cfn-entityresolution-schemamapping-schemainputattribute-type""", alias="Type")
    SubType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-schemamapping-schemainputattribute.html#cfn-entityresolution-schemamapping-schemainputattribute-subtype""", alias="SubType")
    MatchKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-schemamapping-schemainputattribute.html#cfn-entityresolution-schemamapping-schemainputattribute-matchkey""", alias="MatchKey")
    FieldName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-entityresolution-schemamapping-schemainputattribute.html#cfn-entityresolution-schemamapping-schemainputattribute-fieldname""", alias="FieldName")
    


    @property
    def tropo_type(self) -> troposphere.entityresolution.SchemaInputAttribute:
        from troposphere.entityresolution import SchemaInputAttribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class IdMappingWorkflow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idmappingworkflow.html
    Properties:
        - Name: Description
        - Name: InputSourceConfig
        - Name: IdMappingTechniques
        - Name: WorkflowName
        - Name: OutputSourceConfig
        - Name: RoleArn
        - Name: Tags
    Attributes:
        - Name: CreatedAt
        - Name: WorkflowArn
        - Name: UpdatedAt
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idmappingworkflow.html#cfn-entityresolution-idmappingworkflow-description""", alias="Description")
    InputSourceConfig_: List['IdMappingWorkflowInputSource'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idmappingworkflow.html#cfn-entityresolution-idmappingworkflow-inputsourceconfig""", alias="InputSourceConfig")
    IdMappingTechniques_: 'IdMappingTechniques' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idmappingworkflow.html#cfn-entityresolution-idmappingworkflow-idmappingtechniques""", alias="IdMappingTechniques")
    WorkflowName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idmappingworkflow.html#cfn-entityresolution-idmappingworkflow-workflowname""", alias="WorkflowName")
    OutputSourceConfig_: List['IdMappingWorkflowOutputSource'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idmappingworkflow.html#cfn-entityresolution-idmappingworkflow-outputsourceconfig""", alias="OutputSourceConfig")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idmappingworkflow.html#cfn-entityresolution-idmappingworkflow-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idmappingworkflow.html#cfn-entityresolution-idmappingworkflow-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.entityresolution.IdMappingWorkflow:
        from troposphere.entityresolution import IdMappingWorkflow as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.entityresolution import IdMappingWorkflow as TropoT
        return resource_to_troposphere(self, TropoT)


class MatchingWorkflow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html
    Properties:
        - Name: ResolutionTechniques
        - Name: Description
        - Name: InputSourceConfig
        - Name: WorkflowName
        - Name: OutputSourceConfig
        - Name: RoleArn
        - Name: Tags
    Attributes:
        - Name: CreatedAt
        - Name: WorkflowArn
        - Name: UpdatedAt
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResolutionTechniques_: 'ResolutionTechniques' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-resolutiontechniques""", alias="ResolutionTechniques")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-description""", alias="Description")
    InputSourceConfig_: List['InputSource'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-inputsourceconfig""", alias="InputSourceConfig")
    WorkflowName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-workflowname""", alias="WorkflowName")
    OutputSourceConfig_: List['OutputSource'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-outputsourceconfig""", alias="OutputSourceConfig")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-matchingworkflow.html#cfn-entityresolution-matchingworkflow-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.entityresolution.MatchingWorkflow:
        from troposphere.entityresolution import MatchingWorkflow as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.entityresolution import MatchingWorkflow as TropoT
        return resource_to_troposphere(self, TropoT)


class SchemaMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html
    Properties:
        - Name: Description
        - Name: MappedInputFields
        - Name: SchemaName
        - Name: Tags
    Attributes:
        - Name: CreatedAt
        - Name: HasWorkflows
        - Name: UpdatedAt
        - Name: SchemaArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html#cfn-entityresolution-schemamapping-description""", alias="Description")
    MappedInputFields_: List['SchemaInputAttribute'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html#cfn-entityresolution-schemamapping-mappedinputfields""", alias="MappedInputFields")
    SchemaName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html#cfn-entityresolution-schemamapping-schemaname""", alias="SchemaName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-schemamapping.html#cfn-entityresolution-schemamapping-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.entityresolution.SchemaMapping:
        from troposphere.entityresolution import SchemaMapping as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.entityresolution import SchemaMapping as TropoT
        return resource_to_troposphere(self, TropoT)

