from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class IEMap(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html
    Properties:
        - Name: ACCOUNT
        - Name: ORGUNIT
    
    """
    
    ACCOUNT_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-account""", alias="ACCOUNT")
    ORGUNIT_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-orgunit""", alias="ORGUNIT")
    


    @property
    def tropo_type(self) -> troposphere.fms.IEMap:
        from troposphere.fms import IEMap as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class NetworkFirewallPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html
    Properties:
        - Name: FirewallDeploymentModel
    
    """
    
    FirewallDeploymentModel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html#cfn-fms-policy-networkfirewallpolicy-firewalldeploymentmodel""", alias="FirewallDeploymentModel")
    


    @property
    def tropo_type(self) -> troposphere.fms.NetworkFirewallPolicy:
        from troposphere.fms import NetworkFirewallPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PolicyOption(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html
    Properties:
        - Name: NetworkFirewallPolicy
        - Name: ThirdPartyFirewallPolicy
    
    """
    
    NetworkFirewallPolicy_: Optional['NetworkFirewallPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html#cfn-fms-policy-policyoption-networkfirewallpolicy""", alias="NetworkFirewallPolicy")
    ThirdPartyFirewallPolicy_: Optional['ThirdPartyFirewallPolicy'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html#cfn-fms-policy-policyoption-thirdpartyfirewallpolicy""", alias="ThirdPartyFirewallPolicy")
    


    @property
    def tropo_type(self) -> troposphere.fms.PolicyOption:
        from troposphere.fms import PolicyOption as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PolicyTag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.fms.PolicyTag:
        from troposphere.fms import PolicyTag as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ResourceTag(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html
    Properties:
        - Name: Value
        - Name: Key
    
    """
    
    Value_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-value""", alias="Value")
    Key_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-key""", alias="Key")
    


    @property
    def tropo_type(self) -> troposphere.fms.ResourceTag:
        from troposphere.fms import ResourceTag as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SecurityServicePolicyData(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html
    Properties:
        - Name: ManagedServiceData
        - Name: Type
        - Name: PolicyOption
    
    """
    
    ManagedServiceData_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html#cfn-fms-policy-securityservicepolicydata-managedservicedata""", alias="ManagedServiceData")
    Type_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html#cfn-fms-policy-securityservicepolicydata-type""", alias="Type")
    PolicyOption_: Optional['PolicyOption'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html#cfn-fms-policy-securityservicepolicydata-policyoption""", alias="PolicyOption")
    


    @property
    def tropo_type(self) -> troposphere.fms.SecurityServicePolicyData:
        from troposphere.fms import SecurityServicePolicyData as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ThirdPartyFirewallPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html
    Properties:
        - Name: FirewallDeploymentModel
    
    """
    
    FirewallDeploymentModel_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html#cfn-fms-policy-thirdpartyfirewallpolicy-firewalldeploymentmodel""", alias="FirewallDeploymentModel")
    


    @property
    def tropo_type(self) -> troposphere.fms.ThirdPartyFirewallPolicy:
        from troposphere.fms import ThirdPartyFirewallPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class NotificationChannel(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html
    Properties:
        - Name: SnsTopicArn
        - Name: SnsRoleName
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    SnsTopicArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snstopicarn""", alias="SnsTopicArn")
    SnsRoleName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snsrolename""", alias="SnsRoleName")
    

    @property
    def tropo_type(self) -> troposphere.fms.NotificationChannel:
        from troposphere.fms import NotificationChannel as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.fms import NotificationChannel as TropoT
        return resource_to_troposphere(self, TropoT)


class Policy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html
    Properties:
        - Name: ResourcesCleanUp
        - Name: ResourceTags
        - Name: ExcludeResourceTags
        - Name: ResourceType
        - Name: ResourceSetIds
        - Name: SecurityServicePolicyData
        - Name: RemediationEnabled
        - Name: DeleteAllPolicyResources
        - Name: ExcludeMap
        - Name: IncludeMap
        - Name: PolicyDescription
        - Name: PolicyName
        - Name: ResourceTypeList
        - Name: Tags
    Attributes:
        - Name: Id
        - Name: Arn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ResourcesCleanUp_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcescleanup""", alias="ResourcesCleanUp")
    ResourceTags_: Optional[List['ResourceTag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetags""", alias="ResourceTags")
    ExcludeResourceTags_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excluderesourcetags""", alias="ExcludeResourceTags")
    ResourceType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetype""", alias="ResourceType")
    ResourceSetIds_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcesetids""", alias="ResourceSetIds")
    SecurityServicePolicyData_: 'SecurityServicePolicyData' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-securityservicepolicydata""", alias="SecurityServicePolicyData")
    RemediationEnabled_: bool =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-remediationenabled""", alias="RemediationEnabled")
    DeleteAllPolicyResources_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-deleteallpolicyresources""", alias="DeleteAllPolicyResources")
    ExcludeMap_: Optional['IEMap'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excludemap""", alias="ExcludeMap")
    IncludeMap_: Optional['IEMap'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-includemap""", alias="IncludeMap")
    PolicyDescription_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-policydescription""", alias="PolicyDescription")
    PolicyName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-policyname""", alias="PolicyName")
    ResourceTypeList_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetypelist""", alias="ResourceTypeList")
    Tags_: Optional[List['PolicyTag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.fms.Policy:
        from troposphere.fms import Policy as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.fms import Policy as TropoT
        return resource_to_troposphere(self, TropoT)


class ResourceSet(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html
    Properties:
        - Name: Description
        - Name: ResourceTypeList
        - Name: Resources
        - Name: Tags
        - Name: Name
    Attributes:
        - Name: Id
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html#cfn-fms-resourceset-description""", alias="Description")
    ResourceTypeList_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html#cfn-fms-resourceset-resourcetypelist""", alias="ResourceTypeList")
    Resources_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html#cfn-fms-resourceset-resources""", alias="Resources")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html#cfn-fms-resourceset-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html#cfn-fms-resourceset-name""", alias="Name")
    

    @property
    def tropo_type(self) -> troposphere.fms.ResourceSet:
        from troposphere.fms import ResourceSet as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.fms import ResourceSet as TropoT
        return resource_to_troposphere(self, TropoT)

