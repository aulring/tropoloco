from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class ClusterLogging(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-clusterlogging.html
    Properties:
        - Name: EnabledTypes
    
    """
    
    EnabledTypes_: Optional[List['LoggingTypeConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-clusterlogging.html#cfn-eks-cluster-clusterlogging-enabledtypes""", alias="EnabledTypes")
    


    @property
    def tropo_type(self) -> troposphere.eks.ClusterLogging:
        from troposphere.eks import ClusterLogging as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ControlPlanePlacement(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-controlplaneplacement.html
    Properties:
        - Name: GroupName
    
    """
    
    GroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-controlplaneplacement.html#cfn-eks-cluster-controlplaneplacement-groupname""", alias="GroupName")
    


    @property
    def tropo_type(self) -> troposphere.eks.ControlPlanePlacement:
        from troposphere.eks import ControlPlanePlacement as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EncryptionConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-encryptionconfig.html
    Properties:
        - Name: Resources
        - Name: Provider
    
    """
    
    Resources_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-encryptionconfig.html#cfn-eks-cluster-encryptionconfig-resources""", alias="Resources")
    Provider_: Optional['Provider'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-encryptionconfig.html#cfn-eks-cluster-encryptionconfig-provider""", alias="Provider")
    


    @property
    def tropo_type(self) -> troposphere.eks.EncryptionConfig:
        from troposphere.eks import EncryptionConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KubernetesNetworkConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-kubernetesnetworkconfig.html
    Properties:
        - Name: ServiceIpv4Cidr
        - Name: ServiceIpv6Cidr
        - Name: IpFamily
    
    """
    
    ServiceIpv4Cidr_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-kubernetesnetworkconfig.html#cfn-eks-cluster-kubernetesnetworkconfig-serviceipv4cidr""", alias="ServiceIpv4Cidr")
    ServiceIpv6Cidr_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-kubernetesnetworkconfig.html#cfn-eks-cluster-kubernetesnetworkconfig-serviceipv6cidr""", alias="ServiceIpv6Cidr")
    IpFamily_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-kubernetesnetworkconfig.html#cfn-eks-cluster-kubernetesnetworkconfig-ipfamily""", alias="IpFamily")
    


    @property
    def tropo_type(self) -> troposphere.eks.KubernetesNetworkConfig:
        from troposphere.eks import KubernetesNetworkConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Logging(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-logging.html
    Properties:
        - Name: ClusterLogging
    
    """
    
    ClusterLogging_: Optional['ClusterLogging'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-logging.html#cfn-eks-cluster-logging-clusterlogging""", alias="ClusterLogging")
    


    @property
    def tropo_type(self) -> troposphere.eks.Logging:
        from troposphere.eks import Logging as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LoggingTypeConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-loggingtypeconfig.html
    Properties:
        - Name: Type
    
    """
    
    Type_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-loggingtypeconfig.html#cfn-eks-cluster-loggingtypeconfig-type""", alias="Type")
    


    @property
    def tropo_type(self) -> troposphere.eks.LoggingTypeConfig:
        from troposphere.eks import LoggingTypeConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OutpostConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-outpostconfig.html
    Properties:
        - Name: OutpostArns
        - Name: ControlPlanePlacement
        - Name: ControlPlaneInstanceType
    
    """
    
    OutpostArns_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-outpostconfig.html#cfn-eks-cluster-outpostconfig-outpostarns""", alias="OutpostArns")
    ControlPlanePlacement_: Optional['ControlPlanePlacement'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-outpostconfig.html#cfn-eks-cluster-outpostconfig-controlplaneplacement""", alias="ControlPlanePlacement")
    ControlPlaneInstanceType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-outpostconfig.html#cfn-eks-cluster-outpostconfig-controlplaneinstancetype""", alias="ControlPlaneInstanceType")
    


    @property
    def tropo_type(self) -> troposphere.eks.OutpostConfig:
        from troposphere.eks import OutpostConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Provider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-provider.html
    Properties:
        - Name: KeyArn
    
    """
    
    KeyArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-provider.html#cfn-eks-cluster-provider-keyarn""", alias="KeyArn")
    


    @property
    def tropo_type(self) -> troposphere.eks.Provider:
        from troposphere.eks import Provider as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourcesVpcConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html
    Properties:
        - Name: EndpointPublicAccess
        - Name: PublicAccessCidrs
        - Name: EndpointPrivateAccess
        - Name: SecurityGroupIds
        - Name: SubnetIds
    
    """
    
    EndpointPublicAccess_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html#cfn-eks-cluster-resourcesvpcconfig-endpointpublicaccess""", alias="EndpointPublicAccess")
    PublicAccessCidrs_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html#cfn-eks-cluster-resourcesvpcconfig-publicaccesscidrs""", alias="PublicAccessCidrs")
    EndpointPrivateAccess_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html#cfn-eks-cluster-resourcesvpcconfig-endpointprivateaccess""", alias="EndpointPrivateAccess")
    SecurityGroupIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html#cfn-eks-cluster-resourcesvpcconfig-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html#cfn-eks-cluster-resourcesvpcconfig-subnetids""", alias="SubnetIds")
    


    @property
    def tropo_type(self) -> troposphere.eks.ResourcesVpcConfig:
        from troposphere.eks import ResourcesVpcConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Label(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-label.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-label.html#cfn-eks-fargateprofile-label-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-label.html#cfn-eks-fargateprofile-label-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.eks.Label:
        from troposphere.eks import Label as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Selector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-selector.html
    Properties:
        - Name: Labels
        - Name: Namespace
    
    """
    
    Labels_: Optional[List['Label']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-selector.html#cfn-eks-fargateprofile-selector-labels""", alias="Labels")
    Namespace_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-selector.html#cfn-eks-fargateprofile-selector-namespace""", alias="Namespace")
    


    @property
    def tropo_type(self) -> troposphere.eks.Selector:
        from troposphere.eks import Selector as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class OidcIdentityProviderConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-oidcidentityproviderconfig.html
    Properties:
        - Name: UsernamePrefix
        - Name: GroupsPrefix
        - Name: IssuerUrl
        - Name: RequiredClaims
        - Name: ClientId
        - Name: GroupsClaim
        - Name: UsernameClaim
    
    """
    
    UsernamePrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-oidcidentityproviderconfig.html#cfn-eks-identityproviderconfig-oidcidentityproviderconfig-usernameprefix""", alias="UsernamePrefix")
    GroupsPrefix_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-oidcidentityproviderconfig.html#cfn-eks-identityproviderconfig-oidcidentityproviderconfig-groupsprefix""", alias="GroupsPrefix")
    IssuerUrl_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-oidcidentityproviderconfig.html#cfn-eks-identityproviderconfig-oidcidentityproviderconfig-issuerurl""", alias="IssuerUrl")
    RequiredClaims_: Optional[List['RequiredClaim']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-oidcidentityproviderconfig.html#cfn-eks-identityproviderconfig-oidcidentityproviderconfig-requiredclaims""", alias="RequiredClaims")
    ClientId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-oidcidentityproviderconfig.html#cfn-eks-identityproviderconfig-oidcidentityproviderconfig-clientid""", alias="ClientId")
    GroupsClaim_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-oidcidentityproviderconfig.html#cfn-eks-identityproviderconfig-oidcidentityproviderconfig-groupsclaim""", alias="GroupsClaim")
    UsernameClaim_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-oidcidentityproviderconfig.html#cfn-eks-identityproviderconfig-oidcidentityproviderconfig-usernameclaim""", alias="UsernameClaim")
    


    @property
    def tropo_type(self) -> troposphere.eks.OidcIdentityProviderConfig:
        from troposphere.eks import OidcIdentityProviderConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RequiredClaim(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-requiredclaim.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-requiredclaim.html#cfn-eks-identityproviderconfig-requiredclaim-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-requiredclaim.html#cfn-eks-identityproviderconfig-requiredclaim-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.eks.RequiredClaim:
        from troposphere.eks import RequiredClaim as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class LaunchTemplateSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-launchtemplatespecification.html
    Properties:
        - Name: Version
        - Name: Id
        - Name: Name
    
    """
    
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-launchtemplatespecification.html#cfn-eks-nodegroup-launchtemplatespecification-version""", alias="Version")
    Id_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-launchtemplatespecification.html#cfn-eks-nodegroup-launchtemplatespecification-id""", alias="Id")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-launchtemplatespecification.html#cfn-eks-nodegroup-launchtemplatespecification-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.eks.LaunchTemplateSpecification:
        from troposphere.eks import LaunchTemplateSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class RemoteAccess(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-remoteaccess.html
    Properties:
        - Name: SourceSecurityGroups
        - Name: Ec2SshKey
    
    """
    
    SourceSecurityGroups_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-remoteaccess.html#cfn-eks-nodegroup-remoteaccess-sourcesecuritygroups""", alias="SourceSecurityGroups")
    Ec2SshKey_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-remoteaccess.html#cfn-eks-nodegroup-remoteaccess-ec2sshkey""", alias="Ec2SshKey")
    


    @property
    def tropo_type(self) -> troposphere.eks.RemoteAccess:
        from troposphere.eks import RemoteAccess as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ScalingConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html
    Properties:
        - Name: MinSize
        - Name: DesiredSize
        - Name: MaxSize
    
    """
    
    MinSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html#cfn-eks-nodegroup-scalingconfig-minsize""", alias="MinSize")
    DesiredSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html#cfn-eks-nodegroup-scalingconfig-desiredsize""", alias="DesiredSize")
    MaxSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html#cfn-eks-nodegroup-scalingconfig-maxsize""", alias="MaxSize")
    


    @property
    def tropo_type(self) -> troposphere.eks.ScalingConfig:
        from troposphere.eks import ScalingConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class Taint(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-taint.html
    Properties:
        - Name: Value
        - Name: Effect
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-taint.html#cfn-eks-nodegroup-taint-value""", alias="Value")
    Effect_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-taint.html#cfn-eks-nodegroup-taint-effect""", alias="Effect")
    Key_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-taint.html#cfn-eks-nodegroup-taint-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.eks.Taint:
        from troposphere.eks import Taint as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class UpdateConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html
    Properties:
        - Name: MaxUnavailablePercentage
        - Name: MaxUnavailable
    
    """
    
    MaxUnavailablePercentage_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html#cfn-eks-nodegroup-updateconfig-maxunavailablepercentage""", alias="MaxUnavailablePercentage")
    MaxUnavailable_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html#cfn-eks-nodegroup-updateconfig-maxunavailable""", alias="MaxUnavailable")
    


    @property
    def tropo_type(self) -> troposphere.eks.UpdateConfig:
        from troposphere.eks import UpdateConfig as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Addon(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html
    Properties:
        - Name: PreserveOnDelete
        - Name: AddonVersion
        - Name: ServiceAccountRoleArn
        - Name: ClusterName
        - Name: AddonName
        - Name: ResolveConflicts
        - Name: Tags
        - Name: ConfigurationValues
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    PreserveOnDelete_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-preserveondelete""", alias="PreserveOnDelete")
    AddonVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-addonversion""", alias="AddonVersion")
    ServiceAccountRoleArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-serviceaccountrolearn""", alias="ServiceAccountRoleArn")
    ClusterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-clustername""", alias="ClusterName")
    AddonName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-addonname""", alias="AddonName")
    ResolveConflicts_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-resolveconflicts""", alias="ResolveConflicts")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-tags""", alias="Tags")
    ConfigurationValues_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-configurationvalues""", alias="ConfigurationValues")
    

    @property
    def tropo_type(self) -> troposphere.eks.Addon:
        from troposphere.eks import Addon as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.eks import Addon as TropoT
        return resource_to_troposphere(self, TropoT)


class Cluster(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html
    Properties:
        - Name: Logging
        - Name: Version
        - Name: OutpostConfig
        - Name: EncryptionConfig
        - Name: KubernetesNetworkConfig
        - Name: RoleArn
        - Name: ResourcesVpcConfig
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Endpoint
        - Name: ClusterSecurityGroupId
        - Name: EncryptionConfigKeyArn
        - Name: Id
        - Name: CertificateAuthorityData
        - Name: Arn
        - Name: KubernetesNetworkConfig.ServiceIpv6Cidr
        - Name: OpenIdConnectIssuerUrl
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Logging_: Optional['Logging'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-logging""", alias="Logging")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-version""", alias="Version")
    OutpostConfig_: Optional['OutpostConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-outpostconfig""", alias="OutpostConfig")
    EncryptionConfig_: Optional[List['EncryptionConfig']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-encryptionconfig""", alias="EncryptionConfig")
    KubernetesNetworkConfig_: Optional['KubernetesNetworkConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-kubernetesnetworkconfig""", alias="KubernetesNetworkConfig")
    RoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-rolearn""", alias="RoleArn")
    ResourcesVpcConfig_: 'ResourcesVpcConfig' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-resourcesvpcconfig""", alias="ResourcesVpcConfig")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-tags""", alias="Tags")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.eks.Cluster:
        from troposphere.eks import Cluster as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.eks import Cluster as TropoT
        return resource_to_troposphere(self, TropoT)


class FargateProfile(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html
    Properties:
        - Name: Subnets
        - Name: FargateProfileName
        - Name: ClusterName
        - Name: PodExecutionRoleArn
        - Name: Selectors
        - Name: Tags
    Attributes:
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Subnets_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-subnets""", alias="Subnets")
    FargateProfileName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-fargateprofilename""", alias="FargateProfileName")
    ClusterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-clustername""", alias="ClusterName")
    PodExecutionRoleArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-podexecutionrolearn""", alias="PodExecutionRoleArn")
    Selectors_: List['Selector'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-selectors""", alias="Selectors")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.eks.FargateProfile:
        from troposphere.eks import FargateProfile as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.eks import FargateProfile as TropoT
        return resource_to_troposphere(self, TropoT)


class IdentityProviderConfig(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-identityproviderconfig.html
    Properties:
        - Name: Type
        - Name: ClusterName
        - Name: IdentityProviderConfigName
        - Name: Oidc
        - Name: Tags
    Attributes:
        - Name: IdentityProviderConfigArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-identityproviderconfig.html#cfn-eks-identityproviderconfig-type""", alias="Type")
    ClusterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-identityproviderconfig.html#cfn-eks-identityproviderconfig-clustername""", alias="ClusterName")
    IdentityProviderConfigName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-identityproviderconfig.html#cfn-eks-identityproviderconfig-identityproviderconfigname""", alias="IdentityProviderConfigName")
    Oidc_: Optional['OidcIdentityProviderConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-identityproviderconfig.html#cfn-eks-identityproviderconfig-oidc""", alias="Oidc")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-identityproviderconfig.html#cfn-eks-identityproviderconfig-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.eks.IdentityProviderConfig:
        from troposphere.eks import IdentityProviderConfig as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.eks import IdentityProviderConfig as TropoT
        return resource_to_troposphere(self, TropoT)


class Nodegroup(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html
    Properties:
        - Name: UpdateConfig
        - Name: ScalingConfig
        - Name: Labels
        - Name: Taints
        - Name: CapacityType
        - Name: ReleaseVersion
        - Name: NodegroupName
        - Name: NodeRole
        - Name: Subnets
        - Name: AmiType
        - Name: ForceUpdateEnabled
        - Name: Version
        - Name: LaunchTemplate
        - Name: RemoteAccess
        - Name: DiskSize
        - Name: ClusterName
        - Name: InstanceTypes
        - Name: Tags
    Attributes:
        - Name: NodegroupName
        - Name: ClusterName
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    UpdateConfig_: Optional['UpdateConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-updateconfig""", alias="UpdateConfig")
    ScalingConfig_: Optional['ScalingConfig'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-scalingconfig""", alias="ScalingConfig")
    Labels_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-labels""", alias="Labels")
    Taints_: Optional[List['Taint']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-taints""", alias="Taints")
    CapacityType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-capacitytype""", alias="CapacityType")
    ReleaseVersion_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-releaseversion""", alias="ReleaseVersion")
    NodegroupName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-nodegroupname""", alias="NodegroupName")
    NodeRole_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-noderole""", alias="NodeRole")
    Subnets_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-subnets""", alias="Subnets")
    AmiType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-amitype""", alias="AmiType")
    ForceUpdateEnabled_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-forceupdateenabled""", alias="ForceUpdateEnabled")
    Version_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-version""", alias="Version")
    LaunchTemplate_: Optional['LaunchTemplateSpecification'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-launchtemplate""", alias="LaunchTemplate")
    RemoteAccess_: Optional['RemoteAccess'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-remoteaccess""", alias="RemoteAccess")
    DiskSize_: Optional[int] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-disksize""", alias="DiskSize")
    ClusterName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-clustername""", alias="ClusterName")
    InstanceTypes_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-instancetypes""", alias="InstanceTypes")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.eks.Nodegroup:
        from troposphere.eks import Nodegroup as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.eks import Nodegroup as TropoT
        return resource_to_troposphere(self, TropoT)

