from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DataConnector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-dataconnector.html
    Properties:
        - Name: IsNative
        - Name: Lambda
    
    """
    
    IsNative_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-dataconnector.html#cfn-iottwinmaker-componenttype-dataconnector-isnative""", alias="IsNative")
    Lambda_: Optional['LambdaFunction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-dataconnector.html#cfn-iottwinmaker-componenttype-dataconnector-lambda""", alias="Lambda")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.DataConnector:
        from troposphere.iottwinmaker import DataConnector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datatype.html
    Properties:
        - Name: Type
        - Name: AllowedValues
        - Name: UnitOfMeasure
        - Name: Relationship
        - Name: NestedType
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datatype.html#cfn-iottwinmaker-componenttype-datatype-type""", alias="Type")
    AllowedValues_: Optional[List['DataValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datatype.html#cfn-iottwinmaker-componenttype-datatype-allowedvalues""", alias="AllowedValues")
    UnitOfMeasure_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datatype.html#cfn-iottwinmaker-componenttype-datatype-unitofmeasure""", alias="UnitOfMeasure")
    Relationship_: Optional['Relationship'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datatype.html#cfn-iottwinmaker-componenttype-datatype-relationship""", alias="Relationship")
    NestedType_: Optional['DataType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datatype.html#cfn-iottwinmaker-componenttype-datatype-nestedtype""", alias="NestedType")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.DataType:
        from troposphere.iottwinmaker import DataType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datavalue.html
    Properties:
        - Name: DoubleValue
        - Name: Expression
        - Name: BooleanValue
        - Name: IntegerValue
        - Name: ListValue
        - Name: LongValue
        - Name: MapValue
        - Name: RelationshipValue
        - Name: StringValue
    
    """
    
    DoubleValue_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datavalue.html#cfn-iottwinmaker-componenttype-datavalue-doublevalue""", alias="DoubleValue")
    Expression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datavalue.html#cfn-iottwinmaker-componenttype-datavalue-expression""", alias="Expression")
    BooleanValue_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datavalue.html#cfn-iottwinmaker-componenttype-datavalue-booleanvalue""", alias="BooleanValue")
    IntegerValue_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datavalue.html#cfn-iottwinmaker-componenttype-datavalue-integervalue""", alias="IntegerValue")
    ListValue_: Optional[List['DataValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datavalue.html#cfn-iottwinmaker-componenttype-datavalue-listvalue""", alias="ListValue")
    LongValue_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datavalue.html#cfn-iottwinmaker-componenttype-datavalue-longvalue""", alias="LongValue")
    MapValue_: Optional[Dict[str, 'DataValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datavalue.html#cfn-iottwinmaker-componenttype-datavalue-mapvalue""", alias="MapValue")
    RelationshipValue_: Optional['RelationshipValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datavalue.html#cfn-iottwinmaker-componenttype-datavalue-relationshipvalue""", alias="RelationshipValue")
    StringValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-datavalue.html#cfn-iottwinmaker-componenttype-datavalue-stringvalue""", alias="StringValue")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.DataValue:
        from troposphere.iottwinmaker import DataValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Error(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-error.html
    Properties:
        - Name: Message
        - Name: Code
    
    """
    
    Message_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-error.html#cfn-iottwinmaker-componenttype-error-message""", alias="Message")
    Code_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-error.html#cfn-iottwinmaker-componenttype-error-code""", alias="Code")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.Error:
        from troposphere.iottwinmaker import Error as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Function(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-function.html
    Properties:
        - Name: Scope
        - Name: RequiredProperties
        - Name: ImplementedBy
    
    """
    
    Scope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-function.html#cfn-iottwinmaker-componenttype-function-scope""", alias="Scope")
    RequiredProperties_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-function.html#cfn-iottwinmaker-componenttype-function-requiredproperties""", alias="RequiredProperties")
    ImplementedBy_: Optional['DataConnector'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-function.html#cfn-iottwinmaker-componenttype-function-implementedby""", alias="ImplementedBy")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.Function:
        from troposphere.iottwinmaker import Function as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaFunction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-lambdafunction.html
    Properties:
        - Name: Arn
    
    """
    
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-lambdafunction.html#cfn-iottwinmaker-componenttype-lambdafunction-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.LambdaFunction:
        from troposphere.iottwinmaker import LambdaFunction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PropertyDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-propertydefinition.html
    Properties:
        - Name: DefaultValue
        - Name: IsExternalId
        - Name: IsStoredExternally
        - Name: IsTimeSeries
        - Name: IsRequiredInEntity
        - Name: DataType
        - Name: Configurations
    
    """
    
    DefaultValue_: Optional['DataValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-propertydefinition.html#cfn-iottwinmaker-componenttype-propertydefinition-defaultvalue""", alias="DefaultValue")
    IsExternalId_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-propertydefinition.html#cfn-iottwinmaker-componenttype-propertydefinition-isexternalid""", alias="IsExternalId")
    IsStoredExternally_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-propertydefinition.html#cfn-iottwinmaker-componenttype-propertydefinition-isstoredexternally""", alias="IsStoredExternally")
    IsTimeSeries_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-propertydefinition.html#cfn-iottwinmaker-componenttype-propertydefinition-istimeseries""", alias="IsTimeSeries")
    IsRequiredInEntity_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-propertydefinition.html#cfn-iottwinmaker-componenttype-propertydefinition-isrequiredinentity""", alias="IsRequiredInEntity")
    DataType_: Optional['DataType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-propertydefinition.html#cfn-iottwinmaker-componenttype-propertydefinition-datatype""", alias="DataType")
    Configurations_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-propertydefinition.html#cfn-iottwinmaker-componenttype-propertydefinition-configurations""", alias="Configurations")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.PropertyDefinition:
        from troposphere.iottwinmaker import PropertyDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PropertyGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-propertygroup.html
    Properties:
        - Name: GroupType
        - Name: PropertyNames
    
    """
    
    GroupType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-propertygroup.html#cfn-iottwinmaker-componenttype-propertygroup-grouptype""", alias="GroupType")
    PropertyNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-propertygroup.html#cfn-iottwinmaker-componenttype-propertygroup-propertynames""", alias="PropertyNames")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.PropertyGroup:
        from troposphere.iottwinmaker import PropertyGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Relationship(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-relationship.html
    Properties:
        - Name: RelationshipType
        - Name: TargetComponentTypeId
    
    """
    
    RelationshipType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-relationship.html#cfn-iottwinmaker-componenttype-relationship-relationshiptype""", alias="RelationshipType")
    TargetComponentTypeId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-relationship.html#cfn-iottwinmaker-componenttype-relationship-targetcomponenttypeid""", alias="TargetComponentTypeId")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.Relationship:
        from troposphere.iottwinmaker import Relationship as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RelationshipValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-relationshipvalue.html
    Properties:
        - Name: TargetComponentName
        - Name: TargetEntityId
    
    """
    
    TargetComponentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-relationshipvalue.html#cfn-iottwinmaker-componenttype-relationshipvalue-targetcomponentname""", alias="TargetComponentName")
    TargetEntityId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-relationshipvalue.html#cfn-iottwinmaker-componenttype-relationshipvalue-targetentityid""", alias="TargetEntityId")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.RelationshipValue:
        from troposphere.iottwinmaker import RelationshipValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Status(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-status.html
    Properties:
        - Name: State
        - Name: Error
    
    """
    
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-status.html#cfn-iottwinmaker-componenttype-status-state""", alias="State")
    Error_: Optional['Error'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-status.html#cfn-iottwinmaker-componenttype-status-error""", alias="Error")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.Status:
        from troposphere.iottwinmaker import Status as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Component(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-component.html
    Properties:
        - Name: Status
        - Name: Description
        - Name: DefinedIn
        - Name: PropertyGroups
        - Name: ComponentTypeId
        - Name: ComponentName
        - Name: Properties
    
    """
    
    Status_: Optional['Status'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-component.html#cfn-iottwinmaker-entity-component-status""", alias="Status")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-component.html#cfn-iottwinmaker-entity-component-description""", alias="Description")
    DefinedIn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-component.html#cfn-iottwinmaker-entity-component-definedin""", alias="DefinedIn")
    PropertyGroups_: Optional[Dict[str, 'PropertyGroup']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-component.html#cfn-iottwinmaker-entity-component-propertygroups""", alias="PropertyGroups")
    ComponentTypeId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-component.html#cfn-iottwinmaker-entity-component-componenttypeid""", alias="ComponentTypeId")
    ComponentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-component.html#cfn-iottwinmaker-entity-component-componentname""", alias="ComponentName")
    Properties_: Optional[Dict[str, 'Property']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-component.html#cfn-iottwinmaker-entity-component-properties""", alias="Properties")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.Component:
        from troposphere.iottwinmaker import Component as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datatype.html
    Properties:
        - Name: Type
        - Name: AllowedValues
        - Name: UnitOfMeasure
        - Name: Relationship
        - Name: NestedType
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datatype.html#cfn-iottwinmaker-entity-datatype-type""", alias="Type")
    AllowedValues_: Optional[List['DataValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datatype.html#cfn-iottwinmaker-entity-datatype-allowedvalues""", alias="AllowedValues")
    UnitOfMeasure_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datatype.html#cfn-iottwinmaker-entity-datatype-unitofmeasure""", alias="UnitOfMeasure")
    Relationship_: Optional['Relationship'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datatype.html#cfn-iottwinmaker-entity-datatype-relationship""", alias="Relationship")
    NestedType_: Optional['DataType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datatype.html#cfn-iottwinmaker-entity-datatype-nestedtype""", alias="NestedType")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.DataType:
        from troposphere.iottwinmaker import DataType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datavalue.html
    Properties:
        - Name: DoubleValue
        - Name: Expression
        - Name: BooleanValue
        - Name: IntegerValue
        - Name: ListValue
        - Name: LongValue
        - Name: MapValue
        - Name: RelationshipValue
        - Name: StringValue
    
    """
    
    DoubleValue_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datavalue.html#cfn-iottwinmaker-entity-datavalue-doublevalue""", alias="DoubleValue")
    Expression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datavalue.html#cfn-iottwinmaker-entity-datavalue-expression""", alias="Expression")
    BooleanValue_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datavalue.html#cfn-iottwinmaker-entity-datavalue-booleanvalue""", alias="BooleanValue")
    IntegerValue_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datavalue.html#cfn-iottwinmaker-entity-datavalue-integervalue""", alias="IntegerValue")
    ListValue_: Optional[List['DataValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datavalue.html#cfn-iottwinmaker-entity-datavalue-listvalue""", alias="ListValue")
    LongValue_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datavalue.html#cfn-iottwinmaker-entity-datavalue-longvalue""", alias="LongValue")
    MapValue_: Optional[Dict[str, 'DataValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datavalue.html#cfn-iottwinmaker-entity-datavalue-mapvalue""", alias="MapValue")
    RelationshipValue_: Optional['RelationshipValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datavalue.html#cfn-iottwinmaker-entity-datavalue-relationshipvalue""", alias="RelationshipValue")
    StringValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-datavalue.html#cfn-iottwinmaker-entity-datavalue-stringvalue""", alias="StringValue")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.DataValue:
        from troposphere.iottwinmaker import DataValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Definition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-definition.html
    Properties:
        - Name: DefaultValue
        - Name: IsImported
        - Name: IsInherited
        - Name: Configuration
        - Name: IsExternalId
        - Name: IsStoredExternally
        - Name: IsTimeSeries
        - Name: IsRequiredInEntity
        - Name: DataType
        - Name: IsFinal
    
    """
    
    DefaultValue_: Optional['DataValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-definition.html#cfn-iottwinmaker-entity-definition-defaultvalue""", alias="DefaultValue")
    IsImported_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-definition.html#cfn-iottwinmaker-entity-definition-isimported""", alias="IsImported")
    IsInherited_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-definition.html#cfn-iottwinmaker-entity-definition-isinherited""", alias="IsInherited")
    Configuration_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-definition.html#cfn-iottwinmaker-entity-definition-configuration""", alias="Configuration")
    IsExternalId_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-definition.html#cfn-iottwinmaker-entity-definition-isexternalid""", alias="IsExternalId")
    IsStoredExternally_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-definition.html#cfn-iottwinmaker-entity-definition-isstoredexternally""", alias="IsStoredExternally")
    IsTimeSeries_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-definition.html#cfn-iottwinmaker-entity-definition-istimeseries""", alias="IsTimeSeries")
    IsRequiredInEntity_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-definition.html#cfn-iottwinmaker-entity-definition-isrequiredinentity""", alias="IsRequiredInEntity")
    DataType_: Optional['DataType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-definition.html#cfn-iottwinmaker-entity-definition-datatype""", alias="DataType")
    IsFinal_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-definition.html#cfn-iottwinmaker-entity-definition-isfinal""", alias="IsFinal")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.Definition:
        from troposphere.iottwinmaker import Definition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Error(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-error.html
    Properties:
        - Name: Message
        - Name: Code
    
    """
    
    Message_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-error.html#cfn-iottwinmaker-entity-error-message""", alias="Message")
    Code_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-error.html#cfn-iottwinmaker-entity-error-code""", alias="Code")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.Error:
        from troposphere.iottwinmaker import Error as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Property(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-property.html
    Properties:
        - Name: Definition
        - Name: Value
    
    """
    
    Definition_: Optional['Definition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-property.html#cfn-iottwinmaker-entity-property-definition""", alias="Definition")
    Value_: Optional['DataValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-property.html#cfn-iottwinmaker-entity-property-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.Property:
        from troposphere.iottwinmaker import Property as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PropertyGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-propertygroup.html
    Properties:
        - Name: GroupType
        - Name: PropertyNames
    
    """
    
    GroupType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-propertygroup.html#cfn-iottwinmaker-entity-propertygroup-grouptype""", alias="GroupType")
    PropertyNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-propertygroup.html#cfn-iottwinmaker-entity-propertygroup-propertynames""", alias="PropertyNames")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.PropertyGroup:
        from troposphere.iottwinmaker import PropertyGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Relationship(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-relationship.html
    Properties:
        - Name: RelationshipType
        - Name: TargetComponentTypeId
    
    """
    
    RelationshipType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-relationship.html#cfn-iottwinmaker-entity-relationship-relationshiptype""", alias="RelationshipType")
    TargetComponentTypeId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-relationship.html#cfn-iottwinmaker-entity-relationship-targetcomponenttypeid""", alias="TargetComponentTypeId")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.Relationship:
        from troposphere.iottwinmaker import Relationship as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RelationshipValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-relationshipvalue.html
    Properties:
        - Name: TargetComponentName
        - Name: TargetEntityId
    
    """
    
    TargetComponentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-relationshipvalue.html#cfn-iottwinmaker-entity-relationshipvalue-targetcomponentname""", alias="TargetComponentName")
    TargetEntityId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-relationshipvalue.html#cfn-iottwinmaker-entity-relationshipvalue-targetentityid""", alias="TargetEntityId")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.RelationshipValue:
        from troposphere.iottwinmaker import RelationshipValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Status(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-status.html
    Properties:
        - Name: State
        - Name: Error
    
    """
    
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-status.html#cfn-iottwinmaker-entity-status-state""", alias="State")
    Error_: Optional['Error'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-status.html#cfn-iottwinmaker-entity-status-error""", alias="Error")
    


    @property
    def tropo_type(self) -> troposphere.iottwinmaker.Status:
        from troposphere.iottwinmaker import Status as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ComponentType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-componenttype.html
    Properties:
        - Name: ExtendsFrom
        - Name: Description
        - Name: IsSingleton
        - Name: PropertyDefinitions
        - Name: PropertyGroups
        - Name: WorkspaceId
        - Name: ComponentTypeId
        - Name: Functions
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: CreationDateTime
        - Name: Status.Error.Message
        - Name: IsSchemaInitialized
        - Name: Status.State
        - Name: Status.Error
        - Name: UpdateDateTime
        - Name: Status.Error.Code
        - Name: Arn
        - Name: IsAbstract
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ExtendsFrom_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-componenttype.html#cfn-iottwinmaker-componenttype-extendsfrom""", alias="ExtendsFrom")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-componenttype.html#cfn-iottwinmaker-componenttype-description""", alias="Description")
    IsSingleton_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-componenttype.html#cfn-iottwinmaker-componenttype-issingleton""", alias="IsSingleton")
    PropertyDefinitions_: Optional[Dict[str, 'PropertyDefinition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-componenttype.html#cfn-iottwinmaker-componenttype-propertydefinitions""", alias="PropertyDefinitions")
    PropertyGroups_: Optional[Dict[str, 'PropertyGroup']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-componenttype.html#cfn-iottwinmaker-componenttype-propertygroups""", alias="PropertyGroups")
    WorkspaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-componenttype.html#cfn-iottwinmaker-componenttype-workspaceid""", alias="WorkspaceId")
    ComponentTypeId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-componenttype.html#cfn-iottwinmaker-componenttype-componenttypeid""", alias="ComponentTypeId")
    Functions_: Optional[Dict[str, 'Function']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-componenttype.html#cfn-iottwinmaker-componenttype-functions""", alias="Functions")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-componenttype.html#cfn-iottwinmaker-componenttype-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iottwinmaker.ComponentType:
        from troposphere.iottwinmaker import ComponentType as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iottwinmaker import ComponentType as TropoT
        return resource_to_troposphere(self, TropoT)


class Entity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-entity.html
    Properties:
        - Name: EntityId
        - Name: Components
        - Name: ParentEntityId
        - Name: Description
        - Name: EntityName
        - Name: WorkspaceId
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: CreationDateTime
        - Name: Status.Error.Message
        - Name: HasChildEntities
        - Name: Status.State
        - Name: Status.Error
        - Name: UpdateDateTime
        - Name: Status.Error.Code
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EntityId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-entity.html#cfn-iottwinmaker-entity-entityid""", alias="EntityId")
    Components_: Optional[Dict[str, 'Component']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-entity.html#cfn-iottwinmaker-entity-components""", alias="Components")
    ParentEntityId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-entity.html#cfn-iottwinmaker-entity-parententityid""", alias="ParentEntityId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-entity.html#cfn-iottwinmaker-entity-description""", alias="Description")
    EntityName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-entity.html#cfn-iottwinmaker-entity-entityname""", alias="EntityName")
    WorkspaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-entity.html#cfn-iottwinmaker-entity-workspaceid""", alias="WorkspaceId")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-entity.html#cfn-iottwinmaker-entity-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iottwinmaker.Entity:
        from troposphere.iottwinmaker import Entity as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iottwinmaker import Entity as TropoT
        return resource_to_troposphere(self, TropoT)


class Scene(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-scene.html
    Properties:
        - Name: SceneId
        - Name: Description
        - Name: SceneMetadata
        - Name: ContentLocation
        - Name: Capabilities
        - Name: WorkspaceId
        - Name: Tags
    Attributes:
        - Name: CreationDateTime
        - Name: UpdateDateTime
        - Name: Arn
        - Name: GeneratedSceneMetadata
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SceneId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-scene.html#cfn-iottwinmaker-scene-sceneid""", alias="SceneId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-scene.html#cfn-iottwinmaker-scene-description""", alias="Description")
    SceneMetadata_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-scene.html#cfn-iottwinmaker-scene-scenemetadata""", alias="SceneMetadata")
    ContentLocation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-scene.html#cfn-iottwinmaker-scene-contentlocation""", alias="ContentLocation")
    Capabilities_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-scene.html#cfn-iottwinmaker-scene-capabilities""", alias="Capabilities")
    WorkspaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-scene.html#cfn-iottwinmaker-scene-workspaceid""", alias="WorkspaceId")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-scene.html#cfn-iottwinmaker-scene-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iottwinmaker.Scene:
        from troposphere.iottwinmaker import Scene as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iottwinmaker import Scene as TropoT
        return resource_to_troposphere(self, TropoT)


class SyncJob(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-syncjob.html
    Properties:
        - Name: SyncSource
        - Name: SyncRole
        - Name: WorkspaceId
        - Name: Tags
    Attributes:
        - Name: CreationDateTime
        - Name: State
        - Name: UpdateDateTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SyncSource_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-syncjob.html#cfn-iottwinmaker-syncjob-syncsource""", alias="SyncSource")
    SyncRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-syncjob.html#cfn-iottwinmaker-syncjob-syncrole""", alias="SyncRole")
    WorkspaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-syncjob.html#cfn-iottwinmaker-syncjob-workspaceid""", alias="WorkspaceId")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-syncjob.html#cfn-iottwinmaker-syncjob-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iottwinmaker.SyncJob:
        from troposphere.iottwinmaker import SyncJob as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iottwinmaker import SyncJob as TropoT
        return resource_to_troposphere(self, TropoT)


class Workspace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-workspace.html
    Properties:
        - Name: Role
        - Name: Description
        - Name: WorkspaceId
        - Name: S3Location
        - Name: Tags
    Attributes:
        - Name: CreationDateTime
        - Name: UpdateDateTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Role_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-workspace.html#cfn-iottwinmaker-workspace-role""", alias="Role")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-workspace.html#cfn-iottwinmaker-workspace-description""", alias="Description")
    WorkspaceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-workspace.html#cfn-iottwinmaker-workspace-workspaceid""", alias="WorkspaceId")
    S3Location_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-workspace.html#cfn-iottwinmaker-workspace-s3location""", alias="S3Location")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-workspace.html#cfn-iottwinmaker-workspace-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iottwinmaker.Workspace:
        from troposphere.iottwinmaker import Workspace as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iottwinmaker import Workspace as TropoT
        return resource_to_troposphere(self, TropoT)

