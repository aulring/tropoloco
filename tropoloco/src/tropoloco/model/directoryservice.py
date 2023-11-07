from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class VpcSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html
    Properties:
        - Name: SubnetIds
        - Name: VpcId
    
    """
    
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-subnetids""", alias="SubnetIds")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-vpcid""", alias="VpcId")
    


    @property
    def tropo_type(self) -> troposphere.directoryservice.VpcSettings:
        from troposphere.directoryservice import VpcSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html
    Properties:
        - Name: VpcId
        - Name: SubnetIds
    
    """
    
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-vpcid""", alias="VpcId")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.directoryservice.VpcSettings:
        from troposphere.directoryservice import VpcSettings as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class MicrosoftAD(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html
    Properties:
        - Name: CreateAlias
        - Name: Edition
        - Name: EnableSso
        - Name: Name
        - Name: Password
        - Name: ShortName
        - Name: VpcSettings
    Attributes:
        - Name: Alias
        - Name: DnsIpAddresses
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CreateAlias_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-createalias""", alias="CreateAlias")
    Edition_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-edition""", alias="Edition")
    EnableSso_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-enablesso""", alias="EnableSso")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-name""", alias="Name")
    Password_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-password""", alias="Password")
    ShortName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-shortname""", alias="ShortName")
    VpcSettings_: 'VpcSettings' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-vpcsettings""", alias="VpcSettings")
    

    @property
    def tropo_type(self) -> troposphere.directoryservice.MicrosoftAD:
        from troposphere.directoryservice import MicrosoftAD as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.directoryservice import MicrosoftAD as TropoT
        return resource_to_troposphere(self, TropoT)


class SimpleAD(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html
    Properties:
        - Name: Description
        - Name: VpcSettings
        - Name: Size
        - Name: CreateAlias
        - Name: EnableSso
        - Name: ShortName
        - Name: Name
        - Name: Password
    Attributes:
        - Name: DirectoryId
        - Name: Alias
        - Name: DnsIpAddresses
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-description""", alias="Description")
    VpcSettings_: 'VpcSettings' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-vpcsettings""", alias="VpcSettings")
    Size_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-size""", alias="Size")
    CreateAlias_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-createalias""", alias="CreateAlias")
    EnableSso_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-enablesso""", alias="EnableSso")
    ShortName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-shortname""", alias="ShortName")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-name""", alias="Name")
    Password_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-password""", alias="Password")
    

    @property
    def tropo_type(self) -> troposphere.directoryservice.SimpleAD:
        from troposphere.directoryservice import SimpleAD as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.directoryservice import SimpleAD as TropoT
        return resource_to_troposphere(self, TropoT)

