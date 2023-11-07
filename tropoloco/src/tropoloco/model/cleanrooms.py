from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AnalysisParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisparameter.html
    Properties:
        - Name: DefaultValue
        - Name: Type
        - Name: Name
    
    """
    
    DefaultValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisparameter.html#cfn-cleanrooms-analysistemplate-analysisparameter-defaultvalue""", alias="DefaultValue")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisparameter.html#cfn-cleanrooms-analysistemplate-analysisparameter-type""", alias="Type")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisparameter.html#cfn-cleanrooms-analysistemplate-analysisparameter-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.AnalysisParameter:
        from troposphere.cleanrooms import AnalysisParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalysisSchema(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisschema.html
    Properties:
        - Name: ReferencedTables
    
    """
    
    ReferencedTables_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisschema.html#cfn-cleanrooms-analysistemplate-analysisschema-referencedtables""", alias="ReferencedTables")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.AnalysisSchema:
        from troposphere.cleanrooms import AnalysisSchema as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalysisSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysissource.html
    Properties:
        - Name: Text
    
    """
    
    Text_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysissource.html#cfn-cleanrooms-analysistemplate-analysissource-text""", alias="Text")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.AnalysisSource:
        from troposphere.cleanrooms import AnalysisSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataEncryptionMetadata(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html
    Properties:
        - Name: AllowCleartext
        - Name: PreserveNulls
        - Name: AllowJoinsOnColumnsWithDifferentNames
        - Name: AllowDuplicates
    
    """
    
    AllowCleartext_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowcleartext""", alias="AllowCleartext")
    PreserveNulls_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html#cfn-cleanrooms-collaboration-dataencryptionmetadata-preservenulls""", alias="PreserveNulls")
    AllowJoinsOnColumnsWithDifferentNames_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowjoinsoncolumnswithdifferentnames""", alias="AllowJoinsOnColumnsWithDifferentNames")
    AllowDuplicates_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowduplicates""", alias="AllowDuplicates")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.DataEncryptionMetadata:
        from troposphere.cleanrooms import DataEncryptionMetadata as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MemberSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html
    Properties:
        - Name: AccountId
        - Name: DisplayName
        - Name: MemberAbilities
    
    """
    
    AccountId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html#cfn-cleanrooms-collaboration-memberspecification-accountid""", alias="AccountId")
    DisplayName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html#cfn-cleanrooms-collaboration-memberspecification-displayname""", alias="DisplayName")
    MemberAbilities_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html#cfn-cleanrooms-collaboration-memberspecification-memberabilities""", alias="MemberAbilities")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.MemberSpecification:
        from troposphere.cleanrooms import MemberSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AggregateColumn(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregatecolumn.html
    Properties:
        - Name: Function
        - Name: ColumnNames
    
    """
    
    Function_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregatecolumn.html#cfn-cleanrooms-configuredtable-aggregatecolumn-function""", alias="Function")
    ColumnNames_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregatecolumn.html#cfn-cleanrooms-configuredtable-aggregatecolumn-columnnames""", alias="ColumnNames")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.AggregateColumn:
        from troposphere.cleanrooms import AggregateColumn as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AggregationConstraint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregationconstraint.html
    Properties:
        - Name: ColumnName
        - Name: Minimum
        - Name: Type
    
    """
    
    ColumnName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregationconstraint.html#cfn-cleanrooms-configuredtable-aggregationconstraint-columnname""", alias="ColumnName")
    Minimum_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregationconstraint.html#cfn-cleanrooms-configuredtable-aggregationconstraint-minimum""", alias="Minimum")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregationconstraint.html#cfn-cleanrooms-configuredtable-aggregationconstraint-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.AggregationConstraint:
        from troposphere.cleanrooms import AggregationConstraint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalysisRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrule.html
    Properties:
        - Name: Policy
        - Name: Type
    
    """
    
    Policy_: 'ConfiguredTableAnalysisRulePolicy' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrule.html#cfn-cleanrooms-configuredtable-analysisrule-policy""", alias="Policy")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrule.html#cfn-cleanrooms-configuredtable-analysisrule-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.AnalysisRule:
        from troposphere.cleanrooms import AnalysisRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalysisRuleAggregation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html
    Properties:
        - Name: AllowedJoinOperators
        - Name: ScalarFunctions
        - Name: OutputConstraints
        - Name: DimensionColumns
        - Name: JoinColumns
        - Name: JoinRequired
        - Name: AggregateColumns
    
    """
    
    AllowedJoinOperators_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-allowedjoinoperators""", alias="AllowedJoinOperators")
    ScalarFunctions_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-scalarfunctions""", alias="ScalarFunctions")
    OutputConstraints_: List['AggregationConstraint'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-outputconstraints""", alias="OutputConstraints")
    DimensionColumns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-dimensioncolumns""", alias="DimensionColumns")
    JoinColumns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-joincolumns""", alias="JoinColumns")
    JoinRequired_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-joinrequired""", alias="JoinRequired")
    AggregateColumns_: List['AggregateColumn'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-aggregatecolumns""", alias="AggregateColumns")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.AnalysisRuleAggregation:
        from troposphere.cleanrooms import AnalysisRuleAggregation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalysisRuleCustom(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulecustom.html
    Properties:
        - Name: AllowedAnalysisProviders
        - Name: AllowedAnalyses
    
    """
    
    AllowedAnalysisProviders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulecustom.html#cfn-cleanrooms-configuredtable-analysisrulecustom-allowedanalysisproviders""", alias="AllowedAnalysisProviders")
    AllowedAnalyses_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulecustom.html#cfn-cleanrooms-configuredtable-analysisrulecustom-allowedanalyses""", alias="AllowedAnalyses")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.AnalysisRuleCustom:
        from troposphere.cleanrooms import AnalysisRuleCustom as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalysisRuleList(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html
    Properties:
        - Name: AllowedJoinOperators
        - Name: ListColumns
        - Name: JoinColumns
    
    """
    
    AllowedJoinOperators_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html#cfn-cleanrooms-configuredtable-analysisrulelist-allowedjoinoperators""", alias="AllowedJoinOperators")
    ListColumns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html#cfn-cleanrooms-configuredtable-analysisrulelist-listcolumns""", alias="ListColumns")
    JoinColumns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html#cfn-cleanrooms-configuredtable-analysisrulelist-joincolumns""", alias="JoinColumns")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.AnalysisRuleList:
        from troposphere.cleanrooms import AnalysisRuleList as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfiguredTableAnalysisRulePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy.html
    Properties:
        - Name: V1
    
    """
    
    V1_: 'ConfiguredTableAnalysisRulePolicyV1' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy.html#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicy-v1""", alias="V1")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.ConfiguredTableAnalysisRulePolicy:
        from troposphere.cleanrooms import ConfiguredTableAnalysisRulePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfiguredTableAnalysisRulePolicyV1(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.html
    Properties:
        - Name: Aggregation
        - Name: List
        - Name: Custom
    
    """
    
    Aggregation_: Optional['AnalysisRuleAggregation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.html#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-aggregation""", alias="Aggregation")
    List_: Optional['AnalysisRuleList'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.html#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-list""", alias="List")
    Custom_: Optional['AnalysisRuleCustom'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.html#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-custom""", alias="Custom")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.ConfiguredTableAnalysisRulePolicyV1:
        from troposphere.cleanrooms import ConfiguredTableAnalysisRulePolicyV1 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GlueTableReference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-gluetablereference.html
    Properties:
        - Name: TableName
        - Name: DatabaseName
    
    """
    
    TableName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-gluetablereference.html#cfn-cleanrooms-configuredtable-gluetablereference-tablename""", alias="TableName")
    DatabaseName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-gluetablereference.html#cfn-cleanrooms-configuredtable-gluetablereference-databasename""", alias="DatabaseName")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.GlueTableReference:
        from troposphere.cleanrooms import GlueTableReference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TableReference(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-tablereference.html
    Properties:
        - Name: Glue
    
    """
    
    Glue_: 'GlueTableReference' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-tablereference.html#cfn-cleanrooms-configuredtable-tablereference-glue""", alias="Glue")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.TableReference:
        from troposphere.cleanrooms import TableReference as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MembershipProtectedQueryOutputConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedqueryoutputconfiguration.html
    Properties:
        - Name: S3
    
    """
    
    S3_: 'ProtectedQueryS3OutputConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedqueryoutputconfiguration.html#cfn-cleanrooms-membership-membershipprotectedqueryoutputconfiguration-s3""", alias="S3")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.MembershipProtectedQueryOutputConfiguration:
        from troposphere.cleanrooms import MembershipProtectedQueryOutputConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MembershipProtectedQueryResultConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration.html
    Properties:
        - Name: OutputConfiguration
        - Name: RoleArn
    
    """
    
    OutputConfiguration_: 'MembershipProtectedQueryOutputConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration.html#cfn-cleanrooms-membership-membershipprotectedqueryresultconfiguration-outputconfiguration""", alias="OutputConfiguration")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration.html#cfn-cleanrooms-membership-membershipprotectedqueryresultconfiguration-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.MembershipProtectedQueryResultConfiguration:
        from troposphere.cleanrooms import MembershipProtectedQueryResultConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ProtectedQueryS3OutputConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration.html
    Properties:
        - Name: Bucket
        - Name: ResultFormat
        - Name: KeyPrefix
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration.html#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-bucket""", alias="Bucket")
    ResultFormat_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration.html#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-resultformat""", alias="ResultFormat")
    KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration.html#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-keyprefix""", alias="KeyPrefix")
    


    @property
    def tropo_type(self) -> troposphere.cleanrooms.ProtectedQueryS3OutputConfiguration:
        from troposphere.cleanrooms import ProtectedQueryS3OutputConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AnalysisTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html
    Properties:
        - Name: MembershipIdentifier
        - Name: Description
        - Name: Format
        - Name: AnalysisParameters
        - Name: Source
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: CollaborationIdentifier
        - Name: Schema.ReferencedTables
        - Name: MembershipArn
        - Name: Schema
        - Name: Arn
        - Name: CollaborationArn
        - Name: AnalysisTemplateIdentifier
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MembershipIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-membershipidentifier""", alias="MembershipIdentifier")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-description""", alias="Description")
    Format_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-format""", alias="Format")
    AnalysisParameters_: Optional[List['AnalysisParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-analysisparameters""", alias="AnalysisParameters")
    Source_: 'AnalysisSource' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-source""", alias="Source")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.cleanrooms.AnalysisTemplate:
        from troposphere.cleanrooms import AnalysisTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cleanrooms import AnalysisTemplate as TropoT
        return resource_to_troposphere(self, TropoT)


class Collaboration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html
    Properties:
        - Name: CreatorDisplayName
        - Name: CreatorMemberAbilities
        - Name: Description
        - Name: QueryLogStatus
        - Name: DataEncryptionMetadata
        - Name: Tags
        - Name: Members
        - Name: Name
    Attributes:
        - Name: CollaborationIdentifier
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CreatorDisplayName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-creatordisplayname""", alias="CreatorDisplayName")
    CreatorMemberAbilities_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-creatormemberabilities""", alias="CreatorMemberAbilities")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-description""", alias="Description")
    QueryLogStatus_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-querylogstatus""", alias="QueryLogStatus")
    DataEncryptionMetadata_: Optional['DataEncryptionMetadata'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-dataencryptionmetadata""", alias="DataEncryptionMetadata")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-tags""", alias="Tags")
    Members_: List['MemberSpecification'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-members""", alias="Members")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.cleanrooms.Collaboration:
        from troposphere.cleanrooms import Collaboration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cleanrooms import Collaboration as TropoT
        return resource_to_troposphere(self, TropoT)


class ConfiguredTable(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html
    Properties:
        - Name: AnalysisMethod
        - Name: TableReference
        - Name: Description
        - Name: AnalysisRules
        - Name: AllowedColumns
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: ConfiguredTableIdentifier
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AnalysisMethod_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-analysismethod""", alias="AnalysisMethod")
    TableReference_: 'TableReference' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-tablereference""", alias="TableReference")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-description""", alias="Description")
    AnalysisRules_: Optional[List['AnalysisRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-analysisrules""", alias="AnalysisRules")
    AllowedColumns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-allowedcolumns""", alias="AllowedColumns")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.cleanrooms.ConfiguredTable:
        from troposphere.cleanrooms import ConfiguredTable as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cleanrooms import ConfiguredTable as TropoT
        return resource_to_troposphere(self, TropoT)


class ConfiguredTableAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html
    Properties:
        - Name: MembershipIdentifier
        - Name: Description
        - Name: ConfiguredTableIdentifier
        - Name: Tags
        - Name: RoleArn
        - Name: Name
    Attributes:
        - Name: ConfiguredTableAssociationIdentifier
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MembershipIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-membershipidentifier""", alias="MembershipIdentifier")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-description""", alias="Description")
    ConfiguredTableIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-configuredtableidentifier""", alias="ConfiguredTableIdentifier")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-tags""", alias="Tags")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-rolearn""", alias="RoleArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.cleanrooms.ConfiguredTableAssociation:
        from troposphere.cleanrooms import ConfiguredTableAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cleanrooms import ConfiguredTableAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class Membership(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html
    Properties:
        - Name: CollaborationIdentifier
        - Name: DefaultResultConfiguration
        - Name: QueryLogStatus
        - Name: Tags
    Attributes:
        - Name: MembershipIdentifier
        - Name: Arn
        - Name: CollaborationCreatorAccountId
        - Name: CollaborationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CollaborationIdentifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-collaborationidentifier""", alias="CollaborationIdentifier")
    DefaultResultConfiguration_: Optional['MembershipProtectedQueryResultConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-defaultresultconfiguration""", alias="DefaultResultConfiguration")
    QueryLogStatus_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-querylogstatus""", alias="QueryLogStatus")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.cleanrooms.Membership:
        from troposphere.cleanrooms import Membership as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cleanrooms import Membership as TropoT
        return resource_to_troposphere(self, TropoT)

