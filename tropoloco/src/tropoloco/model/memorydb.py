from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Endpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-cluster-endpoint.html
    Properties:
        - Name: Address
        - Name: Port
    
    """
    
    Address_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-cluster-endpoint.html#cfn-memorydb-cluster-endpoint-address""", alias="Address")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-cluster-endpoint.html#cfn-memorydb-cluster-endpoint-port""", alias="Port")
    


    @property
    def tropo_type(self) -> troposphere.memorydb.Endpoint:
        from troposphere.memorydb import Endpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AuthenticationMode(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-user-authenticationmode.html
    Properties:
        - Name: Type
        - Name: Passwords
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-user-authenticationmode.html#cfn-memorydb-user-authenticationmode-type""", alias="Type")
    Passwords_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-user-authenticationmode.html#cfn-memorydb-user-authenticationmode-passwords""", alias="Passwords")
    


    @property
    def tropo_type(self) -> troposphere.memorydb.AuthenticationMode:
        from troposphere.memorydb import AuthenticationMode as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class ACL(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html
    Properties:
        - Name: ACLName
        - Name: UserNames
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ACLName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#cfn-memorydb-acl-aclname""", alias="ACLName")
    UserNames_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#cfn-memorydb-acl-usernames""", alias="UserNames")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#cfn-memorydb-acl-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.memorydb.ACL:
        from troposphere.memorydb import ACL as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.memorydb import ACL as TropoT
        return resource_to_troposphere(self, TropoT)


class Cluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html
    Properties:
        - Name: NumReplicasPerShard
        - Name: Description
        - Name: FinalSnapshotName
        - Name: ParameterGroupName
        - Name: SnapshotArns
        - Name: Port
        - Name: ACLName
        - Name: SnapshotName
        - Name: NumShards
        - Name: TLSEnabled
        - Name: ClusterName
        - Name: SnsTopicArn
        - Name: Tags
        - Name: EngineVersion
        - Name: KmsKeyId
        - Name: SnsTopicStatus
        - Name: SubnetGroupName
        - Name: AutoMinorVersionUpgrade
        - Name: SecurityGroupIds
        - Name: ClusterEndpoint
        - Name: SnapshotWindow
        - Name: SnapshotRetentionLimit
        - Name: DataTiering
        - Name: NodeType
        - Name: MaintenanceWindow
    Attributes:
        - Name: Status
        - Name: ClusterEndpoint.Address
        - Name: ClusterEndpoint.Port
        - Name: ParameterGroupStatus
        - Name: ARN
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NumReplicasPerShard_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-numreplicaspershard""", alias="NumReplicasPerShard")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-description""", alias="Description")
    FinalSnapshotName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-finalsnapshotname""", alias="FinalSnapshotName")
    ParameterGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-parametergroupname""", alias="ParameterGroupName")
    SnapshotArns_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotarns""", alias="SnapshotArns")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-port""", alias="Port")
    ACLName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-aclname""", alias="ACLName")
    SnapshotName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotname""", alias="SnapshotName")
    NumShards_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-numshards""", alias="NumShards")
    TLSEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-tlsenabled""", alias="TLSEnabled")
    ClusterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-clustername""", alias="ClusterName")
    SnsTopicArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snstopicarn""", alias="SnsTopicArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-tags""", alias="Tags")
    EngineVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-engineversion""", alias="EngineVersion")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-kmskeyid""", alias="KmsKeyId")
    SnsTopicStatus_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snstopicstatus""", alias="SnsTopicStatus")
    SubnetGroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-subnetgroupname""", alias="SubnetGroupName")
    AutoMinorVersionUpgrade_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-autominorversionupgrade""", alias="AutoMinorVersionUpgrade")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-securitygroupids""", alias="SecurityGroupIds")
    ClusterEndpoint_: Optional['Endpoint'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-clusterendpoint""", alias="ClusterEndpoint")
    SnapshotWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotwindow""", alias="SnapshotWindow")
    SnapshotRetentionLimit_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotretentionlimit""", alias="SnapshotRetentionLimit")
    DataTiering_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-datatiering""", alias="DataTiering")
    NodeType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-nodetype""", alias="NodeType")
    MaintenanceWindow_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-maintenancewindow""", alias="MaintenanceWindow")
    

    @property
    def tropo_type(self) -> troposphere.memorydb.Cluster:
        from troposphere.memorydb import Cluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.memorydb import Cluster as TropoT
        return resource_to_troposphere(self, TropoT)


class ParameterGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html
    Properties:
        - Name: Description
        - Name: Parameters
        - Name: ParameterGroupName
        - Name: Family
        - Name: Tags
    Attributes:
        - Name: ARN
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-description""", alias="Description")
    Parameters_: Optional[Dict] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-parameters""", alias="Parameters")
    ParameterGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-parametergroupname""", alias="ParameterGroupName")
    Family_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-family""", alias="Family")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.memorydb.ParameterGroup:
        from troposphere.memorydb import ParameterGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.memorydb import ParameterGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class SubnetGroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html
    Properties:
        - Name: Description
        - Name: SubnetGroupName
        - Name: SubnetIds
        - Name: Tags
    Attributes:
        - Name: ARN
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-description""", alias="Description")
    SubnetGroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-subnetgroupname""", alias="SubnetGroupName")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-subnetids""", alias="SubnetIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.memorydb.SubnetGroup:
        from troposphere.memorydb import SubnetGroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.memorydb import SubnetGroup as TropoT
        return resource_to_troposphere(self, TropoT)


class User(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html
    Properties:
        - Name: AuthenticationMode
        - Name: UserName
        - Name: AccessString
        - Name: Tags
    Attributes:
        - Name: Status
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AuthenticationMode_: Optional['AuthenticationMode'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-authenticationmode""", alias="AuthenticationMode")
    UserName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-username""", alias="UserName")
    AccessString_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-accessstring""", alias="AccessString")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.memorydb.User:
        from troposphere.memorydb import User as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.memorydb import User as TropoT
        return resource_to_troposphere(self, TropoT)

