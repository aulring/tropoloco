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


class AssessmentTarget(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html
    Properties:
        - Name: AssessmentTargetName
        - Name: ResourceGroupArn
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AssessmentTargetName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html#cfn-inspector-assessmenttarget-assessmenttargetname""", alias="AssessmentTargetName")
    ResourceGroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html#cfn-inspector-assessmenttarget-resourcegrouparn""", alias="ResourceGroupArn")
    

    @property
    def tropo_type(self) -> troposphere.inspector.AssessmentTarget:
        from troposphere.inspector import AssessmentTarget as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.inspector import AssessmentTarget as TropoT
        return resource_to_troposphere(self, TropoT)


class AssessmentTemplate(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html
    Properties:
        - Name: AssessmentTargetArn
        - Name: DurationInSeconds
        - Name: AssessmentTemplateName
        - Name: RulesPackageArns
        - Name: UserAttributesForFindings
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AssessmentTargetArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-assessmenttargetarn""", alias="AssessmentTargetArn")
    DurationInSeconds_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-durationinseconds""", alias="DurationInSeconds")
    AssessmentTemplateName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-assessmenttemplatename""", alias="AssessmentTemplateName")
    RulesPackageArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-rulespackagearns""", alias="RulesPackageArns")
    UserAttributesForFindings_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-userattributesforfindings""", alias="UserAttributesForFindings")
    

    @property
    def tropo_type(self) -> troposphere.inspector.AssessmentTemplate:
        from troposphere.inspector import AssessmentTemplate as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.inspector import AssessmentTemplate as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourceGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-resourcegroup.html
    Properties:
        - Name: ResourceGroupTags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceGroupTags_: List['Tag'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-resourcegroup.html#cfn-inspector-resourcegroup-resourcegrouptags""", alias="ResourceGroupTags")
    

    @property
    def tropo_type(self) -> troposphere.inspector.ResourceGroup:
        from troposphere.inspector import ResourceGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.inspector import ResourceGroup as TropoT
        return resource_to_troposphere(self, TropoT)

