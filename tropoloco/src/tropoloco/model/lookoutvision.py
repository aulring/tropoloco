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


class Project(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutvision-project.html
    Properties:
        - Name: ProjectName
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ProjectName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutvision-project.html#cfn-lookoutvision-project-projectname""", alias="ProjectName")
    

    @property
    def tropo_type(self) -> troposphere.lookoutvision.Project:
        from troposphere.lookoutvision import Project as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.lookoutvision import Project as TropoT
        return resource_to_troposphere(self, TropoT)

