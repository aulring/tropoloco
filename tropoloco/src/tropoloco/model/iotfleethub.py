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


class Application(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html
    Properties:
        - Name: ApplicationName
        - Name: ApplicationDescription
        - Name: RoleArn
        - Name: Tags
    Attributes:
        - Name: ApplicationUrl
        - Name: ApplicationArn
        - Name: ApplicationState
        - Name: SsoClientId
        - Name: ApplicationId
        - Name: ApplicationLastUpdateDate
        - Name: ErrorMessage
        - Name: ApplicationCreationDate
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ApplicationName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html#cfn-iotfleethub-application-applicationname""", alias="ApplicationName")
    ApplicationDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html#cfn-iotfleethub-application-applicationdescription""", alias="ApplicationDescription")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html#cfn-iotfleethub-application-rolearn""", alias="RoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html#cfn-iotfleethub-application-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.iotfleethub.Application:
        from troposphere.iotfleethub import Application as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.iotfleethub import Application as TropoT
        return resource_to_troposphere(self, TropoT)

