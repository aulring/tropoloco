from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AutomationRulesAction(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesaction.html
    Properties:
        - Name: Type
        - Name: FindingFieldsUpdate
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesaction.html#cfn-securityhub-automationrule-automationrulesaction-type""", alias="Type")
    FindingFieldsUpdate_: 'AutomationRulesFindingFieldsUpdate' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesaction.html#cfn-securityhub-automationrule-automationrulesaction-findingfieldsupdate""", alias="FindingFieldsUpdate")
    


    @property
    def tropo_type(self) -> troposphere.securityhub.AutomationRulesAction:
        from troposphere.securityhub import AutomationRulesAction as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutomationRulesFindingFieldsUpdate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html
    Properties:
        - Name: Types
        - Name: Confidence
        - Name: Note
        - Name: VerificationState
        - Name: RelatedFindings
        - Name: Workflow
        - Name: Severity
        - Name: UserDefinedFields
        - Name: Criticality
    
    """
    
    Types_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-types""", alias="Types")
    Confidence_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-confidence""", alias="Confidence")
    Note_: Optional['NoteUpdate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-note""", alias="Note")
    VerificationState_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-verificationstate""", alias="VerificationState")
    RelatedFindings_: Optional[List['RelatedFinding']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-relatedfindings""", alias="RelatedFindings")
    Workflow_: Optional['WorkflowUpdate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-workflow""", alias="Workflow")
    Severity_: Optional['SeverityUpdate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-severity""", alias="Severity")
    UserDefinedFields_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-userdefinedfields""", alias="UserDefinedFields")
    Criticality_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-criticality""", alias="Criticality")
    


    @property
    def tropo_type(self) -> troposphere.securityhub.AutomationRulesFindingFieldsUpdate:
        from troposphere.securityhub import AutomationRulesFindingFieldsUpdate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AutomationRulesFindingFilters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html
    Properties:
        - Name: ProductArn
        - Name: SourceUrl
        - Name: ResourceDetailsOther
        - Name: Description
        - Name: ProductName
        - Name: ResourceTags
        - Name: FirstObservedAt
        - Name: CreatedAt
        - Name: NoteText
        - Name: LastObservedAt
        - Name: UserDefinedFields
        - Name: NoteUpdatedAt
        - Name: ComplianceSecurityControlId
        - Name: CompanyName
        - Name: ResourceRegion
        - Name: NoteUpdatedBy
        - Name: Confidence
        - Name: ResourcePartition
        - Name: VerificationState
        - Name: Criticality
        - Name: SeverityLabel
        - Name: RelatedFindingsProductArn
        - Name: ComplianceStatus
        - Name: GeneratorId
        - Name: RecordState
        - Name: Title
        - Name: ResourceType
        - Name: ComplianceAssociatedStandardsId
        - Name: UpdatedAt
        - Name: RelatedFindingsId
        - Name: WorkflowStatus
        - Name: Type
        - Name: ResourceId
        - Name: AwsAccountId
        - Name: Id
    
    """
    
    ProductArn_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-productarn""", alias="ProductArn")
    SourceUrl_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-sourceurl""", alias="SourceUrl")
    ResourceDetailsOther_: Optional[List['MapFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourcedetailsother""", alias="ResourceDetailsOther")
    Description_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-description""", alias="Description")
    ProductName_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-productname""", alias="ProductName")
    ResourceTags_: Optional[List['MapFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourcetags""", alias="ResourceTags")
    FirstObservedAt_: Optional[List['DateFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-firstobservedat""", alias="FirstObservedAt")
    CreatedAt_: Optional[List['DateFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-createdat""", alias="CreatedAt")
    NoteText_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-notetext""", alias="NoteText")
    LastObservedAt_: Optional[List['DateFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-lastobservedat""", alias="LastObservedAt")
    UserDefinedFields_: Optional[List['MapFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-userdefinedfields""", alias="UserDefinedFields")
    NoteUpdatedAt_: Optional[List['DateFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-noteupdatedat""", alias="NoteUpdatedAt")
    ComplianceSecurityControlId_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-compliancesecuritycontrolid""", alias="ComplianceSecurityControlId")
    CompanyName_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-companyname""", alias="CompanyName")
    ResourceRegion_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourceregion""", alias="ResourceRegion")
    NoteUpdatedBy_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-noteupdatedby""", alias="NoteUpdatedBy")
    Confidence_: Optional[List['NumberFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-confidence""", alias="Confidence")
    ResourcePartition_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourcepartition""", alias="ResourcePartition")
    VerificationState_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-verificationstate""", alias="VerificationState")
    Criticality_: Optional[List['NumberFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-criticality""", alias="Criticality")
    SeverityLabel_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-severitylabel""", alias="SeverityLabel")
    RelatedFindingsProductArn_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-relatedfindingsproductarn""", alias="RelatedFindingsProductArn")
    ComplianceStatus_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-compliancestatus""", alias="ComplianceStatus")
    GeneratorId_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-generatorid""", alias="GeneratorId")
    RecordState_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-recordstate""", alias="RecordState")
    Title_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-title""", alias="Title")
    ResourceType_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourcetype""", alias="ResourceType")
    ComplianceAssociatedStandardsId_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-complianceassociatedstandardsid""", alias="ComplianceAssociatedStandardsId")
    UpdatedAt_: Optional[List['DateFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-updatedat""", alias="UpdatedAt")
    RelatedFindingsId_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-relatedfindingsid""", alias="RelatedFindingsId")
    WorkflowStatus_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-workflowstatus""", alias="WorkflowStatus")
    Type_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-type""", alias="Type")
    ResourceId_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourceid""", alias="ResourceId")
    AwsAccountId_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-awsaccountid""", alias="AwsAccountId")
    Id_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.securityhub.AutomationRulesFindingFilters:
        from troposphere.securityhub import AutomationRulesFindingFilters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DateFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-datefilter.html
    Properties:
        - Name: DateRange
        - Name: Start
        - Name: End
    
    """
    
    DateRange_: Optional['DateRange'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-datefilter.html#cfn-securityhub-automationrule-datefilter-daterange""", alias="DateRange")
    Start_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-datefilter.html#cfn-securityhub-automationrule-datefilter-start""", alias="Start")
    End_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-datefilter.html#cfn-securityhub-automationrule-datefilter-end""", alias="End")
    


    @property
    def tropo_type(self) -> troposphere.securityhub.DateFilter:
        from troposphere.securityhub import DateFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DateRange(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-daterange.html
    Properties:
        - Name: Value
        - Name: Unit
    
    """
    
    Value_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-daterange.html#cfn-securityhub-automationrule-daterange-value""", alias="Value")
    Unit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-daterange.html#cfn-securityhub-automationrule-daterange-unit""", alias="Unit")
    


    @property
    def tropo_type(self) -> troposphere.securityhub.DateRange:
        from troposphere.securityhub import DateRange as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MapFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-mapfilter.html
    Properties:
        - Name: Comparison
        - Name: Value
        - Name: Key
    
    """
    
    Comparison_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-mapfilter.html#cfn-securityhub-automationrule-mapfilter-comparison""", alias="Comparison")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-mapfilter.html#cfn-securityhub-automationrule-mapfilter-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-mapfilter.html#cfn-securityhub-automationrule-mapfilter-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.securityhub.MapFilter:
        from troposphere.securityhub import MapFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NoteUpdate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-noteupdate.html
    Properties:
        - Name: UpdatedBy
        - Name: Text
    
    """
    
    UpdatedBy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-noteupdate.html#cfn-securityhub-automationrule-noteupdate-updatedby""", alias="UpdatedBy")
    Text_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-noteupdate.html#cfn-securityhub-automationrule-noteupdate-text""", alias="Text")
    


    @property
    def tropo_type(self) -> troposphere.securityhub.NoteUpdate:
        from troposphere.securityhub import NoteUpdate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NumberFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-numberfilter.html
    Properties:
        - Name: Gte
        - Name: Eq
        - Name: Lte
    
    """
    
    Gte_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-numberfilter.html#cfn-securityhub-automationrule-numberfilter-gte""", alias="Gte")
    Eq_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-numberfilter.html#cfn-securityhub-automationrule-numberfilter-eq""", alias="Eq")
    Lte_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-numberfilter.html#cfn-securityhub-automationrule-numberfilter-lte""", alias="Lte")
    


    @property
    def tropo_type(self) -> troposphere.securityhub.NumberFilter:
        from troposphere.securityhub import NumberFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RelatedFinding(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-relatedfinding.html
    Properties:
        - Name: ProductArn
        - Name: Id
    
    """
    
    ProductArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-relatedfinding.html#cfn-securityhub-automationrule-relatedfinding-productarn""", alias="ProductArn")
    Id_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-relatedfinding.html#cfn-securityhub-automationrule-relatedfinding-id""", alias="Id")
    


    @property
    def tropo_type(self) -> troposphere.securityhub.RelatedFinding:
        from troposphere.securityhub import RelatedFinding as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SeverityUpdate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-severityupdate.html
    Properties:
        - Name: Normalized
        - Name: Label
        - Name: Product
    
    """
    
    Normalized_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-severityupdate.html#cfn-securityhub-automationrule-severityupdate-normalized""", alias="Normalized")
    Label_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-severityupdate.html#cfn-securityhub-automationrule-severityupdate-label""", alias="Label")
    Product_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-severityupdate.html#cfn-securityhub-automationrule-severityupdate-product""", alias="Product")
    


    @property
    def tropo_type(self) -> troposphere.securityhub.SeverityUpdate:
        from troposphere.securityhub import SeverityUpdate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StringFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-stringfilter.html
    Properties:
        - Name: Comparison
        - Name: Value
    
    """
    
    Comparison_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-stringfilter.html#cfn-securityhub-automationrule-stringfilter-comparison""", alias="Comparison")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-stringfilter.html#cfn-securityhub-automationrule-stringfilter-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.securityhub.StringFilter:
        from troposphere.securityhub import StringFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WorkflowUpdate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-workflowupdate.html
    Properties:
        - Name: Status
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-workflowupdate.html#cfn-securityhub-automationrule-workflowupdate-status""", alias="Status")
    


    @property
    def tropo_type(self) -> troposphere.securityhub.WorkflowUpdate:
        from troposphere.securityhub import WorkflowUpdate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StandardsControl(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-standard-standardscontrol.html
    Properties:
        - Name: StandardsControlArn
        - Name: Reason
    
    """
    
    StandardsControlArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-standard-standardscontrol.html#cfn-securityhub-standard-standardscontrol-standardscontrolarn""", alias="StandardsControlArn")
    Reason_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-standard-standardscontrol.html#cfn-securityhub-standard-standardscontrol-reason""", alias="Reason")
    


    @property
    def tropo_type(self) -> troposphere.securityhub.StandardsControl:
        from troposphere.securityhub import StandardsControl as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AutomationRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html
    Properties:
        - Name: Description
        - Name: Actions
        - Name: IsTerminal
        - Name: RuleStatus
        - Name: Criteria
        - Name: RuleOrder
        - Name: RuleName
        - Name: Tags
    Attributes:
        - Name: CreatedBy
        - Name: RuleArn
        - Name: CreatedAt
        - Name: UpdatedAt
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-description""", alias="Description")
    Actions_: Optional[List['AutomationRulesAction']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-actions""", alias="Actions")
    IsTerminal_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-isterminal""", alias="IsTerminal")
    RuleStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-rulestatus""", alias="RuleStatus")
    Criteria_: Optional['AutomationRulesFindingFilters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-criteria""", alias="Criteria")
    RuleOrder_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-ruleorder""", alias="RuleOrder")
    RuleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-rulename""", alias="RuleName")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.securityhub.AutomationRule:
        from troposphere.securityhub import AutomationRule as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.securityhub import AutomationRule as TropoT
        return resource_to_troposphere(self, TropoT)


class Hub(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html
    Properties:
        - Name: ControlFindingGenerator
        - Name: EnableDefaultStandards
        - Name: AutoEnableControls
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ControlFindingGenerator_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html#cfn-securityhub-hub-controlfindinggenerator""", alias="ControlFindingGenerator")
    EnableDefaultStandards_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html#cfn-securityhub-hub-enabledefaultstandards""", alias="EnableDefaultStandards")
    AutoEnableControls_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html#cfn-securityhub-hub-autoenablecontrols""", alias="AutoEnableControls")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html#cfn-securityhub-hub-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.securityhub.Hub:
        from troposphere.securityhub import Hub as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.securityhub import Hub as TropoT
        return resource_to_troposphere(self, TropoT)


class Standard(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-standard.html
    Properties:
        - Name: StandardsArn
        - Name: DisabledStandardsControls
    Attributes:
        - Name: StandardsSubscriptionArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StandardsArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-standard.html#cfn-securityhub-standard-standardsarn""", alias="StandardsArn")
    DisabledStandardsControls_: Optional[List['StandardsControl']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-standard.html#cfn-securityhub-standard-disabledstandardscontrols""", alias="DisabledStandardsControls")
    

    @property
    def tropo_type(self) -> troposphere.securityhub.Standard:
        from troposphere.securityhub import Standard as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.securityhub import Standard as TropoT
        return resource_to_troposphere(self, TropoT)

