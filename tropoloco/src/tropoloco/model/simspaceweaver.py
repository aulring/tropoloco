from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class S3Location(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-simspaceweaver-simulation-s3location.html
    Properties:
        - Name: BucketName
        - Name: ObjectKey
    
    """
    
    BucketName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-simspaceweaver-simulation-s3location.html#cfn-simspaceweaver-simulation-s3location-bucketname""", alias="BucketName")
    ObjectKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-simspaceweaver-simulation-s3location.html#cfn-simspaceweaver-simulation-s3location-objectkey""", alias="ObjectKey")
    


    @property
    def tropo_type(self) -> troposphere.simspaceweaver.S3Location:
        from troposphere.simspaceweaver import S3Location as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Simulation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html
    Properties:
        - Name: SchemaS3Location
        - Name: SnapshotS3Location
        - Name: MaximumDuration
        - Name: RoleArn
        - Name: Name
    Attributes:
        - Name: DescribePayload
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SchemaS3Location_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html#cfn-simspaceweaver-simulation-schemas3location""", alias="SchemaS3Location")
    SnapshotS3Location_: Optional['S3Location'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html#cfn-simspaceweaver-simulation-snapshots3location""", alias="SnapshotS3Location")
    MaximumDuration_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html#cfn-simspaceweaver-simulation-maximumduration""", alias="MaximumDuration")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html#cfn-simspaceweaver-simulation-rolearn""", alias="RoleArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html#cfn-simspaceweaver-simulation-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.simspaceweaver.Simulation:
        from troposphere.simspaceweaver import Simulation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.simspaceweaver import Simulation as TropoT
        return resource_to_troposphere(self, TropoT)

