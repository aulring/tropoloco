from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DataInputConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-datainputconfiguration.html
    Properties:
        - Name: InferenceInputNameConfiguration
        - Name: S3InputConfiguration
        - Name: InputTimeZoneOffset
    
    """
    
    InferenceInputNameConfiguration_: Optional['InputNameConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-datainputconfiguration.html#cfn-lookoutequipment-inferencescheduler-datainputconfiguration-inferenceinputnameconfiguration""", alias="InferenceInputNameConfiguration")
    S3InputConfiguration_: 'S3InputConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-datainputconfiguration.html#cfn-lookoutequipment-inferencescheduler-datainputconfiguration-s3inputconfiguration""", alias="S3InputConfiguration")
    InputTimeZoneOffset_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-datainputconfiguration.html#cfn-lookoutequipment-inferencescheduler-datainputconfiguration-inputtimezoneoffset""", alias="InputTimeZoneOffset")
    


    @property
    def tropo_type(self) -> troposphere.lookoutequipment.DataInputConfiguration:
        from troposphere.lookoutequipment import DataInputConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class DataOutputConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-dataoutputconfiguration.html
    Properties:
        - Name: KmsKeyId
        - Name: S3OutputConfiguration
    
    """
    
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-dataoutputconfiguration.html#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration-kmskeyid""", alias="KmsKeyId")
    S3OutputConfiguration_: 'S3OutputConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-dataoutputconfiguration.html#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration-s3outputconfiguration""", alias="S3OutputConfiguration")
    


    @property
    def tropo_type(self) -> troposphere.lookoutequipment.DataOutputConfiguration:
        from troposphere.lookoutequipment import DataOutputConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class InputNameConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-inputnameconfiguration.html
    Properties:
        - Name: ComponentTimestampDelimiter
        - Name: TimestampFormat
    
    """
    
    ComponentTimestampDelimiter_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-inputnameconfiguration.html#cfn-lookoutequipment-inferencescheduler-inputnameconfiguration-componenttimestampdelimiter""", alias="ComponentTimestampDelimiter")
    TimestampFormat_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-inputnameconfiguration.html#cfn-lookoutequipment-inferencescheduler-inputnameconfiguration-timestampformat""", alias="TimestampFormat")
    


    @property
    def tropo_type(self) -> troposphere.lookoutequipment.InputNameConfiguration:
        from troposphere.lookoutequipment import InputNameConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3InputConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-s3inputconfiguration.html
    Properties:
        - Name: Bucket
        - Name: Prefix
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-s3inputconfiguration.html#cfn-lookoutequipment-inferencescheduler-s3inputconfiguration-bucket""", alias="Bucket")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-s3inputconfiguration.html#cfn-lookoutequipment-inferencescheduler-s3inputconfiguration-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.lookoutequipment.S3InputConfiguration:
        from troposphere.lookoutequipment import S3InputConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class S3OutputConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-s3outputconfiguration.html
    Properties:
        - Name: Bucket
        - Name: Prefix
    
    """
    
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-s3outputconfiguration.html#cfn-lookoutequipment-inferencescheduler-s3outputconfiguration-bucket""", alias="Bucket")
    Prefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutequipment-inferencescheduler-s3outputconfiguration.html#cfn-lookoutequipment-inferencescheduler-s3outputconfiguration-prefix""", alias="Prefix")
    


    @property
    def tropo_type(self) -> troposphere.lookoutequipment.S3OutputConfiguration:
        from troposphere.lookoutequipment import S3OutputConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class InferenceScheduler(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html
    Properties:
        - Name: InferenceSchedulerName
        - Name: DataUploadFrequency
        - Name: ModelName
        - Name: DataInputConfiguration
        - Name: DataOutputConfiguration
        - Name: ServerSideKmsKeyId
        - Name: DataDelayOffsetInMinutes
        - Name: RoleArn
        - Name: Tags
    Attributes:
        - Name: InferenceSchedulerArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    InferenceSchedulerName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-inferenceschedulername""", alias="InferenceSchedulerName")
    DataUploadFrequency_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datauploadfrequency""", alias="DataUploadFrequency")
    ModelName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-modelname""", alias="ModelName")
    DataInputConfiguration_: 'DataInputConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datainputconfiguration""", alias="DataInputConfiguration")
    DataOutputConfiguration_: 'DataOutputConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration""", alias="DataOutputConfiguration")
    ServerSideKmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-serversidekmskeyid""", alias="ServerSideKmsKeyId")
    DataDelayOffsetInMinutes_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datadelayoffsetinminutes""", alias="DataDelayOffsetInMinutes")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.lookoutequipment.InferenceScheduler:
        from troposphere.lookoutequipment import InferenceScheduler as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lookoutequipment import InferenceScheduler as TropoT
        return resource_to_troposphere(self, TropoT)

