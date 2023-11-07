from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Any, Union

from pydantic import BaseModel, Field

import troposphere
from tropoloco.tag import Tag, Tags
from tropoloco import resource_to_troposphere, property_to_troposphere


######################################################################
# AWS Property
######################################################################



class VpcInformation(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-connector-vpcinformation.html
    Properties:
        - Name: SecurityGroupIds
    
    """
    
    SecurityGroupIds_: List[str] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-connector-vpcinformation.html#cfn-pcaconnectorad-connector-vpcinformation-securitygroupids""", alias="SecurityGroupIds")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.VpcInformation:
        from troposphere.pcaconnectorad import VpcInformation as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ApplicationPolicies(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicies.html
    Properties:
        - Name: Policies
        - Name: Critical
    
    """
    
    Policies_: List['ApplicationPolicy'] =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicies.html#cfn-pcaconnectorad-template-applicationpolicies-policies""", alias="Policies")
    Critical_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicies.html#cfn-pcaconnectorad-template-applicationpolicies-critical""", alias="Critical")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.ApplicationPolicies:
        from troposphere.pcaconnectorad import ApplicationPolicies as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ApplicationPolicy(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicy.html
    Properties:
        - Name: PolicyType
        - Name: PolicyObjectIdentifier
    
    """
    
    PolicyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicy.html#cfn-pcaconnectorad-template-applicationpolicy-policytype""", alias="PolicyType")
    PolicyObjectIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicy.html#cfn-pcaconnectorad-template-applicationpolicy-policyobjectidentifier""", alias="PolicyObjectIdentifier")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.ApplicationPolicy:
        from troposphere.pcaconnectorad import ApplicationPolicy as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class CertificateValidity(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-certificatevalidity.html
    Properties:
        - Name: ValidityPeriod
        - Name: RenewalPeriod
    
    """
    
    ValidityPeriod_: 'ValidityPeriod' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-certificatevalidity.html#cfn-pcaconnectorad-template-certificatevalidity-validityperiod""", alias="ValidityPeriod")
    RenewalPeriod_: 'ValidityPeriod' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-certificatevalidity.html#cfn-pcaconnectorad-template-certificatevalidity-renewalperiod""", alias="RenewalPeriod")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.CertificateValidity:
        from troposphere.pcaconnectorad import CertificateValidity as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnrollmentFlagsV2(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv2.html
    Properties:
        - Name: NoSecurityExtension
        - Name: IncludeSymmetricAlgorithms
        - Name: UserInteractionRequired
        - Name: EnableKeyReuseOnNtTokenKeysetStorageFull
        - Name: RemoveInvalidCertificateFromPersonalStore
    
    """
    
    NoSecurityExtension_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv2.html#cfn-pcaconnectorad-template-enrollmentflagsv2-nosecurityextension""", alias="NoSecurityExtension")
    IncludeSymmetricAlgorithms_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv2.html#cfn-pcaconnectorad-template-enrollmentflagsv2-includesymmetricalgorithms""", alias="IncludeSymmetricAlgorithms")
    UserInteractionRequired_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv2.html#cfn-pcaconnectorad-template-enrollmentflagsv2-userinteractionrequired""", alias="UserInteractionRequired")
    EnableKeyReuseOnNtTokenKeysetStorageFull_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv2.html#cfn-pcaconnectorad-template-enrollmentflagsv2-enablekeyreuseonnttokenkeysetstoragefull""", alias="EnableKeyReuseOnNtTokenKeysetStorageFull")
    RemoveInvalidCertificateFromPersonalStore_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv2.html#cfn-pcaconnectorad-template-enrollmentflagsv2-removeinvalidcertificatefrompersonalstore""", alias="RemoveInvalidCertificateFromPersonalStore")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.EnrollmentFlagsV2:
        from troposphere.pcaconnectorad import EnrollmentFlagsV2 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnrollmentFlagsV3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv3.html
    Properties:
        - Name: NoSecurityExtension
        - Name: IncludeSymmetricAlgorithms
        - Name: UserInteractionRequired
        - Name: EnableKeyReuseOnNtTokenKeysetStorageFull
        - Name: RemoveInvalidCertificateFromPersonalStore
    
    """
    
    NoSecurityExtension_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv3.html#cfn-pcaconnectorad-template-enrollmentflagsv3-nosecurityextension""", alias="NoSecurityExtension")
    IncludeSymmetricAlgorithms_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv3.html#cfn-pcaconnectorad-template-enrollmentflagsv3-includesymmetricalgorithms""", alias="IncludeSymmetricAlgorithms")
    UserInteractionRequired_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv3.html#cfn-pcaconnectorad-template-enrollmentflagsv3-userinteractionrequired""", alias="UserInteractionRequired")
    EnableKeyReuseOnNtTokenKeysetStorageFull_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv3.html#cfn-pcaconnectorad-template-enrollmentflagsv3-enablekeyreuseonnttokenkeysetstoragefull""", alias="EnableKeyReuseOnNtTokenKeysetStorageFull")
    RemoveInvalidCertificateFromPersonalStore_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv3.html#cfn-pcaconnectorad-template-enrollmentflagsv3-removeinvalidcertificatefrompersonalstore""", alias="RemoveInvalidCertificateFromPersonalStore")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.EnrollmentFlagsV3:
        from troposphere.pcaconnectorad import EnrollmentFlagsV3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class EnrollmentFlagsV4(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv4.html
    Properties:
        - Name: NoSecurityExtension
        - Name: IncludeSymmetricAlgorithms
        - Name: UserInteractionRequired
        - Name: EnableKeyReuseOnNtTokenKeysetStorageFull
        - Name: RemoveInvalidCertificateFromPersonalStore
    
    """
    
    NoSecurityExtension_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv4.html#cfn-pcaconnectorad-template-enrollmentflagsv4-nosecurityextension""", alias="NoSecurityExtension")
    IncludeSymmetricAlgorithms_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv4.html#cfn-pcaconnectorad-template-enrollmentflagsv4-includesymmetricalgorithms""", alias="IncludeSymmetricAlgorithms")
    UserInteractionRequired_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv4.html#cfn-pcaconnectorad-template-enrollmentflagsv4-userinteractionrequired""", alias="UserInteractionRequired")
    EnableKeyReuseOnNtTokenKeysetStorageFull_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv4.html#cfn-pcaconnectorad-template-enrollmentflagsv4-enablekeyreuseonnttokenkeysetstoragefull""", alias="EnableKeyReuseOnNtTokenKeysetStorageFull")
    RemoveInvalidCertificateFromPersonalStore_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv4.html#cfn-pcaconnectorad-template-enrollmentflagsv4-removeinvalidcertificatefrompersonalstore""", alias="RemoveInvalidCertificateFromPersonalStore")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.EnrollmentFlagsV4:
        from troposphere.pcaconnectorad import EnrollmentFlagsV4 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExtensionsV2(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv2.html
    Properties:
        - Name: ApplicationPolicies
        - Name: KeyUsage
    
    """
    
    ApplicationPolicies_: Optional['ApplicationPolicies'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv2.html#cfn-pcaconnectorad-template-extensionsv2-applicationpolicies""", alias="ApplicationPolicies")
    KeyUsage_: 'KeyUsage' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv2.html#cfn-pcaconnectorad-template-extensionsv2-keyusage""", alias="KeyUsage")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.ExtensionsV2:
        from troposphere.pcaconnectorad import ExtensionsV2 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExtensionsV3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv3.html
    Properties:
        - Name: ApplicationPolicies
        - Name: KeyUsage
    
    """
    
    ApplicationPolicies_: Optional['ApplicationPolicies'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv3.html#cfn-pcaconnectorad-template-extensionsv3-applicationpolicies""", alias="ApplicationPolicies")
    KeyUsage_: 'KeyUsage' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv3.html#cfn-pcaconnectorad-template-extensionsv3-keyusage""", alias="KeyUsage")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.ExtensionsV3:
        from troposphere.pcaconnectorad import ExtensionsV3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ExtensionsV4(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv4.html
    Properties:
        - Name: ApplicationPolicies
        - Name: KeyUsage
    
    """
    
    ApplicationPolicies_: Optional['ApplicationPolicies'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv4.html#cfn-pcaconnectorad-template-extensionsv4-applicationpolicies""", alias="ApplicationPolicies")
    KeyUsage_: 'KeyUsage' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv4.html#cfn-pcaconnectorad-template-extensionsv4-keyusage""", alias="KeyUsage")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.ExtensionsV4:
        from troposphere.pcaconnectorad import ExtensionsV4 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GeneralFlagsV2(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv2.html
    Properties:
        - Name: AutoEnrollment
        - Name: MachineType
    
    """
    
    AutoEnrollment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv2.html#cfn-pcaconnectorad-template-generalflagsv2-autoenrollment""", alias="AutoEnrollment")
    MachineType_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv2.html#cfn-pcaconnectorad-template-generalflagsv2-machinetype""", alias="MachineType")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.GeneralFlagsV2:
        from troposphere.pcaconnectorad import GeneralFlagsV2 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GeneralFlagsV3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv3.html
    Properties:
        - Name: AutoEnrollment
        - Name: MachineType
    
    """
    
    AutoEnrollment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv3.html#cfn-pcaconnectorad-template-generalflagsv3-autoenrollment""", alias="AutoEnrollment")
    MachineType_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv3.html#cfn-pcaconnectorad-template-generalflagsv3-machinetype""", alias="MachineType")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.GeneralFlagsV3:
        from troposphere.pcaconnectorad import GeneralFlagsV3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class GeneralFlagsV4(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv4.html
    Properties:
        - Name: AutoEnrollment
        - Name: MachineType
    
    """
    
    AutoEnrollment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv4.html#cfn-pcaconnectorad-template-generalflagsv4-autoenrollment""", alias="AutoEnrollment")
    MachineType_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv4.html#cfn-pcaconnectorad-template-generalflagsv4-machinetype""", alias="MachineType")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.GeneralFlagsV4:
        from troposphere.pcaconnectorad import GeneralFlagsV4 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeyUsage(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusage.html
    Properties:
        - Name: Critical
        - Name: UsageFlags
    
    """
    
    Critical_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusage.html#cfn-pcaconnectorad-template-keyusage-critical""", alias="Critical")
    UsageFlags_: 'KeyUsageFlags' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusage.html#cfn-pcaconnectorad-template-keyusage-usageflags""", alias="UsageFlags")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.KeyUsage:
        from troposphere.pcaconnectorad import KeyUsage as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeyUsageFlags(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageflags.html
    Properties:
        - Name: KeyEncipherment
        - Name: DataEncipherment
        - Name: DigitalSignature
        - Name: KeyAgreement
        - Name: NonRepudiation
    
    """
    
    KeyEncipherment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageflags.html#cfn-pcaconnectorad-template-keyusageflags-keyencipherment""", alias="KeyEncipherment")
    DataEncipherment_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageflags.html#cfn-pcaconnectorad-template-keyusageflags-dataencipherment""", alias="DataEncipherment")
    DigitalSignature_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageflags.html#cfn-pcaconnectorad-template-keyusageflags-digitalsignature""", alias="DigitalSignature")
    KeyAgreement_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageflags.html#cfn-pcaconnectorad-template-keyusageflags-keyagreement""", alias="KeyAgreement")
    NonRepudiation_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageflags.html#cfn-pcaconnectorad-template-keyusageflags-nonrepudiation""", alias="NonRepudiation")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.KeyUsageFlags:
        from troposphere.pcaconnectorad import KeyUsageFlags as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeyUsageProperty(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageproperty.html
    Properties:
        - Name: PropertyFlags
        - Name: PropertyType
    
    """
    
    PropertyFlags_: Optional['KeyUsagePropertyFlags'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageproperty.html#cfn-pcaconnectorad-template-keyusageproperty-propertyflags""", alias="PropertyFlags")
    PropertyType_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageproperty.html#cfn-pcaconnectorad-template-keyusageproperty-propertytype""", alias="PropertyType")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.KeyUsageProperty:
        from troposphere.pcaconnectorad import KeyUsageProperty as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class KeyUsagePropertyFlags(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusagepropertyflags.html
    Properties:
        - Name: Decrypt
        - Name: Sign
        - Name: KeyAgreement
    
    """
    
    Decrypt_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusagepropertyflags.html#cfn-pcaconnectorad-template-keyusagepropertyflags-decrypt""", alias="Decrypt")
    Sign_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusagepropertyflags.html#cfn-pcaconnectorad-template-keyusagepropertyflags-sign""", alias="Sign")
    KeyAgreement_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusagepropertyflags.html#cfn-pcaconnectorad-template-keyusagepropertyflags-keyagreement""", alias="KeyAgreement")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.KeyUsagePropertyFlags:
        from troposphere.pcaconnectorad import KeyUsagePropertyFlags as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateKeyAttributesV2(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv2.html
    Properties:
        - Name: MinimalKeyLength
        - Name: KeySpec
        - Name: CryptoProviders
    
    """
    
    MinimalKeyLength_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv2.html#cfn-pcaconnectorad-template-privatekeyattributesv2-minimalkeylength""", alias="MinimalKeyLength")
    KeySpec_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv2.html#cfn-pcaconnectorad-template-privatekeyattributesv2-keyspec""", alias="KeySpec")
    CryptoProviders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv2.html#cfn-pcaconnectorad-template-privatekeyattributesv2-cryptoproviders""", alias="CryptoProviders")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.PrivateKeyAttributesV2:
        from troposphere.pcaconnectorad import PrivateKeyAttributesV2 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateKeyAttributesV3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv3.html
    Properties:
        - Name: MinimalKeyLength
        - Name: KeySpec
        - Name: KeyUsageProperty
        - Name: Algorithm
        - Name: CryptoProviders
    
    """
    
    MinimalKeyLength_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv3.html#cfn-pcaconnectorad-template-privatekeyattributesv3-minimalkeylength""", alias="MinimalKeyLength")
    KeySpec_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv3.html#cfn-pcaconnectorad-template-privatekeyattributesv3-keyspec""", alias="KeySpec")
    KeyUsageProperty_: 'KeyUsageProperty' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv3.html#cfn-pcaconnectorad-template-privatekeyattributesv3-keyusageproperty""", alias="KeyUsageProperty")
    Algorithm_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv3.html#cfn-pcaconnectorad-template-privatekeyattributesv3-algorithm""", alias="Algorithm")
    CryptoProviders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv3.html#cfn-pcaconnectorad-template-privatekeyattributesv3-cryptoproviders""", alias="CryptoProviders")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.PrivateKeyAttributesV3:
        from troposphere.pcaconnectorad import PrivateKeyAttributesV3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateKeyAttributesV4(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv4.html
    Properties:
        - Name: MinimalKeyLength
        - Name: KeySpec
        - Name: KeyUsageProperty
        - Name: Algorithm
        - Name: CryptoProviders
    
    """
    
    MinimalKeyLength_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv4.html#cfn-pcaconnectorad-template-privatekeyattributesv4-minimalkeylength""", alias="MinimalKeyLength")
    KeySpec_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv4.html#cfn-pcaconnectorad-template-privatekeyattributesv4-keyspec""", alias="KeySpec")
    KeyUsageProperty_: Optional['KeyUsageProperty'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv4.html#cfn-pcaconnectorad-template-privatekeyattributesv4-keyusageproperty""", alias="KeyUsageProperty")
    Algorithm_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv4.html#cfn-pcaconnectorad-template-privatekeyattributesv4-algorithm""", alias="Algorithm")
    CryptoProviders_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv4.html#cfn-pcaconnectorad-template-privatekeyattributesv4-cryptoproviders""", alias="CryptoProviders")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.PrivateKeyAttributesV4:
        from troposphere.pcaconnectorad import PrivateKeyAttributesV4 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateKeyFlagsV2(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv2.html
    Properties:
        - Name: ExportableKey
        - Name: StrongKeyProtectionRequired
        - Name: ClientVersion
    
    """
    
    ExportableKey_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv2.html#cfn-pcaconnectorad-template-privatekeyflagsv2-exportablekey""", alias="ExportableKey")
    StrongKeyProtectionRequired_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv2.html#cfn-pcaconnectorad-template-privatekeyflagsv2-strongkeyprotectionrequired""", alias="StrongKeyProtectionRequired")
    ClientVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv2.html#cfn-pcaconnectorad-template-privatekeyflagsv2-clientversion""", alias="ClientVersion")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.PrivateKeyFlagsV2:
        from troposphere.pcaconnectorad import PrivateKeyFlagsV2 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateKeyFlagsV3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv3.html
    Properties:
        - Name: RequireAlternateSignatureAlgorithm
        - Name: ExportableKey
        - Name: StrongKeyProtectionRequired
        - Name: ClientVersion
    
    """
    
    RequireAlternateSignatureAlgorithm_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv3.html#cfn-pcaconnectorad-template-privatekeyflagsv3-requirealternatesignaturealgorithm""", alias="RequireAlternateSignatureAlgorithm")
    ExportableKey_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv3.html#cfn-pcaconnectorad-template-privatekeyflagsv3-exportablekey""", alias="ExportableKey")
    StrongKeyProtectionRequired_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv3.html#cfn-pcaconnectorad-template-privatekeyflagsv3-strongkeyprotectionrequired""", alias="StrongKeyProtectionRequired")
    ClientVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv3.html#cfn-pcaconnectorad-template-privatekeyflagsv3-clientversion""", alias="ClientVersion")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.PrivateKeyFlagsV3:
        from troposphere.pcaconnectorad import PrivateKeyFlagsV3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class PrivateKeyFlagsV4(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html
    Properties:
        - Name: RequireAlternateSignatureAlgorithm
        - Name: ExportableKey
        - Name: UseLegacyProvider
        - Name: StrongKeyProtectionRequired
        - Name: RequireSameKeyRenewal
        - Name: ClientVersion
    
    """
    
    RequireAlternateSignatureAlgorithm_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html#cfn-pcaconnectorad-template-privatekeyflagsv4-requirealternatesignaturealgorithm""", alias="RequireAlternateSignatureAlgorithm")
    ExportableKey_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html#cfn-pcaconnectorad-template-privatekeyflagsv4-exportablekey""", alias="ExportableKey")
    UseLegacyProvider_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html#cfn-pcaconnectorad-template-privatekeyflagsv4-uselegacyprovider""", alias="UseLegacyProvider")
    StrongKeyProtectionRequired_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html#cfn-pcaconnectorad-template-privatekeyflagsv4-strongkeyprotectionrequired""", alias="StrongKeyProtectionRequired")
    RequireSameKeyRenewal_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html#cfn-pcaconnectorad-template-privatekeyflagsv4-requiresamekeyrenewal""", alias="RequireSameKeyRenewal")
    ClientVersion_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html#cfn-pcaconnectorad-template-privatekeyflagsv4-clientversion""", alias="ClientVersion")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.PrivateKeyFlagsV4:
        from troposphere.pcaconnectorad import PrivateKeyFlagsV4 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SubjectNameFlagsV2(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html
    Properties:
        - Name: SanRequireEmail
        - Name: SanRequireDns
        - Name: RequireCommonName
        - Name: SanRequireUpn
        - Name: SanRequireDomainDns
        - Name: SanRequireSpn
        - Name: RequireEmail
        - Name: RequireDirectoryPath
        - Name: SanRequireDirectoryGuid
        - Name: RequireDnsAsCn
    
    """
    
    SanRequireEmail_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-sanrequireemail""", alias="SanRequireEmail")
    SanRequireDns_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-sanrequiredns""", alias="SanRequireDns")
    RequireCommonName_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-requirecommonname""", alias="RequireCommonName")
    SanRequireUpn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-sanrequireupn""", alias="SanRequireUpn")
    SanRequireDomainDns_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-sanrequiredomaindns""", alias="SanRequireDomainDns")
    SanRequireSpn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-sanrequirespn""", alias="SanRequireSpn")
    RequireEmail_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-requireemail""", alias="RequireEmail")
    RequireDirectoryPath_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-requiredirectorypath""", alias="RequireDirectoryPath")
    SanRequireDirectoryGuid_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-sanrequiredirectoryguid""", alias="SanRequireDirectoryGuid")
    RequireDnsAsCn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-requirednsascn""", alias="RequireDnsAsCn")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.SubjectNameFlagsV2:
        from troposphere.pcaconnectorad import SubjectNameFlagsV2 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SubjectNameFlagsV3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html
    Properties:
        - Name: SanRequireEmail
        - Name: SanRequireDns
        - Name: RequireCommonName
        - Name: SanRequireUpn
        - Name: SanRequireDomainDns
        - Name: SanRequireSpn
        - Name: RequireEmail
        - Name: RequireDirectoryPath
        - Name: SanRequireDirectoryGuid
        - Name: RequireDnsAsCn
    
    """
    
    SanRequireEmail_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-sanrequireemail""", alias="SanRequireEmail")
    SanRequireDns_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-sanrequiredns""", alias="SanRequireDns")
    RequireCommonName_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-requirecommonname""", alias="RequireCommonName")
    SanRequireUpn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-sanrequireupn""", alias="SanRequireUpn")
    SanRequireDomainDns_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-sanrequiredomaindns""", alias="SanRequireDomainDns")
    SanRequireSpn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-sanrequirespn""", alias="SanRequireSpn")
    RequireEmail_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-requireemail""", alias="RequireEmail")
    RequireDirectoryPath_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-requiredirectorypath""", alias="RequireDirectoryPath")
    SanRequireDirectoryGuid_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-sanrequiredirectoryguid""", alias="SanRequireDirectoryGuid")
    RequireDnsAsCn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-requirednsascn""", alias="RequireDnsAsCn")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.SubjectNameFlagsV3:
        from troposphere.pcaconnectorad import SubjectNameFlagsV3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class SubjectNameFlagsV4(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html
    Properties:
        - Name: SanRequireEmail
        - Name: SanRequireDns
        - Name: RequireCommonName
        - Name: SanRequireUpn
        - Name: SanRequireDomainDns
        - Name: SanRequireSpn
        - Name: RequireEmail
        - Name: RequireDirectoryPath
        - Name: SanRequireDirectoryGuid
        - Name: RequireDnsAsCn
    
    """
    
    SanRequireEmail_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-sanrequireemail""", alias="SanRequireEmail")
    SanRequireDns_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-sanrequiredns""", alias="SanRequireDns")
    RequireCommonName_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-requirecommonname""", alias="RequireCommonName")
    SanRequireUpn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-sanrequireupn""", alias="SanRequireUpn")
    SanRequireDomainDns_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-sanrequiredomaindns""", alias="SanRequireDomainDns")
    SanRequireSpn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-sanrequirespn""", alias="SanRequireSpn")
    RequireEmail_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-requireemail""", alias="RequireEmail")
    RequireDirectoryPath_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-requiredirectorypath""", alias="RequireDirectoryPath")
    SanRequireDirectoryGuid_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-sanrequiredirectoryguid""", alias="SanRequireDirectoryGuid")
    RequireDnsAsCn_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-requirednsascn""", alias="RequireDnsAsCn")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.SubjectNameFlagsV4:
        from troposphere.pcaconnectorad import SubjectNameFlagsV4 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TemplateDefinition(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatedefinition.html
    Properties:
        - Name: TemplateV4
        - Name: TemplateV3
        - Name: TemplateV2
    
    """
    
    TemplateV4_: Optional['TemplateV4'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatedefinition.html#cfn-pcaconnectorad-template-templatedefinition-templatev4""", alias="TemplateV4")
    TemplateV3_: Optional['TemplateV3'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatedefinition.html#cfn-pcaconnectorad-template-templatedefinition-templatev3""", alias="TemplateV3")
    TemplateV2_: Optional['TemplateV2'] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatedefinition.html#cfn-pcaconnectorad-template-templatedefinition-templatev2""", alias="TemplateV2")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.TemplateDefinition:
        from troposphere.pcaconnectorad import TemplateDefinition as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TemplateV2(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html
    Properties:
        - Name: SubjectNameFlags
        - Name: SupersededTemplates
        - Name: PrivateKeyFlags
        - Name: PrivateKeyAttributes
        - Name: GeneralFlags
        - Name: CertificateValidity
        - Name: Extensions
        - Name: EnrollmentFlags
    
    """
    
    SubjectNameFlags_: 'SubjectNameFlagsV2' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-subjectnameflags""", alias="SubjectNameFlags")
    SupersededTemplates_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-supersededtemplates""", alias="SupersededTemplates")
    PrivateKeyFlags_: 'PrivateKeyFlagsV2' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-privatekeyflags""", alias="PrivateKeyFlags")
    PrivateKeyAttributes_: 'PrivateKeyAttributesV2' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-privatekeyattributes""", alias="PrivateKeyAttributes")
    GeneralFlags_: 'GeneralFlagsV2' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-generalflags""", alias="GeneralFlags")
    CertificateValidity_: 'CertificateValidity' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-certificatevalidity""", alias="CertificateValidity")
    Extensions_: 'ExtensionsV2' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-extensions""", alias="Extensions")
    EnrollmentFlags_: 'EnrollmentFlagsV2' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-enrollmentflags""", alias="EnrollmentFlags")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.TemplateV2:
        from troposphere.pcaconnectorad import TemplateV2 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TemplateV3(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html
    Properties:
        - Name: SubjectNameFlags
        - Name: SupersededTemplates
        - Name: PrivateKeyFlags
        - Name: PrivateKeyAttributes
        - Name: GeneralFlags
        - Name: CertificateValidity
        - Name: Extensions
        - Name: EnrollmentFlags
        - Name: HashAlgorithm
    
    """
    
    SubjectNameFlags_: 'SubjectNameFlagsV3' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-subjectnameflags""", alias="SubjectNameFlags")
    SupersededTemplates_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-supersededtemplates""", alias="SupersededTemplates")
    PrivateKeyFlags_: 'PrivateKeyFlagsV3' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-privatekeyflags""", alias="PrivateKeyFlags")
    PrivateKeyAttributes_: 'PrivateKeyAttributesV3' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-privatekeyattributes""", alias="PrivateKeyAttributes")
    GeneralFlags_: 'GeneralFlagsV3' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-generalflags""", alias="GeneralFlags")
    CertificateValidity_: 'CertificateValidity' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-certificatevalidity""", alias="CertificateValidity")
    Extensions_: 'ExtensionsV3' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-extensions""", alias="Extensions")
    EnrollmentFlags_: 'EnrollmentFlagsV3' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-enrollmentflags""", alias="EnrollmentFlags")
    HashAlgorithm_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-hashalgorithm""", alias="HashAlgorithm")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.TemplateV3:
        from troposphere.pcaconnectorad import TemplateV3 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class TemplateV4(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html
    Properties:
        - Name: SubjectNameFlags
        - Name: SupersededTemplates
        - Name: PrivateKeyFlags
        - Name: PrivateKeyAttributes
        - Name: GeneralFlags
        - Name: CertificateValidity
        - Name: Extensions
        - Name: EnrollmentFlags
        - Name: HashAlgorithm
    
    """
    
    SubjectNameFlags_: 'SubjectNameFlagsV4' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-subjectnameflags""", alias="SubjectNameFlags")
    SupersededTemplates_: Optional[List[str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-supersededtemplates""", alias="SupersededTemplates")
    PrivateKeyFlags_: 'PrivateKeyFlagsV4' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-privatekeyflags""", alias="PrivateKeyFlags")
    PrivateKeyAttributes_: 'PrivateKeyAttributesV4' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-privatekeyattributes""", alias="PrivateKeyAttributes")
    GeneralFlags_: 'GeneralFlagsV4' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-generalflags""", alias="GeneralFlags")
    CertificateValidity_: 'CertificateValidity' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-certificatevalidity""", alias="CertificateValidity")
    Extensions_: 'ExtensionsV4' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-extensions""", alias="Extensions")
    EnrollmentFlags_: 'EnrollmentFlagsV4' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-enrollmentflags""", alias="EnrollmentFlags")
    HashAlgorithm_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-hashalgorithm""", alias="HashAlgorithm")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.TemplateV4:
        from troposphere.pcaconnectorad import TemplateV4 as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class ValidityPeriod(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-validityperiod.html
    Properties:
        - Name: PeriodType
        - Name: Period
    
    """
    
    PeriodType_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-validityperiod.html#cfn-pcaconnectorad-template-validityperiod-periodtype""", alias="PeriodType")
    Period_: float =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-validityperiod.html#cfn-pcaconnectorad-template-validityperiod-period""", alias="Period")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.ValidityPeriod:
        from troposphere.pcaconnectorad import ValidityPeriod as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    

class AccessRights(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights.html
    Properties:
        - Name: Enroll
        - Name: AutoEnroll
    
    """
    
    Enroll_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights.html#cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights-enroll""", alias="Enroll")
    AutoEnroll_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights.html#cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights-autoenroll""", alias="AutoEnroll")
    


    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.AccessRights:
        from troposphere.pcaconnectorad import AccessRights as TropoT
        return TropoT

    def to_troposphere(self):
        property_to_troposphere(self)

    


######################################################################
# AWS Resource
######################################################################


class Connector(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-connector.html
    Properties:
        - Name: CertificateAuthorityArn
        - Name: DirectoryId
        - Name: VpcInformation
        - Name: Tags
    Attributes:
        - Name: ConnectorArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    CertificateAuthorityArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-connector.html#cfn-pcaconnectorad-connector-certificateauthorityarn""", alias="CertificateAuthorityArn")
    DirectoryId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-connector.html#cfn-pcaconnectorad-connector-directoryid""", alias="DirectoryId")
    VpcInformation_: 'VpcInformation' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-connector.html#cfn-pcaconnectorad-connector-vpcinformation""", alias="VpcInformation")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-connector.html#cfn-pcaconnectorad-connector-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.Connector:
        from troposphere.pcaconnectorad import Connector as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pcaconnectorad import Connector as TropoT
        return resource_to_troposphere(self, TropoT)


class DirectoryRegistration(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-directoryregistration.html
    Properties:
        - Name: DirectoryId
        - Name: Tags
    Attributes:
        - Name: DirectoryRegistrationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    DirectoryId_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-directoryregistration.html#cfn-pcaconnectorad-directoryregistration-directoryid""", alias="DirectoryId")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-directoryregistration.html#cfn-pcaconnectorad-directoryregistration-tags""", alias="Tags")
    

    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.DirectoryRegistration:
        from troposphere.pcaconnectorad import DirectoryRegistration as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pcaconnectorad import DirectoryRegistration as TropoT
        return resource_to_troposphere(self, TropoT)


class ServicePrincipalName(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-serviceprincipalname.html
    Properties:
        - Name: ConnectorArn
        - Name: DirectoryRegistrationArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConnectorArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-serviceprincipalname.html#cfn-pcaconnectorad-serviceprincipalname-connectorarn""", alias="ConnectorArn")
    DirectoryRegistrationArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-serviceprincipalname.html#cfn-pcaconnectorad-serviceprincipalname-directoryregistrationarn""", alias="DirectoryRegistrationArn")
    

    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.ServicePrincipalName:
        from troposphere.pcaconnectorad import ServicePrincipalName as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pcaconnectorad import ServicePrincipalName as TropoT
        return resource_to_troposphere(self, TropoT)


class Template(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html
    Properties:
        - Name: ConnectorArn
        - Name: Definition
        - Name: Tags
        - Name: Name
        - Name: ReenrollAllCertificateHolders
    Attributes:
        - Name: TemplateArn
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    ConnectorArn_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html#cfn-pcaconnectorad-template-connectorarn""", alias="ConnectorArn")
    Definition_: 'TemplateDefinition' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html#cfn-pcaconnectorad-template-definition""", alias="Definition")
    Tags_: Optional[Dict[str, str]] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html#cfn-pcaconnectorad-template-tags""", alias="Tags")
    Name_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html#cfn-pcaconnectorad-template-name""", alias="Name")
    ReenrollAllCertificateHolders_: Optional[bool] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html#cfn-pcaconnectorad-template-reenrollallcertificateholders""", alias="ReenrollAllCertificateHolders")
    

    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.Template:
        from troposphere.pcaconnectorad import Template as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pcaconnectorad import Template as TropoT
        return resource_to_troposphere(self, TropoT)


class TemplateGroupAccessControlEntry(BaseModel):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-templategroupaccesscontrolentry.html
    Properties:
        - Name: AccessRights
        - Name: TemplateArn
        - Name: GroupDisplayName
        - Name: GroupSecurityIdentifier
    """
    
    title: str = Field(description="Title of cloudformation resource.", alias="title")
    AccessRights_: 'AccessRights' =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-templategroupaccesscontrolentry.html#cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights""", alias="AccessRights")
    TemplateArn_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-templategroupaccesscontrolentry.html#cfn-pcaconnectorad-templategroupaccesscontrolentry-templatearn""", alias="TemplateArn")
    GroupDisplayName_: str =  Field(description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-templategroupaccesscontrolentry.html#cfn-pcaconnectorad-templategroupaccesscontrolentry-groupdisplayname""", alias="GroupDisplayName")
    GroupSecurityIdentifier_: Optional[str] = Field(None, description="""http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-templategroupaccesscontrolentry.html#cfn-pcaconnectorad-templategroupaccesscontrolentry-groupsecurityidentifier""", alias="GroupSecurityIdentifier")
    

    @property
    def tropo_type(self) -> troposphere.pcaconnectorad.TemplateGroupAccessControlEntry:
        from troposphere.pcaconnectorad import TemplateGroupAccessControlEntry as TropoT
        return TropoT

    def to_troposphere(self):
        from troposphere.pcaconnectorad import TemplateGroupAccessControlEntry as TropoT
        return resource_to_troposphere(self, TropoT)

