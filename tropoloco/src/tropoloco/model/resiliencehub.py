from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class EventSubscription(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-eventsubscription.html
    Properties:
        - Name: EventType
        - Name: SnsTopicArn
        - Name: Name
    
    """
    
    EventType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-eventsubscription.html#cfn-resiliencehub-app-eventsubscription-eventtype""", alias="EventType")
    SnsTopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-eventsubscription.html#cfn-resiliencehub-app-eventsubscription-snstopicarn""", alias="SnsTopicArn")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-eventsubscription.html#cfn-resiliencehub-app-eventsubscription-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.resiliencehub.EventSubscription:
        from troposphere.resiliencehub import EventSubscription as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PermissionModel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-permissionmodel.html
    Properties:
        - Name: Type
        - Name: CrossAccountRoleArns
        - Name: InvokerRoleName
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-permissionmodel.html#cfn-resiliencehub-app-permissionmodel-type""", alias="Type")
    CrossAccountRoleArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-permissionmodel.html#cfn-resiliencehub-app-permissionmodel-crossaccountrolearns""", alias="CrossAccountRoleArns")
    InvokerRoleName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-permissionmodel.html#cfn-resiliencehub-app-permissionmodel-invokerrolename""", alias="InvokerRoleName")
    


    @property
    def tropo_type(self) -> troposphere.resiliencehub.PermissionModel:
        from troposphere.resiliencehub import PermissionModel as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PhysicalResourceId(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html
    Properties:
        - Name: Type
        - Name: Identifier
        - Name: AwsRegion
        - Name: AwsAccountId
    
    """
    
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html#cfn-resiliencehub-app-physicalresourceid-type""", alias="Type")
    Identifier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html#cfn-resiliencehub-app-physicalresourceid-identifier""", alias="Identifier")
    AwsRegion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html#cfn-resiliencehub-app-physicalresourceid-awsregion""", alias="AwsRegion")
    AwsAccountId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html#cfn-resiliencehub-app-physicalresourceid-awsaccountid""", alias="AwsAccountId")
    


    @property
    def tropo_type(self) -> troposphere.resiliencehub.PhysicalResourceId:
        from troposphere.resiliencehub import PhysicalResourceId as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceMapping(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html
    Properties:
        - Name: MappingType
        - Name: LogicalStackName
        - Name: ResourceName
        - Name: TerraformSourceName
        - Name: PhysicalResourceId
        - Name: EksSourceName
    
    """
    
    MappingType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-mappingtype""", alias="MappingType")
    LogicalStackName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-logicalstackname""", alias="LogicalStackName")
    ResourceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-resourcename""", alias="ResourceName")
    TerraformSourceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-terraformsourcename""", alias="TerraformSourceName")
    PhysicalResourceId_: 'PhysicalResourceId' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-physicalresourceid""", alias="PhysicalResourceId")
    EksSourceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html#cfn-resiliencehub-app-resourcemapping-ekssourcename""", alias="EksSourceName")
    


    @property
    def tropo_type(self) -> troposphere.resiliencehub.ResourceMapping:
        from troposphere.resiliencehub import ResourceMapping as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FailurePolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html
    Properties:
        - Name: RpoInSecs
        - Name: RtoInSecs
    
    """
    
    RpoInSecs_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html#cfn-resiliencehub-resiliencypolicy-failurepolicy-rpoinsecs""", alias="RpoInSecs")
    RtoInSecs_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html#cfn-resiliencehub-resiliencypolicy-failurepolicy-rtoinsecs""", alias="RtoInSecs")
    


    @property
    def tropo_type(self) -> troposphere.resiliencehub.FailurePolicy:
        from troposphere.resiliencehub import FailurePolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class App(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html
    Properties:
        - Name: Description
        - Name: AppTemplateBody
        - Name: AppAssessmentSchedule
        - Name: PermissionModel
        - Name: ResourceMappings
        - Name: EventSubscriptions
        - Name: Tags
        - Name: Name
        - Name: ResiliencyPolicyArn
    Attributes:
        - Name: AppArn
        - Name: DriftStatus
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-description""", alias="Description")
    AppTemplateBody_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-apptemplatebody""", alias="AppTemplateBody")
    AppAssessmentSchedule_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-appassessmentschedule""", alias="AppAssessmentSchedule")
    PermissionModel_: Optional['PermissionModel'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-permissionmodel""", alias="PermissionModel")
    ResourceMappings_: List['ResourceMapping'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-resourcemappings""", alias="ResourceMappings")
    EventSubscriptions_: Optional[List['EventSubscription']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-eventsubscriptions""", alias="EventSubscriptions")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-name""", alias="Name")
    ResiliencyPolicyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html#cfn-resiliencehub-app-resiliencypolicyarn""", alias="ResiliencyPolicyArn")
    

    @property
    def tropo_type(self) -> troposphere.resiliencehub.App:
        from troposphere.resiliencehub import App as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.resiliencehub import App as TropoT
        return resource_to_troposphere(self, TropoT)


class ResiliencyPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html
    Properties:
        - Name: Policy
        - Name: PolicyDescription
        - Name: Tier
        - Name: PolicyName
        - Name: DataLocationConstraint
        - Name: Tags
    Attributes:
        - Name: PolicyArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Policy_: Dict[str, 'FailurePolicy'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-policy""", alias="Policy")
    PolicyDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-policydescription""", alias="PolicyDescription")
    Tier_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-tier""", alias="Tier")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-policyname""", alias="PolicyName")
    DataLocationConstraint_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-datalocationconstraint""", alias="DataLocationConstraint")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html#cfn-resiliencehub-resiliencypolicy-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.resiliencehub.ResiliencyPolicy:
        from troposphere.resiliencehub import ResiliencyPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.resiliencehub import ResiliencyPolicy as TropoT
        return resource_to_troposphere(self, TropoT)

