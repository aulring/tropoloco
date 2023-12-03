from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ActionCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-actioncondition.html
    Properties:
        - Name: Action
    
    """
    
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-actioncondition.html#cfn-wafv2-loggingconfiguration-actioncondition-action""", alias="Action")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ActionCondition:
        from troposphere.wafv2 import ActionCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Condition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-condition.html
    Properties:
        - Name: LabelNameCondition
        - Name: ActionCondition
    
    """
    
    LabelNameCondition_: Optional['LabelNameCondition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-condition.html#cfn-wafv2-loggingconfiguration-condition-labelnamecondition""", alias="LabelNameCondition")
    ActionCondition_: Optional['ActionCondition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-condition.html#cfn-wafv2-loggingconfiguration-condition-actioncondition""", alias="ActionCondition")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Condition:
        from troposphere.wafv2 import Condition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggingConfigurationFieldToMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html
    Properties:
        - Name: JsonBody
        - Name: QueryString
        - Name: UriPath
        - Name: Method
        - Name: SingleHeader
    8
    """
    
    JsonBody_: Optional['JsonBody'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-jsonbody""", alias="JsonBody")
    QueryString_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-querystring""", alias="QueryString")
    UriPath_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-uripath""", alias="UriPath")
    Method_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-method""", alias="Method")
    SingleHeader_: Optional['SingleHeader'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-singleheader""", alias="SingleHeader")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.LoggingConfigurationFieldToMatch:
        from troposphere.wafv2 import LoggingConfigurationFieldToMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Filter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-filter.html
    Properties:
        - Name: Requirement
        - Name: Behavior
        - Name: Conditions
    
    """
    
    Requirement_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-filter.html#cfn-wafv2-loggingconfiguration-filter-requirement""", alias="Requirement")
    Behavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-filter.html#cfn-wafv2-loggingconfiguration-filter-behavior""", alias="Behavior")
    Conditions_: List['Condition'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-filter.html#cfn-wafv2-loggingconfiguration-filter-conditions""", alias="Conditions")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Filter:
        from troposphere.wafv2 import Filter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JsonBody(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-jsonbody.html
    Properties:
        - Name: MatchScope
        - Name: InvalidFallbackBehavior
        - Name: MatchPattern
    
    """
    
    MatchScope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-jsonbody.html#cfn-wafv2-loggingconfiguration-jsonbody-matchscope""", alias="MatchScope")
    InvalidFallbackBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-jsonbody.html#cfn-wafv2-loggingconfiguration-jsonbody-invalidfallbackbehavior""", alias="InvalidFallbackBehavior")
    MatchPattern_: 'MatchPattern' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-jsonbody.html#cfn-wafv2-loggingconfiguration-jsonbody-matchpattern""", alias="MatchPattern")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.JsonBody:
        from troposphere.wafv2 import JsonBody as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LabelNameCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-labelnamecondition.html
    Properties:
        - Name: LabelName
    
    """
    
    LabelName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-labelnamecondition.html#cfn-wafv2-loggingconfiguration-labelnamecondition-labelname""", alias="LabelName")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.LabelNameCondition:
        from troposphere.wafv2 import LabelNameCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggingFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-loggingfilter.html
    Properties:
        - Name: Filters
        - Name: DefaultBehavior
    
    """
    
    Filters_: List['Filter'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-loggingfilter.html#cfn-wafv2-loggingconfiguration-loggingfilter-filters""", alias="Filters")
    DefaultBehavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-loggingfilter.html#cfn-wafv2-loggingconfiguration-loggingfilter-defaultbehavior""", alias="DefaultBehavior")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.LoggingFilter:
        from troposphere.wafv2 import LoggingFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MatchPattern(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-matchpattern.html
    Properties:
        - Name: All
        - Name: IncludedPaths
    
    """
    
    All_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-matchpattern.html#cfn-wafv2-loggingconfiguration-matchpattern-all""", alias="All")
    IncludedPaths_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-matchpattern.html#cfn-wafv2-loggingconfiguration-matchpattern-includedpaths""", alias="IncludedPaths")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.MatchPattern:
        from troposphere.wafv2 import MatchPattern as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SingleHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-singleheader.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-singleheader.html#cfn-wafv2-loggingconfiguration-singleheader-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.SingleHeader:
        from troposphere.wafv2 import SingleHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AllowAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-allowaction.html
    Properties:
        - Name: CustomRequestHandling
    
    """
    
    CustomRequestHandling_: Optional['CustomRequestHandling'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-allowaction.html#cfn-wafv2-rulegroup-allowaction-customrequesthandling""", alias="CustomRequestHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.AllowAction:
        from troposphere.wafv2 import AllowAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AndStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatement.html
    Properties:
        - Name: Statements
    
    """
    
    Statements_: List['Statement'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatement.html#cfn-wafv2-rulegroup-andstatement-statements""", alias="Statements")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.AndStatement:
        from troposphere.wafv2 import AndStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BlockAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-blockaction.html
    Properties:
        - Name: CustomResponse
    
    """
    
    CustomResponse_: Optional['CustomResponse'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-blockaction.html#cfn-wafv2-rulegroup-blockaction-customresponse""", alias="CustomResponse")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.BlockAction:
        from troposphere.wafv2 import BlockAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Body(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-body.html
    Properties:
        - Name: OversizeHandling
    
    """
    
    OversizeHandling_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-body.html#cfn-wafv2-rulegroup-body-oversizehandling""", alias="OversizeHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Body:
        from troposphere.wafv2 import Body as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ByteMatchStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html
    Properties:
        - Name: SearchStringBase64
        - Name: TextTransformations
        - Name: PositionalConstraint
        - Name: SearchString
        - Name: FieldToMatch
    
    """
    
    SearchStringBase64_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-searchstringbase64""", alias="SearchStringBase64")
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-texttransformations""", alias="TextTransformations")
    PositionalConstraint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-positionalconstraint""", alias="PositionalConstraint")
    SearchString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-searchstring""", alias="SearchString")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ByteMatchStatement:
        from troposphere.wafv2 import ByteMatchStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CaptchaAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-captchaaction.html
    Properties:
        - Name: CustomRequestHandling
    
    """
    
    CustomRequestHandling_: Optional['CustomRequestHandling'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-captchaaction.html#cfn-wafv2-rulegroup-captchaaction-customrequesthandling""", alias="CustomRequestHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CaptchaAction:
        from troposphere.wafv2 import CaptchaAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CaptchaConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-captchaconfig.html
    Properties:
        - Name: ImmunityTimeProperty
    
    """
    
    ImmunityTimeProperty_: Optional['ImmunityTimeProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-captchaconfig.html#cfn-wafv2-rulegroup-captchaconfig-immunitytimeproperty""", alias="ImmunityTimeProperty")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CaptchaConfig:
        from troposphere.wafv2 import CaptchaConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ChallengeAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-challengeaction.html
    Properties:
        - Name: CustomRequestHandling
    
    """
    
    CustomRequestHandling_: Optional['CustomRequestHandling'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-challengeaction.html#cfn-wafv2-rulegroup-challengeaction-customrequesthandling""", alias="CustomRequestHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ChallengeAction:
        from troposphere.wafv2 import ChallengeAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ChallengeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-challengeconfig.html
    Properties:
        - Name: ImmunityTimeProperty
    
    """
    
    ImmunityTimeProperty_: Optional['ImmunityTimeProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-challengeconfig.html#cfn-wafv2-rulegroup-challengeconfig-immunitytimeproperty""", alias="ImmunityTimeProperty")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ChallengeConfig:
        from troposphere.wafv2 import ChallengeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CookieMatchPattern(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-cookiematchpattern.html
    Properties:
        - Name: All
        - Name: IncludedCookies
        - Name: ExcludedCookies
    
    """
    
    All_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-cookiematchpattern.html#cfn-wafv2-rulegroup-cookiematchpattern-all""", alias="All")
    IncludedCookies_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-cookiematchpattern.html#cfn-wafv2-rulegroup-cookiematchpattern-includedcookies""", alias="IncludedCookies")
    ExcludedCookies_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-cookiematchpattern.html#cfn-wafv2-rulegroup-cookiematchpattern-excludedcookies""", alias="ExcludedCookies")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CookieMatchPattern:
        from troposphere.wafv2 import CookieMatchPattern as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Cookies(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-cookies.html
    Properties:
        - Name: MatchScope
        - Name: MatchPattern
        - Name: OversizeHandling
    
    """
    
    MatchScope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-cookies.html#cfn-wafv2-rulegroup-cookies-matchscope""", alias="MatchScope")
    MatchPattern_: 'CookieMatchPattern' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-cookies.html#cfn-wafv2-rulegroup-cookies-matchpattern""", alias="MatchPattern")
    OversizeHandling_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-cookies.html#cfn-wafv2-rulegroup-cookies-oversizehandling""", alias="OversizeHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Cookies:
        from troposphere.wafv2 import Cookies as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CountAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-countaction.html
    Properties:
        - Name: CustomRequestHandling
    
    """
    
    CustomRequestHandling_: Optional['CustomRequestHandling'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-countaction.html#cfn-wafv2-rulegroup-countaction-customrequesthandling""", alias="CustomRequestHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CountAction:
        from troposphere.wafv2 import CountAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomHTTPHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customhttpheader.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customhttpheader.html#cfn-wafv2-rulegroup-customhttpheader-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customhttpheader.html#cfn-wafv2-rulegroup-customhttpheader-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CustomHTTPHeader:
        from troposphere.wafv2 import CustomHTTPHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomRequestHandling(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customrequesthandling.html
    Properties:
        - Name: InsertHeaders
    
    """
    
    InsertHeaders_: List['CustomHTTPHeader'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customrequesthandling.html#cfn-wafv2-rulegroup-customrequesthandling-insertheaders""", alias="InsertHeaders")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CustomRequestHandling:
        from troposphere.wafv2 import CustomRequestHandling as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomResponse(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponse.html
    Properties:
        - Name: ResponseCode
        - Name: CustomResponseBodyKey
        - Name: ResponseHeaders
    
    """
    
    ResponseCode_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponse.html#cfn-wafv2-rulegroup-customresponse-responsecode""", alias="ResponseCode")
    CustomResponseBodyKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponse.html#cfn-wafv2-rulegroup-customresponse-customresponsebodykey""", alias="CustomResponseBodyKey")
    ResponseHeaders_: Optional[List['CustomHTTPHeader']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponse.html#cfn-wafv2-rulegroup-customresponse-responseheaders""", alias="ResponseHeaders")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CustomResponse:
        from troposphere.wafv2 import CustomResponse as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomResponseBody(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebody.html
    Properties:
        - Name: ContentType
        - Name: Content
    
    """
    
    ContentType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebody.html#cfn-wafv2-rulegroup-customresponsebody-contenttype""", alias="ContentType")
    Content_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebody.html#cfn-wafv2-rulegroup-customresponsebody-content""", alias="Content")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CustomResponseBody:
        from troposphere.wafv2 import CustomResponseBody as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleGroupFieldToMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html
    Properties:
        - Name: JsonBody
        - Name: AllQueryArguments
        - Name: SingleQueryArgument
        - Name: UriPath
        - Name: QueryString
        - Name: Headers
        - Name: Cookies
        - Name: Method
        - Name: Body
        - Name: SingleHeader
    
    """
    
    JsonBody_: Optional['JsonBody'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-jsonbody""", alias="JsonBody")
    AllQueryArguments_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-allqueryarguments""", alias="AllQueryArguments")
    SingleQueryArgument_: Optional['SingleQueryArgument'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-singlequeryargument""", alias="SingleQueryArgument")
    UriPath_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-uripath""", alias="UriPath")
    QueryString_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-querystring""", alias="QueryString")
    Headers_: Optional['Headers'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-headers""", alias="Headers")
    Cookies_: Optional['Cookies'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-cookies""", alias="Cookies")
    Method_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-method""", alias="Method")
    Body_: Optional['Body'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-body""", alias="Body")
    SingleHeader_: Optional['SingleHeader'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-singleheader""", alias="SingleHeader")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RuleGroupFieldToMatch:
        from troposphere.wafv2 import RuleGroupFieldToMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ForwardedIPConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html
    Properties:
        - Name: FallbackBehavior
        - Name: HeaderName
    
    """
    
    FallbackBehavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html#cfn-wafv2-rulegroup-forwardedipconfiguration-fallbackbehavior""", alias="FallbackBehavior")
    HeaderName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html#cfn-wafv2-rulegroup-forwardedipconfiguration-headername""", alias="HeaderName")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ForwardedIPConfiguration:
        from troposphere.wafv2 import ForwardedIPConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GeoMatchStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html
    Properties:
        - Name: ForwardedIPConfig
        - Name: CountryCodes
    
    """
    
    ForwardedIPConfig_: Optional['ForwardedIPConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html#cfn-wafv2-rulegroup-geomatchstatement-forwardedipconfig""", alias="ForwardedIPConfig")
    CountryCodes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html#cfn-wafv2-rulegroup-geomatchstatement-countrycodes""", alias="CountryCodes")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.GeoMatchStatement:
        from troposphere.wafv2 import GeoMatchStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HeaderMatchPattern(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-headermatchpattern.html
    Properties:
        - Name: All
        - Name: IncludedHeaders
        - Name: ExcludedHeaders
    
    """
    
    All_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-headermatchpattern.html#cfn-wafv2-rulegroup-headermatchpattern-all""", alias="All")
    IncludedHeaders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-headermatchpattern.html#cfn-wafv2-rulegroup-headermatchpattern-includedheaders""", alias="IncludedHeaders")
    ExcludedHeaders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-headermatchpattern.html#cfn-wafv2-rulegroup-headermatchpattern-excludedheaders""", alias="ExcludedHeaders")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.HeaderMatchPattern:
        from troposphere.wafv2 import HeaderMatchPattern as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Headers(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-headers.html
    Properties:
        - Name: MatchScope
        - Name: MatchPattern
        - Name: OversizeHandling
    
    """
    
    MatchScope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-headers.html#cfn-wafv2-rulegroup-headers-matchscope""", alias="MatchScope")
    MatchPattern_: 'HeaderMatchPattern' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-headers.html#cfn-wafv2-rulegroup-headers-matchpattern""", alias="MatchPattern")
    OversizeHandling_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-headers.html#cfn-wafv2-rulegroup-headers-oversizehandling""", alias="OversizeHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Headers:
        from troposphere.wafv2 import Headers as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IPSetForwardedIPConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html
    Properties:
        - Name: FallbackBehavior
        - Name: HeaderName
        - Name: Position
    
    """
    
    FallbackBehavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-fallbackbehavior""", alias="FallbackBehavior")
    HeaderName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-headername""", alias="HeaderName")
    Position_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-position""", alias="Position")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.IPSetForwardedIPConfiguration:
        from troposphere.wafv2 import IPSetForwardedIPConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IPSetReferenceStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html
    Properties:
        - Name: IPSetForwardedIPConfig
        - Name: Arn
    
    """
    
    IPSetForwardedIPConfig_: Optional['IPSetForwardedIPConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html#cfn-wafv2-rulegroup-ipsetreferencestatement-ipsetforwardedipconfig""", alias="IPSetForwardedIPConfig")
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html#cfn-wafv2-rulegroup-ipsetreferencestatement-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.IPSetReferenceStatement:
        from troposphere.wafv2 import IPSetReferenceStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImmunityTimeProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-immunitytimeproperty.html
    Properties:
        - Name: ImmunityTime
    
    """
    
    ImmunityTime_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-immunitytimeproperty.html#cfn-wafv2-rulegroup-immunitytimeproperty-immunitytime""", alias="ImmunityTime")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ImmunityTimeProperty:
        from troposphere.wafv2 import ImmunityTimeProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JsonBody(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html
    Properties:
        - Name: MatchScope
        - Name: MatchPattern
        - Name: InvalidFallbackBehavior
        - Name: OversizeHandling
    
    """
    
    MatchScope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html#cfn-wafv2-rulegroup-jsonbody-matchscope""", alias="MatchScope")
    MatchPattern_: 'JsonMatchPattern' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html#cfn-wafv2-rulegroup-jsonbody-matchpattern""", alias="MatchPattern")
    InvalidFallbackBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html#cfn-wafv2-rulegroup-jsonbody-invalidfallbackbehavior""", alias="InvalidFallbackBehavior")
    OversizeHandling_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html#cfn-wafv2-rulegroup-jsonbody-oversizehandling""", alias="OversizeHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.JsonBody:
        from troposphere.wafv2 import JsonBody as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JsonMatchPattern(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonmatchpattern.html
    Properties:
        - Name: All
        - Name: IncludedPaths
    
    """
    
    All_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonmatchpattern.html#cfn-wafv2-rulegroup-jsonmatchpattern-all""", alias="All")
    IncludedPaths_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonmatchpattern.html#cfn-wafv2-rulegroup-jsonmatchpattern-includedpaths""", alias="IncludedPaths")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.JsonMatchPattern:
        from troposphere.wafv2 import JsonMatchPattern as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Label(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-label.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-label.html#cfn-wafv2-rulegroup-label-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Label:
        from troposphere.wafv2 import Label as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LabelMatchStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelmatchstatement.html
    Properties:
        - Name: Scope
        - Name: Key
    
    """
    
    Scope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelmatchstatement.html#cfn-wafv2-rulegroup-labelmatchstatement-scope""", alias="Scope")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelmatchstatement.html#cfn-wafv2-rulegroup-labelmatchstatement-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.LabelMatchStatement:
        from troposphere.wafv2 import LabelMatchStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LabelSummary(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelsummary.html
    Properties:
        - Name: Name
    
    """
    
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelsummary.html#cfn-wafv2-rulegroup-labelsummary-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.LabelSummary:
        from troposphere.wafv2 import LabelSummary as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatement.html
    Properties:
        - Name: Statement
    
    """
    
    Statement_: 'Statement' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatement.html#cfn-wafv2-rulegroup-notstatement-statement""", alias="Statement")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.NotStatement:
        from troposphere.wafv2 import NotStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OrStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatement.html
    Properties:
        - Name: Statements
    
    """
    
    Statements_: List['Statement'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatement.html#cfn-wafv2-rulegroup-orstatement-statements""", alias="Statements")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.OrStatement:
        from troposphere.wafv2 import OrStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateBasedStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html
    Properties:
        - Name: AggregateKeyType
        - Name: CustomKeys
        - Name: ForwardedIPConfig
        - Name: Limit
        - Name: ScopeDownStatement
    
    """
    
    AggregateKeyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-aggregatekeytype""", alias="AggregateKeyType")
    CustomKeys_: Optional[List['RateBasedStatementCustomKey']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-customkeys""", alias="CustomKeys")
    ForwardedIPConfig_: Optional['ForwardedIPConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-forwardedipconfig""", alias="ForwardedIPConfig")
    Limit_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-limit""", alias="Limit")
    ScopeDownStatement_: Optional['Statement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-scopedownstatement""", alias="ScopeDownStatement")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateBasedStatement:
        from troposphere.wafv2 import RateBasedStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateBasedStatementCustomKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementcustomkey.html
    Properties:
        - Name: Cookie
        - Name: ForwardedIP
        - Name: QueryArgument
        - Name: Header
        - Name: HTTPMethod
        - Name: QueryString
        - Name: UriPath
        - Name: IP
        - Name: LabelNamespace
    
    """
    
    Cookie_: Optional['RateLimitCookie'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementcustomkey.html#cfn-wafv2-rulegroup-ratebasedstatementcustomkey-cookie""", alias="Cookie")
    ForwardedIP_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementcustomkey.html#cfn-wafv2-rulegroup-ratebasedstatementcustomkey-forwardedip""", alias="ForwardedIP")
    QueryArgument_: Optional['RateLimitQueryArgument'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementcustomkey.html#cfn-wafv2-rulegroup-ratebasedstatementcustomkey-queryargument""", alias="QueryArgument")
    Header_: Optional['RateLimitHeader'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementcustomkey.html#cfn-wafv2-rulegroup-ratebasedstatementcustomkey-header""", alias="Header")
    HTTPMethod_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementcustomkey.html#cfn-wafv2-rulegroup-ratebasedstatementcustomkey-httpmethod""", alias="HTTPMethod")
    QueryString_: Optional['RateLimitQueryString'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementcustomkey.html#cfn-wafv2-rulegroup-ratebasedstatementcustomkey-querystring""", alias="QueryString")
    UriPath_: Optional['RateLimitUriPath'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementcustomkey.html#cfn-wafv2-rulegroup-ratebasedstatementcustomkey-uripath""", alias="UriPath")
    IP_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementcustomkey.html#cfn-wafv2-rulegroup-ratebasedstatementcustomkey-ip""", alias="IP")
    LabelNamespace_: Optional['RateLimitLabelNamespace'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementcustomkey.html#cfn-wafv2-rulegroup-ratebasedstatementcustomkey-labelnamespace""", alias="LabelNamespace")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateBasedStatementCustomKey:
        from troposphere.wafv2 import RateBasedStatementCustomKey as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateLimitCookie(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimitcookie.html
    Properties:
        - Name: TextTransformations
        - Name: Name
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimitcookie.html#cfn-wafv2-rulegroup-ratelimitcookie-texttransformations""", alias="TextTransformations")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimitcookie.html#cfn-wafv2-rulegroup-ratelimitcookie-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateLimitCookie:
        from troposphere.wafv2 import RateLimitCookie as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateLimitHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimitheader.html
    Properties:
        - Name: TextTransformations
        - Name: Name
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimitheader.html#cfn-wafv2-rulegroup-ratelimitheader-texttransformations""", alias="TextTransformations")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimitheader.html#cfn-wafv2-rulegroup-ratelimitheader-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateLimitHeader:
        from troposphere.wafv2 import RateLimitHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateLimitLabelNamespace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimitlabelnamespace.html
    Properties:
        - Name: Namespace
    
    """
    
    Namespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimitlabelnamespace.html#cfn-wafv2-rulegroup-ratelimitlabelnamespace-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateLimitLabelNamespace:
        from troposphere.wafv2 import RateLimitLabelNamespace as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateLimitQueryArgument(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimitqueryargument.html
    Properties:
        - Name: TextTransformations
        - Name: Name
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimitqueryargument.html#cfn-wafv2-rulegroup-ratelimitqueryargument-texttransformations""", alias="TextTransformations")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimitqueryargument.html#cfn-wafv2-rulegroup-ratelimitqueryargument-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateLimitQueryArgument:
        from troposphere.wafv2 import RateLimitQueryArgument as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateLimitQueryString(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimitquerystring.html
    Properties:
        - Name: TextTransformations
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimitquerystring.html#cfn-wafv2-rulegroup-ratelimitquerystring-texttransformations""", alias="TextTransformations")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateLimitQueryString:
        from troposphere.wafv2 import RateLimitQueryString as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateLimitUriPath(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimituripath.html
    Properties:
        - Name: TextTransformations
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratelimituripath.html#cfn-wafv2-rulegroup-ratelimituripath-texttransformations""", alias="TextTransformations")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateLimitUriPath:
        from troposphere.wafv2 import RateLimitUriPath as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RegexMatchStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexmatchstatement.html
    Properties:
        - Name: TextTransformations
        - Name: RegexString
        - Name: FieldToMatch
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexmatchstatement.html#cfn-wafv2-rulegroup-regexmatchstatement-texttransformations""", alias="TextTransformations")
    RegexString_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexmatchstatement.html#cfn-wafv2-rulegroup-regexmatchstatement-regexstring""", alias="RegexString")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexmatchstatement.html#cfn-wafv2-rulegroup-regexmatchstatement-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RegexMatchStatement:
        from troposphere.wafv2 import RegexMatchStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RegexPatternSetReferenceStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html
    Properties:
        - Name: TextTransformations
        - Name: Arn
        - Name: FieldToMatch
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-texttransformations""", alias="TextTransformations")
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-arn""", alias="Arn")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RegexPatternSetReferenceStatement:
        from troposphere.wafv2 import RegexPatternSetReferenceStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html
    Properties:
        - Name: Action
        - Name: Priority
        - Name: Statement
        - Name: ChallengeConfig
        - Name: RuleLabels
        - Name: VisibilityConfig
        - Name: CaptchaConfig
        - Name: Name
    
    """
    
    Action_: Optional['RuleAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-action""", alias="Action")
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-priority""", alias="Priority")
    Statement_: 'Statement' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-statement""", alias="Statement")
    ChallengeConfig_: Optional['ChallengeConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-challengeconfig""", alias="ChallengeConfig")
    RuleLabels_: Optional[List['Label']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-rulelabels""", alias="RuleLabels")
    VisibilityConfig_: 'VisibilityConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-visibilityconfig""", alias="VisibilityConfig")
    CaptchaConfig_: Optional['CaptchaConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-captchaconfig""", alias="CaptchaConfig")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Rule:
        from troposphere.wafv2 import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html
    Properties:
        - Name: Captcha
        - Name: Block
        - Name: Count
        - Name: Allow
        - Name: Challenge
    
    """
    
    Captcha_: Optional['CaptchaAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-captcha""", alias="Captcha")
    Block_: Optional['BlockAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-block""", alias="Block")
    Count_: Optional['CountAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-count""", alias="Count")
    Allow_: Optional['AllowAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-allow""", alias="Allow")
    Challenge_: Optional['ChallengeAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-challenge""", alias="Challenge")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RuleAction:
        from troposphere.wafv2 import RuleAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SingleHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-singleheader.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-singleheader.html#cfn-wafv2-rulegroup-singleheader-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.SingleHeader:
        from troposphere.wafv2 import SingleHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SingleQueryArgument(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-singlequeryargument.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-singlequeryargument.html#cfn-wafv2-rulegroup-singlequeryargument-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.SingleQueryArgument:
        from troposphere.wafv2 import SingleQueryArgument as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SizeConstraintStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html
    Properties:
        - Name: ComparisonOperator
        - Name: TextTransformations
        - Name: Size
        - Name: FieldToMatch
    
    """
    
    ComparisonOperator_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-comparisonoperator""", alias="ComparisonOperator")
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-texttransformations""", alias="TextTransformations")
    Size_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-size""", alias="Size")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.SizeConstraintStatement:
        from troposphere.wafv2 import SizeConstraintStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SqliMatchStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html
    Properties:
        - Name: SensitivityLevel
        - Name: TextTransformations
        - Name: FieldToMatch
    
    """
    
    SensitivityLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html#cfn-wafv2-rulegroup-sqlimatchstatement-sensitivitylevel""", alias="SensitivityLevel")
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html#cfn-wafv2-rulegroup-sqlimatchstatement-texttransformations""", alias="TextTransformations")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html#cfn-wafv2-rulegroup-sqlimatchstatement-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.SqliMatchStatement:
        from troposphere.wafv2 import SqliMatchStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Statement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html
    Properties:
        - Name: SizeConstraintStatement
        - Name: AndStatement
        - Name: XssMatchStatement
        - Name: NotStatement
        - Name: ByteMatchStatement
        - Name: RateBasedStatement
        - Name: GeoMatchStatement
        - Name: LabelMatchStatement
        - Name: RegexMatchStatement
        - Name: SqliMatchStatement
        - Name: RegexPatternSetReferenceStatement
        - Name: OrStatement
        - Name: IPSetReferenceStatement
    
    """
    
    SizeConstraintStatement_: Optional['SizeConstraintStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-sizeconstraintstatement""", alias="SizeConstraintStatement")
    AndStatement_: Optional['AndStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-andstatement""", alias="AndStatement")
    XssMatchStatement_: Optional['XssMatchStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-xssmatchstatement""", alias="XssMatchStatement")
    NotStatement_: Optional['NotStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-notstatement""", alias="NotStatement")
    ByteMatchStatement_: Optional['ByteMatchStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-bytematchstatement""", alias="ByteMatchStatement")
    RateBasedStatement_: Optional['RateBasedStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-ratebasedstatement""", alias="RateBasedStatement")
    GeoMatchStatement_: Optional['GeoMatchStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-geomatchstatement""", alias="GeoMatchStatement")
    LabelMatchStatement_: Optional['LabelMatchStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-labelmatchstatement""", alias="LabelMatchStatement")
    RegexMatchStatement_: Optional['RegexMatchStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-regexmatchstatement""", alias="RegexMatchStatement")
    SqliMatchStatement_: Optional['SqliMatchStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-sqlimatchstatement""", alias="SqliMatchStatement")
    RegexPatternSetReferenceStatement_: Optional['RegexPatternSetReferenceStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-regexpatternsetreferencestatement""", alias="RegexPatternSetReferenceStatement")
    OrStatement_: Optional['OrStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-orstatement""", alias="OrStatement")
    IPSetReferenceStatement_: Optional['IPSetReferenceStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-ipsetreferencestatement""", alias="IPSetReferenceStatement")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Statement:
        from troposphere.wafv2 import Statement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TextTransformation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html
    Properties:
        - Name: Type
        - Name: Priority
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html#cfn-wafv2-rulegroup-texttransformation-type""", alias="Type")
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html#cfn-wafv2-rulegroup-texttransformation-priority""", alias="Priority")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.TextTransformation:
        from troposphere.wafv2 import TextTransformation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VisibilityConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html
    Properties:
        - Name: MetricName
        - Name: SampledRequestsEnabled
        - Name: CloudWatchMetricsEnabled
    
    """
    
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-metricname""", alias="MetricName")
    SampledRequestsEnabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-sampledrequestsenabled""", alias="SampledRequestsEnabled")
    CloudWatchMetricsEnabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-cloudwatchmetricsenabled""", alias="CloudWatchMetricsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.VisibilityConfig:
        from troposphere.wafv2 import VisibilityConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class XssMatchStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html
    Properties:
        - Name: TextTransformations
        - Name: FieldToMatch
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html#cfn-wafv2-rulegroup-xssmatchstatement-texttransformations""", alias="TextTransformations")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html#cfn-wafv2-rulegroup-xssmatchstatement-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.XssMatchStatement:
        from troposphere.wafv2 import XssMatchStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AWSManagedRulesACFPRuleSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesacfpruleset.html
    Properties:
        - Name: RegistrationPagePath
        - Name: ResponseInspection
        - Name: CreationPath
        - Name: EnableRegexInPath
        - Name: RequestInspection
    
    """
    
    RegistrationPagePath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesacfpruleset.html#cfn-wafv2-webacl-awsmanagedrulesacfpruleset-registrationpagepath""", alias="RegistrationPagePath")
    ResponseInspection_: Optional['ResponseInspection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesacfpruleset.html#cfn-wafv2-webacl-awsmanagedrulesacfpruleset-responseinspection""", alias="ResponseInspection")
    CreationPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesacfpruleset.html#cfn-wafv2-webacl-awsmanagedrulesacfpruleset-creationpath""", alias="CreationPath")
    EnableRegexInPath_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesacfpruleset.html#cfn-wafv2-webacl-awsmanagedrulesacfpruleset-enableregexinpath""", alias="EnableRegexInPath")
    RequestInspection_: 'RequestInspectionACFP' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesacfpruleset.html#cfn-wafv2-webacl-awsmanagedrulesacfpruleset-requestinspection""", alias="RequestInspection")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.AWSManagedRulesACFPRuleSet:
        from troposphere.wafv2 import AWSManagedRulesACFPRuleSet as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AWSManagedRulesATPRuleSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesatpruleset.html
    Properties:
        - Name: ResponseInspection
        - Name: EnableRegexInPath
        - Name: LoginPath
        - Name: RequestInspection
    
    """
    
    ResponseInspection_: Optional['ResponseInspection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesatpruleset.html#cfn-wafv2-webacl-awsmanagedrulesatpruleset-responseinspection""", alias="ResponseInspection")
    EnableRegexInPath_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesatpruleset.html#cfn-wafv2-webacl-awsmanagedrulesatpruleset-enableregexinpath""", alias="EnableRegexInPath")
    LoginPath_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesatpruleset.html#cfn-wafv2-webacl-awsmanagedrulesatpruleset-loginpath""", alias="LoginPath")
    RequestInspection_: Optional['RequestInspection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesatpruleset.html#cfn-wafv2-webacl-awsmanagedrulesatpruleset-requestinspection""", alias="RequestInspection")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.AWSManagedRulesATPRuleSet:
        from troposphere.wafv2 import AWSManagedRulesATPRuleSet as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AWSManagedRulesBotControlRuleSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesbotcontrolruleset.html
    Properties:
        - Name: InspectionLevel
        - Name: EnableMachineLearning
    
    """
    
    InspectionLevel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesbotcontrolruleset.html#cfn-wafv2-webacl-awsmanagedrulesbotcontrolruleset-inspectionlevel""", alias="InspectionLevel")
    EnableMachineLearning_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-awsmanagedrulesbotcontrolruleset.html#cfn-wafv2-webacl-awsmanagedrulesbotcontrolruleset-enablemachinelearning""", alias="EnableMachineLearning")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.AWSManagedRulesBotControlRuleSet:
        from troposphere.wafv2 import AWSManagedRulesBotControlRuleSet as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AllowAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-allowaction.html
    Properties:
        - Name: CustomRequestHandling
    
    """
    
    CustomRequestHandling_: Optional['CustomRequestHandling'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-allowaction.html#cfn-wafv2-webacl-allowaction-customrequesthandling""", alias="CustomRequestHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.AllowAction:
        from troposphere.wafv2 import AllowAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AndStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatement.html
    Properties:
        - Name: Statements
    
    """
    
    Statements_: List['Statement'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatement.html#cfn-wafv2-webacl-andstatement-statements""", alias="Statements")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.AndStatement:
        from troposphere.wafv2 import AndStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssociationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-associationconfig.html
    Properties:
        - Name: RequestBody
    
    """
    
    RequestBody_: Optional[Dict[str, 'RequestBodyAssociatedResourceTypeConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-associationconfig.html#cfn-wafv2-webacl-associationconfig-requestbody""", alias="RequestBody")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.AssociationConfig:
        from troposphere.wafv2 import AssociationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BlockAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-blockaction.html
    Properties:
        - Name: CustomResponse
    
    """
    
    CustomResponse_: Optional['CustomResponse'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-blockaction.html#cfn-wafv2-webacl-blockaction-customresponse""", alias="CustomResponse")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.BlockAction:
        from troposphere.wafv2 import BlockAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Body(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-body.html
    Properties:
        - Name: OversizeHandling
    
    """
    
    OversizeHandling_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-body.html#cfn-wafv2-webacl-body-oversizehandling""", alias="OversizeHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Body:
        from troposphere.wafv2 import Body as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ByteMatchStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html
    Properties:
        - Name: SearchStringBase64
        - Name: TextTransformations
        - Name: PositionalConstraint
        - Name: SearchString
        - Name: FieldToMatch
    
    """
    
    SearchStringBase64_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-searchstringbase64""", alias="SearchStringBase64")
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-texttransformations""", alias="TextTransformations")
    PositionalConstraint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-positionalconstraint""", alias="PositionalConstraint")
    SearchString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-searchstring""", alias="SearchString")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ByteMatchStatement:
        from troposphere.wafv2 import ByteMatchStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CaptchaAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaaction.html
    Properties:
        - Name: CustomRequestHandling
    
    """
    
    CustomRequestHandling_: Optional['CustomRequestHandling'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaaction.html#cfn-wafv2-webacl-captchaaction-customrequesthandling""", alias="CustomRequestHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CaptchaAction:
        from troposphere.wafv2 import CaptchaAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CaptchaConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaconfig.html
    Properties:
        - Name: ImmunityTimeProperty
    
    """
    
    ImmunityTimeProperty_: Optional['ImmunityTimeProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaconfig.html#cfn-wafv2-webacl-captchaconfig-immunitytimeproperty""", alias="ImmunityTimeProperty")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CaptchaConfig:
        from troposphere.wafv2 import CaptchaConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ChallengeAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-challengeaction.html
    Properties:
        - Name: CustomRequestHandling
    
    """
    
    CustomRequestHandling_: Optional['CustomRequestHandling'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-challengeaction.html#cfn-wafv2-webacl-challengeaction-customrequesthandling""", alias="CustomRequestHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ChallengeAction:
        from troposphere.wafv2 import ChallengeAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ChallengeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-challengeconfig.html
    Properties:
        - Name: ImmunityTimeProperty
    
    """
    
    ImmunityTimeProperty_: Optional['ImmunityTimeProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-challengeconfig.html#cfn-wafv2-webacl-challengeconfig-immunitytimeproperty""", alias="ImmunityTimeProperty")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ChallengeConfig:
        from troposphere.wafv2 import ChallengeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CookieMatchPattern(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-cookiematchpattern.html
    Properties:
        - Name: All
        - Name: IncludedCookies
        - Name: ExcludedCookies
    
    """
    
    All_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-cookiematchpattern.html#cfn-wafv2-webacl-cookiematchpattern-all""", alias="All")
    IncludedCookies_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-cookiematchpattern.html#cfn-wafv2-webacl-cookiematchpattern-includedcookies""", alias="IncludedCookies")
    ExcludedCookies_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-cookiematchpattern.html#cfn-wafv2-webacl-cookiematchpattern-excludedcookies""", alias="ExcludedCookies")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CookieMatchPattern:
        from troposphere.wafv2 import CookieMatchPattern as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Cookies(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-cookies.html
    Properties:
        - Name: MatchScope
        - Name: MatchPattern
        - Name: OversizeHandling
    
    """
    
    MatchScope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-cookies.html#cfn-wafv2-webacl-cookies-matchscope""", alias="MatchScope")
    MatchPattern_: 'CookieMatchPattern' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-cookies.html#cfn-wafv2-webacl-cookies-matchpattern""", alias="MatchPattern")
    OversizeHandling_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-cookies.html#cfn-wafv2-webacl-cookies-oversizehandling""", alias="OversizeHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Cookies:
        from troposphere.wafv2 import Cookies as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CountAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countaction.html
    Properties:
        - Name: CustomRequestHandling
    
    """
    
    CustomRequestHandling_: Optional['CustomRequestHandling'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countaction.html#cfn-wafv2-webacl-countaction-customrequesthandling""", alias="CustomRequestHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CountAction:
        from troposphere.wafv2 import CountAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomHTTPHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html
    Properties:
        - Name: Value
        - Name: Name
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html#cfn-wafv2-webacl-customhttpheader-value""", alias="Value")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html#cfn-wafv2-webacl-customhttpheader-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CustomHTTPHeader:
        from troposphere.wafv2 import CustomHTTPHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomRequestHandling(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customrequesthandling.html
    Properties:
        - Name: InsertHeaders
    
    """
    
    InsertHeaders_: List['CustomHTTPHeader'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customrequesthandling.html#cfn-wafv2-webacl-customrequesthandling-insertheaders""", alias="InsertHeaders")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CustomRequestHandling:
        from troposphere.wafv2 import CustomRequestHandling as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomResponse(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html
    Properties:
        - Name: ResponseCode
        - Name: CustomResponseBodyKey
        - Name: ResponseHeaders
    
    """
    
    ResponseCode_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html#cfn-wafv2-webacl-customresponse-responsecode""", alias="ResponseCode")
    CustomResponseBodyKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html#cfn-wafv2-webacl-customresponse-customresponsebodykey""", alias="CustomResponseBodyKey")
    ResponseHeaders_: Optional[List['CustomHTTPHeader']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html#cfn-wafv2-webacl-customresponse-responseheaders""", alias="ResponseHeaders")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CustomResponse:
        from troposphere.wafv2 import CustomResponse as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomResponseBody(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebody.html
    Properties:
        - Name: ContentType
        - Name: Content
    
    """
    
    ContentType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebody.html#cfn-wafv2-webacl-customresponsebody-contenttype""", alias="ContentType")
    Content_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebody.html#cfn-wafv2-webacl-customresponsebody-content""", alias="Content")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.CustomResponseBody:
        from troposphere.wafv2 import CustomResponseBody as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefaultAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html
    Properties:
        - Name: Block
        - Name: Allow
    
    """
    
    Block_: Optional['BlockAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html#cfn-wafv2-webacl-defaultaction-block""", alias="Block")
    Allow_: Optional['AllowAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html#cfn-wafv2-webacl-defaultaction-allow""", alias="Allow")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.DefaultAction:
        from troposphere.wafv2 import DefaultAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExcludedRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrule.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrule.html#cfn-wafv2-webacl-excludedrule-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ExcludedRule:
        from troposphere.wafv2 import ExcludedRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldIdentifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldidentifier.html
    Properties:
        - Name: Identifier
    
    """
    
    Identifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldidentifier.html#cfn-wafv2-webacl-fieldidentifier-identifier""", alias="Identifier")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.FieldIdentifier:
        from troposphere.wafv2 import FieldIdentifier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WebACLFieldToMatch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html
    Properties:
        - Name: JsonBody
        - Name: AllQueryArguments
        - Name: SingleQueryArgument
        - Name: UriPath
        - Name: QueryString
        - Name: Headers
        - Name: Cookies
        - Name: Method
        - Name: Body
        - Name: SingleHeader
    
    """
    
    JsonBody_: Optional['JsonBody'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-jsonbody""", alias="JsonBody")
    AllQueryArguments_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-allqueryarguments""", alias="AllQueryArguments")
    SingleQueryArgument_: Optional['SingleQueryArgument'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-singlequeryargument""", alias="SingleQueryArgument")
    UriPath_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-uripath""", alias="UriPath")
    QueryString_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-querystring""", alias="QueryString")
    Headers_: Optional['Headers'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-headers""", alias="Headers")
    Cookies_: Optional['Cookies'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-cookies""", alias="Cookies")
    Method_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-method""", alias="Method")
    Body_: Optional['Body'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-body""", alias="Body")
    SingleHeader_: Optional['SingleHeader'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-singleheader""", alias="SingleHeader")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.WebACLFieldToMatch:
        from troposphere.wafv2 import WebACLFieldToMatch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ForwardedIPConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html
    Properties:
        - Name: FallbackBehavior
        - Name: HeaderName
    
    """
    
    FallbackBehavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html#cfn-wafv2-webacl-forwardedipconfiguration-fallbackbehavior""", alias="FallbackBehavior")
    HeaderName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html#cfn-wafv2-webacl-forwardedipconfiguration-headername""", alias="HeaderName")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ForwardedIPConfiguration:
        from troposphere.wafv2 import ForwardedIPConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GeoMatchStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html
    Properties:
        - Name: ForwardedIPConfig
        - Name: CountryCodes
    
    """
    
    ForwardedIPConfig_: Optional['ForwardedIPConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html#cfn-wafv2-webacl-geomatchstatement-forwardedipconfig""", alias="ForwardedIPConfig")
    CountryCodes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html#cfn-wafv2-webacl-geomatchstatement-countrycodes""", alias="CountryCodes")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.GeoMatchStatement:
        from troposphere.wafv2 import GeoMatchStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HeaderMatchPattern(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-headermatchpattern.html
    Properties:
        - Name: All
        - Name: IncludedHeaders
        - Name: ExcludedHeaders
    
    """
    
    All_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-headermatchpattern.html#cfn-wafv2-webacl-headermatchpattern-all""", alias="All")
    IncludedHeaders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-headermatchpattern.html#cfn-wafv2-webacl-headermatchpattern-includedheaders""", alias="IncludedHeaders")
    ExcludedHeaders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-headermatchpattern.html#cfn-wafv2-webacl-headermatchpattern-excludedheaders""", alias="ExcludedHeaders")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.HeaderMatchPattern:
        from troposphere.wafv2 import HeaderMatchPattern as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Headers(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-headers.html
    Properties:
        - Name: MatchScope
        - Name: MatchPattern
        - Name: OversizeHandling
    
    """
    
    MatchScope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-headers.html#cfn-wafv2-webacl-headers-matchscope""", alias="MatchScope")
    MatchPattern_: 'HeaderMatchPattern' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-headers.html#cfn-wafv2-webacl-headers-matchpattern""", alias="MatchPattern")
    OversizeHandling_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-headers.html#cfn-wafv2-webacl-headers-oversizehandling""", alias="OversizeHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Headers:
        from troposphere.wafv2 import Headers as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IPSetForwardedIPConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html
    Properties:
        - Name: FallbackBehavior
        - Name: HeaderName
        - Name: Position
    
    """
    
    FallbackBehavior_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-fallbackbehavior""", alias="FallbackBehavior")
    HeaderName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-headername""", alias="HeaderName")
    Position_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-position""", alias="Position")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.IPSetForwardedIPConfiguration:
        from troposphere.wafv2 import IPSetForwardedIPConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IPSetReferenceStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html
    Properties:
        - Name: IPSetForwardedIPConfig
        - Name: Arn
    
    """
    
    IPSetForwardedIPConfig_: Optional['IPSetForwardedIPConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html#cfn-wafv2-webacl-ipsetreferencestatement-ipsetforwardedipconfig""", alias="IPSetForwardedIPConfig")
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html#cfn-wafv2-webacl-ipsetreferencestatement-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.IPSetReferenceStatement:
        from troposphere.wafv2 import IPSetReferenceStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImmunityTimeProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-immunitytimeproperty.html
    Properties:
        - Name: ImmunityTime
    
    """
    
    ImmunityTime_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-immunitytimeproperty.html#cfn-wafv2-webacl-immunitytimeproperty-immunitytime""", alias="ImmunityTime")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ImmunityTimeProperty:
        from troposphere.wafv2 import ImmunityTimeProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JsonBody(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html
    Properties:
        - Name: MatchScope
        - Name: MatchPattern
        - Name: InvalidFallbackBehavior
        - Name: OversizeHandling
    
    """
    
    MatchScope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html#cfn-wafv2-webacl-jsonbody-matchscope""", alias="MatchScope")
    MatchPattern_: 'JsonMatchPattern' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html#cfn-wafv2-webacl-jsonbody-matchpattern""", alias="MatchPattern")
    InvalidFallbackBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html#cfn-wafv2-webacl-jsonbody-invalidfallbackbehavior""", alias="InvalidFallbackBehavior")
    OversizeHandling_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html#cfn-wafv2-webacl-jsonbody-oversizehandling""", alias="OversizeHandling")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.JsonBody:
        from troposphere.wafv2 import JsonBody as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JsonMatchPattern(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonmatchpattern.html
    Properties:
        - Name: All
        - Name: IncludedPaths
    
    """
    
    All_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonmatchpattern.html#cfn-wafv2-webacl-jsonmatchpattern-all""", alias="All")
    IncludedPaths_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonmatchpattern.html#cfn-wafv2-webacl-jsonmatchpattern-includedpaths""", alias="IncludedPaths")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.JsonMatchPattern:
        from troposphere.wafv2 import JsonMatchPattern as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Label(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-label.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-label.html#cfn-wafv2-webacl-label-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Label:
        from troposphere.wafv2 import Label as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LabelMatchStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-labelmatchstatement.html
    Properties:
        - Name: Scope
        - Name: Key
    
    """
    
    Scope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-labelmatchstatement.html#cfn-wafv2-webacl-labelmatchstatement-scope""", alias="Scope")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-labelmatchstatement.html#cfn-wafv2-webacl-labelmatchstatement-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.LabelMatchStatement:
        from troposphere.wafv2 import LabelMatchStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ManagedRuleGroupConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html
    Properties:
        - Name: UsernameField
        - Name: LoginPath
        - Name: AWSManagedRulesATPRuleSet
        - Name: AWSManagedRulesBotControlRuleSet
        - Name: PasswordField
        - Name: AWSManagedRulesACFPRuleSet
        - Name: PayloadType
    
    """
    
    UsernameField_: Optional['FieldIdentifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-usernamefield""", alias="UsernameField")
    LoginPath_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-loginpath""", alias="LoginPath")
    AWSManagedRulesATPRuleSet_: Optional['AWSManagedRulesATPRuleSet'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-awsmanagedrulesatpruleset""", alias="AWSManagedRulesATPRuleSet")
    AWSManagedRulesBotControlRuleSet_: Optional['AWSManagedRulesBotControlRuleSet'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-awsmanagedrulesbotcontrolruleset""", alias="AWSManagedRulesBotControlRuleSet")
    PasswordField_: Optional['FieldIdentifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-passwordfield""", alias="PasswordField")
    AWSManagedRulesACFPRuleSet_: Optional['AWSManagedRulesACFPRuleSet'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-awsmanagedrulesacfpruleset""", alias="AWSManagedRulesACFPRuleSet")
    PayloadType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-payloadtype""", alias="PayloadType")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ManagedRuleGroupConfig:
        from troposphere.wafv2 import ManagedRuleGroupConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ManagedRuleGroupStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html
    Properties:
        - Name: VendorName
        - Name: Version
        - Name: RuleActionOverrides
        - Name: ManagedRuleGroupConfigs
        - Name: ExcludedRules
        - Name: Name
        - Name: ScopeDownStatement
    
    """
    
    VendorName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-vendorname""", alias="VendorName")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-version""", alias="Version")
    RuleActionOverrides_: Optional[List['RuleActionOverride']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-ruleactionoverrides""", alias="RuleActionOverrides")
    ManagedRuleGroupConfigs_: Optional[List['ManagedRuleGroupConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-managedrulegroupconfigs""", alias="ManagedRuleGroupConfigs")
    ExcludedRules_: Optional[List['ExcludedRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-excludedrules""", alias="ExcludedRules")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-name""", alias="Name")
    ScopeDownStatement_: Optional['Statement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-scopedownstatement""", alias="ScopeDownStatement")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ManagedRuleGroupStatement:
        from troposphere.wafv2 import ManagedRuleGroupStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html
    Properties:
        - Name: Statement
    
    """
    
    Statement_: 'Statement' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html#cfn-wafv2-webacl-notstatement-statement""", alias="Statement")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.NotStatement:
        from troposphere.wafv2 import NotStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OrStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatement.html
    Properties:
        - Name: Statements
    
    """
    
    Statements_: List['Statement'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatement.html#cfn-wafv2-webacl-orstatement-statements""", alias="Statements")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.OrStatement:
        from troposphere.wafv2 import OrStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OverrideAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html
    Properties:
        - Name: Count
        - Name: None
    
    """
    
    Count_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html#cfn-wafv2-webacl-overrideaction-count""", alias="Count")
    None_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html#cfn-wafv2-webacl-overrideaction-none""", alias="None")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.OverrideAction:
        from troposphere.wafv2 import OverrideAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateBasedStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html
    Properties:
        - Name: AggregateKeyType
        - Name: CustomKeys
        - Name: ForwardedIPConfig
        - Name: Limit
        - Name: ScopeDownStatement
    
    """
    
    AggregateKeyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-aggregatekeytype""", alias="AggregateKeyType")
    CustomKeys_: Optional[List['RateBasedStatementCustomKey']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-customkeys""", alias="CustomKeys")
    ForwardedIPConfig_: Optional['ForwardedIPConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-forwardedipconfig""", alias="ForwardedIPConfig")
    Limit_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-limit""", alias="Limit")
    ScopeDownStatement_: Optional['Statement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-scopedownstatement""", alias="ScopeDownStatement")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateBasedStatement:
        from troposphere.wafv2 import RateBasedStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateBasedStatementCustomKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementcustomkey.html
    Properties:
        - Name: Cookie
        - Name: ForwardedIP
        - Name: QueryArgument
        - Name: Header
        - Name: HTTPMethod
        - Name: QueryString
        - Name: UriPath
        - Name: IP
        - Name: LabelNamespace
    
    """
    
    Cookie_: Optional['RateLimitCookie'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementcustomkey.html#cfn-wafv2-webacl-ratebasedstatementcustomkey-cookie""", alias="Cookie")
    ForwardedIP_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementcustomkey.html#cfn-wafv2-webacl-ratebasedstatementcustomkey-forwardedip""", alias="ForwardedIP")
    QueryArgument_: Optional['RateLimitQueryArgument'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementcustomkey.html#cfn-wafv2-webacl-ratebasedstatementcustomkey-queryargument""", alias="QueryArgument")
    Header_: Optional['RateLimitHeader'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementcustomkey.html#cfn-wafv2-webacl-ratebasedstatementcustomkey-header""", alias="Header")
    HTTPMethod_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementcustomkey.html#cfn-wafv2-webacl-ratebasedstatementcustomkey-httpmethod""", alias="HTTPMethod")
    QueryString_: Optional['RateLimitQueryString'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementcustomkey.html#cfn-wafv2-webacl-ratebasedstatementcustomkey-querystring""", alias="QueryString")
    UriPath_: Optional['RateLimitUriPath'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementcustomkey.html#cfn-wafv2-webacl-ratebasedstatementcustomkey-uripath""", alias="UriPath")
    IP_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementcustomkey.html#cfn-wafv2-webacl-ratebasedstatementcustomkey-ip""", alias="IP")
    LabelNamespace_: Optional['RateLimitLabelNamespace'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementcustomkey.html#cfn-wafv2-webacl-ratebasedstatementcustomkey-labelnamespace""", alias="LabelNamespace")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateBasedStatementCustomKey:
        from troposphere.wafv2 import RateBasedStatementCustomKey as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateLimitCookie(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimitcookie.html
    Properties:
        - Name: TextTransformations
        - Name: Name
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimitcookie.html#cfn-wafv2-webacl-ratelimitcookie-texttransformations""", alias="TextTransformations")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimitcookie.html#cfn-wafv2-webacl-ratelimitcookie-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateLimitCookie:
        from troposphere.wafv2 import RateLimitCookie as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateLimitHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimitheader.html
    Properties:
        - Name: TextTransformations
        - Name: Name
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimitheader.html#cfn-wafv2-webacl-ratelimitheader-texttransformations""", alias="TextTransformations")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimitheader.html#cfn-wafv2-webacl-ratelimitheader-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateLimitHeader:
        from troposphere.wafv2 import RateLimitHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateLimitLabelNamespace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimitlabelnamespace.html
    Properties:
        - Name: Namespace
    
    """
    
    Namespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimitlabelnamespace.html#cfn-wafv2-webacl-ratelimitlabelnamespace-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateLimitLabelNamespace:
        from troposphere.wafv2 import RateLimitLabelNamespace as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateLimitQueryArgument(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimitqueryargument.html
    Properties:
        - Name: TextTransformations
        - Name: Name
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimitqueryargument.html#cfn-wafv2-webacl-ratelimitqueryargument-texttransformations""", alias="TextTransformations")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimitqueryargument.html#cfn-wafv2-webacl-ratelimitqueryargument-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateLimitQueryArgument:
        from troposphere.wafv2 import RateLimitQueryArgument as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateLimitQueryString(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimitquerystring.html
    Properties:
        - Name: TextTransformations
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimitquerystring.html#cfn-wafv2-webacl-ratelimitquerystring-texttransformations""", alias="TextTransformations")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateLimitQueryString:
        from troposphere.wafv2 import RateLimitQueryString as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RateLimitUriPath(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimituripath.html
    Properties:
        - Name: TextTransformations
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratelimituripath.html#cfn-wafv2-webacl-ratelimituripath-texttransformations""", alias="TextTransformations")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RateLimitUriPath:
        from troposphere.wafv2 import RateLimitUriPath as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RegexMatchStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexmatchstatement.html
    Properties:
        - Name: TextTransformations
        - Name: RegexString
        - Name: FieldToMatch
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexmatchstatement.html#cfn-wafv2-webacl-regexmatchstatement-texttransformations""", alias="TextTransformations")
    RegexString_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexmatchstatement.html#cfn-wafv2-webacl-regexmatchstatement-regexstring""", alias="RegexString")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexmatchstatement.html#cfn-wafv2-webacl-regexmatchstatement-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RegexMatchStatement:
        from troposphere.wafv2 import RegexMatchStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RegexPatternSetReferenceStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html
    Properties:
        - Name: TextTransformations
        - Name: Arn
        - Name: FieldToMatch
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-texttransformations""", alias="TextTransformations")
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-arn""", alias="Arn")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RegexPatternSetReferenceStatement:
        from troposphere.wafv2 import RegexPatternSetReferenceStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RequestBodyAssociatedResourceTypeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig.html
    Properties:
        - Name: DefaultSizeInspectionLimit
    
    """
    
    DefaultSizeInspectionLimit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-requestbodyassociatedresourcetypeconfig.html#cfn-wafv2-webacl-requestbodyassociatedresourcetypeconfig-defaultsizeinspectionlimit""", alias="DefaultSizeInspectionLimit")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RequestBodyAssociatedResourceTypeConfig:
        from troposphere.wafv2 import RequestBodyAssociatedResourceTypeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RequestInspection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-requestinspection.html
    Properties:
        - Name: UsernameField
        - Name: PasswordField
        - Name: PayloadType
    
    """
    
    UsernameField_: 'FieldIdentifier' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-requestinspection.html#cfn-wafv2-webacl-requestinspection-usernamefield""", alias="UsernameField")
    PasswordField_: 'FieldIdentifier' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-requestinspection.html#cfn-wafv2-webacl-requestinspection-passwordfield""", alias="PasswordField")
    PayloadType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-requestinspection.html#cfn-wafv2-webacl-requestinspection-payloadtype""", alias="PayloadType")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RequestInspection:
        from troposphere.wafv2 import RequestInspection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RequestInspectionACFP(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-requestinspectionacfp.html
    Properties:
        - Name: UsernameField
        - Name: EmailField
        - Name: PasswordField
        - Name: AddressFields
        - Name: PayloadType
        - Name: PhoneNumberFields
    
    """
    
    UsernameField_: Optional['FieldIdentifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-requestinspectionacfp.html#cfn-wafv2-webacl-requestinspectionacfp-usernamefield""", alias="UsernameField")
    EmailField_: Optional['FieldIdentifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-requestinspectionacfp.html#cfn-wafv2-webacl-requestinspectionacfp-emailfield""", alias="EmailField")
    PasswordField_: Optional['FieldIdentifier'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-requestinspectionacfp.html#cfn-wafv2-webacl-requestinspectionacfp-passwordfield""", alias="PasswordField")
    AddressFields_: Optional[List['FieldIdentifier']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-requestinspectionacfp.html#cfn-wafv2-webacl-requestinspectionacfp-addressfields""", alias="AddressFields")
    PayloadType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-requestinspectionacfp.html#cfn-wafv2-webacl-requestinspectionacfp-payloadtype""", alias="PayloadType")
    PhoneNumberFields_: Optional[List['FieldIdentifier']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-requestinspectionacfp.html#cfn-wafv2-webacl-requestinspectionacfp-phonenumberfields""", alias="PhoneNumberFields")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RequestInspectionACFP:
        from troposphere.wafv2 import RequestInspectionACFP as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResponseInspection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspection.html
    Properties:
        - Name: Header
        - Name: BodyContains
        - Name: Json
        - Name: StatusCode
    
    """
    
    Header_: Optional['ResponseInspectionHeader'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspection.html#cfn-wafv2-webacl-responseinspection-header""", alias="Header")
    BodyContains_: Optional['ResponseInspectionBodyContains'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspection.html#cfn-wafv2-webacl-responseinspection-bodycontains""", alias="BodyContains")
    Json_: Optional['ResponseInspectionJson'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspection.html#cfn-wafv2-webacl-responseinspection-json""", alias="Json")
    StatusCode_: Optional['ResponseInspectionStatusCode'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspection.html#cfn-wafv2-webacl-responseinspection-statuscode""", alias="StatusCode")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ResponseInspection:
        from troposphere.wafv2 import ResponseInspection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResponseInspectionBodyContains(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionbodycontains.html
    Properties:
        - Name: SuccessStrings
        - Name: FailureStrings
    
    """
    
    SuccessStrings_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionbodycontains.html#cfn-wafv2-webacl-responseinspectionbodycontains-successstrings""", alias="SuccessStrings")
    FailureStrings_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionbodycontains.html#cfn-wafv2-webacl-responseinspectionbodycontains-failurestrings""", alias="FailureStrings")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ResponseInspectionBodyContains:
        from troposphere.wafv2 import ResponseInspectionBodyContains as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResponseInspectionHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionheader.html
    Properties:
        - Name: SuccessValues
        - Name: FailureValues
        - Name: Name
    
    """
    
    SuccessValues_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionheader.html#cfn-wafv2-webacl-responseinspectionheader-successvalues""", alias="SuccessValues")
    FailureValues_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionheader.html#cfn-wafv2-webacl-responseinspectionheader-failurevalues""", alias="FailureValues")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionheader.html#cfn-wafv2-webacl-responseinspectionheader-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ResponseInspectionHeader:
        from troposphere.wafv2 import ResponseInspectionHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResponseInspectionJson(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionjson.html
    Properties:
        - Name: Identifier
        - Name: SuccessValues
        - Name: FailureValues
    
    """
    
    Identifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionjson.html#cfn-wafv2-webacl-responseinspectionjson-identifier""", alias="Identifier")
    SuccessValues_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionjson.html#cfn-wafv2-webacl-responseinspectionjson-successvalues""", alias="SuccessValues")
    FailureValues_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionjson.html#cfn-wafv2-webacl-responseinspectionjson-failurevalues""", alias="FailureValues")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ResponseInspectionJson:
        from troposphere.wafv2 import ResponseInspectionJson as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResponseInspectionStatusCode(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionstatuscode.html
    Properties:
        - Name: SuccessCodes
        - Name: FailureCodes
    
    """
    
    SuccessCodes_: List[int] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionstatuscode.html#cfn-wafv2-webacl-responseinspectionstatuscode-successcodes""", alias="SuccessCodes")
    FailureCodes_: List[int] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-responseinspectionstatuscode.html#cfn-wafv2-webacl-responseinspectionstatuscode-failurecodes""", alias="FailureCodes")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.ResponseInspectionStatusCode:
        from troposphere.wafv2 import ResponseInspectionStatusCode as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html
    Properties:
        - Name: Action
        - Name: Priority
        - Name: Statement
        - Name: ChallengeConfig
        - Name: OverrideAction
        - Name: RuleLabels
        - Name: VisibilityConfig
        - Name: CaptchaConfig
        - Name: Name
    
    """
    
    Action_: Optional['RuleAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-action""", alias="Action")
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-priority""", alias="Priority")
    Statement_: 'Statement' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-statement""", alias="Statement")
    ChallengeConfig_: Optional['ChallengeConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-challengeconfig""", alias="ChallengeConfig")
    OverrideAction_: Optional['OverrideAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-overrideaction""", alias="OverrideAction")
    RuleLabels_: Optional[List['Label']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-rulelabels""", alias="RuleLabels")
    VisibilityConfig_: 'VisibilityConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-visibilityconfig""", alias="VisibilityConfig")
    CaptchaConfig_: Optional['CaptchaConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-captchaconfig""", alias="CaptchaConfig")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Rule:
        from troposphere.wafv2 import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html
    Properties:
        - Name: Captcha
        - Name: Block
        - Name: Count
        - Name: Allow
        - Name: Challenge
    
    """
    
    Captcha_: Optional['CaptchaAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-captcha""", alias="Captcha")
    Block_: Optional['BlockAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-block""", alias="Block")
    Count_: Optional['CountAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-count""", alias="Count")
    Allow_: Optional['AllowAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-allow""", alias="Allow")
    Challenge_: Optional['ChallengeAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-challenge""", alias="Challenge")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RuleAction:
        from troposphere.wafv2 import RuleAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleActionOverride(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleactionoverride.html
    Properties:
        - Name: ActionToUse
        - Name: Name
    
    """
    
    ActionToUse_: 'RuleAction' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleactionoverride.html#cfn-wafv2-webacl-ruleactionoverride-actiontouse""", alias="ActionToUse")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleactionoverride.html#cfn-wafv2-webacl-ruleactionoverride-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RuleActionOverride:
        from troposphere.wafv2 import RuleActionOverride as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleGroupReferenceStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html
    Properties:
        - Name: RuleActionOverrides
        - Name: Arn
        - Name: ExcludedRules
    
    """
    
    RuleActionOverrides_: Optional[List['RuleActionOverride']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html#cfn-wafv2-webacl-rulegroupreferencestatement-ruleactionoverrides""", alias="RuleActionOverrides")
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html#cfn-wafv2-webacl-rulegroupreferencestatement-arn""", alias="Arn")
    ExcludedRules_: Optional[List['ExcludedRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html#cfn-wafv2-webacl-rulegroupreferencestatement-excludedrules""", alias="ExcludedRules")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.RuleGroupReferenceStatement:
        from troposphere.wafv2 import RuleGroupReferenceStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SingleHeader(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-singleheader.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-singleheader.html#cfn-wafv2-webacl-singleheader-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.SingleHeader:
        from troposphere.wafv2 import SingleHeader as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SingleQueryArgument(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-singlequeryargument.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-singlequeryargument.html#cfn-wafv2-webacl-singlequeryargument-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.SingleQueryArgument:
        from troposphere.wafv2 import SingleQueryArgument as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SizeConstraintStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html
    Properties:
        - Name: ComparisonOperator
        - Name: TextTransformations
        - Name: Size
        - Name: FieldToMatch
    
    """
    
    ComparisonOperator_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-comparisonoperator""", alias="ComparisonOperator")
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-texttransformations""", alias="TextTransformations")
    Size_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-size""", alias="Size")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.SizeConstraintStatement:
        from troposphere.wafv2 import SizeConstraintStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SqliMatchStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html
    Properties:
        - Name: SensitivityLevel
        - Name: TextTransformations
        - Name: FieldToMatch
    
    """
    
    SensitivityLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html#cfn-wafv2-webacl-sqlimatchstatement-sensitivitylevel""", alias="SensitivityLevel")
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html#cfn-wafv2-webacl-sqlimatchstatement-texttransformations""", alias="TextTransformations")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html#cfn-wafv2-webacl-sqlimatchstatement-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.SqliMatchStatement:
        from troposphere.wafv2 import SqliMatchStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Statement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html
    Properties:
        - Name: SizeConstraintStatement
        - Name: AndStatement
        - Name: XssMatchStatement
        - Name: NotStatement
        - Name: ByteMatchStatement
        - Name: RateBasedStatement
        - Name: GeoMatchStatement
        - Name: RuleGroupReferenceStatement
        - Name: LabelMatchStatement
        - Name: RegexMatchStatement
        - Name: SqliMatchStatement
        - Name: RegexPatternSetReferenceStatement
        - Name: OrStatement
        - Name: ManagedRuleGroupStatement
        - Name: IPSetReferenceStatement
    
    """
    
    SizeConstraintStatement_: Optional['SizeConstraintStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-sizeconstraintstatement""", alias="SizeConstraintStatement")
    AndStatement_: Optional['AndStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-andstatement""", alias="AndStatement")
    XssMatchStatement_: Optional['XssMatchStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-xssmatchstatement""", alias="XssMatchStatement")
    NotStatement_: Optional['NotStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-notstatement""", alias="NotStatement")
    ByteMatchStatement_: Optional['ByteMatchStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-bytematchstatement""", alias="ByteMatchStatement")
    RateBasedStatement_: Optional['RateBasedStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-ratebasedstatement""", alias="RateBasedStatement")
    GeoMatchStatement_: Optional['GeoMatchStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-geomatchstatement""", alias="GeoMatchStatement")
    RuleGroupReferenceStatement_: Optional['RuleGroupReferenceStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-rulegroupreferencestatement""", alias="RuleGroupReferenceStatement")
    LabelMatchStatement_: Optional['LabelMatchStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-labelmatchstatement""", alias="LabelMatchStatement")
    RegexMatchStatement_: Optional['RegexMatchStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-regexmatchstatement""", alias="RegexMatchStatement")
    SqliMatchStatement_: Optional['SqliMatchStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-sqlimatchstatement""", alias="SqliMatchStatement")
    RegexPatternSetReferenceStatement_: Optional['RegexPatternSetReferenceStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-regexpatternsetreferencestatement""", alias="RegexPatternSetReferenceStatement")
    OrStatement_: Optional['OrStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-orstatement""", alias="OrStatement")
    ManagedRuleGroupStatement_: Optional['ManagedRuleGroupStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-managedrulegroupstatement""", alias="ManagedRuleGroupStatement")
    IPSetReferenceStatement_: Optional['IPSetReferenceStatement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-ipsetreferencestatement""", alias="IPSetReferenceStatement")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.Statement:
        from troposphere.wafv2 import Statement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TextTransformation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html
    Properties:
        - Name: Type
        - Name: Priority
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html#cfn-wafv2-webacl-texttransformation-type""", alias="Type")
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html#cfn-wafv2-webacl-texttransformation-priority""", alias="Priority")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.TextTransformation:
        from troposphere.wafv2 import TextTransformation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VisibilityConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html
    Properties:
        - Name: MetricName
        - Name: SampledRequestsEnabled
        - Name: CloudWatchMetricsEnabled
    
    """
    
    MetricName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-metricname""", alias="MetricName")
    SampledRequestsEnabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-sampledrequestsenabled""", alias="SampledRequestsEnabled")
    CloudWatchMetricsEnabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-cloudwatchmetricsenabled""", alias="CloudWatchMetricsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.VisibilityConfig:
        from troposphere.wafv2 import VisibilityConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class XssMatchStatement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html
    Properties:
        - Name: TextTransformations
        - Name: FieldToMatch
    
    """
    
    TextTransformations_: List['TextTransformation'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html#cfn-wafv2-webacl-xssmatchstatement-texttransformations""", alias="TextTransformations")
    FieldToMatch_: 'FieldToMatch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html#cfn-wafv2-webacl-xssmatchstatement-fieldtomatch""", alias="FieldToMatch")
    


    @property
    def tropo_type(self) -> troposphere.wafv2.XssMatchStatement:
        from troposphere.wafv2 import XssMatchStatement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class IPSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html
    Properties:
        - Name: Addresses
        - Name: Description
        - Name: Scope
        - Name: IPAddressVersion
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Addresses_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-addresses""", alias="Addresses")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-description""", alias="Description")
    Scope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-scope""", alias="Scope")
    IPAddressVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-ipaddressversion""", alias="IPAddressVersion")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafv2.IPSet:
        from troposphere.wafv2 import IPSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafv2 import IPSet as TropoT
        return resource_to_troposphere(self, TropoT)


class LoggingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html
    Properties:
        - Name: ResourceArn
        - Name: LogDestinationConfigs
        - Name: RedactedFields
        - Name: LoggingFilter
    Attributes:
        - Name: ManagedByFirewallManager
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-resourcearn""", alias="ResourceArn")
    LogDestinationConfigs_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-logdestinationconfigs""", alias="LogDestinationConfigs")
    RedactedFields_: Optional[List['FieldToMatch']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-redactedfields""", alias="RedactedFields")
    LoggingFilter_: Optional['LoggingFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-loggingfilter""", alias="LoggingFilter")
    

    @property
    def tropo_type(self) -> troposphere.wafv2.LoggingConfiguration:
        from troposphere.wafv2 import LoggingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafv2 import LoggingConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class RegexPatternSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html
    Properties:
        - Name: Description
        - Name: RegularExpressionList
        - Name: Scope
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-description""", alias="Description")
    RegularExpressionList_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-regularexpressionlist""", alias="RegularExpressionList")
    Scope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-scope""", alias="Scope")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafv2.RegexPatternSet:
        from troposphere.wafv2 import RegexPatternSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafv2 import RegexPatternSet as TropoT
        return resource_to_troposphere(self, TropoT)


class RuleGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html
    Properties:
        - Name: Description
        - Name: Scope
        - Name: Capacity
        - Name: AvailableLabels
        - Name: CustomResponseBodies
        - Name: ConsumedLabels
        - Name: Rules
        - Name: VisibilityConfig
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
        - Name: LabelNamespace
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-description""", alias="Description")
    Scope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-scope""", alias="Scope")
    Capacity_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-capacity""", alias="Capacity")
    AvailableLabels_: Optional[List['LabelSummary']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-availablelabels""", alias="AvailableLabels")
    CustomResponseBodies_: Optional[Dict[str, 'CustomResponseBody']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-customresponsebodies""", alias="CustomResponseBodies")
    ConsumedLabels_: Optional[List['LabelSummary']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-consumedlabels""", alias="ConsumedLabels")
    Rules_: Optional[List['Rule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-rules""", alias="Rules")
    VisibilityConfig_: 'VisibilityConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-visibilityconfig""", alias="VisibilityConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafv2.RuleGroup:
        from troposphere.wafv2 import RuleGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafv2 import RuleGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class WebACL(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html
    Properties:
        - Name: TokenDomains
        - Name: Description
        - Name: AssociationConfig
        - Name: DefaultAction
        - Name: Scope
        - Name: CustomResponseBodies
        - Name: ChallengeConfig
        - Name: Rules
        - Name: VisibilityConfig
        - Name: CaptchaConfig
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Capacity
        - Name: Id
        - Name: Arn
        - Name: LabelNamespace
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TokenDomains_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-tokendomains""", alias="TokenDomains")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-description""", alias="Description")
    AssociationConfig_: Optional['AssociationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-associationconfig""", alias="AssociationConfig")
    DefaultAction_: 'DefaultAction' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-defaultaction""", alias="DefaultAction")
    Scope_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-scope""", alias="Scope")
    CustomResponseBodies_: Optional[Dict[str, 'CustomResponseBody']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-customresponsebodies""", alias="CustomResponseBodies")
    ChallengeConfig_: Optional['ChallengeConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-challengeconfig""", alias="ChallengeConfig")
    Rules_: Optional[List['Rule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-rules""", alias="Rules")
    VisibilityConfig_: 'VisibilityConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-visibilityconfig""", alias="VisibilityConfig")
    CaptchaConfig_: Optional['CaptchaConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-captchaconfig""", alias="CaptchaConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.wafv2.WebACL:
        from troposphere.wafv2 import WebACL as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafv2 import WebACL as TropoT
        return resource_to_troposphere(self, TropoT)


class WebACLAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html
    Properties:
        - Name: ResourceArn
        - Name: WebACLArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-resourcearn""", alias="ResourceArn")
    WebACLArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-webaclarn""", alias="WebACLArn")
    

    @property
    def tropo_type(self) -> troposphere.wafv2.WebACLAssociation:
        from troposphere.wafv2 import WebACLAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.wafv2 import WebACLAssociation as TropoT
        return resource_to_troposphere(self, TropoT)

