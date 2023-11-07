from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class AWSAccount(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html
    Properties:
        - Name: Id
        - Name: EmailAddress
        - Name: Name
    
    """
    
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html#cfn-auditmanager-assessment-awsaccount-id""", alias="Id")
    EmailAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html#cfn-auditmanager-assessment-awsaccount-emailaddress""", alias="EmailAddress")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html#cfn-auditmanager-assessment-awsaccount-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.auditmanager.AWSAccount:
        from troposphere.auditmanager import AWSAccount as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AWSService(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsservice.html
    Properties:
        - Name: ServiceName
    
    """
    
    ServiceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsservice.html#cfn-auditmanager-assessment-awsservice-servicename""", alias="ServiceName")
    


    @property
    def tropo_type(self) -> troposphere.auditmanager.AWSService:
        from troposphere.auditmanager import AWSService as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AssessmentReportsDestination(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-assessmentreportsdestination.html
    Properties:
        - Name: Destination
        - Name: DestinationType
    
    """
    
    Destination_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-assessmentreportsdestination.html#cfn-auditmanager-assessment-assessmentreportsdestination-destination""", alias="Destination")
    DestinationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-assessmentreportsdestination.html#cfn-auditmanager-assessment-assessmentreportsdestination-destinationtype""", alias="DestinationType")
    


    @property
    def tropo_type(self) -> troposphere.auditmanager.AssessmentReportsDestination:
        from troposphere.auditmanager import AssessmentReportsDestination as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Delegation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html
    Properties:
        - Name: Status
        - Name: Comment
        - Name: CreatedBy
        - Name: RoleType
        - Name: AssessmentId
        - Name: CreationTime
        - Name: LastUpdated
        - Name: Id
        - Name: AssessmentName
        - Name: RoleArn
        - Name: ControlSetId
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-status""", alias="Status")
    Comment_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-comment""", alias="Comment")
    CreatedBy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-createdby""", alias="CreatedBy")
    RoleType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-roletype""", alias="RoleType")
    AssessmentId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-assessmentid""", alias="AssessmentId")
    CreationTime_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-creationtime""", alias="CreationTime")
    LastUpdated_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-lastupdated""", alias="LastUpdated")
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-id""", alias="Id")
    AssessmentName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-assessmentname""", alias="AssessmentName")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-rolearn""", alias="RoleArn")
    ControlSetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-controlsetid""", alias="ControlSetId")
    


    @property
    def tropo_type(self) -> troposphere.auditmanager.Delegation:
        from troposphere.auditmanager import Delegation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Role(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-role.html
    Properties:
        - Name: RoleType
        - Name: RoleArn
    
    """
    
    RoleType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-role.html#cfn-auditmanager-assessment-role-roletype""", alias="RoleType")
    RoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-role.html#cfn-auditmanager-assessment-role-rolearn""", alias="RoleArn")
    


    @property
    def tropo_type(self) -> troposphere.auditmanager.Role:
        from troposphere.auditmanager import Role as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Scope(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-scope.html
    Properties:
        - Name: AwsAccounts
        - Name: AwsServices
    
    """
    
    AwsAccounts_: Optional[List['AWSAccount']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-scope.html#cfn-auditmanager-assessment-scope-awsaccounts""", alias="AwsAccounts")
    AwsServices_: Optional[List['AWSService']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-scope.html#cfn-auditmanager-assessment-scope-awsservices""", alias="AwsServices")
    


    @property
    def tropo_type(self) -> troposphere.auditmanager.Scope:
        from troposphere.auditmanager import Scope as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Assessment(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html
    Properties:
        - Name: Status
        - Name: AssessmentReportsDestination
        - Name: Delegations
        - Name: Description
        - Name: Scope
        - Name: AwsAccount
        - Name: Roles
        - Name: FrameworkId
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: AssessmentId
        - Name: CreationTime
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-status""", alias="Status")
    AssessmentReportsDestination_: Optional['AssessmentReportsDestination'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-assessmentreportsdestination""", alias="AssessmentReportsDestination")
    Delegations_: Optional[List['Delegation']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-delegations""", alias="Delegations")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-description""", alias="Description")
    Scope_: Optional['Scope'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-scope""", alias="Scope")
    AwsAccount_: Optional['AWSAccount'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-awsaccount""", alias="AwsAccount")
    Roles_: Optional[List['Role']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-roles""", alias="Roles")
    FrameworkId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-frameworkid""", alias="FrameworkId")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.auditmanager.Assessment:
        from troposphere.auditmanager import Assessment as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.auditmanager import Assessment as TropoT
        return resource_to_troposphere(self, TropoT)

