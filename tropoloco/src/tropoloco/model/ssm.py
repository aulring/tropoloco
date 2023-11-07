from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class InstanceAssociationOutputLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html
    Properties:
        - Name: S3Location
    
    """
    
    S3Location_: Optional['S3OutputLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html#cfn-ssm-association-instanceassociationoutputlocation-s3location""", alias="S3Location")
    


    @property
    def tropo_type(self) -> troposphere.ssm.InstanceAssociationOutputLocation:
        from troposphere.ssm import InstanceAssociationOutputLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3OutputLocation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html
    Properties:
        - Name: OutputS3KeyPrefix
        - Name: OutputS3Region
        - Name: OutputS3BucketName
    
    """
    
    OutputS3KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3keyprefix""", alias="OutputS3KeyPrefix")
    OutputS3Region_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3region""", alias="OutputS3Region")
    OutputS3BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3bucketname""", alias="OutputS3BucketName")
    


    @property
    def tropo_type(self) -> troposphere.ssm.S3OutputLocation:
        from troposphere.ssm import S3OutputLocation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Target(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html
    Properties:
        - Name: Values
        - Name: Key
    
    """
    
    Values_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html#cfn-ssm-association-target-values""", alias="Values")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html#cfn-ssm-association-target-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.ssm.Target:
        from troposphere.ssm import Target as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AttachmentsSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html
    Properties:
        - Name: Values
        - Name: Key
        - Name: Name
    
    """
    
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html#cfn-ssm-document-attachmentssource-values""", alias="Values")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html#cfn-ssm-document-attachmentssource-key""", alias="Key")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html#cfn-ssm-document-attachmentssource-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ssm.AttachmentsSource:
        from troposphere.ssm import AttachmentsSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DocumentRequires(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html
    Properties:
        - Name: Version
        - Name: Name
    
    """
    
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html#cfn-ssm-document-documentrequires-version""", alias="Version")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html#cfn-ssm-document-documentrequires-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ssm.DocumentRequires:
        from troposphere.ssm import DocumentRequires as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Targets(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html
    Properties:
        - Name: Values
        - Name: Key
    
    """
    
    Values_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html#cfn-ssm-maintenancewindowtarget-targets-values""", alias="Values")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html#cfn-ssm-maintenancewindowtarget-targets-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.ssm.Targets:
        from troposphere.ssm import Targets as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CloudWatchOutputConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html
    Properties:
        - Name: CloudWatchOutputEnabled
        - Name: CloudWatchLogGroupName
    
    """
    
    CloudWatchOutputEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html#cfn-ssm-maintenancewindowtask-cloudwatchoutputconfig-cloudwatchoutputenabled""", alias="CloudWatchOutputEnabled")
    CloudWatchLogGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html#cfn-ssm-maintenancewindowtask-cloudwatchoutputconfig-cloudwatchloggroupname""", alias="CloudWatchLogGroupName")
    


    @property
    def tropo_type(self) -> troposphere.ssm.CloudWatchOutputConfig:
        from troposphere.ssm import CloudWatchOutputConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggingInfo(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html
    Properties:
        - Name: S3Bucket
        - Name: Region
        - Name: S3Prefix
    
    """
    
    S3Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-s3bucket""", alias="S3Bucket")
    Region_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-region""", alias="Region")
    S3Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-s3prefix""", alias="S3Prefix")
    


    @property
    def tropo_type(self) -> troposphere.ssm.LoggingInfo:
        from troposphere.ssm import LoggingInfo as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MaintenanceWindowAutomationParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html
    Properties:
        - Name: Parameters
        - Name: DocumentVersion
    
    """
    
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowautomationparameters-parameters""", alias="Parameters")
    DocumentVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowautomationparameters-documentversion""", alias="DocumentVersion")
    


    @property
    def tropo_type(self) -> troposphere.ssm.MaintenanceWindowAutomationParameters:
        from troposphere.ssm import MaintenanceWindowAutomationParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MaintenanceWindowLambdaParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html
    Properties:
        - Name: ClientContext
        - Name: Qualifier
        - Name: Payload
    
    """
    
    ClientContext_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-clientcontext""", alias="ClientContext")
    Qualifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-qualifier""", alias="Qualifier")
    Payload_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-payload""", alias="Payload")
    


    @property
    def tropo_type(self) -> troposphere.ssm.MaintenanceWindowLambdaParameters:
        from troposphere.ssm import MaintenanceWindowLambdaParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MaintenanceWindowRunCommandParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html
    Properties:
        - Name: TimeoutSeconds
        - Name: Comment
        - Name: OutputS3KeyPrefix
        - Name: Parameters
        - Name: CloudWatchOutputConfig
        - Name: DocumentHashType
        - Name: ServiceRoleArn
        - Name: NotificationConfig
        - Name: DocumentVersion
        - Name: OutputS3BucketName
        - Name: DocumentHash
    
    """
    
    TimeoutSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-timeoutseconds""", alias="TimeoutSeconds")
    Comment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-comment""", alias="Comment")
    OutputS3KeyPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-outputs3keyprefix""", alias="OutputS3KeyPrefix")
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-parameters""", alias="Parameters")
    CloudWatchOutputConfig_: Optional['CloudWatchOutputConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-cloudwatchoutputconfig""", alias="CloudWatchOutputConfig")
    DocumentHashType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-documenthashtype""", alias="DocumentHashType")
    ServiceRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-servicerolearn""", alias="ServiceRoleArn")
    NotificationConfig_: Optional['NotificationConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-notificationconfig""", alias="NotificationConfig")
    DocumentVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-documentversion""", alias="DocumentVersion")
    OutputS3BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-outputs3bucketname""", alias="OutputS3BucketName")
    DocumentHash_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-documenthash""", alias="DocumentHash")
    


    @property
    def tropo_type(self) -> troposphere.ssm.MaintenanceWindowRunCommandParameters:
        from troposphere.ssm import MaintenanceWindowRunCommandParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MaintenanceWindowStepFunctionsParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html
    Properties:
        - Name: Input
        - Name: Name
    
    """
    
    Input_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-input""", alias="Input")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ssm.MaintenanceWindowStepFunctionsParameters:
        from troposphere.ssm import MaintenanceWindowStepFunctionsParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NotificationConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html
    Properties:
        - Name: NotificationArn
        - Name: NotificationType
        - Name: NotificationEvents
    
    """
    
    NotificationArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationarn""", alias="NotificationArn")
    NotificationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationtype""", alias="NotificationType")
    NotificationEvents_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationevents""", alias="NotificationEvents")
    


    @property
    def tropo_type(self) -> troposphere.ssm.NotificationConfig:
        from troposphere.ssm import NotificationConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Target(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html
    Properties:
        - Name: Values
        - Name: Key
    
    """
    
    Values_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html#cfn-ssm-maintenancewindowtask-target-values""", alias="Values")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html#cfn-ssm-maintenancewindowtask-target-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.ssm.Target:
        from troposphere.ssm import Target as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TaskInvocationParameters(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html
    Properties:
        - Name: MaintenanceWindowRunCommandParameters
        - Name: MaintenanceWindowAutomationParameters
        - Name: MaintenanceWindowStepFunctionsParameters
        - Name: MaintenanceWindowLambdaParameters
    
    """
    
    MaintenanceWindowRunCommandParameters_: Optional['MaintenanceWindowRunCommandParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowruncommandparameters""", alias="MaintenanceWindowRunCommandParameters")
    MaintenanceWindowAutomationParameters_: Optional['MaintenanceWindowAutomationParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowautomationparameters""", alias="MaintenanceWindowAutomationParameters")
    MaintenanceWindowStepFunctionsParameters_: Optional['MaintenanceWindowStepFunctionsParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowstepfunctionsparameters""", alias="MaintenanceWindowStepFunctionsParameters")
    MaintenanceWindowLambdaParameters_: Optional['MaintenanceWindowLambdaParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowlambdaparameters""", alias="MaintenanceWindowLambdaParameters")
    


    @property
    def tropo_type(self) -> troposphere.ssm.TaskInvocationParameters:
        from troposphere.ssm import TaskInvocationParameters as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PatchFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html
    Properties:
        - Name: Values
        - Name: Key
    
    """
    
    Values_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html#cfn-ssm-patchbaseline-patchfilter-values""", alias="Values")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html#cfn-ssm-patchbaseline-patchfilter-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.ssm.PatchFilter:
        from troposphere.ssm import PatchFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PatchFilterGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html
    Properties:
        - Name: PatchFilters
    
    """
    
    PatchFilters_: Optional[List['PatchFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html#cfn-ssm-patchbaseline-patchfiltergroup-patchfilters""", alias="PatchFilters")
    


    @property
    def tropo_type(self) -> troposphere.ssm.PatchFilterGroup:
        from troposphere.ssm import PatchFilterGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PatchSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html
    Properties:
        - Name: Products
        - Name: Configuration
        - Name: Name
    
    """
    
    Products_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-products""", alias="Products")
    Configuration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-configuration""", alias="Configuration")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.ssm.PatchSource:
        from troposphere.ssm import PatchSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PatchStringDate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchstringdate.html
    Properties:
        - did not locate and properties
    
    """
    
    pass



    @property
    def tropo_type(self) -> troposphere.ssm.PatchStringDate:
        from troposphere.ssm import PatchStringDate as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Rule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html
    Properties:
        - Name: ApproveUntilDate
        - Name: EnableNonSecurity
        - Name: PatchFilterGroup
        - Name: ApproveAfterDays
        - Name: ComplianceLevel
    
    """
    
    ApproveUntilDate_: Optional['PatchStringDate'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-approveuntildate""", alias="ApproveUntilDate")
    EnableNonSecurity_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-enablenonsecurity""", alias="EnableNonSecurity")
    PatchFilterGroup_: Optional['PatchFilterGroup'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-patchfiltergroup""", alias="PatchFilterGroup")
    ApproveAfterDays_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-approveafterdays""", alias="ApproveAfterDays")
    ComplianceLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-compliancelevel""", alias="ComplianceLevel")
    


    @property
    def tropo_type(self) -> troposphere.ssm.Rule:
        from troposphere.ssm import Rule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RuleGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html
    Properties:
        - Name: PatchRules
    
    """
    
    PatchRules_: Optional[List['Rule']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html#cfn-ssm-patchbaseline-rulegroup-patchrules""", alias="PatchRules")
    


    @property
    def tropo_type(self) -> troposphere.ssm.RuleGroup:
        from troposphere.ssm import RuleGroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AwsOrganizationsSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html
    Properties:
        - Name: OrganizationSourceType
        - Name: OrganizationalUnits
    
    """
    
    OrganizationSourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html#cfn-ssm-resourcedatasync-awsorganizationssource-organizationsourcetype""", alias="OrganizationSourceType")
    OrganizationalUnits_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html#cfn-ssm-resourcedatasync-awsorganizationssource-organizationalunits""", alias="OrganizationalUnits")
    


    @property
    def tropo_type(self) -> troposphere.ssm.AwsOrganizationsSource:
        from troposphere.ssm import AwsOrganizationsSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3Destination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html
    Properties:
        - Name: KMSKeyArn
        - Name: BucketName
        - Name: BucketRegion
        - Name: SyncFormat
        - Name: BucketPrefix
    
    """
    
    KMSKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-kmskeyarn""", alias="KMSKeyArn")
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-bucketname""", alias="BucketName")
    BucketRegion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-bucketregion""", alias="BucketRegion")
    SyncFormat_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-syncformat""", alias="SyncFormat")
    BucketPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-bucketprefix""", alias="BucketPrefix")
    


    @property
    def tropo_type(self) -> troposphere.ssm.S3Destination:
        from troposphere.ssm import S3Destination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SyncSource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html
    Properties:
        - Name: SourceType
        - Name: AwsOrganizationsSource
        - Name: IncludeFutureRegions
        - Name: SourceRegions
    
    """
    
    SourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-sourcetype""", alias="SourceType")
    AwsOrganizationsSource_: Optional['AwsOrganizationsSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-awsorganizationssource""", alias="AwsOrganizationsSource")
    IncludeFutureRegions_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-includefutureregions""", alias="IncludeFutureRegions")
    SourceRegions_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-sourceregions""", alias="SourceRegions")
    


    @property
    def tropo_type(self) -> troposphere.ssm.SyncSource:
        from troposphere.ssm import SyncSource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Association(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html
    Properties:
        - Name: AssociationName
        - Name: CalendarNames
        - Name: ScheduleExpression
        - Name: MaxErrors
        - Name: Parameters
        - Name: InstanceId
        - Name: WaitForSuccessTimeoutSeconds
        - Name: MaxConcurrency
        - Name: ComplianceSeverity
        - Name: Targets
        - Name: SyncCompliance
        - Name: OutputLocation
        - Name: ScheduleOffset
        - Name: Name
        - Name: ApplyOnlyAtCronInterval
        - Name: DocumentVersion
        - Name: AutomationTargetParameterName
    Attributes:
        - Name: AssociationId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AssociationName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-associationname""", alias="AssociationName")
    CalendarNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-calendarnames""", alias="CalendarNames")
    ScheduleExpression_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-scheduleexpression""", alias="ScheduleExpression")
    MaxErrors_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-maxerrors""", alias="MaxErrors")
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-parameters""", alias="Parameters")
    InstanceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-instanceid""", alias="InstanceId")
    WaitForSuccessTimeoutSeconds_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-waitforsuccesstimeoutseconds""", alias="WaitForSuccessTimeoutSeconds")
    MaxConcurrency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-maxconcurrency""", alias="MaxConcurrency")
    ComplianceSeverity_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-complianceseverity""", alias="ComplianceSeverity")
    Targets_: Optional[List['Target']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-targets""", alias="Targets")
    SyncCompliance_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-synccompliance""", alias="SyncCompliance")
    OutputLocation_: Optional['InstanceAssociationOutputLocation'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-outputlocation""", alias="OutputLocation")
    ScheduleOffset_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-scheduleoffset""", alias="ScheduleOffset")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-name""", alias="Name")
    ApplyOnlyAtCronInterval_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-applyonlyatcroninterval""", alias="ApplyOnlyAtCronInterval")
    DocumentVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-documentversion""", alias="DocumentVersion")
    AutomationTargetParameterName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-automationtargetparametername""", alias="AutomationTargetParameterName")
    

    @property
    def tropo_type(self) -> troposphere.ssm.Association:
        from troposphere.ssm import Association as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssm import Association as TropoT
        return resource_to_troposphere(self, TropoT)


class Document(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html
    Properties:
        - Name: DocumentFormat
        - Name: Requires
        - Name: Content
        - Name: TargetType
        - Name: DocumentType
        - Name: VersionName
        - Name: UpdateMethod
        - Name: Attachments
        - Name: Tags
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DocumentFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-documentformat""", alias="DocumentFormat")
    Requires_: Optional[List['DocumentRequires']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-requires""", alias="Requires")
    Content_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-content""", alias="Content")
    TargetType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-targettype""", alias="TargetType")
    DocumentType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-documenttype""", alias="DocumentType")
    VersionName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-versionname""", alias="VersionName")
    UpdateMethod_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-updatemethod""", alias="UpdateMethod")
    Attachments_: Optional[List['AttachmentsSource']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-attachments""", alias="Attachments")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ssm.Document:
        from troposphere.ssm import Document as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssm import Document as TropoT
        return resource_to_troposphere(self, TropoT)


class MaintenanceWindow(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html
    Properties:
        - Name: StartDate
        - Name: Description
        - Name: AllowUnassociatedTargets
        - Name: Cutoff
        - Name: Schedule
        - Name: Duration
        - Name: ScheduleOffset
        - Name: EndDate
        - Name: Tags
        - Name: Name
        - Name: ScheduleTimezone
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    StartDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-startdate""", alias="StartDate")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-description""", alias="Description")
    AllowUnassociatedTargets_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-allowunassociatedtargets""", alias="AllowUnassociatedTargets")
    Cutoff_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-cutoff""", alias="Cutoff")
    Schedule_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-schedule""", alias="Schedule")
    Duration_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-duration""", alias="Duration")
    ScheduleOffset_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduleoffset""", alias="ScheduleOffset")
    EndDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-enddate""", alias="EndDate")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-name""", alias="Name")
    ScheduleTimezone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduletimezone""", alias="ScheduleTimezone")
    

    @property
    def tropo_type(self) -> troposphere.ssm.MaintenanceWindow:
        from troposphere.ssm import MaintenanceWindow as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssm import MaintenanceWindow as TropoT
        return resource_to_troposphere(self, TropoT)


class MaintenanceWindowTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html
    Properties:
        - Name: OwnerInformation
        - Name: Description
        - Name: WindowId
        - Name: ResourceType
        - Name: Targets
        - Name: Name
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OwnerInformation_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-ownerinformation""", alias="OwnerInformation")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-description""", alias="Description")
    WindowId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-windowid""", alias="WindowId")
    ResourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-resourcetype""", alias="ResourceType")
    Targets_: List['Targets'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-targets""", alias="Targets")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ssm.MaintenanceWindowTarget:
        from troposphere.ssm import MaintenanceWindowTarget as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssm import MaintenanceWindowTarget as TropoT
        return resource_to_troposphere(self, TropoT)


class MaintenanceWindowTask(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html
    Properties:
        - Name: MaxErrors
        - Name: Description
        - Name: ServiceRoleArn
        - Name: Priority
        - Name: MaxConcurrency
        - Name: Targets
        - Name: Name
        - Name: TaskArn
        - Name: TaskInvocationParameters
        - Name: WindowId
        - Name: TaskParameters
        - Name: TaskType
        - Name: CutoffBehavior
        - Name: LoggingInfo
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    MaxErrors_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxerrors""", alias="MaxErrors")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-description""", alias="Description")
    ServiceRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-servicerolearn""", alias="ServiceRoleArn")
    Priority_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-priority""", alias="Priority")
    MaxConcurrency_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxconcurrency""", alias="MaxConcurrency")
    Targets_: Optional[List['Target']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-targets""", alias="Targets")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-name""", alias="Name")
    TaskArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskarn""", alias="TaskArn")
    TaskInvocationParameters_: Optional['TaskInvocationParameters'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters""", alias="TaskInvocationParameters")
    WindowId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-windowid""", alias="WindowId")
    TaskParameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskparameters""", alias="TaskParameters")
    TaskType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-tasktype""", alias="TaskType")
    CutoffBehavior_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-cutoffbehavior""", alias="CutoffBehavior")
    LoggingInfo_: Optional['LoggingInfo'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-logginginfo""", alias="LoggingInfo")
    

    @property
    def tropo_type(self) -> troposphere.ssm.MaintenanceWindowTask:
        from troposphere.ssm import MaintenanceWindowTask as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssm import MaintenanceWindowTask as TropoT
        return resource_to_troposphere(self, TropoT)


class Parameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html
    Properties:
        - Name: Type
        - Name: Description
        - Name: Policies
        - Name: AllowedPattern
        - Name: Tier
        - Name: Value
        - Name: DataType
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Type
        - Name: Value
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-type""", alias="Type")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-description""", alias="Description")
    Policies_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-policies""", alias="Policies")
    AllowedPattern_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-allowedpattern""", alias="AllowedPattern")
    Tier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tier""", alias="Tier")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-value""", alias="Value")
    DataType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-datatype""", alias="DataType")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.ssm.Parameter:
        from troposphere.ssm import Parameter as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssm import Parameter as TropoT
        return resource_to_troposphere(self, TropoT)


class PatchBaseline(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html
    Properties:
        - Name: OperatingSystem
        - Name: Description
        - Name: ApprovalRules
        - Name: Sources
        - Name: Name
        - Name: RejectedPatches
        - Name: ApprovedPatches
        - Name: RejectedPatchesAction
        - Name: PatchGroups
        - Name: ApprovedPatchesComplianceLevel
        - Name: ApprovedPatchesEnableNonSecurity
        - Name: GlobalFilters
        - Name: Tags
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    OperatingSystem_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-operatingsystem""", alias="OperatingSystem")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-description""", alias="Description")
    ApprovalRules_: Optional['RuleGroup'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvalrules""", alias="ApprovalRules")
    Sources_: Optional[List['PatchSource']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-sources""", alias="Sources")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-name""", alias="Name")
    RejectedPatches_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatches""", alias="RejectedPatches")
    ApprovedPatches_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatches""", alias="ApprovedPatches")
    RejectedPatchesAction_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatchesaction""", alias="RejectedPatchesAction")
    PatchGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-patchgroups""", alias="PatchGroups")
    ApprovedPatchesComplianceLevel_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchescompliancelevel""", alias="ApprovedPatchesComplianceLevel")
    ApprovedPatchesEnableNonSecurity_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchesenablenonsecurity""", alias="ApprovedPatchesEnableNonSecurity")
    GlobalFilters_: Optional['PatchFilterGroup'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-globalfilters""", alias="GlobalFilters")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.ssm.PatchBaseline:
        from troposphere.ssm import PatchBaseline as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssm import PatchBaseline as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourceDataSync(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html
    Properties:
        - Name: S3Destination
        - Name: KMSKeyArn
        - Name: SyncSource
        - Name: BucketName
        - Name: BucketRegion
        - Name: SyncFormat
        - Name: SyncType
        - Name: BucketPrefix
        - Name: SyncName
    Attributes:
        - Name: SyncName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    S3Destination_: Optional['S3Destination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-s3destination""", alias="S3Destination")
    KMSKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-kmskeyarn""", alias="KMSKeyArn")
    SyncSource_: Optional['SyncSource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncsource""", alias="SyncSource")
    BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketname""", alias="BucketName")
    BucketRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketregion""", alias="BucketRegion")
    SyncFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncformat""", alias="SyncFormat")
    SyncType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-synctype""", alias="SyncType")
    BucketPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketprefix""", alias="BucketPrefix")
    SyncName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncname""", alias="SyncName")
    

    @property
    def tropo_type(self) -> troposphere.ssm.ResourceDataSync:
        from troposphere.ssm import ResourceDataSync as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssm import ResourceDataSync as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourcePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcepolicy.html
    Properties:
        - Name: Policy
        - Name: ResourceArn
    Attributes:
        - Name: PolicyHash
        - Name: PolicyId
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcepolicy.html#cfn-ssm-resourcepolicy-policy""", alias="Policy")
    ResourceArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcepolicy.html#cfn-ssm-resourcepolicy-resourcearn""", alias="ResourceArn")
    

    @property
    def tropo_type(self) -> troposphere.ssm.ResourcePolicy:
        from troposphere.ssm import ResourcePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.ssm import ResourcePolicy as TropoT
        return resource_to_troposphere(self, TropoT)

