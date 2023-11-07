from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Alias(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-alias.html
    Properties:
        - Name: Status
        - Name: Value
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-alias.html#cfn-s3objectlambda-accesspoint-alias-status""", alias="Status")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-alias.html#cfn-s3objectlambda-accesspoint-alias-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.s3objectlambda.Alias:
        from troposphere.s3objectlambda import Alias as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AwsLambda(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-awslambda.html
    Properties:
        - Name: FunctionArn
        - Name: FunctionPayload
    
    """
    
    FunctionArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-awslambda.html#cfn-s3objectlambda-accesspoint-awslambda-functionarn""", alias="FunctionArn")
    FunctionPayload_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-awslambda.html#cfn-s3objectlambda-accesspoint-awslambda-functionpayload""", alias="FunctionPayload")
    


    @property
    def tropo_type(self) -> troposphere.s3objectlambda.AwsLambda:
        from troposphere.s3objectlambda import AwsLambda as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ContentTransformation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-contenttransformation.html
    Properties:
        - Name: AwsLambda
    
    """
    
    AwsLambda_: 'AwsLambda' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-contenttransformation.html#cfn-s3objectlambda-accesspoint-contenttransformation-awslambda""", alias="AwsLambda")
    


    @property
    def tropo_type(self) -> troposphere.s3objectlambda.ContentTransformation:
        from troposphere.s3objectlambda import ContentTransformation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ObjectLambdaConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html
    Properties:
        - Name: SupportingAccessPoint
        - Name: TransformationConfigurations
        - Name: AllowedFeatures
        - Name: CloudWatchMetricsEnabled
    
    """
    
    SupportingAccessPoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-supportingaccesspoint""", alias="SupportingAccessPoint")
    TransformationConfigurations_: List['TransformationConfiguration'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-transformationconfigurations""", alias="TransformationConfigurations")
    AllowedFeatures_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-allowedfeatures""", alias="AllowedFeatures")
    CloudWatchMetricsEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-cloudwatchmetricsenabled""", alias="CloudWatchMetricsEnabled")
    


    @property
    def tropo_type(self) -> troposphere.s3objectlambda.ObjectLambdaConfiguration:
        from troposphere.s3objectlambda import ObjectLambdaConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PublicAccessBlockConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-publicaccessblockconfiguration.html
    Properties:
        - Name: RestrictPublicBuckets
        - Name: BlockPublicPolicy
        - Name: BlockPublicAcls
        - Name: IgnorePublicAcls
    
    """
    
    RestrictPublicBuckets_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-publicaccessblockconfiguration.html#cfn-s3objectlambda-accesspoint-publicaccessblockconfiguration-restrictpublicbuckets""", alias="RestrictPublicBuckets")
    BlockPublicPolicy_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-publicaccessblockconfiguration.html#cfn-s3objectlambda-accesspoint-publicaccessblockconfiguration-blockpublicpolicy""", alias="BlockPublicPolicy")
    BlockPublicAcls_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-publicaccessblockconfiguration.html#cfn-s3objectlambda-accesspoint-publicaccessblockconfiguration-blockpublicacls""", alias="BlockPublicAcls")
    IgnorePublicAcls_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-publicaccessblockconfiguration.html#cfn-s3objectlambda-accesspoint-publicaccessblockconfiguration-ignorepublicacls""", alias="IgnorePublicAcls")
    


    @property
    def tropo_type(self) -> troposphere.s3objectlambda.PublicAccessBlockConfiguration:
        from troposphere.s3objectlambda import PublicAccessBlockConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TransformationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html
    Properties:
        - Name: Actions
        - Name: ContentTransformation
    
    """
    
    Actions_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html#cfn-s3objectlambda-accesspoint-transformationconfiguration-actions""", alias="Actions")
    ContentTransformation_: 'ContentTransformation' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html#cfn-s3objectlambda-accesspoint-transformationconfiguration-contenttransformation""", alias="ContentTransformation")
    


    @property
    def tropo_type(self) -> troposphere.s3objectlambda.TransformationConfiguration:
        from troposphere.s3objectlambda import TransformationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class AccessPoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html
    Properties:
        - Name: ObjectLambdaConfiguration
        - Name: Name
    Attributes:
        - Name: CreationDate
        - Name: PublicAccessBlockConfiguration
        - Name: PublicAccessBlockConfiguration.BlockPublicAcls
        - Name: Alias
        - Name: Alias.Value
        - Name: PublicAccessBlockConfiguration.IgnorePublicAcls
        - Name: PublicAccessBlockConfiguration.RestrictPublicBuckets
        - Name: PublicAccessBlockConfiguration.BlockPublicPolicy
        - Name: Arn
        - Name: Alias.Status
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ObjectLambdaConfiguration_: 'ObjectLambdaConfiguration' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration""", alias="ObjectLambdaConfiguration")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#cfn-s3objectlambda-accesspoint-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.s3objectlambda.AccessPoint:
        from troposphere.s3objectlambda import AccessPoint as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3objectlambda import AccessPoint as TropoT
        return resource_to_troposphere(self, TropoT)


class AccessPointPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html
    Properties:
        - Name: PolicyDocument
        - Name: ObjectLambdaAccessPoint
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html#cfn-s3objectlambda-accesspointpolicy-policydocument""", alias="PolicyDocument")
    ObjectLambdaAccessPoint_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html#cfn-s3objectlambda-accesspointpolicy-objectlambdaaccesspoint""", alias="ObjectLambdaAccessPoint")
    

    @property
    def tropo_type(self) -> troposphere.s3objectlambda.AccessPointPolicy:
        from troposphere.s3objectlambda import AccessPointPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3objectlambda import AccessPointPolicy as TropoT
        return resource_to_troposphere(self, TropoT)

