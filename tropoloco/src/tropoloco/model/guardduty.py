from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class CFNDataSourceConfigurations(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html
    Properties:
        - Name: MalwareProtection
        - Name: S3Logs
        - Name: Kubernetes
    
    """
    
    MalwareProtection_: Optional['CFNMalwareProtectionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html#cfn-guardduty-detector-cfndatasourceconfigurations-malwareprotection""", alias="MalwareProtection")
    S3Logs_: Optional['CFNS3LogsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html#cfn-guardduty-detector-cfndatasourceconfigurations-s3logs""", alias="S3Logs")
    Kubernetes_: Optional['CFNKubernetesConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html#cfn-guardduty-detector-cfndatasourceconfigurations-kubernetes""", alias="Kubernetes")
    


    @property
    def tropo_type(self) -> troposphere.guardduty.CFNDataSourceConfigurations:
        from troposphere.guardduty import CFNDataSourceConfigurations as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CFNFeatureAdditionalConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration.html
    Properties:
        - Name: Status
        - Name: Name
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration.html#cfn-guardduty-detector-cfnfeatureadditionalconfiguration-status""", alias="Status")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnfeatureadditionalconfiguration.html#cfn-guardduty-detector-cfnfeatureadditionalconfiguration-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.guardduty.CFNFeatureAdditionalConfiguration:
        from troposphere.guardduty import CFNFeatureAdditionalConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CFNFeatureConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnfeatureconfiguration.html
    Properties:
        - Name: Status
        - Name: AdditionalConfiguration
        - Name: Name
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnfeatureconfiguration.html#cfn-guardduty-detector-cfnfeatureconfiguration-status""", alias="Status")
    AdditionalConfiguration_: Optional[List['CFNFeatureAdditionalConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnfeatureconfiguration.html#cfn-guardduty-detector-cfnfeatureconfiguration-additionalconfiguration""", alias="AdditionalConfiguration")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnfeatureconfiguration.html#cfn-guardduty-detector-cfnfeatureconfiguration-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.guardduty.CFNFeatureConfiguration:
        from troposphere.guardduty import CFNFeatureConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CFNKubernetesAuditLogsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration.html
    Properties:
        - Name: Enable
    
    """
    
    Enable_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration.html#cfn-guardduty-detector-cfnkubernetesauditlogsconfiguration-enable""", alias="Enable")
    


    @property
    def tropo_type(self) -> troposphere.guardduty.CFNKubernetesAuditLogsConfiguration:
        from troposphere.guardduty import CFNKubernetesAuditLogsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CFNKubernetesConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesconfiguration.html
    Properties:
        - Name: AuditLogs
    
    """
    
    AuditLogs_: 'CFNKubernetesAuditLogsConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesconfiguration.html#cfn-guardduty-detector-cfnkubernetesconfiguration-auditlogs""", alias="AuditLogs")
    


    @property
    def tropo_type(self) -> troposphere.guardduty.CFNKubernetesConfiguration:
        from troposphere.guardduty import CFNKubernetesConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CFNMalwareProtectionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnmalwareprotectionconfiguration.html
    Properties:
        - Name: ScanEc2InstanceWithFindings
    
    """
    
    ScanEc2InstanceWithFindings_: Optional['CFNScanEc2InstanceWithFindingsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnmalwareprotectionconfiguration.html#cfn-guardduty-detector-cfnmalwareprotectionconfiguration-scanec2instancewithfindings""", alias="ScanEc2InstanceWithFindings")
    


    @property
    def tropo_type(self) -> troposphere.guardduty.CFNMalwareProtectionConfiguration:
        from troposphere.guardduty import CFNMalwareProtectionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CFNS3LogsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html
    Properties:
        - Name: Enable
    
    """
    
    Enable_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html#cfn-guardduty-detector-cfns3logsconfiguration-enable""", alias="Enable")
    


    @property
    def tropo_type(self) -> troposphere.guardduty.CFNS3LogsConfiguration:
        from troposphere.guardduty import CFNS3LogsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CFNScanEc2InstanceWithFindingsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnscanec2instancewithfindingsconfiguration.html
    Properties:
        - Name: EbsVolumes
    
    """
    
    EbsVolumes_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnscanec2instancewithfindingsconfiguration.html#cfn-guardduty-detector-cfnscanec2instancewithfindingsconfiguration-ebsvolumes""", alias="EbsVolumes")
    


    @property
    def tropo_type(self) -> troposphere.guardduty.CFNScanEc2InstanceWithFindingsConfiguration:
        from troposphere.guardduty import CFNScanEc2InstanceWithFindingsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-tagitem.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-tagitem.html#cfn-guardduty-detector-tagitem-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-tagitem.html#cfn-guardduty-detector-tagitem-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.guardduty.TagItem:
        from troposphere.guardduty import TagItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Condition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html
    Properties:
        - Name: Equals
        - Name: LessThan
        - Name: LessThanOrEqual
        - Name: GreaterThan
        - Name: Lt
        - Name: Gte
        - Name: GreaterThanOrEqual
        - Name: Neq
        - Name: Eq
        - Name: Lte
        - Name: Gt
        - Name: NotEquals
    
    """
    
    Equals_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-equals""", alias="Equals")
    LessThan_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lessthan""", alias="LessThan")
    LessThanOrEqual_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lessthanorequal""", alias="LessThanOrEqual")
    GreaterThan_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-greaterthan""", alias="GreaterThan")
    Lt_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lt""", alias="Lt")
    Gte_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-gte""", alias="Gte")
    GreaterThanOrEqual_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-greaterthanorequal""", alias="GreaterThanOrEqual")
    Neq_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-neq""", alias="Neq")
    Eq_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-eq""", alias="Eq")
    Lte_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lte""", alias="Lte")
    Gt_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-gt""", alias="Gt")
    NotEquals_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-notequals""", alias="NotEquals")
    


    @property
    def tropo_type(self) -> troposphere.guardduty.Condition:
        from troposphere.guardduty import Condition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FindingCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html
    Properties:
        - Name: Criterion
        - Name: ItemType
    
    """
    
    Criterion_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html#cfn-guardduty-filter-findingcriteria-criterion""", alias="Criterion")
    ItemType_: Optional['Condition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html#cfn-guardduty-filter-findingcriteria-itemtype""", alias="ItemType")
    


    @property
    def tropo_type(self) -> troposphere.guardduty.FindingCriteria:
        from troposphere.guardduty import FindingCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-ipset-tagitem.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-ipset-tagitem.html#cfn-guardduty-ipset-tagitem-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-ipset-tagitem.html#cfn-guardduty-ipset-tagitem-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.guardduty.TagItem:
        from troposphere.guardduty import TagItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagItem(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-threatintelset-tagitem.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-threatintelset-tagitem.html#cfn-guardduty-threatintelset-tagitem-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-threatintelset-tagitem.html#cfn-guardduty-threatintelset-tagitem-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.guardduty.TagItem:
        from troposphere.guardduty import TagItem as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Detector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html
    Properties:
        - Name: FindingPublishingFrequency
        - Name: DataSources
        - Name: Enable
        - Name: Features
        - Name: Tags
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    FindingPublishingFrequency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-findingpublishingfrequency""", alias="FindingPublishingFrequency")
    DataSources_: Optional['CFNDataSourceConfigurations'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-datasources""", alias="DataSources")
    Enable_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-enable""", alias="Enable")
    Features_: Optional[List['CFNFeatureConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-features""", alias="Features")
    Tags_: Optional[List['TagItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.guardduty.Detector:
        from troposphere.guardduty import Detector as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.guardduty import Detector as TropoT
        return resource_to_troposphere(self, TropoT)


class Filter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html
    Properties:
        - Name: Action
        - Name: Description
        - Name: DetectorId
        - Name: FindingCriteria
        - Name: Rank
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Action_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-action""", alias="Action")
    Description_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-description""", alias="Description")
    DetectorId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-detectorid""", alias="DetectorId")
    FindingCriteria_: 'FindingCriteria' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-findingcriteria""", alias="FindingCriteria")
    Rank_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-rank""", alias="Rank")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.guardduty.Filter:
        from troposphere.guardduty import Filter as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.guardduty import Filter as TropoT
        return resource_to_troposphere(self, TropoT)


class IPSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html
    Properties:
        - Name: Format
        - Name: Activate
        - Name: DetectorId
        - Name: Tags
        - Name: Name
        - Name: Location
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Format_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-format""", alias="Format")
    Activate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-activate""", alias="Activate")
    DetectorId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-detectorid""", alias="DetectorId")
    Tags_: Optional[List['TagItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-name""", alias="Name")
    Location_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-location""", alias="Location")
    

    @property
    def tropo_type(self) -> troposphere.guardduty.IPSet:
        from troposphere.guardduty import IPSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.guardduty import IPSet as TropoT
        return resource_to_troposphere(self, TropoT)


class Master(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html
    Properties:
        - Name: DetectorId
        - Name: MasterId
        - Name: InvitationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DetectorId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-detectorid""", alias="DetectorId")
    MasterId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-masterid""", alias="MasterId")
    InvitationId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-invitationid""", alias="InvitationId")
    

    @property
    def tropo_type(self) -> troposphere.guardduty.Master:
        from troposphere.guardduty import Master as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.guardduty import Master as TropoT
        return resource_to_troposphere(self, TropoT)


class Member(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html
    Properties:
        - Name: Status
        - Name: MemberId
        - Name: Email
        - Name: Message
        - Name: DisableEmailNotification
        - Name: DetectorId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-status""", alias="Status")
    MemberId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-memberid""", alias="MemberId")
    Email_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-email""", alias="Email")
    Message_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-message""", alias="Message")
    DisableEmailNotification_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-disableemailnotification""", alias="DisableEmailNotification")
    DetectorId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-detectorid""", alias="DetectorId")
    

    @property
    def tropo_type(self) -> troposphere.guardduty.Member:
        from troposphere.guardduty import Member as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.guardduty import Member as TropoT
        return resource_to_troposphere(self, TropoT)


class ThreatIntelSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html
    Properties:
        - Name: Format
        - Name: Activate
        - Name: DetectorId
        - Name: Tags
        - Name: Name
        - Name: Location
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Format_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-format""", alias="Format")
    Activate_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-activate""", alias="Activate")
    DetectorId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-detectorid""", alias="DetectorId")
    Tags_: Optional[List['TagItem']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-name""", alias="Name")
    Location_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-location""", alias="Location")
    

    @property
    def tropo_type(self) -> troposphere.guardduty.ThreatIntelSet:
        from troposphere.guardduty import ThreatIntelSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.guardduty import ThreatIntelSet as TropoT
        return resource_to_troposphere(self, TropoT)

