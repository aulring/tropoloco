from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DNSTargetResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html
    Properties:
        - Name: TargetResource
        - Name: RecordType
        - Name: DomainName
        - Name: HostedZoneArn
        - Name: RecordSetId
    
    """
    
    TargetResource_: Optional['TargetResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-targetresource""", alias="TargetResource")
    RecordType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-recordtype""", alias="RecordType")
    DomainName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-domainname""", alias="DomainName")
    HostedZoneArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-hostedzonearn""", alias="HostedZoneArn")
    RecordSetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-recordsetid""", alias="RecordSetId")
    


    @property
    def tropo_type(self) -> troposphere.route53recoveryreadiness.DNSTargetResource:
        from troposphere.route53recoveryreadiness import DNSTargetResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NLBResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-nlbresource.html
    Properties:
        - Name: Arn
    
    """
    
    Arn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-nlbresource.html#cfn-route53recoveryreadiness-resourceset-nlbresource-arn""", alias="Arn")
    


    @property
    def tropo_type(self) -> troposphere.route53recoveryreadiness.NLBResource:
        from troposphere.route53recoveryreadiness import NLBResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class R53ResourceRecord(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html
    Properties:
        - Name: DomainName
        - Name: RecordSetId
    
    """
    
    DomainName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-domainname""", alias="DomainName")
    RecordSetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-recordsetid""", alias="RecordSetId")
    


    @property
    def tropo_type(self) -> troposphere.route53recoveryreadiness.R53ResourceRecord:
        from troposphere.route53recoveryreadiness import R53ResourceRecord as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Resource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html
    Properties:
        - Name: ResourceArn
        - Name: DnsTargetResource
        - Name: ReadinessScopes
        - Name: ComponentId
    
    """
    
    ResourceArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-resourcearn""", alias="ResourceArn")
    DnsTargetResource_: Optional['DNSTargetResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-dnstargetresource""", alias="DnsTargetResource")
    ReadinessScopes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-readinessscopes""", alias="ReadinessScopes")
    ComponentId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-componentid""", alias="ComponentId")
    


    @property
    def tropo_type(self) -> troposphere.route53recoveryreadiness.Resource:
        from troposphere.route53recoveryreadiness import Resource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TargetResource(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html
    Properties:
        - Name: R53Resource
        - Name: NLBResource
    
    """
    
    R53Resource_: Optional['R53ResourceRecord'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html#cfn-route53recoveryreadiness-resourceset-targetresource-r53resource""", alias="R53Resource")
    NLBResource_: Optional['NLBResource'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html#cfn-route53recoveryreadiness-resourceset-targetresource-nlbresource""", alias="NLBResource")
    


    @property
    def tropo_type(self) -> troposphere.route53recoveryreadiness.TargetResource:
        from troposphere.route53recoveryreadiness import TargetResource as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Cell(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html
    Properties:
        - Name: CellName
        - Name: Cells
        - Name: Tags
    Attributes:
        - Name: ParentReadinessScopes
        - Name: CellArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CellName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-cellname""", alias="CellName")
    Cells_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-cells""", alias="Cells")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.route53recoveryreadiness.Cell:
        from troposphere.route53recoveryreadiness import Cell as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53recoveryreadiness import Cell as TropoT
        return resource_to_troposphere(self, TropoT)


class ReadinessCheck(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html
    Properties:
        - Name: ResourceSetName
        - Name: ReadinessCheckName
        - Name: Tags
    Attributes:
        - Name: ReadinessCheckArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceSetName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-resourcesetname""", alias="ResourceSetName")
    ReadinessCheckName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-readinesscheckname""", alias="ReadinessCheckName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.route53recoveryreadiness.ReadinessCheck:
        from troposphere.route53recoveryreadiness import ReadinessCheck as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53recoveryreadiness import ReadinessCheck as TropoT
        return resource_to_troposphere(self, TropoT)


class RecoveryGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html
    Properties:
        - Name: RecoveryGroupName
        - Name: Cells
        - Name: Tags
    Attributes:
        - Name: RecoveryGroupArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    RecoveryGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-recoverygroupname""", alias="RecoveryGroupName")
    Cells_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-cells""", alias="Cells")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.route53recoveryreadiness.RecoveryGroup:
        from troposphere.route53recoveryreadiness import RecoveryGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53recoveryreadiness import RecoveryGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourceSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html
    Properties:
        - Name: ResourceSetType
        - Name: ResourceSetName
        - Name: Resources
        - Name: Tags
    Attributes:
        - Name: ResourceSetArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourceSetType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resourcesettype""", alias="ResourceSetType")
    ResourceSetName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resourcesetname""", alias="ResourceSetName")
    Resources_: List['Resource'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resources""", alias="Resources")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.route53recoveryreadiness.ResourceSet:
        from troposphere.route53recoveryreadiness import ResourceSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.route53recoveryreadiness import ResourceSet as TropoT
        return resource_to_troposphere(self, TropoT)

