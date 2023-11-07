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


class Datastore(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthimaging-datastore.html
    Properties:
        - Name: KmsKeyArn
        - Name: DatastoreName
        - Name: Tags
    Attributes:
        - Name: DatastoreArn
        - Name: DatastoreId
        - Name: DatastoreStatus
        - Name: CreatedAt
        - Name: UpdatedAt
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KmsKeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthimaging-datastore.html#cfn-healthimaging-datastore-kmskeyarn""", alias="KmsKeyArn")
    DatastoreName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthimaging-datastore.html#cfn-healthimaging-datastore-datastorename""", alias="DatastoreName")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthimaging-datastore.html#cfn-healthimaging-datastore-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.healthimaging.Datastore:
        from troposphere.healthimaging import Datastore as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.healthimaging import Datastore as TropoT
        return resource_to_troposphere(self, TropoT)

