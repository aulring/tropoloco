from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class IncludedProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourceexplorer2-view-includedproperty.html
    Properties:
        - Name: Name
    
    """
    
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourceexplorer2-view-includedproperty.html#cfn-resourceexplorer2-view-includedproperty-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.resourceexplorer2.IncludedProperty:
        from troposphere.resourceexplorer2 import IncludedProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SearchFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourceexplorer2-view-searchfilter.html
    Properties:
        - Name: FilterString
    
    """
    
    FilterString_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourceexplorer2-view-searchfilter.html#cfn-resourceexplorer2-view-searchfilter-filterstring""", alias="FilterString")
    


    @property
    def tropo_type(self) -> troposphere.resourceexplorer2.SearchFilter:
        from troposphere.resourceexplorer2 import SearchFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class DefaultViewAssociation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-defaultviewassociation.html
    Properties:
        - Name: ViewArn
    Attributes:
        - Name: AssociatedAwsPrincipal
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ViewArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-defaultviewassociation.html#cfn-resourceexplorer2-defaultviewassociation-viewarn""", alias="ViewArn")
    

    @property
    def tropo_type(self) -> troposphere.resourceexplorer2.DefaultViewAssociation:
        from troposphere.resourceexplorer2 import DefaultViewAssociation as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.resourceexplorer2 import DefaultViewAssociation as TropoT
        return resource_to_troposphere(self, TropoT)


class Index(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-index.html
    Properties:
        - Name: Type
        - Name: Tags
    Attributes:
        - Name: Arn
        - Name: IndexState
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-index.html#cfn-resourceexplorer2-index-type""", alias="Type")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-index.html#cfn-resourceexplorer2-index-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.resourceexplorer2.Index:
        from troposphere.resourceexplorer2 import Index as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.resourceexplorer2 import Index as TropoT
        return resource_to_troposphere(self, TropoT)


class View(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html
    Properties:
        - Name: Filters
        - Name: Scope
        - Name: IncludedProperties
        - Name: Tags
        - Name: ViewName
    Attributes:
        - Name: ViewArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Filters_: Optional['SearchFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html#cfn-resourceexplorer2-view-filters""", alias="Filters")
    Scope_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html#cfn-resourceexplorer2-view-scope""", alias="Scope")
    IncludedProperties_: Optional[List['IncludedProperty']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html#cfn-resourceexplorer2-view-includedproperties""", alias="IncludedProperties")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html#cfn-resourceexplorer2-view-tags""", alias="Tags")
    ViewName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html#cfn-resourceexplorer2-view-viewname""", alias="ViewName")
    

    @property
    def tropo_type(self) -> troposphere.resourceexplorer2.View:
        from troposphere.resourceexplorer2 import View as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.resourceexplorer2 import View as TropoT
        return resource_to_troposphere(self, TropoT)

