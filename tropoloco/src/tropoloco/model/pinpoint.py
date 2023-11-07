from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CampaignHook(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html
    Properties:
        - Name: Mode
        - Name: WebUrl
        - Name: LambdaFunctionName
    
    """
    
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-mode""", alias="Mode")
    WebUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-weburl""", alias="WebUrl")
    LambdaFunctionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-lambdafunctionname""", alias="LambdaFunctionName")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.CampaignHook:
        from troposphere.pinpoint import CampaignHook as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Limits(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html
    Properties:
        - Name: Daily
        - Name: MaximumDuration
        - Name: Total
        - Name: MessagesPerSecond
    
    """
    
    Daily_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-daily""", alias="Daily")
    MaximumDuration_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-maximumduration""", alias="MaximumDuration")
    Total_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-total""", alias="Total")
    MessagesPerSecond_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-messagespersecond""", alias="MessagesPerSecond")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.Limits:
        from troposphere.pinpoint import Limits as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QuietTime(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html
    Properties:
        - Name: Start
        - Name: End
    
    """
    
    Start_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html#cfn-pinpoint-applicationsettings-quiettime-start""", alias="Start")
    End_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html#cfn-pinpoint-applicationsettings-quiettime-end""", alias="End")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.QuietTime:
        from troposphere.pinpoint import QuietTime as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AttributeDimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html
    Properties:
        - Name: AttributeType
        - Name: Values
    
    """
    
    AttributeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html#cfn-pinpoint-campaign-attributedimension-attributetype""", alias="AttributeType")
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html#cfn-pinpoint-campaign-attributedimension-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.AttributeDimension:
        from troposphere.pinpoint import AttributeDimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CampaignCustomMessage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigncustommessage.html
    Properties:
        - Name: Data
    
    """
    
    Data_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigncustommessage.html#cfn-pinpoint-campaign-campaigncustommessage-data""", alias="Data")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.CampaignCustomMessage:
        from troposphere.pinpoint import CampaignCustomMessage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CampaignEmailMessage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html
    Properties:
        - Name: FromAddress
        - Name: HtmlBody
        - Name: Title
        - Name: Body
    
    """
    
    FromAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-fromaddress""", alias="FromAddress")
    HtmlBody_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-htmlbody""", alias="HtmlBody")
    Title_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-title""", alias="Title")
    Body_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-body""", alias="Body")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.CampaignEmailMessage:
        from troposphere.pinpoint import CampaignEmailMessage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CampaignEventFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html
    Properties:
        - Name: FilterType
        - Name: Dimensions
    
    """
    
    FilterType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html#cfn-pinpoint-campaign-campaigneventfilter-filtertype""", alias="FilterType")
    Dimensions_: Optional['EventDimensions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html#cfn-pinpoint-campaign-campaigneventfilter-dimensions""", alias="Dimensions")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.CampaignEventFilter:
        from troposphere.pinpoint import CampaignEventFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CampaignHook(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html
    Properties:
        - Name: Mode
        - Name: WebUrl
        - Name: LambdaFunctionName
    
    """
    
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-mode""", alias="Mode")
    WebUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-weburl""", alias="WebUrl")
    LambdaFunctionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-lambdafunctionname""", alias="LambdaFunctionName")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.CampaignHook:
        from troposphere.pinpoint import CampaignHook as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CampaignInAppMessage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html
    Properties:
        - Name: CustomConfig
        - Name: Layout
        - Name: Content
    
    """
    
    CustomConfig_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html#cfn-pinpoint-campaign-campaigninappmessage-customconfig""", alias="CustomConfig")
    Layout_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html#cfn-pinpoint-campaign-campaigninappmessage-layout""", alias="Layout")
    Content_: Optional[List['InAppMessageContent']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html#cfn-pinpoint-campaign-campaigninappmessage-content""", alias="Content")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.CampaignInAppMessage:
        from troposphere.pinpoint import CampaignInAppMessage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CampaignSmsMessage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html
    Properties:
        - Name: EntityId
        - Name: OriginationNumber
        - Name: SenderId
        - Name: Body
        - Name: MessageType
        - Name: TemplateId
    
    """
    
    EntityId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-entityid""", alias="EntityId")
    OriginationNumber_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-originationnumber""", alias="OriginationNumber")
    SenderId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-senderid""", alias="SenderId")
    Body_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-body""", alias="Body")
    MessageType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-messagetype""", alias="MessageType")
    TemplateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-templateid""", alias="TemplateId")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.CampaignSmsMessage:
        from troposphere.pinpoint import CampaignSmsMessage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomDeliveryConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-customdeliveryconfiguration.html
    Properties:
        - Name: DeliveryUri
        - Name: EndpointTypes
    
    """
    
    DeliveryUri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-customdeliveryconfiguration.html#cfn-pinpoint-campaign-customdeliveryconfiguration-deliveryuri""", alias="DeliveryUri")
    EndpointTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-customdeliveryconfiguration.html#cfn-pinpoint-campaign-customdeliveryconfiguration-endpointtypes""", alias="EndpointTypes")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.CustomDeliveryConfiguration:
        from troposphere.pinpoint import CustomDeliveryConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefaultButtonConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html
    Properties:
        - Name: ButtonAction
        - Name: BorderRadius
        - Name: Text
        - Name: TextColor
        - Name: Link
        - Name: BackgroundColor
    
    """
    
    ButtonAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-buttonaction""", alias="ButtonAction")
    BorderRadius_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-borderradius""", alias="BorderRadius")
    Text_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-text""", alias="Text")
    TextColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-textcolor""", alias="TextColor")
    Link_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-link""", alias="Link")
    BackgroundColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-backgroundcolor""", alias="BackgroundColor")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.DefaultButtonConfiguration:
        from troposphere.pinpoint import DefaultButtonConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EventDimensions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html
    Properties:
        - Name: Metrics
        - Name: EventType
        - Name: Attributes
    
    """
    
    Metrics_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-metrics""", alias="Metrics")
    EventType_: Optional['SetDimension'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-eventtype""", alias="EventType")
    Attributes_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-attributes""", alias="Attributes")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.EventDimensions:
        from troposphere.pinpoint import EventDimensions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InAppMessageBodyConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html
    Properties:
        - Name: Alignment
        - Name: TextColor
        - Name: Body
    
    """
    
    Alignment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html#cfn-pinpoint-campaign-inappmessagebodyconfig-alignment""", alias="Alignment")
    TextColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html#cfn-pinpoint-campaign-inappmessagebodyconfig-textcolor""", alias="TextColor")
    Body_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html#cfn-pinpoint-campaign-inappmessagebodyconfig-body""", alias="Body")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.InAppMessageBodyConfig:
        from troposphere.pinpoint import InAppMessageBodyConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InAppMessageButton(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html
    Properties:
        - Name: Web
        - Name: DefaultConfig
        - Name: IOS
        - Name: Android
    
    """
    
    Web_: Optional['OverrideButtonConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-web""", alias="Web")
    DefaultConfig_: Optional['DefaultButtonConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-defaultconfig""", alias="DefaultConfig")
    IOS_: Optional['OverrideButtonConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-ios""", alias="IOS")
    Android_: Optional['OverrideButtonConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-android""", alias="Android")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.InAppMessageButton:
        from troposphere.pinpoint import InAppMessageButton as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InAppMessageContent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html
    Properties:
        - Name: BodyConfig
        - Name: SecondaryBtn
        - Name: ImageUrl
        - Name: PrimaryBtn
        - Name: HeaderConfig
        - Name: BackgroundColor
    
    """
    
    BodyConfig_: Optional['InAppMessageBodyConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-bodyconfig""", alias="BodyConfig")
    SecondaryBtn_: Optional['InAppMessageButton'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-secondarybtn""", alias="SecondaryBtn")
    ImageUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-imageurl""", alias="ImageUrl")
    PrimaryBtn_: Optional['InAppMessageButton'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-primarybtn""", alias="PrimaryBtn")
    HeaderConfig_: Optional['InAppMessageHeaderConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-headerconfig""", alias="HeaderConfig")
    BackgroundColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-backgroundcolor""", alias="BackgroundColor")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.InAppMessageContent:
        from troposphere.pinpoint import InAppMessageContent as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InAppMessageHeaderConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html
    Properties:
        - Name: Alignment
        - Name: Header
        - Name: TextColor
    
    """
    
    Alignment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html#cfn-pinpoint-campaign-inappmessageheaderconfig-alignment""", alias="Alignment")
    Header_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html#cfn-pinpoint-campaign-inappmessageheaderconfig-header""", alias="Header")
    TextColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html#cfn-pinpoint-campaign-inappmessageheaderconfig-textcolor""", alias="TextColor")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.InAppMessageHeaderConfig:
        from troposphere.pinpoint import InAppMessageHeaderConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Limits(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html
    Properties:
        - Name: Daily
        - Name: MaximumDuration
        - Name: Total
        - Name: MessagesPerSecond
        - Name: Session
    
    """
    
    Daily_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-daily""", alias="Daily")
    MaximumDuration_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-maximumduration""", alias="MaximumDuration")
    Total_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-total""", alias="Total")
    MessagesPerSecond_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-messagespersecond""", alias="MessagesPerSecond")
    Session_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-session""", alias="Session")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.Limits:
        from troposphere.pinpoint import Limits as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Message(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html
    Properties:
        - Name: JsonBody
        - Name: Action
        - Name: MediaUrl
        - Name: TimeToLive
        - Name: ImageSmallIconUrl
        - Name: ImageUrl
        - Name: Title
        - Name: ImageIconUrl
        - Name: SilentPush
        - Name: Body
        - Name: RawContent
        - Name: Url
    
    """
    
    JsonBody_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-jsonbody""", alias="JsonBody")
    Action_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-action""", alias="Action")
    MediaUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-mediaurl""", alias="MediaUrl")
    TimeToLive_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-timetolive""", alias="TimeToLive")
    ImageSmallIconUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imagesmalliconurl""", alias="ImageSmallIconUrl")
    ImageUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imageurl""", alias="ImageUrl")
    Title_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-title""", alias="Title")
    ImageIconUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imageiconurl""", alias="ImageIconUrl")
    SilentPush_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-silentpush""", alias="SilentPush")
    Body_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-body""", alias="Body")
    RawContent_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-rawcontent""", alias="RawContent")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.Message:
        from troposphere.pinpoint import Message as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MessageConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html
    Properties:
        - Name: APNSMessage
        - Name: BaiduMessage
        - Name: DefaultMessage
        - Name: InAppMessage
        - Name: EmailMessage
        - Name: GCMMessage
        - Name: SMSMessage
        - Name: CustomMessage
        - Name: ADMMessage
    
    """
    
    APNSMessage_: Optional['Message'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-apnsmessage""", alias="APNSMessage")
    BaiduMessage_: Optional['Message'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-baidumessage""", alias="BaiduMessage")
    DefaultMessage_: Optional['Message'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-defaultmessage""", alias="DefaultMessage")
    InAppMessage_: Optional['CampaignInAppMessage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-inappmessage""", alias="InAppMessage")
    EmailMessage_: Optional['CampaignEmailMessage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-emailmessage""", alias="EmailMessage")
    GCMMessage_: Optional['Message'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-gcmmessage""", alias="GCMMessage")
    SMSMessage_: Optional['CampaignSmsMessage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-smsmessage""", alias="SMSMessage")
    CustomMessage_: Optional['CampaignCustomMessage'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-custommessage""", alias="CustomMessage")
    ADMMessage_: Optional['Message'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-admmessage""", alias="ADMMessage")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.MessageConfiguration:
        from troposphere.pinpoint import MessageConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricDimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html
    Properties:
        - Name: ComparisonOperator
        - Name: Value
    
    """
    
    ComparisonOperator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html#cfn-pinpoint-campaign-metricdimension-comparisonoperator""", alias="ComparisonOperator")
    Value_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html#cfn-pinpoint-campaign-metricdimension-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.MetricDimension:
        from troposphere.pinpoint import MetricDimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OverrideButtonConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html
    Properties:
        - Name: ButtonAction
        - Name: Link
    
    """
    
    ButtonAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html#cfn-pinpoint-campaign-overridebuttonconfiguration-buttonaction""", alias="ButtonAction")
    Link_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html#cfn-pinpoint-campaign-overridebuttonconfiguration-link""", alias="Link")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.OverrideButtonConfiguration:
        from troposphere.pinpoint import OverrideButtonConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QuietTime(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html
    Properties:
        - Name: Start
        - Name: End
    
    """
    
    Start_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html#cfn-pinpoint-campaign-schedule-quiettime-start""", alias="Start")
    End_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html#cfn-pinpoint-campaign-schedule-quiettime-end""", alias="End")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.QuietTime:
        from troposphere.pinpoint import QuietTime as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Schedule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html
    Properties:
        - Name: TimeZone
        - Name: QuietTime
        - Name: EndTime
        - Name: StartTime
        - Name: Frequency
        - Name: EventFilter
        - Name: IsLocalTime
    
    """
    
    TimeZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-timezone""", alias="TimeZone")
    QuietTime_: Optional['QuietTime'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-quiettime""", alias="QuietTime")
    EndTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-endtime""", alias="EndTime")
    StartTime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-starttime""", alias="StartTime")
    Frequency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-frequency""", alias="Frequency")
    EventFilter_: Optional['CampaignEventFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-eventfilter""", alias="EventFilter")
    IsLocalTime_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-islocaltime""", alias="IsLocalTime")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.Schedule:
        from troposphere.pinpoint import Schedule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SetDimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html
    Properties:
        - Name: DimensionType
        - Name: Values
    
    """
    
    DimensionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html#cfn-pinpoint-campaign-setdimension-dimensiontype""", alias="DimensionType")
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html#cfn-pinpoint-campaign-setdimension-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.SetDimension:
        from troposphere.pinpoint import SetDimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Template(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-template.html
    Properties:
        - Name: Version
        - Name: Name
    
    """
    
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-template.html#cfn-pinpoint-campaign-template-version""", alias="Version")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-template.html#cfn-pinpoint-campaign-template-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.Template:
        from troposphere.pinpoint import Template as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TemplateConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-templateconfiguration.html
    Properties:
        - Name: SMSTemplate
        - Name: EmailTemplate
        - Name: PushTemplate
        - Name: VoiceTemplate
    
    """
    
    SMSTemplate_: Optional['Template'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-templateconfiguration.html#cfn-pinpoint-campaign-templateconfiguration-smstemplate""", alias="SMSTemplate")
    EmailTemplate_: Optional['Template'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-templateconfiguration.html#cfn-pinpoint-campaign-templateconfiguration-emailtemplate""", alias="EmailTemplate")
    PushTemplate_: Optional['Template'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-templateconfiguration.html#cfn-pinpoint-campaign-templateconfiguration-pushtemplate""", alias="PushTemplate")
    VoiceTemplate_: Optional['Template'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-templateconfiguration.html#cfn-pinpoint-campaign-templateconfiguration-voicetemplate""", alias="VoiceTemplate")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.TemplateConfiguration:
        from troposphere.pinpoint import TemplateConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WriteTreatmentResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html
    Properties:
        - Name: TreatmentDescription
        - Name: MessageConfiguration
        - Name: Schedule
        - Name: TemplateConfiguration
        - Name: CustomDeliveryConfiguration
        - Name: SizePercent
        - Name: TreatmentName
    
    """
    
    TreatmentDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-treatmentdescription""", alias="TreatmentDescription")
    MessageConfiguration_: Optional['MessageConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-messageconfiguration""", alias="MessageConfiguration")
    Schedule_: Optional['Schedule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-schedule""", alias="Schedule")
    TemplateConfiguration_: Optional['TemplateConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-templateconfiguration""", alias="TemplateConfiguration")
    CustomDeliveryConfiguration_: Optional['CustomDeliveryConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-customdeliveryconfiguration""", alias="CustomDeliveryConfiguration")
    SizePercent_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-sizepercent""", alias="SizePercent")
    TreatmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-treatmentname""", alias="TreatmentName")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.WriteTreatmentResource:
        from troposphere.pinpoint import WriteTreatmentResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BodyConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html
    Properties:
        - Name: Alignment
        - Name: TextColor
        - Name: Body
    
    """
    
    Alignment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html#cfn-pinpoint-inapptemplate-bodyconfig-alignment""", alias="Alignment")
    TextColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html#cfn-pinpoint-inapptemplate-bodyconfig-textcolor""", alias="TextColor")
    Body_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html#cfn-pinpoint-inapptemplate-bodyconfig-body""", alias="Body")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.BodyConfig:
        from troposphere.pinpoint import BodyConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ButtonConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html
    Properties:
        - Name: Web
        - Name: DefaultConfig
        - Name: IOS
        - Name: Android
    
    """
    
    Web_: Optional['OverrideButtonConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-web""", alias="Web")
    DefaultConfig_: Optional['DefaultButtonConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-defaultconfig""", alias="DefaultConfig")
    IOS_: Optional['OverrideButtonConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-ios""", alias="IOS")
    Android_: Optional['OverrideButtonConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-android""", alias="Android")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.ButtonConfig:
        from troposphere.pinpoint import ButtonConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefaultButtonConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html
    Properties:
        - Name: BorderRadius
        - Name: ButtonAction
        - Name: Text
        - Name: TextColor
        - Name: Link
        - Name: BackgroundColor
    
    """
    
    BorderRadius_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-borderradius""", alias="BorderRadius")
    ButtonAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-buttonaction""", alias="ButtonAction")
    Text_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-text""", alias="Text")
    TextColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-textcolor""", alias="TextColor")
    Link_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-link""", alias="Link")
    BackgroundColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-backgroundcolor""", alias="BackgroundColor")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.DefaultButtonConfiguration:
        from troposphere.pinpoint import DefaultButtonConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class HeaderConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html
    Properties:
        - Name: Alignment
        - Name: Header
        - Name: TextColor
    
    """
    
    Alignment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html#cfn-pinpoint-inapptemplate-headerconfig-alignment""", alias="Alignment")
    Header_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html#cfn-pinpoint-inapptemplate-headerconfig-header""", alias="Header")
    TextColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html#cfn-pinpoint-inapptemplate-headerconfig-textcolor""", alias="TextColor")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.HeaderConfig:
        from troposphere.pinpoint import HeaderConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InAppMessageContent(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html
    Properties:
        - Name: BodyConfig
        - Name: SecondaryBtn
        - Name: ImageUrl
        - Name: PrimaryBtn
        - Name: HeaderConfig
        - Name: BackgroundColor
    
    """
    
    BodyConfig_: Optional['BodyConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-bodyconfig""", alias="BodyConfig")
    SecondaryBtn_: Optional['ButtonConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-secondarybtn""", alias="SecondaryBtn")
    ImageUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-imageurl""", alias="ImageUrl")
    PrimaryBtn_: Optional['ButtonConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-primarybtn""", alias="PrimaryBtn")
    HeaderConfig_: Optional['HeaderConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-headerconfig""", alias="HeaderConfig")
    BackgroundColor_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-backgroundcolor""", alias="BackgroundColor")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.InAppMessageContent:
        from troposphere.pinpoint import InAppMessageContent as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OverrideButtonConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-overridebuttonconfiguration.html
    Properties:
        - Name: ButtonAction
        - Name: Link
    
    """
    
    ButtonAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-overridebuttonconfiguration.html#cfn-pinpoint-inapptemplate-overridebuttonconfiguration-buttonaction""", alias="ButtonAction")
    Link_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-overridebuttonconfiguration.html#cfn-pinpoint-inapptemplate-overridebuttonconfiguration-link""", alias="Link")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.OverrideButtonConfiguration:
        from troposphere.pinpoint import OverrideButtonConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class APNSPushNotificationTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html
    Properties:
        - Name: Action
        - Name: MediaUrl
        - Name: Title
        - Name: Sound
        - Name: Body
        - Name: Url
    
    """
    
    Action_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-action""", alias="Action")
    MediaUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-mediaurl""", alias="MediaUrl")
    Title_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-title""", alias="Title")
    Sound_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-sound""", alias="Sound")
    Body_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-body""", alias="Body")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.APNSPushNotificationTemplate:
        from troposphere.pinpoint import APNSPushNotificationTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AndroidPushNotificationTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html
    Properties:
        - Name: Action
        - Name: ImageUrl
        - Name: SmallImageIconUrl
        - Name: Title
        - Name: ImageIconUrl
        - Name: Sound
        - Name: Body
        - Name: Url
    
    """
    
    Action_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-action""", alias="Action")
    ImageUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-imageurl""", alias="ImageUrl")
    SmallImageIconUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-smallimageiconurl""", alias="SmallImageIconUrl")
    Title_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-title""", alias="Title")
    ImageIconUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-imageiconurl""", alias="ImageIconUrl")
    Sound_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-sound""", alias="Sound")
    Body_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-body""", alias="Body")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.AndroidPushNotificationTemplate:
        from troposphere.pinpoint import AndroidPushNotificationTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefaultPushNotificationTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html
    Properties:
        - Name: Action
        - Name: Title
        - Name: Sound
        - Name: Body
        - Name: Url
    
    """
    
    Action_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-action""", alias="Action")
    Title_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-title""", alias="Title")
    Sound_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-sound""", alias="Sound")
    Body_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-body""", alias="Body")
    Url_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-url""", alias="Url")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.DefaultPushNotificationTemplate:
        from troposphere.pinpoint import DefaultPushNotificationTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AttributeDimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html
    Properties:
        - Name: AttributeType
        - Name: Values
    
    """
    
    AttributeType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html#cfn-pinpoint-segment-attributedimension-attributetype""", alias="AttributeType")
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html#cfn-pinpoint-segment-attributedimension-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.AttributeDimension:
        from troposphere.pinpoint import AttributeDimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Behavior(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior.html
    Properties:
        - Name: Recency
    
    """
    
    Recency_: Optional['Recency'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior.html#cfn-pinpoint-segment-segmentdimensions-behavior-recency""", alias="Recency")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.Behavior:
        from troposphere.pinpoint import Behavior as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Coordinates(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html
    Properties:
        - Name: Latitude
        - Name: Longitude
    
    """
    
    Latitude_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates-latitude""", alias="Latitude")
    Longitude_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates-longitude""", alias="Longitude")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.Coordinates:
        from troposphere.pinpoint import Coordinates as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Demographic(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html
    Properties:
        - Name: AppVersion
        - Name: DeviceType
        - Name: Platform
        - Name: Channel
        - Name: Model
        - Name: Make
    
    """
    
    AppVersion_: Optional['SetDimension'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-appversion""", alias="AppVersion")
    DeviceType_: Optional['SetDimension'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-devicetype""", alias="DeviceType")
    Platform_: Optional['SetDimension'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-platform""", alias="Platform")
    Channel_: Optional['SetDimension'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-channel""", alias="Channel")
    Model_: Optional['SetDimension'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-model""", alias="Model")
    Make_: Optional['SetDimension'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-make""", alias="Make")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.Demographic:
        from troposphere.pinpoint import Demographic as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GPSPoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html
    Properties:
        - Name: RangeInKilometers
        - Name: Coordinates
    
    """
    
    RangeInKilometers_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-rangeinkilometers""", alias="RangeInKilometers")
    Coordinates_: 'Coordinates' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates""", alias="Coordinates")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.GPSPoint:
        from troposphere.pinpoint import GPSPoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Groups(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html
    Properties:
        - Name: Type
        - Name: SourceType
        - Name: Dimensions
        - Name: SourceSegments
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-type""", alias="Type")
    SourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-sourcetype""", alias="SourceType")
    Dimensions_: Optional[List['SegmentDimensions']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-dimensions""", alias="Dimensions")
    SourceSegments_: Optional[List['SourceSegments']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-sourcesegments""", alias="SourceSegments")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.Groups:
        from troposphere.pinpoint import Groups as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html
    Properties:
        - Name: GPSPoint
        - Name: Country
    
    """
    
    GPSPoint_: Optional['GPSPoint'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint""", alias="GPSPoint")
    Country_: Optional['SetDimension'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html#cfn-pinpoint-segment-segmentdimensions-location-country""", alias="Country")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.Location:
        from troposphere.pinpoint import Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Recency(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html
    Properties:
        - Name: Duration
        - Name: RecencyType
    
    """
    
    Duration_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html#cfn-pinpoint-segment-segmentdimensions-behavior-recency-duration""", alias="Duration")
    RecencyType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html#cfn-pinpoint-segment-segmentdimensions-behavior-recency-recencytype""", alias="RecencyType")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.Recency:
        from troposphere.pinpoint import Recency as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SegmentDimensions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html
    Properties:
        - Name: Demographic
        - Name: Metrics
        - Name: Attributes
        - Name: Behavior
        - Name: UserAttributes
        - Name: Location
    
    """
    
    Demographic_: Optional['Demographic'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-demographic""", alias="Demographic")
    Metrics_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-metrics""", alias="Metrics")
    Attributes_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-attributes""", alias="Attributes")
    Behavior_: Optional['Behavior'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-behavior""", alias="Behavior")
    UserAttributes_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-userattributes""", alias="UserAttributes")
    Location_: Optional['Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-location""", alias="Location")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.SegmentDimensions:
        from troposphere.pinpoint import SegmentDimensions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SegmentGroups(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html
    Properties:
        - Name: Groups
        - Name: Include
    
    """
    
    Groups_: Optional[List['Groups']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html#cfn-pinpoint-segment-segmentgroups-groups""", alias="Groups")
    Include_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html#cfn-pinpoint-segment-segmentgroups-include""", alias="Include")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.SegmentGroups:
        from troposphere.pinpoint import SegmentGroups as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SetDimension(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html
    Properties:
        - Name: DimensionType
        - Name: Values
    
    """
    
    DimensionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html#cfn-pinpoint-segment-setdimension-dimensiontype""", alias="DimensionType")
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html#cfn-pinpoint-segment-setdimension-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.SetDimension:
        from troposphere.pinpoint import SetDimension as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceSegments(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html
    Properties:
        - Name: Version
        - Name: Id
    
    """
    
    Version_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html#cfn-pinpoint-segment-segmentgroups-groups-sourcesegments-version""", alias="Version")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html#cfn-pinpoint-segment-segmentgroups-groups-sourcesegments-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.pinpoint.SourceSegments:
        from troposphere.pinpoint import SourceSegments as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ADMChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html
    Properties:
        - Name: ClientSecret
        - Name: Enabled
        - Name: ClientId
        - Name: ApplicationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ClientSecret_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-clientsecret""", alias="ClientSecret")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-enabled""", alias="Enabled")
    ClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-clientid""", alias="ClientId")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-applicationid""", alias="ApplicationId")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.ADMChannel:
        from troposphere.pinpoint import ADMChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import ADMChannel as TropoT
        return resource_to_troposphere(self, TropoT)


class APNSChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html
    Properties:
        - Name: BundleId
        - Name: PrivateKey
        - Name: Enabled
        - Name: DefaultAuthenticationMethod
        - Name: TokenKey
        - Name: ApplicationId
        - Name: TeamId
        - Name: Certificate
        - Name: TokenKeyId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BundleId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-bundleid""", alias="BundleId")
    PrivateKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-privatekey""", alias="PrivateKey")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-enabled""", alias="Enabled")
    DefaultAuthenticationMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-defaultauthenticationmethod""", alias="DefaultAuthenticationMethod")
    TokenKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-tokenkey""", alias="TokenKey")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-applicationid""", alias="ApplicationId")
    TeamId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-teamid""", alias="TeamId")
    Certificate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-certificate""", alias="Certificate")
    TokenKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-tokenkeyid""", alias="TokenKeyId")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.APNSChannel:
        from troposphere.pinpoint import APNSChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import APNSChannel as TropoT
        return resource_to_troposphere(self, TropoT)


class APNSSandboxChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html
    Properties:
        - Name: BundleId
        - Name: PrivateKey
        - Name: Enabled
        - Name: DefaultAuthenticationMethod
        - Name: TokenKey
        - Name: ApplicationId
        - Name: TeamId
        - Name: Certificate
        - Name: TokenKeyId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BundleId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-bundleid""", alias="BundleId")
    PrivateKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-privatekey""", alias="PrivateKey")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-enabled""", alias="Enabled")
    DefaultAuthenticationMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-defaultauthenticationmethod""", alias="DefaultAuthenticationMethod")
    TokenKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-tokenkey""", alias="TokenKey")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-applicationid""", alias="ApplicationId")
    TeamId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-teamid""", alias="TeamId")
    Certificate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-certificate""", alias="Certificate")
    TokenKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-tokenkeyid""", alias="TokenKeyId")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.APNSSandboxChannel:
        from troposphere.pinpoint import APNSSandboxChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import APNSSandboxChannel as TropoT
        return resource_to_troposphere(self, TropoT)


class APNSVoipChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html
    Properties:
        - Name: BundleId
        - Name: PrivateKey
        - Name: Enabled
        - Name: DefaultAuthenticationMethod
        - Name: TokenKey
        - Name: ApplicationId
        - Name: TeamId
        - Name: Certificate
        - Name: TokenKeyId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BundleId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-bundleid""", alias="BundleId")
    PrivateKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-privatekey""", alias="PrivateKey")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-enabled""", alias="Enabled")
    DefaultAuthenticationMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-defaultauthenticationmethod""", alias="DefaultAuthenticationMethod")
    TokenKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-tokenkey""", alias="TokenKey")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-applicationid""", alias="ApplicationId")
    TeamId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-teamid""", alias="TeamId")
    Certificate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-certificate""", alias="Certificate")
    TokenKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-tokenkeyid""", alias="TokenKeyId")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.APNSVoipChannel:
        from troposphere.pinpoint import APNSVoipChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import APNSVoipChannel as TropoT
        return resource_to_troposphere(self, TropoT)


class APNSVoipSandboxChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html
    Properties:
        - Name: BundleId
        - Name: PrivateKey
        - Name: Enabled
        - Name: DefaultAuthenticationMethod
        - Name: TokenKey
        - Name: ApplicationId
        - Name: TeamId
        - Name: Certificate
        - Name: TokenKeyId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BundleId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-bundleid""", alias="BundleId")
    PrivateKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-privatekey""", alias="PrivateKey")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-enabled""", alias="Enabled")
    DefaultAuthenticationMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-defaultauthenticationmethod""", alias="DefaultAuthenticationMethod")
    TokenKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-tokenkey""", alias="TokenKey")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-applicationid""", alias="ApplicationId")
    TeamId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-teamid""", alias="TeamId")
    Certificate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-certificate""", alias="Certificate")
    TokenKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-tokenkeyid""", alias="TokenKeyId")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.APNSVoipSandboxChannel:
        from troposphere.pinpoint import APNSVoipSandboxChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import APNSVoipSandboxChannel as TropoT
        return resource_to_troposphere(self, TropoT)


class App(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html
    Properties:
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html#cfn-pinpoint-app-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html#cfn-pinpoint-app-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.App:
        from troposphere.pinpoint import App as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import App as TropoT
        return resource_to_troposphere(self, TropoT)


class ApplicationSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html
    Properties:
        - Name: QuietTime
        - Name: Limits
        - Name: ApplicationId
        - Name: CampaignHook
        - Name: CloudWatchMetricsEnabled
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    QuietTime_: Optional['QuietTime'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-quiettime""", alias="QuietTime")
    Limits_: Optional['Limits'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-limits""", alias="Limits")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-applicationid""", alias="ApplicationId")
    CampaignHook_: Optional['CampaignHook'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-campaignhook""", alias="CampaignHook")
    CloudWatchMetricsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-cloudwatchmetricsenabled""", alias="CloudWatchMetricsEnabled")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.ApplicationSettings:
        from troposphere.pinpoint import ApplicationSettings as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import ApplicationSettings as TropoT
        return resource_to_troposphere(self, TropoT)


class BaiduChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html
    Properties:
        - Name: SecretKey
        - Name: ApiKey
        - Name: Enabled
        - Name: ApplicationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SecretKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-secretkey""", alias="SecretKey")
    ApiKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-apikey""", alias="ApiKey")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-enabled""", alias="Enabled")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-applicationid""", alias="ApplicationId")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.BaiduChannel:
        from troposphere.pinpoint import BaiduChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import BaiduChannel as TropoT
        return resource_to_troposphere(self, TropoT)


class Campaign(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html
    Properties:
        - Name: Description
        - Name: SegmentId
        - Name: Priority
        - Name: TemplateConfiguration
        - Name: IsPaused
        - Name: AdditionalTreatments
        - Name: Name
        - Name: SegmentVersion
        - Name: TreatmentDescription
        - Name: MessageConfiguration
        - Name: Limits
        - Name: HoldoutPercent
        - Name: Schedule
        - Name: CustomDeliveryConfiguration
        - Name: ApplicationId
        - Name: CampaignHook
        - Name: Tags
        - Name: TreatmentName
    Attributes:
        - Name: CampaignId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-description""", alias="Description")
    SegmentId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-segmentid""", alias="SegmentId")
    Priority_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-priority""", alias="Priority")
    TemplateConfiguration_: Optional['TemplateConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-templateconfiguration""", alias="TemplateConfiguration")
    IsPaused_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-ispaused""", alias="IsPaused")
    AdditionalTreatments_: Optional[List['WriteTreatmentResource']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-additionaltreatments""", alias="AdditionalTreatments")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-name""", alias="Name")
    SegmentVersion_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-segmentversion""", alias="SegmentVersion")
    TreatmentDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-treatmentdescription""", alias="TreatmentDescription")
    MessageConfiguration_: Optional['MessageConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-messageconfiguration""", alias="MessageConfiguration")
    Limits_: Optional['Limits'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-limits""", alias="Limits")
    HoldoutPercent_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-holdoutpercent""", alias="HoldoutPercent")
    Schedule_: 'Schedule' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-schedule""", alias="Schedule")
    CustomDeliveryConfiguration_: Optional['CustomDeliveryConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-customdeliveryconfiguration""", alias="CustomDeliveryConfiguration")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-applicationid""", alias="ApplicationId")
    CampaignHook_: Optional['CampaignHook'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-campaignhook""", alias="CampaignHook")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-tags""", alias="Tags")
    TreatmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-treatmentname""", alias="TreatmentName")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.Campaign:
        from troposphere.pinpoint import Campaign as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import Campaign as TropoT
        return resource_to_troposphere(self, TropoT)


class EmailChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html
    Properties:
        - Name: ConfigurationSet
        - Name: FromAddress
        - Name: Enabled
        - Name: ApplicationId
        - Name: Identity
        - Name: RoleArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConfigurationSet_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-configurationset""", alias="ConfigurationSet")
    FromAddress_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-fromaddress""", alias="FromAddress")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-enabled""", alias="Enabled")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-applicationid""", alias="ApplicationId")
    Identity_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-identity""", alias="Identity")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-rolearn""", alias="RoleArn")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.EmailChannel:
        from troposphere.pinpoint import EmailChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import EmailChannel as TropoT
        return resource_to_troposphere(self, TropoT)


class EmailTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html
    Properties:
        - Name: HtmlPart
        - Name: TextPart
        - Name: TemplateName
        - Name: TemplateDescription
        - Name: DefaultSubstitutions
        - Name: Subject
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    HtmlPart_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-htmlpart""", alias="HtmlPart")
    TextPart_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-textpart""", alias="TextPart")
    TemplateName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-templatename""", alias="TemplateName")
    TemplateDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-templatedescription""", alias="TemplateDescription")
    DefaultSubstitutions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-defaultsubstitutions""", alias="DefaultSubstitutions")
    Subject_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-subject""", alias="Subject")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.EmailTemplate:
        from troposphere.pinpoint import EmailTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import EmailTemplate as TropoT
        return resource_to_troposphere(self, TropoT)


class EventStream(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html
    Properties:
        - Name: ApplicationId
        - Name: DestinationStreamArn
        - Name: RoleArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-applicationid""", alias="ApplicationId")
    DestinationStreamArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-destinationstreamarn""", alias="DestinationStreamArn")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-rolearn""", alias="RoleArn")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.EventStream:
        from troposphere.pinpoint import EventStream as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import EventStream as TropoT
        return resource_to_troposphere(self, TropoT)


class GCMChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html
    Properties:
        - Name: ApiKey
        - Name: Enabled
        - Name: ApplicationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApiKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-apikey""", alias="ApiKey")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-enabled""", alias="Enabled")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-applicationid""", alias="ApplicationId")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.GCMChannel:
        from troposphere.pinpoint import GCMChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import GCMChannel as TropoT
        return resource_to_troposphere(self, TropoT)


class InAppTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html
    Properties:
        - Name: CustomConfig
        - Name: Layout
        - Name: Content
        - Name: TemplateName
        - Name: TemplateDescription
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CustomConfig_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-customconfig""", alias="CustomConfig")
    Layout_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-layout""", alias="Layout")
    Content_: Optional[List['InAppMessageContent']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-content""", alias="Content")
    TemplateName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-templatename""", alias="TemplateName")
    TemplateDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-templatedescription""", alias="TemplateDescription")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.InAppTemplate:
        from troposphere.pinpoint import InAppTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import InAppTemplate as TropoT
        return resource_to_troposphere(self, TropoT)


class PushTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html
    Properties:
        - Name: GCM
        - Name: Baidu
        - Name: TemplateName
        - Name: ADM
        - Name: APNS
        - Name: TemplateDescription
        - Name: DefaultSubstitutions
        - Name: Default
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    GCM_: Optional['AndroidPushNotificationTemplate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-gcm""", alias="GCM")
    Baidu_: Optional['AndroidPushNotificationTemplate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-baidu""", alias="Baidu")
    TemplateName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-templatename""", alias="TemplateName")
    ADM_: Optional['AndroidPushNotificationTemplate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-adm""", alias="ADM")
    APNS_: Optional['APNSPushNotificationTemplate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-apns""", alias="APNS")
    TemplateDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-templatedescription""", alias="TemplateDescription")
    DefaultSubstitutions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-defaultsubstitutions""", alias="DefaultSubstitutions")
    Default_: Optional['DefaultPushNotificationTemplate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-default""", alias="Default")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.PushTemplate:
        from troposphere.pinpoint import PushTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import PushTemplate as TropoT
        return resource_to_troposphere(self, TropoT)


class SMSChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html
    Properties:
        - Name: ShortCode
        - Name: Enabled
        - Name: ApplicationId
        - Name: SenderId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ShortCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-shortcode""", alias="ShortCode")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-enabled""", alias="Enabled")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-applicationid""", alias="ApplicationId")
    SenderId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-senderid""", alias="SenderId")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.SMSChannel:
        from troposphere.pinpoint import SMSChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import SMSChannel as TropoT
        return resource_to_troposphere(self, TropoT)


class Segment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html
    Properties:
        - Name: SegmentGroups
        - Name: Dimensions
        - Name: ApplicationId
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: SegmentId
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SegmentGroups_: Optional['SegmentGroups'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-segmentgroups""", alias="SegmentGroups")
    Dimensions_: Optional['SegmentDimensions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-dimensions""", alias="Dimensions")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-applicationid""", alias="ApplicationId")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.Segment:
        from troposphere.pinpoint import Segment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import Segment as TropoT
        return resource_to_troposphere(self, TropoT)


class SmsTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html
    Properties:
        - Name: TemplateName
        - Name: TemplateDescription
        - Name: DefaultSubstitutions
        - Name: Body
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TemplateName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-templatename""", alias="TemplateName")
    TemplateDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-templatedescription""", alias="TemplateDescription")
    DefaultSubstitutions_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-defaultsubstitutions""", alias="DefaultSubstitutions")
    Body_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-body""", alias="Body")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.SmsTemplate:
        from troposphere.pinpoint import SmsTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import SmsTemplate as TropoT
        return resource_to_troposphere(self, TropoT)


class VoiceChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html
    Properties:
        - Name: Enabled
        - Name: ApplicationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Enabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html#cfn-pinpoint-voicechannel-enabled""", alias="Enabled")
    ApplicationId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html#cfn-pinpoint-voicechannel-applicationid""", alias="ApplicationId")
    

    @property
    def tropo_type(self) -> troposphere.pinpoint.VoiceChannel:
        from troposphere.pinpoint import VoiceChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pinpoint import VoiceChannel as TropoT
        return resource_to_troposphere(self, TropoT)

