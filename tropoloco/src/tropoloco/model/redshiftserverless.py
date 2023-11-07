from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class Namespace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html
    Properties:
        - Name: Status
        - Name: NamespaceName
        - Name: AdminUsername
        - Name: CreationDate
        - Name: IamRoles
        - Name: NamespaceArn
        - Name: KmsKeyId
        - Name: DbName
        - Name: NamespaceId
        - Name: DefaultIamRoleArn
        - Name: LogExports
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-status""", alias="Status")
    NamespaceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-namespacename""", alias="NamespaceName")
    AdminUsername_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-adminusername""", alias="AdminUsername")
    CreationDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-creationdate""", alias="CreationDate")
    IamRoles_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-iamroles""", alias="IamRoles")
    NamespaceArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-namespacearn""", alias="NamespaceArn")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-kmskeyid""", alias="KmsKeyId")
    DbName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-dbname""", alias="DbName")
    NamespaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-namespaceid""", alias="NamespaceId")
    DefaultIamRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-defaultiamrolearn""", alias="DefaultIamRoleArn")
    LogExports_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-logexports""", alias="LogExports")
    


    @property
    def tropo_type(self) -> troposphere.redshiftserverless.Namespace:
        from troposphere.redshiftserverless import Namespace as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ConfigParameter(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html
    Properties:
        - Name: ParameterValue
        - Name: ParameterKey
    
    """
    
    ParameterValue_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html#cfn-redshiftserverless-workgroup-configparameter-parametervalue""", alias="ParameterValue")
    ParameterKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html#cfn-redshiftserverless-workgroup-configparameter-parameterkey""", alias="ParameterKey")
    


    @property
    def tropo_type(self) -> troposphere.redshiftserverless.ConfigParameter:
        from troposphere.redshiftserverless import ConfigParameter as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Endpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-endpoint.html
    Properties:
        - Name: Address
        - Name: VpcEndpoints
        - Name: Port
    
    """
    
    Address_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-endpoint.html#cfn-redshiftserverless-workgroup-endpoint-address""", alias="Address")
    VpcEndpoints_: Optional[List['VpcEndpoint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-endpoint.html#cfn-redshiftserverless-workgroup-endpoint-vpcendpoints""", alias="VpcEndpoints")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-endpoint.html#cfn-redshiftserverless-workgroup-endpoint-port""", alias="Port")
    


    @property
    def tropo_type(self) -> troposphere.redshiftserverless.Endpoint:
        from troposphere.redshiftserverless import Endpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkInterface(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html
    Properties:
        - Name: PrivateIpAddress
        - Name: AvailabilityZone
        - Name: SubnetId
        - Name: NetworkInterfaceId
    
    """
    
    PrivateIpAddress_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html#cfn-redshiftserverless-workgroup-networkinterface-privateipaddress""", alias="PrivateIpAddress")
    AvailabilityZone_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html#cfn-redshiftserverless-workgroup-networkinterface-availabilityzone""", alias="AvailabilityZone")
    SubnetId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html#cfn-redshiftserverless-workgroup-networkinterface-subnetid""", alias="SubnetId")
    NetworkInterfaceId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html#cfn-redshiftserverless-workgroup-networkinterface-networkinterfaceid""", alias="NetworkInterfaceId")
    


    @property
    def tropo_type(self) -> troposphere.redshiftserverless.NetworkInterface:
        from troposphere.redshiftserverless import NetworkInterface as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class VpcEndpoint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-vpcendpoint.html
    Properties:
        - Name: VpcId
        - Name: NetworkInterfaces
        - Name: VpcEndpointId
    
    """
    
    VpcId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-vpcendpoint.html#cfn-redshiftserverless-workgroup-vpcendpoint-vpcid""", alias="VpcId")
    NetworkInterfaces_: Optional[List['NetworkInterface']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-vpcendpoint.html#cfn-redshiftserverless-workgroup-vpcendpoint-networkinterfaces""", alias="NetworkInterfaces")
    VpcEndpointId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-vpcendpoint.html#cfn-redshiftserverless-workgroup-vpcendpoint-vpcendpointid""", alias="VpcEndpointId")
    


    @property
    def tropo_type(self) -> troposphere.redshiftserverless.VpcEndpoint:
        from troposphere.redshiftserverless import VpcEndpoint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Workgroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html
    Properties:
        - Name: Status
        - Name: CreationDate
        - Name: WorkgroupName
        - Name: WorkgroupArn
        - Name: BaseCapacity
        - Name: EnhancedVpcRouting
        - Name: WorkgroupId
        - Name: SecurityGroupIds
        - Name: SubnetIds
        - Name: NamespaceName
        - Name: Endpoint
        - Name: ConfigParameters
        - Name: PubliclyAccessible
    
    """
    
    Status_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-status""", alias="Status")
    CreationDate_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-creationdate""", alias="CreationDate")
    WorkgroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-workgroupname""", alias="WorkgroupName")
    WorkgroupArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-workgrouparn""", alias="WorkgroupArn")
    BaseCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-basecapacity""", alias="BaseCapacity")
    EnhancedVpcRouting_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-enhancedvpcrouting""", alias="EnhancedVpcRouting")
    WorkgroupId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-workgroupid""", alias="WorkgroupId")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-subnetids""", alias="SubnetIds")
    NamespaceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-namespacename""", alias="NamespaceName")
    Endpoint_: Optional['Endpoint'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-endpoint""", alias="Endpoint")
    ConfigParameters_: Optional[List['ConfigParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-configparameters""", alias="ConfigParameters")
    PubliclyAccessible_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-publiclyaccessible""", alias="PubliclyAccessible")
    


    @property
    def tropo_type(self) -> troposphere.redshiftserverless.Workgroup:
        from troposphere.redshiftserverless import Workgroup as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Namespace(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html
    Properties:
        - Name: AdminUsername
        - Name: NamespaceName
        - Name: IamRoles
        - Name: KmsKeyId
        - Name: FinalSnapshotName
        - Name: FinalSnapshotRetentionPeriod
        - Name: AdminUserPassword
        - Name: DbName
        - Name: DefaultIamRoleArn
        - Name: Tags
        - Name: LogExports
    Attributes:
        - Name: Namespace.LogExports
        - Name: Namespace.NamespaceName
        - Name: Namespace.CreationDate
        - Name: Namespace.Status
        - Name: Namespace.AdminUsername
        - Name: Namespace.KmsKeyId
        - Name: Namespace.DbName
        - Name: Namespace.IamRoles
        - Name: Namespace.NamespaceArn
        - Name: Namespace.NamespaceId
        - Name: Namespace.DefaultIamRoleArn
        - Name: Namespace
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AdminUsername_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-adminusername""", alias="AdminUsername")
    NamespaceName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-namespacename""", alias="NamespaceName")
    IamRoles_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-iamroles""", alias="IamRoles")
    KmsKeyId_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-kmskeyid""", alias="KmsKeyId")
    FinalSnapshotName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-finalsnapshotname""", alias="FinalSnapshotName")
    FinalSnapshotRetentionPeriod_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-finalsnapshotretentionperiod""", alias="FinalSnapshotRetentionPeriod")
    AdminUserPassword_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-adminuserpassword""", alias="AdminUserPassword")
    DbName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-dbname""", alias="DbName")
    DefaultIamRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-defaultiamrolearn""", alias="DefaultIamRoleArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-tags""", alias="Tags")
    LogExports_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-logexports""", alias="LogExports")
    

    @property
    def tropo_type(self) -> troposphere.redshiftserverless.Namespace:
        from troposphere.redshiftserverless import Namespace as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.redshiftserverless import Namespace as TropoT
        return resource_to_troposphere(self, TropoT)


class Workgroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html
    Properties:
        - Name: NamespaceName
        - Name: ConfigParameters
        - Name: Port
        - Name: WorkgroupName
        - Name: BaseCapacity
        - Name: EnhancedVpcRouting
        - Name: PubliclyAccessible
        - Name: SecurityGroupIds
        - Name: SubnetIds
        - Name: Tags
    Attributes:
        - Name: Workgroup.Endpoint
        - Name: Workgroup.Endpoint.Port
        - Name: Workgroup.SecurityGroupIds
        - Name: Workgroup.CreationDate
        - Name: Workgroup.PubliclyAccessible
        - Name: Workgroup
        - Name: Workgroup.WorkgroupArn
        - Name: Workgroup.WorkgroupName
        - Name: Workgroup.ConfigParameters
        - Name: Workgroup.Status
        - Name: Workgroup.BaseCapacity
        - Name: Workgroup.EnhancedVpcRouting
        - Name: Workgroup.WorkgroupId
        - Name: Workgroup.NamespaceName
        - Name: Workgroup.Endpoint.VpcEndpoints
        - Name: Workgroup.Endpoint.Address
        - Name: Workgroup.SubnetIds
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    NamespaceName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-namespacename""", alias="NamespaceName")
    ConfigParameters_: Optional[List['ConfigParameter']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-configparameters""", alias="ConfigParameters")
    Port_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-port""", alias="Port")
    WorkgroupName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-workgroupname""", alias="WorkgroupName")
    BaseCapacity_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-basecapacity""", alias="BaseCapacity")
    EnhancedVpcRouting_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-enhancedvpcrouting""", alias="EnhancedVpcRouting")
    PubliclyAccessible_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-publiclyaccessible""", alias="PubliclyAccessible")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-subnetids""", alias="SubnetIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.redshiftserverless.Workgroup:
        from troposphere.redshiftserverless import Workgroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.redshiftserverless import Workgroup as TropoT
        return resource_to_troposphere(self, TropoT)

