from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################




######################################################################
# AWS Resource
######################################################################


class ReportDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html
    Properties:
        - Name: AdditionalArtifacts
        - Name: ReportName
        - Name: Compression
        - Name: Format
        - Name: RefreshClosedReports
        - Name: S3Bucket
        - Name: ReportVersioning
        - Name: S3Region
        - Name: TimeUnit
        - Name: BillingViewArn
        - Name: S3Prefix
        - Name: AdditionalSchemaElements
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AdditionalArtifacts_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-additionalartifacts""", alias="AdditionalArtifacts")
    ReportName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-reportname""", alias="ReportName")
    Compression_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-compression""", alias="Compression")
    Format_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-format""", alias="Format")
    RefreshClosedReports_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-refreshclosedreports""", alias="RefreshClosedReports")
    S3Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-s3bucket""", alias="S3Bucket")
    ReportVersioning_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-reportversioning""", alias="ReportVersioning")
    S3Region_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-s3region""", alias="S3Region")
    TimeUnit_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-timeunit""", alias="TimeUnit")
    BillingViewArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-billingviewarn""", alias="BillingViewArn")
    S3Prefix_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-s3prefix""", alias="S3Prefix")
    AdditionalSchemaElements_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-additionalschemaelements""", alias="AdditionalSchemaElements")
    

    @property
    def tropo_type(self) -> troposphere.cur.ReportDefinition:
        from troposphere.cur import ReportDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.cur import ReportDefinition as TropoT
        return resource_to_troposphere(self, TropoT)

