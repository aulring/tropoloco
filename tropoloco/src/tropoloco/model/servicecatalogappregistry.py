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
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-application.html
    Properties:
        - Name: Description
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-application.html#cfn-servicecatalogappregistry-application-description""", alias="Description")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-application.html#cfn-servicecatalogappregistry-application-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-application.html#cfn-servicecatalogappregistry-application-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalogappregistry.Application:
        from troposphere.servicecatalogappregistry import Application as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalogappregistry import Application as TropoT
        return resource_to_troposphere(self, TropoT)


class AttributeGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroup.html
    Properties:
        - Name: Description
        - Name: Attributes
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroup.html#cfn-servicecatalogappregistry-attributegroup-description""", alias="Description")
    Attributes_: Dict =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroup.html#cfn-servicecatalogappregistry-attributegroup-attributes""", alias="Attributes")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroup.html#cfn-servicecatalogappregistry-attributegroup-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroup.html#cfn-servicecatalogappregistry-attributegroup-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalogappregistry.AttributeGroup:
        from troposphere.servicecatalogappregistry import AttributeGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalogappregistry import AttributeGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class AttributeGroupAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroupassociation.html
    Properties:
        - Name: AttributeGroup
        - Name: Application
    Attributes:
        - Name: ApplicationArn
        - Name: AttributeGroupArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AttributeGroup_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroupassociation.html#cfn-servicecatalogappregistry-attributegroupassociation-attributegroup""", alias="AttributeGroup")
    Application_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroupassociation.html#cfn-servicecatalogappregistry-attributegroupassociation-application""", alias="Application")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalogappregistry.AttributeGroupAssociation:
        from troposphere.servicecatalogappregistry import AttributeGroupAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalogappregistry import AttributeGroupAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourceAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-resourceassociation.html
    Properties:
        - Name: Resource
        - Name: ResourceType
        - Name: Application
    Attributes:
        - Name: ResourceArn
        - Name: ApplicationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Resource_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-resourceassociation.html#cfn-servicecatalogappregistry-resourceassociation-resource""", alias="Resource")
    ResourceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-resourceassociation.html#cfn-servicecatalogappregistry-resourceassociation-resourcetype""", alias="ResourceType")
    Application_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-resourceassociation.html#cfn-servicecatalogappregistry-resourceassociation-application""", alias="Application")
    

    @property
    def tropo_type(self) -> troposphere.servicecatalogappregistry.ResourceAssociation:
        from troposphere.servicecatalogappregistry import ResourceAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.servicecatalogappregistry import ResourceAssociation as TropoT
        return resource_to_troposphere(self, TropoT)

