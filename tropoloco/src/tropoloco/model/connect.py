from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class EvaluationFormBaseItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformbaseitem.html
    Properties:
        - Name: Section
    
    """
    
    Section_: 'EvaluationFormSection' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformbaseitem.html#cfn-connect-evaluationform-evaluationformbaseitem-section""", alias="Section")
    


    @property
    def tropo_type(self) -> troposphere.connect.EvaluationFormBaseItem:
        from troposphere.connect import EvaluationFormBaseItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluationFormItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformitem.html
    Properties:
        - Name: Question
        - Name: Section
    
    """
    
    Question_: Optional['EvaluationFormQuestion'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformitem.html#cfn-connect-evaluationform-evaluationformitem-question""", alias="Question")
    Section_: Optional['EvaluationFormSection'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformitem.html#cfn-connect-evaluationform-evaluationformitem-section""", alias="Section")
    


    @property
    def tropo_type(self) -> troposphere.connect.EvaluationFormItem:
        from troposphere.connect import EvaluationFormItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluationFormNumericQuestionAutomation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionautomation.html
    Properties:
        - Name: PropertyValue
    
    """
    
    PropertyValue_: 'NumericQuestionPropertyValueAutomation' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionautomation.html#cfn-connect-evaluationform-evaluationformnumericquestionautomation-propertyvalue""", alias="PropertyValue")
    


    @property
    def tropo_type(self) -> troposphere.connect.EvaluationFormNumericQuestionAutomation:
        from troposphere.connect import EvaluationFormNumericQuestionAutomation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluationFormNumericQuestionOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionoption.html
    Properties:
        - Name: Score
        - Name: MinValue
        - Name: MaxValue
        - Name: AutomaticFail
    
    """
    
    Score_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionoption.html#cfn-connect-evaluationform-evaluationformnumericquestionoption-score""", alias="Score")
    MinValue_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionoption.html#cfn-connect-evaluationform-evaluationformnumericquestionoption-minvalue""", alias="MinValue")
    MaxValue_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionoption.html#cfn-connect-evaluationform-evaluationformnumericquestionoption-maxvalue""", alias="MaxValue")
    AutomaticFail_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionoption.html#cfn-connect-evaluationform-evaluationformnumericquestionoption-automaticfail""", alias="AutomaticFail")
    


    @property
    def tropo_type(self) -> troposphere.connect.EvaluationFormNumericQuestionOption:
        from troposphere.connect import EvaluationFormNumericQuestionOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluationFormNumericQuestionProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionproperties.html
    Properties:
        - Name: Options
        - Name: Automation
        - Name: MinValue
        - Name: MaxValue
    
    """
    
    Options_: Optional[List['EvaluationFormNumericQuestionOption']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionproperties.html#cfn-connect-evaluationform-evaluationformnumericquestionproperties-options""", alias="Options")
    Automation_: Optional['EvaluationFormNumericQuestionAutomation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionproperties.html#cfn-connect-evaluationform-evaluationformnumericquestionproperties-automation""", alias="Automation")
    MinValue_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionproperties.html#cfn-connect-evaluationform-evaluationformnumericquestionproperties-minvalue""", alias="MinValue")
    MaxValue_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionproperties.html#cfn-connect-evaluationform-evaluationformnumericquestionproperties-maxvalue""", alias="MaxValue")
    


    @property
    def tropo_type(self) -> troposphere.connect.EvaluationFormNumericQuestionProperties:
        from troposphere.connect import EvaluationFormNumericQuestionProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluationFormQuestion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html
    Properties:
        - Name: NotApplicableEnabled
        - Name: Title
        - Name: QuestionType
        - Name: Instructions
        - Name: RefId
        - Name: QuestionTypeProperties
        - Name: Weight
    
    """
    
    NotApplicableEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-notapplicableenabled""", alias="NotApplicableEnabled")
    Title_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-title""", alias="Title")
    QuestionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-questiontype""", alias="QuestionType")
    Instructions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-instructions""", alias="Instructions")
    RefId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-refid""", alias="RefId")
    QuestionTypeProperties_: Optional['EvaluationFormQuestionTypeProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-questiontypeproperties""", alias="QuestionTypeProperties")
    Weight_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-weight""", alias="Weight")
    


    @property
    def tropo_type(self) -> troposphere.connect.EvaluationFormQuestion:
        from troposphere.connect import EvaluationFormQuestion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluationFormQuestionTypeProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestiontypeproperties.html
    Properties:
        - Name: Numeric
        - Name: SingleSelect
    
    """
    
    Numeric_: Optional['EvaluationFormNumericQuestionProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestiontypeproperties.html#cfn-connect-evaluationform-evaluationformquestiontypeproperties-numeric""", alias="Numeric")
    SingleSelect_: Optional['EvaluationFormSingleSelectQuestionProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestiontypeproperties.html#cfn-connect-evaluationform-evaluationformquestiontypeproperties-singleselect""", alias="SingleSelect")
    


    @property
    def tropo_type(self) -> troposphere.connect.EvaluationFormQuestionTypeProperties:
        from troposphere.connect import EvaluationFormQuestionTypeProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluationFormSection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsection.html
    Properties:
        - Name: Title
        - Name: Instructions
        - Name: Items
        - Name: RefId
        - Name: Weight
    
    """
    
    Title_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsection.html#cfn-connect-evaluationform-evaluationformsection-title""", alias="Title")
    Instructions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsection.html#cfn-connect-evaluationform-evaluationformsection-instructions""", alias="Instructions")
    Items_: Optional[List['EvaluationFormItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsection.html#cfn-connect-evaluationform-evaluationformsection-items""", alias="Items")
    RefId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsection.html#cfn-connect-evaluationform-evaluationformsection-refid""", alias="RefId")
    Weight_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsection.html#cfn-connect-evaluationform-evaluationformsection-weight""", alias="Weight")
    


    @property
    def tropo_type(self) -> troposphere.connect.EvaluationFormSection:
        from troposphere.connect import EvaluationFormSection as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluationFormSingleSelectQuestionAutomation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionautomation.html
    Properties:
        - Name: Options
        - Name: DefaultOptionRefId
    
    """
    
    Options_: List['EvaluationFormSingleSelectQuestionAutomationOption'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionautomation.html#cfn-connect-evaluationform-evaluationformsingleselectquestionautomation-options""", alias="Options")
    DefaultOptionRefId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionautomation.html#cfn-connect-evaluationform-evaluationformsingleselectquestionautomation-defaultoptionrefid""", alias="DefaultOptionRefId")
    


    @property
    def tropo_type(self) -> troposphere.connect.EvaluationFormSingleSelectQuestionAutomation:
        from troposphere.connect import EvaluationFormSingleSelectQuestionAutomation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluationFormSingleSelectQuestionAutomationOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionautomationoption.html
    Properties:
        - Name: RuleCategory
    
    """
    
    RuleCategory_: 'SingleSelectQuestionRuleCategoryAutomation' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionautomationoption.html#cfn-connect-evaluationform-evaluationformsingleselectquestionautomationoption-rulecategory""", alias="RuleCategory")
    


    @property
    def tropo_type(self) -> troposphere.connect.EvaluationFormSingleSelectQuestionAutomationOption:
        from troposphere.connect import EvaluationFormSingleSelectQuestionAutomationOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluationFormSingleSelectQuestionOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption.html
    Properties:
        - Name: Score
        - Name: Text
        - Name: RefId
        - Name: AutomaticFail
    
    """
    
    Score_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption.html#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-score""", alias="Score")
    Text_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption.html#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-text""", alias="Text")
    RefId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption.html#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-refid""", alias="RefId")
    AutomaticFail_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption.html#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-automaticfail""", alias="AutomaticFail")
    


    @property
    def tropo_type(self) -> troposphere.connect.EvaluationFormSingleSelectQuestionOption:
        from troposphere.connect import EvaluationFormSingleSelectQuestionOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluationFormSingleSelectQuestionProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionproperties.html
    Properties:
        - Name: DisplayAs
        - Name: Options
        - Name: Automation
    
    """
    
    DisplayAs_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionproperties.html#cfn-connect-evaluationform-evaluationformsingleselectquestionproperties-displayas""", alias="DisplayAs")
    Options_: List['EvaluationFormSingleSelectQuestionOption'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionproperties.html#cfn-connect-evaluationform-evaluationformsingleselectquestionproperties-options""", alias="Options")
    Automation_: Optional['EvaluationFormSingleSelectQuestionAutomation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionproperties.html#cfn-connect-evaluationform-evaluationformsingleselectquestionproperties-automation""", alias="Automation")
    


    @property
    def tropo_type(self) -> troposphere.connect.EvaluationFormSingleSelectQuestionProperties:
        from troposphere.connect import EvaluationFormSingleSelectQuestionProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NumericQuestionPropertyValueAutomation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-numericquestionpropertyvalueautomation.html
    Properties:
        - Name: Label
    
    """
    
    Label_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-numericquestionpropertyvalueautomation.html#cfn-connect-evaluationform-numericquestionpropertyvalueautomation-label""", alias="Label")
    


    @property
    def tropo_type(self) -> troposphere.connect.NumericQuestionPropertyValueAutomation:
        from troposphere.connect import NumericQuestionPropertyValueAutomation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScoringStrategy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-scoringstrategy.html
    Properties:
        - Name: Status
        - Name: Mode
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-scoringstrategy.html#cfn-connect-evaluationform-scoringstrategy-status""", alias="Status")
    Mode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-scoringstrategy.html#cfn-connect-evaluationform-scoringstrategy-mode""", alias="Mode")
    


    @property
    def tropo_type(self) -> troposphere.connect.ScoringStrategy:
        from troposphere.connect import ScoringStrategy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SingleSelectQuestionRuleCategoryAutomation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-singleselectquestionrulecategoryautomation.html
    Properties:
        - Name: Condition
        - Name: Category
        - Name: OptionRefId
    
    """
    
    Condition_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-singleselectquestionrulecategoryautomation.html#cfn-connect-evaluationform-singleselectquestionrulecategoryautomation-condition""", alias="Condition")
    Category_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-singleselectquestionrulecategoryautomation.html#cfn-connect-evaluationform-singleselectquestionrulecategoryautomation-category""", alias="Category")
    OptionRefId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-singleselectquestionrulecategoryautomation.html#cfn-connect-evaluationform-singleselectquestionrulecategoryautomation-optionrefid""", alias="OptionRefId")
    


    @property
    def tropo_type(self) -> troposphere.connect.SingleSelectQuestionRuleCategoryAutomation:
        from troposphere.connect import SingleSelectQuestionRuleCategoryAutomation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HoursOfOperationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html
    Properties:
        - Name: EndTime
        - Name: StartTime
        - Name: Day
    
    """
    
    EndTime_: 'HoursOfOperationTimeSlice' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html#cfn-connect-hoursofoperation-hoursofoperationconfig-endtime""", alias="EndTime")
    StartTime_: 'HoursOfOperationTimeSlice' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html#cfn-connect-hoursofoperation-hoursofoperationconfig-starttime""", alias="StartTime")
    Day_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html#cfn-connect-hoursofoperation-hoursofoperationconfig-day""", alias="Day")
    


    @property
    def tropo_type(self) -> troposphere.connect.HoursOfOperationConfig:
        from troposphere.connect import HoursOfOperationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HoursOfOperationTimeSlice(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html
    Properties:
        - Name: Hours
        - Name: Minutes
    
    """
    
    Hours_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html#cfn-connect-hoursofoperation-hoursofoperationtimeslice-hours""", alias="Hours")
    Minutes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html#cfn-connect-hoursofoperation-hoursofoperationtimeslice-minutes""", alias="Minutes")
    


    @property
    def tropo_type(self) -> troposphere.connect.HoursOfOperationTimeSlice:
        from troposphere.connect import HoursOfOperationTimeSlice as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Attributes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html
    Properties:
        - Name: InboundCalls
        - Name: UseCustomTTSVoices
        - Name: OutboundCalls
        - Name: EarlyMedia
        - Name: ContactflowLogs
        - Name: ContactLens
        - Name: AutoResolveBestVoices
    
    """
    
    InboundCalls_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-inboundcalls""", alias="InboundCalls")
    UseCustomTTSVoices_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-usecustomttsvoices""", alias="UseCustomTTSVoices")
    OutboundCalls_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-outboundcalls""", alias="OutboundCalls")
    EarlyMedia_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-earlymedia""", alias="EarlyMedia")
    ContactflowLogs_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-contactflowlogs""", alias="ContactflowLogs")
    ContactLens_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-contactlens""", alias="ContactLens")
    AutoResolveBestVoices_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-autoresolvebestvoices""", alias="AutoResolveBestVoices")
    


    @property
    def tropo_type(self) -> troposphere.connect.Attributes:
        from troposphere.connect import Attributes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-encryptionconfig.html
    Properties:
        - Name: EncryptionType
        - Name: KeyId
    
    """
    
    EncryptionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-encryptionconfig.html#cfn-connect-instancestorageconfig-encryptionconfig-encryptiontype""", alias="EncryptionType")
    KeyId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-encryptionconfig.html#cfn-connect-instancestorageconfig-encryptionconfig-keyid""", alias="KeyId")
    


    @property
    def tropo_type(self) -> troposphere.connect.EncryptionConfig:
        from troposphere.connect import EncryptionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisFirehoseConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig.html
    Properties:
        - Name: FirehoseArn
    
    """
    
    FirehoseArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig.html#cfn-connect-instancestorageconfig-kinesisfirehoseconfig-firehosearn""", alias="FirehoseArn")
    


    @property
    def tropo_type(self) -> troposphere.connect.KinesisFirehoseConfig:
        from troposphere.connect import KinesisFirehoseConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisStreamConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisstreamconfig.html
    Properties:
        - Name: StreamArn
    
    """
    
    StreamArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisstreamconfig.html#cfn-connect-instancestorageconfig-kinesisstreamconfig-streamarn""", alias="StreamArn")
    


    @property
    def tropo_type(self) -> troposphere.connect.KinesisStreamConfig:
        from troposphere.connect import KinesisStreamConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KinesisVideoStreamConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisvideostreamconfig.html
    Properties:
        - Name: Prefix
        - Name: RetentionPeriodHours
        - Name: EncryptionConfig
    
    """
    
    Prefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisvideostreamconfig.html#cfn-connect-instancestorageconfig-kinesisvideostreamconfig-prefix""", alias="Prefix")
    RetentionPeriodHours_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisvideostreamconfig.html#cfn-connect-instancestorageconfig-kinesisvideostreamconfig-retentionperiodhours""", alias="RetentionPeriodHours")
    EncryptionConfig_: Optional['EncryptionConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisvideostreamconfig.html#cfn-connect-instancestorageconfig-kinesisvideostreamconfig-encryptionconfig""", alias="EncryptionConfig")
    


    @property
    def tropo_type(self) -> troposphere.connect.KinesisVideoStreamConfig:
        from troposphere.connect import KinesisVideoStreamConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Config(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-s3config.html
    Properties:
        - Name: BucketName
        - Name: BucketPrefix
        - Name: EncryptionConfig
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-s3config.html#cfn-connect-instancestorageconfig-s3config-bucketname""", alias="BucketName")
    BucketPrefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-s3config.html#cfn-connect-instancestorageconfig-s3config-bucketprefix""", alias="BucketPrefix")
    EncryptionConfig_: Optional['EncryptionConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-s3config.html#cfn-connect-instancestorageconfig-s3config-encryptionconfig""", alias="EncryptionConfig")
    


    @property
    def tropo_type(self) -> troposphere.connect.S3Config:
        from troposphere.connect import S3Config as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutboundCallerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-queue-outboundcallerconfig.html
    Properties:
        - Name: OutboundCallerIdNumberArn
        - Name: OutboundFlowArn
        - Name: OutboundCallerIdName
    
    """
    
    OutboundCallerIdNumberArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-queue-outboundcallerconfig.html#cfn-connect-queue-outboundcallerconfig-outboundcalleridnumberarn""", alias="OutboundCallerIdNumberArn")
    OutboundFlowArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-queue-outboundcallerconfig.html#cfn-connect-queue-outboundcallerconfig-outboundflowarn""", alias="OutboundFlowArn")
    OutboundCallerIdName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-queue-outboundcallerconfig.html#cfn-connect-queue-outboundcallerconfig-outboundcalleridname""", alias="OutboundCallerIdName")
    


    @property
    def tropo_type(self) -> troposphere.connect.OutboundCallerConfig:
        from troposphere.connect import OutboundCallerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PhoneNumberQuickConnectConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-phonenumberquickconnectconfig.html
    Properties:
        - Name: PhoneNumber
    
    """
    
    PhoneNumber_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-phonenumberquickconnectconfig.html#cfn-connect-quickconnect-phonenumberquickconnectconfig-phonenumber""", alias="PhoneNumber")
    


    @property
    def tropo_type(self) -> troposphere.connect.PhoneNumberQuickConnectConfig:
        from troposphere.connect import PhoneNumberQuickConnectConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QueueQuickConnectConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html
    Properties:
        - Name: ContactFlowArn
        - Name: QueueArn
    
    """
    
    ContactFlowArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html#cfn-connect-quickconnect-queuequickconnectconfig-contactflowarn""", alias="ContactFlowArn")
    QueueArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html#cfn-connect-quickconnect-queuequickconnectconfig-queuearn""", alias="QueueArn")
    


    @property
    def tropo_type(self) -> troposphere.connect.QueueQuickConnectConfig:
        from troposphere.connect import QueueQuickConnectConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QuickConnectConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html
    Properties:
        - Name: QueueConfig
        - Name: PhoneConfig
        - Name: QuickConnectType
        - Name: UserConfig
    
    """
    
    QueueConfig_: Optional['QueueQuickConnectConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-queueconfig""", alias="QueueConfig")
    PhoneConfig_: Optional['PhoneNumberQuickConnectConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-phoneconfig""", alias="PhoneConfig")
    QuickConnectType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-quickconnecttype""", alias="QuickConnectType")
    UserConfig_: Optional['UserQuickConnectConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-userconfig""", alias="UserConfig")
    


    @property
    def tropo_type(self) -> troposphere.connect.QuickConnectConfig:
        from troposphere.connect import QuickConnectConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserQuickConnectConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html
    Properties:
        - Name: UserArn
        - Name: ContactFlowArn
    
    """
    
    UserArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html#cfn-connect-quickconnect-userquickconnectconfig-userarn""", alias="UserArn")
    ContactFlowArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html#cfn-connect-quickconnect-userquickconnectconfig-contactflowarn""", alias="ContactFlowArn")
    


    @property
    def tropo_type(self) -> troposphere.connect.UserQuickConnectConfig:
        from troposphere.connect import UserQuickConnectConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CrossChannelBehavior(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-crosschannelbehavior.html
    Properties:
        - Name: BehaviorType
    
    """
    
    BehaviorType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-crosschannelbehavior.html#cfn-connect-routingprofile-crosschannelbehavior-behaviortype""", alias="BehaviorType")
    


    @property
    def tropo_type(self) -> troposphere.connect.CrossChannelBehavior:
        from troposphere.connect import CrossChannelBehavior as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MediaConcurrency(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-mediaconcurrency.html
    Properties:
        - Name: Concurrency
        - Name: Channel
        - Name: CrossChannelBehavior
    
    """
    
    Concurrency_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-mediaconcurrency.html#cfn-connect-routingprofile-mediaconcurrency-concurrency""", alias="Concurrency")
    Channel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-mediaconcurrency.html#cfn-connect-routingprofile-mediaconcurrency-channel""", alias="Channel")
    CrossChannelBehavior_: Optional['CrossChannelBehavior'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-mediaconcurrency.html#cfn-connect-routingprofile-mediaconcurrency-crosschannelbehavior""", alias="CrossChannelBehavior")
    


    @property
    def tropo_type(self) -> troposphere.connect.MediaConcurrency:
        from troposphere.connect import MediaConcurrency as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RoutingProfileQueueConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeueconfig.html
    Properties:
        - Name: Priority
        - Name: QueueReference
        - Name: Delay
    
    """
    
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeueconfig.html#cfn-connect-routingprofile-routingprofilequeueconfig-priority""", alias="Priority")
    QueueReference_: 'RoutingProfileQueueReference' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeueconfig.html#cfn-connect-routingprofile-routingprofilequeueconfig-queuereference""", alias="QueueReference")
    Delay_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeueconfig.html#cfn-connect-routingprofile-routingprofilequeueconfig-delay""", alias="Delay")
    


    @property
    def tropo_type(self) -> troposphere.connect.RoutingProfileQueueConfig:
        from troposphere.connect import RoutingProfileQueueConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RoutingProfileQueueReference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeuereference.html
    Properties:
        - Name: Channel
        - Name: QueueArn
    
    """
    
    Channel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeuereference.html#cfn-connect-routingprofile-routingprofilequeuereference-channel""", alias="Channel")
    QueueArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeuereference.html#cfn-connect-routingprofile-routingprofilequeuereference-queuearn""", alias="QueueArn")
    


    @property
    def tropo_type(self) -> troposphere.connect.RoutingProfileQueueReference:
        from troposphere.connect import RoutingProfileQueueReference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Actions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html
    Properties:
        - Name: EventBridgeActions
        - Name: AssignContactCategoryActions
        - Name: TaskActions
        - Name: SendNotificationActions
    
    """
    
    EventBridgeActions_: Optional[List['EventBridgeAction']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html#cfn-connect-rule-actions-eventbridgeactions""", alias="EventBridgeActions")
    AssignContactCategoryActions_: Optional[List[Dict]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html#cfn-connect-rule-actions-assigncontactcategoryactions""", alias="AssignContactCategoryActions")
    TaskActions_: Optional[List['TaskAction']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html#cfn-connect-rule-actions-taskactions""", alias="TaskActions")
    SendNotificationActions_: Optional[List['SendNotificationAction']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html#cfn-connect-rule-actions-sendnotificationactions""", alias="SendNotificationActions")
    


    @property
    def tropo_type(self) -> troposphere.connect.Actions:
        from troposphere.connect import Actions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EventBridgeAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-eventbridgeaction.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-eventbridgeaction.html#cfn-connect-rule-eventbridgeaction-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.connect.EventBridgeAction:
        from troposphere.connect import EventBridgeAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationRecipientType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-notificationrecipienttype.html
    Properties:
        - Name: UserTags
        - Name: UserArns
    
    """
    
    UserTags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-notificationrecipienttype.html#cfn-connect-rule-notificationrecipienttype-usertags""", alias="UserTags")
    UserArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-notificationrecipienttype.html#cfn-connect-rule-notificationrecipienttype-userarns""", alias="UserArns")
    


    @property
    def tropo_type(self) -> troposphere.connect.NotificationRecipientType:
        from troposphere.connect import NotificationRecipientType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Reference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-reference.html
    Properties:
        - Name: Type
        - Name: Value
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-reference.html#cfn-connect-rule-reference-type""", alias="Type")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-reference.html#cfn-connect-rule-reference-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.connect.Reference:
        from troposphere.connect import Reference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleTriggerEventSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-ruletriggereventsource.html
    Properties:
        - Name: IntegrationAssociationArn
        - Name: EventSourceName
    
    """
    
    IntegrationAssociationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-ruletriggereventsource.html#cfn-connect-rule-ruletriggereventsource-integrationassociationarn""", alias="IntegrationAssociationArn")
    EventSourceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-ruletriggereventsource.html#cfn-connect-rule-ruletriggereventsource-eventsourcename""", alias="EventSourceName")
    


    @property
    def tropo_type(self) -> troposphere.connect.RuleTriggerEventSource:
        from troposphere.connect import RuleTriggerEventSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SendNotificationAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-sendnotificationaction.html
    Properties:
        - Name: DeliveryMethod
        - Name: ContentType
        - Name: Content
        - Name: Recipient
        - Name: Subject
    
    """
    
    DeliveryMethod_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-sendnotificationaction.html#cfn-connect-rule-sendnotificationaction-deliverymethod""", alias="DeliveryMethod")
    ContentType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-sendnotificationaction.html#cfn-connect-rule-sendnotificationaction-contenttype""", alias="ContentType")
    Content_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-sendnotificationaction.html#cfn-connect-rule-sendnotificationaction-content""", alias="Content")
    Recipient_: 'NotificationRecipientType' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-sendnotificationaction.html#cfn-connect-rule-sendnotificationaction-recipient""", alias="Recipient")
    Subject_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-sendnotificationaction.html#cfn-connect-rule-sendnotificationaction-subject""", alias="Subject")
    


    @property
    def tropo_type(self) -> troposphere.connect.SendNotificationAction:
        from troposphere.connect import SendNotificationAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TaskAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-taskaction.html
    Properties:
        - Name: Description
        - Name: References
        - Name: ContactFlowArn
        - Name: Name
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-taskaction.html#cfn-connect-rule-taskaction-description""", alias="Description")
    References_: Optional[Dict[str, 'Reference']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-taskaction.html#cfn-connect-rule-taskaction-references""", alias="References")
    ContactFlowArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-taskaction.html#cfn-connect-rule-taskaction-contactflowarn""", alias="ContactFlowArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-taskaction.html#cfn-connect-rule-taskaction-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.connect.TaskAction:
        from troposphere.connect import TaskAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Constraints(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-constraints.html
    Properties:
        - Name: ReadOnlyFields
        - Name: InvisibleFields
        - Name: RequiredFields
    
    """
    
    ReadOnlyFields_: Optional[List['ReadOnlyFieldInfo']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-constraints.html#cfn-connect-tasktemplate-constraints-readonlyfields""", alias="ReadOnlyFields")
    InvisibleFields_: Optional[List['InvisibleFieldInfo']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-constraints.html#cfn-connect-tasktemplate-constraints-invisiblefields""", alias="InvisibleFields")
    RequiredFields_: Optional[List['RequiredFieldInfo']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-constraints.html#cfn-connect-tasktemplate-constraints-requiredfields""", alias="RequiredFields")
    


    @property
    def tropo_type(self) -> troposphere.connect.Constraints:
        from troposphere.connect import Constraints as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefaultFieldValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-defaultfieldvalue.html
    Properties:
        - Name: DefaultValue
        - Name: Id
    
    """
    
    DefaultValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-defaultfieldvalue.html#cfn-connect-tasktemplate-defaultfieldvalue-defaultvalue""", alias="DefaultValue")
    Id_: 'FieldIdentifier' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-defaultfieldvalue.html#cfn-connect-tasktemplate-defaultfieldvalue-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.connect.DefaultFieldValue:
        from troposphere.connect import DefaultFieldValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Field(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: Id
        - Name: SingleSelectOptions
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html#cfn-connect-tasktemplate-field-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html#cfn-connect-tasktemplate-field-description""", alias="Description")
    Id_: 'FieldIdentifier' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html#cfn-connect-tasktemplate-field-id""", alias="Id")
    SingleSelectOptions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html#cfn-connect-tasktemplate-field-singleselectoptions""", alias="SingleSelectOptions")
    


    @property
    def tropo_type(self) -> troposphere.connect.Field:
        from troposphere.connect import Field as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldIdentifier(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-fieldidentifier.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-fieldidentifier.html#cfn-connect-tasktemplate-fieldidentifier-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.connect.FieldIdentifier:
        from troposphere.connect import FieldIdentifier as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InvisibleFieldInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-invisiblefieldinfo.html
    Properties:
        - Name: Id
    
    """
    
    Id_: 'FieldIdentifier' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-invisiblefieldinfo.html#cfn-connect-tasktemplate-invisiblefieldinfo-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.connect.InvisibleFieldInfo:
        from troposphere.connect import InvisibleFieldInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReadOnlyFieldInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-readonlyfieldinfo.html
    Properties:
        - Name: Id
    
    """
    
    Id_: 'FieldIdentifier' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-readonlyfieldinfo.html#cfn-connect-tasktemplate-readonlyfieldinfo-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.connect.ReadOnlyFieldInfo:
        from troposphere.connect import ReadOnlyFieldInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RequiredFieldInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-requiredfieldinfo.html
    Properties:
        - Name: Id
    
    """
    
    Id_: 'FieldIdentifier' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-requiredfieldinfo.html#cfn-connect-tasktemplate-requiredfieldinfo-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.connect.RequiredFieldInfo:
        from troposphere.connect import RequiredFieldInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserIdentityInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html
    Properties:
        - Name: Email
        - Name: FirstName
        - Name: SecondaryEmail
        - Name: LastName
        - Name: Mobile
    
    """
    
    Email_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-email""", alias="Email")
    FirstName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-firstname""", alias="FirstName")
    SecondaryEmail_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-secondaryemail""", alias="SecondaryEmail")
    LastName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-lastname""", alias="LastName")
    Mobile_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-mobile""", alias="Mobile")
    


    @property
    def tropo_type(self) -> troposphere.connect.UserIdentityInfo:
        from troposphere.connect import UserIdentityInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UserPhoneConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html
    Properties:
        - Name: AutoAccept
        - Name: PhoneType
        - Name: DeskPhoneNumber
        - Name: AfterContactWorkTimeLimit
    
    """
    
    AutoAccept_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-autoaccept""", alias="AutoAccept")
    PhoneType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-phonetype""", alias="PhoneType")
    DeskPhoneNumber_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-deskphonenumber""", alias="DeskPhoneNumber")
    AfterContactWorkTimeLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-aftercontactworktimelimit""", alias="AfterContactWorkTimeLimit")
    


    @property
    def tropo_type(self) -> troposphere.connect.UserPhoneConfig:
        from troposphere.connect import UserPhoneConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ApprovedOrigin(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-approvedorigin.html
    Properties:
        - Name: Origin
        - Name: InstanceId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Origin_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-approvedorigin.html#cfn-connect-approvedorigin-origin""", alias="Origin")
    InstanceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-approvedorigin.html#cfn-connect-approvedorigin-instanceid""", alias="InstanceId")
    

    @property
    def tropo_type(self) -> troposphere.connect.ApprovedOrigin:
        from troposphere.connect import ApprovedOrigin as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import ApprovedOrigin as TropoT
        return resource_to_troposphere(self, TropoT)


class ContactFlow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: Content
        - Name: State
        - Name: InstanceArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ContactFlowArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-description""", alias="Description")
    Content_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-content""", alias="Content")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-state""", alias="State")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-instancearn""", alias="InstanceArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.connect.ContactFlow:
        from troposphere.connect import ContactFlow as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import ContactFlow as TropoT
        return resource_to_troposphere(self, TropoT)


class ContactFlowModule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html
    Properties:
        - Name: Description
        - Name: Content
        - Name: State
        - Name: InstanceArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ContactFlowModuleArn
        - Name: Status
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-description""", alias="Description")
    Content_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-content""", alias="Content")
    State_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-state""", alias="State")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-instancearn""", alias="InstanceArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.connect.ContactFlowModule:
        from troposphere.connect import ContactFlowModule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import ContactFlowModule as TropoT
        return resource_to_troposphere(self, TropoT)


class EvaluationForm(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html
    Properties:
        - Name: ScoringStrategy
        - Name: Status
        - Name: Description
        - Name: InstanceArn
        - Name: Title
        - Name: Items
        - Name: Tags
    Attributes:
        - Name: EvaluationFormArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ScoringStrategy_: Optional['ScoringStrategy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-scoringstrategy""", alias="ScoringStrategy")
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-status""", alias="Status")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-description""", alias="Description")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-instancearn""", alias="InstanceArn")
    Title_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-title""", alias="Title")
    Items_: List['EvaluationFormBaseItem'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-items""", alias="Items")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.connect.EvaluationForm:
        from troposphere.connect import EvaluationForm as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import EvaluationForm as TropoT
        return resource_to_troposphere(self, TropoT)


class HoursOfOperation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html
    Properties:
        - Name: TimeZone
        - Name: Description
        - Name: Config
        - Name: InstanceArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: HoursOfOperationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TimeZone_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-timezone""", alias="TimeZone")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-description""", alias="Description")
    Config_: List['HoursOfOperationConfig'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-config""", alias="Config")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-instancearn""", alias="InstanceArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.connect.HoursOfOperation:
        from troposphere.connect import HoursOfOperation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import HoursOfOperation as TropoT
        return resource_to_troposphere(self, TropoT)


class Instance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html
    Properties:
        - Name: DirectoryId
        - Name: IdentityManagementType
        - Name: InstanceAlias
        - Name: Attributes
    Attributes:
        - Name: CreatedTime
        - Name: ServiceRole
        - Name: InstanceStatus
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DirectoryId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html#cfn-connect-instance-directoryid""", alias="DirectoryId")
    IdentityManagementType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html#cfn-connect-instance-identitymanagementtype""", alias="IdentityManagementType")
    InstanceAlias_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html#cfn-connect-instance-instancealias""", alias="InstanceAlias")
    Attributes_: 'Attributes' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html#cfn-connect-instance-attributes""", alias="Attributes")
    

    @property
    def tropo_type(self) -> troposphere.connect.Instance:
        from troposphere.connect import Instance as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import Instance as TropoT
        return resource_to_troposphere(self, TropoT)


class InstanceStorageConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html
    Properties:
        - Name: KinesisStreamConfig
        - Name: S3Config
        - Name: StorageType
        - Name: InstanceArn
        - Name: ResourceType
        - Name: KinesisVideoStreamConfig
        - Name: KinesisFirehoseConfig
    Attributes:
        - Name: AssociationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KinesisStreamConfig_: Optional['KinesisStreamConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-kinesisstreamconfig""", alias="KinesisStreamConfig")
    S3Config_: Optional['S3Config'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-s3config""", alias="S3Config")
    StorageType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-storagetype""", alias="StorageType")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-instancearn""", alias="InstanceArn")
    ResourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-resourcetype""", alias="ResourceType")
    KinesisVideoStreamConfig_: Optional['KinesisVideoStreamConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-kinesisvideostreamconfig""", alias="KinesisVideoStreamConfig")
    KinesisFirehoseConfig_: Optional['KinesisFirehoseConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-kinesisfirehoseconfig""", alias="KinesisFirehoseConfig")
    

    @property
    def tropo_type(self) -> troposphere.connect.InstanceStorageConfig:
        from troposphere.connect import InstanceStorageConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import InstanceStorageConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class IntegrationAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-integrationassociation.html
    Properties:
        - Name: IntegrationArn
        - Name: InstanceId
        - Name: IntegrationType
    Attributes:
        - Name: IntegrationAssociationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IntegrationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-integrationassociation.html#cfn-connect-integrationassociation-integrationarn""", alias="IntegrationArn")
    InstanceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-integrationassociation.html#cfn-connect-integrationassociation-instanceid""", alias="InstanceId")
    IntegrationType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-integrationassociation.html#cfn-connect-integrationassociation-integrationtype""", alias="IntegrationType")
    

    @property
    def tropo_type(self) -> troposphere.connect.IntegrationAssociation:
        from troposphere.connect import IntegrationAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import IntegrationAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class PhoneNumber(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: TargetArn
        - Name: Prefix
        - Name: CountryCode
        - Name: Tags
    Attributes:
        - Name: Address
        - Name: PhoneNumberArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-description""", alias="Description")
    TargetArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-targetarn""", alias="TargetArn")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-prefix""", alias="Prefix")
    CountryCode_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-countrycode""", alias="CountryCode")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.connect.PhoneNumber:
        from troposphere.connect import PhoneNumber as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import PhoneNumber as TropoT
        return resource_to_troposphere(self, TropoT)


class Prompt(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html
    Properties:
        - Name: Description
        - Name: S3Uri
        - Name: InstanceArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: PromptArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html#cfn-connect-prompt-description""", alias="Description")
    S3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html#cfn-connect-prompt-s3uri""", alias="S3Uri")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html#cfn-connect-prompt-instancearn""", alias="InstanceArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html#cfn-connect-prompt-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html#cfn-connect-prompt-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.connect.Prompt:
        from troposphere.connect import Prompt as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import Prompt as TropoT
        return resource_to_troposphere(self, TropoT)


class Queue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html
    Properties:
        - Name: Status
        - Name: HoursOfOperationArn
        - Name: Description
        - Name: InstanceArn
        - Name: QuickConnectArns
        - Name: OutboundCallerConfig
        - Name: MaxContacts
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Type
        - Name: QueueArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-status""", alias="Status")
    HoursOfOperationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-hoursofoperationarn""", alias="HoursOfOperationArn")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-description""", alias="Description")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-instancearn""", alias="InstanceArn")
    QuickConnectArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-quickconnectarns""", alias="QuickConnectArns")
    OutboundCallerConfig_: Optional['OutboundCallerConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-outboundcallerconfig""", alias="OutboundCallerConfig")
    MaxContacts_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-maxcontacts""", alias="MaxContacts")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.connect.Queue:
        from troposphere.connect import Queue as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import Queue as TropoT
        return resource_to_troposphere(self, TropoT)


class QuickConnect(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html
    Properties:
        - Name: Description
        - Name: QuickConnectConfig
        - Name: InstanceArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: QuickConnectArn
        - Name: QuickConnectType
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-description""", alias="Description")
    QuickConnectConfig_: 'QuickConnectConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-quickconnectconfig""", alias="QuickConnectConfig")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-instancearn""", alias="InstanceArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.connect.QuickConnect:
        from troposphere.connect import QuickConnect as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import QuickConnect as TropoT
        return resource_to_troposphere(self, TropoT)


class RoutingProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html
    Properties:
        - Name: Description
        - Name: MediaConcurrencies
        - Name: InstanceArn
        - Name: AgentAvailabilityTimer
        - Name: QueueConfigs
        - Name: DefaultOutboundQueueArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: RoutingProfileArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-description""", alias="Description")
    MediaConcurrencies_: List['MediaConcurrency'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-mediaconcurrencies""", alias="MediaConcurrencies")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-instancearn""", alias="InstanceArn")
    AgentAvailabilityTimer_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-agentavailabilitytimer""", alias="AgentAvailabilityTimer")
    QueueConfigs_: Optional[List['RoutingProfileQueueConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-queueconfigs""", alias="QueueConfigs")
    DefaultOutboundQueueArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-defaultoutboundqueuearn""", alias="DefaultOutboundQueueArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.connect.RoutingProfile:
        from troposphere.connect import RoutingProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import RoutingProfile as TropoT
        return resource_to_troposphere(self, TropoT)


class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html
    Properties:
        - Name: Function
        - Name: TriggerEventSource
        - Name: Actions
        - Name: InstanceArn
        - Name: Tags
        - Name: Name
        - Name: PublishStatus
    Attributes:
        - Name: RuleArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Function_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-function""", alias="Function")
    TriggerEventSource_: 'RuleTriggerEventSource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-triggereventsource""", alias="TriggerEventSource")
    Actions_: 'Actions' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-actions""", alias="Actions")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-instancearn""", alias="InstanceArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-name""", alias="Name")
    PublishStatus_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-publishstatus""", alias="PublishStatus")
    

    @property
    def tropo_type(self) -> troposphere.connect.Rule:
        from troposphere.connect import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import Rule as TropoT
        return resource_to_troposphere(self, TropoT)


class SecurityKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securitykey.html
    Properties:
        - Name: InstanceId
        - Name: Key
    Attributes:
        - Name: AssociationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InstanceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securitykey.html#cfn-connect-securitykey-instanceid""", alias="InstanceId")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securitykey.html#cfn-connect-securitykey-key""", alias="Key")
    

    @property
    def tropo_type(self) -> troposphere.connect.SecurityKey:
        from troposphere.connect import SecurityKey as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import SecurityKey as TropoT
        return resource_to_troposphere(self, TropoT)


class SecurityProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html
    Properties:
        - Name: AllowedAccessControlTags
        - Name: Description
        - Name: InstanceArn
        - Name: Permissions
        - Name: SecurityProfileName
        - Name: TagRestrictedResources
        - Name: Tags
    Attributes:
        - Name: SecurityProfileArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AllowedAccessControlTags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-allowedaccesscontroltags""", alias="AllowedAccessControlTags")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-description""", alias="Description")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-instancearn""", alias="InstanceArn")
    Permissions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-permissions""", alias="Permissions")
    SecurityProfileName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-securityprofilename""", alias="SecurityProfileName")
    TagRestrictedResources_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-tagrestrictedresources""", alias="TagRestrictedResources")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.connect.SecurityProfile:
        from troposphere.connect import SecurityProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import SecurityProfile as TropoT
        return resource_to_troposphere(self, TropoT)


class TaskTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html
    Properties:
        - Name: Status
        - Name: Description
        - Name: Constraints
        - Name: Defaults
        - Name: Fields
        - Name: InstanceArn
        - Name: ContactFlowArn
        - Name: ClientToken
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-status""", alias="Status")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-description""", alias="Description")
    Constraints_: Optional['Constraints'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-constraints""", alias="Constraints")
    Defaults_: Optional[List['DefaultFieldValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-defaults""", alias="Defaults")
    Fields_: Optional[List['Field']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-fields""", alias="Fields")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-instancearn""", alias="InstanceArn")
    ContactFlowArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-contactflowarn""", alias="ContactFlowArn")
    ClientToken_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-clienttoken""", alias="ClientToken")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.connect.TaskTemplate:
        from troposphere.connect import TaskTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import TaskTemplate as TropoT
        return resource_to_troposphere(self, TropoT)


class TrafficDistributionGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html
    Properties:
        - Name: Description
        - Name: InstanceArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Status
        - Name: IsDefault
        - Name: TrafficDistributionGroupArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html#cfn-connect-trafficdistributiongroup-description""", alias="Description")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html#cfn-connect-trafficdistributiongroup-instancearn""", alias="InstanceArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html#cfn-connect-trafficdistributiongroup-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html#cfn-connect-trafficdistributiongroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.connect.TrafficDistributionGroup:
        from troposphere.connect import TrafficDistributionGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import TrafficDistributionGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class User(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html
    Properties:
        - Name: RoutingProfileArn
        - Name: Username
        - Name: PhoneConfig
        - Name: InstanceArn
        - Name: DirectoryUserId
        - Name: IdentityInfo
        - Name: HierarchyGroupArn
        - Name: SecurityProfileArns
        - Name: Tags
        - Name: Password
    Attributes:
        - Name: UserArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RoutingProfileArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-routingprofilearn""", alias="RoutingProfileArn")
    Username_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-username""", alias="Username")
    PhoneConfig_: 'UserPhoneConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-phoneconfig""", alias="PhoneConfig")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-instancearn""", alias="InstanceArn")
    DirectoryUserId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-directoryuserid""", alias="DirectoryUserId")
    IdentityInfo_: Optional['UserIdentityInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-identityinfo""", alias="IdentityInfo")
    HierarchyGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-hierarchygrouparn""", alias="HierarchyGroupArn")
    SecurityProfileArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-securityprofilearns""", alias="SecurityProfileArns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-tags""", alias="Tags")
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-password""", alias="Password")
    

    @property
    def tropo_type(self) -> troposphere.connect.User:
        from troposphere.connect import User as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import User as TropoT
        return resource_to_troposphere(self, TropoT)


class UserHierarchyGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html
    Properties:
        - Name: InstanceArn
        - Name: ParentGroupArn
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: UserHierarchyGroupArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-instancearn""", alias="InstanceArn")
    ParentGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-parentgrouparn""", alias="ParentGroupArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.connect.UserHierarchyGroup:
        from troposphere.connect import UserHierarchyGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import UserHierarchyGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class View(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html
    Properties:
        - Name: Description
        - Name: Actions
        - Name: InstanceArn
        - Name: Tags
        - Name: Name
        - Name: Template
    Attributes:
        - Name: ViewArn
        - Name: ViewContentSha256
        - Name: ViewId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html#cfn-connect-view-description""", alias="Description")
    Actions_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html#cfn-connect-view-actions""", alias="Actions")
    InstanceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html#cfn-connect-view-instancearn""", alias="InstanceArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html#cfn-connect-view-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html#cfn-connect-view-name""", alias="Name")
    Template_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html#cfn-connect-view-template""", alias="Template")
    

    @property
    def tropo_type(self) -> troposphere.connect.View:
        from troposphere.connect import View as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import View as TropoT
        return resource_to_troposphere(self, TropoT)


class ViewVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.html
    Properties:
        - Name: ViewArn
        - Name: VersionDescription
        - Name: ViewContentSha256
    Attributes:
        - Name: ViewVersionArn
        - Name: Version
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ViewArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.html#cfn-connect-viewversion-viewarn""", alias="ViewArn")
    VersionDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.html#cfn-connect-viewversion-versiondescription""", alias="VersionDescription")
    ViewContentSha256_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.html#cfn-connect-viewversion-viewcontentsha256""", alias="ViewContentSha256")
    

    @property
    def tropo_type(self) -> troposphere.connect.ViewVersion:
        from troposphere.connect import ViewVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.connect import ViewVersion as TropoT
        return resource_to_troposphere(self, TropoT)

