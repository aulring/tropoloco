from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AdvancedBackupSettingResourceType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html
    Properties:
        - Name: BackupOptions
        - Name: ResourceType
    
    """
    
    BackupOptions_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html#cfn-backup-backupplan-advancedbackupsettingresourcetype-backupoptions""", alias="BackupOptions")
    ResourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html#cfn-backup-backupplan-advancedbackupsettingresourcetype-resourcetype""", alias="ResourceType")
    


    @property
    def tropo_type(self) -> troposphere.backup.AdvancedBackupSettingResourceType:
        from troposphere.backup import AdvancedBackupSettingResourceType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BackupPlanResourceType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html
    Properties:
        - Name: BackupPlanName
        - Name: AdvancedBackupSettings
        - Name: BackupPlanRule
    
    """
    
    BackupPlanName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-backupplanname""", alias="BackupPlanName")
    AdvancedBackupSettings_: Optional[List['AdvancedBackupSettingResourceType']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-advancedbackupsettings""", alias="AdvancedBackupSettings")
    BackupPlanRule_: List['BackupRuleResourceType'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-backupplanrule""", alias="BackupPlanRule")
    


    @property
    def tropo_type(self) -> troposphere.backup.BackupPlanResourceType:
        from troposphere.backup import BackupPlanResourceType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BackupRuleResourceType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html
    Properties:
        - Name: CompletionWindowMinutes
        - Name: ScheduleExpression
        - Name: RecoveryPointTags
        - Name: CopyActions
        - Name: EnableContinuousBackup
        - Name: Lifecycle
        - Name: TargetBackupVault
        - Name: StartWindowMinutes
        - Name: ScheduleExpressionTimezone
        - Name: RuleName
    
    """
    
    CompletionWindowMinutes_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-completionwindowminutes""", alias="CompletionWindowMinutes")
    ScheduleExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-scheduleexpression""", alias="ScheduleExpression")
    RecoveryPointTags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-recoverypointtags""", alias="RecoveryPointTags")
    CopyActions_: Optional[List['CopyActionResourceType']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-copyactions""", alias="CopyActions")
    EnableContinuousBackup_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-enablecontinuousbackup""", alias="EnableContinuousBackup")
    Lifecycle_: Optional['LifecycleResourceType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-lifecycle""", alias="Lifecycle")
    TargetBackupVault_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-targetbackupvault""", alias="TargetBackupVault")
    StartWindowMinutes_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-startwindowminutes""", alias="StartWindowMinutes")
    ScheduleExpressionTimezone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-scheduleexpressiontimezone""", alias="ScheduleExpressionTimezone")
    RuleName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-rulename""", alias="RuleName")
    


    @property
    def tropo_type(self) -> troposphere.backup.BackupRuleResourceType:
        from troposphere.backup import BackupRuleResourceType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CopyActionResourceType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html
    Properties:
        - Name: Lifecycle
        - Name: DestinationBackupVaultArn
    
    """
    
    Lifecycle_: Optional['LifecycleResourceType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html#cfn-backup-backupplan-copyactionresourcetype-lifecycle""", alias="Lifecycle")
    DestinationBackupVaultArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html#cfn-backup-backupplan-copyactionresourcetype-destinationbackupvaultarn""", alias="DestinationBackupVaultArn")
    


    @property
    def tropo_type(self) -> troposphere.backup.CopyActionResourceType:
        from troposphere.backup import CopyActionResourceType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LifecycleResourceType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html
    Properties:
        - Name: DeleteAfterDays
        - Name: MoveToColdStorageAfterDays
    
    """
    
    DeleteAfterDays_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html#cfn-backup-backupplan-lifecycleresourcetype-deleteafterdays""", alias="DeleteAfterDays")
    MoveToColdStorageAfterDays_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html#cfn-backup-backupplan-lifecycleresourcetype-movetocoldstorageafterdays""", alias="MoveToColdStorageAfterDays")
    


    @property
    def tropo_type(self) -> troposphere.backup.LifecycleResourceType:
        from troposphere.backup import LifecycleResourceType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BackupSelectionResourceType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html
    Properties:
        - Name: ListOfTags
        - Name: NotResources
        - Name: SelectionName
        - Name: IamRoleArn
        - Name: Resources
        - Name: Conditions
    
    """
    
    ListOfTags_: Optional[List['ConditionResourceType']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-listoftags""", alias="ListOfTags")
    NotResources_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-notresources""", alias="NotResources")
    SelectionName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-selectionname""", alias="SelectionName")
    IamRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-iamrolearn""", alias="IamRoleArn")
    Resources_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-resources""", alias="Resources")
    Conditions_: Optional['Conditions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-conditions""", alias="Conditions")
    


    @property
    def tropo_type(self) -> troposphere.backup.BackupSelectionResourceType:
        from troposphere.backup import BackupSelectionResourceType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConditionParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionparameter.html
    Properties:
        - Name: ConditionValue
        - Name: ConditionKey
    
    """
    
    ConditionValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionparameter.html#cfn-backup-backupselection-conditionparameter-conditionvalue""", alias="ConditionValue")
    ConditionKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionparameter.html#cfn-backup-backupselection-conditionparameter-conditionkey""", alias="ConditionKey")
    


    @property
    def tropo_type(self) -> troposphere.backup.ConditionParameter:
        from troposphere.backup import ConditionParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConditionResourceType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html
    Properties:
        - Name: ConditionValue
        - Name: ConditionKey
        - Name: ConditionType
    
    """
    
    ConditionValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditionvalue""", alias="ConditionValue")
    ConditionKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditionkey""", alias="ConditionKey")
    ConditionType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditiontype""", alias="ConditionType")
    


    @property
    def tropo_type(self) -> troposphere.backup.ConditionResourceType:
        from troposphere.backup import ConditionResourceType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Conditions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html
    Properties:
        - Name: StringEquals
        - Name: StringNotLike
        - Name: StringLike
        - Name: StringNotEquals
    
    """
    
    StringEquals_: Optional[List['ConditionParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html#cfn-backup-backupselection-conditions-stringequals""", alias="StringEquals")
    StringNotLike_: Optional[List['ConditionParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html#cfn-backup-backupselection-conditions-stringnotlike""", alias="StringNotLike")
    StringLike_: Optional[List['ConditionParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html#cfn-backup-backupselection-conditions-stringlike""", alias="StringLike")
    StringNotEquals_: Optional[List['ConditionParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html#cfn-backup-backupselection-conditions-stringnotequals""", alias="StringNotEquals")
    


    @property
    def tropo_type(self) -> troposphere.backup.Conditions:
        from troposphere.backup import Conditions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LockConfigurationType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html
    Properties:
        - Name: ChangeableForDays
        - Name: MaxRetentionDays
        - Name: MinRetentionDays
    
    """
    
    ChangeableForDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-changeablefordays""", alias="ChangeableForDays")
    MaxRetentionDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-maxretentiondays""", alias="MaxRetentionDays")
    MinRetentionDays_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-minretentiondays""", alias="MinRetentionDays")
    


    @property
    def tropo_type(self) -> troposphere.backup.LockConfigurationType:
        from troposphere.backup import LockConfigurationType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationObjectType(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html
    Properties:
        - Name: SNSTopicArn
        - Name: BackupVaultEvents
    
    """
    
    SNSTopicArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html#cfn-backup-backupvault-notificationobjecttype-snstopicarn""", alias="SNSTopicArn")
    BackupVaultEvents_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html#cfn-backup-backupvault-notificationobjecttype-backupvaultevents""", alias="BackupVaultEvents")
    


    @property
    def tropo_type(self) -> troposphere.backup.NotificationObjectType:
        from troposphere.backup import NotificationObjectType as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ControlInputParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html
    Properties:
        - Name: ParameterValue
        - Name: ParameterName
    
    """
    
    ParameterValue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html#cfn-backup-framework-controlinputparameter-parametervalue""", alias="ParameterValue")
    ParameterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html#cfn-backup-framework-controlinputparameter-parametername""", alias="ParameterName")
    


    @property
    def tropo_type(self) -> troposphere.backup.ControlInputParameter:
        from troposphere.backup import ControlInputParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ControlScope(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlscope.html
    Properties:
        - Name: ComplianceResourceTypes
        - Name: Tags
        - Name: ComplianceResourceIds
    
    """
    
    ComplianceResourceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlscope.html#cfn-backup-framework-controlscope-complianceresourcetypes""", alias="ComplianceResourceTypes")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlscope.html#cfn-backup-framework-controlscope-tags""", alias="Tags")
    ComplianceResourceIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlscope.html#cfn-backup-framework-controlscope-complianceresourceids""", alias="ComplianceResourceIds")
    


    @property
    def tropo_type(self) -> troposphere.backup.ControlScope:
        from troposphere.backup import ControlScope as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FrameworkControl(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html
    Properties:
        - Name: ControlName
        - Name: ControlInputParameters
        - Name: ControlScope
    
    """
    
    ControlName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlname""", alias="ControlName")
    ControlInputParameters_: Optional[List['ControlInputParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlinputparameters""", alias="ControlInputParameters")
    ControlScope_: Optional['ControlScope'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlscope""", alias="ControlScope")
    


    @property
    def tropo_type(self) -> troposphere.backup.FrameworkControl:
        from troposphere.backup import FrameworkControl as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReportDeliveryChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportdeliverychannel.html
    Properties:
        - Name: S3KeyPrefix
        - Name: Formats
        - Name: S3BucketName
    
    """
    
    S3KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportdeliverychannel.html#cfn-backup-reportplan-reportdeliverychannel-s3keyprefix""", alias="S3KeyPrefix")
    Formats_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportdeliverychannel.html#cfn-backup-reportplan-reportdeliverychannel-formats""", alias="Formats")
    S3BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportdeliverychannel.html#cfn-backup-reportplan-reportdeliverychannel-s3bucketname""", alias="S3BucketName")
    


    @property
    def tropo_type(self) -> troposphere.backup.ReportDeliveryChannel:
        from troposphere.backup import ReportDeliveryChannel as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReportSetting(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html
    Properties:
        - Name: FrameworkArns
        - Name: ReportTemplate
        - Name: OrganizationUnits
        - Name: Regions
        - Name: Accounts
    
    """
    
    FrameworkArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-frameworkarns""", alias="FrameworkArns")
    ReportTemplate_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-reporttemplate""", alias="ReportTemplate")
    OrganizationUnits_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-organizationunits""", alias="OrganizationUnits")
    Regions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-regions""", alias="Regions")
    Accounts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-accounts""", alias="Accounts")
    


    @property
    def tropo_type(self) -> troposphere.backup.ReportSetting:
        from troposphere.backup import ReportSetting as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class BackupPlan(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html
    Properties:
        - Name: BackupPlan
        - Name: BackupPlanTags
    Attributes:
        - Name: VersionId
        - Name: BackupPlanId
        - Name: BackupPlanArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BackupPlan_: 'BackupPlanResourceType' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#cfn-backup-backupplan-backupplan""", alias="BackupPlan")
    BackupPlanTags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#cfn-backup-backupplan-backupplantags""", alias="BackupPlanTags")
    

    @property
    def tropo_type(self) -> troposphere.backup.BackupPlan:
        from troposphere.backup import BackupPlan as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.backup import BackupPlan as TropoT
        return resource_to_troposphere(self, TropoT)


class BackupSelection(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html
    Properties:
        - Name: BackupSelection
        - Name: BackupPlanId
    Attributes:
        - Name: BackupPlanId
        - Name: Id
        - Name: SelectionId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BackupSelection_: 'BackupSelectionResourceType' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#cfn-backup-backupselection-backupselection""", alias="BackupSelection")
    BackupPlanId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#cfn-backup-backupselection-backupplanid""", alias="BackupPlanId")
    

    @property
    def tropo_type(self) -> troposphere.backup.BackupSelection:
        from troposphere.backup import BackupSelection as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.backup import BackupSelection as TropoT
        return resource_to_troposphere(self, TropoT)


class BackupVault(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html
    Properties:
        - Name: BackupVaultTags
        - Name: BackupVaultName
        - Name: EncryptionKeyArn
        - Name: LockConfiguration
        - Name: Notifications
        - Name: AccessPolicy
    Attributes:
        - Name: BackupVaultName
        - Name: BackupVaultArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BackupVaultTags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-backupvaulttags""", alias="BackupVaultTags")
    BackupVaultName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-backupvaultname""", alias="BackupVaultName")
    EncryptionKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-encryptionkeyarn""", alias="EncryptionKeyArn")
    LockConfiguration_: Optional['LockConfigurationType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-lockconfiguration""", alias="LockConfiguration")
    Notifications_: Optional['NotificationObjectType'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-notifications""", alias="Notifications")
    AccessPolicy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-accesspolicy""", alias="AccessPolicy")
    

    @property
    def tropo_type(self) -> troposphere.backup.BackupVault:
        from troposphere.backup import BackupVault as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.backup import BackupVault as TropoT
        return resource_to_troposphere(self, TropoT)


class Framework(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html
    Properties:
        - Name: FrameworkControls
        - Name: FrameworkName
        - Name: FrameworkTags
        - Name: FrameworkDescription
    Attributes:
        - Name: CreationTime
        - Name: FrameworkStatus
        - Name: DeploymentStatus
        - Name: FrameworkArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FrameworkControls_: List['FrameworkControl'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkcontrols""", alias="FrameworkControls")
    FrameworkName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkname""", alias="FrameworkName")
    FrameworkTags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworktags""", alias="FrameworkTags")
    FrameworkDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkdescription""", alias="FrameworkDescription")
    

    @property
    def tropo_type(self) -> troposphere.backup.Framework:
        from troposphere.backup import Framework as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.backup import Framework as TropoT
        return resource_to_troposphere(self, TropoT)


class ReportPlan(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html
    Properties:
        - Name: ReportSetting
        - Name: ReportPlanDescription
        - Name: ReportPlanName
        - Name: ReportDeliveryChannel
        - Name: ReportPlanTags
    Attributes:
        - Name: ReportPlanArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ReportSetting_: 'ReportSetting' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportsetting""", alias="ReportSetting")
    ReportPlanDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplandescription""", alias="ReportPlanDescription")
    ReportPlanName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplanname""", alias="ReportPlanName")
    ReportDeliveryChannel_: 'ReportDeliveryChannel' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportdeliverychannel""", alias="ReportDeliveryChannel")
    ReportPlanTags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplantags""", alias="ReportPlanTags")
    

    @property
    def tropo_type(self) -> troposphere.backup.ReportPlan:
        from troposphere.backup import ReportPlan as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.backup import ReportPlan as TropoT
        return resource_to_troposphere(self, TropoT)

