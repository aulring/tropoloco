from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Compliance(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-compliance.html
    Properties:
        - Name: Type
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-compliance.html#cfn-config-configrule-compliance-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.config.Compliance:
        from troposphere.config import Compliance as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CustomPolicyDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html
    Properties:
        - Name: EnableDebugLogDelivery
        - Name: PolicyText
        - Name: PolicyRuntime
    
    """
    
    EnableDebugLogDelivery_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html#cfn-config-configrule-custompolicydetails-enabledebuglogdelivery""", alias="EnableDebugLogDelivery")
    PolicyText_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html#cfn-config-configrule-custompolicydetails-policytext""", alias="PolicyText")
    PolicyRuntime_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html#cfn-config-configrule-custompolicydetails-policyruntime""", alias="PolicyRuntime")
    


    @property
    def tropo_type(self) -> troposphere.config.CustomPolicyDetails:
        from troposphere.config import CustomPolicyDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EvaluationModeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-evaluationmodeconfiguration.html
    Properties:
        - Name: Mode
    
    """
    
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-evaluationmodeconfiguration.html#cfn-config-configrule-evaluationmodeconfiguration-mode""", alias="Mode")
    


    @property
    def tropo_type(self) -> troposphere.config.EvaluationModeConfiguration:
        from troposphere.config import EvaluationModeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Scope(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html
    Properties:
        - Name: ComplianceResourceId
        - Name: TagKey
        - Name: ComplianceResourceTypes
        - Name: TagValue
    
    """
    
    ComplianceResourceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-complianceresourceid""", alias="ComplianceResourceId")
    TagKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-tagkey""", alias="TagKey")
    ComplianceResourceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-complianceresourcetypes""", alias="ComplianceResourceTypes")
    TagValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-tagvalue""", alias="TagValue")
    


    @property
    def tropo_type(self) -> troposphere.config.Scope:
        from troposphere.config import Scope as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Source(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html
    Properties:
        - Name: Owner
        - Name: CustomPolicyDetails
        - Name: SourceIdentifier
        - Name: SourceDetails
    
    """
    
    Owner_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-owner""", alias="Owner")
    CustomPolicyDetails_: Optional['CustomPolicyDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-custompolicydetails""", alias="CustomPolicyDetails")
    SourceIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-sourceidentifier""", alias="SourceIdentifier")
    SourceDetails_: Optional[List['SourceDetail']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-sourcedetails""", alias="SourceDetails")
    


    @property
    def tropo_type(self) -> troposphere.config.Source:
        from troposphere.config import Source as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceDetail(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-sourcedetail.html
    Properties:
        - Name: EventSource
        - Name: MaximumExecutionFrequency
        - Name: MessageType
    
    """
    
    EventSource_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-sourcedetail.html#cfn-config-configrule-sourcedetail-eventsource""", alias="EventSource")
    MaximumExecutionFrequency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-sourcedetail.html#cfn-config-configrule-sourcedetail-maximumexecutionfrequency""", alias="MaximumExecutionFrequency")
    MessageType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-sourcedetail.html#cfn-config-configrule-sourcedetail-messagetype""", alias="MessageType")
    


    @property
    def tropo_type(self) -> troposphere.config.SourceDetail:
        from troposphere.config import SourceDetail as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccountAggregationSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html
    Properties:
        - Name: AllAwsRegions
        - Name: AwsRegions
        - Name: AccountIds
    
    """
    
    AllAwsRegions_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html#cfn-config-configurationaggregator-accountaggregationsource-allawsregions""", alias="AllAwsRegions")
    AwsRegions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html#cfn-config-configurationaggregator-accountaggregationsource-awsregions""", alias="AwsRegions")
    AccountIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html#cfn-config-configurationaggregator-accountaggregationsource-accountids""", alias="AccountIds")
    


    @property
    def tropo_type(self) -> troposphere.config.AccountAggregationSource:
        from troposphere.config import AccountAggregationSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OrganizationAggregationSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html
    Properties:
        - Name: AllAwsRegions
        - Name: AwsRegions
        - Name: RoleArn
    
    """
    
    AllAwsRegions_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html#cfn-config-configurationaggregator-organizationaggregationsource-allawsregions""", alias="AllAwsRegions")
    AwsRegions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html#cfn-config-configurationaggregator-organizationaggregationsource-awsregions""", alias="AwsRegions")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html#cfn-config-configurationaggregator-organizationaggregationsource-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.config.OrganizationAggregationSource:
        from troposphere.config import OrganizationAggregationSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExclusionByResourceTypes(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-exclusionbyresourcetypes.html
    Properties:
        - Name: ResourceTypes
    
    """
    
    ResourceTypes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-exclusionbyresourcetypes.html#cfn-config-configurationrecorder-exclusionbyresourcetypes-resourcetypes""", alias="ResourceTypes")
    


    @property
    def tropo_type(self) -> troposphere.config.ExclusionByResourceTypes:
        from troposphere.config import ExclusionByResourceTypes as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecordingGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html
    Properties:
        - Name: AllSupported
        - Name: ExclusionByResourceTypes
        - Name: IncludeGlobalResourceTypes
        - Name: RecordingStrategy
        - Name: ResourceTypes
    
    """
    
    AllSupported_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-allsupported""", alias="AllSupported")
    ExclusionByResourceTypes_: Optional['ExclusionByResourceTypes'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-exclusionbyresourcetypes""", alias="ExclusionByResourceTypes")
    IncludeGlobalResourceTypes_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-includeglobalresourcetypes""", alias="IncludeGlobalResourceTypes")
    RecordingStrategy_: Optional['RecordingStrategy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-recordingstrategy""", alias="RecordingStrategy")
    ResourceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-resourcetypes""", alias="ResourceTypes")
    


    @property
    def tropo_type(self) -> troposphere.config.RecordingGroup:
        from troposphere.config import RecordingGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecordingMode(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmode.html
    Properties:
        - Name: RecordingFrequency
        - Name: RecordingModeOverrides
    
    """
    
    RecordingFrequency_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmode.html#cfn-config-configurationrecorder-recordingmode-recordingfrequency""", alias="RecordingFrequency")
    RecordingModeOverrides_: Optional[List['RecordingModeOverride']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmode.html#cfn-config-configurationrecorder-recordingmode-recordingmodeoverrides""", alias="RecordingModeOverrides")
    


    @property
    def tropo_type(self) -> troposphere.config.RecordingMode:
        from troposphere.config import RecordingMode as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecordingModeOverride(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmodeoverride.html
    Properties:
        - Name: Description
        - Name: RecordingFrequency
        - Name: ResourceTypes
    
    """
    
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmodeoverride.html#cfn-config-configurationrecorder-recordingmodeoverride-description""", alias="Description")
    RecordingFrequency_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmodeoverride.html#cfn-config-configurationrecorder-recordingmodeoverride-recordingfrequency""", alias="RecordingFrequency")
    ResourceTypes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmodeoverride.html#cfn-config-configurationrecorder-recordingmodeoverride-resourcetypes""", alias="ResourceTypes")
    


    @property
    def tropo_type(self) -> troposphere.config.RecordingModeOverride:
        from troposphere.config import RecordingModeOverride as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RecordingStrategy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingstrategy.html
    Properties:
        - Name: UseOnly
    
    """
    
    UseOnly_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingstrategy.html#cfn-config-configurationrecorder-recordingstrategy-useonly""", alias="UseOnly")
    


    @property
    def tropo_type(self) -> troposphere.config.RecordingStrategy:
        from troposphere.config import RecordingStrategy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConformancePackInputParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-conformancepackinputparameter.html
    Properties:
        - Name: ParameterValue
        - Name: ParameterName
    
    """
    
    ParameterValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-conformancepackinputparameter.html#cfn-config-conformancepack-conformancepackinputparameter-parametervalue""", alias="ParameterValue")
    ParameterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-conformancepackinputparameter.html#cfn-config-conformancepack-conformancepackinputparameter-parametername""", alias="ParameterName")
    


    @property
    def tropo_type(self) -> troposphere.config.ConformancePackInputParameter:
        from troposphere.config import ConformancePackInputParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TemplateSSMDocumentDetails(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-templatessmdocumentdetails.html
    Properties:
        - Name: DocumentVersion
        - Name: DocumentName
    
    """
    
    DocumentVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-templatessmdocumentdetails.html#cfn-config-conformancepack-templatessmdocumentdetails-documentversion""", alias="DocumentVersion")
    DocumentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-templatessmdocumentdetails.html#cfn-config-conformancepack-templatessmdocumentdetails-documentname""", alias="DocumentName")
    


    @property
    def tropo_type(self) -> troposphere.config.TemplateSSMDocumentDetails:
        from troposphere.config import TemplateSSMDocumentDetails as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfigSnapshotDeliveryProperties(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-deliverychannel-configsnapshotdeliveryproperties.html
    Properties:
        - Name: DeliveryFrequency
    
    """
    
    DeliveryFrequency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-deliverychannel-configsnapshotdeliveryproperties.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties-deliveryfrequency""", alias="DeliveryFrequency")
    


    @property
    def tropo_type(self) -> troposphere.config.ConfigSnapshotDeliveryProperties:
        from troposphere.config import ConfigSnapshotDeliveryProperties as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OrganizationCustomPolicyRuleMetadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html
    Properties:
        - Name: TagKeyScope
        - Name: TagValueScope
        - Name: Runtime
        - Name: PolicyText
        - Name: Description
        - Name: ResourceIdScope
        - Name: OrganizationConfigRuleTriggerTypes
        - Name: DebugLogDeliveryAccounts
        - Name: ResourceTypesScope
        - Name: MaximumExecutionFrequency
        - Name: InputParameters
    
    """
    
    TagKeyScope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-tagkeyscope""", alias="TagKeyScope")
    TagValueScope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-tagvaluescope""", alias="TagValueScope")
    Runtime_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-runtime""", alias="Runtime")
    PolicyText_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-policytext""", alias="PolicyText")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-description""", alias="Description")
    ResourceIdScope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-resourceidscope""", alias="ResourceIdScope")
    OrganizationConfigRuleTriggerTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-organizationconfigruletriggertypes""", alias="OrganizationConfigRuleTriggerTypes")
    DebugLogDeliveryAccounts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-debuglogdeliveryaccounts""", alias="DebugLogDeliveryAccounts")
    ResourceTypesScope_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-resourcetypesscope""", alias="ResourceTypesScope")
    MaximumExecutionFrequency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-maximumexecutionfrequency""", alias="MaximumExecutionFrequency")
    InputParameters_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-inputparameters""", alias="InputParameters")
    


    @property
    def tropo_type(self) -> troposphere.config.OrganizationCustomPolicyRuleMetadata:
        from troposphere.config import OrganizationCustomPolicyRuleMetadata as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OrganizationCustomRuleMetadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html
    Properties:
        - Name: TagKeyScope
        - Name: TagValueScope
        - Name: Description
        - Name: ResourceIdScope
        - Name: LambdaFunctionArn
        - Name: OrganizationConfigRuleTriggerTypes
        - Name: ResourceTypesScope
        - Name: MaximumExecutionFrequency
        - Name: InputParameters
    
    """
    
    TagKeyScope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-tagkeyscope""", alias="TagKeyScope")
    TagValueScope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-tagvaluescope""", alias="TagValueScope")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-description""", alias="Description")
    ResourceIdScope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-resourceidscope""", alias="ResourceIdScope")
    LambdaFunctionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-lambdafunctionarn""", alias="LambdaFunctionArn")
    OrganizationConfigRuleTriggerTypes_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-organizationconfigruletriggertypes""", alias="OrganizationConfigRuleTriggerTypes")
    ResourceTypesScope_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-resourcetypesscope""", alias="ResourceTypesScope")
    MaximumExecutionFrequency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-maximumexecutionfrequency""", alias="MaximumExecutionFrequency")
    InputParameters_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-inputparameters""", alias="InputParameters")
    


    @property
    def tropo_type(self) -> troposphere.config.OrganizationCustomRuleMetadata:
        from troposphere.config import OrganizationCustomRuleMetadata as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OrganizationManagedRuleMetadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html
    Properties:
        - Name: TagKeyScope
        - Name: TagValueScope
        - Name: Description
        - Name: ResourceIdScope
        - Name: RuleIdentifier
        - Name: ResourceTypesScope
        - Name: MaximumExecutionFrequency
        - Name: InputParameters
    
    """
    
    TagKeyScope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-tagkeyscope""", alias="TagKeyScope")
    TagValueScope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-tagvaluescope""", alias="TagValueScope")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-description""", alias="Description")
    ResourceIdScope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-resourceidscope""", alias="ResourceIdScope")
    RuleIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-ruleidentifier""", alias="RuleIdentifier")
    ResourceTypesScope_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-resourcetypesscope""", alias="ResourceTypesScope")
    MaximumExecutionFrequency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-maximumexecutionfrequency""", alias="MaximumExecutionFrequency")
    InputParameters_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-inputparameters""", alias="InputParameters")
    


    @property
    def tropo_type(self) -> troposphere.config.OrganizationManagedRuleMetadata:
        from troposphere.config import OrganizationManagedRuleMetadata as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConformancePackInputParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconformancepack-conformancepackinputparameter.html
    Properties:
        - Name: ParameterValue
        - Name: ParameterName
    
    """
    
    ParameterValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconformancepack-conformancepackinputparameter.html#cfn-config-organizationconformancepack-conformancepackinputparameter-parametervalue""", alias="ParameterValue")
    ParameterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconformancepack-conformancepackinputparameter.html#cfn-config-organizationconformancepack-conformancepackinputparameter-parametername""", alias="ParameterName")
    


    @property
    def tropo_type(self) -> troposphere.config.ConformancePackInputParameter:
        from troposphere.config import ConformancePackInputParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExecutionControls(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-executioncontrols.html
    Properties:
        - Name: SsmControls
    
    """
    
    SsmControls_: Optional['SsmControls'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-executioncontrols.html#cfn-config-remediationconfiguration-executioncontrols-ssmcontrols""", alias="SsmControls")
    


    @property
    def tropo_type(self) -> troposphere.config.ExecutionControls:
        from troposphere.config import ExecutionControls as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RemediationParameterValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-remediationparametervalue.html
    Properties:
        - Name: ResourceValue
        - Name: StaticValue
    
    """
    
    ResourceValue_: Optional['ResourceValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-remediationparametervalue.html#cfn-config-remediationconfiguration-remediationparametervalue-resourcevalue""", alias="ResourceValue")
    StaticValue_: Optional['StaticValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-remediationparametervalue.html#cfn-config-remediationconfiguration-remediationparametervalue-staticvalue""", alias="StaticValue")
    


    @property
    def tropo_type(self) -> troposphere.config.RemediationParameterValue:
        from troposphere.config import RemediationParameterValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-resourcevalue.html
    Properties:
        - Name: Value
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-resourcevalue.html#cfn-config-remediationconfiguration-resourcevalue-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.config.ResourceValue:
        from troposphere.config import ResourceValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SsmControls(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-ssmcontrols.html
    Properties:
        - Name: ErrorPercentage
        - Name: ConcurrentExecutionRatePercentage
    
    """
    
    ErrorPercentage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-ssmcontrols.html#cfn-config-remediationconfiguration-ssmcontrols-errorpercentage""", alias="ErrorPercentage")
    ConcurrentExecutionRatePercentage_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-ssmcontrols.html#cfn-config-remediationconfiguration-ssmcontrols-concurrentexecutionratepercentage""", alias="ConcurrentExecutionRatePercentage")
    


    @property
    def tropo_type(self) -> troposphere.config.SsmControls:
        from troposphere.config import SsmControls as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StaticValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-staticvalue.html
    Properties:
        - Name: Values
    
    """
    
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-staticvalue.html#cfn-config-remediationconfiguration-staticvalue-values""", alias="Values")
    


    @property
    def tropo_type(self) -> troposphere.config.StaticValue:
        from troposphere.config import StaticValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AggregationAuthorization(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html
    Properties:
        - Name: AuthorizedAccountId
        - Name: AuthorizedAwsRegion
        - Name: Tags
    Attributes:
        - Name: AggregationAuthorizationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AuthorizedAccountId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-authorizedaccountid""", alias="AuthorizedAccountId")
    AuthorizedAwsRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-authorizedawsregion""", alias="AuthorizedAwsRegion")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.config.AggregationAuthorization:
        from troposphere.config import AggregationAuthorization as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.config import AggregationAuthorization as TropoT
        return resource_to_troposphere(self, TropoT)


class ConfigRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html
    Properties:
        - Name: EvaluationModes
        - Name: Description
        - Name: Scope
        - Name: Compliance
        - Name: ConfigRuleName
        - Name: MaximumExecutionFrequency
        - Name: Source
        - Name: InputParameters
    Attributes:
        - Name: ConfigRuleId
        - Name: Compliance.Type
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    EvaluationModes_: Optional[List['EvaluationModeConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-evaluationmodes""", alias="EvaluationModes")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-description""", alias="Description")
    Scope_: Optional['Scope'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-scope""", alias="Scope")
    Compliance_: Optional['Compliance'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-compliance""", alias="Compliance")
    ConfigRuleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-configrulename""", alias="ConfigRuleName")
    MaximumExecutionFrequency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-maximumexecutionfrequency""", alias="MaximumExecutionFrequency")
    Source_: 'Source' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-source""", alias="Source")
    InputParameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-inputparameters""", alias="InputParameters")
    

    @property
    def tropo_type(self) -> troposphere.config.ConfigRule:
        from troposphere.config import ConfigRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.config import ConfigRule as TropoT
        return resource_to_troposphere(self, TropoT)


class ConfigurationAggregator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html
    Properties:
        - Name: AccountAggregationSources
        - Name: ConfigurationAggregatorName
        - Name: OrganizationAggregationSource
        - Name: Tags
    Attributes:
        - Name: ConfigurationAggregatorArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AccountAggregationSources_: Optional[List['AccountAggregationSource']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-accountaggregationsources""", alias="AccountAggregationSources")
    ConfigurationAggregatorName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-configurationaggregatorname""", alias="ConfigurationAggregatorName")
    OrganizationAggregationSource_: Optional['OrganizationAggregationSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-organizationaggregationsource""", alias="OrganizationAggregationSource")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.config.ConfigurationAggregator:
        from troposphere.config import ConfigurationAggregator as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.config import ConfigurationAggregator as TropoT
        return resource_to_troposphere(self, TropoT)


class ConfigurationRecorder(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html
    Properties:
        - Name: Name
        - Name: RecordingGroup
        - Name: RecordingMode
        - Name: RoleARN
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-name""", alias="Name")
    RecordingGroup_: Optional['RecordingGroup'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-recordinggroup""", alias="RecordingGroup")
    RecordingMode_: Optional['RecordingMode'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-recordingmode""", alias="RecordingMode")
    RoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-rolearn""", alias="RoleARN")
    

    @property
    def tropo_type(self) -> troposphere.config.ConfigurationRecorder:
        from troposphere.config import ConfigurationRecorder as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.config import ConfigurationRecorder as TropoT
        return resource_to_troposphere(self, TropoT)


class ConformancePack(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html
    Properties:
        - Name: ConformancePackInputParameters
        - Name: TemplateSSMDocumentDetails
        - Name: DeliveryS3Bucket
        - Name: ConformancePackName
        - Name: DeliveryS3KeyPrefix
        - Name: TemplateBody
        - Name: TemplateS3Uri
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConformancePackInputParameters_: Optional[List['ConformancePackInputParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-conformancepackinputparameters""", alias="ConformancePackInputParameters")
    TemplateSSMDocumentDetails_: Optional['TemplateSSMDocumentDetails'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-templatessmdocumentdetails""", alias="TemplateSSMDocumentDetails")
    DeliveryS3Bucket_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-deliverys3bucket""", alias="DeliveryS3Bucket")
    ConformancePackName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-conformancepackname""", alias="ConformancePackName")
    DeliveryS3KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-deliverys3keyprefix""", alias="DeliveryS3KeyPrefix")
    TemplateBody_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-templatebody""", alias="TemplateBody")
    TemplateS3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-templates3uri""", alias="TemplateS3Uri")
    

    @property
    def tropo_type(self) -> troposphere.config.ConformancePack:
        from troposphere.config import ConformancePack as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.config import ConformancePack as TropoT
        return resource_to_troposphere(self, TropoT)


class DeliveryChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html
    Properties:
        - Name: ConfigSnapshotDeliveryProperties
        - Name: Name
        - Name: S3BucketName
        - Name: S3KeyPrefix
        - Name: S3KmsKeyArn
        - Name: SnsTopicARN
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConfigSnapshotDeliveryProperties_: Optional['ConfigSnapshotDeliveryProperties'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties""", alias="ConfigSnapshotDeliveryProperties")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-name""", alias="Name")
    S3BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3bucketname""", alias="S3BucketName")
    S3KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3keyprefix""", alias="S3KeyPrefix")
    S3KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3kmskeyarn""", alias="S3KmsKeyArn")
    SnsTopicARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-snstopicarn""", alias="SnsTopicARN")
    

    @property
    def tropo_type(self) -> troposphere.config.DeliveryChannel:
        from troposphere.config import DeliveryChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.config import DeliveryChannel as TropoT
        return resource_to_troposphere(self, TropoT)


class OrganizationConfigRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html
    Properties:
        - Name: OrganizationManagedRuleMetadata
        - Name: OrganizationConfigRuleName
        - Name: OrganizationCustomRuleMetadata
        - Name: ExcludedAccounts
        - Name: OrganizationCustomPolicyRuleMetadata
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OrganizationManagedRuleMetadata_: Optional['OrganizationManagedRuleMetadata'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata""", alias="OrganizationManagedRuleMetadata")
    OrganizationConfigRuleName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationconfigrulename""", alias="OrganizationConfigRuleName")
    OrganizationCustomRuleMetadata_: Optional['OrganizationCustomRuleMetadata'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata""", alias="OrganizationCustomRuleMetadata")
    ExcludedAccounts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-excludedaccounts""", alias="ExcludedAccounts")
    OrganizationCustomPolicyRuleMetadata_: Optional['OrganizationCustomPolicyRuleMetadata'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata""", alias="OrganizationCustomPolicyRuleMetadata")
    

    @property
    def tropo_type(self) -> troposphere.config.OrganizationConfigRule:
        from troposphere.config import OrganizationConfigRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.config import OrganizationConfigRule as TropoT
        return resource_to_troposphere(self, TropoT)


class OrganizationConformancePack(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html
    Properties:
        - Name: ConformancePackInputParameters
        - Name: DeliveryS3Bucket
        - Name: ExcludedAccounts
        - Name: DeliveryS3KeyPrefix
        - Name: TemplateBody
        - Name: OrganizationConformancePackName
        - Name: TemplateS3Uri
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConformancePackInputParameters_: Optional[List['ConformancePackInputParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-conformancepackinputparameters""", alias="ConformancePackInputParameters")
    DeliveryS3Bucket_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-deliverys3bucket""", alias="DeliveryS3Bucket")
    ExcludedAccounts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-excludedaccounts""", alias="ExcludedAccounts")
    DeliveryS3KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-deliverys3keyprefix""", alias="DeliveryS3KeyPrefix")
    TemplateBody_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-templatebody""", alias="TemplateBody")
    OrganizationConformancePackName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-organizationconformancepackname""", alias="OrganizationConformancePackName")
    TemplateS3Uri_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-templates3uri""", alias="TemplateS3Uri")
    

    @property
    def tropo_type(self) -> troposphere.config.OrganizationConformancePack:
        from troposphere.config import OrganizationConformancePack as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.config import OrganizationConformancePack as TropoT
        return resource_to_troposphere(self, TropoT)


class RemediationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html
    Properties:
        - Name: TargetVersion
        - Name: ExecutionControls
        - Name: Parameters
        - Name: TargetType
        - Name: ConfigRuleName
        - Name: ResourceType
        - Name: RetryAttemptSeconds
        - Name: MaximumAutomaticAttempts
        - Name: TargetId
        - Name: Automatic
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TargetVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-targetversion""", alias="TargetVersion")
    ExecutionControls_: Optional['ExecutionControls'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-executioncontrols""", alias="ExecutionControls")
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-parameters""", alias="Parameters")
    TargetType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-targettype""", alias="TargetType")
    ConfigRuleName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-configrulename""", alias="ConfigRuleName")
    ResourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-resourcetype""", alias="ResourceType")
    RetryAttemptSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-retryattemptseconds""", alias="RetryAttemptSeconds")
    MaximumAutomaticAttempts_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-maximumautomaticattempts""", alias="MaximumAutomaticAttempts")
    TargetId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-targetid""", alias="TargetId")
    Automatic_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-automatic""", alias="Automatic")
    

    @property
    def tropo_type(self) -> troposphere.config.RemediationConfiguration:
        from troposphere.config import RemediationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.config import RemediationConfiguration as TropoT
        return resource_to_troposphere(self, TropoT)


class StoredQuery(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html
    Properties:
        - Name: QueryDescription
        - Name: QueryExpression
        - Name: Tags
        - Name: QueryName
    Attributes:
        - Name: QueryArn
        - Name: QueryId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    QueryDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-querydescription""", alias="QueryDescription")
    QueryExpression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-queryexpression""", alias="QueryExpression")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-tags""", alias="Tags")
    QueryName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-queryname""", alias="QueryName")
    

    @property
    def tropo_type(self) -> troposphere.config.StoredQuery:
        from troposphere.config import StoredQuery as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.config import StoredQuery as TropoT
        return resource_to_troposphere(self, TropoT)

