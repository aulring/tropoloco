from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class RegionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-regionconfiguration.html
    Properties:
        - Name: SseKmsKeyId
    
    """
    
    SseKmsKeyId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-regionconfiguration.html#cfn-ssmincidents-replicationset-regionconfiguration-ssekmskeyid""", alias="SseKmsKeyId")
    


    @property
    def tropo_type(self) -> troposphere.ssmincidents.RegionConfiguration:
        from troposphere.ssmincidents import RegionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationRegion(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-replicationregion.html
    Properties:
        - Name: RegionConfiguration
        - Name: RegionName
    
    """
    
    RegionConfiguration_: Optional['RegionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-replicationregion.html#cfn-ssmincidents-replicationset-replicationregion-regionconfiguration""", alias="RegionConfiguration")
    RegionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-replicationregion.html#cfn-ssmincidents-replicationset-replicationregion-regionname""", alias="RegionName")
    


    @property
    def tropo_type(self) -> troposphere.ssmincidents.ReplicationRegion:
        from troposphere.ssmincidents import ReplicationRegion as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Action(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-action.html
    Properties:
        - Name: SsmAutomation
    
    """
    
    SsmAutomation_: Optional['SsmAutomation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-action.html#cfn-ssmincidents-responseplan-action-ssmautomation""", alias="SsmAutomation")
    


    @property
    def tropo_type(self) -> troposphere.ssmincidents.Action:
        from troposphere.ssmincidents import Action as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ChatChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-chatchannel.html
    Properties:
        - Name: ChatbotSns
    
    """
    
    ChatbotSns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-chatchannel.html#cfn-ssmincidents-responseplan-chatchannel-chatbotsns""", alias="ChatbotSns")
    


    @property
    def tropo_type(self) -> troposphere.ssmincidents.ChatChannel:
        from troposphere.ssmincidents import ChatChannel as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynamicSsmParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparameter.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: 'DynamicSsmParameterValue' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparameter.html#cfn-ssmincidents-responseplan-dynamicssmparameter-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparameter.html#cfn-ssmincidents-responseplan-dynamicssmparameter-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.ssmincidents.DynamicSsmParameter:
        from troposphere.ssmincidents import DynamicSsmParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DynamicSsmParameterValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparametervalue.html
    Properties:
        - Name: Variable
    
    """
    
    Variable_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparametervalue.html#cfn-ssmincidents-responseplan-dynamicssmparametervalue-variable""", alias="Variable")
    


    @property
    def tropo_type(self) -> troposphere.ssmincidents.DynamicSsmParameterValue:
        from troposphere.ssmincidents import DynamicSsmParameterValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IncidentTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html
    Properties:
        - Name: Impact
        - Name: IncidentTags
        - Name: Summary
        - Name: Title
        - Name: NotificationTargets
        - Name: DedupeString
    
    """
    
    Impact_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-impact""", alias="Impact")
    IncidentTags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-incidenttags""", alias="IncidentTags")
    Summary_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-summary""", alias="Summary")
    Title_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-title""", alias="Title")
    NotificationTargets_: Optional[List['NotificationTargetItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-notificationtargets""", alias="NotificationTargets")
    DedupeString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-dedupestring""", alias="DedupeString")
    


    @property
    def tropo_type(self) -> troposphere.ssmincidents.IncidentTemplate:
        from troposphere.ssmincidents import IncidentTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Integration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-integration.html
    Properties:
        - Name: PagerDutyConfiguration
    
    """
    
    PagerDutyConfiguration_: 'PagerDutyConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-integration.html#cfn-ssmincidents-responseplan-integration-pagerdutyconfiguration""", alias="PagerDutyConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.ssmincidents.Integration:
        from troposphere.ssmincidents import Integration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationTargetItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-notificationtargetitem.html
    Properties:
        - Name: SnsTopicArn
    
    """
    
    SnsTopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-notificationtargetitem.html#cfn-ssmincidents-responseplan-notificationtargetitem-snstopicarn""", alias="SnsTopicArn")
    


    @property
    def tropo_type(self) -> troposphere.ssmincidents.NotificationTargetItem:
        from troposphere.ssmincidents import NotificationTargetItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PagerDutyConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-pagerdutyconfiguration.html
    Properties:
        - Name: SecretId
        - Name: PagerDutyIncidentConfiguration
        - Name: Name
    
    """
    
    SecretId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-pagerdutyconfiguration.html#cfn-ssmincidents-responseplan-pagerdutyconfiguration-secretid""", alias="SecretId")
    PagerDutyIncidentConfiguration_: 'PagerDutyIncidentConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-pagerdutyconfiguration.html#cfn-ssmincidents-responseplan-pagerdutyconfiguration-pagerdutyincidentconfiguration""", alias="PagerDutyIncidentConfiguration")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-pagerdutyconfiguration.html#cfn-ssmincidents-responseplan-pagerdutyconfiguration-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ssmincidents.PagerDutyConfiguration:
        from troposphere.ssmincidents import PagerDutyConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PagerDutyIncidentConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-pagerdutyincidentconfiguration.html
    Properties:
        - Name: ServiceId
    
    """
    
    ServiceId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-pagerdutyincidentconfiguration.html#cfn-ssmincidents-responseplan-pagerdutyincidentconfiguration-serviceid""", alias="ServiceId")
    


    @property
    def tropo_type(self) -> troposphere.ssmincidents.PagerDutyIncidentConfiguration:
        from troposphere.ssmincidents import PagerDutyIncidentConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SsmAutomation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html
    Properties:
        - Name: Parameters
        - Name: TargetAccount
        - Name: DynamicParameters
        - Name: DocumentVersion
        - Name: RoleArn
        - Name: DocumentName
    
    """
    
    Parameters_: Optional[List['SsmParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-parameters""", alias="Parameters")
    TargetAccount_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-targetaccount""", alias="TargetAccount")
    DynamicParameters_: Optional[List['DynamicSsmParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-dynamicparameters""", alias="DynamicParameters")
    DocumentVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-documentversion""", alias="DocumentVersion")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-rolearn""", alias="RoleArn")
    DocumentName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-documentname""", alias="DocumentName")
    


    @property
    def tropo_type(self) -> troposphere.ssmincidents.SsmAutomation:
        from troposphere.ssmincidents import SsmAutomation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SsmParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmparameter.html
    Properties:
        - Name: Values
        - Name: Key
    
    """
    
    Values_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmparameter.html#cfn-ssmincidents-responseplan-ssmparameter-values""", alias="Values")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmparameter.html#cfn-ssmincidents-responseplan-ssmparameter-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.ssmincidents.SsmParameter:
        from troposphere.ssmincidents import SsmParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ReplicationSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html
    Properties:
        - Name: Regions
        - Name: DeletionProtected
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Regions_: List['ReplicationRegion'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-regions""", alias="Regions")
    DeletionProtected_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-deletionprotected""", alias="DeletionProtected")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ssmincidents.ReplicationSet:
        from troposphere.ssmincidents import ReplicationSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssmincidents import ReplicationSet as TropoT
        return resource_to_troposphere(self, TropoT)


class ResponsePlan(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html
    Properties:
        - Name: ChatChannel
        - Name: Integrations
        - Name: Actions
        - Name: DisplayName
        - Name: IncidentTemplate
        - Name: Engagements
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ChatChannel_: Optional['ChatChannel'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-chatchannel""", alias="ChatChannel")
    Integrations_: Optional[List['Integration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-integrations""", alias="Integrations")
    Actions_: Optional[List['Action']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-actions""", alias="Actions")
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-displayname""", alias="DisplayName")
    IncidentTemplate_: 'IncidentTemplate' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-incidenttemplate""", alias="IncidentTemplate")
    Engagements_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-engagements""", alias="Engagements")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ssmincidents.ResponsePlan:
        from troposphere.ssmincidents import ResponsePlan as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssmincidents import ResponsePlan as TropoT
        return resource_to_troposphere(self, TropoT)

