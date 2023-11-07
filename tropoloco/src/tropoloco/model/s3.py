from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class PublicAccessBlockConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-publicaccessblockconfiguration.html
    Properties:
        - Name: RestrictPublicBuckets
        - Name: BlockPublicPolicy
        - Name: BlockPublicAcls
        - Name: IgnorePublicAcls
    
    """
    
    RestrictPublicBuckets_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-publicaccessblockconfiguration.html#cfn-s3-accesspoint-publicaccessblockconfiguration-restrictpublicbuckets""", alias="RestrictPublicBuckets")
    BlockPublicPolicy_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-publicaccessblockconfiguration.html#cfn-s3-accesspoint-publicaccessblockconfiguration-blockpublicpolicy""", alias="BlockPublicPolicy")
    BlockPublicAcls_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-publicaccessblockconfiguration.html#cfn-s3-accesspoint-publicaccessblockconfiguration-blockpublicacls""", alias="BlockPublicAcls")
    IgnorePublicAcls_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-publicaccessblockconfiguration.html#cfn-s3-accesspoint-publicaccessblockconfiguration-ignorepublicacls""", alias="IgnorePublicAcls")
    


    @property
    def tropo_type(self) -> troposphere.s3.PublicAccessBlockConfiguration:
        from troposphere.s3 import PublicAccessBlockConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-vpcconfiguration.html
    Properties:
        - Name: VpcId
    
    """
    
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-vpcconfiguration.html#cfn-s3-accesspoint-vpcconfiguration-vpcid""", alias="VpcId")
    


    @property
    def tropo_type(self) -> troposphere.s3.VpcConfiguration:
        from troposphere.s3 import VpcConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AbortIncompleteMultipartUpload(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-abortincompletemultipartupload.html
    Properties:
        - Name: DaysAfterInitiation
    
    """
    
    DaysAfterInitiation_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-abortincompletemultipartupload.html#cfn-s3-bucket-abortincompletemultipartupload-daysafterinitiation""", alias="DaysAfterInitiation")
    


    @property
    def tropo_type(self) -> troposphere.s3.AbortIncompleteMultipartUpload:
        from troposphere.s3 import AbortIncompleteMultipartUpload as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccelerateConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-accelerateconfiguration.html
    Properties:
        - Name: AccelerationStatus
    
    """
    
    AccelerationStatus_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-accelerateconfiguration.html#cfn-s3-bucket-accelerateconfiguration-accelerationstatus""", alias="AccelerationStatus")
    


    @property
    def tropo_type(self) -> troposphere.s3.AccelerateConfiguration:
        from troposphere.s3 import AccelerateConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessControlTranslation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-accesscontroltranslation.html
    Properties:
        - Name: Owner
    
    """
    
    Owner_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-accesscontroltranslation.html#cfn-s3-bucket-accesscontroltranslation-owner""", alias="Owner")
    


    @property
    def tropo_type(self) -> troposphere.s3.AccessControlTranslation:
        from troposphere.s3 import AccessControlTranslation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AnalyticsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-analyticsconfiguration.html
    Properties:
        - Name: Id
        - Name: Prefix
        - Name: StorageClassAnalysis
        - Name: TagFilters
    
    """
    
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-analyticsconfiguration.html#cfn-s3-bucket-analyticsconfiguration-id""", alias="Id")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-analyticsconfiguration.html#cfn-s3-bucket-analyticsconfiguration-prefix""", alias="Prefix")
    StorageClassAnalysis_: 'StorageClassAnalysis' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-analyticsconfiguration.html#cfn-s3-bucket-analyticsconfiguration-storageclassanalysis""", alias="StorageClassAnalysis")
    TagFilters_: Optional[List['TagFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-analyticsconfiguration.html#cfn-s3-bucket-analyticsconfiguration-tagfilters""", alias="TagFilters")
    


    @property
    def tropo_type(self) -> troposphere.s3.AnalyticsConfiguration:
        from troposphere.s3 import AnalyticsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BucketEncryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-bucketencryption.html
    Properties:
        - Name: ServerSideEncryptionConfiguration
    
    """
    
    ServerSideEncryptionConfiguration_: List['ServerSideEncryptionRule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-bucketencryption.html#cfn-s3-bucket-bucketencryption-serversideencryptionconfiguration""", alias="ServerSideEncryptionConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.s3.BucketEncryption:
        from troposphere.s3 import BucketEncryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CorsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors.html
    Properties:
        - Name: CorsRules
    
    """
    
    CorsRules_: List['CorsRule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors.html#cfn-s3-bucket-cors-corsrule""", alias="CorsRules")
    


    @property
    def tropo_type(self) -> troposphere.s3.CorsConfiguration:
        from troposphere.s3 import CorsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CorsRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors-corsrule.html
    Properties:
        - Name: AllowedHeaders
        - Name: AllowedMethods
        - Name: AllowedOrigins
        - Name: ExposedHeaders
        - Name: Id
        - Name: MaxAge
    
    """
    
    AllowedHeaders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors-corsrule.html#cfn-s3-bucket-cors-corsrule-allowedheaders""", alias="AllowedHeaders")
    AllowedMethods_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors-corsrule.html#cfn-s3-bucket-cors-corsrule-allowedmethods""", alias="AllowedMethods")
    AllowedOrigins_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors-corsrule.html#cfn-s3-bucket-cors-corsrule-allowedorigins""", alias="AllowedOrigins")
    ExposedHeaders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors-corsrule.html#cfn-s3-bucket-cors-corsrule-exposedheaders""", alias="ExposedHeaders")
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors-corsrule.html#cfn-s3-bucket-cors-corsrule-id""", alias="Id")
    MaxAge_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors-corsrule.html#cfn-s3-bucket-cors-corsrule-maxage""", alias="MaxAge")
    


    @property
    def tropo_type(self) -> troposphere.s3.CorsRule:
        from troposphere.s3 import CorsRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataExport(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-dataexport.html
    Properties:
        - Name: Destination
        - Name: OutputSchemaVersion
    
    """
    
    Destination_: 'Destination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-dataexport.html#cfn-s3-bucket-dataexport-destination""", alias="Destination")
    OutputSchemaVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-dataexport.html#cfn-s3-bucket-dataexport-outputschemaversion""", alias="OutputSchemaVersion")
    


    @property
    def tropo_type(self) -> troposphere.s3.DataExport:
        from troposphere.s3 import DataExport as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DefaultRetention(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-defaultretention.html
    Properties:
        - Name: Days
        - Name: Mode
        - Name: Years
    
    """
    
    Days_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-defaultretention.html#cfn-s3-bucket-defaultretention-days""", alias="Days")
    Mode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-defaultretention.html#cfn-s3-bucket-defaultretention-mode""", alias="Mode")
    Years_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-defaultretention.html#cfn-s3-bucket-defaultretention-years""", alias="Years")
    


    @property
    def tropo_type(self) -> troposphere.s3.DefaultRetention:
        from troposphere.s3 import DefaultRetention as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DeleteMarkerReplication(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-deletemarkerreplication.html
    Properties:
        - Name: Status
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-deletemarkerreplication.html#cfn-s3-bucket-deletemarkerreplication-status""", alias="Status")
    


    @property
    def tropo_type(self) -> troposphere.s3.DeleteMarkerReplication:
        from troposphere.s3 import DeleteMarkerReplication as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Destination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-destination.html
    Properties:
        - Name: BucketAccountId
        - Name: BucketArn
        - Name: Format
        - Name: Prefix
    
    """
    
    BucketAccountId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-destination.html#cfn-s3-bucket-destination-bucketaccountid""", alias="BucketAccountId")
    BucketArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-destination.html#cfn-s3-bucket-destination-bucketarn""", alias="BucketArn")
    Format_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-destination.html#cfn-s3-bucket-destination-format""", alias="Format")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-destination.html#cfn-s3-bucket-destination-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.s3.Destination:
        from troposphere.s3 import Destination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-encryptionconfiguration.html
    Properties:
        - Name: ReplicaKmsKeyID
    
    """
    
    ReplicaKmsKeyID_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-encryptionconfiguration.html#cfn-s3-bucket-encryptionconfiguration-replicakmskeyid""", alias="ReplicaKmsKeyID")
    


    @property
    def tropo_type(self) -> troposphere.s3.EncryptionConfiguration:
        from troposphere.s3 import EncryptionConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EventBridgeConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-eventbridgeconfig.html
    Properties:
        - Name: EventBridgeEnabled
    
    """
    
    EventBridgeEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-eventbridgeconfig.html#cfn-s3-bucket-eventbridgeconfiguration-eventbridgeenabled""", alias="EventBridgeEnabled")
    


    @property
    def tropo_type(self) -> troposphere.s3.EventBridgeConfiguration:
        from troposphere.s3 import EventBridgeConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FilterRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter-s3key-rules.html
    Properties:
        - Name: Name
        - Name: Value
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter-s3key-rules.html#cfn-s3-bucket-notificationconfiguraiton-config-filter-s3key-rules-name""", alias="Name")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter-s3key-rules.html#cfn-s3-bucket-notificationconfiguraiton-config-filter-s3key-rules-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.s3.FilterRule:
        from troposphere.s3 import FilterRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class IntelligentTieringConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-intelligenttieringconfiguration.html
    Properties:
        - Name: Id
        - Name: Prefix
        - Name: Status
        - Name: TagFilters
        - Name: Tierings
    
    """
    
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-intelligenttieringconfiguration.html#cfn-s3-bucket-intelligenttieringconfiguration-id""", alias="Id")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-intelligenttieringconfiguration.html#cfn-s3-bucket-intelligenttieringconfiguration-prefix""", alias="Prefix")
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-intelligenttieringconfiguration.html#cfn-s3-bucket-intelligenttieringconfiguration-status""", alias="Status")
    TagFilters_: Optional[List['TagFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-intelligenttieringconfiguration.html#cfn-s3-bucket-intelligenttieringconfiguration-tagfilters""", alias="TagFilters")
    Tierings_: List['Tiering'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-intelligenttieringconfiguration.html#cfn-s3-bucket-intelligenttieringconfiguration-tierings""", alias="Tierings")
    


    @property
    def tropo_type(self) -> troposphere.s3.IntelligentTieringConfiguration:
        from troposphere.s3 import IntelligentTieringConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InventoryConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html
    Properties:
        - Name: Destination
        - Name: Enabled
        - Name: Id
        - Name: IncludedObjectVersions
        - Name: OptionalFields
        - Name: Prefix
        - Name: ScheduleFrequency
    
    """
    
    Destination_: 'Destination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-destination""", alias="Destination")
    Enabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-enabled""", alias="Enabled")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-id""", alias="Id")
    IncludedObjectVersions_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-includedobjectversions""", alias="IncludedObjectVersions")
    OptionalFields_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-optionalfields""", alias="OptionalFields")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-prefix""", alias="Prefix")
    ScheduleFrequency_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-inventoryconfiguration.html#cfn-s3-bucket-inventoryconfiguration-schedulefrequency""", alias="ScheduleFrequency")
    


    @property
    def tropo_type(self) -> troposphere.s3.InventoryConfiguration:
        from troposphere.s3 import InventoryConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LambdaConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-lambdaconfig.html
    Properties:
        - Name: Event
        - Name: Filter
        - Name: Function
    
    """
    
    Event_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-lambdaconfig.html#cfn-s3-bucket-notificationconfig-lambdaconfig-event""", alias="Event")
    Filter_: Optional['NotificationFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-lambdaconfig.html#cfn-s3-bucket-notificationconfig-lambdaconfig-filter""", alias="Filter")
    Function_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-lambdaconfig.html#cfn-s3-bucket-notificationconfig-lambdaconfig-function""", alias="Function")
    


    @property
    def tropo_type(self) -> troposphere.s3.LambdaConfiguration:
        from troposphere.s3 import LambdaConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LifecycleConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig.html
    Properties:
        - Name: Rules
    
    """
    
    Rules_: List['Rule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig.html#cfn-s3-bucket-lifecycleconfig-rules""", alias="Rules")
    


    @property
    def tropo_type(self) -> troposphere.s3.LifecycleConfiguration:
        from troposphere.s3 import LifecycleConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggingConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-loggingconfig.html
    Properties:
        - Name: DestinationBucketName
        - Name: LogFilePrefix
    
    """
    
    DestinationBucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-loggingconfig.html#cfn-s3-bucket-loggingconfig-destinationbucketname""", alias="DestinationBucketName")
    LogFilePrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-loggingconfig.html#cfn-s3-bucket-loggingconfig-logfileprefix""", alias="LogFilePrefix")
    


    @property
    def tropo_type(self) -> troposphere.s3.LoggingConfiguration:
        from troposphere.s3 import LoggingConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Metrics(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-metrics.html
    Properties:
        - Name: EventThreshold
        - Name: Status
    
    """
    
    EventThreshold_: Optional['ReplicationTimeValue'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-metrics.html#cfn-s3-bucket-metrics-eventthreshold""", alias="EventThreshold")
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-metrics.html#cfn-s3-bucket-metrics-status""", alias="Status")
    


    @property
    def tropo_type(self) -> troposphere.s3.Metrics:
        from troposphere.s3 import Metrics as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MetricsConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-metricsconfiguration.html
    Properties:
        - Name: AccessPointArn
        - Name: Id
        - Name: Prefix
        - Name: TagFilters
    
    """
    
    AccessPointArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-metricsconfiguration.html#cfn-s3-bucket-metricsconfiguration-accesspointarn""", alias="AccessPointArn")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-metricsconfiguration.html#cfn-s3-bucket-metricsconfiguration-id""", alias="Id")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-metricsconfiguration.html#cfn-s3-bucket-metricsconfiguration-prefix""", alias="Prefix")
    TagFilters_: Optional[List['TagFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-metricsconfiguration.html#cfn-s3-bucket-metricsconfiguration-tagfilters""", alias="TagFilters")
    


    @property
    def tropo_type(self) -> troposphere.s3.MetricsConfiguration:
        from troposphere.s3 import MetricsConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NoncurrentVersionExpiration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-noncurrentversionexpiration.html
    Properties:
        - Name: NewerNoncurrentVersions
        - Name: NoncurrentDays
    
    """
    
    NewerNoncurrentVersions_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-noncurrentversionexpiration.html#cfn-s3-bucket-lifecycleconfig-rule-noncurrentversionexpiration-newernoncurrentversions""", alias="NewerNoncurrentVersions")
    NoncurrentDays_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-noncurrentversionexpiration.html#cfn-s3-bucket-lifecycleconfig-rule-noncurrentversionexpiration-noncurrentdays""", alias="NoncurrentDays")
    


    @property
    def tropo_type(self) -> troposphere.s3.NoncurrentVersionExpiration:
        from troposphere.s3 import NoncurrentVersionExpiration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NoncurrentVersionTransition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-noncurrentversiontransition.html
    Properties:
        - Name: NewerNoncurrentVersions
        - Name: StorageClass
        - Name: TransitionInDays
    
    """
    
    NewerNoncurrentVersions_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-noncurrentversiontransition.html#cfn-s3-bucket-lifecycleconfig-rule-noncurrentversiontransition-newernoncurrentversions""", alias="NewerNoncurrentVersions")
    StorageClass_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-noncurrentversiontransition.html#cfn-s3-bucket-lifecycleconfig-rule-noncurrentversiontransition-storageclass""", alias="StorageClass")
    TransitionInDays_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-noncurrentversiontransition.html#cfn-s3-bucket-lifecycleconfig-rule-noncurrentversiontransition-transitionindays""", alias="TransitionInDays")
    


    @property
    def tropo_type(self) -> troposphere.s3.NoncurrentVersionTransition:
        from troposphere.s3 import NoncurrentVersionTransition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig.html
    Properties:
        - Name: EventBridgeConfiguration
        - Name: LambdaConfigurations
        - Name: QueueConfigurations
        - Name: TopicConfigurations
    
    """
    
    EventBridgeConfiguration_: Optional['EventBridgeConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig.html#cfn-s3-bucket-notificationconfig-eventbridgeconfig""", alias="EventBridgeConfiguration")
    LambdaConfigurations_: Optional[List['LambdaConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig.html#cfn-s3-bucket-notificationconfig-lambdaconfig""", alias="LambdaConfigurations")
    QueueConfigurations_: Optional[List['QueueConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig.html#cfn-s3-bucket-notificationconfig-queueconfig""", alias="QueueConfigurations")
    TopicConfigurations_: Optional[List['TopicConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig.html#cfn-s3-bucket-notificationconfig-topicconfig""", alias="TopicConfigurations")
    


    @property
    def tropo_type(self) -> troposphere.s3.NotificationConfiguration:
        from troposphere.s3 import NotificationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter.html
    Properties:
        - Name: S3Key
    
    """
    
    S3Key_: 'S3KeyFilter' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter.html#cfn-s3-bucket-notificationconfiguraiton-config-filter-s3key""", alias="S3Key")
    


    @property
    def tropo_type(self) -> troposphere.s3.NotificationFilter:
        from troposphere.s3 import NotificationFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ObjectLockConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-objectlockconfiguration.html
    Properties:
        - Name: ObjectLockEnabled
        - Name: Rule
    
    """
    
    ObjectLockEnabled_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-objectlockconfiguration.html#cfn-s3-bucket-objectlockconfiguration-objectlockenabled""", alias="ObjectLockEnabled")
    Rule_: Optional['ObjectLockRule'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-objectlockconfiguration.html#cfn-s3-bucket-objectlockconfiguration-rule""", alias="Rule")
    


    @property
    def tropo_type(self) -> troposphere.s3.ObjectLockConfiguration:
        from troposphere.s3 import ObjectLockConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ObjectLockRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-objectlockrule.html
    Properties:
        - Name: DefaultRetention
    
    """
    
    DefaultRetention_: Optional['DefaultRetention'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-objectlockrule.html#cfn-s3-bucket-objectlockrule-defaultretention""", alias="DefaultRetention")
    


    @property
    def tropo_type(self) -> troposphere.s3.ObjectLockRule:
        from troposphere.s3 import ObjectLockRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OwnershipControls(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrols.html
    Properties:
        - Name: Rules
    
    """
    
    Rules_: List['OwnershipControlsRule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrols.html#cfn-s3-bucket-ownershipcontrols-rules""", alias="Rules")
    


    @property
    def tropo_type(self) -> troposphere.s3.OwnershipControls:
        from troposphere.s3 import OwnershipControls as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OwnershipControlsRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrolsrule.html
    Properties:
        - Name: ObjectOwnership
    
    """
    
    ObjectOwnership_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrolsrule.html#cfn-s3-bucket-ownershipcontrolsrule-objectownership""", alias="ObjectOwnership")
    


    @property
    def tropo_type(self) -> troposphere.s3.OwnershipControlsRule:
        from troposphere.s3 import OwnershipControlsRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PublicAccessBlockConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-publicaccessblockconfiguration.html
    Properties:
        - Name: BlockPublicAcls
        - Name: BlockPublicPolicy
        - Name: IgnorePublicAcls
        - Name: RestrictPublicBuckets
    
    """
    
    BlockPublicAcls_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-publicaccessblockconfiguration.html#cfn-s3-bucket-publicaccessblockconfiguration-blockpublicacls""", alias="BlockPublicAcls")
    BlockPublicPolicy_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-publicaccessblockconfiguration.html#cfn-s3-bucket-publicaccessblockconfiguration-blockpublicpolicy""", alias="BlockPublicPolicy")
    IgnorePublicAcls_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-publicaccessblockconfiguration.html#cfn-s3-bucket-publicaccessblockconfiguration-ignorepublicacls""", alias="IgnorePublicAcls")
    RestrictPublicBuckets_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-publicaccessblockconfiguration.html#cfn-s3-bucket-publicaccessblockconfiguration-restrictpublicbuckets""", alias="RestrictPublicBuckets")
    


    @property
    def tropo_type(self) -> troposphere.s3.PublicAccessBlockConfiguration:
        from troposphere.s3 import PublicAccessBlockConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class QueueConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-queueconfig.html
    Properties:
        - Name: Event
        - Name: Filter
        - Name: Queue
    
    """
    
    Event_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-queueconfig.html#cfn-s3-bucket-notificationconfig-queueconfig-event""", alias="Event")
    Filter_: Optional['NotificationFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-queueconfig.html#cfn-s3-bucket-notificationconfig-queueconfig-filter""", alias="Filter")
    Queue_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-queueconfig.html#cfn-s3-bucket-notificationconfig-queueconfig-queue""", alias="Queue")
    


    @property
    def tropo_type(self) -> troposphere.s3.QueueConfiguration:
        from troposphere.s3 import QueueConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RedirectAllRequestsTo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-redirectallrequeststo.html
    Properties:
        - Name: HostName
        - Name: Protocol
    
    """
    
    HostName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-redirectallrequeststo.html#cfn-s3-websiteconfiguration-redirectallrequeststo-hostname""", alias="HostName")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-redirectallrequeststo.html#cfn-s3-websiteconfiguration-redirectallrequeststo-protocol""", alias="Protocol")
    


    @property
    def tropo_type(self) -> troposphere.s3.RedirectAllRequestsTo:
        from troposphere.s3 import RedirectAllRequestsTo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RedirectRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules-redirectrule.html
    Properties:
        - Name: HostName
        - Name: HttpRedirectCode
        - Name: Protocol
        - Name: ReplaceKeyPrefixWith
        - Name: ReplaceKeyWith
    
    """
    
    HostName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules-redirectrule.html#cfn-s3-websiteconfiguration-redirectrule-hostname""", alias="HostName")
    HttpRedirectCode_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules-redirectrule.html#cfn-s3-websiteconfiguration-redirectrule-httpredirectcode""", alias="HttpRedirectCode")
    Protocol_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules-redirectrule.html#cfn-s3-websiteconfiguration-redirectrule-protocol""", alias="Protocol")
    ReplaceKeyPrefixWith_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules-redirectrule.html#cfn-s3-websiteconfiguration-redirectrule-replacekeyprefixwith""", alias="ReplaceKeyPrefixWith")
    ReplaceKeyWith_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules-redirectrule.html#cfn-s3-websiteconfiguration-redirectrule-replacekeywith""", alias="ReplaceKeyWith")
    


    @property
    def tropo_type(self) -> troposphere.s3.RedirectRule:
        from troposphere.s3 import RedirectRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicaModifications(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicamodifications.html
    Properties:
        - Name: Status
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicamodifications.html#cfn-s3-bucket-replicamodifications-status""", alias="Status")
    


    @property
    def tropo_type(self) -> troposphere.s3.ReplicaModifications:
        from troposphere.s3 import ReplicaModifications as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration.html
    Properties:
        - Name: Role
        - Name: Rules
    
    """
    
    Role_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration.html#cfn-s3-bucket-replicationconfiguration-role""", alias="Role")
    Rules_: List['ReplicationRule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration.html#cfn-s3-bucket-replicationconfiguration-rules""", alias="Rules")
    


    @property
    def tropo_type(self) -> troposphere.s3.ReplicationConfiguration:
        from troposphere.s3 import ReplicationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules-destination.html
    Properties:
        - Name: AccessControlTranslation
        - Name: Account
        - Name: Bucket
        - Name: EncryptionConfiguration
        - Name: Metrics
        - Name: ReplicationTime
        - Name: StorageClass
    
    """
    
    AccessControlTranslation_: Optional['AccessControlTranslation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules-destination.html#cfn-s3-bucket-replicationdestination-accesscontroltranslation""", alias="AccessControlTranslation")
    Account_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules-destination.html#cfn-s3-bucket-replicationdestination-account""", alias="Account")
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules-destination.html#cfn-s3-bucket-replicationconfiguration-rules-destination-bucket""", alias="Bucket")
    EncryptionConfiguration_: Optional['EncryptionConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules-destination.html#cfn-s3-bucket-replicationdestination-encryptionconfiguration""", alias="EncryptionConfiguration")
    Metrics_: Optional['Metrics'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules-destination.html#cfn-s3-bucket-replicationdestination-metrics""", alias="Metrics")
    ReplicationTime_: Optional['ReplicationTime'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules-destination.html#cfn-s3-bucket-replicationdestination-replicationtime""", alias="ReplicationTime")
    StorageClass_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules-destination.html#cfn-s3-bucket-replicationconfiguration-rules-destination-storageclass""", alias="StorageClass")
    


    @property
    def tropo_type(self) -> troposphere.s3.ReplicationDestination:
        from troposphere.s3 import ReplicationDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules.html
    Properties:
        - Name: DeleteMarkerReplication
        - Name: Destination
        - Name: Filter
        - Name: Id
        - Name: Prefix
        - Name: Priority
        - Name: SourceSelectionCriteria
        - Name: Status
    
    """
    
    DeleteMarkerReplication_: Optional['DeleteMarkerReplication'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules.html#cfn-s3-bucket-replicationrule-deletemarkerreplication""", alias="DeleteMarkerReplication")
    Destination_: 'ReplicationDestination' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules.html#cfn-s3-bucket-replicationconfiguration-rules-destination""", alias="Destination")
    Filter_: Optional['ReplicationRuleFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules.html#cfn-s3-bucket-replicationrule-filter""", alias="Filter")
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules.html#cfn-s3-bucket-replicationconfiguration-rules-id""", alias="Id")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules.html#cfn-s3-bucket-replicationconfiguration-rules-prefix""", alias="Prefix")
    Priority_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules.html#cfn-s3-bucket-replicationrule-priority""", alias="Priority")
    SourceSelectionCriteria_: Optional['SourceSelectionCriteria'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules.html#cfn-s3-bucket-replicationrule-sourceselectioncriteria""", alias="SourceSelectionCriteria")
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationconfiguration-rules.html#cfn-s3-bucket-replicationconfiguration-rules-status""", alias="Status")
    


    @property
    def tropo_type(self) -> troposphere.s3.ReplicationRule:
        from troposphere.s3 import ReplicationRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationRuleAndOperator(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationruleandoperator.html
    Properties:
        - Name: Prefix
        - Name: TagFilters
    
    """
    
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationruleandoperator.html#cfn-s3-bucket-replicationruleandoperator-prefix""", alias="Prefix")
    TagFilters_: Optional[List['TagFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationruleandoperator.html#cfn-s3-bucket-replicationruleandoperator-tagfilters""", alias="TagFilters")
    


    @property
    def tropo_type(self) -> troposphere.s3.ReplicationRuleAndOperator:
        from troposphere.s3 import ReplicationRuleAndOperator as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationRuleFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationrulefilter.html
    Properties:
        - Name: And
        - Name: Prefix
        - Name: TagFilter
    
    """
    
    And_: Optional['ReplicationRuleAndOperator'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationrulefilter.html#cfn-s3-bucket-replicationrulefilter-and""", alias="And")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationrulefilter.html#cfn-s3-bucket-replicationrulefilter-prefix""", alias="Prefix")
    TagFilter_: Optional['TagFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationrulefilter.html#cfn-s3-bucket-replicationrulefilter-tagfilter""", alias="TagFilter")
    


    @property
    def tropo_type(self) -> troposphere.s3.ReplicationRuleFilter:
        from troposphere.s3 import ReplicationRuleFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationTime(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationtime.html
    Properties:
        - Name: Status
        - Name: Time
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationtime.html#cfn-s3-bucket-replicationtime-status""", alias="Status")
    Time_: 'ReplicationTimeValue' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationtime.html#cfn-s3-bucket-replicationtime-time""", alias="Time")
    


    @property
    def tropo_type(self) -> troposphere.s3.ReplicationTime:
        from troposphere.s3 import ReplicationTime as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ReplicationTimeValue(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationtimevalue.html
    Properties:
        - Name: Minutes
    
    """
    
    Minutes_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-replicationtimevalue.html#cfn-s3-bucket-replicationtimevalue-minutes""", alias="Minutes")
    


    @property
    def tropo_type(self) -> troposphere.s3.ReplicationTimeValue:
        from troposphere.s3 import ReplicationTimeValue as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RoutingRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html
    Properties:
        - Name: RedirectRule
        - Name: RoutingRuleCondition
    
    """
    
    RedirectRule_: 'RedirectRule' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html#cfn-s3-websiteconfiguration-routingrules-redirectrule""", alias="RedirectRule")
    RoutingRuleCondition_: Optional['RoutingRuleCondition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html#cfn-s3-websiteconfiguration-routingrules-routingrulecondition""", alias="RoutingRuleCondition")
    


    @property
    def tropo_type(self) -> troposphere.s3.RoutingRule:
        from troposphere.s3 import RoutingRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RoutingRuleCondition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules-routingrulecondition.html
    Properties:
        - Name: HttpErrorCodeReturnedEquals
        - Name: KeyPrefixEquals
    
    """
    
    HttpErrorCodeReturnedEquals_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules-routingrulecondition.html#cfn-s3-websiteconfiguration-routingrules-routingrulecondition-httperrorcodereturnedequals""", alias="HttpErrorCodeReturnedEquals")
    KeyPrefixEquals_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules-routingrulecondition.html#cfn-s3-websiteconfiguration-routingrules-routingrulecondition-keyprefixequals""", alias="KeyPrefixEquals")
    


    @property
    def tropo_type(self) -> troposphere.s3.RoutingRuleCondition:
        from troposphere.s3 import RoutingRuleCondition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html
    Properties:
        - Name: AbortIncompleteMultipartUpload
        - Name: ExpirationDate
        - Name: ExpirationInDays
        - Name: ExpiredObjectDeleteMarker
        - Name: Id
        - Name: NoncurrentVersionExpiration
        - Name: NoncurrentVersionExpirationInDays
        - Name: NoncurrentVersionTransition
        - Name: NoncurrentVersionTransitions
        - Name: ObjectSizeGreaterThan
        - Name: ObjectSizeLessThan
        - Name: Prefix
        - Name: Status
        - Name: TagFilters
        - Name: Transition
        - Name: Transitions
    
    """
    
    AbortIncompleteMultipartUpload_: Optional['AbortIncompleteMultipartUpload'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-rule-abortincompletemultipartupload""", alias="AbortIncompleteMultipartUpload")
    ExpirationDate_: Optional[datetime.datetime] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-lifecycleconfig-rule-expirationdate""", alias="ExpirationDate")
    ExpirationInDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-lifecycleconfig-rule-expirationindays""", alias="ExpirationInDays")
    ExpiredObjectDeleteMarker_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-rule-expiredobjectdeletemarker""", alias="ExpiredObjectDeleteMarker")
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-lifecycleconfig-rule-id""", alias="Id")
    NoncurrentVersionExpiration_: Optional['NoncurrentVersionExpiration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-lifecycleconfig-rule-noncurrentversionexpiration""", alias="NoncurrentVersionExpiration")
    NoncurrentVersionExpirationInDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-lifecycleconfig-rule-noncurrentversionexpirationindays""", alias="NoncurrentVersionExpirationInDays")
    NoncurrentVersionTransition_: Optional['NoncurrentVersionTransition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-lifecycleconfig-rule-noncurrentversiontransition""", alias="NoncurrentVersionTransition")
    NoncurrentVersionTransitions_: Optional[List['NoncurrentVersionTransition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-lifecycleconfig-rule-noncurrentversiontransitions""", alias="NoncurrentVersionTransitions")
    ObjectSizeGreaterThan_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-lifecycleconfig-rule-objectsizegreaterthan""", alias="ObjectSizeGreaterThan")
    ObjectSizeLessThan_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-lifecycleconfig-rule-objectsizelessthan""", alias="ObjectSizeLessThan")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-lifecycleconfig-rule-prefix""", alias="Prefix")
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-lifecycleconfig-rule-status""", alias="Status")
    TagFilters_: Optional[List['TagFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-rule-tagfilters""", alias="TagFilters")
    Transition_: Optional['Transition'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-lifecycleconfig-rule-transition""", alias="Transition")
    Transitions_: Optional[List['Transition']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule.html#cfn-s3-bucket-lifecycleconfig-rule-transitions""", alias="Transitions")
    


    @property
    def tropo_type(self) -> troposphere.s3.Rule:
        from troposphere.s3 import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3KeyFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter-s3key.html
    Properties:
        - Name: Rules
    
    """
    
    Rules_: List['FilterRule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter-s3key.html#cfn-s3-bucket-notificationconfiguraiton-config-filter-s3key-rules""", alias="Rules")
    


    @property
    def tropo_type(self) -> troposphere.s3.S3KeyFilter:
        from troposphere.s3 import S3KeyFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServerSideEncryptionByDefault(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionbydefault.html
    Properties:
        - Name: KMSMasterKeyID
        - Name: SSEAlgorithm
    
    """
    
    KMSMasterKeyID_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionbydefault.html#cfn-s3-bucket-serversideencryptionbydefault-kmsmasterkeyid""", alias="KMSMasterKeyID")
    SSEAlgorithm_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionbydefault.html#cfn-s3-bucket-serversideencryptionbydefault-ssealgorithm""", alias="SSEAlgorithm")
    


    @property
    def tropo_type(self) -> troposphere.s3.ServerSideEncryptionByDefault:
        from troposphere.s3 import ServerSideEncryptionByDefault as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ServerSideEncryptionRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionrule.html
    Properties:
        - Name: BucketKeyEnabled
        - Name: ServerSideEncryptionByDefault
    
    """
    
    BucketKeyEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionrule.html#cfn-s3-bucket-serversideencryptionrule-bucketkeyenabled""", alias="BucketKeyEnabled")
    ServerSideEncryptionByDefault_: Optional['ServerSideEncryptionByDefault'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionrule.html#cfn-s3-bucket-serversideencryptionrule-serversideencryptionbydefault""", alias="ServerSideEncryptionByDefault")
    


    @property
    def tropo_type(self) -> troposphere.s3.ServerSideEncryptionRule:
        from troposphere.s3 import ServerSideEncryptionRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SourceSelectionCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-sourceselectioncriteria.html
    Properties:
        - Name: ReplicaModifications
        - Name: SseKmsEncryptedObjects
    
    """
    
    ReplicaModifications_: Optional['ReplicaModifications'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-sourceselectioncriteria.html#cfn-s3-bucket-sourceselectioncriteria-replicamodifications""", alias="ReplicaModifications")
    SseKmsEncryptedObjects_: Optional['SseKmsEncryptedObjects'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-sourceselectioncriteria.html#cfn-s3-bucket-sourceselectioncriteria-ssekmsencryptedobjects""", alias="SseKmsEncryptedObjects")
    


    @property
    def tropo_type(self) -> troposphere.s3.SourceSelectionCriteria:
        from troposphere.s3 import SourceSelectionCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SseKmsEncryptedObjects(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ssekmsencryptedobjects.html
    Properties:
        - Name: Status
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ssekmsencryptedobjects.html#cfn-s3-bucket-ssekmsencryptedobjects-status""", alias="Status")
    


    @property
    def tropo_type(self) -> troposphere.s3.SseKmsEncryptedObjects:
        from troposphere.s3 import SseKmsEncryptedObjects as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StorageClassAnalysis(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-storageclassanalysis.html
    Properties:
        - Name: DataExport
    
    """
    
    DataExport_: Optional['DataExport'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-storageclassanalysis.html#cfn-s3-bucket-storageclassanalysis-dataexport""", alias="DataExport")
    


    @property
    def tropo_type(self) -> troposphere.s3.StorageClassAnalysis:
        from troposphere.s3 import StorageClassAnalysis as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TagFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-tagfilter.html
    Properties:
        - Name: Key
        - Name: Value
    
    """
    
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-tagfilter.html#cfn-s3-bucket-tagfilter-key""", alias="Key")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-tagfilter.html#cfn-s3-bucket-tagfilter-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.s3.TagFilter:
        from troposphere.s3 import TagFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Tiering(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-tiering.html
    Properties:
        - Name: AccessTier
        - Name: Days
    
    """
    
    AccessTier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-tiering.html#cfn-s3-bucket-tiering-accesstier""", alias="AccessTier")
    Days_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-tiering.html#cfn-s3-bucket-tiering-days""", alias="Days")
    


    @property
    def tropo_type(self) -> troposphere.s3.Tiering:
        from troposphere.s3 import Tiering as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TopicConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-topicconfig.html
    Properties:
        - Name: Event
        - Name: Filter
        - Name: Topic
    
    """
    
    Event_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-topicconfig.html#cfn-s3-bucket-notificationconfig-topicconfig-event""", alias="Event")
    Filter_: Optional['NotificationFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-topicconfig.html#cfn-s3-bucket-notificationconfig-topicconfig-filter""", alias="Filter")
    Topic_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-topicconfig.html#cfn-s3-bucket-notificationconfig-topicconfig-topic""", alias="Topic")
    


    @property
    def tropo_type(self) -> troposphere.s3.TopicConfiguration:
        from troposphere.s3 import TopicConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Transition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-transition.html
    Properties:
        - Name: StorageClass
        - Name: TransitionDate
        - Name: TransitionInDays
    
    """
    
    StorageClass_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-transition.html#cfn-s3-bucket-lifecycleconfig-rule-transition-storageclass""", alias="StorageClass")
    TransitionDate_: Optional[datetime.datetime] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-transition.html#cfn-s3-bucket-lifecycleconfig-rule-transition-transitiondate""", alias="TransitionDate")
    TransitionInDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-transition.html#cfn-s3-bucket-lifecycleconfig-rule-transition-transitionindays""", alias="TransitionInDays")
    


    @property
    def tropo_type(self) -> troposphere.s3.Transition:
        from troposphere.s3 import Transition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VersioningConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-versioningconfig.html
    Properties:
        - Name: Status
    
    """
    
    Status_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-versioningconfig.html#cfn-s3-bucket-versioningconfig-status""", alias="Status")
    


    @property
    def tropo_type(self) -> troposphere.s3.VersioningConfiguration:
        from troposphere.s3 import VersioningConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class WebsiteConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration.html
    Properties:
        - Name: ErrorDocument
        - Name: IndexDocument
        - Name: RedirectAllRequestsTo
        - Name: RoutingRules
    
    """
    
    ErrorDocument_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration.html#cfn-s3-websiteconfiguration-errordocument""", alias="ErrorDocument")
    IndexDocument_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration.html#cfn-s3-websiteconfiguration-indexdocument""", alias="IndexDocument")
    RedirectAllRequestsTo_: Optional['RedirectAllRequestsTo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration.html#cfn-s3-websiteconfiguration-redirectallrequeststo""", alias="RedirectAllRequestsTo")
    RoutingRules_: Optional[List['RoutingRule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration.html#cfn-s3-websiteconfiguration-routingrules""", alias="RoutingRules")
    


    @property
    def tropo_type(self) -> troposphere.s3.WebsiteConfiguration:
        from troposphere.s3 import WebsiteConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PublicAccessBlockConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.html
    Properties:
        - Name: RestrictPublicBuckets
        - Name: BlockPublicPolicy
        - Name: BlockPublicAcls
        - Name: IgnorePublicAcls
    
    """
    
    RestrictPublicBuckets_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.html#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration-restrictpublicbuckets""", alias="RestrictPublicBuckets")
    BlockPublicPolicy_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.html#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration-blockpublicpolicy""", alias="BlockPublicPolicy")
    BlockPublicAcls_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.html#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration-blockpublicacls""", alias="BlockPublicAcls")
    IgnorePublicAcls_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.html#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration-ignorepublicacls""", alias="IgnorePublicAcls")
    


    @property
    def tropo_type(self) -> troposphere.s3.PublicAccessBlockConfiguration:
        from troposphere.s3 import PublicAccessBlockConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Region(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-region.html
    Properties:
        - Name: Bucket
        - Name: BucketAccountId
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-region.html#cfn-s3-multiregionaccesspoint-region-bucket""", alias="Bucket")
    BucketAccountId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-region.html#cfn-s3-multiregionaccesspoint-region-bucketaccountid""", alias="BucketAccountId")
    


    @property
    def tropo_type(self) -> troposphere.s3.Region:
        from troposphere.s3 import Region as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PolicyStatus(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspointpolicy-policystatus.html
    Properties:
        - Name: IsPublic
    
    """
    
    IsPublic_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspointpolicy-policystatus.html#cfn-s3-multiregionaccesspointpolicy-policystatus-ispublic""", alias="IsPublic")
    


    @property
    def tropo_type(self) -> troposphere.s3.PolicyStatus:
        from troposphere.s3 import PolicyStatus as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccountLevel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-accountlevel.html
    Properties:
        - Name: AdvancedDataProtectionMetrics
        - Name: StorageLensGroupLevel
        - Name: ActivityMetrics
        - Name: BucketLevel
        - Name: AdvancedCostOptimizationMetrics
        - Name: DetailedStatusCodesMetrics
    
    """
    
    AdvancedDataProtectionMetrics_: Optional['AdvancedDataProtectionMetrics'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-accountlevel.html#cfn-s3-storagelens-accountlevel-advanceddataprotectionmetrics""", alias="AdvancedDataProtectionMetrics")
    StorageLensGroupLevel_: Optional['StorageLensGroupLevel'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-accountlevel.html#cfn-s3-storagelens-accountlevel-storagelensgrouplevel""", alias="StorageLensGroupLevel")
    ActivityMetrics_: Optional['ActivityMetrics'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-accountlevel.html#cfn-s3-storagelens-accountlevel-activitymetrics""", alias="ActivityMetrics")
    BucketLevel_: 'BucketLevel' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-accountlevel.html#cfn-s3-storagelens-accountlevel-bucketlevel""", alias="BucketLevel")
    AdvancedCostOptimizationMetrics_: Optional['AdvancedCostOptimizationMetrics'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-accountlevel.html#cfn-s3-storagelens-accountlevel-advancedcostoptimizationmetrics""", alias="AdvancedCostOptimizationMetrics")
    DetailedStatusCodesMetrics_: Optional['DetailedStatusCodesMetrics'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-accountlevel.html#cfn-s3-storagelens-accountlevel-detailedstatuscodesmetrics""", alias="DetailedStatusCodesMetrics")
    


    @property
    def tropo_type(self) -> troposphere.s3.AccountLevel:
        from troposphere.s3 import AccountLevel as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ActivityMetrics(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-activitymetrics.html
    Properties:
        - Name: IsEnabled
    
    """
    
    IsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-activitymetrics.html#cfn-s3-storagelens-activitymetrics-isenabled""", alias="IsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.s3.ActivityMetrics:
        from troposphere.s3 import ActivityMetrics as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AdvancedCostOptimizationMetrics(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-advancedcostoptimizationmetrics.html
    Properties:
        - Name: IsEnabled
    
    """
    
    IsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-advancedcostoptimizationmetrics.html#cfn-s3-storagelens-advancedcostoptimizationmetrics-isenabled""", alias="IsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.s3.AdvancedCostOptimizationMetrics:
        from troposphere.s3 import AdvancedCostOptimizationMetrics as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AdvancedDataProtectionMetrics(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-advanceddataprotectionmetrics.html
    Properties:
        - Name: IsEnabled
    
    """
    
    IsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-advanceddataprotectionmetrics.html#cfn-s3-storagelens-advanceddataprotectionmetrics-isenabled""", alias="IsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.s3.AdvancedDataProtectionMetrics:
        from troposphere.s3 import AdvancedDataProtectionMetrics as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AwsOrg(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-awsorg.html
    Properties:
        - Name: Arn
    
    """
    
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-awsorg.html#cfn-s3-storagelens-awsorg-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.s3.AwsOrg:
        from troposphere.s3 import AwsOrg as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BucketLevel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-bucketlevel.html
    Properties:
        - Name: AdvancedDataProtectionMetrics
        - Name: PrefixLevel
        - Name: ActivityMetrics
        - Name: AdvancedCostOptimizationMetrics
        - Name: DetailedStatusCodesMetrics
    
    """
    
    AdvancedDataProtectionMetrics_: Optional['AdvancedDataProtectionMetrics'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-bucketlevel.html#cfn-s3-storagelens-bucketlevel-advanceddataprotectionmetrics""", alias="AdvancedDataProtectionMetrics")
    PrefixLevel_: Optional['PrefixLevel'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-bucketlevel.html#cfn-s3-storagelens-bucketlevel-prefixlevel""", alias="PrefixLevel")
    ActivityMetrics_: Optional['ActivityMetrics'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-bucketlevel.html#cfn-s3-storagelens-bucketlevel-activitymetrics""", alias="ActivityMetrics")
    AdvancedCostOptimizationMetrics_: Optional['AdvancedCostOptimizationMetrics'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-bucketlevel.html#cfn-s3-storagelens-bucketlevel-advancedcostoptimizationmetrics""", alias="AdvancedCostOptimizationMetrics")
    DetailedStatusCodesMetrics_: Optional['DetailedStatusCodesMetrics'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-bucketlevel.html#cfn-s3-storagelens-bucketlevel-detailedstatuscodesmetrics""", alias="DetailedStatusCodesMetrics")
    


    @property
    def tropo_type(self) -> troposphere.s3.BucketLevel:
        from troposphere.s3 import BucketLevel as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class BucketsAndRegions(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-bucketsandregions.html
    Properties:
        - Name: Regions
        - Name: Buckets
    
    """
    
    Regions_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-bucketsandregions.html#cfn-s3-storagelens-bucketsandregions-regions""", alias="Regions")
    Buckets_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-bucketsandregions.html#cfn-s3-storagelens-bucketsandregions-buckets""", alias="Buckets")
    


    @property
    def tropo_type(self) -> troposphere.s3.BucketsAndRegions:
        from troposphere.s3 import BucketsAndRegions as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchMetrics(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-cloudwatchmetrics.html
    Properties:
        - Name: IsEnabled
    
    """
    
    IsEnabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-cloudwatchmetrics.html#cfn-s3-storagelens-cloudwatchmetrics-isenabled""", alias="IsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.s3.CloudWatchMetrics:
        from troposphere.s3 import CloudWatchMetrics as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataExport(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-dataexport.html
    Properties:
        - Name: S3BucketDestination
        - Name: CloudWatchMetrics
    
    """
    
    S3BucketDestination_: Optional['S3BucketDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-dataexport.html#cfn-s3-storagelens-dataexport-s3bucketdestination""", alias="S3BucketDestination")
    CloudWatchMetrics_: Optional['CloudWatchMetrics'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-dataexport.html#cfn-s3-storagelens-dataexport-cloudwatchmetrics""", alias="CloudWatchMetrics")
    


    @property
    def tropo_type(self) -> troposphere.s3.DataExport:
        from troposphere.s3 import DataExport as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DetailedStatusCodesMetrics(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-detailedstatuscodesmetrics.html
    Properties:
        - Name: IsEnabled
    
    """
    
    IsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-detailedstatuscodesmetrics.html#cfn-s3-storagelens-detailedstatuscodesmetrics-isenabled""", alias="IsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.s3.DetailedStatusCodesMetrics:
        from troposphere.s3 import DetailedStatusCodesMetrics as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Encryption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-encryption.html
    Properties:
        - Name: SSEKMS
        - Name: SSES3
    
    """
    
    SSEKMS_: Optional['SSEKMS'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-encryption.html#cfn-s3-storagelens-encryption-ssekms""", alias="SSEKMS")
    SSES3_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-encryption.html#cfn-s3-storagelens-encryption-sses3""", alias="SSES3")
    


    @property
    def tropo_type(self) -> troposphere.s3.Encryption:
        from troposphere.s3 import Encryption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrefixLevel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-prefixlevel.html
    Properties:
        - Name: StorageMetrics
    
    """
    
    StorageMetrics_: 'PrefixLevelStorageMetrics' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-prefixlevel.html#cfn-s3-storagelens-prefixlevel-storagemetrics""", alias="StorageMetrics")
    


    @property
    def tropo_type(self) -> troposphere.s3.PrefixLevel:
        from troposphere.s3 import PrefixLevel as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrefixLevelStorageMetrics(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-prefixlevelstoragemetrics.html
    Properties:
        - Name: IsEnabled
        - Name: SelectionCriteria
    
    """
    
    IsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-prefixlevelstoragemetrics.html#cfn-s3-storagelens-prefixlevelstoragemetrics-isenabled""", alias="IsEnabled")
    SelectionCriteria_: Optional['SelectionCriteria'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-prefixlevelstoragemetrics.html#cfn-s3-storagelens-prefixlevelstoragemetrics-selectioncriteria""", alias="SelectionCriteria")
    


    @property
    def tropo_type(self) -> troposphere.s3.PrefixLevelStorageMetrics:
        from troposphere.s3 import PrefixLevelStorageMetrics as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3BucketDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-s3bucketdestination.html
    Properties:
        - Name: OutputSchemaVersion
        - Name: Format
        - Name: AccountId
        - Name: Prefix
        - Name: Encryption
        - Name: Arn
    
    """
    
    OutputSchemaVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-s3bucketdestination.html#cfn-s3-storagelens-s3bucketdestination-outputschemaversion""", alias="OutputSchemaVersion")
    Format_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-s3bucketdestination.html#cfn-s3-storagelens-s3bucketdestination-format""", alias="Format")
    AccountId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-s3bucketdestination.html#cfn-s3-storagelens-s3bucketdestination-accountid""", alias="AccountId")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-s3bucketdestination.html#cfn-s3-storagelens-s3bucketdestination-prefix""", alias="Prefix")
    Encryption_: Optional['Encryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-s3bucketdestination.html#cfn-s3-storagelens-s3bucketdestination-encryption""", alias="Encryption")
    Arn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-s3bucketdestination.html#cfn-s3-storagelens-s3bucketdestination-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.s3.S3BucketDestination:
        from troposphere.s3 import S3BucketDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SSEKMS(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-ssekms.html
    Properties:
        - Name: KeyId
    
    """
    
    KeyId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-ssekms.html#cfn-s3-storagelens-ssekms-keyid""", alias="KeyId")
    


    @property
    def tropo_type(self) -> troposphere.s3.SSEKMS:
        from troposphere.s3 import SSEKMS as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SelectionCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-selectioncriteria.html
    Properties:
        - Name: Delimiter
        - Name: MaxDepth
        - Name: MinStorageBytesPercentage
    
    """
    
    Delimiter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-selectioncriteria.html#cfn-s3-storagelens-selectioncriteria-delimiter""", alias="Delimiter")
    MaxDepth_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-selectioncriteria.html#cfn-s3-storagelens-selectioncriteria-maxdepth""", alias="MaxDepth")
    MinStorageBytesPercentage_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-selectioncriteria.html#cfn-s3-storagelens-selectioncriteria-minstoragebytespercentage""", alias="MinStorageBytesPercentage")
    


    @property
    def tropo_type(self) -> troposphere.s3.SelectionCriteria:
        from troposphere.s3 import SelectionCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StorageLensConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensconfiguration.html
    Properties:
        - Name: AccountLevel
        - Name: Exclude
        - Name: IsEnabled
        - Name: Include
        - Name: AwsOrg
        - Name: Id
        - Name: StorageLensArn
        - Name: DataExport
    
    """
    
    AccountLevel_: 'AccountLevel' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensconfiguration.html#cfn-s3-storagelens-storagelensconfiguration-accountlevel""", alias="AccountLevel")
    Exclude_: Optional['BucketsAndRegions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensconfiguration.html#cfn-s3-storagelens-storagelensconfiguration-exclude""", alias="Exclude")
    IsEnabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensconfiguration.html#cfn-s3-storagelens-storagelensconfiguration-isenabled""", alias="IsEnabled")
    Include_: Optional['BucketsAndRegions'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensconfiguration.html#cfn-s3-storagelens-storagelensconfiguration-include""", alias="Include")
    AwsOrg_: Optional['AwsOrg'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensconfiguration.html#cfn-s3-storagelens-storagelensconfiguration-awsorg""", alias="AwsOrg")
    Id_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensconfiguration.html#cfn-s3-storagelens-storagelensconfiguration-id""", alias="Id")
    StorageLensArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensconfiguration.html#cfn-s3-storagelens-storagelensconfiguration-storagelensarn""", alias="StorageLensArn")
    DataExport_: Optional['DataExport'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensconfiguration.html#cfn-s3-storagelens-storagelensconfiguration-dataexport""", alias="DataExport")
    


    @property
    def tropo_type(self) -> troposphere.s3.StorageLensConfiguration:
        from troposphere.s3 import StorageLensConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StorageLensGroupLevel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensgrouplevel.html
    Properties:
        - Name: StorageLensGroupSelectionCriteria
    
    """
    
    StorageLensGroupSelectionCriteria_: Optional['StorageLensGroupSelectionCriteria'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensgrouplevel.html#cfn-s3-storagelens-storagelensgrouplevel-storagelensgroupselectioncriteria""", alias="StorageLensGroupSelectionCriteria")
    


    @property
    def tropo_type(self) -> troposphere.s3.StorageLensGroupLevel:
        from troposphere.s3 import StorageLensGroupLevel as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StorageLensGroupSelectionCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensgroupselectioncriteria.html
    Properties:
        - Name: Exclude
        - Name: Include
    
    """
    
    Exclude_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensgroupselectioncriteria.html#cfn-s3-storagelens-storagelensgroupselectioncriteria-exclude""", alias="Exclude")
    Include_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensgroupselectioncriteria.html#cfn-s3-storagelens-storagelensgroupselectioncriteria-include""", alias="Include")
    


    @property
    def tropo_type(self) -> troposphere.s3.StorageLensGroupSelectionCriteria:
        from troposphere.s3 import StorageLensGroupSelectionCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AccessPoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html
    Properties:
        - Name: Policy
        - Name: PublicAccessBlockConfiguration
        - Name: Bucket
        - Name: BucketAccountId
        - Name: VpcConfiguration
        - Name: Name
    Attributes:
        - Name: Alias
        - Name: Arn
        - Name: NetworkOrigin
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html#cfn-s3-accesspoint-policy""", alias="Policy")
    PublicAccessBlockConfiguration_: Optional['PublicAccessBlockConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html#cfn-s3-accesspoint-publicaccessblockconfiguration""", alias="PublicAccessBlockConfiguration")
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html#cfn-s3-accesspoint-bucket""", alias="Bucket")
    BucketAccountId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html#cfn-s3-accesspoint-bucketaccountid""", alias="BucketAccountId")
    VpcConfiguration_: Optional['VpcConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html#cfn-s3-accesspoint-vpcconfiguration""", alias="VpcConfiguration")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html#cfn-s3-accesspoint-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.s3.AccessPoint:
        from troposphere.s3 import AccessPoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3 import AccessPoint as TropoT
        return resource_to_troposphere(self, TropoT)


class Bucket(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html
    Properties:
        - Name: AccelerateConfiguration
        - Name: AccessControl
        - Name: AnalyticsConfigurations
        - Name: BucketEncryption
        - Name: BucketName
        - Name: CorsConfiguration
        - Name: IntelligentTieringConfigurations
        - Name: InventoryConfigurations
        - Name: LifecycleConfiguration
        - Name: LoggingConfiguration
        - Name: MetricsConfigurations
        - Name: NotificationConfiguration
        - Name: ObjectLockConfiguration
        - Name: ObjectLockEnabled
        - Name: OwnershipControls
        - Name: PublicAccessBlockConfiguration
        - Name: ReplicationConfiguration
        - Name: Tags
        - Name: VersioningConfiguration
        - Name: WebsiteConfiguration
    Attributes:
        - Name: Arn
        - Name: DomainName
        - Name: DualStackDomainName
        - Name: RegionalDomainName
        - Name: WebsiteURL
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AccelerateConfiguration_: Optional['AccelerateConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-accelerateconfiguration""", alias="AccelerateConfiguration")
    AccessControl_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-accesscontrol""", alias="AccessControl")
    AnalyticsConfigurations_: Optional[List['AnalyticsConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-analyticsconfigurations""", alias="AnalyticsConfigurations")
    BucketEncryption_: Optional['BucketEncryption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-bucketencryption""", alias="BucketEncryption")
    BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-name""", alias="BucketName")
    CorsConfiguration_: Optional['CorsConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-crossoriginconfig""", alias="CorsConfiguration")
    IntelligentTieringConfigurations_: Optional[List['IntelligentTieringConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-intelligenttieringconfigurations""", alias="IntelligentTieringConfigurations")
    InventoryConfigurations_: Optional[List['InventoryConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-inventoryconfigurations""", alias="InventoryConfigurations")
    LifecycleConfiguration_: Optional['LifecycleConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-lifecycleconfig""", alias="LifecycleConfiguration")
    LoggingConfiguration_: Optional['LoggingConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-loggingconfig""", alias="LoggingConfiguration")
    MetricsConfigurations_: Optional[List['MetricsConfiguration']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-metricsconfigurations""", alias="MetricsConfigurations")
    NotificationConfiguration_: Optional['NotificationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-notification""", alias="NotificationConfiguration")
    ObjectLockConfiguration_: Optional['ObjectLockConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-objectlockconfiguration""", alias="ObjectLockConfiguration")
    ObjectLockEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-objectlockenabled""", alias="ObjectLockEnabled")
    OwnershipControls_: Optional['OwnershipControls'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-ownershipcontrols""", alias="OwnershipControls")
    PublicAccessBlockConfiguration_: Optional['PublicAccessBlockConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-publicaccessblockconfiguration""", alias="PublicAccessBlockConfiguration")
    ReplicationConfiguration_: Optional['ReplicationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-replicationconfiguration""", alias="ReplicationConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-tags""", alias="Tags")
    VersioningConfiguration_: Optional['VersioningConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-versioning""", alias="VersioningConfiguration")
    WebsiteConfiguration_: Optional['WebsiteConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#cfn-s3-bucket-websiteconfiguration""", alias="WebsiteConfiguration")
    

    @property
    def tropo_type(self) -> troposphere.s3.Bucket:
        from troposphere.s3 import Bucket as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3 import Bucket as TropoT
        return resource_to_troposphere(self, TropoT)


class BucketPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-bucketpolicy.html
    Properties:
        - Name: Bucket
        - Name: PolicyDocument
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-bucketpolicy.html#cfn-s3-bucketpolicy-bucket""", alias="Bucket")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-bucketpolicy.html#cfn-s3-bucketpolicy-policydocument""", alias="PolicyDocument")
    

    @property
    def tropo_type(self) -> troposphere.s3.BucketPolicy:
        from troposphere.s3 import BucketPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3 import BucketPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class MultiRegionAccessPoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html
    Properties:
        - Name: PublicAccessBlockConfiguration
        - Name: Regions
        - Name: Name
    Attributes:
        - Name: Alias
        - Name: CreatedAt
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PublicAccessBlockConfiguration_: Optional['PublicAccessBlockConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration""", alias="PublicAccessBlockConfiguration")
    Regions_: List['Region'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-regions""", alias="Regions")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.s3.MultiRegionAccessPoint:
        from troposphere.s3 import MultiRegionAccessPoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3 import MultiRegionAccessPoint as TropoT
        return resource_to_troposphere(self, TropoT)


class MultiRegionAccessPointPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspointpolicy.html
    Properties:
        - Name: Policy
        - Name: MrapName
    Attributes:
        - Name: PolicyStatus.IsPublic
        - Name: PolicyStatus
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspointpolicy.html#cfn-s3-multiregionaccesspointpolicy-policy""", alias="Policy")
    MrapName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspointpolicy.html#cfn-s3-multiregionaccesspointpolicy-mrapname""", alias="MrapName")
    

    @property
    def tropo_type(self) -> troposphere.s3.MultiRegionAccessPointPolicy:
        from troposphere.s3 import MultiRegionAccessPointPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3 import MultiRegionAccessPointPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class StorageLens(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelens.html
    Properties:
        - Name: StorageLensConfiguration
        - Name: Tags
    Attributes:
        - Name: StorageLensConfiguration.StorageLensArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StorageLensConfiguration_: 'StorageLensConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelens.html#cfn-s3-storagelens-storagelensconfiguration""", alias="StorageLensConfiguration")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelens.html#cfn-s3-storagelens-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.s3.StorageLens:
        from troposphere.s3 import StorageLens as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3 import StorageLens as TropoT
        return resource_to_troposphere(self, TropoT)

