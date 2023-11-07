from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class SSESpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dax-cluster-ssespecification.html
    Properties:
        - Name: SSEEnabled
    
    """
    
    SSEEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dax-cluster-ssespecification.html#cfn-dax-cluster-ssespecification-sseenabled""", alias="SSEEnabled")
    


    @property
    def tropo_type(self) -> troposphere.dax.SSESpecification:
        from troposphere.dax import SSESpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Cluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html
    Properties:
        - Name: SSESpecification
        - Name: Description
        - Name: ReplicationFactor
        - Name: ParameterGroupName
        - Name: AvailabilityZones
        - Name: IAMRoleARN
        - Name: SubnetGroupName
        - Name: PreferredMaintenanceWindow
        - Name: ClusterEndpointEncryptionType
        - Name: NotificationTopicARN
        - Name: SecurityGroupIds
        - Name: NodeType
        - Name: ClusterName
        - Name: Tags
    Attributes:
        - Name: ClusterDiscoveryEndpointURL
        - Name: ClusterDiscoveryEndpoint
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SSESpecification_: Optional['SSESpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-ssespecification""", alias="SSESpecification")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-description""", alias="Description")
    ReplicationFactor_: int =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-replicationfactor""", alias="ReplicationFactor")
    ParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-parametergroupname""", alias="ParameterGroupName")
    AvailabilityZones_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-availabilityzones""", alias="AvailabilityZones")
    IAMRoleARN_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-iamrolearn""", alias="IAMRoleARN")
    SubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-subnetgroupname""", alias="SubnetGroupName")
    PreferredMaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-preferredmaintenancewindow""", alias="PreferredMaintenanceWindow")
    ClusterEndpointEncryptionType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-clusterendpointencryptiontype""", alias="ClusterEndpointEncryptionType")
    NotificationTopicARN_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-notificationtopicarn""", alias="NotificationTopicARN")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-securitygroupids""", alias="SecurityGroupIds")
    NodeType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-nodetype""", alias="NodeType")
    ClusterName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-clustername""", alias="ClusterName")
    Tags_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html#cfn-dax-cluster-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.dax.Cluster:
        from troposphere.dax import Cluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.dax import Cluster as TropoT
        return resource_to_troposphere(self, TropoT)


class ParameterGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-parametergroup.html
    Properties:
        - Name: ParameterNameValues
        - Name: Description
        - Name: ParameterGroupName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ParameterNameValues_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-parametergroup.html#cfn-dax-parametergroup-parameternamevalues""", alias="ParameterNameValues")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-parametergroup.html#cfn-dax-parametergroup-description""", alias="Description")
    ParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-parametergroup.html#cfn-dax-parametergroup-parametergroupname""", alias="ParameterGroupName")
    

    @property
    def tropo_type(self) -> troposphere.dax.ParameterGroup:
        from troposphere.dax import ParameterGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.dax import ParameterGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class SubnetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-subnetgroup.html
    Properties:
        - Name: Description
        - Name: SubnetGroupName
        - Name: SubnetIds
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-subnetgroup.html#cfn-dax-subnetgroup-description""", alias="Description")
    SubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-subnetgroup.html#cfn-dax-subnetgroup-subnetgroupname""", alias="SubnetGroupName")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-subnetgroup.html#cfn-dax-subnetgroup-subnetids""", alias="SubnetIds")
    

    @property
    def tropo_type(self) -> troposphere.dax.SubnetGroup:
        from troposphere.dax import SubnetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.dax import SubnetGroup as TropoT
        return resource_to_troposphere(self, TropoT)

