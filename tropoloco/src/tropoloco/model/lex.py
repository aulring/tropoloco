from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AdvancedRecognitionSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-advancedrecognitionsetting.html
    Properties:
        - Name: AudioRecognitionStrategy
    
    """
    
    AudioRecognitionStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-advancedrecognitionsetting.html#cfn-lex-bot-advancedrecognitionsetting-audiorecognitionstrategy""", alias="AudioRecognitionStrategy")
    


    @property
    def tropo_type(self) -> troposphere.lex.AdvancedRecognitionSetting:
        from troposphere.lex import AdvancedRecognitionSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AllowedInputTypes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-allowedinputtypes.html
    Properties:
        - Name: AllowDTMFInput
        - Name: AllowAudioInput
    
    """
    
    AllowDTMFInput_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-allowedinputtypes.html#cfn-lex-bot-allowedinputtypes-allowdtmfinput""", alias="AllowDTMFInput")
    AllowAudioInput_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-allowedinputtypes.html#cfn-lex-bot-allowedinputtypes-allowaudioinput""", alias="AllowAudioInput")
    


    @property
    def tropo_type(self) -> troposphere.lex.AllowedInputTypes:
        from troposphere.lex import AllowedInputTypes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioAndDTMFInputSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audioanddtmfinputspecification.html
    Properties:
        - Name: DTMFSpecification
        - Name: AudioSpecification
        - Name: StartTimeoutMs
    
    """
    
    DTMFSpecification_: Optional['DTMFSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audioanddtmfinputspecification.html#cfn-lex-bot-audioanddtmfinputspecification-dtmfspecification""", alias="DTMFSpecification")
    AudioSpecification_: Optional['AudioSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audioanddtmfinputspecification.html#cfn-lex-bot-audioanddtmfinputspecification-audiospecification""", alias="AudioSpecification")
    StartTimeoutMs_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audioanddtmfinputspecification.html#cfn-lex-bot-audioanddtmfinputspecification-starttimeoutms""", alias="StartTimeoutMs")
    


    @property
    def tropo_type(self) -> troposphere.lex.AudioAndDTMFInputSpecification:
        from troposphere.lex import AudioAndDTMFInputSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioLogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiologdestination.html
    Properties:
        - Name: S3Bucket
    
    """
    
    S3Bucket_: 'S3BucketLogDestination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiologdestination.html#cfn-lex-bot-audiologdestination-s3bucket""", alias="S3Bucket")
    


    @property
    def tropo_type(self) -> troposphere.lex.AudioLogDestination:
        from troposphere.lex import AudioLogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioLogSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiologsetting.html
    Properties:
        - Name: Destination
        - Name: Enabled
    
    """
    
    Destination_: 'AudioLogDestination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiologsetting.html#cfn-lex-bot-audiologsetting-destination""", alias="Destination")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiologsetting.html#cfn-lex-bot-audiologsetting-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.lex.AudioLogSetting:
        from troposphere.lex import AudioLogSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiospecification.html
    Properties:
        - Name: EndTimeoutMs
        - Name: MaxLengthMs
    
    """
    
    EndTimeoutMs_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiospecification.html#cfn-lex-bot-audiospecification-endtimeoutms""", alias="EndTimeoutMs")
    MaxLengthMs_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiospecification.html#cfn-lex-bot-audiospecification-maxlengthms""", alias="MaxLengthMs")
    


    @property
    def tropo_type(self) -> troposphere.lex.AudioSpecification:
        from troposphere.lex import AudioSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BotAliasLocaleSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botaliaslocalesettings.html
    Properties:
        - Name: CodeHookSpecification
        - Name: Enabled
    
    """
    
    CodeHookSpecification_: Optional['CodeHookSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botaliaslocalesettings.html#cfn-lex-bot-botaliaslocalesettings-codehookspecification""", alias="CodeHookSpecification")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botaliaslocalesettings.html#cfn-lex-bot-botaliaslocalesettings-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.lex.BotAliasLocaleSettings:
        from troposphere.lex import BotAliasLocaleSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BotAliasLocaleSettingsItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botaliaslocalesettingsitem.html
    Properties:
        - Name: LocaleId
        - Name: BotAliasLocaleSetting
    
    """
    
    LocaleId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botaliaslocalesettingsitem.html#cfn-lex-bot-botaliaslocalesettingsitem-localeid""", alias="LocaleId")
    BotAliasLocaleSetting_: 'BotAliasLocaleSettings' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botaliaslocalesettingsitem.html#cfn-lex-bot-botaliaslocalesettingsitem-botaliaslocalesetting""", alias="BotAliasLocaleSetting")
    


    @property
    def tropo_type(self) -> troposphere.lex.BotAliasLocaleSettingsItem:
        from troposphere.lex import BotAliasLocaleSettingsItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BotLocale(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html
    Properties:
        - Name: NluConfidenceThreshold
        - Name: LocaleId
        - Name: Description
        - Name: CustomVocabulary
        - Name: SlotTypes
        - Name: Intents
        - Name: VoiceSettings
    
    """
    
    NluConfidenceThreshold_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-nluconfidencethreshold""", alias="NluConfidenceThreshold")
    LocaleId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-localeid""", alias="LocaleId")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-description""", alias="Description")
    CustomVocabulary_: Optional['CustomVocabulary'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-customvocabulary""", alias="CustomVocabulary")
    SlotTypes_: Optional[List['SlotType']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-slottypes""", alias="SlotTypes")
    Intents_: Optional[List['Intent']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-intents""", alias="Intents")
    VoiceSettings_: Optional['VoiceSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-voicesettings""", alias="VoiceSettings")
    


    @property
    def tropo_type(self) -> troposphere.lex.BotLocale:
        from troposphere.lex import BotLocale as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Button(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-button.html
    Properties:
        - Name: Value
        - Name: Text
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-button.html#cfn-lex-bot-button-value""", alias="Value")
    Text_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-button.html#cfn-lex-bot-button-text""", alias="Text")
    


    @property
    def tropo_type(self) -> troposphere.lex.Button:
        from troposphere.lex import Button as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchLogGroupLogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-cloudwatchloggrouplogdestination.html
    Properties:
        - Name: CloudWatchLogGroupArn
        - Name: LogPrefix
    
    """
    
    CloudWatchLogGroupArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-cloudwatchloggrouplogdestination.html#cfn-lex-bot-cloudwatchloggrouplogdestination-cloudwatchloggrouparn""", alias="CloudWatchLogGroupArn")
    LogPrefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-cloudwatchloggrouplogdestination.html#cfn-lex-bot-cloudwatchloggrouplogdestination-logprefix""", alias="LogPrefix")
    


    @property
    def tropo_type(self) -> troposphere.lex.CloudWatchLogGroupLogDestination:
        from troposphere.lex import CloudWatchLogGroupLogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CodeHookSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-codehookspecification.html
    Properties:
        - Name: LambdaCodeHook
    
    """
    
    LambdaCodeHook_: 'LambdaCodeHook' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-codehookspecification.html#cfn-lex-bot-codehookspecification-lambdacodehook""", alias="LambdaCodeHook")
    


    @property
    def tropo_type(self) -> troposphere.lex.CodeHookSpecification:
        from troposphere.lex import CodeHookSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Condition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-condition.html
    Properties:
        - Name: ExpressionString
    
    """
    
    ExpressionString_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-condition.html#cfn-lex-bot-condition-expressionstring""", alias="ExpressionString")
    


    @property
    def tropo_type(self) -> troposphere.lex.Condition:
        from troposphere.lex import Condition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConditionalBranch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalbranch.html
    Properties:
        - Name: Condition
        - Name: Response
        - Name: Name
        - Name: NextStep
    
    """
    
    Condition_: 'Condition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalbranch.html#cfn-lex-bot-conditionalbranch-condition""", alias="Condition")
    Response_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalbranch.html#cfn-lex-bot-conditionalbranch-response""", alias="Response")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalbranch.html#cfn-lex-bot-conditionalbranch-name""", alias="Name")
    NextStep_: 'DialogState' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalbranch.html#cfn-lex-bot-conditionalbranch-nextstep""", alias="NextStep")
    


    @property
    def tropo_type(self) -> troposphere.lex.ConditionalBranch:
        from troposphere.lex import ConditionalBranch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConditionalSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalspecification.html
    Properties:
        - Name: DefaultBranch
        - Name: IsActive
        - Name: ConditionalBranches
    
    """
    
    DefaultBranch_: 'DefaultConditionalBranch' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalspecification.html#cfn-lex-bot-conditionalspecification-defaultbranch""", alias="DefaultBranch")
    IsActive_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalspecification.html#cfn-lex-bot-conditionalspecification-isactive""", alias="IsActive")
    ConditionalBranches_: List['ConditionalBranch'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalspecification.html#cfn-lex-bot-conditionalspecification-conditionalbranches""", alias="ConditionalBranches")
    


    @property
    def tropo_type(self) -> troposphere.lex.ConditionalSpecification:
        from troposphere.lex import ConditionalSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConversationLogSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conversationlogsettings.html
    Properties:
        - Name: TextLogSettings
        - Name: AudioLogSettings
    
    """
    
    TextLogSettings_: Optional[List['TextLogSetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conversationlogsettings.html#cfn-lex-bot-conversationlogsettings-textlogsettings""", alias="TextLogSettings")
    AudioLogSettings_: Optional[List['AudioLogSetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conversationlogsettings.html#cfn-lex-bot-conversationlogsettings-audiologsettings""", alias="AudioLogSettings")
    


    @property
    def tropo_type(self) -> troposphere.lex.ConversationLogSettings:
        from troposphere.lex import ConversationLogSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomPayload(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-custompayload.html
    Properties:
        - Name: Value
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-custompayload.html#cfn-lex-bot-custompayload-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.lex.CustomPayload:
        from troposphere.lex import CustomPayload as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomVocabulary(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-customvocabulary.html
    Properties:
        - Name: CustomVocabularyItems
    
    """
    
    CustomVocabularyItems_: List['CustomVocabularyItem'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-customvocabulary.html#cfn-lex-bot-customvocabulary-customvocabularyitems""", alias="CustomVocabularyItems")
    


    @property
    def tropo_type(self) -> troposphere.lex.CustomVocabulary:
        from troposphere.lex import CustomVocabulary as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomVocabularyItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-customvocabularyitem.html
    Properties:
        - Name: DisplayAs
        - Name: Phrase
        - Name: Weight
    
    """
    
    DisplayAs_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-customvocabularyitem.html#cfn-lex-bot-customvocabularyitem-displayas""", alias="DisplayAs")
    Phrase_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-customvocabularyitem.html#cfn-lex-bot-customvocabularyitem-phrase""", alias="Phrase")
    Weight_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-customvocabularyitem.html#cfn-lex-bot-customvocabularyitem-weight""", alias="Weight")
    


    @property
    def tropo_type(self) -> troposphere.lex.CustomVocabularyItem:
        from troposphere.lex import CustomVocabularyItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DTMFSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dtmfspecification.html
    Properties:
        - Name: DeletionCharacter
        - Name: EndTimeoutMs
        - Name: EndCharacter
        - Name: MaxLength
    
    """
    
    DeletionCharacter_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dtmfspecification.html#cfn-lex-bot-dtmfspecification-deletioncharacter""", alias="DeletionCharacter")
    EndTimeoutMs_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dtmfspecification.html#cfn-lex-bot-dtmfspecification-endtimeoutms""", alias="EndTimeoutMs")
    EndCharacter_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dtmfspecification.html#cfn-lex-bot-dtmfspecification-endcharacter""", alias="EndCharacter")
    MaxLength_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dtmfspecification.html#cfn-lex-bot-dtmfspecification-maxlength""", alias="MaxLength")
    


    @property
    def tropo_type(self) -> troposphere.lex.DTMFSpecification:
        from troposphere.lex import DTMFSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataPrivacy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dataprivacy.html
    Properties:
        - Name: ChildDirected
    
    """
    
    ChildDirected_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dataprivacy.html#cfn-lex-bot-dataprivacy-childdirected""", alias="ChildDirected")
    


    @property
    def tropo_type(self) -> troposphere.lex.DataPrivacy:
        from troposphere.lex import DataPrivacy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefaultConditionalBranch(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-defaultconditionalbranch.html
    Properties:
        - Name: Response
        - Name: NextStep
    
    """
    
    Response_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-defaultconditionalbranch.html#cfn-lex-bot-defaultconditionalbranch-response""", alias="Response")
    NextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-defaultconditionalbranch.html#cfn-lex-bot-defaultconditionalbranch-nextstep""", alias="NextStep")
    


    @property
    def tropo_type(self) -> troposphere.lex.DefaultConditionalBranch:
        from troposphere.lex import DefaultConditionalBranch as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DialogAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogaction.html
    Properties:
        - Name: Type
        - Name: SlotToElicit
        - Name: SuppressNextMessage
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogaction.html#cfn-lex-bot-dialogaction-type""", alias="Type")
    SlotToElicit_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogaction.html#cfn-lex-bot-dialogaction-slottoelicit""", alias="SlotToElicit")
    SuppressNextMessage_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogaction.html#cfn-lex-bot-dialogaction-suppressnextmessage""", alias="SuppressNextMessage")
    


    @property
    def tropo_type(self) -> troposphere.lex.DialogAction:
        from troposphere.lex import DialogAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DialogCodeHookInvocationSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehookinvocationsetting.html
    Properties:
        - Name: EnableCodeHookInvocation
        - Name: InvocationLabel
        - Name: IsActive
        - Name: PostCodeHookSpecification
    
    """
    
    EnableCodeHookInvocation_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehookinvocationsetting.html#cfn-lex-bot-dialogcodehookinvocationsetting-enablecodehookinvocation""", alias="EnableCodeHookInvocation")
    InvocationLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehookinvocationsetting.html#cfn-lex-bot-dialogcodehookinvocationsetting-invocationlabel""", alias="InvocationLabel")
    IsActive_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehookinvocationsetting.html#cfn-lex-bot-dialogcodehookinvocationsetting-isactive""", alias="IsActive")
    PostCodeHookSpecification_: 'PostDialogCodeHookInvocationSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehookinvocationsetting.html#cfn-lex-bot-dialogcodehookinvocationsetting-postcodehookspecification""", alias="PostCodeHookSpecification")
    


    @property
    def tropo_type(self) -> troposphere.lex.DialogCodeHookInvocationSetting:
        from troposphere.lex import DialogCodeHookInvocationSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DialogCodeHookSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehooksetting.html
    Properties:
        - Name: Enabled
    
    """
    
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehooksetting.html#cfn-lex-bot-dialogcodehooksetting-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.lex.DialogCodeHookSetting:
        from troposphere.lex import DialogCodeHookSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DialogState(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogstate.html
    Properties:
        - Name: DialogAction
        - Name: SessionAttributes
        - Name: Intent
    
    """
    
    DialogAction_: Optional['DialogAction'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogstate.html#cfn-lex-bot-dialogstate-dialogaction""", alias="DialogAction")
    SessionAttributes_: Optional[List['SessionAttribute']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogstate.html#cfn-lex-bot-dialogstate-sessionattributes""", alias="SessionAttributes")
    Intent_: Optional['IntentOverride'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogstate.html#cfn-lex-bot-dialogstate-intent""", alias="Intent")
    


    @property
    def tropo_type(self) -> troposphere.lex.DialogState:
        from troposphere.lex import DialogState as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ElicitationCodeHookInvocationSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-elicitationcodehookinvocationsetting.html
    Properties:
        - Name: EnableCodeHookInvocation
        - Name: InvocationLabel
    
    """
    
    EnableCodeHookInvocation_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-elicitationcodehookinvocationsetting.html#cfn-lex-bot-elicitationcodehookinvocationsetting-enablecodehookinvocation""", alias="EnableCodeHookInvocation")
    InvocationLabel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-elicitationcodehookinvocationsetting.html#cfn-lex-bot-elicitationcodehookinvocationsetting-invocationlabel""", alias="InvocationLabel")
    


    @property
    def tropo_type(self) -> troposphere.lex.ElicitationCodeHookInvocationSetting:
        from troposphere.lex import ElicitationCodeHookInvocationSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExternalSourceSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-externalsourcesetting.html
    Properties:
        - Name: GrammarSlotTypeSetting
    
    """
    
    GrammarSlotTypeSetting_: Optional['GrammarSlotTypeSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-externalsourcesetting.html#cfn-lex-bot-externalsourcesetting-grammarslottypesetting""", alias="GrammarSlotTypeSetting")
    


    @property
    def tropo_type(self) -> troposphere.lex.ExternalSourceSetting:
        from troposphere.lex import ExternalSourceSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FulfillmentCodeHookSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html
    Properties:
        - Name: PostFulfillmentStatusSpecification
        - Name: FulfillmentUpdatesSpecification
        - Name: IsActive
        - Name: Enabled
    
    """
    
    PostFulfillmentStatusSpecification_: Optional['PostFulfillmentStatusSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-postfulfillmentstatusspecification""", alias="PostFulfillmentStatusSpecification")
    FulfillmentUpdatesSpecification_: Optional['FulfillmentUpdatesSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-fulfillmentupdatesspecification""", alias="FulfillmentUpdatesSpecification")
    IsActive_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-isactive""", alias="IsActive")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.lex.FulfillmentCodeHookSetting:
        from troposphere.lex import FulfillmentCodeHookSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FulfillmentStartResponseSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html
    Properties:
        - Name: DelayInSeconds
        - Name: MessageGroups
        - Name: AllowInterrupt
    
    """
    
    DelayInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html#cfn-lex-bot-fulfillmentstartresponsespecification-delayinseconds""", alias="DelayInSeconds")
    MessageGroups_: List['MessageGroup'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html#cfn-lex-bot-fulfillmentstartresponsespecification-messagegroups""", alias="MessageGroups")
    AllowInterrupt_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html#cfn-lex-bot-fulfillmentstartresponsespecification-allowinterrupt""", alias="AllowInterrupt")
    


    @property
    def tropo_type(self) -> troposphere.lex.FulfillmentStartResponseSpecification:
        from troposphere.lex import FulfillmentStartResponseSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FulfillmentUpdateResponseSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html
    Properties:
        - Name: MessageGroups
        - Name: AllowInterrupt
        - Name: FrequencyInSeconds
    
    """
    
    MessageGroups_: List['MessageGroup'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html#cfn-lex-bot-fulfillmentupdateresponsespecification-messagegroups""", alias="MessageGroups")
    AllowInterrupt_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html#cfn-lex-bot-fulfillmentupdateresponsespecification-allowinterrupt""", alias="AllowInterrupt")
    FrequencyInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html#cfn-lex-bot-fulfillmentupdateresponsespecification-frequencyinseconds""", alias="FrequencyInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.lex.FulfillmentUpdateResponseSpecification:
        from troposphere.lex import FulfillmentUpdateResponseSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FulfillmentUpdatesSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html
    Properties:
        - Name: UpdateResponse
        - Name: Active
        - Name: TimeoutInSeconds
        - Name: StartResponse
    
    """
    
    UpdateResponse_: Optional['FulfillmentUpdateResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-updateresponse""", alias="UpdateResponse")
    Active_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-active""", alias="Active")
    TimeoutInSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-timeoutinseconds""", alias="TimeoutInSeconds")
    StartResponse_: Optional['FulfillmentStartResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-startresponse""", alias="StartResponse")
    


    @property
    def tropo_type(self) -> troposphere.lex.FulfillmentUpdatesSpecification:
        from troposphere.lex import FulfillmentUpdatesSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrammarSlotTypeSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesetting.html
    Properties:
        - Name: Source
    
    """
    
    Source_: Optional['GrammarSlotTypeSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesetting.html#cfn-lex-bot-grammarslottypesetting-source""", alias="Source")
    


    @property
    def tropo_type(self) -> troposphere.lex.GrammarSlotTypeSetting:
        from troposphere.lex import GrammarSlotTypeSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GrammarSlotTypeSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html
    Properties:
        - Name: KmsKeyArn
        - Name: S3BucketName
        - Name: S3ObjectKey
    
    """
    
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html#cfn-lex-bot-grammarslottypesource-kmskeyarn""", alias="KmsKeyArn")
    S3BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html#cfn-lex-bot-grammarslottypesource-s3bucketname""", alias="S3BucketName")
    S3ObjectKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html#cfn-lex-bot-grammarslottypesource-s3objectkey""", alias="S3ObjectKey")
    


    @property
    def tropo_type(self) -> troposphere.lex.GrammarSlotTypeSource:
        from troposphere.lex import GrammarSlotTypeSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ImageResponseCard(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html
    Properties:
        - Name: Subtitle
        - Name: Title
        - Name: ImageUrl
        - Name: Buttons
    
    """
    
    Subtitle_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-subtitle""", alias="Subtitle")
    Title_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-title""", alias="Title")
    ImageUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-imageurl""", alias="ImageUrl")
    Buttons_: Optional[List['Button']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-buttons""", alias="Buttons")
    


    @property
    def tropo_type(self) -> troposphere.lex.ImageResponseCard:
        from troposphere.lex import ImageResponseCard as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InitialResponseSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-initialresponsesetting.html
    Properties:
        - Name: CodeHook
        - Name: InitialResponse
        - Name: Conditional
        - Name: NextStep
    
    """
    
    CodeHook_: Optional['DialogCodeHookInvocationSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-initialresponsesetting.html#cfn-lex-bot-initialresponsesetting-codehook""", alias="CodeHook")
    InitialResponse_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-initialresponsesetting.html#cfn-lex-bot-initialresponsesetting-initialresponse""", alias="InitialResponse")
    Conditional_: Optional['ConditionalSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-initialresponsesetting.html#cfn-lex-bot-initialresponsesetting-conditional""", alias="Conditional")
    NextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-initialresponsesetting.html#cfn-lex-bot-initialresponsesetting-nextstep""", alias="NextStep")
    


    @property
    def tropo_type(self) -> troposphere.lex.InitialResponseSetting:
        from troposphere.lex import InitialResponseSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputContext(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-inputcontext.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-inputcontext.html#cfn-lex-bot-inputcontext-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lex.InputContext:
        from troposphere.lex import InputContext as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Intent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html
    Properties:
        - Name: Description
        - Name: ParentIntentSignature
        - Name: InitialResponseSetting
        - Name: FulfillmentCodeHook
        - Name: IntentConfirmationSetting
        - Name: Name
        - Name: Slots
        - Name: DialogCodeHook
        - Name: InputContexts
        - Name: KendraConfiguration
        - Name: IntentClosingSetting
        - Name: OutputContexts
        - Name: SlotPriorities
        - Name: SampleUtterances
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-description""", alias="Description")
    ParentIntentSignature_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-parentintentsignature""", alias="ParentIntentSignature")
    InitialResponseSetting_: Optional['InitialResponseSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-initialresponsesetting""", alias="InitialResponseSetting")
    FulfillmentCodeHook_: Optional['FulfillmentCodeHookSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-fulfillmentcodehook""", alias="FulfillmentCodeHook")
    IntentConfirmationSetting_: Optional['IntentConfirmationSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-intentconfirmationsetting""", alias="IntentConfirmationSetting")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-name""", alias="Name")
    Slots_: Optional[List['Slot']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-slots""", alias="Slots")
    DialogCodeHook_: Optional['DialogCodeHookSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-dialogcodehook""", alias="DialogCodeHook")
    InputContexts_: Optional[List['InputContext']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-inputcontexts""", alias="InputContexts")
    KendraConfiguration_: Optional['KendraConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-kendraconfiguration""", alias="KendraConfiguration")
    IntentClosingSetting_: Optional['IntentClosingSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-intentclosingsetting""", alias="IntentClosingSetting")
    OutputContexts_: Optional[List['OutputContext']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-outputcontexts""", alias="OutputContexts")
    SlotPriorities_: Optional[List['SlotPriority']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-slotpriorities""", alias="SlotPriorities")
    SampleUtterances_: Optional[List['SampleUtterance']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-sampleutterances""", alias="SampleUtterances")
    


    @property
    def tropo_type(self) -> troposphere.lex.Intent:
        from troposphere.lex import Intent as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IntentClosingSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html
    Properties:
        - Name: IsActive
        - Name: ClosingResponse
        - Name: Conditional
        - Name: NextStep
    
    """
    
    IsActive_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html#cfn-lex-bot-intentclosingsetting-isactive""", alias="IsActive")
    ClosingResponse_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html#cfn-lex-bot-intentclosingsetting-closingresponse""", alias="ClosingResponse")
    Conditional_: Optional['ConditionalSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html#cfn-lex-bot-intentclosingsetting-conditional""", alias="Conditional")
    NextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html#cfn-lex-bot-intentclosingsetting-nextstep""", alias="NextStep")
    


    @property
    def tropo_type(self) -> troposphere.lex.IntentClosingSetting:
        from troposphere.lex import IntentClosingSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IntentConfirmationSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html
    Properties:
        - Name: PromptSpecification
        - Name: ConfirmationResponse
        - Name: DeclinationConditional
        - Name: FailureConditional
        - Name: ConfirmationConditional
        - Name: IsActive
        - Name: FailureResponse
        - Name: CodeHook
        - Name: DeclinationNextStep
        - Name: ElicitationCodeHook
        - Name: ConfirmationNextStep
        - Name: FailureNextStep
        - Name: DeclinationResponse
    
    """
    
    PromptSpecification_: 'PromptSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-promptspecification""", alias="PromptSpecification")
    ConfirmationResponse_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-confirmationresponse""", alias="ConfirmationResponse")
    DeclinationConditional_: Optional['ConditionalSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-declinationconditional""", alias="DeclinationConditional")
    FailureConditional_: Optional['ConditionalSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-failureconditional""", alias="FailureConditional")
    ConfirmationConditional_: Optional['ConditionalSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-confirmationconditional""", alias="ConfirmationConditional")
    IsActive_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-isactive""", alias="IsActive")
    FailureResponse_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-failureresponse""", alias="FailureResponse")
    CodeHook_: Optional['DialogCodeHookInvocationSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-codehook""", alias="CodeHook")
    DeclinationNextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-declinationnextstep""", alias="DeclinationNextStep")
    ElicitationCodeHook_: Optional['ElicitationCodeHookInvocationSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-elicitationcodehook""", alias="ElicitationCodeHook")
    ConfirmationNextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-confirmationnextstep""", alias="ConfirmationNextStep")
    FailureNextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-failurenextstep""", alias="FailureNextStep")
    DeclinationResponse_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-declinationresponse""", alias="DeclinationResponse")
    


    @property
    def tropo_type(self) -> troposphere.lex.IntentConfirmationSetting:
        from troposphere.lex import IntentConfirmationSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IntentOverride(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentoverride.html
    Properties:
        - Name: Slots
        - Name: Name
    
    """
    
    Slots_: Optional[List['SlotValueOverrideMap']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentoverride.html#cfn-lex-bot-intentoverride-slots""", alias="Slots")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentoverride.html#cfn-lex-bot-intentoverride-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lex.IntentOverride:
        from troposphere.lex import IntentOverride as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KendraConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html
    Properties:
        - Name: QueryFilterString
        - Name: QueryFilterStringEnabled
        - Name: KendraIndex
    
    """
    
    QueryFilterString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html#cfn-lex-bot-kendraconfiguration-queryfilterstring""", alias="QueryFilterString")
    QueryFilterStringEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html#cfn-lex-bot-kendraconfiguration-queryfilterstringenabled""", alias="QueryFilterStringEnabled")
    KendraIndex_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html#cfn-lex-bot-kendraconfiguration-kendraindex""", alias="KendraIndex")
    


    @property
    def tropo_type(self) -> troposphere.lex.KendraConfiguration:
        from troposphere.lex import KendraConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaCodeHook(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-lambdacodehook.html
    Properties:
        - Name: LambdaArn
        - Name: CodeHookInterfaceVersion
    
    """
    
    LambdaArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-lambdacodehook.html#cfn-lex-bot-lambdacodehook-lambdaarn""", alias="LambdaArn")
    CodeHookInterfaceVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-lambdacodehook.html#cfn-lex-bot-lambdacodehook-codehookinterfaceversion""", alias="CodeHookInterfaceVersion")
    


    @property
    def tropo_type(self) -> troposphere.lex.LambdaCodeHook:
        from troposphere.lex import LambdaCodeHook as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Message(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html
    Properties:
        - Name: CustomPayload
        - Name: ImageResponseCard
        - Name: PlainTextMessage
        - Name: SSMLMessage
    
    """
    
    CustomPayload_: Optional['CustomPayload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-custompayload""", alias="CustomPayload")
    ImageResponseCard_: Optional['ImageResponseCard'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-imageresponsecard""", alias="ImageResponseCard")
    PlainTextMessage_: Optional['PlainTextMessage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-plaintextmessage""", alias="PlainTextMessage")
    SSMLMessage_: Optional['SSMLMessage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-ssmlmessage""", alias="SSMLMessage")
    


    @property
    def tropo_type(self) -> troposphere.lex.Message:
        from troposphere.lex import Message as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MessageGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-messagegroup.html
    Properties:
        - Name: Message
        - Name: Variations
    
    """
    
    Message_: 'Message' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-messagegroup.html#cfn-lex-bot-messagegroup-message""", alias="Message")
    Variations_: Optional[List['Message']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-messagegroup.html#cfn-lex-bot-messagegroup-variations""", alias="Variations")
    


    @property
    def tropo_type(self) -> troposphere.lex.MessageGroup:
        from troposphere.lex import MessageGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MultipleValuesSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-multiplevaluessetting.html
    Properties:
        - Name: AllowMultipleValues
    
    """
    
    AllowMultipleValues_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-multiplevaluessetting.html#cfn-lex-bot-multiplevaluessetting-allowmultiplevalues""", alias="AllowMultipleValues")
    


    @property
    def tropo_type(self) -> troposphere.lex.MultipleValuesSetting:
        from troposphere.lex import MultipleValuesSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ObfuscationSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-obfuscationsetting.html
    Properties:
        - Name: ObfuscationSettingType
    
    """
    
    ObfuscationSettingType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-obfuscationsetting.html#cfn-lex-bot-obfuscationsetting-obfuscationsettingtype""", alias="ObfuscationSettingType")
    


    @property
    def tropo_type(self) -> troposphere.lex.ObfuscationSetting:
        from troposphere.lex import ObfuscationSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutputContext(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html
    Properties:
        - Name: TurnsToLive
        - Name: TimeToLiveInSeconds
        - Name: Name
    
    """
    
    TurnsToLive_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html#cfn-lex-bot-outputcontext-turnstolive""", alias="TurnsToLive")
    TimeToLiveInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html#cfn-lex-bot-outputcontext-timetoliveinseconds""", alias="TimeToLiveInSeconds")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html#cfn-lex-bot-outputcontext-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lex.OutputContext:
        from troposphere.lex import OutputContext as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PlainTextMessage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-plaintextmessage.html
    Properties:
        - Name: Value
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-plaintextmessage.html#cfn-lex-bot-plaintextmessage-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.lex.PlainTextMessage:
        from troposphere.lex import PlainTextMessage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PostDialogCodeHookInvocationSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html
    Properties:
        - Name: SuccessResponse
        - Name: FailureConditional
        - Name: TimeoutNextStep
        - Name: SuccessConditional
        - Name: TimeoutResponse
        - Name: SuccessNextStep
        - Name: FailureResponse
        - Name: FailureNextStep
        - Name: TimeoutConditional
    
    """
    
    SuccessResponse_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-successresponse""", alias="SuccessResponse")
    FailureConditional_: Optional['ConditionalSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-failureconditional""", alias="FailureConditional")
    TimeoutNextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-timeoutnextstep""", alias="TimeoutNextStep")
    SuccessConditional_: Optional['ConditionalSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-successconditional""", alias="SuccessConditional")
    TimeoutResponse_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-timeoutresponse""", alias="TimeoutResponse")
    SuccessNextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-successnextstep""", alias="SuccessNextStep")
    FailureResponse_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-failureresponse""", alias="FailureResponse")
    FailureNextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-failurenextstep""", alias="FailureNextStep")
    TimeoutConditional_: Optional['ConditionalSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-timeoutconditional""", alias="TimeoutConditional")
    


    @property
    def tropo_type(self) -> troposphere.lex.PostDialogCodeHookInvocationSpecification:
        from troposphere.lex import PostDialogCodeHookInvocationSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PostFulfillmentStatusSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html
    Properties:
        - Name: SuccessResponse
        - Name: FailureConditional
        - Name: TimeoutNextStep
        - Name: SuccessConditional
        - Name: TimeoutResponse
        - Name: SuccessNextStep
        - Name: FailureResponse
        - Name: FailureNextStep
        - Name: TimeoutConditional
    
    """
    
    SuccessResponse_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-successresponse""", alias="SuccessResponse")
    FailureConditional_: Optional['ConditionalSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-failureconditional""", alias="FailureConditional")
    TimeoutNextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-timeoutnextstep""", alias="TimeoutNextStep")
    SuccessConditional_: Optional['ConditionalSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-successconditional""", alias="SuccessConditional")
    TimeoutResponse_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-timeoutresponse""", alias="TimeoutResponse")
    SuccessNextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-successnextstep""", alias="SuccessNextStep")
    FailureResponse_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-failureresponse""", alias="FailureResponse")
    FailureNextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-failurenextstep""", alias="FailureNextStep")
    TimeoutConditional_: Optional['ConditionalSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-timeoutconditional""", alias="TimeoutConditional")
    


    @property
    def tropo_type(self) -> troposphere.lex.PostFulfillmentStatusSpecification:
        from troposphere.lex import PostFulfillmentStatusSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PromptAttemptSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptattemptspecification.html
    Properties:
        - Name: TextInputSpecification
        - Name: AllowInterrupt
        - Name: AllowedInputTypes
        - Name: AudioAndDTMFInputSpecification
    
    """
    
    TextInputSpecification_: Optional['TextInputSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptattemptspecification.html#cfn-lex-bot-promptattemptspecification-textinputspecification""", alias="TextInputSpecification")
    AllowInterrupt_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptattemptspecification.html#cfn-lex-bot-promptattemptspecification-allowinterrupt""", alias="AllowInterrupt")
    AllowedInputTypes_: 'AllowedInputTypes' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptattemptspecification.html#cfn-lex-bot-promptattemptspecification-allowedinputtypes""", alias="AllowedInputTypes")
    AudioAndDTMFInputSpecification_: Optional['AudioAndDTMFInputSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptattemptspecification.html#cfn-lex-bot-promptattemptspecification-audioanddtmfinputspecification""", alias="AudioAndDTMFInputSpecification")
    


    @property
    def tropo_type(self) -> troposphere.lex.PromptAttemptSpecification:
        from troposphere.lex import PromptAttemptSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PromptSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html
    Properties:
        - Name: MaxRetries
        - Name: MessageGroupsList
        - Name: PromptAttemptsSpecification
        - Name: AllowInterrupt
        - Name: MessageSelectionStrategy
    
    """
    
    MaxRetries_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-maxretries""", alias="MaxRetries")
    MessageGroupsList_: List['MessageGroup'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-messagegroupslist""", alias="MessageGroupsList")
    PromptAttemptsSpecification_: Optional[Dict[str, 'PromptAttemptSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-promptattemptsspecification""", alias="PromptAttemptsSpecification")
    AllowInterrupt_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-allowinterrupt""", alias="AllowInterrupt")
    MessageSelectionStrategy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-messageselectionstrategy""", alias="MessageSelectionStrategy")
    


    @property
    def tropo_type(self) -> troposphere.lex.PromptSpecification:
        from troposphere.lex import PromptSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResponseSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-responsespecification.html
    Properties:
        - Name: MessageGroupsList
        - Name: AllowInterrupt
    
    """
    
    MessageGroupsList_: List['MessageGroup'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-responsespecification.html#cfn-lex-bot-responsespecification-messagegroupslist""", alias="MessageGroupsList")
    AllowInterrupt_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-responsespecification.html#cfn-lex-bot-responsespecification-allowinterrupt""", alias="AllowInterrupt")
    


    @property
    def tropo_type(self) -> troposphere.lex.ResponseSpecification:
        from troposphere.lex import ResponseSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3BucketLogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3bucketlogdestination.html
    Properties:
        - Name: KmsKeyArn
        - Name: LogPrefix
        - Name: S3BucketArn
    
    """
    
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3bucketlogdestination.html#cfn-lex-bot-s3bucketlogdestination-kmskeyarn""", alias="KmsKeyArn")
    LogPrefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3bucketlogdestination.html#cfn-lex-bot-s3bucketlogdestination-logprefix""", alias="LogPrefix")
    S3BucketArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3bucketlogdestination.html#cfn-lex-bot-s3bucketlogdestination-s3bucketarn""", alias="S3BucketArn")
    


    @property
    def tropo_type(self) -> troposphere.lex.S3BucketLogDestination:
        from troposphere.lex import S3BucketLogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html
    Properties:
        - Name: S3ObjectVersion
        - Name: S3Bucket
        - Name: S3ObjectKey
    
    """
    
    S3ObjectVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html#cfn-lex-bot-s3location-s3objectversion""", alias="S3ObjectVersion")
    S3Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html#cfn-lex-bot-s3location-s3bucket""", alias="S3Bucket")
    S3ObjectKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html#cfn-lex-bot-s3location-s3objectkey""", alias="S3ObjectKey")
    


    @property
    def tropo_type(self) -> troposphere.lex.S3Location:
        from troposphere.lex import S3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SSMLMessage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-ssmlmessage.html
    Properties:
        - Name: Value
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-ssmlmessage.html#cfn-lex-bot-ssmlmessage-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.lex.SSMLMessage:
        from troposphere.lex import SSMLMessage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SampleUtterance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sampleutterance.html
    Properties:
        - Name: Utterance
    
    """
    
    Utterance_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sampleutterance.html#cfn-lex-bot-sampleutterance-utterance""", alias="Utterance")
    


    @property
    def tropo_type(self) -> troposphere.lex.SampleUtterance:
        from troposphere.lex import SampleUtterance as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SampleValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-samplevalue.html
    Properties:
        - Name: Value
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-samplevalue.html#cfn-lex-bot-samplevalue-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.lex.SampleValue:
        from troposphere.lex import SampleValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SentimentAnalysisSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sentimentanalysissettings.html
    Properties:
        - Name: DetectSentiment
    
    """
    
    DetectSentiment_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sentimentanalysissettings.html#cfn-lex-bot-sentimentanalysissettings-detectsentiment""", alias="DetectSentiment")
    


    @property
    def tropo_type(self) -> troposphere.lex.SentimentAnalysisSettings:
        from troposphere.lex import SentimentAnalysisSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SessionAttribute(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sessionattribute.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sessionattribute.html#cfn-lex-bot-sessionattribute-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sessionattribute.html#cfn-lex-bot-sessionattribute-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.lex.SessionAttribute:
        from troposphere.lex import SessionAttribute as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Slot(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html
    Properties:
        - Name: Description
        - Name: SlotTypeName
        - Name: ValueElicitationSetting
        - Name: ObfuscationSetting
        - Name: Name
        - Name: MultipleValuesSetting
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-description""", alias="Description")
    SlotTypeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-slottypename""", alias="SlotTypeName")
    ValueElicitationSetting_: 'SlotValueElicitationSetting' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-valueelicitationsetting""", alias="ValueElicitationSetting")
    ObfuscationSetting_: Optional['ObfuscationSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-obfuscationsetting""", alias="ObfuscationSetting")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-name""", alias="Name")
    MultipleValuesSetting_: Optional['MultipleValuesSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-multiplevaluessetting""", alias="MultipleValuesSetting")
    


    @property
    def tropo_type(self) -> troposphere.lex.Slot:
        from troposphere.lex import Slot as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlotCaptureSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html
    Properties:
        - Name: CaptureConditional
        - Name: FailureConditional
        - Name: CaptureResponse
        - Name: CaptureNextStep
        - Name: FailureResponse
        - Name: CodeHook
        - Name: FailureNextStep
        - Name: ElicitationCodeHook
    
    """
    
    CaptureConditional_: Optional['ConditionalSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-captureconditional""", alias="CaptureConditional")
    FailureConditional_: Optional['ConditionalSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-failureconditional""", alias="FailureConditional")
    CaptureResponse_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-captureresponse""", alias="CaptureResponse")
    CaptureNextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-capturenextstep""", alias="CaptureNextStep")
    FailureResponse_: Optional['ResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-failureresponse""", alias="FailureResponse")
    CodeHook_: Optional['DialogCodeHookInvocationSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-codehook""", alias="CodeHook")
    FailureNextStep_: Optional['DialogState'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-failurenextstep""", alias="FailureNextStep")
    ElicitationCodeHook_: Optional['ElicitationCodeHookInvocationSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-elicitationcodehook""", alias="ElicitationCodeHook")
    


    @property
    def tropo_type(self) -> troposphere.lex.SlotCaptureSetting:
        from troposphere.lex import SlotCaptureSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlotDefaultValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvalue.html
    Properties:
        - Name: DefaultValue
    
    """
    
    DefaultValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvalue.html#cfn-lex-bot-slotdefaultvalue-defaultvalue""", alias="DefaultValue")
    


    @property
    def tropo_type(self) -> troposphere.lex.SlotDefaultValue:
        from troposphere.lex import SlotDefaultValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlotDefaultValueSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvaluespecification.html
    Properties:
        - Name: DefaultValueList
    
    """
    
    DefaultValueList_: List['SlotDefaultValue'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvaluespecification.html#cfn-lex-bot-slotdefaultvaluespecification-defaultvaluelist""", alias="DefaultValueList")
    


    @property
    def tropo_type(self) -> troposphere.lex.SlotDefaultValueSpecification:
        from troposphere.lex import SlotDefaultValueSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlotPriority(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotpriority.html
    Properties:
        - Name: Priority
        - Name: SlotName
    
    """
    
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotpriority.html#cfn-lex-bot-slotpriority-priority""", alias="Priority")
    SlotName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotpriority.html#cfn-lex-bot-slotpriority-slotname""", alias="SlotName")
    


    @property
    def tropo_type(self) -> troposphere.lex.SlotPriority:
        from troposphere.lex import SlotPriority as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlotType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html
    Properties:
        - Name: SlotTypeValues
        - Name: Description
        - Name: ParentSlotTypeSignature
        - Name: ValueSelectionSetting
        - Name: ExternalSourceSetting
        - Name: Name
    
    """
    
    SlotTypeValues_: Optional[List['SlotTypeValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-slottypevalues""", alias="SlotTypeValues")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-description""", alias="Description")
    ParentSlotTypeSignature_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-parentslottypesignature""", alias="ParentSlotTypeSignature")
    ValueSelectionSetting_: Optional['SlotValueSelectionSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-valueselectionsetting""", alias="ValueSelectionSetting")
    ExternalSourceSetting_: Optional['ExternalSourceSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-externalsourcesetting""", alias="ExternalSourceSetting")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.lex.SlotType:
        from troposphere.lex import SlotType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlotTypeValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottypevalue.html
    Properties:
        - Name: Synonyms
        - Name: SampleValue
    
    """
    
    Synonyms_: Optional[List['SampleValue']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottypevalue.html#cfn-lex-bot-slottypevalue-synonyms""", alias="Synonyms")
    SampleValue_: 'SampleValue' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottypevalue.html#cfn-lex-bot-slottypevalue-samplevalue""", alias="SampleValue")
    


    @property
    def tropo_type(self) -> troposphere.lex.SlotTypeValue:
        from troposphere.lex import SlotTypeValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlotValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalue.html
    Properties:
        - Name: InterpretedValue
    
    """
    
    InterpretedValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalue.html#cfn-lex-bot-slotvalue-interpretedvalue""", alias="InterpretedValue")
    


    @property
    def tropo_type(self) -> troposphere.lex.SlotValue:
        from troposphere.lex import SlotValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlotValueElicitationSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html
    Properties:
        - Name: PromptSpecification
        - Name: WaitAndContinueSpecification
        - Name: SlotConstraint
        - Name: SlotCaptureSetting
        - Name: SampleUtterances
        - Name: DefaultValueSpecification
    
    """
    
    PromptSpecification_: Optional['PromptSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-promptspecification""", alias="PromptSpecification")
    WaitAndContinueSpecification_: Optional['WaitAndContinueSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-waitandcontinuespecification""", alias="WaitAndContinueSpecification")
    SlotConstraint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-slotconstraint""", alias="SlotConstraint")
    SlotCaptureSetting_: Optional['SlotCaptureSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-slotcapturesetting""", alias="SlotCaptureSetting")
    SampleUtterances_: Optional[List['SampleUtterance']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-sampleutterances""", alias="SampleUtterances")
    DefaultValueSpecification_: Optional['SlotDefaultValueSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-defaultvaluespecification""", alias="DefaultValueSpecification")
    


    @property
    def tropo_type(self) -> troposphere.lex.SlotValueElicitationSetting:
        from troposphere.lex import SlotValueElicitationSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlotValueOverride(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverride.html
    Properties:
        - Name: Shape
        - Name: Value
        - Name: Values
    
    """
    
    Shape_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverride.html#cfn-lex-bot-slotvalueoverride-shape""", alias="Shape")
    Value_: Optional['SlotValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverride.html#cfn-lex-bot-slotvalueoverride-value""", alias="Value")
    Values_: Optional[List['SlotValueOverride']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverride.html#cfn-lex-bot-slotvalueoverride-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.lex.SlotValueOverride:
        from troposphere.lex import SlotValueOverride as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlotValueOverrideMap(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverridemap.html
    Properties:
        - Name: SlotName
        - Name: SlotValueOverride
    
    """
    
    SlotName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverridemap.html#cfn-lex-bot-slotvalueoverridemap-slotname""", alias="SlotName")
    SlotValueOverride_: Optional['SlotValueOverride'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverridemap.html#cfn-lex-bot-slotvalueoverridemap-slotvalueoverride""", alias="SlotValueOverride")
    


    @property
    def tropo_type(self) -> troposphere.lex.SlotValueOverrideMap:
        from troposphere.lex import SlotValueOverrideMap as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlotValueRegexFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueregexfilter.html
    Properties:
        - Name: Pattern
    
    """
    
    Pattern_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueregexfilter.html#cfn-lex-bot-slotvalueregexfilter-pattern""", alias="Pattern")
    


    @property
    def tropo_type(self) -> troposphere.lex.SlotValueRegexFilter:
        from troposphere.lex import SlotValueRegexFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SlotValueSelectionSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html
    Properties:
        - Name: AdvancedRecognitionSetting
        - Name: RegexFilter
        - Name: ResolutionStrategy
    
    """
    
    AdvancedRecognitionSetting_: Optional['AdvancedRecognitionSetting'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html#cfn-lex-bot-slotvalueselectionsetting-advancedrecognitionsetting""", alias="AdvancedRecognitionSetting")
    RegexFilter_: Optional['SlotValueRegexFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html#cfn-lex-bot-slotvalueselectionsetting-regexfilter""", alias="RegexFilter")
    ResolutionStrategy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html#cfn-lex-bot-slotvalueselectionsetting-resolutionstrategy""", alias="ResolutionStrategy")
    


    @property
    def tropo_type(self) -> troposphere.lex.SlotValueSelectionSetting:
        from troposphere.lex import SlotValueSelectionSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StillWaitingResponseSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html
    Properties:
        - Name: MessageGroupsList
        - Name: TimeoutInSeconds
        - Name: AllowInterrupt
        - Name: FrequencyInSeconds
    
    """
    
    MessageGroupsList_: List['MessageGroup'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-messagegroupslist""", alias="MessageGroupsList")
    TimeoutInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-timeoutinseconds""", alias="TimeoutInSeconds")
    AllowInterrupt_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-allowinterrupt""", alias="AllowInterrupt")
    FrequencyInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-frequencyinseconds""", alias="FrequencyInSeconds")
    


    @property
    def tropo_type(self) -> troposphere.lex.StillWaitingResponseSpecification:
        from troposphere.lex import StillWaitingResponseSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TestBotAliasSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-testbotaliassettings.html
    Properties:
        - Name: Description
        - Name: BotAliasLocaleSettings
        - Name: ConversationLogSettings
        - Name: SentimentAnalysisSettings
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-testbotaliassettings.html#cfn-lex-bot-testbotaliassettings-description""", alias="Description")
    BotAliasLocaleSettings_: Optional[List['BotAliasLocaleSettingsItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-testbotaliassettings.html#cfn-lex-bot-testbotaliassettings-botaliaslocalesettings""", alias="BotAliasLocaleSettings")
    ConversationLogSettings_: Optional['ConversationLogSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-testbotaliassettings.html#cfn-lex-bot-testbotaliassettings-conversationlogsettings""", alias="ConversationLogSettings")
    SentimentAnalysisSettings_: Optional['SentimentAnalysisSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-testbotaliassettings.html#cfn-lex-bot-testbotaliassettings-sentimentanalysissettings""", alias="SentimentAnalysisSettings")
    


    @property
    def tropo_type(self) -> troposphere.lex.TestBotAliasSettings:
        from troposphere.lex import TestBotAliasSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TextInputSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textinputspecification.html
    Properties:
        - Name: StartTimeoutMs
    
    """
    
    StartTimeoutMs_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textinputspecification.html#cfn-lex-bot-textinputspecification-starttimeoutms""", alias="StartTimeoutMs")
    


    @property
    def tropo_type(self) -> troposphere.lex.TextInputSpecification:
        from troposphere.lex import TextInputSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TextLogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textlogdestination.html
    Properties:
        - Name: CloudWatch
    
    """
    
    CloudWatch_: 'CloudWatchLogGroupLogDestination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textlogdestination.html#cfn-lex-bot-textlogdestination-cloudwatch""", alias="CloudWatch")
    


    @property
    def tropo_type(self) -> troposphere.lex.TextLogDestination:
        from troposphere.lex import TextLogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TextLogSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textlogsetting.html
    Properties:
        - Name: Destination
        - Name: Enabled
    
    """
    
    Destination_: 'TextLogDestination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textlogsetting.html#cfn-lex-bot-textlogsetting-destination""", alias="Destination")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textlogsetting.html#cfn-lex-bot-textlogsetting-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.lex.TextLogSetting:
        from troposphere.lex import TextLogSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VoiceSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-voicesettings.html
    Properties:
        - Name: VoiceId
        - Name: Engine
    
    """
    
    VoiceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-voicesettings.html#cfn-lex-bot-voicesettings-voiceid""", alias="VoiceId")
    Engine_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-voicesettings.html#cfn-lex-bot-voicesettings-engine""", alias="Engine")
    


    @property
    def tropo_type(self) -> troposphere.lex.VoiceSettings:
        from troposphere.lex import VoiceSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WaitAndContinueSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html
    Properties:
        - Name: WaitingResponse
        - Name: StillWaitingResponse
        - Name: IsActive
        - Name: ContinueResponse
    
    """
    
    WaitingResponse_: 'ResponseSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-waitingresponse""", alias="WaitingResponse")
    StillWaitingResponse_: Optional['StillWaitingResponseSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-stillwaitingresponse""", alias="StillWaitingResponse")
    IsActive_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-isactive""", alias="IsActive")
    ContinueResponse_: 'ResponseSpecification' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-continueresponse""", alias="ContinueResponse")
    


    @property
    def tropo_type(self) -> troposphere.lex.WaitAndContinueSpecification:
        from troposphere.lex import WaitAndContinueSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioLogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologdestination.html
    Properties:
        - Name: S3Bucket
    
    """
    
    S3Bucket_: 'S3BucketLogDestination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologdestination.html#cfn-lex-botalias-audiologdestination-s3bucket""", alias="S3Bucket")
    


    @property
    def tropo_type(self) -> troposphere.lex.AudioLogDestination:
        from troposphere.lex import AudioLogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AudioLogSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologsetting.html
    Properties:
        - Name: Destination
        - Name: Enabled
    
    """
    
    Destination_: 'AudioLogDestination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologsetting.html#cfn-lex-botalias-audiologsetting-destination""", alias="Destination")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologsetting.html#cfn-lex-botalias-audiologsetting-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.lex.AudioLogSetting:
        from troposphere.lex import AudioLogSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BotAliasLocaleSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettings.html
    Properties:
        - Name: CodeHookSpecification
        - Name: Enabled
    
    """
    
    CodeHookSpecification_: Optional['CodeHookSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettings.html#cfn-lex-botalias-botaliaslocalesettings-codehookspecification""", alias="CodeHookSpecification")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettings.html#cfn-lex-botalias-botaliaslocalesettings-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.lex.BotAliasLocaleSettings:
        from troposphere.lex import BotAliasLocaleSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BotAliasLocaleSettingsItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettingsitem.html
    Properties:
        - Name: LocaleId
        - Name: BotAliasLocaleSetting
    
    """
    
    LocaleId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettingsitem.html#cfn-lex-botalias-botaliaslocalesettingsitem-localeid""", alias="LocaleId")
    BotAliasLocaleSetting_: 'BotAliasLocaleSettings' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettingsitem.html#cfn-lex-botalias-botaliaslocalesettingsitem-botaliaslocalesetting""", alias="BotAliasLocaleSetting")
    


    @property
    def tropo_type(self) -> troposphere.lex.BotAliasLocaleSettingsItem:
        from troposphere.lex import BotAliasLocaleSettingsItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchLogGroupLogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-cloudwatchloggrouplogdestination.html
    Properties:
        - Name: CloudWatchLogGroupArn
        - Name: LogPrefix
    
    """
    
    CloudWatchLogGroupArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-cloudwatchloggrouplogdestination.html#cfn-lex-botalias-cloudwatchloggrouplogdestination-cloudwatchloggrouparn""", alias="CloudWatchLogGroupArn")
    LogPrefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-cloudwatchloggrouplogdestination.html#cfn-lex-botalias-cloudwatchloggrouplogdestination-logprefix""", alias="LogPrefix")
    


    @property
    def tropo_type(self) -> troposphere.lex.CloudWatchLogGroupLogDestination:
        from troposphere.lex import CloudWatchLogGroupLogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CodeHookSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-codehookspecification.html
    Properties:
        - Name: LambdaCodeHook
    
    """
    
    LambdaCodeHook_: 'LambdaCodeHook' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-codehookspecification.html#cfn-lex-botalias-codehookspecification-lambdacodehook""", alias="LambdaCodeHook")
    


    @property
    def tropo_type(self) -> troposphere.lex.CodeHookSpecification:
        from troposphere.lex import CodeHookSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConversationLogSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-conversationlogsettings.html
    Properties:
        - Name: TextLogSettings
        - Name: AudioLogSettings
    
    """
    
    TextLogSettings_: Optional[List['TextLogSetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-conversationlogsettings.html#cfn-lex-botalias-conversationlogsettings-textlogsettings""", alias="TextLogSettings")
    AudioLogSettings_: Optional[List['AudioLogSetting']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-conversationlogsettings.html#cfn-lex-botalias-conversationlogsettings-audiologsettings""", alias="AudioLogSettings")
    


    @property
    def tropo_type(self) -> troposphere.lex.ConversationLogSettings:
        from troposphere.lex import ConversationLogSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaCodeHook(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-lambdacodehook.html
    Properties:
        - Name: LambdaArn
        - Name: CodeHookInterfaceVersion
    
    """
    
    LambdaArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-lambdacodehook.html#cfn-lex-botalias-lambdacodehook-lambdaarn""", alias="LambdaArn")
    CodeHookInterfaceVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-lambdacodehook.html#cfn-lex-botalias-lambdacodehook-codehookinterfaceversion""", alias="CodeHookInterfaceVersion")
    


    @property
    def tropo_type(self) -> troposphere.lex.LambdaCodeHook:
        from troposphere.lex import LambdaCodeHook as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3BucketLogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html
    Properties:
        - Name: KmsKeyArn
        - Name: LogPrefix
        - Name: S3BucketArn
    
    """
    
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html#cfn-lex-botalias-s3bucketlogdestination-kmskeyarn""", alias="KmsKeyArn")
    LogPrefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html#cfn-lex-botalias-s3bucketlogdestination-logprefix""", alias="LogPrefix")
    S3BucketArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html#cfn-lex-botalias-s3bucketlogdestination-s3bucketarn""", alias="S3BucketArn")
    


    @property
    def tropo_type(self) -> troposphere.lex.S3BucketLogDestination:
        from troposphere.lex import S3BucketLogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SentimentAnalysisSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-sentimentanalysissettings.html
    Properties:
        - Name: DetectSentiment
    
    """
    
    DetectSentiment_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-sentimentanalysissettings.html#cfn-lex-botalias-sentimentanalysissettings-detectsentiment""", alias="DetectSentiment")
    


    @property
    def tropo_type(self) -> troposphere.lex.SentimentAnalysisSettings:
        from troposphere.lex import SentimentAnalysisSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TextLogDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogdestination.html
    Properties:
        - Name: CloudWatch
    
    """
    
    CloudWatch_: 'CloudWatchLogGroupLogDestination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogdestination.html#cfn-lex-botalias-textlogdestination-cloudwatch""", alias="CloudWatch")
    


    @property
    def tropo_type(self) -> troposphere.lex.TextLogDestination:
        from troposphere.lex import TextLogDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TextLogSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogsetting.html
    Properties:
        - Name: Destination
        - Name: Enabled
    
    """
    
    Destination_: 'TextLogDestination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogsetting.html#cfn-lex-botalias-textlogsetting-destination""", alias="Destination")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogsetting.html#cfn-lex-botalias-textlogsetting-enabled""", alias="Enabled")
    


    @property
    def tropo_type(self) -> troposphere.lex.TextLogSetting:
        from troposphere.lex import TextLogSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BotVersionLocaleDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocaledetails.html
    Properties:
        - Name: SourceBotVersion
    
    """
    
    SourceBotVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocaledetails.html#cfn-lex-botversion-botversionlocaledetails-sourcebotversion""", alias="SourceBotVersion")
    


    @property
    def tropo_type(self) -> troposphere.lex.BotVersionLocaleDetails:
        from troposphere.lex import BotVersionLocaleDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BotVersionLocaleSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocalespecification.html
    Properties:
        - Name: LocaleId
        - Name: BotVersionLocaleDetails
    
    """
    
    LocaleId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocalespecification.html#cfn-lex-botversion-botversionlocalespecification-localeid""", alias="LocaleId")
    BotVersionLocaleDetails_: 'BotVersionLocaleDetails' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocalespecification.html#cfn-lex-botversion-botversionlocalespecification-botversionlocaledetails""", alias="BotVersionLocaleDetails")
    


    @property
    def tropo_type(self) -> troposphere.lex.BotVersionLocaleSpecification:
        from troposphere.lex import BotVersionLocaleSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Bot(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html
    Properties:
        - Name: Description
        - Name: AutoBuildBotLocales
        - Name: BotLocales
        - Name: IdleSessionTTLInSeconds
        - Name: BotFileS3Location
        - Name: TestBotAliasSettings
        - Name: RoleArn
        - Name: Name
        - Name: BotTags
        - Name: TestBotAliasTags
        - Name: DataPrivacy
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-description""", alias="Description")
    AutoBuildBotLocales_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-autobuildbotlocales""", alias="AutoBuildBotLocales")
    BotLocales_: Optional[List['BotLocale']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-botlocales""", alias="BotLocales")
    IdleSessionTTLInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-idlesessionttlinseconds""", alias="IdleSessionTTLInSeconds")
    BotFileS3Location_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-botfiles3location""", alias="BotFileS3Location")
    TestBotAliasSettings_: Optional['TestBotAliasSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-testbotaliassettings""", alias="TestBotAliasSettings")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-rolearn""", alias="RoleArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-name""", alias="Name")
    BotTags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-bottags""", alias="BotTags")
    TestBotAliasTags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-testbotaliastags""", alias="TestBotAliasTags")
    DataPrivacy_: 'DataPrivacy' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-dataprivacy""", alias="DataPrivacy")
    

    @property
    def tropo_type(self) -> troposphere.lex.Bot:
        from troposphere.lex import Bot as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lex import Bot as TropoT
        return resource_to_troposphere(self, TropoT)


class BotAlias(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html
    Properties:
        - Name: BotVersion
        - Name: Description
        - Name: BotId
        - Name: BotAliasLocaleSettings
        - Name: ConversationLogSettings
        - Name: SentimentAnalysisSettings
        - Name: BotAliasName
        - Name: BotAliasTags
    Attributes:
        - Name: BotAliasStatus
        - Name: Arn
        - Name: BotAliasId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BotVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botversion""", alias="BotVersion")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-description""", alias="Description")
    BotId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botid""", alias="BotId")
    BotAliasLocaleSettings_: Optional[List['BotAliasLocaleSettingsItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botaliaslocalesettings""", alias="BotAliasLocaleSettings")
    ConversationLogSettings_: Optional['ConversationLogSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-conversationlogsettings""", alias="ConversationLogSettings")
    SentimentAnalysisSettings_: Optional['SentimentAnalysisSettings'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-sentimentanalysissettings""", alias="SentimentAnalysisSettings")
    BotAliasName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botaliasname""", alias="BotAliasName")
    BotAliasTags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botaliastags""", alias="BotAliasTags")
    

    @property
    def tropo_type(self) -> troposphere.lex.BotAlias:
        from troposphere.lex import BotAlias as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lex import BotAlias as TropoT
        return resource_to_troposphere(self, TropoT)


class BotVersion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html
    Properties:
        - Name: Description
        - Name: BotId
        - Name: BotVersionLocaleSpecification
    Attributes:
        - Name: BotVersion
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html#cfn-lex-botversion-description""", alias="Description")
    BotId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html#cfn-lex-botversion-botid""", alias="BotId")
    BotVersionLocaleSpecification_: List['BotVersionLocaleSpecification'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html#cfn-lex-botversion-botversionlocalespecification""", alias="BotVersionLocaleSpecification")
    

    @property
    def tropo_type(self) -> troposphere.lex.BotVersion:
        from troposphere.lex import BotVersion as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lex import BotVersion as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourcePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html
    Properties:
        - Name: Policy
        - Name: ResourceArn
    Attributes:
        - Name: Id
        - Name: RevisionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html#cfn-lex-resourcepolicy-policy""", alias="Policy")
    ResourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html#cfn-lex-resourcepolicy-resourcearn""", alias="ResourceArn")
    

    @property
    def tropo_type(self) -> troposphere.lex.ResourcePolicy:
        from troposphere.lex import ResourcePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lex import ResourcePolicy as TropoT
        return resource_to_troposphere(self, TropoT)

