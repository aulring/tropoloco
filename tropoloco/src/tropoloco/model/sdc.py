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


class Deployment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html
    Properties:
        - Name: ConfigName
        - Name: S3Bucket
        - Name: TargetRegionOverride
        - Name: S3Key
        - Name: Stage
        - Name: PipelineId
        - Name: Dimension
    """

    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConfigName_: str = Field(
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-configname""",
        alias="ConfigName",
    )
    S3Bucket_: str = Field(
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-s3bucket""",
        alias="S3Bucket",
    )
    TargetRegionOverride_: Optional[str] = Field(
        None,
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-targetregionoverride""",
        alias="TargetRegionOverride",
    )
    S3Key_: str = Field(
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-s3key""",
        alias="S3Key",
    )
    Stage_: str = Field(
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-stage""",
        alias="Stage",
    )
    PipelineId_: Optional[str] = Field(
        None,
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-pipelineid""",
        alias="PipelineId",
    )
    Dimension_: str = Field(
        description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-dimension""",
        alias="Dimension",
    )

    def to_troposphere(self):
        from troposphere.sdc import Deployment as TropoT

        return resource_to_troposphere(self, TropoT)
