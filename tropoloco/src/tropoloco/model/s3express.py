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


class BucketPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-bucketpolicy.html
    Properties:
        - Name: Bucket
        - Name: PolicyDocument
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Bucket_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-bucketpolicy.html#cfn-s3express-bucketpolicy-bucket""", alias="Bucket")
    PolicyDocument_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-bucketpolicy.html#cfn-s3express-bucketpolicy-policydocument""", alias="PolicyDocument")
    

    @property
    def tropo_type(self) -> troposphere.s3express.BucketPolicy:
        from troposphere.s3express import BucketPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3express import BucketPolicy as TropoT
        return resource_to_troposphere(self, TropoT)


class DirectoryBucket(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html
    Properties:
        - Name: BucketName
        - Name: DataRedundancy
        - Name: LocationName
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BucketName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html#cfn-s3express-directorybucket-bucketname""", alias="BucketName")
    DataRedundancy_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html#cfn-s3express-directorybucket-dataredundancy""", alias="DataRedundancy")
    LocationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html#cfn-s3express-directorybucket-locationname""", alias="LocationName")
    

    @property
    def tropo_type(self) -> troposphere.s3express.DirectoryBucket:
        from troposphere.s3express import DirectoryBucket as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.s3express import DirectoryBucket as TropoT
        return resource_to_troposphere(self, TropoT)

