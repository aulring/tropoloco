from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ActionParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html
    Properties:
        - Name: Type
        - Name: Anchor
        - Name: Target
        - Name: Fields
        - Name: State
        - Name: Model
        - Name: Id
        - Name: Url
        - Name: Global
    
    """
    
    Type_: Optional['ComponentProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-type""", alias="Type")
    Anchor_: Optional['ComponentProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-anchor""", alias="Anchor")
    Target_: Optional['ComponentProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-target""", alias="Target")
    Fields_: Optional[Dict[str, 'ComponentProperty']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-fields""", alias="Fields")
    State_: Optional['MutationActionSetStateParameter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-state""", alias="State")
    Model_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-model""", alias="Model")
    Id_: Optional['ComponentProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-id""", alias="Id")
    Url_: Optional['ComponentProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-url""", alias="Url")
    Global_: Optional['ComponentProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html#cfn-amplifyuibuilder-component-actionparameters-global""", alias="Global")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ActionParameters:
        from troposphere.amplifyuibuilder import ActionParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentBindingPropertiesValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalue.html
    Properties:
        - Name: DefaultValue
        - Name: Type
        - Name: BindingProperties
    
    """
    
    DefaultValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalue.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalue-defaultvalue""", alias="DefaultValue")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalue.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalue-type""", alias="Type")
    BindingProperties_: Optional['ComponentBindingPropertiesValueProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalue.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalue-bindingproperties""", alias="BindingProperties")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ComponentBindingPropertiesValue:
        from troposphere.amplifyuibuilder import ComponentBindingPropertiesValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentBindingPropertiesValueProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html
    Properties:
        - Name: Field
        - Name: DefaultValue
        - Name: Bucket
        - Name: UserAttribute
        - Name: Model
        - Name: Predicates
        - Name: Key
    
    """
    
    Field_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-field""", alias="Field")
    DefaultValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-defaultvalue""", alias="DefaultValue")
    Bucket_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-bucket""", alias="Bucket")
    UserAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-userattribute""", alias="UserAttribute")
    Model_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-model""", alias="Model")
    Predicates_: Optional[List['Predicate']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-predicates""", alias="Predicates")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html#cfn-amplifyuibuilder-component-componentbindingpropertiesvalueproperties-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ComponentBindingPropertiesValueProperties:
        from troposphere.amplifyuibuilder import ComponentBindingPropertiesValueProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentChild(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentchild.html
    Properties:
        - Name: ComponentType
        - Name: Events
        - Name: Children
        - Name: Properties
        - Name: Name
    
    """
    
    ComponentType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentchild.html#cfn-amplifyuibuilder-component-componentchild-componenttype""", alias="ComponentType")
    Events_: Optional[Dict[str, 'ComponentEvent']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentchild.html#cfn-amplifyuibuilder-component-componentchild-events""", alias="Events")
    Children_: Optional[List['ComponentChild']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentchild.html#cfn-amplifyuibuilder-component-componentchild-children""", alias="Children")
    Properties_: Dict[str, 'ComponentProperty'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentchild.html#cfn-amplifyuibuilder-component-componentchild-properties""", alias="Properties")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentchild.html#cfn-amplifyuibuilder-component-componentchild-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ComponentChild:
        from troposphere.amplifyuibuilder import ComponentChild as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentConditionProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html
    Properties:
        - Name: Operator
        - Name: Field
        - Name: Operand
        - Name: OperandType
        - Name: Else
        - Name: Then
        - Name: Property
    
    """
    
    Operator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-operator""", alias="Operator")
    Field_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-field""", alias="Field")
    Operand_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-operand""", alias="Operand")
    OperandType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-operandtype""", alias="OperandType")
    Else_: Optional['ComponentProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-else""", alias="Else")
    Then_: Optional['ComponentProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-then""", alias="Then")
    Property_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html#cfn-amplifyuibuilder-component-componentconditionproperty-property""", alias="Property")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ComponentConditionProperty:
        from troposphere.amplifyuibuilder import ComponentConditionProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentDataConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentdataconfiguration.html
    Properties:
        - Name: Model
        - Name: Sort
        - Name: Identifiers
        - Name: Predicate
    
    """
    
    Model_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentdataconfiguration.html#cfn-amplifyuibuilder-component-componentdataconfiguration-model""", alias="Model")
    Sort_: Optional[List['SortProperty']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentdataconfiguration.html#cfn-amplifyuibuilder-component-componentdataconfiguration-sort""", alias="Sort")
    Identifiers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentdataconfiguration.html#cfn-amplifyuibuilder-component-componentdataconfiguration-identifiers""", alias="Identifiers")
    Predicate_: Optional['Predicate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentdataconfiguration.html#cfn-amplifyuibuilder-component-componentdataconfiguration-predicate""", alias="Predicate")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ComponentDataConfiguration:
        from troposphere.amplifyuibuilder import ComponentDataConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentEvent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentevent.html
    Properties:
        - Name: Action
        - Name: Parameters
    
    """
    
    Action_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentevent.html#cfn-amplifyuibuilder-component-componentevent-action""", alias="Action")
    Parameters_: Optional['ActionParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentevent.html#cfn-amplifyuibuilder-component-componentevent-parameters""", alias="Parameters")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ComponentEvent:
        from troposphere.amplifyuibuilder import ComponentEvent as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html
    Properties:
        - Name: Condition
        - Name: UserAttribute
        - Name: ImportedValue
        - Name: BindingProperties
        - Name: Bindings
        - Name: Configured
        - Name: Concat
        - Name: DefaultValue
        - Name: Type
        - Name: Value
        - Name: Model
        - Name: CollectionBindingProperties
        - Name: Event
        - Name: ComponentName
        - Name: Property
    
    """
    
    Condition_: Optional['ComponentConditionProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-condition""", alias="Condition")
    UserAttribute_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-userattribute""", alias="UserAttribute")
    ImportedValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-importedvalue""", alias="ImportedValue")
    BindingProperties_: Optional['ComponentPropertyBindingProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-bindingproperties""", alias="BindingProperties")
    Bindings_: Optional[Dict[str, 'FormBindingElement']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-bindings""", alias="Bindings")
    Configured_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-configured""", alias="Configured")
    Concat_: Optional[List['ComponentProperty']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-concat""", alias="Concat")
    DefaultValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-defaultvalue""", alias="DefaultValue")
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-type""", alias="Type")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-value""", alias="Value")
    Model_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-model""", alias="Model")
    CollectionBindingProperties_: Optional['ComponentPropertyBindingProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-collectionbindingproperties""", alias="CollectionBindingProperties")
    Event_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-event""", alias="Event")
    ComponentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-componentname""", alias="ComponentName")
    Property_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html#cfn-amplifyuibuilder-component-componentproperty-property""", alias="Property")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ComponentProperty:
        from troposphere.amplifyuibuilder import ComponentProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentPropertyBindingProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentpropertybindingproperties.html
    Properties:
        - Name: Field
        - Name: Property
    
    """
    
    Field_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentpropertybindingproperties.html#cfn-amplifyuibuilder-component-componentpropertybindingproperties-field""", alias="Field")
    Property_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentpropertybindingproperties.html#cfn-amplifyuibuilder-component-componentpropertybindingproperties-property""", alias="Property")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ComponentPropertyBindingProperties:
        from troposphere.amplifyuibuilder import ComponentPropertyBindingProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ComponentVariant(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentvariant.html
    Properties:
        - Name: VariantValues
        - Name: Overrides
    
    """
    
    VariantValues_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentvariant.html#cfn-amplifyuibuilder-component-componentvariant-variantvalues""", alias="VariantValues")
    Overrides_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentvariant.html#cfn-amplifyuibuilder-component-componentvariant-overrides""", alias="Overrides")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ComponentVariant:
        from troposphere.amplifyuibuilder import ComponentVariant as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FormBindingElement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-formbindingelement.html
    Properties:
        - Name: Element
        - Name: Property
    
    """
    
    Element_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-formbindingelement.html#cfn-amplifyuibuilder-component-formbindingelement-element""", alias="Element")
    Property_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-formbindingelement.html#cfn-amplifyuibuilder-component-formbindingelement-property""", alias="Property")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.FormBindingElement:
        from troposphere.amplifyuibuilder import FormBindingElement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MutationActionSetStateParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter.html
    Properties:
        - Name: Set
        - Name: ComponentName
        - Name: Property
    
    """
    
    Set_: 'ComponentProperty' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter.html#cfn-amplifyuibuilder-component-mutationactionsetstateparameter-set""", alias="Set")
    ComponentName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter.html#cfn-amplifyuibuilder-component-mutationactionsetstateparameter-componentname""", alias="ComponentName")
    Property_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter.html#cfn-amplifyuibuilder-component-mutationactionsetstateparameter-property""", alias="Property")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.MutationActionSetStateParameter:
        from troposphere.amplifyuibuilder import MutationActionSetStateParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Predicate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-predicate.html
    Properties:
        - Name: Operator
        - Name: Field
        - Name: Or
        - Name: And
        - Name: Operand
    
    """
    
    Operator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-predicate.html#cfn-amplifyuibuilder-component-predicate-operator""", alias="Operator")
    Field_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-predicate.html#cfn-amplifyuibuilder-component-predicate-field""", alias="Field")
    Or_: Optional[List['Predicate']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-predicate.html#cfn-amplifyuibuilder-component-predicate-or""", alias="Or")
    And_: Optional[List['Predicate']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-predicate.html#cfn-amplifyuibuilder-component-predicate-and""", alias="And")
    Operand_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-predicate.html#cfn-amplifyuibuilder-component-predicate-operand""", alias="Operand")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.Predicate:
        from troposphere.amplifyuibuilder import Predicate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SortProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-sortproperty.html
    Properties:
        - Name: Field
        - Name: Direction
    
    """
    
    Field_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-sortproperty.html#cfn-amplifyuibuilder-component-sortproperty-field""", alias="Field")
    Direction_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-sortproperty.html#cfn-amplifyuibuilder-component-sortproperty-direction""", alias="Direction")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.SortProperty:
        from troposphere.amplifyuibuilder import SortProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html
    Properties:
        - Name: Validations
        - Name: InputType
        - Name: Position
        - Name: Label
        - Name: Excluded
    
    """
    
    Validations_: Optional[List['FieldValidationConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html#cfn-amplifyuibuilder-form-fieldconfig-validations""", alias="Validations")
    InputType_: Optional['FieldInputConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html#cfn-amplifyuibuilder-form-fieldconfig-inputtype""", alias="InputType")
    Position_: Optional['FieldPosition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html#cfn-amplifyuibuilder-form-fieldconfig-position""", alias="Position")
    Label_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html#cfn-amplifyuibuilder-form-fieldconfig-label""", alias="Label")
    Excluded_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html#cfn-amplifyuibuilder-form-fieldconfig-excluded""", alias="Excluded")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.FieldConfig:
        from troposphere.amplifyuibuilder import FieldConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldInputConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html
    Properties:
        - Name: ReadOnly
        - Name: Placeholder
        - Name: FileUploaderConfig
        - Name: IsArray
        - Name: ValueMappings
        - Name: DefaultCountryCode
        - Name: MaxValue
        - Name: Step
        - Name: Name
        - Name: DefaultValue
        - Name: DescriptiveText
        - Name: Type
        - Name: Required
        - Name: MinValue
        - Name: Value
        - Name: DefaultChecked
    
    """
    
    ReadOnly_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-readonly""", alias="ReadOnly")
    Placeholder_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-placeholder""", alias="Placeholder")
    FileUploaderConfig_: Optional['FileUploaderFieldConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-fileuploaderconfig""", alias="FileUploaderConfig")
    IsArray_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-isarray""", alias="IsArray")
    ValueMappings_: Optional['ValueMappings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-valuemappings""", alias="ValueMappings")
    DefaultCountryCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-defaultcountrycode""", alias="DefaultCountryCode")
    MaxValue_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-maxvalue""", alias="MaxValue")
    Step_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-step""", alias="Step")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-name""", alias="Name")
    DefaultValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-defaultvalue""", alias="DefaultValue")
    DescriptiveText_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-descriptivetext""", alias="DescriptiveText")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-type""", alias="Type")
    Required_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-required""", alias="Required")
    MinValue_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-minvalue""", alias="MinValue")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-value""", alias="Value")
    DefaultChecked_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html#cfn-amplifyuibuilder-form-fieldinputconfig-defaultchecked""", alias="DefaultChecked")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.FieldInputConfig:
        from troposphere.amplifyuibuilder import FieldInputConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldPosition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldposition.html
    Properties:
        - Name: Below
        - Name: RightOf
        - Name: Fixed
    
    """
    
    Below_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldposition.html#cfn-amplifyuibuilder-form-fieldposition-below""", alias="Below")
    RightOf_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldposition.html#cfn-amplifyuibuilder-form-fieldposition-rightof""", alias="RightOf")
    Fixed_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldposition.html#cfn-amplifyuibuilder-form-fieldposition-fixed""", alias="Fixed")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.FieldPosition:
        from troposphere.amplifyuibuilder import FieldPosition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldValidationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html
    Properties:
        - Name: Type
        - Name: ValidationMessage
        - Name: StrValues
        - Name: NumValues
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-type""", alias="Type")
    ValidationMessage_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-validationmessage""", alias="ValidationMessage")
    StrValues_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-strvalues""", alias="StrValues")
    NumValues_: Optional[List[float]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html#cfn-amplifyuibuilder-form-fieldvalidationconfiguration-numvalues""", alias="NumValues")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.FieldValidationConfiguration:
        from troposphere.amplifyuibuilder import FieldValidationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FileUploaderFieldConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fileuploaderfieldconfig.html
    Properties:
        - Name: IsResumable
        - Name: ShowThumbnails
        - Name: AcceptedFileTypes
        - Name: MaxFileCount
        - Name: MaxSize
        - Name: AccessLevel
    
    """
    
    IsResumable_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fileuploaderfieldconfig.html#cfn-amplifyuibuilder-form-fileuploaderfieldconfig-isresumable""", alias="IsResumable")
    ShowThumbnails_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fileuploaderfieldconfig.html#cfn-amplifyuibuilder-form-fileuploaderfieldconfig-showthumbnails""", alias="ShowThumbnails")
    AcceptedFileTypes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fileuploaderfieldconfig.html#cfn-amplifyuibuilder-form-fileuploaderfieldconfig-acceptedfiletypes""", alias="AcceptedFileTypes")
    MaxFileCount_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fileuploaderfieldconfig.html#cfn-amplifyuibuilder-form-fileuploaderfieldconfig-maxfilecount""", alias="MaxFileCount")
    MaxSize_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fileuploaderfieldconfig.html#cfn-amplifyuibuilder-form-fileuploaderfieldconfig-maxsize""", alias="MaxSize")
    AccessLevel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fileuploaderfieldconfig.html#cfn-amplifyuibuilder-form-fileuploaderfieldconfig-accesslevel""", alias="AccessLevel")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.FileUploaderFieldConfig:
        from troposphere.amplifyuibuilder import FileUploaderFieldConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FormButton(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formbutton.html
    Properties:
        - Name: Position
        - Name: Children
        - Name: Excluded
    
    """
    
    Position_: Optional['FieldPosition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formbutton.html#cfn-amplifyuibuilder-form-formbutton-position""", alias="Position")
    Children_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formbutton.html#cfn-amplifyuibuilder-form-formbutton-children""", alias="Children")
    Excluded_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formbutton.html#cfn-amplifyuibuilder-form-formbutton-excluded""", alias="Excluded")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.FormButton:
        from troposphere.amplifyuibuilder import FormButton as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FormCTA(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formcta.html
    Properties:
        - Name: Position
        - Name: Cancel
        - Name: Submit
        - Name: Clear
    
    """
    
    Position_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formcta.html#cfn-amplifyuibuilder-form-formcta-position""", alias="Position")
    Cancel_: Optional['FormButton'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formcta.html#cfn-amplifyuibuilder-form-formcta-cancel""", alias="Cancel")
    Submit_: Optional['FormButton'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formcta.html#cfn-amplifyuibuilder-form-formcta-submit""", alias="Submit")
    Clear_: Optional['FormButton'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formcta.html#cfn-amplifyuibuilder-form-formcta-clear""", alias="Clear")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.FormCTA:
        from troposphere.amplifyuibuilder import FormCTA as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FormDataTypeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formdatatypeconfig.html
    Properties:
        - Name: DataSourceType
        - Name: DataTypeName
    
    """
    
    DataSourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formdatatypeconfig.html#cfn-amplifyuibuilder-form-formdatatypeconfig-datasourcetype""", alias="DataSourceType")
    DataTypeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formdatatypeconfig.html#cfn-amplifyuibuilder-form-formdatatypeconfig-datatypename""", alias="DataTypeName")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.FormDataTypeConfig:
        from troposphere.amplifyuibuilder import FormDataTypeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FormInputValueProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-forminputvalueproperty.html
    Properties:
        - Name: Value
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-forminputvalueproperty.html#cfn-amplifyuibuilder-form-forminputvalueproperty-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.FormInputValueProperty:
        from troposphere.amplifyuibuilder import FormInputValueProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FormStyle(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyle.html
    Properties:
        - Name: VerticalGap
        - Name: OuterPadding
        - Name: HorizontalGap
    
    """
    
    VerticalGap_: Optional['FormStyleConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyle.html#cfn-amplifyuibuilder-form-formstyle-verticalgap""", alias="VerticalGap")
    OuterPadding_: Optional['FormStyleConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyle.html#cfn-amplifyuibuilder-form-formstyle-outerpadding""", alias="OuterPadding")
    HorizontalGap_: Optional['FormStyleConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyle.html#cfn-amplifyuibuilder-form-formstyle-horizontalgap""", alias="HorizontalGap")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.FormStyle:
        from troposphere.amplifyuibuilder import FormStyle as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FormStyleConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyleconfig.html
    Properties:
        - Name: Value
        - Name: TokenReference
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyleconfig.html#cfn-amplifyuibuilder-form-formstyleconfig-value""", alias="Value")
    TokenReference_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyleconfig.html#cfn-amplifyuibuilder-form-formstyleconfig-tokenreference""", alias="TokenReference")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.FormStyleConfig:
        from troposphere.amplifyuibuilder import FormStyleConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SectionalElement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html
    Properties:
        - Name: Type
        - Name: Position
        - Name: Text
        - Name: Level
        - Name: Orientation
        - Name: Excluded
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html#cfn-amplifyuibuilder-form-sectionalelement-type""", alias="Type")
    Position_: Optional['FieldPosition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html#cfn-amplifyuibuilder-form-sectionalelement-position""", alias="Position")
    Text_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html#cfn-amplifyuibuilder-form-sectionalelement-text""", alias="Text")
    Level_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html#cfn-amplifyuibuilder-form-sectionalelement-level""", alias="Level")
    Orientation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html#cfn-amplifyuibuilder-form-sectionalelement-orientation""", alias="Orientation")
    Excluded_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html#cfn-amplifyuibuilder-form-sectionalelement-excluded""", alias="Excluded")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.SectionalElement:
        from troposphere.amplifyuibuilder import SectionalElement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ValueMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemapping.html
    Properties:
        - Name: DisplayValue
        - Name: Value
    
    """
    
    DisplayValue_: Optional['FormInputValueProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemapping.html#cfn-amplifyuibuilder-form-valuemapping-displayvalue""", alias="DisplayValue")
    Value_: 'FormInputValueProperty' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemapping.html#cfn-amplifyuibuilder-form-valuemapping-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ValueMapping:
        from troposphere.amplifyuibuilder import ValueMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ValueMappings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemappings.html
    Properties:
        - Name: Values
    
    """
    
    Values_: List['ValueMapping'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemappings.html#cfn-amplifyuibuilder-form-valuemappings-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ValueMappings:
        from troposphere.amplifyuibuilder import ValueMappings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ThemeValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalue.html
    Properties:
        - Name: Value
        - Name: Children
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalue.html#cfn-amplifyuibuilder-theme-themevalue-value""", alias="Value")
    Children_: Optional[List['ThemeValues']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalue.html#cfn-amplifyuibuilder-theme-themevalue-children""", alias="Children")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ThemeValue:
        from troposphere.amplifyuibuilder import ThemeValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ThemeValues(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalues.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional['ThemeValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalues.html#cfn-amplifyuibuilder-theme-themevalues-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalues.html#cfn-amplifyuibuilder-theme-themevalues-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.ThemeValues:
        from troposphere.amplifyuibuilder import ThemeValues as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Component(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html
    Properties:
        - Name: ComponentType
        - Name: SchemaVersion
        - Name: EnvironmentName
        - Name: BindingProperties
        - Name: SourceId
        - Name: Properties
        - Name: CollectionProperties
        - Name: Name
        - Name: Variants
        - Name: AppId
        - Name: Events
        - Name: Overrides
        - Name: Children
        - Name: Tags
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ComponentType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-componenttype""", alias="ComponentType")
    SchemaVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-schemaversion""", alias="SchemaVersion")
    EnvironmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-environmentname""", alias="EnvironmentName")
    BindingProperties_: Dict[str, 'ComponentBindingPropertiesValue'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-bindingproperties""", alias="BindingProperties")
    SourceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-sourceid""", alias="SourceId")
    Properties_: Dict[str, 'ComponentProperty'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-properties""", alias="Properties")
    CollectionProperties_: Optional[Dict[str, 'ComponentDataConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-collectionproperties""", alias="CollectionProperties")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-name""", alias="Name")
    Variants_: List['ComponentVariant'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-variants""", alias="Variants")
    AppId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-appid""", alias="AppId")
    Events_: Optional[Dict[str, 'ComponentEvent']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-events""", alias="Events")
    Overrides_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-overrides""", alias="Overrides")
    Children_: Optional[List['ComponentChild']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-children""", alias="Children")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html#cfn-amplifyuibuilder-component-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.Component:
        from troposphere.amplifyuibuilder import Component as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.amplifyuibuilder import Component as TropoT
        return resource_to_troposphere(self, TropoT)


class Form(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html
    Properties:
        - Name: FormActionType
        - Name: Cta
        - Name: Fields
        - Name: SchemaVersion
        - Name: AppId
        - Name: EnvironmentName
        - Name: LabelDecorator
        - Name: SectionalElements
        - Name: DataType
        - Name: Style
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FormActionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-formactiontype""", alias="FormActionType")
    Cta_: Optional['FormCTA'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-cta""", alias="Cta")
    Fields_: Dict[str, 'FieldConfig'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-fields""", alias="Fields")
    SchemaVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-schemaversion""", alias="SchemaVersion")
    AppId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-appid""", alias="AppId")
    EnvironmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-environmentname""", alias="EnvironmentName")
    LabelDecorator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-labeldecorator""", alias="LabelDecorator")
    SectionalElements_: Dict[str, 'SectionalElement'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-sectionalelements""", alias="SectionalElements")
    DataType_: 'FormDataTypeConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-datatype""", alias="DataType")
    Style_: 'FormStyle' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-style""", alias="Style")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html#cfn-amplifyuibuilder-form-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.Form:
        from troposphere.amplifyuibuilder import Form as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.amplifyuibuilder import Form as TropoT
        return resource_to_troposphere(self, TropoT)


class Theme(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html
    Properties:
        - Name: AppId
        - Name: EnvironmentName
        - Name: Values
        - Name: Overrides
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AppId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-appid""", alias="AppId")
    EnvironmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-environmentname""", alias="EnvironmentName")
    Values_: List['ThemeValues'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-values""", alias="Values")
    Overrides_: Optional[List['ThemeValues']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-overrides""", alias="Overrides")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html#cfn-amplifyuibuilder-theme-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.amplifyuibuilder.Theme:
        from troposphere.amplifyuibuilder import Theme as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.amplifyuibuilder import Theme as TropoT
        return resource_to_troposphere(self, TropoT)

