from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class IpRule(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-ipaccesssettings-iprule.html
    Properties:
        - Name: IpRange
        - Name: Description
    
    """
    
    IpRange_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-ipaccesssettings-iprule.html#cfn-workspacesweb-ipaccesssettings-iprule-iprange""", alias="IpRange")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-ipaccesssettings-iprule.html#cfn-workspacesweb-ipaccesssettings-iprule-description""", alias="Description")
    


    @property
    def tropo_type(self) -> troposphere.workspacesweb.IpRule:
        from troposphere.workspacesweb import IpRule as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CookieSpecification(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiespecification.html
    Properties:
        - Name: Path
        - Name: Domain
        - Name: Name
    
    """
    
    Path_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiespecification.html#cfn-workspacesweb-usersettings-cookiespecification-path""", alias="Path")
    Domain_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiespecification.html#cfn-workspacesweb-usersettings-cookiespecification-domain""", alias="Domain")
    Name_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiespecification.html#cfn-workspacesweb-usersettings-cookiespecification-name""", alias="Name")
    


    @property
    def tropo_type(self) -> troposphere.workspacesweb.CookieSpecification:
        from troposphere.workspacesweb import CookieSpecification as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CookieSynchronizationConfiguration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiesynchronizationconfiguration.html
    Properties:
        - Name: Blocklist
        - Name: Allowlist
    
    """
    
    Blocklist_: Optional[List['CookieSpecification']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiesynchronizationconfiguration.html#cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration-blocklist""", alias="Blocklist")
    Allowlist_: List['CookieSpecification'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiesynchronizationconfiguration.html#cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration-allowlist""", alias="Allowlist")
    


    @property
    def tropo_type(self) -> troposphere.workspacesweb.CookieSynchronizationConfiguration:
        from troposphere.workspacesweb import CookieSynchronizationConfiguration as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class BrowserSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-browsersettings.html
    Properties:
        - Name: BrowserPolicy
        - Name: CustomerManagedKey
        - Name: AdditionalEncryptionContext
        - Name: Tags
    Attributes:
        - Name: AssociatedPortalArns
        - Name: BrowserSettingsArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    BrowserPolicy_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-browsersettings.html#cfn-workspacesweb-browsersettings-browserpolicy""", alias="BrowserPolicy")
    CustomerManagedKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-browsersettings.html#cfn-workspacesweb-browsersettings-customermanagedkey""", alias="CustomerManagedKey")
    AdditionalEncryptionContext_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-browsersettings.html#cfn-workspacesweb-browsersettings-additionalencryptioncontext""", alias="AdditionalEncryptionContext")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-browsersettings.html#cfn-workspacesweb-browsersettings-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.workspacesweb.BrowserSettings:
        from troposphere.workspacesweb import BrowserSettings as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.workspacesweb import BrowserSettings as TropoT
        return resource_to_troposphere(self, TropoT)


class IdentityProvider(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-identityprovider.html
    Properties:
        - Name: IdentityProviderDetails
        - Name: PortalArn
        - Name: IdentityProviderName
        - Name: IdentityProviderType
    Attributes:
        - Name: IdentityProviderArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IdentityProviderDetails_: Dict[str, str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-identityprovider.html#cfn-workspacesweb-identityprovider-identityproviderdetails""", alias="IdentityProviderDetails")
    PortalArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-identityprovider.html#cfn-workspacesweb-identityprovider-portalarn""", alias="PortalArn")
    IdentityProviderName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-identityprovider.html#cfn-workspacesweb-identityprovider-identityprovidername""", alias="IdentityProviderName")
    IdentityProviderType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-identityprovider.html#cfn-workspacesweb-identityprovider-identityprovidertype""", alias="IdentityProviderType")
    

    @property
    def tropo_type(self) -> troposphere.workspacesweb.IdentityProvider:
        from troposphere.workspacesweb import IdentityProvider as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.workspacesweb import IdentityProvider as TropoT
        return resource_to_troposphere(self, TropoT)


class IpAccessSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html
    Properties:
        - Name: IpRules
        - Name: Description
        - Name: CustomerManagedKey
        - Name: AdditionalEncryptionContext
        - Name: DisplayName
        - Name: Tags
    Attributes:
        - Name: CreationDate
        - Name: AssociatedPortalArns
        - Name: IpAccessSettingsArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IpRules_: List['IpRule'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html#cfn-workspacesweb-ipaccesssettings-iprules""", alias="IpRules")
    Description_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html#cfn-workspacesweb-ipaccesssettings-description""", alias="Description")
    CustomerManagedKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html#cfn-workspacesweb-ipaccesssettings-customermanagedkey""", alias="CustomerManagedKey")
    AdditionalEncryptionContext_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html#cfn-workspacesweb-ipaccesssettings-additionalencryptioncontext""", alias="AdditionalEncryptionContext")
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html#cfn-workspacesweb-ipaccesssettings-displayname""", alias="DisplayName")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html#cfn-workspacesweb-ipaccesssettings-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.workspacesweb.IpAccessSettings:
        from troposphere.workspacesweb import IpAccessSettings as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.workspacesweb import IpAccessSettings as TropoT
        return resource_to_troposphere(self, TropoT)


class NetworkSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-networksettings.html
    Properties:
        - Name: VpcId
        - Name: SecurityGroupIds
        - Name: SubnetIds
        - Name: Tags
    Attributes:
        - Name: AssociatedPortalArns
        - Name: NetworkSettingsArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    VpcId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-networksettings.html#cfn-workspacesweb-networksettings-vpcid""", alias="VpcId")
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-networksettings.html#cfn-workspacesweb-networksettings-securitygroupids""", alias="SecurityGroupIds")
    SubnetIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-networksettings.html#cfn-workspacesweb-networksettings-subnetids""", alias="SubnetIds")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-networksettings.html#cfn-workspacesweb-networksettings-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.workspacesweb.NetworkSettings:
        from troposphere.workspacesweb import NetworkSettings as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.workspacesweb import NetworkSettings as TropoT
        return resource_to_troposphere(self, TropoT)


class Portal(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html
    Properties:
        - Name: TrustStoreArn
        - Name: UserAccessLoggingSettingsArn
        - Name: CustomerManagedKey
        - Name: AdditionalEncryptionContext
        - Name: DisplayName
        - Name: UserSettingsArn
        - Name: BrowserSettingsArn
        - Name: IpAccessSettingsArn
        - Name: NetworkSettingsArn
        - Name: Tags
        - Name: AuthenticationType
    Attributes:
        - Name: CreationDate
        - Name: BrowserType
        - Name: ServiceProviderSamlMetadata
        - Name: StatusReason
        - Name: PortalArn
        - Name: PortalStatus
        - Name: RendererType
        - Name: PortalEndpoint
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    TrustStoreArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-truststorearn""", alias="TrustStoreArn")
    UserAccessLoggingSettingsArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-useraccessloggingsettingsarn""", alias="UserAccessLoggingSettingsArn")
    CustomerManagedKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-customermanagedkey""", alias="CustomerManagedKey")
    AdditionalEncryptionContext_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-additionalencryptioncontext""", alias="AdditionalEncryptionContext")
    DisplayName_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-displayname""", alias="DisplayName")
    UserSettingsArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-usersettingsarn""", alias="UserSettingsArn")
    BrowserSettingsArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-browsersettingsarn""", alias="BrowserSettingsArn")
    IpAccessSettingsArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-ipaccesssettingsarn""", alias="IpAccessSettingsArn")
    NetworkSettingsArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-networksettingsarn""", alias="NetworkSettingsArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-tags""", alias="Tags")
    AuthenticationType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-authenticationtype""", alias="AuthenticationType")
    

    @property
    def tropo_type(self) -> troposphere.workspacesweb.Portal:
        from troposphere.workspacesweb import Portal as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.workspacesweb import Portal as TropoT
        return resource_to_troposphere(self, TropoT)


class TrustStore(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-truststore.html
    Properties:
        - Name: CertificateList
        - Name: Tags
    Attributes:
        - Name: AssociatedPortalArns
        - Name: TrustStoreArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CertificateList_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-truststore.html#cfn-workspacesweb-truststore-certificatelist""", alias="CertificateList")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-truststore.html#cfn-workspacesweb-truststore-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.workspacesweb.TrustStore:
        from troposphere.workspacesweb import TrustStore as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.workspacesweb import TrustStore as TropoT
        return resource_to_troposphere(self, TropoT)


class UserAccessLoggingSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-useraccessloggingsettings.html
    Properties:
        - Name: KinesisStreamArn
        - Name: Tags
    Attributes:
        - Name: AssociatedPortalArns
        - Name: UserAccessLoggingSettingsArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    KinesisStreamArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-useraccessloggingsettings.html#cfn-workspacesweb-useraccessloggingsettings-kinesisstreamarn""", alias="KinesisStreamArn")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-useraccessloggingsettings.html#cfn-workspacesweb-useraccessloggingsettings-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.workspacesweb.UserAccessLoggingSettings:
        from troposphere.workspacesweb import UserAccessLoggingSettings as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.workspacesweb import UserAccessLoggingSettings as TropoT
        return resource_to_troposphere(self, TropoT)


class UserSettings(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html
    Properties:
        - Name: IdleDisconnectTimeoutInMinutes
        - Name: UploadAllowed
        - Name: CustomerManagedKey
        - Name: AdditionalEncryptionContext
        - Name: DisconnectTimeoutInMinutes
        - Name: PrintAllowed
        - Name: CopyAllowed
        - Name: CookieSynchronizationConfiguration
        - Name: DownloadAllowed
        - Name: PasteAllowed
        - Name: Tags
    Attributes:
        - Name: AssociatedPortalArns
        - Name: UserSettingsArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    IdleDisconnectTimeoutInMinutes_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-idledisconnecttimeoutinminutes""", alias="IdleDisconnectTimeoutInMinutes")
    UploadAllowed_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-uploadallowed""", alias="UploadAllowed")
    CustomerManagedKey_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-customermanagedkey""", alias="CustomerManagedKey")
    AdditionalEncryptionContext_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-additionalencryptioncontext""", alias="AdditionalEncryptionContext")
    DisconnectTimeoutInMinutes_: Optional[float] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-disconnecttimeoutinminutes""", alias="DisconnectTimeoutInMinutes")
    PrintAllowed_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-printallowed""", alias="PrintAllowed")
    CopyAllowed_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-copyallowed""", alias="CopyAllowed")
    CookieSynchronizationConfiguration_: Optional['CookieSynchronizationConfiguration'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration""", alias="CookieSynchronizationConfiguration")
    DownloadAllowed_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-downloadallowed""", alias="DownloadAllowed")
    PasteAllowed_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-pasteallowed""", alias="PasteAllowed")
    Tags_: Optional[List['Tag']] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.workspacesweb.UserSettings:
        from troposphere.workspacesweb import UserSettings as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.workspacesweb import UserSettings as TropoT
        return resource_to_troposphere(self, TropoT)

