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
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html
    Properties:
        - Name: TargetString
        - Name: TargetStringBase64
        - Name: PositionalConstraint
        - Name: TextTransformation
        - Name: FieldToMatch
    
    """
    
    TargetString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-targetstring""", alias="TargetString")
    TargetStringBase64_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-targetstringbase64""", alias="TargetStringBase64")
    PositionalConstraint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-positionalconstraint""", alias="PositionalConstraint")
    TextTransformation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-texttransformation""", alias="TextTransformation")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.ByteMatchTuple:
        from troposphere.wafregional import ByteMatchTuple as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldToMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html
    Properties:
        - Name: Type
        - Name: Data
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html#cfn-wafregional-bytematchset-fieldtomatch-type""", alias="Type")
    Data_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html#cfn-wafregional-bytematchset-fieldtomatch-data""", alias="Data")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.FieldToMatch:
        from troposphere.wafregional import FieldToMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GeoMatchConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html#cfn-wafregional-geomatchset-geomatchconstraint-type""", alias="Type")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html#cfn-wafregional-geomatchset-geomatchconstraint-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.GeoMatchConstraint:
        from troposphere.wafregional import GeoMatchConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IPSetDescriptor(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html#cfn-wafregional-ipset-ipsetdescriptor-type""", alias="Type")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html#cfn-wafregional-ipset-ipsetdescriptor-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.IPSetDescriptor:
        from troposphere.wafregional import IPSetDescriptor as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Predicate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html
    Properties:
        - Name: Type
        - Name: DataId
        - Name: Negated
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html#cfn-wafregional-ratebasedrule-predicate-type""", alias="Type")
    DataId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html#cfn-wafregional-ratebasedrule-predicate-dataid""", alias="DataId")
    Negated_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html#cfn-wafregional-ratebasedrule-predicate-negated""", alias="Negated")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.Predicate:
        from troposphere.wafregional import Predicate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Predicate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html
    Properties:
        - Name: Type
        - Name: DataId
        - Name: Negated
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-type""", alias="Type")
    DataId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-dataid""", alias="DataId")
    Negated_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-negated""", alias="Negated")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.Predicate:
        from troposphere.wafregional import Predicate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldToMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html
    Properties:
        - Name: Type
        - Name: Data
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html#cfn-wafregional-sizeconstraintset-fieldtomatch-type""", alias="Type")
    Data_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html#cfn-wafregional-sizeconstraintset-fieldtomatch-data""", alias="Data")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.FieldToMatch:
        from troposphere.wafregional import FieldToMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SizeConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html
    Properties:
        - Name: ComparisonOperator
        - Name: Size
        - Name: TextTransformation
        - Name: FieldToMatch
    
    """
    
    ComparisonOperator_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-comparisonoperator""", alias="ComparisonOperator")
    Size_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-size""", alias="Size")
    TextTransformation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-texttransformation""", alias="TextTransformation")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.SizeConstraint:
        from troposphere.wafregional import SizeConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldToMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html
    Properties:
        - Name: Type
        - Name: Data
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html#cfn-wafregional-sqlinjectionmatchset-fieldtomatch-type""", alias="Type")
    Data_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html#cfn-wafregional-sqlinjectionmatchset-fieldtomatch-data""", alias="Data")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.FieldToMatch:
        from troposphere.wafregional import FieldToMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SqlInjectionMatchTuple(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html
    Properties:
        - Name: TextTransformation
        - Name: FieldToMatch
    
    """
    
    TextTransformation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple-texttransformation""", alias="TextTransformation")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.SqlInjectionMatchTuple:
        from troposphere.wafregional import SqlInjectionMatchTuple as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-action.html
    Properties:
        - Name: Type
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-action.html#cfn-wafregional-webacl-action-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.Action:
        from troposphere.wafregional import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html
    Properties:
        - Name: Action
        - Name: Priority
        - Name: RuleId
    
    """
    
    Action_: 'Action' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-action""", alias="Action")
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-priority""", alias="Priority")
    RuleId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-ruleid""", alias="RuleId")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.Rule:
        from troposphere.wafregional import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldToMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html
    Properties:
        - Name: Type
        - Name: Data
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html#cfn-wafregional-xssmatchset-fieldtomatch-type""", alias="Type")
    Data_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html#cfn-wafregional-xssmatchset-fieldtomatch-data""", alias="Data")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.FieldToMatch:
        from troposphere.wafregional import FieldToMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class XssMatchTuple(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html
    Properties:
        - Name: TextTransformation
        - Name: FieldToMatch
    
    """
    
    TextTransformation_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html#cfn-wafregional-xssmatchset-xssmatchtuple-texttransformation""", alias="TextTransformation")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html#cfn-wafregional-xssmatchset-xssmatchtuple-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafregional.XssMatchTuple:
        from troposphere.wafregional import XssMatchTuple as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ByteMatchSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html
    Properties:
        - Name: ByteMatchTuples
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ByteMatchTuples_: Optional[List['ByteMatchTuple']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html#cfn-wafregional-bytematchset-bytematchtuples""", alias="ByteMatchTuples")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html#cfn-wafregional-bytematchset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafregional.ByteMatchSet:
        from troposphere.wafregional import ByteMatchSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafregional import ByteMatchSet as TropoT
        return resource_to_troposphere(self, TropoT)


class GeoMatchSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html
    Properties:
        - Name: GeoMatchConstraints
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GeoMatchConstraints_: Optional[List['GeoMatchConstraint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html#cfn-wafregional-geomatchset-geomatchconstraints""", alias="GeoMatchConstraints")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html#cfn-wafregional-geomatchset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafregional.GeoMatchSet:
        from troposphere.wafregional import GeoMatchSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafregional import GeoMatchSet as TropoT
        return resource_to_troposphere(self, TropoT)


class IPSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html
    Properties:
        - Name: IPSetDescriptors
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IPSetDescriptors_: Optional[List['IPSetDescriptor']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html#cfn-wafregional-ipset-ipsetdescriptors""", alias="IPSetDescriptors")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html#cfn-wafregional-ipset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafregional.IPSet:
        from troposphere.wafregional import IPSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafregional import IPSet as TropoT
        return resource_to_troposphere(self, TropoT)


class RateBasedRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html
    Properties:
        - Name: MetricName
        - Name: RateLimit
        - Name: MatchPredicates
        - Name: RateKey
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-metricname""", alias="MetricName")
    RateLimit_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-ratelimit""", alias="RateLimit")
    MatchPredicates_: Optional[List['Predicate']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-matchpredicates""", alias="MatchPredicates")
    RateKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-ratekey""", alias="RateKey")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafregional.RateBasedRule:
        from troposphere.wafregional import RateBasedRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafregional import RateBasedRule as TropoT
        return resource_to_troposphere(self, TropoT)


class RegexPatternSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html
    Properties:
        - Name: RegexPatternStrings
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RegexPatternStrings_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html#cfn-wafregional-regexpatternset-regexpatternstrings""", alias="RegexPatternStrings")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html#cfn-wafregional-regexpatternset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafregional.RegexPatternSet:
        from troposphere.wafregional import RegexPatternSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafregional import RegexPatternSet as TropoT
        return resource_to_troposphere(self, TropoT)


class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html
    Properties:
        - Name: MetricName
        - Name: Predicates
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-metricname""", alias="MetricName")
    Predicates_: Optional[List['Predicate']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-predicates""", alias="Predicates")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafregional.Rule:
        from troposphere.wafregional import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafregional import Rule as TropoT
        return resource_to_troposphere(self, TropoT)


class SizeConstraintSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html
    Properties:
        - Name: SizeConstraints
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SizeConstraints_: Optional[List['SizeConstraint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html#cfn-wafregional-sizeconstraintset-sizeconstraints""", alias="SizeConstraints")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html#cfn-wafregional-sizeconstraintset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafregional.SizeConstraintSet:
        from troposphere.wafregional import SizeConstraintSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafregional import SizeConstraintSet as TropoT
        return resource_to_troposphere(self, TropoT)


class SqlInjectionMatchSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html
    Properties:
        - Name: SqlInjectionMatchTuples
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SqlInjectionMatchTuples_: Optional[List['SqlInjectionMatchTuple']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuples""", alias="SqlInjectionMatchTuples")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html#cfn-wafregional-sqlinjectionmatchset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafregional.SqlInjectionMatchSet:
        from troposphere.wafregional import SqlInjectionMatchSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafregional import SqlInjectionMatchSet as TropoT
        return resource_to_troposphere(self, TropoT)


class WebACL(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html
    Properties:
        - Name: MetricName
        - Name: DefaultAction
        - Name: Rules
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-metricname""", alias="MetricName")
    DefaultAction_: 'Action' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-defaultaction""", alias="DefaultAction")
    Rules_: Optional[List['Rule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-rules""", alias="Rules")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafregional.WebACL:
        from troposphere.wafregional import WebACL as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafregional import WebACL as TropoT
        return resource_to_troposphere(self, TropoT)


class WebACLAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html
    Properties:
        - Name: ResourceArn
        - Name: WebACLId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html#cfn-wafregional-webaclassociation-resourcearn""", alias="ResourceArn")
    WebACLId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html#cfn-wafregional-webaclassociation-webaclid""", alias="WebACLId")
    

    @property
    def tropo_type(self) -> troposphere.wafregional.WebACLAssociation:
        from troposphere.wafregional import WebACLAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafregional import WebACLAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class XssMatchSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html
    Properties:
        - Name: XssMatchTuples
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    XssMatchTuples_: Optional[List['XssMatchTuple']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html#cfn-wafregional-xssmatchset-xssmatchtuples""", alias="XssMatchTuples")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html#cfn-wafregional-xssmatchset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafregional.XssMatchSet:
        from troposphere.wafregional import XssMatchSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafregional import XssMatchSet as TropoT
        return resource_to_troposphere(self, TropoT)

