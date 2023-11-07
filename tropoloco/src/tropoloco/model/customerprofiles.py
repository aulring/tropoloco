from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AttributeDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributedetails.html
    Properties:
        - Name: Expression
        - Name: Attributes
    
    """
    
    Expression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributedetails.html#cfn-customerprofiles-calculatedattributedefinition-attributedetails-expression""", alias="Expression")
    Attributes_: List['AttributeItem'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributedetails.html#cfn-customerprofiles-calculatedattributedefinition-attributedetails-attributes""", alias="Attributes")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.AttributeDetails:
        from troposphere.customerprofiles import AttributeDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AttributeItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributeitem.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributeitem.html#cfn-customerprofiles-calculatedattributedefinition-attributeitem-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.AttributeItem:
        from troposphere.customerprofiles import AttributeItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Conditions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-conditions.html
    Properties:
        - Name: Range
        - Name: ObjectCount
        - Name: Threshold
    
    """
    
    Range_: Optional['Range'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-conditions.html#cfn-customerprofiles-calculatedattributedefinition-conditions-range""", alias="Range")
    ObjectCount_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-conditions.html#cfn-customerprofiles-calculatedattributedefinition-conditions-objectcount""", alias="ObjectCount")
    Threshold_: Optional['Threshold'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-conditions.html#cfn-customerprofiles-calculatedattributedefinition-conditions-threshold""", alias="Threshold")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.Conditions:
        from troposphere.customerprofiles import Conditions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Range(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-range.html
    Properties:
        - Name: Value
        - Name: Unit
    
    """
    
    Value_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-range.html#cfn-customerprofiles-calculatedattributedefinition-range-value""", alias="Value")
    Unit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-range.html#cfn-customerprofiles-calculatedattributedefinition-range-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.Range:
        from troposphere.customerprofiles import Range as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Threshold(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-threshold.html
    Properties:
        - Name: Operator
        - Name: Value
    
    """
    
    Operator_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-threshold.html#cfn-customerprofiles-calculatedattributedefinition-threshold-operator""", alias="Operator")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-threshold.html#cfn-customerprofiles-calculatedattributedefinition-threshold-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.Threshold:
        from troposphere.customerprofiles import Threshold as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AttributeTypesSelector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-attributetypesselector.html
    Properties:
        - Name: Address
        - Name: AttributeMatchingModel
        - Name: PhoneNumber
        - Name: EmailAddress
    
    """
    
    Address_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-attributetypesselector.html#cfn-customerprofiles-domain-attributetypesselector-address""", alias="Address")
    AttributeMatchingModel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-attributetypesselector.html#cfn-customerprofiles-domain-attributetypesselector-attributematchingmodel""", alias="AttributeMatchingModel")
    PhoneNumber_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-attributetypesselector.html#cfn-customerprofiles-domain-attributetypesselector-phonenumber""", alias="PhoneNumber")
    EmailAddress_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-attributetypesselector.html#cfn-customerprofiles-domain-attributetypesselector-emailaddress""", alias="EmailAddress")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.AttributeTypesSelector:
        from troposphere.customerprofiles import AttributeTypesSelector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutoMerging(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-automerging.html
    Properties:
        - Name: Consolidation
        - Name: Enabled
        - Name: ConflictResolution
        - Name: MinAllowedConfidenceScoreForMerging
    
    """
    
    Consolidation_: Optional['Consolidation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-automerging.html#cfn-customerprofiles-domain-automerging-consolidation""", alias="Consolidation")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-automerging.html#cfn-customerprofiles-domain-automerging-enabled""", alias="Enabled")
    ConflictResolution_: Optional['ConflictResolution'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-automerging.html#cfn-customerprofiles-domain-automerging-conflictresolution""", alias="ConflictResolution")
    MinAllowedConfidenceScoreForMerging_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-automerging.html#cfn-customerprofiles-domain-automerging-minallowedconfidencescoreformerging""", alias="MinAllowedConfidenceScoreForMerging")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.AutoMerging:
        from troposphere.customerprofiles import AutoMerging as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConflictResolution(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-conflictresolution.html
    Properties:
        - Name: ConflictResolvingModel
        - Name: SourceName
    
    """
    
    ConflictResolvingModel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-conflictresolution.html#cfn-customerprofiles-domain-conflictresolution-conflictresolvingmodel""", alias="ConflictResolvingModel")
    SourceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-conflictresolution.html#cfn-customerprofiles-domain-conflictresolution-sourcename""", alias="SourceName")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.ConflictResolution:
        from troposphere.customerprofiles import ConflictResolution as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Consolidation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-consolidation.html
    Properties:
        - Name: MatchingAttributesList
    
    """
    
    MatchingAttributesList_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-consolidation.html#cfn-customerprofiles-domain-consolidation-matchingattributeslist""", alias="MatchingAttributesList")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.Consolidation:
        from troposphere.customerprofiles import Consolidation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DomainStats(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-domainstats.html
    Properties:
        - Name: MeteringProfileCount
        - Name: ProfileCount
        - Name: ObjectCount
        - Name: TotalSize
    
    """
    
    MeteringProfileCount_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-domainstats.html#cfn-customerprofiles-domain-domainstats-meteringprofilecount""", alias="MeteringProfileCount")
    ProfileCount_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-domainstats.html#cfn-customerprofiles-domain-domainstats-profilecount""", alias="ProfileCount")
    ObjectCount_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-domainstats.html#cfn-customerprofiles-domain-domainstats-objectcount""", alias="ObjectCount")
    TotalSize_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-domainstats.html#cfn-customerprofiles-domain-domainstats-totalsize""", alias="TotalSize")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.DomainStats:
        from troposphere.customerprofiles import DomainStats as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExportingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-exportingconfig.html
    Properties:
        - Name: S3Exporting
    
    """
    
    S3Exporting_: Optional['S3ExportingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-exportingconfig.html#cfn-customerprofiles-domain-exportingconfig-s3exporting""", alias="S3Exporting")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.ExportingConfig:
        from troposphere.customerprofiles import ExportingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class JobSchedule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-jobschedule.html
    Properties:
        - Name: DayOfTheWeek
        - Name: Time
    
    """
    
    DayOfTheWeek_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-jobschedule.html#cfn-customerprofiles-domain-jobschedule-dayoftheweek""", alias="DayOfTheWeek")
    Time_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-jobschedule.html#cfn-customerprofiles-domain-jobschedule-time""", alias="Time")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.JobSchedule:
        from troposphere.customerprofiles import JobSchedule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Matching(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matching.html
    Properties:
        - Name: AutoMerging
        - Name: JobSchedule
        - Name: Enabled
        - Name: ExportingConfig
    
    """
    
    AutoMerging_: Optional['AutoMerging'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matching.html#cfn-customerprofiles-domain-matching-automerging""", alias="AutoMerging")
    JobSchedule_: Optional['JobSchedule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matching.html#cfn-customerprofiles-domain-matching-jobschedule""", alias="JobSchedule")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matching.html#cfn-customerprofiles-domain-matching-enabled""", alias="Enabled")
    ExportingConfig_: Optional['ExportingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matching.html#cfn-customerprofiles-domain-matching-exportingconfig""", alias="ExportingConfig")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.Matching:
        from troposphere.customerprofiles import Matching as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MatchingRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matchingrule.html
    Properties:
        - Name: Rule
    
    """
    
    Rule_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matchingrule.html#cfn-customerprofiles-domain-matchingrule-rule""", alias="Rule")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.MatchingRule:
        from troposphere.customerprofiles import MatchingRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleBasedMatching(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html
    Properties:
        - Name: Status
        - Name: MaxAllowedRuleLevelForMerging
        - Name: Enabled
        - Name: MatchingRules
        - Name: AttributeTypesSelector
        - Name: ConflictResolution
        - Name: ExportingConfig
        - Name: MaxAllowedRuleLevelForMatching
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-status""", alias="Status")
    MaxAllowedRuleLevelForMerging_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-maxallowedrulelevelformerging""", alias="MaxAllowedRuleLevelForMerging")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-enabled""", alias="Enabled")
    MatchingRules_: Optional[List['MatchingRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-matchingrules""", alias="MatchingRules")
    AttributeTypesSelector_: Optional['AttributeTypesSelector'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-attributetypesselector""", alias="AttributeTypesSelector")
    ConflictResolution_: Optional['ConflictResolution'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-conflictresolution""", alias="ConflictResolution")
    ExportingConfig_: Optional['ExportingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-exportingconfig""", alias="ExportingConfig")
    MaxAllowedRuleLevelForMatching_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-maxallowedrulelevelformatching""", alias="MaxAllowedRuleLevelForMatching")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.RuleBasedMatching:
        from troposphere.customerprofiles import RuleBasedMatching as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3ExportingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-s3exportingconfig.html
    Properties:
        - Name: S3BucketName
        - Name: S3KeyName
    
    """
    
    S3BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-s3exportingconfig.html#cfn-customerprofiles-domain-s3exportingconfig-s3bucketname""", alias="S3BucketName")
    S3KeyName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-s3exportingconfig.html#cfn-customerprofiles-domain-s3exportingconfig-s3keyname""", alias="S3KeyName")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.S3ExportingConfig:
        from troposphere.customerprofiles import S3ExportingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DestinationDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventstream-destinationdetails.html
    Properties:
        - Name: Status
        - Name: Uri
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventstream-destinationdetails.html#cfn-customerprofiles-eventstream-destinationdetails-status""", alias="Status")
    Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventstream-destinationdetails.html#cfn-customerprofiles-eventstream-destinationdetails-uri""", alias="Uri")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.DestinationDetails:
        from troposphere.customerprofiles import DestinationDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConnectorOperator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html
    Properties:
        - Name: S3
        - Name: ServiceNow
        - Name: Zendesk
        - Name: Marketo
        - Name: Salesforce
    
    """
    
    S3_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-s3""", alias="S3")
    ServiceNow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-servicenow""", alias="ServiceNow")
    Zendesk_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-zendesk""", alias="Zendesk")
    Marketo_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-marketo""", alias="Marketo")
    Salesforce_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-salesforce""", alias="Salesforce")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.ConnectorOperator:
        from troposphere.customerprofiles import ConnectorOperator as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FlowDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html
    Properties:
        - Name: Description
        - Name: Tasks
        - Name: FlowName
        - Name: TriggerConfig
        - Name: SourceFlowConfig
        - Name: KmsArn
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-description""", alias="Description")
    Tasks_: List['Task'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-tasks""", alias="Tasks")
    FlowName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-flowname""", alias="FlowName")
    TriggerConfig_: 'TriggerConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-triggerconfig""", alias="TriggerConfig")
    SourceFlowConfig_: 'SourceFlowConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-sourceflowconfig""", alias="SourceFlowConfig")
    KmsArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-kmsarn""", alias="KmsArn")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.FlowDefinition:
        from troposphere.customerprofiles import FlowDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IncrementalPullConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html
    Properties:
        - Name: DatetimeTypeFieldName
    
    """
    
    DatetimeTypeFieldName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html#cfn-customerprofiles-integration-incrementalpullconfig-datetimetypefieldname""", alias="DatetimeTypeFieldName")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.IncrementalPullConfig:
        from troposphere.customerprofiles import IncrementalPullConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MarketoSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html#cfn-customerprofiles-integration-marketosourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.MarketoSourceProperties:
        from troposphere.customerprofiles import MarketoSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ObjectTypeMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-objecttypemapping.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-objecttypemapping.html#cfn-customerprofiles-integration-objecttypemapping-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-objecttypemapping.html#cfn-customerprofiles-integration-objecttypemapping-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.ObjectTypeMapping:
        from troposphere.customerprofiles import ObjectTypeMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3SourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html
    Properties:
        - Name: BucketName
        - Name: BucketPrefix
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html#cfn-customerprofiles-integration-s3sourceproperties-bucketname""", alias="BucketName")
    BucketPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html#cfn-customerprofiles-integration-s3sourceproperties-bucketprefix""", alias="BucketPrefix")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.S3SourceProperties:
        from troposphere.customerprofiles import S3SourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SalesforceSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html
    Properties:
        - Name: IncludeDeletedRecords
        - Name: Object
        - Name: EnableDynamicFieldUpdate
    
    """
    
    IncludeDeletedRecords_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-includedeletedrecords""", alias="IncludeDeletedRecords")
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-object""", alias="Object")
    EnableDynamicFieldUpdate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-enabledynamicfieldupdate""", alias="EnableDynamicFieldUpdate")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.SalesforceSourceProperties:
        from troposphere.customerprofiles import SalesforceSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScheduledTriggerProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html
    Properties:
        - Name: ScheduleEndTime
        - Name: Timezone
        - Name: ScheduleExpression
        - Name: FirstExecutionFrom
        - Name: ScheduleStartTime
        - Name: DataPullMode
        - Name: ScheduleOffset
    
    """
    
    ScheduleEndTime_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleendtime""", alias="ScheduleEndTime")
    Timezone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-timezone""", alias="Timezone")
    ScheduleExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleexpression""", alias="ScheduleExpression")
    FirstExecutionFrom_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-firstexecutionfrom""", alias="FirstExecutionFrom")
    ScheduleStartTime_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-schedulestarttime""", alias="ScheduleStartTime")
    DataPullMode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-datapullmode""", alias="DataPullMode")
    ScheduleOffset_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleoffset""", alias="ScheduleOffset")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.ScheduledTriggerProperties:
        from troposphere.customerprofiles import ScheduledTriggerProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServiceNowSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html#cfn-customerprofiles-integration-servicenowsourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.ServiceNowSourceProperties:
        from troposphere.customerprofiles import ServiceNowSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceConnectorProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html
    Properties:
        - Name: S3
        - Name: ServiceNow
        - Name: Zendesk
        - Name: Marketo
        - Name: Salesforce
    
    """
    
    S3_: Optional['S3SourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-s3""", alias="S3")
    ServiceNow_: Optional['ServiceNowSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-servicenow""", alias="ServiceNow")
    Zendesk_: Optional['ZendeskSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-zendesk""", alias="Zendesk")
    Marketo_: Optional['MarketoSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-marketo""", alias="Marketo")
    Salesforce_: Optional['SalesforceSourceProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-salesforce""", alias="Salesforce")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.SourceConnectorProperties:
        from troposphere.customerprofiles import SourceConnectorProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceFlowConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html
    Properties:
        - Name: ConnectorProfileName
        - Name: SourceConnectorProperties
        - Name: ConnectorType
        - Name: IncrementalPullConfig
    
    """
    
    ConnectorProfileName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-connectorprofilename""", alias="ConnectorProfileName")
    SourceConnectorProperties_: 'SourceConnectorProperties' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-sourceconnectorproperties""", alias="SourceConnectorProperties")
    ConnectorType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-connectortype""", alias="ConnectorType")
    IncrementalPullConfig_: Optional['IncrementalPullConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-incrementalpullconfig""", alias="IncrementalPullConfig")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.SourceFlowConfig:
        from troposphere.customerprofiles import SourceFlowConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Task(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html
    Properties:
        - Name: SourceFields
        - Name: DestinationField
        - Name: ConnectorOperator
        - Name: TaskType
        - Name: TaskProperties
    
    """
    
    SourceFields_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-sourcefields""", alias="SourceFields")
    DestinationField_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-destinationfield""", alias="DestinationField")
    ConnectorOperator_: Optional['ConnectorOperator'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-connectoroperator""", alias="ConnectorOperator")
    TaskType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-tasktype""", alias="TaskType")
    TaskProperties_: Optional[List['TaskPropertiesMap']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-taskproperties""", alias="TaskProperties")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.Task:
        from troposphere.customerprofiles import Task as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TaskPropertiesMap(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html
    Properties:
        - Name: OperatorPropertyKey
        - Name: Property
    
    """
    
    OperatorPropertyKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html#cfn-customerprofiles-integration-taskpropertiesmap-operatorpropertykey""", alias="OperatorPropertyKey")
    Property_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html#cfn-customerprofiles-integration-taskpropertiesmap-property""", alias="Property")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.TaskPropertiesMap:
        from troposphere.customerprofiles import TaskPropertiesMap as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TriggerConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html
    Properties:
        - Name: TriggerType
        - Name: TriggerProperties
    
    """
    
    TriggerType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html#cfn-customerprofiles-integration-triggerconfig-triggertype""", alias="TriggerType")
    TriggerProperties_: Optional['TriggerProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html#cfn-customerprofiles-integration-triggerconfig-triggerproperties""", alias="TriggerProperties")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.TriggerConfig:
        from troposphere.customerprofiles import TriggerConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TriggerProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html
    Properties:
        - Name: Scheduled
    
    """
    
    Scheduled_: Optional['ScheduledTriggerProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html#cfn-customerprofiles-integration-triggerproperties-scheduled""", alias="Scheduled")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.TriggerProperties:
        from troposphere.customerprofiles import TriggerProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ZendeskSourceProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html
    Properties:
        - Name: Object
    
    """
    
    Object_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html#cfn-customerprofiles-integration-zendesksourceproperties-object""", alias="Object")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.ZendeskSourceProperties:
        from troposphere.customerprofiles import ZendeskSourceProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FieldMap(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html
    Properties:
        - Name: Name
        - Name: ObjectTypeField
    
    """
    
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-name""", alias="Name")
    ObjectTypeField_: Optional['ObjectTypeField'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-objecttypefield""", alias="ObjectTypeField")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.FieldMap:
        from troposphere.customerprofiles import FieldMap as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeyMap(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html
    Properties:
        - Name: ObjectTypeKeyList
        - Name: Name
    
    """
    
    ObjectTypeKeyList_: Optional[List['ObjectTypeKey']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-objecttypekeylist""", alias="ObjectTypeKeyList")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.KeyMap:
        from troposphere.customerprofiles import KeyMap as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ObjectTypeField(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html
    Properties:
        - Name: Target
        - Name: ContentType
        - Name: Source
    
    """
    
    Target_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-target""", alias="Target")
    ContentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-contenttype""", alias="ContentType")
    Source_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-source""", alias="Source")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.ObjectTypeField:
        from troposphere.customerprofiles import ObjectTypeField as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ObjectTypeKey(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html
    Properties:
        - Name: FieldNames
        - Name: StandardIdentifiers
    
    """
    
    FieldNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-fieldnames""", alias="FieldNames")
    StandardIdentifiers_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-standardidentifiers""", alias="StandardIdentifiers")
    


    @property
    def tropo_type(self) -> troposphere.customerprofiles.ObjectTypeKey:
        from troposphere.customerprofiles import ObjectTypeKey as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class CalculatedAttributeDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html
    Properties:
        - Name: Description
        - Name: AttributeDetails
        - Name: Statistic
        - Name: DomainName
        - Name: DisplayName
        - Name: CalculatedAttributeName
        - Name: Conditions
        - Name: Tags
    Attributes:
        - Name: LastUpdatedAt
        - Name: CreatedAt
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-description""", alias="Description")
    AttributeDetails_: 'AttributeDetails' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-attributedetails""", alias="AttributeDetails")
    Statistic_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-statistic""", alias="Statistic")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-domainname""", alias="DomainName")
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-displayname""", alias="DisplayName")
    CalculatedAttributeName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-calculatedattributename""", alias="CalculatedAttributeName")
    Conditions_: Optional['Conditions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-conditions""", alias="Conditions")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.customerprofiles.CalculatedAttributeDefinition:
        from troposphere.customerprofiles import CalculatedAttributeDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.customerprofiles import CalculatedAttributeDefinition as TropoT
        return resource_to_troposphere(self, TropoT)


class Domain(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html
    Properties:
        - Name: Matching
        - Name: DefaultExpirationDays
        - Name: DomainName
        - Name: DeadLetterQueueUrl
        - Name: DefaultEncryptionKey
        - Name: RuleBasedMatching
        - Name: Tags
    Attributes:
        - Name: Stats.ProfileCount
        - Name: Stats.ObjectCount
        - Name: LastUpdatedAt
        - Name: CreatedAt
        - Name: Stats
        - Name: Stats.MeteringProfileCount
        - Name: Stats.TotalSize
        - Name: RuleBasedMatching.Status
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Matching_: Optional['Matching'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-matching""", alias="Matching")
    DefaultExpirationDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultexpirationdays""", alias="DefaultExpirationDays")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-domainname""", alias="DomainName")
    DeadLetterQueueUrl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-deadletterqueueurl""", alias="DeadLetterQueueUrl")
    DefaultEncryptionKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultencryptionkey""", alias="DefaultEncryptionKey")
    RuleBasedMatching_: Optional['RuleBasedMatching'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-rulebasedmatching""", alias="RuleBasedMatching")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.customerprofiles.Domain:
        from troposphere.customerprofiles import Domain as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.customerprofiles import Domain as TropoT
        return resource_to_troposphere(self, TropoT)


class EventStream(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html
    Properties:
        - Name: DomainName
        - Name: EventStreamName
        - Name: Uri
        - Name: Tags
    Attributes:
        - Name: DestinationDetails.Status
        - Name: EventStreamArn
        - Name: State
        - Name: CreatedAt
        - Name: DestinationDetails.Uri
        - Name: DestinationDetails
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html#cfn-customerprofiles-eventstream-domainname""", alias="DomainName")
    EventStreamName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html#cfn-customerprofiles-eventstream-eventstreamname""", alias="EventStreamName")
    Uri_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html#cfn-customerprofiles-eventstream-uri""", alias="Uri")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html#cfn-customerprofiles-eventstream-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.customerprofiles.EventStream:
        from troposphere.customerprofiles import EventStream as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.customerprofiles import EventStream as TropoT
        return resource_to_troposphere(self, TropoT)


class Integration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html
    Properties:
        - Name: ObjectTypeNames
        - Name: DomainName
        - Name: ObjectTypeName
        - Name: Uri
        - Name: FlowDefinition
        - Name: Tags
    Attributes:
        - Name: LastUpdatedAt
        - Name: CreatedAt
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ObjectTypeNames_: Optional[List['ObjectTypeMapping']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-objecttypenames""", alias="ObjectTypeNames")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-domainname""", alias="DomainName")
    ObjectTypeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-objecttypename""", alias="ObjectTypeName")
    Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-uri""", alias="Uri")
    FlowDefinition_: Optional['FlowDefinition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-flowdefinition""", alias="FlowDefinition")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.customerprofiles.Integration:
        from troposphere.customerprofiles import Integration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.customerprofiles import Integration as TropoT
        return resource_to_troposphere(self, TropoT)


class ObjectType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html
    Properties:
        - Name: Description
        - Name: Fields
        - Name: DomainName
        - Name: AllowProfileCreation
        - Name: ObjectTypeName
        - Name: Keys
        - Name: SourceLastUpdatedTimestampFormat
        - Name: EncryptionKey
        - Name: Tags
        - Name: TemplateId
        - Name: ExpirationDays
    Attributes:
        - Name: LastUpdatedAt
        - Name: CreatedAt
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-description""", alias="Description")
    Fields_: Optional[List['FieldMap']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-fields""", alias="Fields")
    DomainName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-domainname""", alias="DomainName")
    AllowProfileCreation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-allowprofilecreation""", alias="AllowProfileCreation")
    ObjectTypeName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-objecttypename""", alias="ObjectTypeName")
    Keys_: Optional[List['KeyMap']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-keys""", alias="Keys")
    SourceLastUpdatedTimestampFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-sourcelastupdatedtimestampformat""", alias="SourceLastUpdatedTimestampFormat")
    EncryptionKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-encryptionkey""", alias="EncryptionKey")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-tags""", alias="Tags")
    TemplateId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-templateid""", alias="TemplateId")
    ExpirationDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-expirationdays""", alias="ExpirationDays")
    

    @property
    def tropo_type(self) -> troposphere.customerprofiles.ObjectType:
        from troposphere.customerprofiles import ObjectType as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.customerprofiles import ObjectType as TropoT
        return resource_to_troposphere(self, TropoT)

