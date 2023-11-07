from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ByteMatchTuple(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html
    Properties:
        - Name: FieldToMatch
        - Name: PositionalConstraint
        - Name: TargetString
        - Name: TargetStringBase64
        - Name: TextTransformation
    
    """
    
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch""", alias="FieldToMatch")
    PositionalConstraint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-positionalconstraint""", alias="PositionalConstraint")
    TargetString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-targetstring""", alias="TargetString")
    TargetStringBase64_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-targetstringbase64""", alias="TargetStringBase64")
    TextTransformation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-texttransformation""", alias="TextTransformation")
    


    @property
    def tropo_type(self) -> troposphere.waf.ByteMatchTuple:
        from troposphere.waf import ByteMatchTuple as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldToMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html
    Properties:
        - Name: Data
        - Name: Type
    
    """
    
    Data_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch-data""", alias="Data")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.waf.FieldToMatch:
        from troposphere.waf import FieldToMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IPSetDescriptor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-type""", alias="Type")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.waf.IPSetDescriptor:
        from troposphere.waf import IPSetDescriptor as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Predicate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html
    Properties:
        - Name: DataId
        - Name: Negated
        - Name: Type
    
    """
    
    DataId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-dataid""", alias="DataId")
    Negated_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-negated""", alias="Negated")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.waf.Predicate:
        from troposphere.waf import Predicate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldToMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html
    Properties:
        - Name: Data
        - Name: Type
    
    """
    
    Data_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-data""", alias="Data")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.waf.FieldToMatch:
        from troposphere.waf import FieldToMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SizeConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html
    Properties:
        - Name: ComparisonOperator
        - Name: FieldToMatch
        - Name: Size
        - Name: TextTransformation
    
    """
    
    ComparisonOperator_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-comparisonoperator""", alias="ComparisonOperator")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch""", alias="FieldToMatch")
    Size_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-size""", alias="Size")
    TextTransformation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-texttransformation""", alias="TextTransformation")
    


    @property
    def tropo_type(self) -> troposphere.waf.SizeConstraint:
        from troposphere.waf import SizeConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldToMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html
    Properties:
        - Name: Data
        - Name: Type
    
    """
    
    Data_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-data""", alias="Data")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.waf.FieldToMatch:
        from troposphere.waf import FieldToMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SqlInjectionMatchTuple(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html
    Properties:
        - Name: FieldToMatch
        - Name: TextTransformation
    
    """
    
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples-fieldtomatch""", alias="FieldToMatch")
    TextTransformation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples-texttransformation""", alias="TextTransformation")
    


    @property
    def tropo_type(self) -> troposphere.waf.SqlInjectionMatchTuple:
        from troposphere.waf import SqlInjectionMatchTuple as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ActivatedRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html
    Properties:
        - Name: Action
        - Name: Priority
        - Name: RuleId
    
    """
    
    Action_: Optional['WafAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-action""", alias="Action")
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-priority""", alias="Priority")
    RuleId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-ruleid""", alias="RuleId")
    


    @property
    def tropo_type(self) -> troposphere.waf.ActivatedRule:
        from troposphere.waf import ActivatedRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WafAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-action.html
    Properties:
        - Name: Type
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-action.html#cfn-waf-webacl-action-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.waf.WafAction:
        from troposphere.waf import WafAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldToMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html
    Properties:
        - Name: Data
        - Name: Type
    
    """
    
    Data_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch-data""", alias="Data")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.waf.FieldToMatch:
        from troposphere.waf import FieldToMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class XssMatchTuple(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html
    Properties:
        - Name: FieldToMatch
        - Name: TextTransformation
    
    """
    
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch""", alias="FieldToMatch")
    TextTransformation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html#cfn-waf-xssmatchset-xssmatchtuple-texttransformation""", alias="TextTransformation")
    


    @property
    def tropo_type(self) -> troposphere.waf.XssMatchTuple:
        from troposphere.waf import XssMatchTuple as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ByteMatchSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html
    Properties:
        - Name: ByteMatchTuples
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ByteMatchTuples_: Optional[List['ByteMatchTuple']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-bytematchtuples""", alias="ByteMatchTuples")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.waf.ByteMatchSet:
        from troposphere.waf import ByteMatchSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.waf import ByteMatchSet as TropoT
        return resource_to_troposphere(self, TropoT)


class IPSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html
    Properties:
        - Name: IPSetDescriptors
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IPSetDescriptors_: Optional[List['IPSetDescriptor']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-ipsetdescriptors""", alias="IPSetDescriptors")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.waf.IPSet:
        from troposphere.waf import IPSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.waf import IPSet as TropoT
        return resource_to_troposphere(self, TropoT)


class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html
    Properties:
        - Name: MetricName
        - Name: Name
        - Name: Predicates
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-metricname""", alias="MetricName")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-name""", alias="Name")
    Predicates_: Optional[List['Predicate']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-predicates""", alias="Predicates")
    

    @property
    def tropo_type(self) -> troposphere.waf.Rule:
        from troposphere.waf import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.waf import Rule as TropoT
        return resource_to_troposphere(self, TropoT)


class SizeConstraintSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html
    Properties:
        - Name: Name
        - Name: SizeConstraints
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-name""", alias="Name")
    SizeConstraints_: List['SizeConstraint'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-sizeconstraints""", alias="SizeConstraints")
    

    @property
    def tropo_type(self) -> troposphere.waf.SizeConstraintSet:
        from troposphere.waf import SizeConstraintSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.waf import SizeConstraintSet as TropoT
        return resource_to_troposphere(self, TropoT)


class SqlInjectionMatchSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html
    Properties:
        - Name: Name
        - Name: SqlInjectionMatchTuples
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-name""", alias="Name")
    SqlInjectionMatchTuples_: Optional[List['SqlInjectionMatchTuple']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples""", alias="SqlInjectionMatchTuples")
    

    @property
    def tropo_type(self) -> troposphere.waf.SqlInjectionMatchSet:
        from troposphere.waf import SqlInjectionMatchSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.waf import SqlInjectionMatchSet as TropoT
        return resource_to_troposphere(self, TropoT)


class WebACL(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html
    Properties:
        - Name: DefaultAction
        - Name: MetricName
        - Name: Name
        - Name: Rules
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DefaultAction_: 'WafAction' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-defaultaction""", alias="DefaultAction")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-metricname""", alias="MetricName")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-name""", alias="Name")
    Rules_: Optional[List['ActivatedRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-rules""", alias="Rules")
    

    @property
    def tropo_type(self) -> troposphere.waf.WebACL:
        from troposphere.waf import WebACL as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.waf import WebACL as TropoT
        return resource_to_troposphere(self, TropoT)


class XssMatchSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html
    Properties:
        - Name: Name
        - Name: XssMatchTuples
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-name""", alias="Name")
    XssMatchTuples_: List['XssMatchTuple'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-xssmatchtuples""", alias="XssMatchTuples")
    

    @property
    def tropo_type(self) -> troposphere.waf.XssMatchSet:
        from troposphere.waf import XssMatchSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.waf import XssMatchSet as TropoT
        return resource_to_troposphere(self, TropoT)

