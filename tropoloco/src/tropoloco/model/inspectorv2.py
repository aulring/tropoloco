from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class DateFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-datefilter.html
    Properties:
        - Name: EndInclusive
        - Name: StartInclusive
    
    """
    
    EndInclusive_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-datefilter.html#cfn-inspectorv2-filter-datefilter-endinclusive""", alias="EndInclusive")
    StartInclusive_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-datefilter.html#cfn-inspectorv2-filter-datefilter-startinclusive""", alias="StartInclusive")
    


    @property
    def tropo_type(self) -> troposphere.inspectorv2.DateFilter:
        from troposphere.inspectorv2 import DateFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class FilterCriteria(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html
    Properties:
        - Name: ResourceTags
        - Name: Ec2InstanceImageId
        - Name: FirstObservedAt
        - Name: InspectorScore
        - Name: Ec2InstanceVpcId
        - Name: LastObservedAt
        - Name: EcrImagePushedAt
        - Name: EcrImageArchitecture
        - Name: RelatedVulnerabilities
        - Name: EcrImageTags
        - Name: VulnerabilityId
        - Name: ComponentType
        - Name: VendorSeverity
        - Name: EcrImageRepositoryName
        - Name: Title
        - Name: ResourceType
        - Name: Severity
        - Name: NetworkProtocol
        - Name: UpdatedAt
        - Name: EcrImageHash
        - Name: PortRange
        - Name: VulnerabilitySource
        - Name: Ec2InstanceSubnetId
        - Name: FindingArn
        - Name: ResourceId
        - Name: FindingStatus
        - Name: VulnerablePackages
        - Name: AwsAccountId
        - Name: ComponentId
        - Name: EcrImageRegistry
        - Name: FindingType
    
    """
    
    ResourceTags_: Optional[List['MapFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-resourcetags""", alias="ResourceTags")
    Ec2InstanceImageId_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ec2instanceimageid""", alias="Ec2InstanceImageId")
    FirstObservedAt_: Optional[List['DateFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-firstobservedat""", alias="FirstObservedAt")
    InspectorScore_: Optional[List['NumberFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-inspectorscore""", alias="InspectorScore")
    Ec2InstanceVpcId_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ec2instancevpcid""", alias="Ec2InstanceVpcId")
    LastObservedAt_: Optional[List['DateFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-lastobservedat""", alias="LastObservedAt")
    EcrImagePushedAt_: Optional[List['DateFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagepushedat""", alias="EcrImagePushedAt")
    EcrImageArchitecture_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagearchitecture""", alias="EcrImageArchitecture")
    RelatedVulnerabilities_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-relatedvulnerabilities""", alias="RelatedVulnerabilities")
    EcrImageTags_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagetags""", alias="EcrImageTags")
    VulnerabilityId_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-vulnerabilityid""", alias="VulnerabilityId")
    ComponentType_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-componenttype""", alias="ComponentType")
    VendorSeverity_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-vendorseverity""", alias="VendorSeverity")
    EcrImageRepositoryName_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagerepositoryname""", alias="EcrImageRepositoryName")
    Title_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-title""", alias="Title")
    ResourceType_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-resourcetype""", alias="ResourceType")
    Severity_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-severity""", alias="Severity")
    NetworkProtocol_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-networkprotocol""", alias="NetworkProtocol")
    UpdatedAt_: Optional[List['DateFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-updatedat""", alias="UpdatedAt")
    EcrImageHash_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagehash""", alias="EcrImageHash")
    PortRange_: Optional[List['PortRangeFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-portrange""", alias="PortRange")
    VulnerabilitySource_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-vulnerabilitysource""", alias="VulnerabilitySource")
    Ec2InstanceSubnetId_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ec2instancesubnetid""", alias="Ec2InstanceSubnetId")
    FindingArn_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-findingarn""", alias="FindingArn")
    ResourceId_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-resourceid""", alias="ResourceId")
    FindingStatus_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-findingstatus""", alias="FindingStatus")
    VulnerablePackages_: Optional[List['PackageFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-vulnerablepackages""", alias="VulnerablePackages")
    AwsAccountId_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-awsaccountid""", alias="AwsAccountId")
    ComponentId_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-componentid""", alias="ComponentId")
    EcrImageRegistry_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimageregistry""", alias="EcrImageRegistry")
    FindingType_: Optional[List['StringFilter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-findingtype""", alias="FindingType")
    


    @property
    def tropo_type(self) -> troposphere.inspectorv2.FilterCriteria:
        from troposphere.inspectorv2 import FilterCriteria as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class MapFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-mapfilter.html
    Properties:
        - Name: Comparison
        - Name: Value
        - Name: Key
    
    """
    
    Comparison_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-mapfilter.html#cfn-inspectorv2-filter-mapfilter-comparison""", alias="Comparison")
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-mapfilter.html#cfn-inspectorv2-filter-mapfilter-value""", alias="Value")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-mapfilter.html#cfn-inspectorv2-filter-mapfilter-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.inspectorv2.MapFilter:
        from troposphere.inspectorv2 import MapFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NumberFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-numberfilter.html
    Properties:
        - Name: LowerInclusive
        - Name: UpperInclusive
    
    """
    
    LowerInclusive_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-numberfilter.html#cfn-inspectorv2-filter-numberfilter-lowerinclusive""", alias="LowerInclusive")
    UpperInclusive_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-numberfilter.html#cfn-inspectorv2-filter-numberfilter-upperinclusive""", alias="UpperInclusive")
    


    @property
    def tropo_type(self) -> troposphere.inspectorv2.NumberFilter:
        from troposphere.inspectorv2 import NumberFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PackageFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html
    Properties:
        - Name: Architecture
        - Name: Version
        - Name: Epoch
        - Name: SourceLayerHash
        - Name: Release
        - Name: Name
    
    """
    
    Architecture_: Optional['StringFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-architecture""", alias="Architecture")
    Version_: Optional['StringFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-version""", alias="Version")
    Epoch_: Optional['NumberFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-epoch""", alias="Epoch")
    SourceLayerHash_: Optional['StringFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-sourcelayerhash""", alias="SourceLayerHash")
    Release_: Optional['StringFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-release""", alias="Release")
    Name_: Optional['StringFilter'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.inspectorv2.PackageFilter:
        from troposphere.inspectorv2 import PackageFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PortRangeFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-portrangefilter.html
    Properties:
        - Name: BeginInclusive
        - Name: EndInclusive
    
    """
    
    BeginInclusive_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-portrangefilter.html#cfn-inspectorv2-filter-portrangefilter-begininclusive""", alias="BeginInclusive")
    EndInclusive_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-portrangefilter.html#cfn-inspectorv2-filter-portrangefilter-endinclusive""", alias="EndInclusive")
    


    @property
    def tropo_type(self) -> troposphere.inspectorv2.PortRangeFilter:
        from troposphere.inspectorv2 import PortRangeFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class StringFilter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-stringfilter.html
    Properties:
        - Name: Comparison
        - Name: Value
    
    """
    
    Comparison_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-stringfilter.html#cfn-inspectorv2-filter-stringfilter-comparison""", alias="Comparison")
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-stringfilter.html#cfn-inspectorv2-filter-stringfilter-value""", alias="Value")
    


    @property
    def tropo_type(self) -> troposphere.inspectorv2.StringFilter:
        from troposphere.inspectorv2 import StringFilter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Filter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html
    Properties:
        - Name: Description
        - Name: FilterCriteria
        - Name: FilterAction
        - Name: Name
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html#cfn-inspectorv2-filter-description""", alias="Description")
    FilterCriteria_: 'FilterCriteria' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html#cfn-inspectorv2-filter-filtercriteria""", alias="FilterCriteria")
    FilterAction_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html#cfn-inspectorv2-filter-filteraction""", alias="FilterAction")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html#cfn-inspectorv2-filter-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.inspectorv2.Filter:
        from troposphere.inspectorv2 import Filter as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.inspectorv2 import Filter as TropoT
        return resource_to_troposphere(self, TropoT)

